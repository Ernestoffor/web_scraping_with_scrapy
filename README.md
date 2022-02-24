# Web scraping with scrapy

Scrapy is an effective web scraper with five components, namely:

1. Spiders - defines what to be extracted from web page as a python class. There five of them, viz: 
    1. scrapy.Spider
    2. crawlSpider
    3. XMLFeedSpider
    4. CSVFeedSpider
    5. SitemapSpider

2. Pipelines:
    . Cleaning the data
    . Removing Duplications
    . Storing the data
3. Middlewares:
    . Requests
    . Response to the website
    . Injecting custom headers
    . Proxying
4. Engine- coordinates the other components thereby maintaining consistency
5. Scheduler
