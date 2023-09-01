from peewee import MySQLDatabase

from config import MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PASSWORD, MYSQL_NAME

database = MySQLDatabase(
    database=MYSQL_NAME,
    user=MYSQL_USER,
    password=MYSQL_PASSWORD,
    host=MYSQL_HOST,
    port=MYSQL_PORT,
    charset='utf8mb4',
    autoconnect=True
)


