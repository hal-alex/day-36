import requests
import newsapi

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
VANTAGE_API_KEY = "CFWSGXJVS2L2S6B5"

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": VANTAGE_API_KEY,
}

response = requests.get("https://www.alphavantage.co/query", params=parameters)
response.raise_for_status()

data = response.json()["Time Series (Daily)"]



    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries.
# e.g. [new_value for (key, value) in dictionary.items()]

price_list = [value for (key, value) in data.items()]
yesterdays_close_price = float(price_list[0]["4. close"])
print(yesterdays_close_price)


#TODO 2. - Get the day before yesterday's closing stock price

day_before_yesterday_close = float(price_list[1]["4. close"])
print(day_before_yesterday_close)

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

raw_difference = abs(yesterdays_close_price - day_before_yesterday_close)

print(raw_difference)

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

perctange_difference = (raw_difference / yesterdays_close_price)  * 100

print(perctange_difference)

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

if perctange_difference > 1:
    api = newsapi.NewsApiClient(api_key="b0228b5ce50e4adca6509a06cd549232")
    news_api_articles = api.get_everything(q=COMPANY_NAME)
    top_three_articles = news_api_articles["articles"][:3]


    list_articles = [article["title"] for article in top_three_articles]
    for article in list_articles:
        print(article)

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9.  - Send each article as a separate message via Twilio.



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

