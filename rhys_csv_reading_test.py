import csv
from webexteamssdk import WebexTeamsAPI, Webhook
import time
import random

#snmp_push = input("What's the test SNMP input: ") <-- old code used before snmp_generator()
api = WebexTeamsAPI(access_token='NjExNTI0MmMtYWUwMi00NDk0LWJmMzAtZDA5NzA3ZGVkMDdhYzI0Y2MzNDUtYzYz_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f')

def snmp_generator():
    # This code, every 22s, picks an snmp and calls functions to post details in the chat
    while True:
        snmp_selection = ['cpsIfViolationAction', 'BGP-2-INSUFMEM', 'badsnmpvalue', 'NAT64-3-ENOMEM', 'AAAA-3-AAAFORKFAIL']
        snmp_push = random.choice(snmp_selection)
        print("Collected SNMP: " + snmp_push)
        team, severity, message, explanation, component, action = CSV_Reading(snmp_push)
        send_message(team, severity, message, explanation, component, action, snmp_push)
        time.sleep(12)

def CSV_Reading(snmp_push):
    with open ('stripped_sys_messages.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        column_number = 1
        found = False
        for row in csv_reader:
            if row[0] == snmp_push:
                return row[1], row[2], row[3], row[4], row[5], row[6]
                # ^^ above returns team, severity, message, message_expl, component, action
                found = True
            else:
                column_number+=1
        if found == False:
            return "", "", "", "", "", ""

def send_message(team, severity, message, explanation, component, action, snmp_push):
    room_id = ""
    if team == "Network":
        room_id = "Y2lzY29zcGFyazovL3VybjpURUFNOnVzLWVhc3QtMl9hOmlkZW50aXR5TG9va3VwL1JPT00vZTg4YmJkYzAtZDY2My0xMWVhLTgxMTgtMTFjNTkwNThlZjQ3"
    elif team == "Security":
        room_id = "Y2lzY29zcGFyazovL3VybjpURUFNOnVzLWVhc3QtMl9hOmlkZW50aXR5TG9va3VwL1JPT00vZTI0ZjM2ZDAtZDY2My0xMWVhLWE2ODUtN2Y5YWJjMDM4M2Ix"
    else:
        print("team/snmp not understood")
        return "team/snmp not understood" # Breaks the def as nothing found in csv
    markdown_txt = "**New SNMP message:**"
    api.messages.create(room_id, markdown="**New SNMP Message!**")
    api.messages.create(room_id, markdown="*Name: " + snmp_push + "*")
    api.messages.create(room_id, text="Severity: " + severity)
    api.messages.create(room_id, text="Message: " + message)
    api.messages.create(room_id, text="Explanation: " + explanation)
    api.messages.create(room_id, text="Component: " + component)
    api.messages.create(room_id, text="Recommended Action: " + action)
    return "Messages sent"

snmp_generator()
