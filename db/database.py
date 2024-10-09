import sqlite3

from utils.logger import logger

class Database:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS jobs (
                id TEXT PRIMARY KEY,
                title TEXT,
                location TEXT,
                date TEXT,
                url TEXT,
                description TEXT,
                summary TEXT
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS url (
                id TEXT PRIMARY KEY,
                url TEXT 
            )
        ''')
        self.conn.commit()

    def insert_url(self,id,url):
        try:
            self.cursor.execute('''
                INSERT INTO url (id, url)
                VALUES (?, ?)
            ''', [id,url])
            self.conn.commit()
            logger.info(f"成功插入数据: {url}")
        except sqlite3.IntegrityError:
            logger.warning(f"数据已存在: {url}")
        except Exception as e:
            logger.error(f"插入数据失败: {url}")
            

    def udate_url(self,id,url):
        try:
            self.cursor.execute('''
                UPDATE url
                SET url = ?
                WHERE id = ?
            ''', [url,id])
            self.conn.commit()
            logger.info(f"成功插入数据: {url}")
        except sqlite3.IntegrityError:
            logger.warning(f"数据已存在: {url}")
        except Exception as e:
            logger.error(f"插入数据失败: {url}, 错误: {e}")

    def get_url(self,id):
            self.cursor.execute('''
                SELECT url from url WHERE id = ?
        ''',[id])
            row = self.cursor.fetchone()
            return row[0] if row else None
    


    def insert_job(self, job_data):
        try:
            self.cursor.execute('''
                INSERT INTO jobs (id, title, location, date, url, description, summary)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (
                job_data['id'],
                job_data['title'],
                job_data['location'],
                job_data['date'],
                job_data['url'],
                job_data['description'],
                job_data['summary']  # 添加 summary 字段
            ))
            self.conn.commit()
            #logger.info(f"成功插入数据: {job_data['id']}")
        except sqlite3.IntegrityError:
            logger.warning(f"数据已存在: {job_data['id']}")
        except Exception as e:
            logger.error(f"插入数据失败: {job_data['id']}, 错误: {e}")

    # ... other methods