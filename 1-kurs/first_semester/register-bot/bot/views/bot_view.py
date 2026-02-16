from config import API_TOKEN
import telebot

bot = telebot.TeleBot(API_TOKEN)


class BotView:
    def send_hello(self, message):
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(telebot.types.KeyboardButton("🚀 Ro'yxatdan o'tishni boshlash"))
        bot.send_message(
            message.chat.id,
            "👋 Salom! Botimizga xush kelibsiz!\n\nRo'yxatdan o'tishni boshlash uchun pastdagi 🚀 tugmani bosing.",
            reply_markup=markup,
        )
