class details() :
    def __init__(self,name,lastname,phoneNumber,email,course,cost,studentNum) :
           self.name=name
           self.lastname=lastname 
           self.phoneNumber=phoneNumber
           self.course=course
           self.cost=cost
           self.email=email
           self.id=studentNum

    def smsPrint(self) :
        print("----------------------------------------")
        print(f"Aprroval massage to {self.phoneNumber}"+"\n"+f"you have signed up Succesfuly in {self.course}")
        print(f"STUDENT NAME : {self.name}")
        print(f"STUDENT SURNAME : {self.lastname}")
        print(f"STUDENT Phone Number : {self.email}")
        print(f"STUDENT ID : {self.id}")
        print(f"COURSE NAME : {self.course}")
        print(f"COURSE Cost : {self.cost} (toman)")
       

    def emailPrint(self) :
        print("----------------------------------------")
        print(f"Aprroval EMAIL to {self.email}"+"\n"+f"You have signed up Succesfuly in {self.course}")
        print(f"STUDENT NAME : {self.name}")
        print(f"STUDENT SURNAME : {self.lastname}")
        print(f"STUDENT ID : {self.id}")
        print(f"STUDENT EMAIL : {self.phoneNumber}")
        print(f"COURSE NAME : {self.course}")
        print(f"COURSE Cost : {self.cost} (toman)")
    
  