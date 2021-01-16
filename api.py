# -*- coding: utf-8 -*- 0

import os
import xml.etree.ElementTree as ET
import requests
from entity import *
from urllib.parse import urlencode, urljoin


KEY = os.environ.get("API_KEY")
HOST = "http://api.seibro.or.kr/openapi/service/StockSvc/getShotnByMartN1"

# 시장별 단축코드 전체 조회
# ServiceKey
# -
# 공공데이터포털에서 받은 인증키
# pageNo
# 1
# 페이지번호
# numOfRows
# 10
# 한 페이지 결과 수
# martTpcd
# 11
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
        id = item.find('shotnIsin').text
        name = item.find('korSecnNm').text
        stocks.append(ShortStockInfo(id, name))

    for stock in stocks:
        print(stock)

    return stocks
