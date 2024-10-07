from telegram import Bot
from config.Config import Config
import requests

# 使用你在 BotFather 生成的 Token
config = Config()
bot_token = config.get('telegram','key')
channel_id = config.get('telegram','channel_id') # 或者使用 Chat ID: -100xxxxxx




def telegram_msg(msg):

    md_str = msg.replace('**','*')

    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    # 请求参数
    data = {
        'chat_id': channel_id,
        'text': md_str,
        'parse_mode': 'Markdown'  # 使用Markdown
    }

    # 发送POST请求
    response = requests.post(url, data=data)

    # 检查响应
    if response.status_code == 200:
        print('Message sent successfully!')
    else:
        print(f"Failed to send message. Error: {response.text}")