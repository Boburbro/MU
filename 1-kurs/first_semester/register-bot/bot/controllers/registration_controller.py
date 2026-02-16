from config import API_TOKEN
import telebot

bot = telebot.TeleBot(API_TOKEN)

from models.google_sheet import write_user_to_sheet

bot = telebot.TeleBot(API_TOKEN)

# Registration states
STATE_NONE = 0
STATE_NAME = 1
STATE_SURNAME = 2
STATE_AGE = 3
STATE_EMAIL = 4
STATE_DONE = 5

# In-memory user state and data (for demo, use DB for production)
user_states = {}
user_data = {}


# Validation helpers
def is_valid_name(name):
    return name.isalpha() and 2 <= len(name) <= 32


def is_valid_age(age):
    return age.isdigit() and 10 <= int(age) <= 100


def is_valid_email(email):
    import re

    return re.match(r"^[\w\.-]+@[\w\.-]+\.\w{2,}$", email)


# Cancel button markup
def cancel_markup():
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(telebot.types.KeyboardButton("❌ Ro'yxatdan o'tishni bekor qilish"))
    return markup


# Start registration
def start_registration(message):
    user_states[message.from_user.id] = STATE_NAME
    user_data[message.from_user.id] = {}
    bot.send_message(
        message.chat.id, "Ismingizni kiriting:", reply_markup=cancel_markup()
    )


# Handle registration steps
def handle_registration(message):
    uid = message.from_user.id
    state = user_states.get(uid, STATE_NONE)
    data = user_data.get(uid, {})
    # Cancel registration if cancel button pressed
    if message.text == "❌ Ro'yxatdan o'tishni bekor qilish":
        cancel_registration(message)
        return
    if state == STATE_NAME:
        if not is_valid_name(message.text):
            bot.send_message(
                message.chat.id,
                "Ism noto'g'ri. Faqat harflar va 2-32 belgidan iborat bo'lishi kerak.",
            )
            return
        data["name"] = message.text
        user_states[uid] = STATE_SURNAME
        bot.send_message(
            message.chat.id, "Familiyangizni kiriting:", reply_markup=cancel_markup()
        )
    elif state == STATE_SURNAME:
        if not is_valid_name(message.text):
            bot.send_message(
                message.chat.id,
                "Familiya noto'g'ri. Faqat harflar va 2-32 belgidan iborat bo'lishi kerak.",
            )
            return
        data["surname"] = message.text
        user_states[uid] = STATE_AGE
        bot.send_message(
            message.chat.id,
            "Yoshingizni kiriting (10-100):",
            reply_markup=cancel_markup(),
        )
    elif state == STATE_AGE:
        if not is_valid_age(message.text):
            bot.send_message(
                message.chat.id, "Yosh noto'g'ri. 10-100 oralig'ida raqam kiriting."
            )
            return
        data["age"] = int(message.text)
        user_states[uid] = STATE_EMAIL
        bot.send_message(
            message.chat.id, "Emailingizni kiriting:", reply_markup=cancel_markup()
        )
    elif state == STATE_EMAIL:
        if not is_valid_email(message.text):
            bot.send_message(message.chat.id, "Email noto'g'ri. Qayta kiriting.")
            return
        data["email"] = message.text
        user_states[uid] = STATE_DONE
        # Save data to DB
        from models.user_model import upsert_user

        db_error = None
        sheet_error = None
        try:
            upsert_user(
                user_id=uid,
                full_name=f"{data['name']} {data['surname']}",
                username=message.from_user.username or "",
                surname=data["surname"],
                age=data["age"],
                email=data["email"],
            )
        except Exception as e:
            db_error = str(e)
        try:
            write_user_to_sheet(
                {
                    "id": uid,
                    "full_name": f"{data['name']} {data['surname']}",
                    "username": message.from_user.username or "",
                    "surname": data["surname"],
                    "age": data["age"],
                    "email": data["email"],
                }
            )
        except Exception as e:
            sheet_error = str(e)
        if db_error:
            bot.send_message(message.chat.id, f"DB xatolik: {db_error}")
        if sheet_error:
            bot.send_message(message.chat.id, f"Google Sheet xatolik: {sheet_error}")
        bot.send_message(
            message.chat.id,
            "Ro'yxatdan o'tish muvofaqiyatli yakunlandi!",
            reply_markup=telebot.types.ReplyKeyboardRemove(),
        )
        # Show summary
        bot.send_message(
            message.chat.id,
            f"Sizning ma'lumotlaringiz:\nIsm: {data['name']}\nFamiliya: {data['surname']}\nYosh: {data['age']}\nEmail: {data['email']}",
        )
        # Clean up state
        user_states[uid] = STATE_NONE
        user_data[uid] = data


# Cancel registration
def cancel_registration(message):
    uid = message.from_user.id
    user_states[uid] = STATE_NONE
    user_data.pop(uid, None)
    bot.send_message(
        message.chat.id,
        "Ro'yxatdan o'tish bekor qilindi.",
        reply_markup=telebot.types.ReplyKeyboardRemove(),
    )
