import smtplib
import datetime as dt
import random

with open("quotes.txt", "r") as file:
    quotes = file.readlines()

quote_today = random.choice(quotes).strip("\n")

my_email = "projectday32@gmail.com"
my_password = "haptuhzlomyddunu"

current = dt.datetime.now()
current_weekday = current.weekday()

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    if current_weekday == 2:
        connection.sendmail(from_addr=my_email, to_addrs="achooaswinjr@gmail.com", msg=f"Subject:Quote "
                                                                                       f"Today\n\n{quote_today}")
