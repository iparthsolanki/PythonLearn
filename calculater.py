print("WELCOME MY CALCULATER")

def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mult(x,y):
    return x*y

def divede(x,y):
    return x/y

print("select opration : ")
print("1 = addition")
print("2 = subtraction")
print("3 = multiplication")
print("4 = divition")

choice = int(input("enter what you want :  "))

n1 = int(input("enter frist number : "))

n2 = int(input("enter second number : "))



if choice == 1:
    print("result:" , add(n1,n2))

elif choice == 2:
    print("result:" , sub(n1,n2))

elif choice == 3:
    print("result:" , mult(n1,n2))

elif choice == 4:
    print("result:" , divede(n1,n2))

else:
    print("invalid input")
