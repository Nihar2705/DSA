# #increment error
# a=[1,2,3,4,5,6,7,8,9]
# a[::2] =  10,20,30,40,50,60 # since the sixth index is empty it will give error because we are trying to assign value to empty index which is not possible.
# print(a)


# arr = [[1,2,3,4],
#        [4,5,6,7],
#        [8,9,10,11],
#        [12,13,14,15]]
# for i in range(0,4): #i=4 #only focussed on your row's
#     print(arr[i], end = "") #arr[0][0] #1

# arr = [1,2,3,4,5,6]
# for i in range(1,6):
#     arr[i-1] = arr[i]

# for i in range(0,6):
#     print(arr[i], end = " ")

fruit_list1 = ["apple", "berry", "cherry", "papaya"]
fruit_list2 = fruit_list1
fruit_list3 = fruit_list1[:]
fruit_list2[0] = "guava"
fruit_list3[1] = "kiwi"

sum = 0
for ls in (fruit_list1, fruit_list2, fruit_list3):
    if ls[0] == "guava":
        sum += 1
    if ls[1] == "kiwi":
        sum += 20
print(sum)