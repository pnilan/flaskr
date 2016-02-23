# all the imports
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
	abort, render_template, flash

# create application
app = Flask(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

# Connects to the database
def connect_db():
	return sqlite3.connect(app.config['DAATABASE'])

# Runs app
if __name__ == '__main__':
	app.run()