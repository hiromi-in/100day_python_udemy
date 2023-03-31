##################### Extra Hard Starting Project ######################
import pandas, smtplib, random
import datetime as dt

# 1. Update the birthdays.csv
birthday_data = pandas.read_csv("birthdays.csv")
month_list = birthday_data['month'].tolist()
day_list = birthday_data['day'].tolist()

birthday_tuples = []

for i in range(len(month_list)):
    birthday_tuples.append((month_list[i], day_list[i]))

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
month = now.month
day = now.day
now_tuple = (month, day)

# 3. If step 2 is true, pick a random letter from letter
# templates and replace the [NAME] with the person's actual name from birthdays.csv

PLACE_HOLDER = "[NAME]"

if now_tuple in birthday_tuples:
    name_index = birthday_tuples.index(now_tuple)
    name = birthday_data.at[name_index, 'name']
    TO_EMAIL = birthday_data.at[name_index, 'email']

    with open(f"letter_templates/letter_{random.randint(1,3)}.txt", ) as letter:
       draft = letter.read()
       new_letter = draft.replace(PLACE_HOLDER, name)
# 4. Send the letter generated in step 3 to that person's email address.
    with smtplib.SMTP("smtp.gmail.com") as connection:
        MY_EMAIL = "XXX@gmail.com"
        PASSWORD = "XXX"
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=TO_EMAIL, msg=f"Subject:Happy Birthday!\n\n{new_letter}")




