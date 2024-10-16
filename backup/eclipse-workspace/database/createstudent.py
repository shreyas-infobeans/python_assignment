import mysql.connector

conn = mysql.connector.connect(host='localhost',database='school',username='root',password='Root@123')

if conn.is_connected():
    print("Connected")
cursor = conn.cursor()
try:
    cursor.execute("INSERT INTO `student`(`id`,`name`,`age`)VALUES(100,'Abby',5)")
    conn.commit()
except:
    conn.rollback()

conn.close()
    