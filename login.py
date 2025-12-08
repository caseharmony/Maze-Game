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

def signup(username,password):
    cur.execute("INSERT INTO login VALUES(%s,%s)",(username,bcrypt.hashpw(password.encode("utf-8"),bcrypt.gensalt())))
    db.commit()

print(login('admin','admin123'))
cur.execute("DELETE FROM login")
cur.execute("SELECT * FROM login")
print(cur.fetchall())
