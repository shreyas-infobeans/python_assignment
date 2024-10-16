import mysql.connector

conn = mysql.connector.connect(host='localhost',database='school',username='root',password='Root@123')

if conn.is_connected():
    print("Connected")
cursor = conn.cursor()
cursor.execute('select * from student')
"""row = cursor.fetchone()

while row is not None:
    print(row)
    row = cursor.fetchone()"""
rows = cursor.fetchall()
print("Total number of records",cursor.rowcount)
for row in rows:
    print(row)
conn.close()
    