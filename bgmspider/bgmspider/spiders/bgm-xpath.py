# -*- coding: utf-8 -*-
import scrapy


class BgmSpider(scrapy.Spider):
    name = 'bgm-xpath'
    allowed_domains = ['bgm.tv']
    start_urls = [
         'http://bgm.tv/anime/browser?sort=rank&page=1',
        # 'http://bgm.tv/anime/browser/?sort=date&page=1'
        # 'http://bgm.tv/anime/browser/?sort=title',
    ]

    def parse(self, response):
        for quote in response.xpath('//ul[@class="browserFull"]//div[@class="inner"]'):
            yield {
                'text': quote.xpath('./h3/a/text()').extract(),

                'rate': quote.xpath('.//p[@class="rateInfo"]//small/text()').extract(),

                'number': quote.xpath('.//p[@class="rateInfo"]//span[@class="tip_j"]/text()').extract(),
                'rank': quote.xpath('.//span[@class="rank"]/text()').extract(),
                'inform_tip': quote.xpath('.//p[@class="info tip"]/text()').extract(),
            }

        next_page_url = response.xpath('//div[@class="page_inner"]/a/@href').extract()[-2]
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))
