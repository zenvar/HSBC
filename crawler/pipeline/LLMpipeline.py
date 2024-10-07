
from asyncio import sleep
from LLM.gemini import GeminiSummary
from utils.logger import logger

class LLMpipeline:
    def process_item(self, item, spider):
        # 对 item 进行语言模型处理
        text = 'Apply URL:'+item['url']+'\n'+item['description']
        item['summary'] = self.llm_process(text)
        logger.info(item['summary'])
        return item

    def llm_process(self, raw_data):
        # 具体的处理逻辑（调用语言模型）
        return GeminiSummary(raw_data)


