from dotenv import load_dotenv
import os
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
load_dotenv()
line_bot_api = LineBotApi(os.getenv('LINE_ACCESS_TOKEN'))

def send_message(text):
    line_bot_api.push_message(os.getenv('LINE_USER_ID'), TextSendMessage(text=text))

# 測試
# send_message("hi Neil")