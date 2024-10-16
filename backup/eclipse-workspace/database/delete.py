import mysql.connector

def delete(id):
    
    conn = mysql.connector.connect(host='localhost',database='pythondb',username='root',password='Root@123')

    if conn.is_connected():
        print("Connected")
    cursor = conn.cursor()
    query = "delete from emp where idemp='%d'"
    args = (id)
    try:
        cursor.execute(query % args)
        conn.commit()
        print("Employee deleted")
    except:
        conn.rollback()
    finally:
        cursor.close()
        conn.close()
    
empid = int(input("Enter id to delete:"))
delete(empid)

        