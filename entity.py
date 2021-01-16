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


class ListingInfo:
    def __init__(self, element):
        self.listing_date = element.find('apliDt').text
        self.closing_date = element.find('dlistDt').text
        self.issu_company_id = element.find('issucoCustno').text
        self.type = element.find('listTpcd').text
        self.expired_at = element.find('xpitDt').text
