import sqlite3

conn = sqlite3.connect('product_info.db')
cursor = conn.cursor()

cursor.execute('SELECT * FROM product_info')

sqlins="""
INSERT INTO "main"."product_info"
("name","version","remark")
VALUES('Laptop','ASUS','I LUV ASUS')
"""
cursor.execute(sqlins)

records = cursor.fetchall()
conn.commit()
print(records)