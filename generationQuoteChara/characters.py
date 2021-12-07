# -*- coding: utf-8 -*-
import scrapy


class blogSpider(scrapy.Spider):
    name = "characterSpider"
    start_urls = ['https://fr.wikipedia.org/wiki/Personnages_de_League_of_Legends', ]

    def parse(self, response):
        for link in response.css('div.mw-parser-output  h2'):
            yield {
                'character': link.css('span ::text').extract_first(),
            }
