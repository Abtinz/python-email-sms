import datetime
def dateTime() :
   date=datetime.datetime.now()
   print(f"Date : {date.year} / {date.month} / {date.day}")
   print(f"clock : {date.hour}:{date.minute}:{date.second}")
   print("----------------------------------------")