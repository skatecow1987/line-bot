

from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('b0fn45ik/NPDWwp2BCWr4oE/XJikXlgBxdFlPey/A9SdOrZ6NxYHKPV28tsFdx2/8cQYI0yhxkyP1FlSUxp3v2xDsTnC+QRbbl30fwj4jK5cFpK/WZHkjs6z7SZFU71J2F2P2EWzh8cVXZVekqKoRQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('fff6f38d6208a1a76e4e4f36b40034a2')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    r = '我不懂你說甚麼'

    if msg == 'hi':
        r = 'hi'
    elif msg == '你吃飯了嗎'
       	r = '還沒'

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))


if __name__ == "__main__":
    app.run()