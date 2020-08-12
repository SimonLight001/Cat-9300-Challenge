import csv
from webexteamssdk import WebexTeamsAPI, Webhook

snmp_push = input("What's the test SNMP input: ")
severity_append = "Severity: "
#CSV_Reading(snmp_push)
api = WebexTeamsAPI(access_token='NjExNTI0MmMtYWUwMi00NDk0LWJmMzAtZDA5NzA3ZGVkMDdhYzI0Y2MzNDUtYzYz_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f')


def CSV_Reading(snmp_push):
    #FOR RHYS' TESTING: snmp_push = input("What's the test SNMP input: ")
    with open ('stripped_sys_messages.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        column_number = 1
        found = False
        for row in csv_reader:
            if row[0] == snmp_push:
                return row[1], row[2], row[3], row[4], row[5], row[6]
                #return team, severity, message, message_expl, component, action
                found = True
            else:
                column_number+=1
        if found == False:
            return "", "", "", "", "", ""
            #print("This is an error not in our logs")

team, severity, message, explanation, component, action = CSV_Reading(snmp_push)
if team == "Network":
    room_id = "Y2lzY29zcGFyazovL3VybjpURUFNOnVzLWVhc3QtMl9hOmlkZW50aXR5TG9va3VwL1JPT00vZTg4YmJkYzAtZDY2My0xMWVhLTgxMTgtMTFjNTkwNThlZjQ3"
    markdown_txt = "*New SNMP message:*"
    api.messages.create(room_id, markdown=markdown_txt)
    severity = "Severity: " + severity
    api.messages.create(room_id, text=severity)
    api.messages.create(room_id, text=message)
    api.messages.create(room_id, text=explanation)
    api.messages.create(room_id, text=component)
    api.messages.create(room_id, text=action)

elif team == "Security":
    room_id = "Y2lzY29zcGFyazovL3VybjpURUFNOnVzLWVhc3QtMl9hOmlkZW50aXR5TG9va3VwL1JPT00vZTI0ZjM2ZDAtZDY2My0xMWVhLWE2ODUtN2Y5YWJjMDM4M2Ix"
    markdown_txt = "*New SNMP message:*"
    api.messages.create(room_id, markdown=markdown_txt)
    severity = "Severity: " + severity
    api.messages.create(room_id, text=severity)
    api.messages.create(room_id, text=message)
    api.messages.create(room_id, text=explanation)
    api.messages.create(room_id, text=component)
    api.messages.create(room_id, text=action)
else:
    print("team/snmp not understood")
