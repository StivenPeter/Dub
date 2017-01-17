import hashlib
import sqlite3

#CREATE TABLE users2 (fname TEXT, lname TEXT, username TEXT, hashedpassword TEXT);

def hashOG(x):
	h = hashlib.sha256()
	h.update(x)
	return h.hexdigest()

def createAccount(fn, ln, usern, unhashedp):
	f = "data/data.db"
	db = sqlite3.connect(f)
	og = db.cursor()
	insert = "INSERT INTO users2 VALUES ('%s', '%s', '%s', '%s')"%(fn, ln, usern, hashOG(unhashedp))
	og.execute(insert)
	db.commit()
	db.close()

def checkLogin(userN, pw):
	hashed = hashOG(pw)
	f = "data/data.db"
	db = sqlite3.connect(f)
	og = db.cursor()
	s = "SELECT username, hashedpassword FROM users2 WHERE username =='" + userN + "';"
	t = og.execute(s)
	for record in t:
		if record[1] == hashed:
			print "hi"
    			db.close()
    			return True	
    		else:
    			print "hello"
    			db.close()
    			return False
	print "hi"
	db.close()
	return False



def checkRegister(userN):
	f = "data/data.db"
	db = sqlite3.connect(f)
	og = db.cursor()
	s = "SELECT username FROM users2"
	t = og.execute(s)
	for record in t:
		if record[0] == userN:
    		#username already taken
			return False 
	return True

