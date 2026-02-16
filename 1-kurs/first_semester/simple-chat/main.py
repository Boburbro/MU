from typing import List, Optional
from datetime import datetime
from fastapi import (
    FastAPI,
    WebSocket,
    WebSocketDisconnect,
    Depends,
    HTTPException,
    status,
    Form,
    Request,
    Header,
    Query,
)
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.security import OAuth2PasswordRequestForm

from sqlmodel import select
from sqlalchemy import or_, and_, func

from db import async_session, init_db, run_migrations

from auth import (
    create_access_token,
    get_password_hash,
    authenticate_user,
    decode_token,
    get_user_by_username,
)
from models import User, PrivateMessage

app = FastAPI(title="Simple Chat")
app.mount("/static", StaticFiles(directory="static"), name="static")


class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        try:
            self.active_connections.remove(websocket)
        except ValueError:
            pass

    async def broadcast(self, message: str):
        for connection in list(self.active_connections):
            try:
                await connection.send_text(message)
            except Exception:
                self.disconnect(connection)


manager = ConnectionManager()


@app.on_event("startup")
async def on_startup():
    await init_db()
    await run_migrations()


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    # If user has a valid access_token cookie, redirect to home
    token = request.cookies.get("access_token")
    if token:
        # support tokens with or without "Bearer " prefix
        if token.startswith("Bearer "):
            token = token.split(" ", 1)[1]
        try:
            payload = decode_token(token)
            username = payload.get("sub")
            if username:
                async with async_session() as session:
                    q = await session.execute(
                        select(User).where(User.username == username)
                    )
                    user = q.scalar_one_or_none()
                    if user:
                        return RedirectResponse(url="/home")
        except Exception:
            pass

    # Serve login page; client will handle redirect after auth
    with open("static/login.html", "r", encoding="utf-8") as f:
        return HTMLResponse(f.read())


@app.post("/register")
async def register(
    first_name: str = Form(...),
    last_name: str = Form(...),
    username: str = Form(...),
    password: str = Form(...),
):
    # normalize and validate username (store lowercase)
    username = username.strip().lower()
    if not username:
        raise HTTPException(status_code=400, detail="Username is required")
    if len(username) < 5 or len(username) > 32:
        raise HTTPException(
            status_code=400, detail="Username must be between 5 and 32 characters"
        )

    async with async_session() as session:
        q = await session.execute(select(User).where(User.username == username))
        exists = q.scalar_one_or_none()
        if exists:
            raise HTTPException(status_code=400, detail="Username already taken")

        user = User(
            username=username,
            hashed_password=get_password_hash(password),
            first_name=first_name,
            last_name=last_name,
        )
        session.add(user)
        await session.commit()
        await session.refresh(user)
        token = create_access_token({"sub": user.username})
        response = RedirectResponse(url="/home", status_code=303)
        # set raw token (no "Bearer " prefix) to match /token behavior
        response.set_cookie(key="access_token", value=token, httponly=True)
        return response


from fastapi.responses import JSONResponse


@app.post("/token")
async def login_for_access_token(
    request: Request, form_data: OAuth2PasswordRequestForm = Depends()
):
    async with async_session() as session:
        user = await authenticate_user(session, form_data.username, form_data.password)
        if not user:
            # for form submissions return a user-friendly page error
            raise HTTPException(
                status_code=400, detail="Incorrect username or password"
            )
        access_token = create_access_token({"sub": user.username})
        # set HttpOnly cookie so frontend JS cannot read it (mitigates XSS)
        # For local dev, secure=False. In production set secure=True and samesite='lax' or 'strict'
        if "text/html" in request.headers.get("accept", ""):
            resp = RedirectResponse(url="/home")
            resp.set_cookie(
                key="access_token", value=access_token, httponly=True, samesite="lax"
            )
            return resp
        else:
            resp = JSONResponse({"access_token": access_token, "token_type": "bearer"})
            resp.set_cookie(
                key="access_token", value=access_token, httponly=True, samesite="lax"
            )
            return resp


@app.get("/username-available")
async def username_available(username: str):
    username = username.strip().lower()
    if len(username) < 5 or len(username) > 32:
        return {"available": False}
    async with async_session() as session:
        q = await session.execute(select(User).where(User.username == username))
        exists = q.scalar_one_or_none()
        return {"available": exists is None}


async def get_current_user(
    request: Request, authorization: Optional[str] = Header(None, alias="Authorization")
):
    # Prefer cookie token (HttpOnly), fall back to Authorization header
    token_value = request.cookies.get("access_token")
    if not token_value and authorization:
        token_value = authorization
    if not token_value:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token"
        )
    if token_value.startswith("Bearer "):
        token_value = token_value.split(" ", 1)[1]
    payload = decode_token(token_value)
    username: str = payload.get("sub")
    if username is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token"
        )
    async with async_session() as session:
        q = await session.execute(select(User).where(User.username == username))
        user = q.scalar_one_or_none()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user


@app.get("/me")
async def read_me(current_user: User = Depends(get_current_user)):
    return {
        "id": current_user.id,
        "username": current_user.username,
        "first_name": current_user.first_name,
        "last_name": current_user.last_name,
        "bio": current_user.bio,
        "created_at": current_user.created_at,
    }


@app.get("/users")
async def list_users(current_user: User = Depends(get_current_user)):
    async with async_session() as session:
        q = await session.execute(select(User))
        users = q.scalars().all()
        result = []
        for user in users:
            if user.id == current_user.id:
                continue
            unread_q = await session.execute(
                select(func.count())
                .select_from(PrivateMessage)
                .where(
                    and_(
                        PrivateMessage.sender_id == user.id,
                        PrivateMessage.receiver_id == current_user.id,
                        PrivateMessage.read_at.is_(None),
                    )
                )
            )
            unread_count = unread_q.scalar() or 0
            result.append(
                {
                    "username": user.username,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "bio": user.bio,
                    "unread": unread_count,
                }
            )
        return result


@app.get("/home", response_class=HTMLResponse)
async def home(request: Request):
    # If not authenticated redirect to login
    cookie_token = request.cookies.get("access_token")
    if not cookie_token:
        return RedirectResponse(url="/")
    with open("static/home.html", "r", encoding="utf-8") as f:
        return HTMLResponse(f.read())


@app.get("/profile", response_class=HTMLResponse)
async def profile(request: Request):
    # Protect page; rely on cookie token
    cookie_token = request.cookies.get("access_token")
    if not cookie_token:
        return RedirectResponse(url="/")
    with open("static/profile.html", "r", encoding="utf-8") as f:
        return HTMLResponse(f.read())


@app.get("/user/{username}", response_class=HTMLResponse)
async def public_profile(username: str):
    with open("static/user.html", "r", encoding="utf-8") as f:
        return HTMLResponse(f.read())


@app.patch("/me")
async def update_me(
    first_name: Optional[str] = Form(None),
    last_name: Optional[str] = Form(None),
    bio: Optional[str] = Form(None),
    current_user: User = Depends(get_current_user),
):
    async with async_session() as session:
        q = await session.execute(select(User).where(User.id == current_user.id))
        user = q.scalar_one_or_none()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        if first_name is not None:
            user.first_name = first_name
        if last_name is not None:
            user.last_name = last_name
        if bio is not None:
            user.bio = bio
        session.add(user)
        await session.commit()
        await session.refresh(user)
        return {
            "username": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "bio": user.bio,
            "created_at": user.created_at,
        }


@app.get("/users/{username}")
async def get_user(username: str, current_user: User = Depends(get_current_user)):
    async with async_session() as session:
        q = await session.execute(select(User).where(User.username == username))
        user = q.scalar_one_or_none()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return {
            "username": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "bio": user.bio,
            "created_at": user.created_at,
        }


@app.get("/messages/{username}")
async def get_messages(
    username: str,
    limit: int = Query(100, ge=1, le=500),
    current_user: User = Depends(get_current_user),
):
    async with async_session() as session:
        other = await get_user_by_username(session, username)
        if not other:
            raise HTTPException(status_code=404, detail="User not found")
        q = await session.execute(
            select(PrivateMessage)
            .where(
                or_(
                    and_(
                        PrivateMessage.sender_id == current_user.id,
                        PrivateMessage.receiver_id == other.id,
                    ),
                    and_(
                        PrivateMessage.sender_id == other.id,
                        PrivateMessage.receiver_id == current_user.id,
                    ),
                )
            )
            .order_by(PrivateMessage.created_at.asc())
            .limit(limit)
        )
        messages = q.scalars().all()

        # Mark received messages as read
        updated = False
        now = datetime.utcnow()
        for m in messages:
            if m.receiver_id == current_user.id and m.read_at is None:
                m.read_at = now
                session.add(m)
                updated = True
        if updated:
            await session.commit()

        return [
            {
                "id": m.id,
                "sender_id": m.sender_id,
                "receiver_id": m.receiver_id,
                "content": m.content,
                "created_at": m.created_at,
                "read_at": m.read_at,
            }
            for m in messages
        ]


@app.post("/messages/{username}")
async def send_message(
    username: str,
    content: str = Form(...),
    current_user: User = Depends(get_current_user),
):
    content = (content or "").strip()
    if not content:
        raise HTTPException(status_code=400, detail="Message cannot be empty")
    if len(content) > 2000:
        raise HTTPException(status_code=400, detail="Message too long")
    async with async_session() as session:
        other = await get_user_by_username(session, username)
        if not other:
            raise HTTPException(status_code=404, detail="User not found")
        msg = PrivateMessage(
            sender_id=current_user.id, receiver_id=other.id, content=content
        )
        session.add(msg)
        await session.commit()
        await session.refresh(msg)
        return {
            "id": msg.id,
            "sender_id": msg.sender_id,
            "receiver_id": msg.receiver_id,
            "content": msg.content,
            "created_at": msg.created_at,
            "read_at": msg.read_at,
        }


from fastapi.responses import JSONResponse


@app.post("/logout")
async def logout():
    response = JSONResponse({"ok": True})
    response.delete_cookie("access_token")
    return response


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket, token: Optional[str] = None):
    # token expected as query param: /ws?token=... or from cookies (HttpOnly) sent automatically
    if not token:
        # try to read from query params
        token = websocket.query_params.get("token")
    if not token:
        # try cookies (cookie header)
        cookie_header = websocket.headers.get("cookie", "")
        # parse cookie header simple way
        for part in cookie_header.split(";"):
            if "=" in part:
                k, v = part.strip().split("=", 1)
                if k == "access_token":
                    token = v
                    break
    if not token:
        await websocket.close(code=1008)
        return
    try:
        payload = decode_token(token)
        username = payload.get("sub")
    except Exception:
        await websocket.close(code=1008)
        return

    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(f"{username}: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
