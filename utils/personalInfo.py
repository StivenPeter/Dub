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

def getInterestList(username):
        userData=getData(username)
        data=[]
        for x in range(1, 4):
    		if userData[x] == "bio":
    			data.append("Biology")
    		if userData[x] == "chem":
    			data.append("Chemistry")
    		if userData[x] == "math":
    			data.append("Math")
    		if userData[x] == "history":
    			data.append("History")
    		if userData[x] == "physics":
    			data.append("Physics")
    		if userData[x] == "compsci":
    			data.append("Computer Science")
    		if userData[x] == "art":
    			data.append("Art")
    		if userData[x] == "music":
    			data.append("Music")
    		if userData[x] == "travel":
    			data.append("Travel")
    		if userData[x] == "popcult":
    			data.append("Pop Culture")
    		if userData[x] == "sports":
    			data.append("Sports")
    		if userData[x] == "lit":
    			data.append("Literature")
    		if userData[x] == "food":
    			data.append("Food")
    		if userData[x] == "pol":
    			data.append("Politics")
    		if userData[x] == "fem":
    			data.append("Feminism")
    		if userData[x] == "memes":
    			data.append("Memes")
        #print data
        return data

# def getIntrestList(username):
#         userData=getData(username)
#         data=[]
#         data.append(userData[1])
#         data.append(userData[2])
#         data.append(userData[3])
#         return data

# def getHobbyList(username):
#         userData=getData(username)
#         data=[]
#         data.append(userData[13])
#         data.append(userData[14])
#         data.append(userData[15])
#         return data

def getHobbiesForEvents(username):
    userData=getData(username)
    li = []
    li.append(userData[13])
    li.append(userData[14])
    li.append(userData[15])
    return li

def getHobbyList(username):
        userData=getData(username)
        hobbies = ['gaming','anime', 'comedy', 'eating', 'bike', 'hike', 'walks', 'hacking', 'music', 'instrument', 'sleeping', 'reading', 'sports', 'drama', 'animals', 'culinary', 'knitting', 'diy', 'concerts']
        hobbies2 = ['Gaming', 'Watching Anime', 'Watching Comedy TV', 'Eating', 'Biking', 'Hiking', 'Taking Walks', 'Hacking', 'Listening to Music', 'Playing an Instrument', 'Sleeping', 'Reading', 'Playing Sports', 'Watching Drama T.V.', 'Playing with Animals', 'Cooking/Baking', 'Knitting', 'DIY', 'Going to Concerts']
        indexes = []
        data = []
        for x in range(13,16):
            indexes.append(hobbies.index(userData[x]))
        for i in indexes:
            data.append(hobbies2[i])
        #print data
        return data


def getPolitic(username):
    userData=getData(username)
    politics = ['fiscalCon', 'mainCons', 'liberal', 'socCon', 'moderate', 'socialist', 'libertarian', 'green', 'na']
    politics2= ['Fiscal Conservative', 'Mainstream Conservative', 'Liberal', 'Social Conservative', 'Moderate', 'Socialist', 'Libertarian', 'Green Party', ' ']
    userData = getData(username)
    i = politics.index(userData[16])
    return politics2[i]


def getBig(username):
        bigthings = ['loyal', 'stable', 'laugh', 'intel', 'sex', 'emo', 'spont', 'study']
        bigthings2 = ['Loyalty', 'Stability', 'Laughter', 'Intellectual Stimulation', 'Sex', 'A Deep Emotional Connection', 'Spontaneity', 'A Study Buddy']
        userData=getData(username)
        i = bigthings.index(userData[4])
        return bigthings2[i]

def getZip(username):
        userData=getData(username)
        return userData[5]

def getGender(username):
    userData=getData(username)
    if userData[6] == 'woman':
        return "Female"
    if userData[6] == 'man':
        return "Male"
    if userData[6] == 'noncomforming':
        return "Agender"
    return userData[6]

def getInterest(username):
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
        if userData[10] == 'christ':
        	return "Christian"
        if userData[10] == 'cath':
        	return  "Catholic"
        if userData[10] == 'prot':
        	return "Protestant"
        if userData[10] == 'shi':
        	return "Shi'a"
        if userData[10] == 'sunni':
        	return "Sunni"
        if userData[10] == 'jewish':
        	return "Jewish"
        if userData[10] == 'atheist':
        	return "Atheist" 
        if userData[10] == 'agno':
        	return "Agnostic"
        if userData[10] == 'hind':
        	return "Hindu"
        if userData[10] == 'budd':
        	return "Buddhist"
        if userData[10] == 'baha':
        	return "Bahaist"
        if userData[10] == 'EO':
        	return "Eastern Orthodox"
        if userData[10] == 'na':
        	return " "
        return userData[10]


def getJob(username):
        userData=getData(username)
        jobs = ['acct', 'exec', 'manu', 'admin', 'franch', 'nonp', 'bank', 'gov', 'pt', 'busi', 'HC', 'retail', 'contract', 'student', 'sales','cust', 'HR', 'sci', 'diversity', 'IT', 'trans','eng', 'internships']
        jobs2 = ['Accounting', 'Executive', 'Manufacturing', 'Administration', 'Franchise', 'Nonprofit', 'Banking', 'Government', 'Part Time', 'Business', 'Health Care', 'Retail', 'Contracting and Freelance', 'Student', 'Sales', 'Customer Service', 'Human Resources', 'Science and Biotech', 'Diversity Opportunities', 'Information Technology', 'Transportation', 'Engineering', 'Internships and College']
        return jobs2[jobs.index(userData[11])]

def getReligiousPartner(username):
        userData=getData(username)
        return userData[9]

def getPoliticPartner(username):
        userData=getData(username)
        return userData[12]

def getName(username):
	string = ""
	f = "data/data.db"
	db = sqlite3.connect(f)
	og = db.cursor()
	blob = "SELECT fname, lname FROM users2 WHERE username=='%s'"%(username)
	t = og.execute(blob)
	for item in t:
		string = string + item[0] + ' ' + item[1]
	return string



def getRouteForPfp(username):
	f = "data/data.db"
	db = sqlite3.connect(f)
	og = db.cursor()
	command = "SELECT pfp FROM users WHERE username='%s'"%(username)
	t = og.execute(command)
	for item in t:
		returnRoute= item
	return returnRoute

def getCardInfo(username):
	info = []
	info.append(getName(username))
	info.append(getAge(username) + " year old")
	info.append(getGender(username))
	info.append(getPolitic(username))
	info.append(getBig(username))
	info.append(getReligion(username))
	info.append(getInterestList(username))
	info.append(getHobbyList(username))
	info.append(getJob(username))
	path = "../" + getRouteForPfp(username)[0]
	info.append(path)
	return info

def addprofile(username, filename):
	f = "data/data.db"
	db = sqlite3.connect(f)
	sp = db.cursor()
	path =  path = "static/pfp/" + filename
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
	for item in prevfile:
		prevfilepath = item
	db.commit()
	db.close()
	if (getprev != 'static/pfp/default.png'):
		os.remove(prevfilepath)


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


def getGenderRaw(username):
    userData=getData(username)
    return userData[6]


def getReligionRaw(username):
    userData=getData(username)
    return userData[10]

def getJobRaw(username):
    userData=getData(username)
    return userData[11]


def getPoliticRaw(username):
    
    userData=getData(username)
    return userData[16]


def getBigRaw(username):
    userData=getData(username)
    return userData[4]


def getInterestListRaw(username):
    userData=getData(username)
    data=[]
    data.append(userData[1])
    data.append(userData[2])
    data.append(userData[3])
    return data

def getHobbyListRaw(username):
    userData=getData(username)
    data=[]
    data.append(userData[13])
    data.append(userData[14])
    data.append(userData[15])
    return data

#getRouteForPfp('L')
#print getIntrestList('billy123')
#print getName("jb7")


