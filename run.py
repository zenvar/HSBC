from multiprocessing import Process
import time
import schedule
from crawler.spiders.start import start_scrapy
from db.database import Database
from config.Config import Config

config = Config()

# 设置定时任务（例如每隔1小时运行一次爬虫）
#schedule.every(120).seconds.do(start_scrapy)

def run_spider_in_process():
    p = Process(target=start_scrapy)  # 在新进程中运行爬虫
    p.start()
    p.join()  # 等待进程结束

# 设置定时任务（例如每隔1小时运行一次爬虫）
schedule.every(90).seconds.do(run_spider_in_process)



if __name__ == "__main__":
    #db = Database(config.get('database','path'))
    #db.insert_url(config.get('url','latest'))
    #db.insert_url('2','https://mycareer.hsbc.com/en_GB/external/PipelineDetail/Software-Engineer/246371')
    
    # 启动定时任务调度器
    while True:
        schedule.run_pending()  # 检查是否有任务需要执行
        time.sleep(1)  # 每秒检查一次
