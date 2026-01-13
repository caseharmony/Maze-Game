import bcrypt
import mysql.connector as mc
password="x"
if password=="x":
    db=mc.connect(host="localhost",user="root",password="sql123")
    cur=db.cursor()
    sql_script = """
    CREATE DATABASE IF NOT EXISTS amazeing;
    USE amazeing;
    CREATE TABLE IF NOT EXISTS login(
        gamertag VARCHAR(50),
        password BLOB,
        firstname VARCHAR(50),
        lastname VARCHAR(50),
        email VARCHAR(50)
    );
    """
    cur.execute(sql_script)
    db.commit()
    db.close()
    db=mc.connect(host="localhost",user="root",password="sql123",database="amazeing")
    cur=db.cursor()
else:
    config = {
    "user": "amazeing_involvedbe",
    "password": password,
    "host": "7ax81r.h.filess.io",
    "port": 3307,
    "database": "amazeing_involvedbe"
    }
    db=mc.connect(**config)
    cur=db.cursor()

def login(username,password):
    db.ping(reconnect=True)
    cur.execute("SELECT * FROM login")
    logindb=list(cur.fetchall())
    try:
        check=bcrypt.checkpw(password.encode("utf-8"),logindb[list(map(lambda item: item[0],logindb)).index(username)][1])
        return check
    except:
        return False

def signup(username,password,firstname,lastname,email):
    db.ping(reconnect=True)
    cur.execute("SELECT * FROM login")
    logindb=list(cur.fetchall())
    for i in logindb:
        if username == i[0]:
            return False
    password=bcrypt.hashpw(password.encode("utf-8"),bcrypt.gensalt())
    cur.execute("INSERT INTO login (gamertag, password, firstname, lastname, email) VALUES (%s, %s, %s, %s, %s)", (username,password,firstname,lastname,email))
    db.commit()
    return True

#FUNCTIONS FOR SAVE FILES

def importsave(username,name):
    cur.execute(f"SELECT * FROM {username}")
    saves=dict(cur.fetchall())
    file=saves[name]
    return file

def savefile(username):
    db.ping(reconnect=True)
    cur.execute(f"CREATE TABLE IF NOT EXISTS {username} (name VARCHAR(50), file MEDIUMTEXT)")
    db.commit()
    cur.execute(f"SELECT name FROM {username}")
    return [row[0] for row in cur.fetchall()]

def exportsave(username, name, file):
    db.ping(reconnect=True)
    cur.execute(f"SELECT * FROM {username}")
    savedb=list(cur.fetchall())
    for i in savedb:
        if name == i[0]:
            return False
    cur.execute(f"INSERT INTO {username} (name, file) VALUES (%s, %s)", (name, file))
    db.commit()
    return True


