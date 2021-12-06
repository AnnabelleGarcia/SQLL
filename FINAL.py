import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Agg35241",
  database= "menagerie"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT DISTINCT name, birth FROM pet")
for x in mycursor:
  print(x)
print(mydb)