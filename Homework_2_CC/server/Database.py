import mysql.connector
import json

database = mysql.connector.connect(
    host="localhost",
    user="cloud.computing",
    passwd="12345",
    auth_plugin='mysql_native_password',
    database="database_cloud_computing"
)


def get_users():
    users = {}
    cursor = database.cursor()

    cursor.execute("SELECT * FROM users")
    results = cursor.fetchall()

    for row in results:
        user_data = {}

        user_id = row[0]
        first_name = row[1]
        last_name = row[2]
        date_of_birth = row[3]
        is_premium = row[4]

        user_data["first_name"] = first_name
        user_data["last_name"] = last_name
        user_data["date_of_birth"] = str(date_of_birth)
        user_data["is_premium"] = str(bool(is_premium))

        users[str(user_id)] = user_data

    return json.dumps(users)
