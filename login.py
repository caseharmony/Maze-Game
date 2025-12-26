import bcrypt
import mysql.connector as mc

db=mc.connect(host="localhost",user="root",password="sql123",database="amazeing")
cur=db.cursor()
cur.execute("commit")
def login(username,password):
    cur.execute("SELECT * FROM login")
    logindb=list(cur.fetchall())
    try:
        check=bcrypt.checkpw(password.encode("utf-8"),logindb[list(map(lambda item: item[0],logindb)).index(username)][1])
        return check
    except:
        return False

def signup(username,password,firstname,lastname,email):
    password=bcrypt.hashpw(password.encode("utf-8"),bcrypt.gensalt())
    cur.execute("INSERT INTO login (gamertag, password, firstname, lastname, email) VALUES (%s, %s, %s, %s, %s)", (username,password,firstname,lastname,email))
    db.commit()
