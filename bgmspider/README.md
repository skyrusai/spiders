## 切换到文件夹

	$ cd E:\git\spiders\bgmspider
	
## 检查爬虫列表

    $ scrapy list
    bgm-xpath

## 运行爬虫 bgm-xpath

    $ scrapy crawl bgm-xpath

## 保存数据 -o :
    
    $ scrapy crawl bgm-xpath -o bgm.json
	$ scrapy crawl bgm-xpath -o bgm.csv