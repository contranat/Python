class Person:

    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last
    
    
    #changes operator overload for print    
    def __str__(self):
        return "First Name: " + self.firstname  +"\n" + "Last Name: " + self.lastname
        
    ##Add operator overload for print that prints
    ##First Name: firstname
    ##Last  Name: lastname


full_name = Person("Natalia", "Contreras")
print(f'EXERCISE 1: \n{full_name}')

#Make derived class "Employee" that inherits the base class Person
#In the constructor, grab all the Person methods using the super() method
#(1) Add a new variable to hold date of birth called "dob" to the __init__
#   Overload __str__ with super and add "\nDOB: " + str(self.dob)
#(2) Also add a new variable "ssn" to the __init__ to hold the social security number
#    Add a new method called get_ssn that returns the ssn

class Employee(Person):
    def __init__(self, first, last, dob, ssn):
        super().__init__(first, last)
        self.dob = dob
        self.ssn = ssn
        
    def __str__(self):
        return super().__str__() + "\nDOB:" + self.dob + "\nSSN:" + str(self.ssn)



if __name__=="__main__":
    employee_dets = Employee("Natalia", "Contreras", "08/24/1999", 000-000-0000)
    print(f'EXERCISE 2: \n{employee_dets}')
    
    
    ##Test situation
    boss = Person("Hamed", "Haq")
    empl = Employee("Ted", "McMaster", "03151970", 999999999)

    print(boss)
    print(empl)
    print("Employee SSN is:", empl.ssn)


