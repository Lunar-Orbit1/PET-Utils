# Atmois
# https://replit.com/@Atmois/PET-Message-Writer?v=1 (Last Updated: 16/04/23)

import time
import datetime
import math

print(
  "Welcome to the Message Typer for PET Events! Follow the Steps Below for a Message for All Circumstances in Scheduling or Hosting! ~ Developed by Atmois"
)

mode = input("Mode - Schedule or Announce:")
mode = mode.lower()

if mode == "schedule" or mode == "announce":

  eventtype = input("Event Type - RR or Support:").strip()
  eventtype = eventtype.lower()

  if eventtype == 'rr':

    if mode == 'schedule':
      host = input("Please Enter the Raid Host's Name:")
      type = input(
        "Please Enter the Raid Type - Meltdown, Freezedown, Incursion or Chaos:"
      )
      level = input("Enter the Raid Level - L1 or L2:")
      if level == 'l1' or level == 'L1':
        points = "5"
      elif level == 'l2' or level == 'L2':
        points = "6"
      else:
        print("That is Not a Valid Entry Prompt Please Restart the Program.")
        exit()
      year = input("Enter the Year the Event Occurs On:")
      month = input("Enter the Month of Year the Event Occurs On:")
      day = input("Enter the Day of the Month the Event Occurs On:")
      hour = input("Enter the Hour of the Day the Event Occurs On:")
      minute = input("Enter the Time in the Hour the Event Occurs On:")
      second = 0
      date_time = datetime.datetime(int(year), int(month), int(day), int(hour),
                                    int(minute), int(second))
      timestamp = (time.mktime(date_time.timetuple()))
      timestamp = math.floor(timestamp)

      print("Timestamp:", timestamp)
      print("Raid Response! Responding to", host + "'s", level, type,
            "Raid! Gain Up to", points, "Points by Attending!")
      exit()

    elif mode == 'announce':
      host = input("Please Enter the Raid Host's Name:")
      type = input(
        "Please Enter the Raid Type - Meltdown, Freezedown, Incursion or Chaos:"
      )
      level = input("Enter the Raid Level - L1 or L2:")
      if level == 'l1' or level == 'L1':
        points = "5"
      elif level == 'l2' or level == 'L2':
        points = "6"
      link = input("Please Enter the Joining Link:")
      print("@here Raid Response! Responding to", host + "'s", level, type,
            "Raid! Gain Up to", points,
            "Points by Attending! Join and Begin Straight Away! Link:", link)
      time.sleep(1)
      print(";db shout Raid Response! Responding to", host + "'s", level, type,
            "Raid! Join and Begin Straight Away! Link:", link)
      exit()

  elif eventtype == 'support':

    if mode == 'schedule':
      host = input("Please Enter the PBST Host's Name:")
      length = input("Please Enter the Event's Length:")
      length = int(length)
      points = length / 15
      points = math.floor(points)

      year = input("Enter the Year the Event Occurs On:")
      month = input("Enter the Month of Year the Event Occurs On:")
      day = input("Enter the Day of the Month the Event Occurs On:")
      hour = input("Enter the Hour of the Day the Event Occurs On:")
      minute = input("Enter the Time in the Hour the Event Occurs On:")
      second = 0
      date_time = datetime.datetime(int(year), int(month), int(day), int(hour),
                                    int(minute), int(second))
      timestamp = (time.mktime(date_time.timetuple()))
      timestamp = math.floor(timestamp)

      print("Timestamp:", timestamp)
      print("PBST Patrol Support! Supporting",
            host + "'s PBST Patrol! Gain Up to", points,
            "Points by Attending!")
      exit()

    elif mode == 'announce':
      host = input("Please Enter the PBST Host's Name:")
      length = input("Please Enter the Event's Length:")
      length = int(length)
      points = length / 15
      points = math.floor(points)
      link = input("Please Enter the Joining Link:")
      print("@here PBST Patrol Support! Supporting",
            host + "'s PBST Patrol! Gain Up to", points,
            "Points by Attending! Join and STS at PET HQ! Link:", link)
      time.sleep(1)
      print(";db shout PBST Patrol Support! Supporting",
            host + "'s PBST Patrol! Join and STS at PET HQ! Link:", link)
      exit()

  else:
    print("That is Not a Valid Entry Prompt Please Restart the Program.")
    exit()

else:
  print("That is Not a Valid Entry Prompt Please Restart the Program.")
  exit()
