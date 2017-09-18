from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy import Request
from ieeespider.items import Paper

class IEEESpider(Spider):
    name = "ieeespider"
    allow_domain = ["ieee.org"]

    def start_requests(self):
        total_page = 10
        base_url = "http://ieeexplore.ieee.org/search/searchresult.jsp?queryText=machine%20"
        base_url2= "learning&pageNumber=%s&rowsPerPage=10"
        for page in range(total_page):
            yield Request(base_url + base_url2 % str(page+1), self.parse)

    def parse(self, response):
        sel = Selector(response)
        print sel.xpath('//body/text()').extract_first()
        paper_url_list = sel.xpath('//div[@class="pure-u-22-24"]/h2/a/@href').extract()
        print paper_url_list
        for paper_url in paper_url_list:
            print paper_url

