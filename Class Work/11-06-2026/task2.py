from task1 import *

mydb = pymysql.connect(host="localhost", user="root", password="2005", database="curd")
mycursor = mydb.cursor()

while True:
    menu = """
        Press 1 for insert data
        Press 2 for update data
        Press 3 for delete data
        Press 4 for Show data
        Press 5 for Exit
    """
    print(menu)
    ch = int(input("Enter your choice : "))
    
    if ch == 1:
        
        name = input("Enter your name : ")
        age = int(input("Enter your age : "))
        query = "INSERT INTO python80(name,age) VALUES (%s,%s)"
        args = (name,age)
        
        mycursor.execute(query, args)
        mydb.commit()
        
        print("Successsfully Data Insert!!")
        
    elif ch == 2:
        query = "select * from python80"
        mycursor.execute(query)
        data = mycursor.fetchall()
        print(data)

        id = int(input("Enter the id : "))
        name = input("Enter the name : ")
        age = int(input("Enter the age : "))
        
        query = "UPDATE python80 SET name = '%s' , age = '%s' WHERE id = '%s'"
        args = (id,name,age)
        mycursor.execute(query,args)

        print("Update Successfully!!!")
        
    elif ch == 3:
        query = "SELECT * FROM python80"
        mycursor.execute(query)
        data = mycursor.fetchall()
        print(data)
        id = int(input("Enter your id : "))

        query = "DELETE FROM python80 WHERE id = '%s'"
        args = (id)
        
        mycursor.execute(query,args)
        mydb.commit()
        print("Delete Successfully!!!")
        
    elif ch == 4:
        query = "SELECT * FROM python80"
        mycursor.execute(query)
        
        data = mycursor.fetchall()
        
        print("\nid | name | age")
        print("-" * 20)
        
        for row in data:
            print(row[0], "|", row[1],"|",row[2])
            
    elif ch == 5:
        print("Exiting Programe!!")
        break
    
    else:
        print("Invaild Choice!!")
        break