from bs4 import BeautifulSoup
import requests
from line_message import send_message

YAHOO_STOCK_URL = 'https://tw.stock.yahoo.com/q/q?s='


def check_price(stock_name='2330', operator='less_than', price=650):
    current_price = get_current_price(stock_name)
    if operator == 'less_than':
        print("current price is less than target price")
        if current_price < price:
            send_message(f"{stock_name} is less than {price}. current price is {current_price}")
    elif operator == 'larger_than':
        print("current price is larger than target price")
        if current_price > price:
            send_message(f"{stock_name} is larger than {price}. current price is {current_price}")
    else:
        print(f"{stock_name} {operator} {price}")
def get_current_price(stock_id):
    url = f"{YAHOO_STOCK_URL}{stock_id}"
    print(url)
    list_req = requests.get(url)
    soup = BeautifulSoup(list_req.content, "html.parser")
    temp_html = soup.select("#main-0-QuoteHeader-Proxy > div > div:nth-child(2) > div > div > span")
    stock_price = temp_html[0].text
    return float(stock_price)
# 測試
check_price()