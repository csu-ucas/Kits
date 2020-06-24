import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database = "NodesInfo"
)

mycursor = mydb.cursor()

mycursor.execute("select * from Nodes;")

for x in mycursor:
  print(x)