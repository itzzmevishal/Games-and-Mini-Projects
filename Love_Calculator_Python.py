# Hint
import random
# The lower() function changes all the letters in a string to lowercase.
# The count() function will give you the number of times a letter occurs in a string.


# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
score = random.randint(1,100)
if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >40 and score <50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")

