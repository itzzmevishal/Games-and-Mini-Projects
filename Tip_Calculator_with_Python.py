# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Write your code below this line 👇

# ANSWER👇👇👇👇👇👇👇

print("Welcome to the tip calculator: ")
bill = float(input("What is the total bill? "))
tip = float(input("What percent tip you want to give? 10% 12% 15% "))
people = int(input("In how many people you want to divide? "))

tip_per = tip / 100
total_tip = bill * tip_per
totle_bill = bill + total_tip
pay = totle_bill / people
# pay_final=round(pay,2)  #for rounding off we use this method (:-->round(veriable_name,digits after decimal))
# or for rounding off we can use (:.2f) after the veriable.
print(f" Each person should have to pay {pay:.2f}.")
