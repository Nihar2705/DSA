# data structures are different ways of organizing data on your computer, 
#   that can be used effectively.

#The aspects that matters in an algorithm
# 1. correctness
# 2. effectiveness

# def findBiggestNumber(sampleArray):
#     biggestNumber = sampleArray[0]
#     for index in range(1, len(sampleArray)):
#         if sampleArray[index]>biggestNumber:
#             biggestNumber = sampleArray[index]
#     print(biggestNumber)

# sampleArray = [5,7,9,2,3,4]
# findBiggestNumber(sampleArray)

#--------------------------------------------------------------------------------------
# def linearSearch(array, target):
#      for i in range(0, len(array)):
#           if array[i] == target:
#                return i
          
# array = [1,2,3,4,8,6,7]
# target = 7 
# linearSearch(array, target)

#--------------------------------------------------------------------------------------

# def linearSearch(array, target):
#     for i in range(0, len(array)):
#         if array[i] == target:
#             return i
#     return -1
    
          
# array = [1,2,3,4,8,6,7]
# target = 7 
# result = linearSearch(array, target)

# if result == -1:
#     print("The searched value is not present in the array")
# else:
#     print("The target was found at index - ",result)


#Removing spcaes from the string:
#1. rstrip() --> To remove spaces at right hand side
#2. lstrip() --> To remove spaces at left hand side
#3. strip() --> To remove spaces on both sides

# city = input("Enter your city name")
# scity=city.strip()
# if scity =='Hyedrabad':
#     print("Hyedrabad, Aadab")
# elif scity =='Chennai':
#     print("Chennai Vanakkam")
# elif scity =='Bangalore':
#     print("Bangalore, Shubhodhaya")
# else:
#     print("your entered city is invalid")

#--------------------------------------------------------------------------------------

#Row wise max value

# Q. find row wise max value
# row = [[100,198,333,323],
#  [122,232,221,111],
#  [223,565,245,764]]

# newlist=[]
# for i in range(3):
#     j =0 
#     max = row[i][j]
#     for j in range(4):
#         c_max = row[i][j]
#         if max < c_max:
#             max = c_max
#     newlist.append(max)
# print(newlist)

#--------------------------------------------------------------------------------------

name = "nihar*is*a*Good*Programmer"
newname = '' 
val = '' 
for i in name:
    if i !='*':
        newname += i
    else:
        val+=i
print(newname)
print(str(val+newname))

#--------------------------------------------------------------------------------------

