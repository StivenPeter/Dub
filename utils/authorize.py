import hashlib
import sqlite3


def hashOG(x):
	h = hashlib.sha256()
	h.update(x)
	return h.hexdigest()

def createAccount(fn, ln, usern, unhashedp):
	f = "data.db"
	db = sqlite3.connect(f)
	og = db.cursor()
	insert = "INSERT INTO users2 VALUES ('%s', '%s', '%s', '%s')"%(fn, ln, usern, hashOG(unhashedp))
	og.execute(insert)
	db.commit()
	db.close()

def checkLogin(userN, pw):
	f = "data.db"
	db = sqlite3.connect(f)
	og = db.cursor()
	s = "SELECT username, password FROM users WHERE username == userN;"
	t = og.execute(s)
	hashed = hashOG(pw)
	for record in t:
		if record[1] == hashed:
			db.close()
    		return True
	db.close()



def checkRegister(userN):
	f = "data.db"
	db = sqlite3.connect(f)
	og = db.cursor()
	s = "SELECT username FROM users"
	t = og.execute(s)
	for record in t:
		if record[0] == userN:
    		#username already taken
			return False 
	return True

