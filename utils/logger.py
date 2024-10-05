import logging
import logging.handlers
from config.Config import Config

config = Config()

# 获取日志级别
log_level = config.get('logging', 'level').upper()
level = getattr(logging, log_level, logging.INFO)

# 创建 logger
logger = logging.getLogger('job_crawler')
logger.setLevel(level)

# 创建 handler
# 输出到文件
file_handler = logging.handlers.RotatingFileHandler(
    config.get('logging', 'file'),
    maxBytes=1024 * 1024 * 10,  # 10 MB
    backupCount=5,
    encoding='utf-8'
)
file_handler.setLevel(level)

# 输出到控制台
console_handler = logging.StreamHandler()
console_handler.setLevel(level)

# 创建 formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# 添加 formatter 到 handler
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# 添加 handler 到 logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)