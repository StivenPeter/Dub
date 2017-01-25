import json
from datetime import datetime
import sqlite3


def insert_message(recipient, message, user):
    f = "data/data.db"
    db = sqlite3.connect(f)
    og = db.cursor()
    datestr = datetime.now().strftime('%B %d, %Y - %H:%M')
    try:
        insert = "INSERT INTO messages VALUES ('%s', '%s', '%s', '%s', '%s')"%(recipient, user, datestr, 'sent', message)
        og.execute(insert)
        db.commit()
        db.close()
        return True
    except Exception as e:
        return False

# @app.route("/get_messages", methods=['POST'])
# def messages_post():
#     message_option = request.form.get('message_options')
#     # db_results is a list of dictionaries
#     # [ {'msgid': 1, 'body': 'hello', 'sender': 'abc', 'recipient': 'user'},
#     #   {'msgid': 2, 'body': 'hello', 'sender': 'def', 'recipient': 'user'}]
#     db_results = {}
#     if message_option == 'All my messages':
#         db_results = # select from messages where recipient = userid
#     else:
#         db_results = # select from messages where recipient = userid and status = 'sent'
#     return render_template("messages.html", message_output=db_results)


# @app.route("/send_message", methods=['POST'])
# def send_message():
#     recipient = request.form.get('recipient')
#     message = request.form.get('message')

#     # save to db, add db values like datetime, status = SENT, sender= user
#     return render_template("messages.html")



