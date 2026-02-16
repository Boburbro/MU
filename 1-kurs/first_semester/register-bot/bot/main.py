import telebot
from controllers.bot_controller import BotController
from controllers.registration_controller import (
    start_registration,
    handle_registration,
    cancel_registration,
    user_states,
    STATE_NONE,
)
from config import API_TOKEN

bot = telebot.TeleBot(API_TOKEN)
controller = BotController()


@bot.message_handler(commands=["start"])
def start_handler(message):
    controller.handle_start(message)


@bot.message_handler(func=lambda m: m.text == "🚀 Ro'yxatdan o'tishni boshlash")
def registration_start_handler(message):
    start_registration(message)


@bot.message_handler(func=lambda m: m.text == "Ro'yxatdan o'tishni bekor qilish")
def registration_cancel_handler(message):
    cancel_registration(message)


@bot.message_handler(
    func=lambda m: user_states.get(m.from_user.id, STATE_NONE) != STATE_NONE
)
def registration_flow_handler(message):
    handle_registration(message)


@bot.message_handler(func=lambda m: True)
def all_handler(message):
    controller.handle_any(message)


if __name__ == "__main__":
    bot.polling(none_stop=True)
