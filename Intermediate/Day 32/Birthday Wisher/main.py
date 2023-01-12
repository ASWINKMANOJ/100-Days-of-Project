import datetime as dt
import pandas
import random
import smtplib

today = dt.datetime.now()
today_tuple = (today.month, today.day)

birthday_details = pandas.read_csv("birthdaydetails.csv")
birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in birthday_details.iterrows()}

if today_tuple in birthday_dict:
    person = birthday_dict[today_tuple]
    random_number = random.randint(1, 2)
    files = f"./wishes/letter_{random_number}.txt"
    with open(files) as data_file:
        wish = data_file.read()
        text = wish.replace("[NAME]", person["name"])
    my_email = "projectday32@gmail.com"
    my_password = "lvrfucjyiojwaylo"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs=person["email"], msg=f"Subject:HAPPY BIRTHDAY\n\n{text}")

