import mysql.connector
from mysql.connector import connect, errorcode

USER = 'root'
PASSWORD = 'admin'
DB = 'course_management'

USER_ADD = """
            INSERT INTO user (username, email) VALUES
                ('john_doe', 'john@example.com'),
                ('jane_smith', 'jane@example.com'),
                ('mike_jones', 'mike@example.com'),
                ('emily_white', 'emily@example.com'),
                ('alex_brown', 'alex@example.com')  
            """

COURSE_ADD = """
            INSERT INTO course (title, description, start_data, end_date) VALUES
                ('Matematyka podstawowa ','Kurs z podstaw matematyki dla początkujących.','2024-01-01','2024-03-01'),
                ('Historia sztuki','Wprowadzenie do historii sztuki i jej głównych nurtów.','2024-02-15','2024-05-15'),
                ('Programowanie w języku Python','Kurs programowania w języku Python dla początkujących.','2024-03-10','2024-06-10'),
                ('Angielski dla zaawansowanych ','Kurs angielskiego dla osób posługujących się językiem na poziomie zaawansowanym.','2024-04-01','2024-07-01'),
                ('Marketing internetowy','Omówienie podstawowych technik marketingu w internecie.','2024-05-15','2024-08-15')
            """

USER_COURSE_ADD = """
            INSERT INTO user_course (user_id, course_id, enrollment_data) VALUES
                (1,1,'2024-01-20'),
                (1,3,'2024-03-15'),
                (2,2,'2024-02-25'),
                (3,4,'2024-04-10'),
                (4,5,'2024-05-20'),
                (5,3,'2024-03-20'),
                (5,5,'2024-06-01')
            """

ADD_USER_PROFILE = """
            INSERT INTO user_profile (user_id, first_name, last_name, address, phone_number, registration_date) VALUES
            (1,'John','Doe','123 Main St, Anytown','555-1234','2023-01-15'),
            (2,'Jane','Smith','456 Oak St, Anycity','555-5678','2023-02-20'),
            (3,'Mike','Jones','789 Elm St, Anycity','555-9012','2023-03-10'),
            (4,'Emily','White','101 Pine St, Anytown','555-3456','2023-04-05'),
            (5,'Alex','Brown','202 Maple St, Anycity','555-7890','2023-05-12')
            """

try:
    with connect(user=USER, password=PASSWORD, database=DB) as cnx:
        with cnx.cursor() as cursor:
            cursor.execute(USER_ADD)
            cursor.execute(COURSE_ADD)
            cursor.execute(USER_COURSE_ADD)
            cursor.execute(ADD_USER_PROFILE)
            cnx.commit()

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