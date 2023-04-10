import random

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

score = random.randint(1,100)
if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >40 and score <50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")

