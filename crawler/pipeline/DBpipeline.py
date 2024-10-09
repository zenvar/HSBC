from config.Config import Config
from db.database import Database

from utils.logger import logger


class DBpipeline:
    def process_item(self, item, spider):
        config = Config()
        db = Database(config.get('database', 'path'))
        db.insert_job(item)
        # 将 item 存储到数据库中
        id = item['id']
        #logger.info(f'DB pipeline saving item to database.. ID:{id}')
        # 这里可以添加数据库存储的逻辑
        return item


