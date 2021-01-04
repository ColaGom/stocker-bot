from urllib.parse import urlencode, urljoin
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

HOST = "http://api.seibro.or.kr/openapi/service/StockSvc/getShotnByMartN1"


def stock_short(page_num, martket):
    queries = {"pageNo": page_num, "numbOfRows": 10000 }
    query_string = urlencode()
    return urljoin(HOST, "getShotnByMartN1")+'?'+''
