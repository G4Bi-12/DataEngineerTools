import scrapy

class ChurchillQuotesSpider(scrapy.Spider):
    name = "citations de Churchill"
    start_urls = ["http://evene.lefigaro.fr/citations/winston-churchill",]

    def parse(self, response):
        for cit in response.xpath('//li[@class="figsco__selection__list__evene__list__item"]'):
            
            text_value = cit.xpath('//div[@class="figsco__quote__text"]').xpath('a/text()').extract_first()
            if text_value:
                text_value = text_value.replace('“','').replace('”','')
            author_value = cit.xpath('//div[@class="figsco__fake__col-9"]').xpath('a/text()').extract_first()
            yield {'text': text_value, 'author': author_value}