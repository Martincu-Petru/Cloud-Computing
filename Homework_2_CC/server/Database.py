import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="cloud.computing",
    passwd="12345",
    auth_plugin='mysql_native_password'
)


print(database)
