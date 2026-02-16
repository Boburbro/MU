# This script creates a MySQL database and user using environment variables from .env
import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv(os.path.join(os.path.dirname(__file__), "../.env"))

MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_DB = os.getenv("MYSQL_DB")

# Connect as root or admin user to create db/user
admin_user = "root"  # Change if needed
admin_password = ""  # Set your root password here

conn = mysql.connector.connect(
    host=MYSQL_HOST, user=admin_user, password=admin_password
)
cursor = conn.cursor()

# Create database
cursor.execute(f"CREATE DATABASE IF NOT EXISTS {MYSQL_DB}")
# Create user and grant privileges
cursor.execute(
    f"CREATE USER IF NOT EXISTS '{MYSQL_USER}'@'%' IDENTIFIED BY '{MYSQL_PASSWORD}'"
)
cursor.execute(f"GRANT ALL PRIVILEGES ON {MYSQL_DB}.* TO '{MYSQL_USER}'@'%'")
cursor.execute("FLUSH PRIVILEGES")

print(f"Database {MYSQL_DB} and user {MYSQL_USER} created/updated.")
cursor.close()
conn.close()
