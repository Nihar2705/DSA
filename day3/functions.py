import sys
# def arithmatic():
#     a = int(input("Enter value of a:"))
#     b = int(input("Enter value of b:"))
#     sum = a +b
#     sub = a -b
#     multi = a * b
#     div = a/b
#     return sum, sub, multi, div
# R = arithmatic()
# print(R)

# How many types of arguements we pass in a function
# 1. positional argument
# 2. keyword argument
# 3. default argument
# 4. variable length arguments / variable number of arguments

#--------------------------------------------------------------------------------------

# def arithmatic(a,b):
#     sum = a +b
#     sub = a -b
#     multi = a * b
#     div = a/b
#     return sum, sub, multi, div
# #postional argument
# result = arithmatic(5,5)
# print("Arithmatic = ", result)

#--------------------------------------------------------------------------------------

# def credential(username,password):
#     if username == password:
#         print("login successful")
#     else:
#         print("lofin failed")

# credential(username="admin", password="admin") #calling function

#--------------------------------------------------------------------------------------

#default argument
# def cityName(city="Pune"):
#     print(city)
# cityName("Nagpur")
# cityName("Balaghat")    
# cityName()

#--------------------------------------------------------------------------------------

# 4. variable length arguments / variable number of arguments

# def cityName (*name):
#     print(name)

# cityName("Nagpur","delhi","Bomb","Muju")

#--------------------------------------------------------------------------------------
def add():
    a = int(input("Enter value of a:"))
    b = int(input("Enter value of b:"))
    print(a+b)
def sub():
    a = int(input("Enter value of a:"))
    b = int(input("Enter value of b:"))
    print(a-b)
def div():
    a = int(input("Enter value of a:"))
    b = int(input("Enter value of b:"))
    print(a/b)
def mul():
    a = int(input("Enter value of a:"))
    b = int(input("Enter value of b:"))
    print(a*b)

while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Division")
    print("4. Multiplication")
    print("5. Exit")
    choice = int(input("Enter your choice:"))
    if choice == 1:
        add() #calling function    
    elif choice ==2:
        sub()
    elif choice ==3:
        div()
    elif choice ==4:
        mul()
    elif choice == 5:
        sys.exit()