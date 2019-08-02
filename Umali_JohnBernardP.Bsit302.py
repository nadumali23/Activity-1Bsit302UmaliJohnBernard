#TODO:
#Duplicate Entry
#Remove/Edit Employee
#Sub Options


print("Welcome to my Employee Management System by: John Bernard Umali")

loop = True
list = []



class Employee:
    def __init__(self, id, name, department, position, rate):
        self.id = id
        self.name = name
        self.department = department
        self.position = position
        self.rate = rate
    

while loop:
    print("================================")
    print("[0] - Add New Employee")
    print("[1] - Calculate Salary")
    print("[2] - Show Employee ")
    print("[3] - Show Employee Information")
    print("[4] - Exit")

    opt = int(input("Enter Option: "))
    print("================================")
    if opt == 0:
        id = int(input("Enter Employee Number: "))
        name = input("Enter Employee Name: ")
        department = input("Enter Department: ")
        position = input("Enter Position: ")
        salary = float(input("Salary Rate: "))
        empA = [id, name, department ,position, salary]
        list.append(empA)
        print("================================")
        print("New Employee Added.")
        print("================================")
    elif opt == 1:
            empNo = int(input("Employee number: "))
            hours = int(input("Enter Employee Hours: "))
            x = True
            counter = 0
            tmpEmpNo = empNo
            
            while x:
                try:
                    tmparray = (list[counter])
                    if tmpEmpNo == tmparray[0]:
                        tmpEmpNo == tmparray[0]
                        x = True
                        print("Employee ID: " + str(tmparray[0]))
                        print("Employee Name: " + str(tmparray[1]))
                        print("Employee Department: " + str(tmparray[2]))
                        print("Employee Position: " + str(tmparray[3]))
                        print("Employee Salary: " + str(float(tmparray[4]) * hours))
                        break
                    else:
                        counter+=1
                except IOError :
                    print("Employee Not Found!")
                    break
                    
    elif opt == 2:
        x = True
        counter = 0
        tmpname = ""
        while x:
            try:
                tmparray = (list[counter])
                if tmpname == tmparray[1]:
                    x = True
                else:
                    print("Employee ID: [" + str(tmparray[0]) + "] - " + tmparray[1])
                    tmpname == tmparray[1]
                counter+=1
            except:
                print("================================")
                print("**Nothing Follows**")
                break
            
            
    elif opt == 3:
            empNo = int(input("Employee number: "))
            x = True
            counter = 0
            tmpEmpNo = empNo
            
            while x:
                try:
                    tmparray = (list[counter])
                    if tmpEmpNo == tmparray[0]:
                        tmpEmpNo == tmparray[0]
                        print("==============================")
                        print("Employee ID: " + str(tmparray[0]))
                        print("Employee Name: " + str(tmparray[1]))
                        print("Employee Department: " + str(tmparray[2]))
                        print("Employee Position: " + str(tmparray[3]))
                        print("Employee Rate: " + str(tmparray[4]))
                        print("==============================")
                        x = True
                        break
                    else:
                        counter+=1
                except :
                    print("Employee Not Found!")
                    break
    elif opt == 4:
        print("Closing Program....")
        loop = False
    else:
        print("Invalid Input!")
