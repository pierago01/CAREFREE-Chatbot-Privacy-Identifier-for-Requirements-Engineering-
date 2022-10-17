import slack
import os
from flask import Flask
from dotenv import load_dotenv
from pathlib import Path
from slackeventsapi import SlackEventAdapter

load_dotenv()

app = Flask(__name__)
slack_event_adapter = SlackEventAdapter(os.environ['SIGNING_SECRET'], '/slack/events', app)

client = slack.WebClient(token=os.environ['SLACK_TOKEN'])
BOT_ID = client.api_call("auth.test")['user_id']


@slack_event_adapter.on('message')
def message(payload):
    print(payload)
    event = payload.get('event', {})
    channel_id = event.get('channel')
    user_id = event.get('user')
    text = event.get('text')

    if event.get('bot_id') == os.environ['TRELLO_ID']:
        client.chat_postMessage(channel='casuale',text='Notifica da Trello')


if __name__ == "__main__":
    app.run(debug=True)

