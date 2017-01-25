import json
from datetime import datetime
import sqlite3

def insert_message(recipient, message, user):
	f = "data/data.db"
	db = sqlite3.connect(f)
	og = db.cursor()
	datestr = datetime.now().strftime('%B %d, %Y - %H:%M')
	try:
		insert = "INSERT INTO messages (recipient, sender, messagedatetime, status, body) VALUES ('%s', '%s', '%s', '%s', '%s')"%(recipient, user, datestr, 'sent', message)
		#print ' INSERTTTTTT ', insert
		og.execute(insert)
		db.commit()
		db.close()
		return True
	except Exception as e:
		return False

def get_message(user):
	f = "data/data.db"
	db = sqlite3.connect(f)
	og = db.cursor()
	db_results = {}
	db_results = "SELECT body, messagedatetime, sender FROM messages WHERE recipient == '%s'" %(user)
	#print 'db_results', db_results
	output = og.execute(db_results)
	#print 'output len ', output
	db.commit()
	allmsgs = []
	ctr = 0
	for item in output:
		msg = {}
		for idx, x in enumerate(item):
			#print 'item x', x, type(x), idx
			if idx == 0:
				msg['body'] = x
			if idx == 1:
				msg['messagedatetime'] = x
			if idx == 2:
				msg['sender'] = x
			#print 'msg ', msg
		ctr = ctr + 1
		#print "counter = ", ctr
		allmsgs.append(msg)
	#print 'allllllll ', allmsgs
	db.close()
	return allmsgs

#item x yeet <type 'unicode'>
#tem x January 24, 2017 - 21:27
#tem x lorenz <type 'unicode'>