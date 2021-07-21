import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
from .models import Prices, Company

from celery import shared_task
from celery import Celery

from celery.schedules import crontab

# app = Celery('tasks')
#
# app.conf.beat_schedule = {
#     # executes every 1 minute
#     'scraping-task-one-min': {
#         'task': 'tasks.hackernews_rss',
#         'schedule': crontab()
#     }
# }

def months(month):
    switcher = {
        'sty': 1,
        'lut': 2,
        'mar': 3,
        'kwi': 4,
        'maj': 5,
        'cze': 6,
        'lip': 7,
        'sie': 8,
        'wrz': 9,
        'paź': 10,
        'lis': 11,
        'gru': 12
    }
    return switcher.get(month, "Invalid day of week")


def convert_date_to_date_field(info):
    if len(info) == 10:
        day = info[0:1]
        month = months(info[2:5])
        year = info[6:10]
    else:
        day = info[0:2]
        month = months(info[3:6])
        year = info[7:11]
    result = year + '-' + str(month) + '-' + day
    print(result)
    return result


@shared_task
def stock_prices_rss():
    companies = ['ale', 'acp', 'pzu']
    print('Start scraping')
    try:
        print('hello te')
        req = requests.get("https://stooq.pl/q/d/?s=acp")
        soup = BeautifulSoup(req.content, 'html.parser')
        company = Company.objects.get(company_name='ACP')
        for x in soup.find_all("tr"):
            if x.text[0:1].isdigit():
                if x.text[4:5].isdigit():
                    if x.text[5:6].isdigit():
                        data = convert_date_to_date_field(x.text[4:15])
                        opening = float(x.text[15:20])
                        highest = float(x.text[20:25])
                        lowest = float(x.text[25:30])
                        closing = float(x.text[30:35])
                        # opening = 33.33
                        # highest = 22.22
                        # lowest = 11.11
                        # closing = 55.55

                    else:
                        data = convert_date_to_date_field(x.text[4:14])
                        opening = float(x.text[14:19])
                        highest = float(x.text[19:24])
                        lowest = float(x.text[24:29])
                        closing = float(x.text[29:34])
                        # opening = 22.22
                        # highest = 22.22
                        # lowest = 11.11
                        # closing = 55.55

                    price = Prices.objects.create(
                        opening_price=opening,
                        highest_price=highest,
                        lowest_price=lowest,
                        closing_price=closing,
                        date=data,
                    )
                    company.prices.add(price)
                    company.save()
    except Exception as e:
        print('The scraping job failed. See exception:')
        print(e)


