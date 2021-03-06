file = open("Hackathon Data - user.csv","r")
userFile = file.read()
file.close()
file = open("Hackathon Data - trips.csv","r")
tripFile = file.read()
file.close

userAndTrip = []
users = []
trips = []
userAllLists = userFile.split("\n")
tripAllLists = tripFile.split("\n")

for i in userAllLists:
    x = i.split(",")
    users.append(x)

for i in tripAllLists:
    x = i.split(",")
    trips.append(x)

jsonList = []
usersTotal = len(users)
userCount = 0
jsonList.append('{"user":[')
for i in users:
    x = '\t{"breezecard_id":"' + str(i[0]) + '",' \
                '"first_name":"' + str(i[1]) + '",' \
                '"last_name":"' + str(i[2]) + '",' \
                '"dob":"' + str(i[3]) + '",' \
                '"date_joined":"' + str(i[4]) + '",' \
                '"username":"' + str(i[5]) + '",' \
                '"password":"' + str(i[6]) + '",' \
                '"trips": ['
    jsonList.append(x)
    tripCount = 0
    iterations = 1
    userCount += 1
    if userCount == usersTotal:
        for j in trips:
            if i[0] == j[1]:
                    tripCount += 1
        for j in trips:
            if i[0] == j[1] and iterations < tripCount:
                y = '\t\t{"trip_id":"' + str(j[0]) + '",' \
                    '"Breezecard_id":"' + str(j[1]) + '",' \
                    '"Route_Type":"' +str(j[2]) + '",' \
                    '"stop_enter_name":"' + str(j[3]) + '",' \
                    '"stop_enter_lat":' + str(j[4]) +',' \
                    '"stop_enter_long":' + str(j[5]) + ',' \
                    '"stop_exit_name":"' + str(j[6]) + '",' \
                    '"stop_exit_lat":' + str(j[7]) + ',' \
                    '"stop_exit_long":' + str(j[8]) + ',' \
                    '"trip_date":"' + str(j[9]) + '",' \
                    '"trip_mileage":' + str(j[10]) + ',' \
                    '"trip_duration":' + str(j[11]) + ',' \
                    '"fare":' + str(j[12]) + '},'               
                jsonList.append(y)
                iterations += 1
            elif i[0] == j[1]:
                y = '\t\t{"trip_id":"' + str(j[0]) + '",' \
                    '"Breezecard_id":"' + str(j[1]) + '",' \
                    '"Route_Type":"' +str(j[2]) + '",' \
                    '"stop_enter_name":"' + str(j[3]) + '",' \
                    '"stop_enter_lat":' + str(j[4]) +',' \
                    '"stop_enter_long":' + str(j[5]) + ',' \
                    '"stop_exit_name":"' + str(j[6]) + '",' \
                    '"stop_exit_lat":' + str(j[7]) + ',' \
                    '"stop_exit_long":' + str(j[8]) + ',' \
                    '"trip_date":"' + str(j[9]) + '",' \
                    '"trip_mileage":' + str(j[10]) + ',' \
                    '"trip_duration":' + str(j[11]) + ',' \
                    '"fare":' + str(j[12]) + '}]}'
                jsonList.append(y)
        if tripCount == 0:
            jsonList.append('{}]}')
    else:
        for j in trips:
            if i[0] == j[1]:
                    tripCount += 1
        for j in trips:
            if i[0] == j[1] and iterations < tripCount:
                y = '\t\t{"trip_id":"' + str(j[0]) + '",' \
                    '"Breezecard_id":"' + str(j[1]) + '",' \
                    '"Route_Type":"' +str(j[2]) + '",' \
                    '"stop_enter_name":"' + str(j[3]) + '",' \
                    '"stop_enter_lat":' + str(j[4]) +',' \
                    '"stop_enter_long":' + str(j[5]) + ',' \
                    '"stop_exit_name":"' + str(j[6]) + '",' \
                    '"stop_exit_lat":' + str(j[7]) + ',' \
                    '"stop_exit_long":' + str(j[8]) + ',' \
                    '"trip_date":"' + str(j[9]) + '",' \
                    '"trip_mileage":' + str(j[10]) + ',' \
                    '"trip_duration":' + str(j[11]) + ',' \
                    '"fare":' + str(j[12]) + '},'               
                jsonList.append(y)
                iterations += 1
            elif i[0] == j[1]:
                y = '\t\t{"trip_id":"' + str(j[0]) + '",' \
                    '"Breezecard_id":"' + str(j[1]) + '",' \
                    '"Route_Type":"' +str(j[2]) + '",' \
                    '"stop_enter_name":"' + str(j[3]) + '",' \
                    '"stop_enter_lat":' + str(j[4]) +',' \
                    '"stop_enter_long":' + str(j[5]) + ',' \
                    '"stop_exit_name":"' + str(j[6]) + '",' \
                    '"stop_exit_lat":' + str(j[7]) + ',' \
                    '"stop_exit_long":' + str(j[8]) + ',' \
                    '"trip_date":"' + str(j[9]) + '",' \
                    '"trip_mileage":' + str(j[10]) + ',' \
                    '"trip_duration":' + str(j[11]) + ',' \
                    '"fare":' + str(j[12]) + '}]},'
                jsonList.append(y)
        if tripCount == 0:
            jsonList.append('{}]},')
jsonList.append(']}')
f = open("output.txt", "w")
for item in jsonList:
    f.write(item + "\n")
f.close()
