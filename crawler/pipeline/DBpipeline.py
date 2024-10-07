

from utils.logger import logger


class DBpipeline:
    def process_item(self, item, spider):
        # 将 item 存储到数据库中
        print("")
        id = item['id']
        logger.info(f'DB pipeline saving item to database.. ID:{id}')
        # 这里可以添加数据库存储的逻辑
        return item


