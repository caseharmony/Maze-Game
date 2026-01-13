import mysql.connector as mc
db=mc.connect(host="localhost",user="root",password="sql123",database="amazeing")
cur=db.cursor()
sql_script = """
DROP DATABASE IF EXISTS amazeing;
CREATE DATABASE amazeing;
USE amazeing;

CREATE TABLE login(
    gamertag VARCHAR(50),
    password BLOB,
    firstname VARCHAR(50),
    lastname VARCHAR(50),
    email VARCHAR(50)
);
"""
cur.execute(sql_script)
cur.execute("commit")