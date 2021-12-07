# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector


class blogSpider(scrapy.Spider):
    name = 'blogSpider'
    start_urls = ['https://www.babelio.com/auteur/Howard-Phillips-Lovecraft/54210/citations?filtre=3857']

    def parse(self, response):
        for title in response.css('div.post_con div.text.row div'):
            yield {'quote': title.css('div ::text').extract_first()}

        nextPages = response.css('div.pagination.row > a').extract()
        for index, page in enumerate(nextPages):
            if 'class="active"' in page:
                nPage = nextPages[index + 1]
                nextPage = Selector(text=nPage).xpath('//a/@href').extract()
                nextPage_url = nextPage[0]
                if index == (len(nextPages) - 1):
                    nextPage = False

        if nextPage:
            yield scrapy.Request(response.urljoin(nextPage_url), callback=self.parse)