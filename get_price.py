from bs4 import BeautifulSoup
import requests

YAHOO_SROCK_URL = 'https://tw.stock.yahoo.com/q/q?s='

def get_current_price(stick_id):
        url = f"{YAHOO_SROCK_URL}{stick_id}"
        print(url)
        list_req = requests.get(url)
        soup = BeautifulSoup(list_req.content,"html.parser")
        css_selector = "#main-0-QuoteHeader-Proxy > div > div:nth-child(2) div > div > span"
        temp_html = soup.select(css_selector)
        stock_price = temp_html[0].text
        print(stock_price)
        return float(stock_price)

# 測試
get_current_price(2303)