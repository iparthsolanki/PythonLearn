print("Welcome to the Student Data Organizer!")
students = []  

while True:
    print("\nSelect an option:")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display All Subjects")
    print("6. Exit")

    Choice = int(input("Enter your Choice: "))

    if Choice == 1:
    
        Name = input("Enter Name: ")
        Age = int(input("Enter Age: "))
        Grade = input("Enter Grade: ")
        Subjects = set(input("Enter Subjects (comma separated): ").split(","))
        ID = int(input("Enter student ID: "))
        dob = input("Enter date of birth (dd-mm-yyyy): ")

        Tuple = (ID, dob) 
        student = {
            "Tuple": Tuple,
            "Name": Name,
            "Age": Age,
            "Grade": Grade,
            "Subjects": Subjects
        }
        students.append(student)
        print(" Student added successfully!")

    elif Choice == 2:
        print("\n--- All Student Records ---")
        if not students:
            print("No student records found.")
        else:
            for s in students:
                print(f"ID: {s['Tuple'][0]}, Name: {s['Name']}, Age: {s['Age']}, Grade: {s['Grade']}")
                print(f"Subjects: {', '.join(s['Subjects'])}, Date of Birth: {s['Tuple'][1]}")
                print("--------------------------------------------------")

    elif Choice == 3:
        a = int(input("Enter Student ID to update: "))
        for i in students:
            if i ["Tuple"][0] == a:
                i["Age"] = int(input("Enter New Age: "))
                i["Subjects"] = set(input("Enter New Subjects (comma Saprated): ").split(","))
                print("Student Information Updated")  
                break
            else:
                print("Student not Found") 
    
    elif Choice == 4:
        id = int(input("Enter Student ID to delete : "))      
        for i in range(len(students)):
            if students[i]["Tuple"][0] == id:
                del students[i]
                print("Delete Student Successfuly !")
                break
            else:
                print("Student ID not Found...")
                
    elif Choice == 5:
        All_sub = set()
        for j in students:
            All_sub.update(j["Subjects"])
            print("Unique subject offered:\n")
            print(",".join(All_sub))
            break
                 
    elif Choice == 6:
        print("Thank you for using the Student Data Organizer!")
        break

    else:
        print(" Invalid Choice! Please try again.")
