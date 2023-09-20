import sqlite3

db = sqlite3.connect('news.db')

cursor = db.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS news(
news_id INTEGER PRIMARY KEY AUTOINCREMENT,
Title TEXT,
Publisher TEXT,
Image TEXT,
Link TEXT
);
''')

db.commit()
db.close()
