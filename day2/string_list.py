# # add a new character to the string if it is not already present in the string
# name = "chinnuswami"
# newname =""
# for i in name:
#     if i not in newname:
#         newname += i
# print(newname)

# # do the same thing just, reverse the string
# name = "chinnuswami"

# newname =""
# N = len(name)
# for i in range(N-1,-1,-1):
#     if name[i] not in newname:
#         newname += name[i]
# print(newname)

# palindrome sequenece

# name = "nihar"
# print(name)
# print(name[::-1])
# if name == name[::-1]:
#     print("palindrome")
# else:
#     print("not palindrome")

# check for anagrams

# word =input("Enter your string")
# vowels = ['a','e','i','o','u']
# count = 0
# vow = 0
# for i in word:
#     if i in vowels:
#        vow += 1
#     else:
#         count += 1
# print("vowels:", vow)
# print("consonants:", count)



# #string functions
# print('nihard984'.isalnum()) # True
# print('nihar'.isalpha()) # True
# print('nihar'.isdigit()) # False
# print('nihar'.islower()) # True
# print(''.islower()) # False
# print('NIHAR'.isupper()) # True
# print('My Name is Nihar'.istitle()) 
# print(''.istitle()) 
# print(' '.isspace()) 
# print('nihar'.startswith('nh')) 
# print('nihar'.endswith('umi'))

#-------------------------------------------------------------

# print("jay".find('y'))
# print("maahi".index('a  '))
# print("hritik".count('a'))

# import time
# n=int(input("Enter the number of rows: "))
# for i in range(1,n+1):
#     print(" "*(n-i),end = "")
#     for j in range(1,i+1):
#         time.sleep(3)
#         print("* ",end = "")
#     print()
    

# number = [1,2,3,4]
# for i in number:
#     for j in number:
#         if i == j:
#             continue
        
            