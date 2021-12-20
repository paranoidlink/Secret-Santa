import random

list1 = []
list2 = []
usrInput = ""
print("Type the names of everyone taking part, type run to run the program once ready:")
while usrInput != "run":
    usrInput = str(input())
    if usrInput == "run":
        break
    list1.append(usrInput)
    list2.append(usrInput)

while len(list1) > 0:
    choice1 = list1[random.randint(0,len(list1)) - 1]
    choice2 = list2[random.randint(0,len(list2)) - 1]

    if choice1 == choice2:
        continue
    else:
        print(choice1 + " Has to give a present to " + choice2)
        list1.remove(choice1)
        list2.remove(choice2)
exit()
