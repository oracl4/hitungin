from datetime import datetime 
import mysql.connector 

mydb = mysql.connector.connect( 
host="192.168.43.238",
user="AdminHitungin",
passwd="",
database="hitungin"
) 

mycursor = mydb.cursor()

totalLantai2=2

sql = "INSERT INTO record1(value) VALUES (%s)"
val = (totalLantai2,)
mycursor.execute(sql, val)
mydb.commit()

