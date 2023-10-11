from dotenv import dotenv_values
import psycopg2

config = dotenv_values(".env")

host = config["HOST"]
port = config["PORT"]
user = config["USER_ID"]
password = config["USER_PW"]
database = config["DB_NAME"]

try:
    connection = psycopg2.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database=database
    )

    connection.autocommit = True


    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         '''
    #             CREATE TABLE project (
    #                 ID INT PRIMARY KEY ,
    #                 NAME VARCHAR(50) NOT NULL ,
    #                 description VARCHAR(255) NOT NULL
    #             );
    #         '''
    #     )

    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         '''
    #             INSERT INTO project (id, name, description)
    #             VALUES
    #             (1, 'project1', 'project1 description'),
    #             (2, 'project2', 'project2 description'),
    #             (3, 'project3', 'project3 description');
    #         '''
    #     )

    with connection.cursor() as cursor:
        cursor.execute(
        '''
                 INSERT INTO project (id, name, description)
                 VALUES (%s, %s, %s);
            ''',
        (4, 'project4', 'project4 description')
        )


    # with connection.cursor() as cursor:
    #     cursor.execute(
    # '''
    #         INSERT INTO project (id, name, description)
    #         VALUES (%s, %s, %s), (%s, %s, %s);
    #     ''',
    #     [(5, 'project5', 'project5 description'),
    #             (6, 'project6', 'project6 description')]
    #     )


    with connection.cursor() as cursor:
        cursor.execute(
            '''
                SELECT * FROM project;
            '''
        )

        # for line in cursor.fetchall():
        #     print(line)

        # print(cursor.fetchone())
#
        for line in cursor.fetchall():
            print(f'ID: {line[0]}')
            print(f'Name: {line[1]}')
            print(f'Description: {line[2]}')
            print(f'TimeStamp: {line[3]}')
            print()

    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         '''
    #             ALTER TABLE project
    #             ADD COLUMN created_on timestamp NOT NULL DEFAULT now();
    #         '''
    #     )


    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         '''
    #             update project
    #             set description = 'new desc'
    #             where name = 'project1';
    #         '''
    #     )

    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         '''
    #             delete from project
    #             where name = 'project4';
    #         '''
    #     )



    connection.close()

except Exception as e:
    print(e)
