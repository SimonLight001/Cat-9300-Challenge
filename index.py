from flask import Flask, request
import requests
import pysnmp
from webexteamssdk import WebexTeamsAPI, Webhook
#from easysnmp import Session


app = Flask(__name__)
api = WebexTeamsAPI(access_token='NjExNTI0MmMtYWUwMi00NDk0LWJmMzAtZDA5NzA3ZGVkMDdhYzI0Y2MzNDUtYzYz_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f')

@app.route("/", methods=['GET', 'POST'])
def main_page():
    if request.method == 'GET':
        return 'This is the status page'
    else:
        data = json.loads(request.data)
        SNMP_Update(data)
        return 'Successful Update'


def SNMP_Update(data):
    message_space(data)
    return True


def message_space(txt):
    roomId = "Y2lzY29zcGFyazovL3VzL1JPT00vYzM4ZDE5NTAtYzgwNC0xMWVhLWEyZTgtYjdhOWFhMmIyM2Uy"
    print(txt)
    api.messages.create(roomId, text=txt)
    return "Complete"

#forces to listen to all hosts on port 80
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("80"), debug=True)
