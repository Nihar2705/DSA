mydict = {
    101: "nihar",
    102: "jay",
    "103":"mohit",
    104:"trivani",
    101:"ashish",
    104:"ashish"
}
print(mydict)

# a= mydict[102]
# print(a)

# mydict[102] = "peter"
# print(mydict)

# #only print keys
# for x in mydict:
#     print(x)

# #only print values
# for x in mydict.values():
#     print(x)

# for x,y in mydict.items():
#     print(x,y)


# #adding a new key and value pair
# mydict["mobile_no"]=9868658909
# print(mydict)

# mydict.pop(101)
# print(mydict)
#pop method removes pair by specific key name

rec = {"Name" : "Python", "Age": "20"}
r = rec.copy()
print(id(r) == id(rec))
print(id(r))
print(id(rec))