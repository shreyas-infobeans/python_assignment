import mysql.connector

def delete(id):
    
    conn = mysql.connector.connect(host='localhost',database='school',username='root',password='Root@123')

    if conn.is_connected():
        print("Connected")
    cursor = conn.cursor()
    query = "delete from student where id='%d'"
    args = (id)
    try:
        cursor.execute(query % args)
        conn.commit()
        print("Student deleted")
    except:
        conn.rollback()
    finally:
        cursor.close()
        conn.close()
    
#empid = int(input("Enter id to delete:"))
#delete(empid)

def update(name,id):
    
    conn = mysql.connector.connect(host='localhost',database='school',username='root',password='Root@123')

    if conn.is_connected():
        print("Connected")
    cursor = conn.cursor()
    query = "UPDATE student SET name=%s where id=%s"
    args = (name,id)
    try:
        cursor.execute(query , args)
        conn.commit()
        print("Student updated")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        
    finally:
        cursor.close()
        conn.close()
    
empid = int(input("Enter id to delete:"))
name = (input("Enter updated name:"))
update(name,empid)
        