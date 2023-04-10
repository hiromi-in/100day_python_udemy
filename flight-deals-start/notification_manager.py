from twilio.rest import Client

class NotificationManager:

    def __init__(self, sid, token, message_from, message_to):
        self.sid = sid
        self.token = token
        self.from_num = message_from
        self.to_num = message_to
        self.client = Client(self.sid, self.token)

    def send_message(self, cheapest, from_airport, to_airport, date_from, date_to):
            self.client.messages.create(
            body=f"Low price alert! Only ${cheapest} to fly from {from_airport} to {to_airport}, "
                 f"from {date_from} to {date_to}.",
                from_=self.from_num,
                to=self.to_num,
        )
