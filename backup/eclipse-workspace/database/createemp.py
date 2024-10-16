import mysql.connector

conn = mysql.connector.connect(host='localhost',database='pythondb',username='root',password='Root@123')

if conn.is_connected():
    print("Connected")
cursor = conn.cursor()
try:
    cursor.execute("INSERT INTO `emp`(`idemp`,`name`,`salary`)VALUES(300,'Abby',5000)")
    conn.commit()
except:
    conn.rollback()

conn.close()
    