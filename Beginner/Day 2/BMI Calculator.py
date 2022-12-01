height = input("Type your Height in m:")
weight = input("Type your Weight in kg:")
# Don't Change the Code above
new_height = float(height)
new_weight = float(weight)
BMI = new_weight/new_height**2
new_BMI = round(BMI, 2)
new_BMI_2 = str(new_BMI)
print("BMI :"+new_BMI_2)

close = input("Press Any Key to Close the Program.")