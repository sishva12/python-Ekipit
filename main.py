class employee:
    def __init__(self):
        self.name = "sishva"
        self.age = 25
        self.salary = 20000
        self.designation = "engineer"
        self.place = "vijayawada"
    def display(self,salary):
        if(salary==20000):
            print("the employee is sishva")
        elif(salary>20000):
            print("the employee is kiran")
        else:
            print("the employee is sai")
employeeobj=employee()
employeeobj.display(25000)






