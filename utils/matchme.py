import hashlib
import sqlite3



##OG's rad matching algo: certain preferences will be "red flags" and all matches are required to have one interest/hobby in common
#username    interest1   interest2   interest3   bigthing    zipcode     gender      age         gendpref    religionpref  myreligion  job         politicalpref  hobby1      hobby2      hobby3      mypolitics  agediff     pfp       
#----------  ----------  ----------  ----------  ----------  ----------  ----------  ----------  ----------  ------------  ----------  ----------  -------------  ----------  ----------  ----------  ----------  ----------  ----------

def isAnInterest(key):
    if key == "bio" or key =="chem" or key == "math" or key =="history" or key=="physics" or key=="compsci" or key=="art" or key=="music" or key=="travel" or key=="popcult" or key=="sports" or key=="lit" or key=="food" or key=="pol" or key=="fem" or key=="memes":
        return True
    return False


def isAHobby(key):
    if key == "gaming" or key =="anime" or key == "comedy" or key =="eating" or key=="bike" or key=="hike" or key=="walks" or key=="hacking" or key=="music" or key=="instrument" or key=="sleeping" or key=="reading" or key=="sports" or key=="drama" or key=="animals" or key=="culinary" or key=="knitting" or key=="diy" or key=="concerts":
        return True
    return False



def findMyPreferences(username):
	f = "data/data.db"
	db = sqlite3.connect(f)
	og = db.cursor()
	command = "SELECT * FROM users WHERE username=='%s'" %(username)
	x = og.execute(command)
	dic = {}
	#print x[1]
	for item in x:
		dic['username'] = item[0]
		dic['interests'] = [item[1], item[2], item[3]]
		dic['bigthing'] = item[4]
		dic['zipcode'] = item[5]
		dic['gender'] = item[6]
		dic['age'] = item[7]
		dic['gendpref'] = item[8]
		dic['religionpref'] = item[9]
		dic['myreligion'] = item[10]
		dic['job'] = item[11]
		dic['politicalpref'] = item[12]
		dic['hobbies'] = [item[13], item[14], item[15]]
		dic['mypolitics'] = item[16]
		dic['agediff'] = item[17]
	return dic		

#each item has 18 subitems (includes pfp)
#0 username/
#1interest1/
#2interest2/
#3interest3   
#4bigthing    
#5zipcode     
#6gender      
#7age         
#8gendpref    
#9religionpref  
#10myreligion  
#11job         
#12politicalpref  
#13hobby1      
#14hobby2      
#15hobby3      
#16mypolitics  
#17agediff     
#18pfp  
# dic['username'] = item[0]
# dic['interests'] = [item[1], item[2], item[3]]
# dic['bigthing'] = item[4]
# dic['zipcode'] = item[5]
# dic['gender'] = item[6]
#  dic [age ] =7
# dic['gendpref'] = item[8]
# dic['religionpref'] = item[9]
# dic['myreligion'] = item[10]
# dic['job'] = item[11]
# dic['politicalpref'] = item[12]
# dic['hobbies'] = [item[13], item[14], item[15]]
# dic['mypolitics'] = item[16]
# dic['agediff'] = item[17]

def genderMatching(gender1, genderpref1, gender2, genderpref2):
	print "hi from gender matching"
	if gender1 == 'nonconform' or gender2=='nonconform':
		if gender1=='nonconform':
			if genderpref2 == 'nopref':
				if genderpref1 =='both':
					return (gender2 == 'woman' or gender2=='man')
				elif genderpref1 == 'nopref':
					return True
				else:
					return (genderpref1==gender2)
			else:
				return False
		if gender2=='nonconform':
			if genderpref1 == 'nopref':
				if genderpref2 =='both':
					return (gender1 == 'woman' or gender1=='man')
				elif genderpref2 == 'nopref':
					return True
				else:
					return (genderpref2==gender1)
			else:
				return False
	else:
		if (genderpref1 =='both' or genderpref2 =='both'):
			if genderpref1=='both':
				if gender2 == 'woman' or gender2 == 'man':
					if genderpref2 == 'both':
						return (gender1=='woman' or gender1 =='man')
					else:
						return (gender1==genderpref2)
			if genderpref2=='both':
				if gender1 == 'woman' or gender1 == 'man':
					if genderpref1 == 'both':
						return (gender2=='woman' or gender2 =='man')
					else:
						return (gender2==genderpref1)
		else:
			return (genderpref1 == gender2 and genderpref2 == gender1)


def politics(polview1, polpref1, polview2, polpref2):
	#if either person gives a shit:
	if ( int(polpref1) >= 1 and int(polpref1) <= 5 ) or ( int(polpref2) >= 1 and int(polpref2) <= 5 ):
		if (polview1 == polview2):
			return True
		else:
			return False
	else:
		return True

def religion(religion1, religionpref1, religion2, religionpref2):
	#if either person gives a shit:
	if ( int(religionpref1) >= 1 and int(religionpref1) <= 5 ) or ( int(religionpref2) >= 1 and int(religionpref2) <= 5 ):
		if (religion1 == religion2):
			return True
		else:
			return False
	else:
		return True

def anythingInCommon(list1, list2):
	for item in list1:
		if item in list2:
			return True
	return False


def conflicts(bigthing1, bigthing2):
	if ( bigthing1 == 'sex' and bigthing2 == 'emo' ):
		return False
	if ( bigthing1== 'spont' and bigthing2 == 'stable' ):
		return False
	if ( bigthing1=='study' and bigthing2== 'sex' ):
		return False
	else:
		return True



def findMatches(username):
	f = "data/data.db"
	db = sqlite3.connect(f)
	og = db.cursor()
	UD = findMyPreferences(username)
	matches = []
	command = "SELECT * from users WHERE username !='%s'"%(username)
	x = og.execute(command)
	for item in x:
		#print "item " + str(item[0])
		#print item[6]
		#print item[8]
		#print UD['gender']
		#print UD['gendpref']
	##~~RED FLAG REGION~~##	
		##GENDER PREFERENCES
		print genderMatching(str(item[6]), str(item[8]), str(UD['gender']), str(UD['gendpref']))
		if genderMatching(str(item[6]), str(item[8]), str(UD['gender']), str(UD['gendpref'])):
			print "passed gender"
			##agE DIFFERENCE
			if ( int(UD['age']) + int(UD['agediff']) >= int(item[7]) and int(UD['age']) - int(UD['agediff']) <= int(item[7])):		
				print "passed age"	
				##POLTICS
				if politics(UD['mypolitics'], UD['politicalpref'], item[16], item[12]):			
					##RELIGION
					if religion(UD['myreligion'], UD['religionpref'], item[10], item[9]):
						##~~Yellow flag region - must have SoMeThInG in common!~~##
						newlis = [UD['interests']]
						newlis.extend(UD['hobbies'])
						print newlis
						if anythingInCommon(newlis, [item[1], item[2], item[3], item[13], item[14], item[15]]):
							#dont want a sex freak w someone lookin for a deep connection
							if (conflicts(item[4], UD['bigthing'])):
								matches.append(item[0])
	#print "hi"
	if len(matches) == 0:
		return "No Matches Found!"
	else:
		return matches



#testing
#findMyPreferences("statefarm")
#findMatches("statefarm")
#print genderMatching('woman', 'woman', 'woman', 'man')
#print genderMatching('woman', 'woman', 'woman', 'man')
#print genderMatching('woman', 'man', 'man', 'man')
#print genderMatching('woman', 'man', 'man', 'woman')
#print genderMatching('woman', 'woman', 'woman', 'man')







