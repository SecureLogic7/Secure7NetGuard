# Project name: Secure7NetGuard_1.01_Offline
# Author: Nelsomar Barros
# Github: https://github.com/SecureLogic7/Secure7NetGuard
# Contact: nelsom.one8@gmail.com

from flask import Flask, render_template, redirect, url_for, flash, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from flask_wtf.csrf import CSRFProtect
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
import os
import re
from cryptography.fernet import Fernet
from datetime import datetime, timedelta
import socket
from html import escape

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

if 'DYNO' in os.environ:
    app.config['PREFERRED_URL_SCHEME'] = 'https'

@app.before_request
def before_request():
    if request.url.startswith('http:'):
        url = request.url.replace('http:', 'https:', 1)
        return redirect(url)

@app.after_request
def add_security_headers(response):
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    return response

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.remember_me = False
csrf = CSRFProtect(app)

key = Fernet.generate_key()
cipher_suite = Fernet(key)

login_attempts = {}

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(150), nullable=False)
    is_locked = db.Column(db.Boolean, default=False)
    failed_login_attempts = db.Column(db.Integer, default=0)
    last_failed_login = db.Column(db.DateTime)
    two_factor_secret = db.Column(db.String(150))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def anonymize_data(self):
        self.email = cipher_suite.encrypt(self.email.encode()).decode()
        self.username = cipher_suite.encrypt(self.username.encode()).decode()

    def increment_failed_login_attempts(self):
        self.failed_login_attempts += 1
        self.last_failed_login = datetime.utcnow()
        db.session.commit()

    def reset_failed_login_attempts(self):
        self.failed_login_attempts = 0
        db.session.commit()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def home():
    if current_user.is_authenticated and current_user.is_locked:
        return redirect(url_for('lock_screen'))
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        now = datetime.utcnow()
        if email in login_attempts and login_attempts[email]['attempts'] >= 5 and (now - login_attempts[email]['last_attempt']) < timedelta(minutes=5):
            flash('Too many login attempts. Please try again later.', 'danger')
    return render_template('login.html')

        if not re.match(r"^[\w\.-]+@([\w-]+\.)+[\w-]{2,4}$", email):
            flash('Invalid email address', 'danger')
            return render_template('login.html')

    if len(password) < 8:
            flash('Password must be at least 8 characters', 'danger')
    return render_template('login.html')

        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            if user.failed_login_attempts >= 5 and (datetime.utcnow() - user.last_failed_login) < timedelta(minutes=30):
                flash('Too many failed login attempts. Please try again later.', 'danger')
                return redirect(url_for('login'))
            login_user(user)
            session.regenerate_id()
            user.reset_failed_login_attempts()
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
    else:
            if email in login_attempts:
                login_attempts[email]['attempts'] += 1
                login_attempts[email]['last_attempt'] = now
            else:
                login_attempts[email] = {'attempts': 1, 'last_attempt': now}

            if user:
                user.increment_failed_login_attempts()
            flash('Login failed. Check email and password.', 'danger')
            return render_template('login.html')

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        email = escape(email)
        username = escape(username)

        if not re.match(r"^[\w\.-]+@([\w-]+\.)+[\w-]{2,4}$", email):
            flash('Invalid email address', 'danger')
    return render_template('register.html')

    if len(username) < 3 or len(username) > 20:
            flash('Username must be between 3 and 20 characters', 'danger')
            return render_template('register.html')

    if not re.match(r"^[a-zA-Z0-9_]+$", username):
            flash('Username can only contain letters, numbers, and underscores', 'danger')
            return render_template('register.html')

    if len(password) < 8:
            flash('Password must be at least 8 characters', 'danger')
            return render_template('register.html')

    if not re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$", password):
            flash('Password must contain at least 8 characters, including one uppercase letter, one lowercase letter, one number, and one symbol', 'danger')
            return render_template('register.html')

    if password != confirm_password:
            flash('Passwords do not match', 'danger')
            return render_template('register.html')

        user = User(email=email, username=username)
        user.set_password(password)
        user.anonymize_data()
        db.session.add(user)
        db.session.commit()
        flash('Registration successful!', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('home'))

@app.route('/lock')
@login_required
def lock_screen():
    current_user.is_locked = True
    db.session.commit()
    return render_template('lock.html')

@app.route('/unlock', methods=['POST'])
@login_required
def unlock_screen():
    password = request.form['password']
    password = escape(password)
    if current_user.check_password(password):
        current_user.is_locked = False
        db.session.commit()
        flash('Screen unlocked!', 'success')
        return redirect(url_for('home'))
    else:
        flash('Incorrect password. Try again.', 'danger')
        return redirect(url_for('lock_screen'))

@app.route('/network_status')
@login_required
def network_status():
    try:
        socket.create_connection(("www.google.com", 80))
        network_status = "Connected"
    except OSError:
        network_status = "Disconnected"
    return jsonify({"status": network_status})

if __name__ == '__main__':
    app.run(debug=True)

