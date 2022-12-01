print("Welcome to the Love Calculator")
name1 = input("What is your Name?\n").lower()
name2 = input("What is His/Her Name?\n").lower()

combine_name = name2 + name1

t = combine_name.count("t")
r = combine_name.count("r")
u = combine_name.count("u")
e = combine_name.count("e")

L = combine_name.count("l")
O = combine_name.count("o")
V = combine_name.count("v")
E = combine_name.count("e")

first_digit = str(t + r + u + e)
second_digit = str(L + O + V + E)
combine_digit = (first_digit + second_digit)
new_combine = int(combine_digit)

if (new_combine < 10) or (new_combine > 90):
    print(f"Your Score is {combine_digit}, you go together like coke and mentos.")
elif (new_combine >= 40) and (new_combine <= 50):
    print(f"Your Score is {combine_digit}, you are alright together.")
else:
    print(f"Your Score is {combine_digit}")

close = input("Press Any Key to Close the Program.")