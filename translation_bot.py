from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from googletrans import Translator
import os

# SlackアプリのBotトークン
app = App(token=os.environ.get("SLACK_BOT_TOKEN"))
translator = Translator()

# メンションに反応するイベント
@app.event("app_mention")
def handle_mentions(body, say):
    text = body["event"]["text"]
    query = text.split(" ", 1)[1] if " " in text else ""
    if query:
        translated = translator.translate(query, dest="en").text
        say(f"🇬🇧 {translated}")
    else:
        say("翻訳したい文章を @translation のあとに入力してください。")

if __name__ == "__main__":
    handler = SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"])
    handler.start()

