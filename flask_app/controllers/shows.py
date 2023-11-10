from flask_app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from flask import render_template, redirect, request, session
from flask_app.models import show, user # import entire file, rather than class, to avoid circular imports
from flask import flash

# CREATE
@app.route('/shows/new')
def create_show():
    if not session:
        return redirect('/')
    return render_template('createshow.html')

@app.route('/createshow', methods=['POST'])
def createshow():
    if not show.Show.validate_show(request.form):
        return redirect('/shows/new')
    data = {
        "title": request.form['title'],
        "network": request.form['network'],
        "date": request.form['date'],
        "description": request.form['description'],
        "user_id": session['id']
    }
    show.Show.save(data)
    return redirect('/shows')

#READ
@app.route('/shows')
def display():
    shows = show.Show.get_all()
    if 'id' not in session:
        return redirect('/')
    return render_template('homepage.html', shows=shows)

@app.route('/shows/<int:id>')
def showone(id):
    if 'id' not in session:
        return redirect ('/')
    one_show = show.Show.get_by_id(id)
    return render_template('show.html', one_show = one_show)

#UPDATE
@app.route('/shows/edit/<int:id>')
def update(id):
    if 'id' not in session:
        return redirect ('/')
    one_show = show.Show.get_by_id(id)
    return render_template('update.html', one_show = one_show)

@app.route('/updateshow/<int:id>', methods=['POST', 'GET'])
def updating(id):
    if 'id' not in session:
        return redirect ('/')
    if not show.Show.validate_show(request.form):
        return redirect(f'/shows/edit/{id}')
    data = {
        'title' : request.form['title'],
        'network' : request.form['network'],
        'date' : request.form['date'],
        'description' : request.form['description'],
        'id' : id
    }
    show.Show.update(data)
    return redirect('/shows')

#DELETE
@app.route("/delete/<int:id>", methods=['POST', 'GET'])
def deleteshow(id):
    if 'id' not in session:
        return redirect ('/')
    show.Show.delete(id)
    return redirect('/shows')