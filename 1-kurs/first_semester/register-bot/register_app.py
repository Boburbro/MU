import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
from dotenv import load_dotenv

# Google Sheets setup
SCOPE = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive",
]
CREDS_PATH = "bot/credentials.json"
load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))
SHEET_URL = os.getenv("GOOGLE_SHEET_URL")


def extract_sheet_id(sheet_url):
    try:
        return sheet_url.split("/d/")[1].split("/")[0]
    except Exception:
        return None


def write_user_to_sheet(user_dict):
    sheet_id = extract_sheet_id(SHEET_URL)
    if not sheet_id:
        return False, "Sheet ID not found"
    creds = ServiceAccountCredentials.from_json_keyfile_name(CREDS_PATH, SCOPE)
    client = gspread.authorize(creds)
    sheet = client.open_by_key(sheet_id).sheet1
    import uuid

    unique_key = user_dict.get("unique_key", str(uuid.uuid4()))
    sheet.append_row(
        [
            unique_key,
            user_dict.get("full_name", ""),
            unique_key,
            user_dict.get("surname", ""),
            user_dict.get("age", ""),
            user_dict.get("email", ""),
        ]
    )
    return True, None


def is_valid_name(name):
    return name.isalpha() and 2 <= len(name) <= 32


def is_valid_age(age):
    return age.isdigit() and 10 <= int(age) <= 100


def is_valid_email(email):
    import re

    return re.match(r"^[\w\.-]+@[\w\.-]+\.\w{2,}$", email)


class RegisterApp:
    def show_loader(self):
        self.loader_win = tk.Toplevel(self.root)
        self.loader_win.title("Saqlanmoqda...")
        self.loader_win.geometry("250x80")
        self.loader_win.transient(self.root)
        self.loader_win.grab_set()
        self.loader_win.resizable(False, False)
        tk.Label(
            self.loader_win, text="Ma'lumotlar saqlanmoqda...", font=("Arial", 12)
        ).pack(pady=10)
        pb = ttk.Progressbar(self.loader_win, mode="indeterminate")
        pb.pack(pady=5, padx=20, fill="x")
        pb.start(10)

    def __init__(self, root):
        self.root = root
        self.root.title("Splash Page")
        self.show_splash()

    def show_splash(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.root.configure(bg="#f5f6fa")
        splash = tk.Frame(self.root, bg="#f5f6fa")
        splash.pack(expand=True, fill="both")
        card = tk.Frame(splash, bg="white", bd=2, relief="groove")
        card.place(relx=0.5, rely=0.5, anchor="center", width=340, height=220)
        tk.Label(card, text="📝", font=("Arial", 32), bg="white").pack(pady=(18, 0))
        tk.Label(
            card,
            text="Welcome to Registration App!",
            font=("Arial", 18, "bold"),
            bg="white",
            fg="#2d3436",
        ).pack(pady=(8, 0))
        btn = tk.Button(
            card,
            text="Ro'yxatdan o'tish",
            font=("Arial", 14, "bold"),
            bg="#00b894",
            fg="white",
            activebackground="#00cec9",
            activeforeground="white",
            command=self.show_register_page,
            bd=0,
            relief="flat",
            cursor="hand2",
        )
        btn.pack(pady=24, ipadx=10, ipady=4)

    def show_register_page(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.root.configure(bg="#f5f6fa")
        reg = tk.Frame(self.root, bg="#f5f6fa")
        reg.pack(expand=True, fill="both")
        card = tk.Frame(reg, bg="white", bd=2, relief="groove")
        card.place(relx=0.5, rely=0.5, anchor="center", width=340, height=340)
        tk.Label(
            card,
            text="Ro'yxatdan o'tish",
            font=("Arial", 16, "bold"),
            bg="white",
            fg="#0984e3",
        ).pack(pady=(18, 8))
        self.fields = {}
        for label, key in [
            ("Ism", "full_name"),
            ("Familiya", "surname"),
            ("Yosh", "age"),
            ("Email", "email"),
        ]:
            frame = tk.Frame(card, bg="white")
            frame.pack(pady=5)
            tk.Label(
                frame, text=label, width=12, anchor="w", font=("Arial", 12), bg="white"
            ).pack(side="left")
            entry = tk.Entry(
                frame,
                width=22,
                font=("Arial", 12),
                bd=1,
                relief="solid",
                highlightthickness=1,
                highlightbackground="#dfe6e9",
            )
            entry.pack(side="left", padx=2)
            self.fields[key] = entry
        btn_frame = tk.Frame(card, bg="white")
        btn_frame.pack(pady=18)
        tk.Button(
            btn_frame,
            text="❌ Bekor qilish",
            command=self.show_splash,
            width=12,
            font=("Arial", 12, "bold"),
            bg="#dfe6e9",
            fg="#636e72",
            activebackground="#b2bec3",
            activeforeground="#636e72",
            bd=0,
            relief="flat",
            cursor="hand2",
        ).pack(side="left", padx=8)
        tk.Button(
            btn_frame,
            text="✅ Saqlash",
            command=self.save_user,
            width=12,
            font=("Arial", 12, "bold"),
            bg="#00b894",
            fg="white",
            activebackground="#00cec9",
            activeforeground="white",
            bd=0,
            relief="flat",
            cursor="hand2",
        ).pack(side="left", padx=8)

    def save_user(self):
        import uuid

        data = {k: v.get().strip() for k, v in self.fields.items()}
        data["unique_key"] = str(uuid.uuid4())
        if not is_valid_name(data["full_name"]):
            messagebox.showerror(
                "Xatolik",
                "Ism noto'g'ri. Faqat harflar va 2-32 belgidan iborat bo'lishi kerak.",
            )
            return
        if not is_valid_name(data["surname"]):
            messagebox.showerror(
                "Xatolik",
                "Familiya noto'g'ri. Faqat harflar va 2-32 belgidan iborat bo'lishi kerak.",
            )
            return
        if not is_valid_age(data["age"]):
            messagebox.showerror(
                "Xatolik", "Yosh noto'g'ri. 10-100 oralig'ida raqam kiriting."
            )
            return
        if not is_valid_email(data["email"]):
            messagebox.showerror("Xatolik", "Email noto'g'ri. Qayta kiriting.")
            return
        self.show_loader()
        self.root.after(100, lambda: self._do_save(data))

    def _do_save(self, data):
        success, err = write_user_to_sheet(data)
        self.loader_win.destroy()
        if success:
            messagebox.showinfo(
                "Muvaffaqiyatli",
                f"Ro'yxatdan o'tish muvofaqiyatli yakunlandi!\nSizning ID: {data['unique_key']}",
            )
            self.show_splash()
        else:
            messagebox.showerror("Xatolik", f"Google Sheet xatolik: {err}")


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x400")
    app = RegisterApp(root)
    root.mainloop()
