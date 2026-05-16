# basicSalary = 20000

# so we have to calculate the 
# HRA of basicSalary = 20%
# TA of ____________ = 30%
# DA of basicSalary  = 45%

# def calSal(base):
#     HRA = base * (2/5)
#     TA = base * (30/100)
#     DA =  base * (45/100)
#     return (base+HRA+TA+DA)

# result = calSal(float(input("Enter your salary")))
# print(result)

#--------------------------------------------------------------------------------------

x = [8,7,6,7,9,3,0,7,5,4]
count =0
print ("length of array", len(x))
new = []
for i in range (len(x)):
    if i in range (len(new)):
        print ("new array", new[i] )
        break

    for j in range (i+1,len(x)):
        if x[i] == x[j]:
            print ("x is ",x[i], "and y is ", x[j] )
            print ("checked array",new)
            count+=1
            # break
            new = [x[i]]

print ("count is ", count)


# add student
# show student
# update student
# delete student
# exit

# add
# id, roll no, name, city

