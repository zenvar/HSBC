import re
import scrapy
from config.Config import Config
from utils.logger import logger

config = Config()

class JobSpider(scrapy.Spider):
    name = 'job_spider'
    start_urls = [config.get('crawler_url', 'fullurl')]
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
    }
    max_pages = 6  # 定义最大翻页数
    page_counter = 1  # 计数当前的页数

    def parse(self, response):
        results_div = response.css('div.section__content__results')
        for article in results_div.css('article.article--result'):
            job_title = article.css('h3 a::text').get()
            job_title = re.sub(r'\s+', ' ', job_title).strip()  # 将多个空白字符替换成一个空格，并去除开头和结尾的空格

            job_url = article.css('h3 a::attr(href)').get()

            job_location = article.css('span.location::text').get()
            job_location = re.sub(r'\s+', ' ', job_location).strip()  

            job_date = article.css('div.item__container:has(i.icon--calendar) span::text').get()
            job_date = re.sub(r'\s+', ' ', job_date).strip()  

            # logger.info(f"爬取到岗位信息: 标题={job_title}, URL={job_url}, 地址={job_location}, 日期={job_date}")

            yield scrapy.Request(
                job_url, 
                callback=self.parse_job_detail,
                meta={
                    'title': job_title,
                    'location': job_location,
                    'date': job_date
                })
            
        # 翻页逻辑
        if self.page_counter < self.max_pages:  # 如果当前页数小于最大页数
            next_page_url = response.css('a.paginationNextLink::attr(href)').get()  # 获取下一页的链接
            if next_page_url:  # 如果存在下一页的链接
                self.page_counter += 1  # 增加当前页数计数
                logger.info('-----Next page, page %s ------',self.page_counter)
                yield scrapy.Request(next_page_url, callback=self.parse)  # 请求下一页


    def parse_job_detail(self, response):
        job_id = response.css('div.article__content__view__field.field--w--icon.view-icon--pen div.article__content__view__field__value::text').get()
        job_id = re.sub(r'\s+', ' ', job_id).strip()  # 将多个空白字符替换成一个空格，并去除开头和结尾的空格

        job_description = response.css('div.section__content *::text').getall()
        job_description = ' '.join(job_description)  # 先将列表拼接成字符串
        job_description = re.sub(r'\s+', ' ', job_description)  # 将多个空白字符替换成一个空格
        job_description = re.sub(r' ', ' ', job_description)  # 将   替换成空格
        job_description = re.sub(r'"', '', job_description)  # 去除双引号
        job_description = job_description.strip()  # 去除开头和结尾的空格

        #job_summary = GeminiSummary(job_description)

        logger.info(f"爬取到岗位详情: ID={job_id},  URL={response.url}")
         # 从 meta 参数中获取列表页面提取到的数据
        job_title = response.meta['title']
        job_location = response.meta['location']
        job_date = response.meta['date']

        # 组装完整数据并入库
        job_data = {
            'title': job_title,
            'id': job_id,
            'location': job_location,
            'date': job_date,
            'url': response.url,
            'description': job_description
        }
        yield job_data

