
from notify.telegram.bot import telegram_msg
from utils.logger import logger


class NotifyPipeline:
    def process_item(self, item, spider):
        # 发送通知，例如发邮件或消息通知
        #print("")
        id = item['id']
        #logger.info(f'Notify pipeline sending notification...ID:{id}')
        telegram_msg(item['summary'])
        # 通知逻辑
        return item
