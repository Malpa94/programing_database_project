import mysql.connector
from mysql.connector import connect, errorcode


USER = 'root'
PASSWORD = 'admin'
DB = 'course_management'

CREATE_DATABASE_USER = """
            CREATE TABLE IF NOT EXISTS user(
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(255),
                email VARCHAR(255)
            )
            """

CREATE_DATABASE_COURSE = """
            CREATE TABLE IF NOT EXISTS course(
                id INT AUTO_INCREMENT PRIMARY KEY,
                title VARCHAR(255),
                description TEXT NOT NULL,
                start_data DATE,
                end_date DATE
            )
            """

CREATE_DATABASE_USER_COURSE = """
            CREATE TABLE IF NOT EXISTS user_course(
                id INT AUTO_INCREMENT PRIMARY KEY,
                user_id INT,
                course_id INT,
                enrollment_data DATE,
                FOREIGN KEY (user_id) REFERENCES user(id),
                FOREIGN KEY (course_id) REFERENCES course(id)                
            )
            """

CREATE_DATABASE_USER_PROFILE = """
            CREATE TABLE IF NOT EXISTS user_profile(
                id INT AUTO_INCREMENT PRIMARY KEY,
                user_id INT NOT NULL,
                registration_date DATE,
                first_name VARCHAR(100),
                last_name VARCHAR(100),
                address VARCHAR(255),
                phone_number VARCHAR(20),
                FOREIGN KEY (user_id) REFERENCES user(id) 
            )
            """


try:
    with connect(user=USER, password=PASSWORD, database=DB) as cnx:
        with cnx.cursor() as cursor:
            cursor.execute(CREATE_DATABASE_USER)
            cursor.execute(CREATE_DATABASE_COURSE)
            cursor.execute(CREATE_DATABASE_USER_COURSE)
            cursor.execute(CREATE_DATABASE_USER_PROFILE)

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