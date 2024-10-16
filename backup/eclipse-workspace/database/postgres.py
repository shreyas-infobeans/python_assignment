import psycopg2

connection = psycopg2.connect(database="employeedb",user="test",password="password",host="127.0.0.1")

print("Connected to db")
cursor = connection.cursor()
cursor.execute("insert into employee (name,sal) values ('abc',20000)")
connection.commit()
connection.close()