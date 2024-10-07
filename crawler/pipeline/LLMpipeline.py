
from LLM.gemini import GeminiSummary
from utils.logger import logger

class LLMpipeline:
    def process_item(self, item, spider):
        # 对 item 进行语言模型处理
        item['summary'] = self.llm_process(item['description'])
        logger.info(item['summary'])
        return item

    def llm_process(self, raw_data):
        # 具体的处理逻辑（调用语言模型）
        return GeminiSummary(raw_data)


