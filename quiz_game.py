print("Welcome to Robbie's IT quiz!!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    print("Sorry to see you leave, Have a great day :)")
    quit()

print("Okay let's play :) ")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!!")
    score += 1
else:
    print("I'm sorry this answer is incorrect. Please try again :( ")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!!")
    score += 1
else:
    print("I'm sorry this answer is incorrect. Please try again :( ")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!!")
    score += 1
else:
    print("I'm sorry this answer is incorrect. Please try again :( ")

answer = input("What does SSD stand for? ")
if answer.lower() == "solid state drive":
    print("Correct!!")
    score += 1
else:
    print("I'm sorry this answer is incorrect. Please try again :( ")

print("You have got " + str(score) +" questions correct!!")
print("You have got " + str((score / 4) * 100) +"%.")
