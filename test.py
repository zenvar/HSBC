from crawler.spiders.job_spider import JobSpider
from crawler.spiders.job_spider import JobSpider
from scrapy.crawler import CrawlerProcess
from utils.logger import logger

logger.info('started!')
# 创建配置字典
custom_settings = {
    'CONCURRENT_REQUESTS': 32,  # 控制全局并发请求数
    'CONCURRENT_REQUESTS_PER_DOMAIN': 16,  # 控制每个域名的并发请求数
    'DOWNLOAD_DELAY': 0,  # 关闭下载延迟
}
# 传入配置
process = CrawlerProcess(settings=custom_settings)
process.crawl(JobSpider)
process.start()
