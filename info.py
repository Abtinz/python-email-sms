courses = {
    "cost" : [],
    "name" : []
}

def defualt() :

    courses["name"].append("Java")
    courses["cost"].append(150000)
    
    courses["name"].append("Python")
    courses["cost"].append(100000)
    
    courses["name"].append("Html Css")
    courses["cost"].append(50000)

    courses["name"].append("(C/C++/C#)")
    courses["cost"].append(200000)

    courses["name"].append("Php")
    courses["cost"].append(80000)

    courses["name"].append("Java Script")
    courses["cost"].append(75000)

    courses["name"].append("Asp.net core")
    courses["cost"].append(100000)

    courses["name"].append("Type script")
    courses["cost"].append(90000)

    courses["name"].append("SQL Server")
    courses["cost"].append(100000)

defualt()
def main() :
    num=0
    print("Availabe courses : ") 
    for item in courses['cost'] :
       print(f"{num + 1}) {courses['name'][num]} / {item}(Toman) ")
       num-=-1

def courseTake(index) :
    courseName = courses['name'][index]
    return courseName

def costTake(index) :
    courseCost = courses['cost'][index]
    return courseCost

