import smsModules as text 
import dateModules as calander
import info
import random

def  mainTab() :
    print("Welcome to coding course")
    info.main()
    choice=int(input())
    choice-=1
    print("personal informations")
    name=input('NAME :')
    lastname=input('LAST NAME :')
    while 1 == 1 :
      email=input('Email :')
      emailCheck=0
      for item in email :
          if item == "@" :
              emailCheck = 1
      if emailCheck == 1 : break
      else : print("Invalid Email")
    phoneNumber=int(input('Phone Number :'))
    id=random.randint(10000,1000000000000)
    smsTEXT=text.details(name,lastname,phoneNumber,email,info.courseTake(choice),info.costTake(choice),id)
    while 1 == 1 :
        print("1) Email")
        print("2) SMS")
        print("3) Email/SMS")
        choice=int(input())
        if choice == 1 :
            smsTEXT.emailPrint()
            calander.dateTime()
            break
        elif choice == 2 :
             smsTEXT.smsPrint()
             calander.dateTime()
             break
        elif choice == 3 :
             smsTEXT.emailPrint()
             calander.dateTime()
             smsTEXT.smsPrint()
             calander.dateTime()
             break

    
    
mainTab()

