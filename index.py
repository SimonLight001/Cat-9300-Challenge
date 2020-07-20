from flask import Flask
import requests
import pysnmp
from webexteamssdk import WebexTeamsAPI, Webhook
from pysnmp.entity import engine, config
from pysnmp.carrier.asyncore.dgram import udp
from pysnmp.entity.rfc3413 import ntfrcv

app = Flask(__name__)
snmpEngine = engine.SnmpEngine()
api = WebexTeamsAPI(access_token='NjExNTI0MmMtYWUwMi00NDk0LWJmMzAtZDA5NzA3ZGVkMDdhYzI0Y2MzNDUtYzYz_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f')

TrapAgentAddress='0.0.0.0'; #Trap listerner address
Port=163;  #trap listerner port

print("Agent is listening SNMP Trap on "+TrapAgentAddress+" , Port : " +str(Port));
print('--------------------------------------------------------------------------');
config.addTransport(
    snmpEngine,
    udp.domainName + (1,),
    udp.UdpTransport().openServerMode((TrapAgentAddress, Port))
)

#Configure community here
config.addV1System(snmpEngine, 'my-area', 'public')

def cbFun(snmpEngine, stateReference, contextEngineId, contextName,
          varBinds, cbCtx):
    print("Received new Trap message")
    for name, val in varBinds:        
        print('%s = %s' % (name.prettyPrint(), val.prettyPrint()))

ntfrcv.NotificationReceiver(snmpEngine, cbFun)

snmpEngine.transportDispatcher.jobStarted(1)  

try:
    snmpEngine.transportDispatcher.runDispatcher()
except:
    snmpEngine.transportDispatcher.closeDispatcher()
    raise

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
