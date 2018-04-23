# -*- coding: utf-8 -*-
import scrapy


class ToScrapeSpiderXPath(scrapy.Spider):

    
    
    
    name = 'toscrape-xpath'
    start_urls = [
        #'http://bgm.tv/anime/browser?sort=rank&page=1',
		#'http://bgm.tv/anime/browser/?sort=date&page=1'
		'http://wanimal1983.org/',
    ]

    def parse(self, response):
        print(response.body)
        for quote in response.xpath('//div[@class="photoset_row photoset_row_1"]'):
            yield {
                'text': quote.xpath('./a/@href()').extract(),
                
                'rate': quote.xpath('./a/@rel()').extract(),
				
				# 'number': quote.xpath('.//p[@class="rateInfo"]//span[@class="tip_j"]/text()').extract(),
				# 'rank': quote.xpath('.//span[@class="rank"]/text()').extract(),
				# 'inform_tip': quote.xpath('.//p[@class="info tip"]/text()').extract(),
            }

        next_page_url = response.xpath('//a[@id="next"]/@href()').extract()[-2]
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))

