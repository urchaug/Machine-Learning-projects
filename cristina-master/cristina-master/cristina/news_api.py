from env_variables import *
from newsapi import NewsApiClient
import requests
import json
import asyncio
import datetime

#Init
newsapi = NewsApiClient(api_key=news_api_key)

all_articles = newsapi.get_everything(q='tesla',
                                      domains='bbc.co.uk',
                                      language='en',
                                      page=2)
from_date = datetime.date.fromordinal(datetime.date.today().toordinal()-1).strftime("%F")
to_date = datetime.datetime.today().strftime('%d-%m-%Y')

url = (f'https://newsapi.org/v2/everything?q=bitcoin&from=2019-04-05&sortBy=popularity&apiKey={news_api_key}')
response = requests.get(url)
response_json = response.json()
