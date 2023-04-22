print("Welcome to the tip calculator: ")
bill = float(input("What is the total bill? "))
tip = float(input("What percent tip you want to give? 10% 12% 15% "))
people = int(input("In how many people you want to divide? "))

tip_per = tip / 100
total_tip = bill * tip_per
totle_bill = bill + total_tip
pay = totle_bill / people

print(f" Each person should have to pay {pay:.2f}.")
