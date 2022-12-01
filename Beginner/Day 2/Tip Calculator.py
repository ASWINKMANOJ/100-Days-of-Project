print("Welcome to the tip calculator.")
bill = (float(input("What was the total bill? $")))
pers = (float(input("What percentage tip would you like give? 10, 12, or 15? ")))
num = (int(input("How many people to Split the bill? ")))
tip = (bill*pers)/100 + bill
tip_per = "{:.2f}".format((tip/num))
print(f"Each person should pay : ${tip_per}")

close = input("Press Any Key to Close the Program.")