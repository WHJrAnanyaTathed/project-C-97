import random

random_number=random.randint(1,9)

chances =0
while chances < 5:
    guess_number = int(input("Please guess the number between 1 and 9 : "))
    if(guess_number == random_number):
        print("Congragulation YOU WON!")
        break
    elif(random_number < guess_number):
        print("The number is smaller than your guess", guess_number)
    else:
        print("The number is grater than your guess", guess_number)
    
    chances += 1

    if not chances < 5:
        print("YOU LOSE!!! The number was ", random_number)