#simple tool for understanding the working of a dice
import random
print("a simple app for rolling a dice")


def roll(num=1):
    x = random.randint(1, 6)
    print(x)


app = True
while app:
    user = input("press r to roll the dice ")
    if user == "r":
        print("rolling the dice")
        roll()
    else:
        app = False
print("closing the application cuz you didnt entered r ")
cancel = input("pres enter to close the program")
