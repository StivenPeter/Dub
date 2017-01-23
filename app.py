from flask import Flask, render_template, request, session, redirect, url_for
import urllib2, os
import hashlib
import time
from utils import authorize, personalInfo, matchme
#from utils import users
from werkzeug.utils import secure_filename

#from flask_bootstrap import Bootstrap
#from utils import

#Bootstrap(app)
#app.secret_key = os.urandom(10)
UPLOAD_FOLDER="static/pfp"
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
message = ""

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


app.secret_key = "ajbddwhdajwwwwajfbsaiwfbsakqk72884bd"

def numberToMonth(num):
	if (num == 1):
		return "January"
	if (num == 2):
		return "February"
	if (num == 3):
		return "March"
	if (num == 4):
		return "April"
	if (num == 5):
		return "May"
	if (num == 6):
		return "June"
	if (num == 7):
		return "July"
	if (num == 8):
		return "August"
	if (num == 9):
		return "September"
	if (num == 10):
		return "October"
	if (num == 11):
		return "November"
	if (num == 12):
		return "December"

def aujourdhui():
	retstr = ""
	datelist = time.localtime()
	year = str(datelist[0])
	month = numberToMonth(datelist[1])
	day = str(datelist[2])
	retstr = month + " " + day + ", " + year
	return retstr
	#for item in time.localtime():
		


def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

def upload_file(f):
	file = f['upload']
	filename = "default.png"
	if file.filename == '':
		return filename
	try:
		filename = secure_filename(file.filename)
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
	except IOError:
		return filename
	return filename



def isAnInterest(key):
	if key == "bio" or key =="chem" or key == "math" or key =="history" or key=="physics" or key=="compsci" or key=="art" or key=="music" or key=="travel" or key=="popcult" or key=="sports" or key=="lit" or key=="food" or key=="pol" or key=="fem" or key=="memes":
		return True
	return False


def isAHobby(key):
	if key == "gaming" or key =="anime" or key == "comedy" or key =="eating" or key=="bike" or key=="hike" or key=="walks" or key=="hacking" or key=="music" or key=="instrument" or key=="sleeping" or key=="reading" or key=="sports" or key=="drama" or key=="animals" or key=="culinary" or key=="knitting" or key=="diy" or key=="concerts":
		return True
	return False


@app.route("/")
@app.route("/home/")
def main():
	if 'user' in session: 
		return redirect(url_for("userHomePage"))
	return render_template("login.html", message = message)

# def auth():
#     #users2 (fname TEXT, lname TEXT, username TEXT, hashedpassword TEXT);
#     loginResponse = request.form
#     username = loginResponse["user"]
#     password = loginResponse["pw"]
#     if authorize.checkLogin(username, password):
#         session['user'] = username
#         return render_template("userHomePage.html")
#     return render_template("login.html", message="not a match")
#     #check if they good

@app.route("/profilepic/", methods=["POST"])
def pfp(): 
	print request.files
	filename = upload_file(request.files)
	personalInfo.addprofile(session['user'],filename)
	return redirect(url_for("userHomePage"))



@app.route("/auth/", methods = ["POST"])
def auth():
	loginResponse = request.form
	username = loginResponse["user"]
	password = loginResponse["pw"]
	formMethod = loginResponse['enter']
	if formMethod == "Login":
		if authorize.checkLogin(username,password) == True:
			session['user']= username
			return redirect(url_for("userHomePage"))
		else:
			message = "login failed"
			if 'user' in session:
				session.pop('user')
			return redirect(url_for("main"))
	if formMethod == "Register":
		return redirect(url_for("register"))


	# if loginResponse["enter"]=='Register':
	# 	if username=='' or password =='':
	# 		session['message']='Invalid'
	# 		return redirect(url_for('main'))    
	# 	elif users.checkAccount(username)==False:
	# 		session['message']='Username exists'
	# 		return redirect(url_for('main'))           
	# 	result=users.addAccount(username,password)
	# 	if result==True:
	# 		session['user']=username
	# 		return redirect(url_for('userHomePage'))
	# 	else:
	# 		return redirect(url_for('main')) 

	# elif request.form['enter']=='Login':
	# 	dbPassword=users.getAccountPass(username)
	# 	if dbPassword==hashlib.sha256(password).hexdigest() and dbPassword != 'None':
	# 		session['user']=username
	# 		return redirect(url_for('userHomePage'))
	# 	else:
	# 		session['message']='Username or Password is incorrect'
	# 		redirect(url_for('main'))     
	# return redirect(url_for('main'))

@app.route("/logout/")
def logout():
	session.pop("user")
	return redirect(url_for("main"))

@app.route("/userHomePage/")
def userHomePage():
	datestring = aujourdhui()
	#print datestring
	#print ''
	pfp = "../"+personalInfo.getRouteForPfp(session['user'])[0]
	print pfp
	return render_template("userHomePage.html", date=datestring, pfp = pfp)

@app.route("/register/")
def register():
	return render_template("form1.html", message="")

@app.route("/form1/", methods =["POST"])
def form1():
	registerResponse = request.form
	username = registerResponse['userN']
	#if username ain't already taken
	if authorize.checkRegister(username):
		fn = registerResponse['fName']
		ln = registerResponse['lName']
		pw = registerResponse['pw']
		authorize.createAccount(fn,ln,username, pw)
		session['user'] = username
		return redirect(url_for("form2"))
		#hash password, create acct
	else: 
		message = "username taken"
		return redirect(url_for("register"))

	#store the username and password from form1 ^^ in session

@app.route("/form2/")
def form2():
	return render_template("form2.html")
#function from personalinfo
#def addEntry(username, interestList, bigthing, zipcode, gender, age, gendpref, religionpref,myreligion, job, politicalpref, hobbies, mypolitics, agediff):

@app.route("/userinfo/", methods=["POST"])
def userinfo():
	personalInfoStuff=request.form
	newDict={'interests':[], 'hobbies':[]}
	for key in personalInfoStuff:
		if (isAHobby(key) or isAnInterest(key)):
			if isAHobby(key):
				newDict['hobbies'].append(key)
			if isAnInterest(key):
				newDict['interests'].append(key)
		else:
			newDict[key] = personalInfoStuff[key]
	username = session['user']
	interestList=newDict['interests']
	hobbies = newDict['hobbies']
	personalInfo.addEntry(username, interestList, newDict['bigthing'], newDict['zip'], newDict['gender'], newDict['age'], newDict['gendpref'], newDict['religionpref'], newDict['myreligion'], newDict['job'], newDict['politicalpref'], hobbies, newDict['mypolitics'], newDict['agediff'])
	return render_template("upload.html")
	#return redirect(url_for("userHomePage"))
	
@app.route("/change/", methods=["POST"])
def change():
	personalInfoStuff=request.form
	newDict={'interests':[], 'hobbies':[]}
	full = True
	for key in personalInfoStuff:
		if personalInfoStuff[key] == '':
			full = False
		if (isAHobby(key) or isAnInterest(key)):
			if isAHobby(key):
				newDict['hobbies'].append(key)
			if isAnInterest(key):
				newDict['interests'].append(key)
		else:
			newDict[key] = personalInfoStuff[key]
	username = session['user']
	interestList=newDict['interests']
	hobbies = newDict['hobbies']
	if (full):
		personalInfo.changeSettings(username, interestList, newDict['bigthing'], newDict['zip'], newDict['gender'], newDict['age'], newDict['gendpref'], newDict['religionpref'], newDict['myreligion'], newDict['job'], newDict['politicalpref'], hobbies, newDict['mypolitics'], newDict['agediff'])
	print type(request.files['upload'])
	filename = upload_file(request.files)
	print filename
	personalInfo.changeProfile(username, filename)
	return redirect(url_for("userHomePage"))

	



@app.route("/about/")
def about():
	return render_template("about.html") 

@app.route("/settings/")
def settings():
        print personalInfo.getData(session['user'])
        payload={}
        payload['intrest']=personalInfo.getIntrestList(session['user'])
        payload['hobby']=personalInfo.getHobbyList(session['user'])
        payload['politic']=personalInfo.getPolitic(session['user'])
        payload['big']=personalInfo.getBig(session['user'])
        payload['zip']=personalInfo.getZip(session['user'])
        payload['gender']=personalInfo.getGender(session['user'])
        payload['attract']=personalInfo.getIntrest(session['user'])
        payload['age']=personalInfo.getAge(session['user'])
        payload['agedif']=personalInfo.getAgeDif(session['user'])
        payload['religion']=personalInfo.getReligion(session['user'])
        payload['job']=personalInfo.getJob(session['user'])
        payload['religionpartner']=personalInfo.getReligiousPartner(session['user'])
        payload['politicpartner']=personalInfo.getPoliticPartner(session['user'])
	return render_template("settings.html", data=payload)


@app.route("/messages/", methods=["POST"])
def messages():
	return render_template("messages.html")


@app.route("/matches/", methods=["POST"])
def matches():
	matchList = matchme.findMatches(session['user'])
	return render_template("matches.html", matches = matchList)

@app.route("/events/", methods=["POST"])
def events():
	return render_template("events.html")





if(__name__ == "__main__"):
	app.debug = True
	app.run();
