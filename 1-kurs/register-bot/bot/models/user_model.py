from config import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB
import mysql.connector


def upsert_user(
    user_id: int, full_name: str, username: str, surname=None, age=None, email=None
):
    conn = mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DB,
        autocommit=True,
    )
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id BIGINT PRIMARY KEY,
            full_name VARCHAR(255),
            username VARCHAR(255),
            surname VARCHAR(255),
            age INT,
            email VARCHAR(255)
        )
        """
    )
    cur.execute(
        """
        INSERT INTO users (id, full_name, username, surname, age, email)
        VALUES (%s, %s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE 
            full_name=VALUES(full_name), 
            username=VALUES(username),
            surname=VALUES(surname),
            age=VALUES(age),
            email=VALUES(email)
        """,
        (user_id, full_name, username, surname, age, email),
    )
    conn.commit()
    cur.close()
    conn.close()
