import slack
import os
from flask import Flask
from slackeventsapi import SlackEventAdapter

SLACK_TOKEN = "xoxb-4203317923554-4200442240501-XkAdLkWB1ob4CIeR9V9RoN8H"

app = Flask()

client = slack.WebClient(token=SLACK_TOKEN)
client.chat_postMessage(channel='casuale',text='Hello')