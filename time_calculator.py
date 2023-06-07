def add_time(start, duration, dayOfWeek = False):
  daysOfTheWeekIndex = {"monday" : 0, "tuesday" : 1, "wednesday" : 2, "thursday" : 3, "friday" : 4, "saturday" : 5, "sunday" : 6}
  
  daysOfTheWeekArray = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

  durationList = list()
  durationList = duration.split(":")
  durationHours = int(durationList[0])
  durationMinutes = int(durationList[1])
  
  startList = start.split(":")
  startMinutesList = startList[1].split(" ")
  amOrPm = startMinutesList[1]
  startHours = int(startList[0])
  startMinutes = int (startMinutesList[0])
  amPmShift = {"AM": "PM", "PM": "AM"}
  amountOfDays = int(durationHours / 24)

  endMinutes = startMinutes + durationMinutes
  if (endMinutes >= 60):
    startHours += 1
    endMinutes = endMinutes % 60

  endHours = (startHours + durationHours) % 12
  
  if (endMinutes > 9):
    endMinutes = endMinutes
  else:
    endMinutes = "0" + str(endMinutes)

  if (amOrPm == "PM" and startHours + (durationHours % 12) >= 12):
    amountOfDays += 1
  
  if (endHours == 0):
    endHours = 12
  else:
    endHours = endHours

  amountAmPmShift = int((startHours + durationHours) / 12)
  if (amountAmPmShift % 2) == 1:
    amOrPm = amPmShift[amOrPm]
  else:
    amOrPm = amOrPm

  returnTime = str(endHours) + ":" + str(endMinutes) + " " + amOrPm

  if (dayOfWeek):
    dayOfWeek = dayOfWeek.lower()
    index = int(((daysOfTheWeekIndex[dayOfWeek]) + amountOfDays) % 7)
    newDay = daysOfTheWeekArray[index]
    returnTime = returnTime + ", " + newDay

  if (amountOfDays == 1):
    return returnTime + " (next day)" 
  elif (amountOfDays > 1):
    return returnTime + " (" + str(amountOfDays) + " days later)"
  
  return returnTime
