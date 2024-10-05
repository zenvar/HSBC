import sqlite3

class Database:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS jobs (
                url TEXT PRIMARY KEY,
                title TEXT
            )
        ''')
        self.conn.commit()

    def job_exists(self, url):
        self.cursor.execute("SELECT 1 FROM jobs WHERE url = ?", (url,))
        return self.cursor.fetchone() is not None

    def insert_job(self, url, title):
        self.cursor.execute("INSERT INTO jobs (url, title) VALUES (?, ?)", (url, title))
        self.conn.commit()

    # ... other methods