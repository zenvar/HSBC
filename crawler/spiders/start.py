from crawler.spiders.job_spider import JobSpider
from crawler.spiders.job_spider import JobSpider
from scrapy.crawler import CrawlerProcess
from utils.logger import logger

def start_scrapy():
    logger.info('started!')
    # 创建配置字典
    custom_settings = {
      'ITEM_PIPELINES': {
        'crawler.pipeline.LLMpipeline.LLMpipeline': 300,  # 先通过 LLM 处理
        'crawler.pipeline.DBpipeline.DBpipeline': 400,   # 然后存储到数据库
        'crawler.pipeline.NotifyPipeline.NotifyPipeline': 500,  # 最后发送通知
    },
    'CONCURRENT_REQUESTS': 32,  # 控制全局并发请求数
    'CONCURRENT_REQUESTS_PER_DOMAIN': 16,  # 控制每个域名的并发请求数
    'DOWNLOAD_DELAY': 0.25,  # 关闭下载延迟
    'CONCURRENT_ITEMS' : 1,  # 一次只允许一个 item 被处理
    'LOG_LEVEL' : 'WARNING'

    }
    # 传入配置 settings=custom_settings
    process = CrawlerProcess(settings=custom_settings)
    process.crawl(JobSpider)
    process.start()