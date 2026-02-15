import bcrypt
import mysql.connector as mc
import os
password=os.getenv('DB_KEY')
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

def savefile(username):
    db.ping(reconnect=True)
    query = "SELECT savename FROM saves WHERE username = %s"
    cur.execute(query, (username,))
    return [row[0] for row in cur.fetchall()]

def importsave(username, name):
    db.ping(reconnect=True)
    query = "SELECT file FROM saves WHERE username = %s AND savename = %s"
    cur.execute(query, (username, name))
    result = cur.fetchone()
    return result[0] if result else None

def exportsave(username, name, file):
    db.ping(reconnect=True)
    query = """
        INSERT INTO saves (username, savename, file) 
        VALUES (%s, %s, %s)
        ON DUPLICATE KEY UPDATE file = VALUES(file)
    """
    cur.execute(query, (username, name, file))
    db.commit()

def closedb():
    cur.close()
    db.close()
