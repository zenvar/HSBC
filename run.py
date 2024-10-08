import time
import schedule
from scrapy.crawler import CrawlerProcess
from crawler.spiders.start import start_scrapy
from db.database import Database
from config.Config import Config

config = Config()

# 设置定时任务（例如每隔1小时运行一次爬虫）
schedule.every(120).seconds.do(start_scrapy)

if __name__ == "__main__":
    #db = Database(config.get('database','path'))
    #db.insert_url(config.get('url','latest'))
    # 启动定时任务调度器
    while True:
        schedule.run_pending()  # 检查是否有任务需要执行
        time.sleep(1)  # 每秒检查一次
