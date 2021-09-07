import mysql.connector
connection = mysql.connector.connect(host='localhost',
                                    database = 'rinku',
                                     user='root',
                                     password='rinku')
cursor = connection.cursor()
cursor.execute("select * from student;")
record = cursor.fetchall()
for i in record:
    print(i)


