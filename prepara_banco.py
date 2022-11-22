import mysql.connector
from mysql.connector import errorcode

print("Conectando...")
try:
      conn = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='admin'
      )
except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Existe algo errado no nome de usuário ou senha')
      else:
            print(err)

cursor = conn.cursor()

cursor.execute("DROP DATABASE IF EXISTS `api2`;")

cursor.execute("CREATE DATABASE `api2`;")

cursor.execute("USE `api2`;")

print('passou')
# criando tabelas


conn.commit()

cursor.close()
conn.close()
print('fechou')