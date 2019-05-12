import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
from datetime import datetime

def insertPythonVaribleInTable(value):
	try:
		connection = mysql.connector.connect(host='localhost',
							 database='hitungin',
							 user='root',
							 password='')
		cursor = connection.cursor(prepared=True)
		sql_insert_query = """ INSERT INTO `record`
						  (`value`) VALUES (%s)"""
		insert_tuple = (value)
		result  = cursor.execute(sql_insert_query, insert_tuple)
		connection.commit()
		print ("Record inserted successfully into python_users table")
	except mysql.connector.Error as error :
		connection.rollback()
		print("Failed to insert into MySQL table {}".format(error))
	finally:
		#closing database connection.
		if(connection.is_connected()):
			cursor.close()
			connection.close()
			print("MySQL connection is closed")

insertPythonVaribleInTable(31)
insertPythonVaribleInTable(32)
