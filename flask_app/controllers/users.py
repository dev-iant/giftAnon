from flask_app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from flask import render_template, redirect, request, session
from flask_app.models import user # import entire file, rather than class, to avoid circular imports
from flask import flash # import entire file, rather than class, to avoid circular imports

# Create Users Controller
@app.route('/register/user', methods=['POST'])
def register():
    if not user.User.validate_user(request.form):
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": pw_hash
    }
    user.User.save(data)
    user_in_db = user.User.get_by_email(data)
    session['first_name'] = user_in_db.first_name
    session['last_name'] = user_in_db.last_name
    session['id'] = user_in_db.id
    return redirect('/shows')


# Read Users Controller
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    # see if the username provided exists in the database
    data = { "email" : request.form["email"] }
    user_in_db = user.User.get_by_email(data)
    # user is not registered in the db
    if not user_in_db:
        flash("Invalid Email or Password", "login")
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        # if we get False after checking the password
        flash("Invalid Email or Password", "login")
        return redirect('/')
    # if the passwords matched, we set the user_id into session
    session['first_name'] = user_in_db.first_name
    session['last_name'] = user_in_db.last_name
    session['id'] = user_in_db.id
    # never render on a post!!!
    return redirect("/shows")

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')