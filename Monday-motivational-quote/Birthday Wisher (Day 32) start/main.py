#import smtplib
#
#my_email = "i69265264@gmail.com"
#password = "qrqihghowtminnmn"
#
#
#with smtplib.SMTP("smtp.gmail.com") as connection:
#    connection.starttls()
#
#    connection.login(user=my_email, password=password)
#    connection.sendmail(from_addr=my_email, to_addrs="hiromi.thomas@yahoo.com",
#                        msg="Subject:Hello\n\nThis is the body of my email.")
#
##
#import datetime as dt
#
#now = dt.datetime.now()
#year = now.year
#day_of_week = now.weekday()
#print(day_of_week)
#
#date_of_birth = dt.datetime(year= 1987, month=12 , day=3, hour=5 )
#print(date_of_birth)

#-----------Monday Quote--------------------------------#
import smtplib
import datetime as dt
import random

with open("quotes.txt") as file:
    quote_list = file.readlines()

now = dt.datetime.now()
day_of_week = now.weekday()
if day_of_week == 3:

    with smtplib.SMTP("smtp.gmail.com") as connection:
        my_email = "i69265264@gmail.com"
        password = "apvfimpalknkcobu"
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="hiromi.thomas@yahoo.com",
                            msg=f"Subject:It's Monday!\n\n{random.choice(quote_list)}")