menu = {                                                
    'pizza' : 150,
    'burger' :70,
    'vadapau' : 30,
    'sendwich' : 100,
    'lawacake' : 80,
}                                                       
print("Welcome Python Cafe")
print(" (1) pizza : rs150 \n (2) burger : rs70 \n (3) vadapau : rs30 \n (4) sendwich : rs100 \n (5) lawacake : rs80")
total_order = 0
order_1 = input("Enter your order : ")
if order_1 in menu:
    total_order += menu[order_1]
    print(f"your order {order_1} has been added ")
else:
    print(f"your order {order_1} is not avelable")

another_order = input("Do you want another order? (yes/no)")
if another_order == "yes":
    order_2 = input("Enter your second order : ")
    if order_2 in menu:
        total_order += menu[order_2]
        print(f"your order {order_2} has been added")
    else:
        print(f"your order {order_2} has been not avelable")

print(f"the pay to bill is {total_order}")
