from random import *

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number larger than 0 next time.")
        quit()
else:    
    print("You were asked to type a number :( \nPlease enter a number next time.")
    quit() 
    
random_number = randint(0, top_of_range)
# Print the random number
#print(random_number)

# Guesses from user
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time.")
        continue

    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
        print("Guess lower!")
    else:
        print("Guess higher!")
print(f"You got it in {guesses} guesses!")