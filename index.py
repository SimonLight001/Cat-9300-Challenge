from flask import Flask
import requests
import pysnmp
from webexteamssdk import WebexTeamsAPI, Webhook

app = Flask(__name__)
api = WebexTeamsAPI(access_token='NjExNTI0MmMtYWUwMi00NDk0LWJmMzAtZDA5NzA3ZGVkMDdhYzI0Y2MzNDUtYzYz_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f')

print("--- Starting teams bot ---")

@app.route("/")
def send_message():
    roomId = "Y2lzY29zcGFyazovL3VzL1JPT00vYzM4ZDE5NTAtYzgwNC0xMWVhLWEyZTgtYjdhOWFhMmIyM2Uy"
    api.messages.create(roomId, text="Testing123")
    return "Complete"

@app.route("/message/")
def get_message():
    url = "http://webexapis.com/v1/messages?roomId=Y2lzY29zcGFyazovL3VzL1JPT00vYzM4ZDE5NTAtYzgwNC0xMWVhLWEyZTgtYjdhOWFhMmIyM2Uy"
    headers = {'Authrorization':'Bearer NjExNTI0MmMtYWUwMi00NDk0LWJmMzAtZDA5NzA3ZGVkMDdhYzI0Y2MzNDUtYzYz_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f'}
    try:
        r = requests.get(url)
        return r.text
    except requests.exceptions.ConnectionError:
        return "error"

    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("80"), debug=True)
