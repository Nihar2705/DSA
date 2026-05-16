# mycart =[10,20,30,40]
# for item in mycart:
#     if item>400:
#         print("This is not in my budget")
#         continue
#     print(item)
# else:
#     print("you have purchased everything")

#----------------------------------------------------------------------------

#Tower of hanoi
import time
class Tower:
    def __init__(self):
        print("Welcome to tower of hanoi game")
        print()
        print("given problem   A=[3,2,1]        B=[]        C=[]        ")
        print()
        print("Expected Output A=[]")

    def pass3(self):
        self.temp = self.C.pop(0)
        self.B.append(self.temp)
        time.sleep(3)
        print("A=",self.A, "            ",      )