from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import purchase, user # import entire file, rather than class, to avoid circular imports
from flask import flash

# CREATE
@app.route('/item/custom')
def create_item():
    if not session:
        return redirect('/')
    return render_template('[INSERT ITEM/CUSTOM HTML HERE]')

@app.route('/createitem', methods=['POST'])
def createitem():
    if not purchase.Purchase.validate_purchase(request.form):
        return redirect('/item/custom')
    data = {
        "item_name": request.form['item_name'],
        "category": request.form['category'],
        "facility": request.form['facility'],
        "city": request.form['city'],
        "quantity": request.form['quantity'],
        "user_id": session['id']
    }
    purchase.Purchase.save(data)
    return redirect('/my_gifts')

#READ
@app.route('/my_gifts')
def display(id):
    user_purchases = user.User.get_user_purchases(id)
    if 'id' not in session:
        return redirect('/')
    return render_template('[INSERT MY_GIFTS HTML HERE]', user_purchases = user_purchases)

@app.route('/item/<int:id>')
def showone(id):
    if 'id' not in session:
        return redirect ('/')
    one_purchase = purchase.Purchase.get_by_id(id)
    return render_template('[INSERT ITEM INFO DISPLAY PAGE HERE]', one_purchase = one_purchase)

@app.route('/gift/given')
def show_user_gifts(id):
    if 'id' not in session:
        return redirect('/')
    user_gifts = purchase.Purchase.get_all_purchases(id)
    return render_template('[INSERT GIFT/GIVEN HTML FILE HERE]', user_gifts = user_gifts)

#UPDATE
@app.route('/item/edit/<int:id>')
def update(id):
    if 'id' not in session:
        return redirect ('/')
    one_purchase = purchase.Purchase.get_by_id(id)
    return render_template('[INSERT UPDATE PAGE HTML HERE]', one_purchase = one_purchase)

@app.route('/updateitem/<int:id>', methods=['POST', 'GET'])
def updating(id):
    if 'id' not in session:
        return redirect ('/')
    if not purchase.Purchase.validate_purchase(request.form):
        return redirect(f'/item/edit/{id}')
    data = {
        'item_name' : request.form['item_name'],
        "category": request.form['category'],
        "facility": request.form['facility'],
        "city": request.form['city'],
        "quantity": request.form['quantity'],
        'id' : id
    }
    purchase.Purchase.update(data)
    return redirect('[INSERT MY_GIFTS PAGE HTML HERE]')

#DELETE
@app.route("/delete/<int:id>", methods=['POST', 'GET'])
def deleteshow(id):
    if 'id' not in session:
        return redirect ('/')
    purchase.Purchase.delete(id)
    return redirect('[INSERT MY_GIFTS PAGE HTML HERE]')