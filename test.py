from crawler.spiders.job_spider import JobSpider
from crawler.spiders.job_spider import JobSpider
from scrapy.crawler import CrawlerProcess


process = CrawlerProcess()
process.crawl(JobSpider)
process.start()
