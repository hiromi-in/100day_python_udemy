import requests, datetime, os
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
CORE_STOCK_API_KEY = os.environ.get(STOCK_EPIKEY)
NEWS_API_KEY = os.environ.get(NEWS_API_KEY)
account_sid = os.environ.get(ACCOUNT_SID)
auth_token = os.environ.get(AUTH_TOKEN)

STOCK_END_POINT = "https://www.alphavantage.co/query"
NEWS_ENDPONT = "https://newsapi.org/v2/everything"

yesterday = (datetime.date.today() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
the_day_before_yesterday = (datetime.date.today() - datetime.timedelta(days=2)).strftime('%Y-%m-%d')

stock_params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey":CORE_STOCK_API_KEY
}
param_for_news = {
    "q": COMPANY_NAME,
    "from": yesterday,
    "sortBy": "popularity",
    "apiKey": NEWS_API_KEY,
}

response = requests.get(STOCK_END_POINT, params=stock_params)
data = response.json()


data_to_compare = {
    "Yesterday": float(data["Time Series (Daily)"][yesterday]["4. close"]),
    "The day before": float(data["Time Series (Daily)"][the_day_before_yesterday]["4. close"]),
}

gap_percent = ((data_to_compare["Yesterday"] - data_to_compare["The day before"])/data_to_compare["The day before"]) * 100
up_down = None
if gap_percent > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

def get_send_news():
    news_response = requests.get(NEWS_ENDPONT, params=param_for_news)
    top_three = news_response.json()["articles"][:3]
    three_article = [f"{STOCK}: {up_down}{round(gap_percent)}%\nHeadline: {top_three[i]['title']}\nBrief: {top_three[i]['description']}" for i in range(len(top_three))]
    client = Client(account_sid, auth_token)
    for article in three_article:
            message = client.messages.create(
                body= article,
                from_=XXXX,
                to=XXXX
            )
            print(message.status)

if gap_percent > 5 or gap_percent < -5:
    get_send_news()



