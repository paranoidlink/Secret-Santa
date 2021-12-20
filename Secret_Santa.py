import random

list1 = ["Ben", "Jay", "Mike", "Meg", "Brooke", "Oscar", "Levi"]
list2 = ["Ben", "Jay", "Mike", "Meg", "Brooke", "Oscar", "Levi"]

while len(list1) > 0:
    choice1 = list1[random.randint(0,len(list1)) - 1]
    choice2 = list2[random.randint(0,len(list2)) - 1]

    if choice1 == choice2:
        continue
    else:
        print(choice1 + " Has to give a present to " + choice2)
        list1.remove(choice1)
        list2.remove(choice2)
