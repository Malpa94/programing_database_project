import mysql.connector
from mysql.connector import connect, errorcode

USER = 'root'
PASSWORD = 'admin'
DB = 'course_management'

stmt1 = """SELECT * FROM course"""

stmt2 = """ SELECT email FROM user WHERE id=5;"""

stmt3 = """ 
SELECT u.id, u.username, u.email FROM user u
JOIN user_course uc ON u.id = uc.user_id
WHERE uc.course_id = 2"""

stmt4 = """
SELECT c.id, c.title, c.description, c.start_data, c.end_date FROM course c
JOIN user_course uc ON c.id = uc.course_id
WHERE uc.user_id = 1
AND c.start_data > CURDATE()
"""

stmt5 = """
SELECT up.first_name, up.last_name, u.email
FROM user_profile up
JOIN user u ON up.user_id = u.id
WHERE registration_date > '2023-06-15'
"""

stmt6 = """
SELECT * FROM user_profile up
JOIN user u ON up.user_id = u.id
WHERE u.email = 'alex@example.com'
"""


try:
    with connect(user=USER, password=PASSWORD, database=DB) as cnx:
        with cnx.cursor() as cursor:
            #cursor.execute(stmt1)
            #cursor.execute(stmt2)
            #cursor.execute(stmt3)
            #cursor.execute(stmt4)
            #cursor.execute(stmt5)
            # cursor.execute(stmt6)
            #result = cursor.fetchall()
            #result2 = cursor.fetchone()
            #printing stmt1
            # for row in result:
            #     print(row)
            #printing stmt2
            # for row in result2:
            #     print(row)
            #printing stmt3
            # for row in cursor:
            #     print(row)
            #printing stmt4
            # for row in cursor:
            #     print(row)
            #printing stmt5
            # for row in cursor:
            #     print(row)
            #printing stmt6
            # for row in cursor:
            #     print(row)
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your username or password.")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exists.")
    elif err.errno == errorcode.ER_PARSE_ERROR:
        print("SQL syntax error\n", err)
    else:
        print("An error occured\n", err)
else:
    print("Done.")