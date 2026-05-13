# mylist = ["nihar", "sumaiya", "suma", "jayanth kumar", "sumanth kumar reddy","777","sandip",60.52, "nihar"]

# print(mylist)
# print(type(mylist)) #<class 'list'>
# print(mylist[0]) #nihar
# print(mylist[1]) #sumaiya
# print(mylist[2]) #suma
# print(mylist[-1]) #nihar
# print(mylist[2:5]) # n=5, n-1=4, 2,3,4 #['suma', 'jayanth kumar', 'sumanth kumar reddy']
# print(mylist[:5]) # n=5, n-1=4, 0,1,2,3,4 #['nihar', 'sumaiya', 'suma', 'jayanth kumar', 'sumanth kumar reddy']
# print(mylist[1:5]) # n=8, n-1=8-1

# mylist[2] = "Akshay"
# print(mylist)

# if "nihar" in mylist:
#     print("nihar is present in the list")
# else:
#     print("nihar is not present in the list")

# mylist.append("harsh")
# mylist.append("RAM")
# print(mylist)
# #append and extend both work like same;

# mylist.insert(3, "jay")
# print(mylist)

# newlist = mylist.copy()
# print(newlist,"New List")

# mylist = [['nihar','dongre'],[87.99],[87679,'yyy']]
# print("examples of nested list:")
# print(mylist)
# # print(mylist[row][column]) 
# print(mylist[0][0]) #nihar
# print(mylist[0][1]) #dongre
# print(mylist[1][0]) #87.99
# print(mylist[2][0]) #87679
# print(mylist[2][1]) #yyy

#----------------------------------------------------
# [[      0         1
#  0 = 'nihar', 'dongre'],
#  1 = [87.99],
#  2 = [87679, 'yyy']]

# list2 = [1, 2]
# #del list2[2]
# del list2
# print(list2)

# list1 = [1, 'saif']
# list1.clear()
# print(list1)




# mylist = [10, 56, 36, 22, 44]
# #mylist.sort()
# mylist.sort(reverse=True)
# print(mylist)
#default sort order for number is ascending
# default sort order for string is alphabetical order
# we should know that list should contain homogeneous data to sort the list otherwise it will give error.
# python2 first short number then string follow    

#-----------------------------------------------------------------------------------------------------------------
# Alising
# alising is a process of creating a new reference to the same object in memory.
# mylist = [10, 56, 36, 22, 44]
# newlist = mylist
# print(id(mylist)) 
# print(id(newlist))

# inp = [0,1,4,0,5,2]



input_list = [7,3,9,2,8]

input_list.sort(reverse=True)
print(input_list[1])