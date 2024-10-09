from db.database import Database
from config.Config import Config
config = Config()
db = Database(config.get('database','path'))
db.insert_url('1','https://mycareer.hsbc.com/en_GB/external/PipelineDetail/Senior-Software-Engineering-Manager/246610')
db.insert_url('2','https://mycareer.hsbc.com/en_GB/external/PipelineDetail/Software-Engineer/246371')