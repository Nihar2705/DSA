# questions

# def func(value, values):
#     var = 1
#     values[0]=44
# t =3 
# v=[1,2,3]
# func(t,v)
# print(t,v[0])

# A. 1 44
# B. 3 1
# C. 3 44
# D. 1 1

# def f(i, values = []):
#     values.append(i)
#     print(values)
#     #return values 
# f(1) #calling function
# f(2)
# f(3)

# A. [1] [2] [3]
# B. [1,2,3]
# C. [1] [1,2] [1,2,3]
# D. 1 2 3


# fruit = {}
# def addone(index):
#     if index in fruit:
#         fruit[index] += 1
#     else:
#         fruit[index] = 1

# addone('Apple')
# addone('Banana')
# addone('apple')
# print(len(fruit))

# A. 1
# B. 2
# C. 3
# D. 4


# Write a program to accept student name and marks from the keyboard and creates a dictionary.
# Also display student marks by taking student name

n = int(input("enter the number of students: "))
d ={}
for i in range(n):
    name = input("Enter Student Name:")
    marks = input("Enter student makrs:")
    d[name] = marks # add key:value
while True:
    name = input ("Enter student name to find marks")
    marks = d.get(name,-1)
    if marks == -1:
        print("Student not found")
    else:
        print("The marks of ",name,"are",marks)
    option = input("Do you want to find another student marks[Yes|No]")
    if option == "No":
        break

print ("Thanks for using the application")