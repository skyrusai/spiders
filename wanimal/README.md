print(response.body)

scrapy shell http://wanimal1983.org/

photo-wrapper

response.xpath('//div[@class="photo-wrapper"]').extract()

class="photoset_row photoset_row_1"
response.xpath('//div[@class="photoset_row photoset_row_1"]/a/@href()').extract()

photoset_photo rapid-noclick-resp

response.xpath('//a[@class="photoset_photo rapid-noclick-resp"]')