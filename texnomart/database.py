import sqlite3
import psycopg2

database = psycopg2.connect(
    dbname='Sr-Sub-15-00',
    host='localhost',
    user='postgres',
    password='123456',
    port='5432'
)

cursor = database.cursor()

cursor.execute('''
    DROP TABLE IF EXISTS texnomart_products;
    
    CREATE TABLE IF NOT EXISTS texnomart_products(
    product_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    product_title TEXT,
    price TEXT,
    image TEXT,
    product_page_link TEXT
    );
    
''')
database.commit()
database.close()



db = sqlite3.connect('products.db')

cursor = db.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS texnomart_products(
product_id INTEGER PRIMARY KEY AUTOINCREMENT,
product_name TEXT,
product_price TEXT,
product_image TEXT,
product_page_link TEXT,
characteristics TEXT
);
''')

db.commit()
db.close()




