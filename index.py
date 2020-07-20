from flask import Flask
import requests
import pysnmp
from webexteamssdk import WebexTeamsAPI, Webhook

app = Flask(__name__)
api = WebexTeamsAPI(access_token='NjExNTI0MmMtYWUwMi00NDk0LWJmMzAtZDA5NzA3ZGVkMDdhYzI0Y2MzNDUtYzYz_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f')

@app.route("/", methods=['GET'])
def webhook_events():
    return message_space("refactor")

def message_space(txt):
    roomId = "Y2lzY29zcGFyazovL3VzL1JPT00vYzM4ZDE5NTAtYzgwNC0xMWVhLWEyZTgtYjdhOWFhMmIyM2Uy"
    api.messages.create(roomId, text=txt)
    return "Complete"
    









#forces to listen to all hosts on port 80
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("80"), debug=True)
