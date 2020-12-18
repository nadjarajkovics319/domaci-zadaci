import hashlib
import time
from datetime import datetime

import mysql.connector
from bson import ObjectId
from flask import Flask, redirect, render_template, request, session, url_for
from flaskext.mysql import MySQL

# mysql = MySQL()
# mysql.init_app(app)

mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="",
	database="dz67"
)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'januar2020'

@app.route('/')
@app.route('/raspored')
def raspored():
	mc = mydb.cursor()
	mc.execute("SELECT * FROM raspored")
	ceoraspored = mc.fetchall()

	nastavnici = []
	ucionice = []
	for i in ceoraspored:
		if i[7] not in ucionice:
			ucionice.append(i[7])

	for i in ceoraspored:
		if i[3] not in nastavnici:
			nastavnici.append(i[3])
		
	return render_template("schedule.html", ceoraspored = ceoraspored, nastavnici = nastavnici, ucionice = ucionice)

if __name__ == '__main__':
	app.run(debug=True)
