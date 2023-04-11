from twilio.rest import Client
import smtplib, sys

class NotificationManager:

    def __init__(self, sid, token, message_from, message_to, my_email):
        self.sid = sid
        self.token = token
        self.from_num = message_from
        self.to_num = message_to
        self.client = Client(self.sid, self.token)
        self.my_email = my_email

    def send_message(self, cheapest, from_airport, to_airport, date_from, date_to, stop_over, via_city):
        if stop_over != 0:
            body = f"Low price alert! Only ${cheapest} to fly from {from_airport} to {to_airport}, "
            f"from {date_from} to {date_to}.\n\nFlight has {stop_over}, via {via_city}"
        else:
            body = f"Low price alert! Only ${cheapest} to fly from {from_airport} to {to_airport}, "
            f"from {date_from} to {date_to}."

        self.client.messages.create(
            body= body,
            from_=self.from_num,
            to=self.to_num,
        )

    def send_email(self, password,cheapest, from_airport, to_airport, date_from, date_to, stop_over, via_city):
        if stop_over != 0:
            body = f"Low price alert! Only ${cheapest} to fly from {from_airport} to {to_airport} from {date_from} to {date_to}.\nFlight has {stop_over} stop over, via {via_city}."
            body = body.encode('ascii', 'ignore').decode('ascii')
        else:
            body = f"Low price alert! Only ${cheapest} to fly from {from_airport} to {to_airport} from {date_from} to {date_to}."
            body = body.encode('ascii', 'ignore').decode('ascii')

        LINK = f"https://www.google.co.uk/flights?hl=en#flt={from_airport}.{to_airport}.{date_from}*{to_airport}.{from_airport}.{date_to}"

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=self.my_email, password=password)
            connection.sendmail(from_addr=self.my_email, to_addrs=self.my_email,
                                msg=f"Subject:New Flight Deals!\n\n {body}\nBook from here: {LINK}")

