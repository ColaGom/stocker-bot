# -*- coding: utf-8 -*- 0

import os
import xml.etree.ElementTree as ET
import requests
from entity import *
from urllib.parse import urlencode, urljoin


KEY = os.environ.get("API_KEY")
HOST = "http://api.seibro.or.kr/openapi/service/StockSvc/getShotnByMartN1"

# 시장별 단축코드 전체 조회
# martTpcd
# 11.유가증권시장, 12.코스닥, 13.K-OTC, 14.코넥스, 50.기타시장


def stock_short(page_num, market):
    queries = {"pageNo": page_num,
               "numOfRows": 10000, "martTpcd": market}
    query_string = urlencode(queries)
    url = urljoin(HOST, "getShotnByMartN1")+'?'+query_string+'&serviceKey='+KEY
    response = requests.get(url)
    root = ET.fromstring(response.text)

    items = root.findall('.//items/item')
    print("Response : " + str(len(items)))

    stocks = []

    for item in items:
        stocks.append(Stock(item))

    for stock in stocks:
        print(stock)

    return stocks

# 주식 기본 정보


def dispatch_basic(stock):
    queries = {"shortIsin": stock.short_id,
               "numOfRows": 10, "pageNo": 1}
    query_string = urlencode(queries)
    url = urljoin(HOST, "getStkIsinByShortIsinN1") + \
        '?'+query_string+'&serviceKey='+KEY
    response = requests.get(url)
    root = ET.fromstring(response.text)
    element = root.find('.//items/item')
    stock.append_basic(element)
    return stock


# 주식상장정보
#
def dispatch_listing_info(stock):
    queries = {"isin": stock.id,
               "numOfRows": 10, "pageNo": 1}
    query_string = urlencode(queries)
    url = urljoin(HOST, "getStkListInfoN1") + \
        '?'+query_string+'&serviceKey='+KEY
    response = requests.get(url)
    root = ET.fromstring(response.text)
    elements = root.findall('.//items/item')
    stock.append_listing_info(elements)
    return stock
