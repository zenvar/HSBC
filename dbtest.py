from config.Config import Config
from db.database import Database


config = Config()
path = config.get('database','path')
print(path)
db = Database(path)
job_data = {
            'id': 'job_id',
            'title': 'job_title',
            'description': 'job_description',
            'url': 'job_url',
            'location': 'job_location',
            'date': 'job_date',
            'summary':'summary'
        }
db.insert_job(job_data)