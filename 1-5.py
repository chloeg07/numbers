import random
a = random.randint(1,5)
userchoice = int(input("Choose a number between 1 and 5.........."))
if userchoice == a:
    print("you guessed right")
else:
    if userchoice < a:
         print("your guess is too low")
    else:
         print("your guess is too high")
userchoice2 = int(input("choose another number between 1 and 5.........."))
if userchoice2 == a:
         print("you guessed right")
else:
    if userchoice2 < a:
        print("you lose")
                  