import hashlib
import sqlite3
import os


#CREATE TABLE users (username TEXT, interest1 TEXT, 
#interest2 TEXT, interest3 TEXT, bigthing TEXT, 
#zipcode TEXT, gender TEXT, age TEXT, gendpref TEXT, 
#religionpref TEXT, myreligion TEXT, job TEXT, 
#politicalpref TEXT, hobby1 TEXT, hobby2 TEXT, hobby3 TEXT, 
#mypolitics TEXT, agediff TEXT, pfp TEXT);

def addEntry(username, interestList, bigthing, zipcode, gender, age, gendpref, religionpref,myreligion, job, politicalpref, hobbies, mypolitics, agediff):
	f = "data/data.db"
	db = sqlite3.connect(f)
	og = db.cursor()
	interest1 = interestList[0]
	interest2 = interestList[1]
	interest3 = interestList[2]
	hobby1 = hobbies[0]
	hobby2 = hobbies[1]
	hobby3 = hobbies[2]
	insert = "INSERT INTO users VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s','%s', '%s','')"%(username, interest1, interest2, interest3, bigthing, zipcode, gender, age, gendpref, religionpref, myreligion, job, politicalpref, hobby1, hobby2, hobby3, mypolitics, agediff)
	og.execute(insert)
	db.commit()
	db.close()
	return True

def getData(username):
	f = "data/data.db"
	db = sqlite3.connect(f)
	c = db.cursor()
	checkUser = "SELECT * FROM users WHERE username==?"
	c.execute(checkUser, (username,))
	r = c.fetchone()
	db.commit()
	db.close()
	return r

def getIntrestList(username):
        userData=getData(username)
        data=[]
        data.append(userData[1])
        data.append(userData[2])
        data.append(userData[3])
        return data

def getHobbyList(username):
        userData=getData(username)
        data=[]
        data.append(userData[13])
        data.append(userData[14])
        data.append(userData[15])
        return data

def getPolitic(username):
        userData=getData(username)
        return userData[16]

def getBig(username):
        userData=getData(username)
        return userData[4]

def getZip(username):
        userData=getData(username)
        return userData[5]

def getGender(username):
        userData=getData(username)
        return userData[6]

def getIntrest(username):
        userData=getData(username)
        return userData[8]

def getAge(username):
        userData=getData(username)
        return userData[7]

def getAgeDif(username):
        userData=getData(username)
        return userData[17]

def getReligion(username):
        userData=getData(username)
        return userData[10]

def getJob(username):
        userData=getData(username)
        return userData[11]

def getReligiousPartner(username):
        userData=getData(username)
        return userData[9]

def getPoliticPartner(username):
        userData=getData(username)
        return userData[12]
        



def getRouteForPfp(username):
	f = "data/data.db"
	db = sqlite3.connect(f)
	og = db.cursor()
	command = "SELECT pfp FROM users WHERE username='%s'"%(username)
	t = og.execute(command)
	for item in t:
		returnRoute= item
	return returnRoute


def addprofile(username, filename):
	f = "data/data.db"
	db = sqlite3.connect(f)
	sp = db.cursor()
	path =  path = "static/pfp/" + filename
	print "path:  " + path
	insert = "UPDATE users SET pfp='%s' WHERE username= '%s'"%(path, username)
	sp.execute(insert)
	db.commit()
	db.close()
	return True

def deletedup():
	f = "data/data.db"
	db = sqlite3.connect(f)
	sp = db.cursor()
	delete = "DELETE FROM users WHERE rowid NOT IN (SELECT min(rowid) FROM users GROUP BY username)"
	sp.execute(delete)
	db.close()
	return True

def changeProfile(username, filename):
	deleteProfile(username)
	addprofile(username,filename)

def deleteProfile(username):
	f = "data/data.db"
	db = sqlite3.connect(f)
	sp = db.cursor()
	getprev = "SELECT pfp FROM users WHERE username='%s'"%(username)
	prevfile = sp.execute(getprev)
	db.commit
	db.close()
	if (getprev != 'static/pfp/default.png'):
		os.remove(prevfile)


def changeSettings(username, interestList, bigthing, zipcode, gender, age, gendpref, religionpref, myreligion, job, politicalpref, hobbies, mypolitics, agediff):
	f = "data/data.db"
	db = sqlite3.connect(f)
	sp = db.cursor()
	interest1 = interestList[0]
	interest2 = interestList[1]
	interest3 = interestList[2]
	hobby1 = hobbies[0]
	hobby2 = hobbies[1]
	hobby3 = hobbies[2]
	insert = " UPDATE users SET interest1 = '%s', interest2='%s', interest3 = '%s', bigthing = '%s', zipcode = '%s', gender = '%s', age = '%s', gendpref = '%s', religionpref = '%s', myreligion = '%s', job = '%s', politicalpref = '%s', hobby1 = '%s', hobby2 = '%s', hobby3 = '%s', mypolitics = '%s', agediff = '%s' WHERE username = '%s'"%(interest1, interest2, interest3, bigthing, zipcode, gender, age, gendpref, religionpref, myreligion, job, politicalpref, hobby1, hobby2, hobby3, mypolitics, agediff, username)
	sp.execute(insert)
	db.commit()
	db.close()
	return True


#getRouteForPfp('L')
#print getIntrestList('billy123')



