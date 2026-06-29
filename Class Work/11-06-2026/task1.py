import pymysql
mydb = pymysql.connect(host="localhost", user= "root", password="2005")
mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS curd")
mydb.commit()

mydb = pymysql.connect(host="localhost", user= "root", password="2005" , database="curd")
mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE IF NOT EXISTS python80(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50), age INT)")
mydb.commit()