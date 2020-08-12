import csv

snmp_push = input("What's the test SNMP input: ")

with open ('stripped_sys_messages.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 1
    found = False
    for row in csv_reader:
        if row[0] == snmp_push:
            print(snmp_push + " is in line: " + str(line_count) + ". The " + row[1] + " team should be alerted")
            found = True
    if found == False:
        print("This is an error not in our logs")
