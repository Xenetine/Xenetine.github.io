import csv
from datetime import date, datetime
from pytz import timezone, utc
import pytz

all_roster= open('rostertest.csv')
file = csv.DictReader(all_roster)

Studentid = []
Student = []
Guardian = []
Guardianemail = []
Nameidguardemail_dict = {}

for col in file:
  Studentid.append(col['ID Number'])
  Student.append(col['Name'])
  Guardian.append(col['Guardian 1'])
  Guardianemail.append(col['Guardian 1 email'])

for i in range(len(Studentid)):
  Nameidguardemail_dict[Studentid[i]] = {
    'Student': Student[i],
    'Guardian': Guardian[i],
    'Guardian email': Guardianemail[i]
    }

def Bathroom_checkout():
  ID1 = input('Enter your ID to check out: ')
  timeout = datetime.now(tz=pytz.utc)
  timeout = timeout.astimezone(timezone('US/Pacific'))
  time1 = timeout.strftime ('%I:%M:%S %p')
  if ID1 not in Studentid:
    print ("ID not recognized in the system.  Try again")
    Bathroom_checkout()
  if ID1 in Studentid:
    print (Nameidguardemail_dict[ID1].get('Student'),', you left the classroom at:', time1)
    Bathroom_checkin(ID1,timeout,time1)

def Bathroom_checkin(ID1,timeout,time1):  
  ID2 = input('Enter your ID to check in: ')
    
  if ID2 not in Studentid:
    print ("ID not recognized in the system.  Try again")
    Bathroom_checkin(ID1,timeout,time1)
  if ID2 != ID1:
    print("Wait your turn.")
    Bathroom_checkin(ID1,timeout,time1)
  if ID2 == ID1:
    timein = datetime.now(tz=pytz.utc)
    timein = timein.astimezone(timezone('US/Pacific'))
    time2 = timein.strftime ('%I:%M:%S %p')

    totaltime = (timein-timeout)

    print ('You returned to the classroom at:', time2)
    print ('You were out of class for',totaltime)
        
    Bathroom_record(ID1, time1, ID2, time2, totaltime)


def Bathroom_record(ID, time1, ID2, time2, totaltime):
  Result = {'ID': ID ,'Name': Nameidguardemail_dict[ID].get('Student'),'Day': date.today(), 'Start_time': time1, 'End_time': time2, 'Time': totaltime}

  with open("Bathroom.csv", "a", newline='') as csvfile:
    fieldnames = ['ID','Name','Day',"Start_time","End_time",'Time']
    writer_object = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer_object.writerow(Result)
        
  Bathroom_checkout()

Bathroom_checkout()
