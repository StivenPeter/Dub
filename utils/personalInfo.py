import hashlib
import sqlite3



#CREATE TABLE users (username TEXT, interest1 TEXT, 
#interest2 TEXT, interest3 TEXT, bigthing TEXT, 
#zipcode TEXT, gender TEXT, age TEXT, gendpref TEXT, 
#religionpref TEXT, myreligion TEXT, job TEXT, 
#politicalpref TEXT, hobby1 TEXT, hobby2 TEXT, hobby3 TEXT, 
#mypolitics TEXT, agediff TEXT);

def addEntry(username, interestList, bigthing, zipcode, gender, age, gendpref, religionpref,myreligion, job, politicalpref, hobbies, mypolitics, agediff):
	f = "data.db"
	db = sqlite3.connect(f)
	og = db.cursor()
	interest1 = interestList[0]
	interest2 = interestList[1]
	interest3 = interestList[2]
	hobby1 = hobbies[0]
	hobby2 = hobbies[1]
	hobby3 = hobbies[2]
	insert = "INSERT INTO users VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s','%s', '%s')"%(username, interest1, interest2, interest3, bigthing, zipcode, gender, age, gendpref, religionpref, myreligion, job, politicalpref, hobby1, hobby2, hobby3, mypolitics, agediff)
	og.execute(insert)
	db.commit()
	db.close()
	return True


