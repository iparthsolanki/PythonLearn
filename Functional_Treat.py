print("Welcome to the Data Analyzer and Transformer Program\n")
print("Main Menu: ")
print("1.Input Data")
print("2.Display Data Sammary (Built in function)")
print("3.Calculate Factorial (Recursion)")
print("4.Filter Data by Threshold (Lambda Function)")
print("5.Sort Data")
print("6.Display Dataset Statstics (Return Multiple Values)")
print("7.Exit Program\n")
one_D = []
two_D = []
c = 0

while True:
    a = int(input("\nplease enter your choice: "))
    def choice(n):
        global one_D,two_D,c
        if(n==1):
            c = int(input("what you want 1D(1) or 2D(2) : "))
            if(c==1):
                print("Enter data for a 1D Array:")
                size = int(input("Enter 1D array size: "))
                
                for i in range(size):
                    element = int(input())
                    one_D.append(element)
                print(one_D)
                print("Data has been Stored Successfuly!")
                
            elif(c==2):
                print("Enter Data for a 2D Array :")
                row = int(input("Enter 2D Array row: "))
                collum = int(input("Enter 2D Array collum: "))
                for i in range(row):
                    row_data = []   
                    for j in range(collum):
                        Element = int(input(f"Element[{i}][{j}]"))
                        row_data.append(Element)
                    two_D.append(row_data)
                    print("2D Array is:") 
                for r in two_D:
                    print(r)
                print("Data has been Stored Successfuly!")
                
        elif(n==2):
            if c==1:
                total = len(one_D)
                print("Data Summary:")
                print(f"Total Elements: {total}")
                smallest = min(one_D)
                print(f"Minimum Value: {smallest}")
                large = max(one_D)
                print(f"Maximum Value: {large}")
                summ = sum(one_D)
                print(f"Sum of all Elements {summ}")
                average = summ/len(one_D)
                print(f"Average Value: {average}")
                
            elif(c==2):
                print("Data sammary of 2D Array:")
                t_e = 0
                s_e = 0
                small = 0
                large = 0
                
                for r in two_D:
                    for t in r:
                        t_e+=1
                        s_e+=t
                        if(small is 0 or t<small):
                            small = t
                        if(large is 0 or t>large):
                            large = t
                        ave = s_e/t_e
                print(f"Total Elements: {t_e}")
                print(f"Minimum value: {small}")
                print(f"Meximum Value {large}")
                print(f"Sum of all Values: {s_e}")
                print(f"Average Value: {ave}")
                
        elif(n==3):
            print("1.Factorial")
            print("2.Fibbonacci")
            z = int(input())
            if(z==1):
                F = int(input("Enter a number to calculate its factorial: "))
                def factorial(w):
                    if(w==1 or w==0):
                        return 1
                    else:
                        return w*(factorial(w-1))
                
                result = factorial(F)
                print(result)
            elif(z==2):
                F = int(input("Enter number to calculate its fibbinacci: "))
                def fibonacci(n):
                    if n == 0:
                        return 0  # base case 1
                    elif n == 1:
                        return 1 
                    else:
                        return fibonacci(n-1) + fibonacci(n-2) 

                for i in range(F):
                    print(fibonacci(i), end=' ')
                              
                             
        elif(n==4):
            if(c==1):
                f = int(input("Enter a threshold value to filter out data above this value: "))
                s = list(filter(lambda x : x > f,one_D))
                print(f"Filtered Data (Value >= {f}):")
                print(s)
                
            elif(c==2):
                sett=[]
                f = int(input("Enter a threshold value to filter out data above this value: "))
                for i in two_D:
                    for j in i:
                        sett.append(j)
                        s = list(filter(lambda x : x > f , sett ))
                print(f"Filtered Data (Value >= {f}):")
                print(s)
                
        elif(n==5):
             print("Choose Sorting Option: ")
             print("1.Ascending")
             print("2.Descending")
             if(c==1):
                o = int(input())
                if(o==1):
                    x = one_D.sort()
                    print(one_D) 
                elif(o==2):
                    y = one_D.sort(reverse=True)
                    print(one_D)  
             elif(c==2):
                 add = []
                 for i in two_D:
                     for j in i:
                         add.append(j)
                 p = int(input())
                 if(p==1):
                     x = add.sort()
                     print(add)
                 elif(p==2):
                    y = add.sort(reverse=True)
                    print(add)
                    
        elif(n==6):
            print("Dataset Statistics: ")
            if(c==1):
                mn = min(one_D)
                mx = max(one_D)
                sm = sum(one_D)
                ave = sm/len(one_D)
                print(f"Minimum Value: {mn}")
                print(f"Meximum Value: {mx}")
                print(f"Sum of all Value: {sm}")
                print(f"Average Value: {ave}")
            elif(c==2):
                one = []
            
                for i in two_D:
                    for j in i:
                        one.append(j)
                mn = min(one)
                mx = max(one)
                sm = sum(one)
                ave = sm/len(one)
                print(f"Minimum Value: {mn}")
                print(f"Meximum Value: {mx}")
                print(f"Sum of all Value: {sm}")
                print(f"Average Value: {ave}")
                
        elif(n==7):
            print("Thankyou for using Data Analyzer and Transform Programe. Good by !")
            exit()                             
    choice(a)