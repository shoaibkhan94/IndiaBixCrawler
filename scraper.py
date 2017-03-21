import scrapy

class IndiaBixSpider(scrapy.Spider):
    name = "indiabix"
    allowed_domain = ["www.indiabix.com"]
    with open('crawled.txt') as f:
        start_urls = [url.strip() for url in f.readlines()]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, meta={
                'splash': {
                    'endpoint': 'render.html',
                    'args': {'wait': 0.5}
                }
            })

    def parse(self, response):
        main_tag = response.url.split('/')[3]
        sub_tag = response.url.split('/')[4]
        page_tag = response.url.split('/')[5]
        for question in response.css("div.bix-div-container"):
            answer = question.xpath(".//input[starts-with(@id, 'hdnAnswer')]/@value").extract()
            qs = question.xpath(".//p/text()").extract_first()
            optiona = question.xpath(".//td[starts-with(@id, 'tdOptionDt_A')]/text()").extract()
            optionb = question.xpath(".//td[starts-with(@id, 'tdOptionDt_B')]/text()").extract()
            optionc = question.xpath(".//td[starts-with(@id, 'tdOptionDt_C')]/text()").extract()
            optiond = question.xpath(".//td[starts-with(@id, 'tdOptionDt_D')]/text()").extract()
            optione = question.xpath(".//td[starts-with(@id, 'tdOptionDt_E')]/text()").extract()
            code = question.xpath(".//code/text()").extract_first()
            yield {
                'question' : qs,
                'optionA' : optiona,
                'optionB' : optionb,
                'optionC' : optionc,
                'optionD' : optiond,
                'optionE' : optione,
                'answer' : answer,
                'code' : code,
                'main_tag' : main_tag,
                'sub_tag' : sub_tag,
                'page_tag' : page_tag
            }

