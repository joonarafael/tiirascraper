import requests

from env import TELEGRAM_BOT_API_KEY, CHAT_IDS

class Messenger():
    def __init__(self, io, io_constants):
        self.io = io
        self.io_constants = io_constants

        self.token = TELEGRAM_BOT_API_KEY
        self.chat_ids = CHAT_IDS

    def send_message(self, message):
        try:
            for chat_id in self.chat_ids:
                url = f"https://api.telegram.org/bot{self.token}/sendMessage?chat_id={chat_id}&text={message}"
                requests.get(url)

        except Exception as e:
            self.io.write(self.io_constants.BOLD + self.io_constants.BG_RED + "[ERRR] Error while sending the Telegram Message.")
            self.io.write(f"       {str(e)}.")