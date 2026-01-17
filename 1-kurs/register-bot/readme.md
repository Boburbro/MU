 # Register-bot

Bu loyiha ikki qismdan iborat: 1) Tkinter orqali ishga tushadigan Desktop ro'yxatdan o'tish ilovasi va 2) Telegram bot (telebot) orqali ro'yxatdan o'tish oqimi.

**Vazifasi:** foydalanuvchilarning ism, familiya, yosh va email ma'lumotlarini Google Sheets-ga yozish va Telegram orqali ro'yxatga olish jarayonini boshqarish.

**Talablar:**
- Python 3.8 yoki undan yuqori
- System package: `python3-tk` (GUI uchun, Linuxda)
- Pip paketlari (quyida)

**O'rnatish:**
1. Virtual muhit yarating va faollashtiring:

```
python3 -m venv venv
source venv/bin/activate
```

2. Paketlarni o'rnating (loyiha ildizida):

```
pip install -r requirements.txt
pip install pyTelegramBotAPI gspread oauth2client
```

**Konfiguratsiya (.env):**
Loyiha ildizida `.env` faylini yarating va quyidagilarni to'ldiring:

```
API_TOKEN=YOUR_TELEGRAM_BOT_TOKEN
GOOGLE_SHEET_URL=https://docs.google.com/spreadsheets/d/XXX/...
MYSQL_HOST=localhost
MYSQL_USER=your_db_user
MYSQL_PASSWORD=your_db_password
MYSQL_DB=your_db_name
```

`GOOGLE_SHEET_URL` — Google Sheets hujjatining URL manzili. `API_TOKEN` — sizning Telegram bot token.

Shuningdek, Google Sheets uchun service account JSON faylini `bot/credentials.json` nomi bilan joylashtiring.

**Ishga tushirish:**

- Desktop GUI ilovasini ishga tushirish (mahalliy kompyuter, grafik muhiti kerak):

```
python register_app.py
```

- Telegram botni ishga tushirish (server yoki mahalliy mashina):

```
python -m bot.main
```

**MySQL bazasini yaratish (ixtiyoriy):**
`bot/create_db.py` skripti `.env` dagi MySQL ma'lumotlari asosida DB va user yaratadi. Skriptni ishga tushurish uchun `bot/create_db.py` ichidagi `admin_user` va `admin_password` maydonlarini moslashtiring, keyin:

```
python bot/create_db.py
```

**Fayllar haqida qisqacha:**
- `register_app.py` — Tkinter GUI, foydalanuvchi ma'lumotlarini Google Sheets ga yuboradi.
- `bot/main.py` — Telegram botning asosiy polling loop.
- `bot/credentials.json` — Google service account kaliti (xavfsiz joyda saqlang).
- `bot/config.py` — `.env` dan konfiguratsiyalarni yuklaydi.
- `bot/create_db.py` — MySQL db va user yaratish uchun yordamchi skript.

**Muammolar va maslahatlar:**
- Agar GUI ishlamasa, `python3-tk` paketining o'rnatilganligini tekshiring.
- Telegram bot uchun `API_TOKEN` to'g'ri ekanligini va bot aktivligini tekshiring.
- Google Sheets bilan ishlaganda `bot/credentials.json` va `GOOGLE_SHEET_URL` mos kelishi kerak.

Savol bo'lsa yoki yordam kerak bo'lsa, yozing — yordam beraman.

