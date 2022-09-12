import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="team",
  passwd="*Azerty01*",
  db="projet_equides",
  )

my_cursor = mydb.cursor()

my_cursor.execute("SELECT* FROM equides")

for db in my_cursor :
  print(db)

