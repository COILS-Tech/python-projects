print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    print("Looks like you don't want to play. That's okay.")
    quit()

print("Okay! Let's play :)")
score = 0
# Question 1
answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    score += 0

# Question 2
answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    score += 0

# Question 3
answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    score += 0

# Question 4
answer = input("What does SSD stand for? ")
if answer.lower() == "solid state drive":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    score += 0

# Question 5
answer = input("What does ADLS stand for? ")
if answer.lower() == "azure data lake storage":
    print("Correct!")
    print(f"You got {score} questions right! See you next time!")
    print(f"Total Score: {score * 20}% :)!")
else:
    print("Incorrect!")
    score += 0
    print(f"Total Score: {score * 20}% of perfect score:)!")