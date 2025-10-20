print("---Python OOP Project: Employee Management System---\n")
print("Choose an Operation")     

class Person:
    def __init__(self, Name, Age):
        self.Name = Name
        self.Age = Age

class Employee(Person):
    def __init__(self, Name, Age, Employe_Id, Salary):
        super().__init__(Name, Age)
        self.Employe_Id = Employe_Id
        self.Salary = Salary
       
class ManAger(Employee):
    def __init__(self, Name, Age, Employe_Id, Salary, Department):
        super().__init__(Name, Age, Employe_Id, Salary)
        self.Department = Department

# Initialize all as None
one = None
Two = None
Three = None

while True:       
    print("Choose another Operation")  
    print("1. Create a Person")
    print("2. Create an Employee")
    print("3. Create a Manager")
    print("4. Show Details")
    print("5. Exit")
    choice = int(input("\nEnter Your Choice: "))
    
    if choice == 1:
        n = input("\nEnter Name: ")
        a = int(input("Enter Age: "))
        one = Person(n, a)
        print(f"\nPerson Created With Name: {one.Name} and Age: {one.Age}\n")
            
    elif choice == 2:
        n = input("Enter Name: ")
        a = int(input("Enter Age: "))
        i = int(input("Enter Employee ID: "))
        s = int(input("Enter Salary: "))
        Two = Employee(n, a, i, s)
        print(f"Employee Created With Name: {Two.Name}, Age:{Two.Age}, ID:{Two.Employe_Id} and Salary:{Two.Salary}\n")
     
    elif choice == 3:
        n = input("Enter Name: ")
        a = int(input("Enter Age: "))
        i = int(input("Enter Employee ID: "))
        s = int(input("Enter Salary: "))
        d = input("Enter Department: ")
        Three = ManAger(n, a, i, s, d)
        print(f"Manager Created with Name: {Three.Name}, Age:{Three.Age}, ID:{Three.Employe_Id}, Salary:{Three.Salary}, Department:{Three.Department}\n")
        
        
    elif choice == 4:
        print("Choose Details to Show: ")
        print("1. Person")
        print("2. Employee")
        print("3. Manager")
        choice2 = int(input("Enter Your Choice: "))
            
        if choice2 == 1:
        
            print("\n--- Person Details ---")
            print(f"Name: {one.Name}")
            print(f"Age: {one.Age}\n")


        elif choice2 == 2:

            print("\n--- Employee Details ---")
            print(f"Name: {Two.Name}")
            print(f"Age: {Two.Age}")
            print(f"Employee ID: {Two.Employe_Id}")          
            print(f"Salary: {Two.Salary}\n")


        elif choice2 == 3:
            
            print("\n--- Manager Details ---")
            print(f"Name: {Three.Name}")
            print(f"Age: {Three.Age}")
            print(f"Employee ID: {Three.Employe_Id}")          
            print(f"Salary: {Three.Salary}")
            print(f"Department: {Three.Department}\n")
    
    elif choice == 5:
        print("Exiting the system . All resorurces have been freed.\n")
        print("Good Bye")
        break

