from views.bot_view import BotView
from models.user_model import upsert_user


class BotController:
    def __init__(self):
        self.view = BotView()

    def handle_start(self, message):
        self._upsert_telegram_user(message)
        self.view.send_hello(message)

    def handle_any(self, message):
        self._upsert_telegram_user(message)
        self.view.send_hello(message)

    def _upsert_telegram_user(self, message):
        user = message.from_user
        from models.user_model import upsert_user

        upsert_user(
            user_id=user.id,
            full_name=user.full_name or "",
            username=user.username or "",
        )
