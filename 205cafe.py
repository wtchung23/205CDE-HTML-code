from flask import Flask, render_template, request, redirect, url_for, session
import pymysql
from datetime import date
#create an instance of FLask class
app = Flask(__name__)
app.static_folder = 'static'
app.secret_key = 'any random string'
@app.route("/home")
def home():
	if 'username' in session:
		return render_template('home.html',username=session['username'])
	else:
	
		return render_template('home.html')

@app.route("/coffee")
def coffee():
	if 'username' in session:
		return render_template('coffee.html',username=session['username'])
	else:
		return render_template('coffee.html')

@app.route("/menu")
def menu():
	if 'username' in session:
		return render_template('menu.html',username=session['username'])
	else:
		return render_template('menu.html')

@app.route("/breakfast")
def breakfast():
	if 'username' in session:
		return render_template('breakfast.html',username=session['username'])
	else:
		return render_template('breakfast.html')

@app.route("/lunch")
def lunch():
	if 'username' in session:
		return render_template('lunch.html',username=session['username'])
	else:
		return render_template('lunch.html')

@app.route("/dessert")
def dessert():
	if 'username' in session:
		return render_template('dessert.html',username=session['username'])
	else:
		return render_template('dessert.html')

@app.route("/event")
def event():
	if 'username' in session:
		return render_template('event.html',username=session['username'])
	else:
		return render_template('event.html')

@app.route("/contact")
def contact():
	if 'username' in session:
		return render_template('contact.html',username=session['username'])
	else:
		return render_template('contact.html')

@app.route("/contactSend", methods=['POST', 'GET'])
def contactSend():
	if request.method=='POST':
		questioner = request.form.get("questioner")
		questionerEmail = request.form.get("questionerEmail")
		question = request.form.get("question")
		today = date.today()
		db = pymysql.connect(host="localhost",user="root",password="password819",db="205cafe")
		"""
		connection = pymysql.connect(host='localhost',
    	                             user='user',
        	                     password='passwd',
            	                     db='db',
                	             charset='utf8mb4',
                    	             cursorclass=pymysql.cursors.DictCursor)
		"""
		# prepare a cursor object using cursor() medthod
		cursor = db.cursor()
		sql = """INSERT INTO user_question(`questioner`,`questioner-email`,`question`,`question-date`,`Done?`)
				 VALUES('%s','%s','%s','%s','no')""" %(questioner,questionerEmail,question,today)
		try:
			cursor.execute(sql)
			#commit your changes in the database
			db.commit()
		except:
			db.rollback()
	if 'username' in session:
		return render_template('contactSend.html',username=session['username'])
	else:
		return render_template('contactSend.html')

@app.route("/userinfo")
def userinfo():
	if 'username' in session:
		db = pymysql.connect(host="localhost",user="root",password="password819",db="205cafe")
		cursor = db.cursor()
		sql="SELECT `username`,`password`,`email`,`integral` FROM `userInfo` WHERE `username`='%s'"%(session['username'])
		cursor.execute(sql)
		dataResults = cursor.fetchone()
		return render_template('userInfo.html',username=session['username'],password=dataResults[1],email=dataResults[2],integral=dataResults[3])
	else:
		return redirect(url_for('home'))
	db.close()

@app.route("/changePwdPage")
def changePwdPage():
	return render_template('changePwdPage.html',username=session['username'])

@app.route("/changePassword",methods=['POST', 'GET'])
def changePassword():
	if request.method == 'POST':
		oldpassword = request.form.get("oldpassword")
		newPassword = request.form.get("newPassword")
		confirmPassword = request.form.get("confirmPassword")
		db = pymysql.connect(host="localhost",user="root",password="password819",db="205cafe")
		cursor = db.cursor()
		sql="SELECT `password` FROM `userInfo` WHERE `username`='%s'"%(session['username'])
		cursor.execute(sql)
		dataResults = cursor.fetchone()
		if oldpassword==dataResults[0]:
			if newPassword==confirmPassword:
				sql="UPDATE `userInfo` SET `password`='%s' WHERE `username`='%s'"%(newPassword,session['username'])
				try:
					cursor.execute(sql)
					#commit your changes in the database
					db.commit()
				except:
					#rollback in case there is any error
					db.rollback()
				return redirect(url_for('userinfo'))
			else:
				return render_template('changePwdPage.html',message2='Password and confirm password are not the same')
		else:
			return render_template('changePwdPage.html',message2='Your old password is not correct')
	db.close()

@app.route("/login", methods=['POST', 'GET'])
def login():
	db = pymysql.connect(host="localhost",user="root",password="password819",db="205cafe")
	"""
	connection = pymysql.connect(host='localhost',
    	                             user='user',
        	                     password='passwd',
            	                     db='db',
                	             charset='utf8mb4',
                    	             cursorclass=pymysql.cursors.DictCursor)
	"""
	# prepare a cursor object using cursor() medthod
	#error = None;
	cursor = db.cursor()
	sql = "SELECT `username`,`password` FROM `userInfo`"
	cursor.execute(sql)
	dataResults = cursor.fetchall()
	if request.method == 'POST':
		userName = request.form.get("name")
		userPassword = request.form.get("password")
		for row in dataResults:
			dbUserName=row[0]
			dbUserPassword=row[1]
			if userName==dbUserName and userPassword==dbUserPassword :
				session['username'] = dbUserName
				return redirect(url_for('home'))
				break
		else:
				#url_for('name of the function of the route','parameters(if required)')
				return render_template('home.html',message='false')
		db.close()
		"""
		result = request.form.to_dict(),
		return render_template('result', result=result, data=dataResults)
		"""
@app.route("/signup")
def signup():
	return render_template('signUp.html')

@app.route("/register", methods=['POST', 'GET'])
def register():
	if request.method=='POST':
		NewUsername = request.form.get("newUsername")
		NewPassword = request.form.get("newPassword")
		ConfirmPassword = request.form.get("confirmPassword")
		email = request.form.get("email")
		db = pymysql.connect(host="localhost",user="root",password="password819",db="205cafe")
		cursor = db.cursor()
		"""
		connection = pymysql.connect(host='localhost',
    	                             user='user',
        	                     password='passwd',
            	                     db='db',
                	             charset='utf8mb4',
                    	             cursorclass=pymysql.cursors.DictCursor)
		"""
		sql = "SELECT `username` FROM `userInfo`"
		cursor.execute(sql)
		results = cursor.fetchall()
		for row in results:
			username=row[0]
			if username==NewUsername:
				return render_template('signUp.html',wrongMessage='Username is already used. Please try another one')
				break
		else:
			if NewPassword==ConfirmPassword:
				# prepare a cursor object using cursor() medthod

				sql = """INSERT INTO userInfo(`username`,`password`,`email`,`integral`)VALUES('%s','%s','%s',0)""" %(NewUsername,NewPassword,email)
				try:
					cursor.execute(sql)
					#commit your changes in the database
					db.commit()
				except:
					db.rollback()
				return render_template('register.html',NewUsername=NewUsername,NewPassword=NewPassword,email=email)
			else:
				return render_template('signUp.html',wrongMessage='Password and confirm password are not the same',NewUsername=NewUsername)			
		db.close()
		"""
		result = request.form.to_dict(),
		return render_template('result', result=result, data=dataResults)
		"""
@app.route("/signout")
def signout():
	session.pop('username',None)
	return redirect(url_for('home'))

if __name__ == '__main__':
	app.run(debug=True)
