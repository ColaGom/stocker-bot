class Stock:
    def __init__(self, element):
        self.short_id = element.find('shotnIsin').text
        self.name = element.find('korSecnNm').text

    def __str__(self) -> str:
        return "["+self.short_id+"]" + self.name

    def append_basic(self, element):
        self.nameEng = element.find('engSecnNm').text
        self.id = element.find('isin').text
        self.issu_date = element.find('issuDt').text
        self.issu_company_id = element.find('issucoCustno').text
        self.stock_type = element.find('secnKacdNm').text

    def append_listing_info(self, elements):
        self.listing_info = []
        for element in elements:
            self.listing_info.append(ListingInfo(element))
            
    def append_listing_info(self, elements):
        self.bond_info = []
        for element in elements:
            self.bond_info.append(BondInfo(element))


class ListingInfo:
    def __init__(self, element):
        self.listing_date = element.find('apliDt').text
        self.closing_date = element.find('dlistDt').text
        self.issu_company_id = element.find('issucoCustno').text
        self.type = element.find('listTpcd').text
        self.expired_at = element.find('xpitDt').text


class BondInfo:
    def __init__(self, element):
        self.issucoCustno = element.find('issucoCustno').text
        self.korSecnNm = element.find('korSecnNm').text
        self.newstkAlocDdBfLimitDays = element.find('newstkAlocDdBfLimitDays').text # 신주배정일전제한일수
        self.setaccEndtermLimitDays = element.find('setaccEndtermLimitDays').text # 결산기말제한일
        self.wrtbIsin = element.find('wrtbIsin').text # 신주인수권증권 종목번호
        self.xrcPrice = element.find('xrcPrice').text # 행사가
        self.xrcRatio = element.find('xrcRatio').text # 행사비율
        self.xrcStkIsin = element.find('xrcStkIsin').text # 행사주식종목번호 
        self.xrcStkIsinNm = element.find('xrcStkIsinNm').text #행사주식명