## 切换到文件夹

	$ cd E:\git\spiders\bgmspider
	
## 检查爬虫列表

    $ scrapy list
    bgm-xpath

## Running the spiders

    $ scrapy crawl bgm-xpath

## 保存数据 `-o` :
    
    $ scrapy crawl bgm-xpath -o bgm.json
	$ scrapy crawl bgm-xpath -o bgm.csv