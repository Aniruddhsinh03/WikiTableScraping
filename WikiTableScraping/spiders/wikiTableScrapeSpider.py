# -*- coding: utf-8 -*-
import scrapy


class WikitablescrapespiderSpider(scrapy.Spider):
    name = 'wikiTableScrapeSpider'
    allowed_domains = ['en.wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/List_of_cities_in_India_by_population']

    def parse(self, response):
        # Select Table From html
        table = response.xpath('//table[contains(@class, "wikitable sortable")]')[0]
        # Select Rows
        trs = table.xpath('.//tr')[1:]
        # Extract Each Row One By One
        for tr in trs:
            # Extract Table Data
            rank = tr.xpath('.//td[1]/text()').extract_first()
            city = tr.xpath('.//td[2]//text()').extract_first()
            population = tr.xpath('.//td[3]//text()').extract_first()
            state = tr.xpath('.//td[5]//text()').extract_first()

            yield {'rank': rank,
                   'city': city,
                   'state': state,
                   'population': population}
