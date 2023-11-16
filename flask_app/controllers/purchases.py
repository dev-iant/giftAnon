from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import purchase, user # import entire file, rather than class, to avoid circular imports
from flask import flash

# CREATE
@app.route('/item/custom')
def create_item():
    if not session:
        return redirect('/')
    return render_template('items_form.html')

@app.route('/create/item', methods=['POST'])
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
@app.route('/city/<city>')
def showcity(city):
    city_gifts = purchase.Purchase.get_by_city(city)
    if city == 'newyork':
        citystring = 'New York, NY'
    if city == 'maui':
        citystring = 'Maui, HI'
    if city == 'losangeles' :
        citystring = 'Los Angeles, CA'
    if city == 'houston' :
        citystring = 'Houston, TX'
    if 'id' not in session:
        return redirect('/')
    return render_template('by_city.html', city_gifts = city_gifts, citystring = citystring)

@app.route('/viewall')
def viewallgifts():
    all_gifts = purchase.Purchase.get_all()
    if 'id' not in session:
        return redirect('/')
    return render_template('allgifts.html', all_gifts = all_gifts)

@app.route('/facility/<facility>')
def showfacility(facility):
    facility_gifts = purchase.Purchase.get_by_facility(facility)
    if facility == 'goodwill':
        facilitystring = 'Goodwill'
    if facility == 'salvationarmy':
        facilitystring = 'Salvation Army'
    if facility == 'foodbank' :
        facilitystring = 'Food Bank'
    if facility == 'reliefcharity' :
        facilitystring = 'Relief Charity'
    if 'id' not in session:
        return redirect('/')
    return render_template('by_facility.html', facility_gifts = facility_gifts, facilitystring = facilitystring)

@app.route('/category/<category>')
def showcategory(category):
    category_gifts = purchase.Purchase.get_by_category(category)
    if category == 'clothing':
        categorystring = 'Clothing'
    if category == 'homegoods':
        categorystring = 'Home Goods'
    if category == 'groceries' :
        categorystring = 'Groceries'
    if category == 'water' :
        categorystring = 'Water (Case)'
    if 'id' not in session:
        return redirect('/')
    return render_template('by_category.html', category_gifts = category_gifts, categorystring = categorystring)

@app.route('/my_gifts')
def display():
    data = {
        "id": session['id']
    }
    user_gifts = user.User.get_user_gifts(data)
    if 'id' not in session:
        return redirect('/')
    return render_template('my_request.html', user_gifts = user_gifts)

@app.route('/item/<int:id>')
def showone(id):
    if 'id' not in session:
        return redirect ('/')
    one_purchase = purchase.Purchase.get_by_id(id)
    return render_template('items_form.html', one_purchase = one_purchase)

@app.route('/gift/given')
def show_user_gifts():
    if 'id' not in session:
        return redirect('/')
    id = session['id']
    user_gifts = purchase.Purchase.get_all_purchases(id)
    return render_template('gifts_given.html', user_gifts = user_gifts)

#UPDATE
@app.route('/item/edit/<int:id>')
def update(id):
    if 'id' not in session:
        return redirect ('/')
    one_purchase = purchase.Purchase.get_by_id(id)
    return render_template('items_form.html', one_purchase = one_purchase)

@app.route('/repop/<int:id>', methods=['POST', 'GET'])
def removePurchaserID(id):
    if 'id' not in session:
        return redirect ('/')
    purchase.Purchase.removePurchaser(id)
    return redirect('/gift/given')


@app.route('/gift/<int:id>/<int:purchaser_id>', methods=['POST', 'GET'])
def purchaseItem(id, purchaser_id):
    data = {
        'id' : id,
        'purchaser_id' : purchaser_id
    }
    purchase.Purchase.updatePurchaser(data)
    one_gift = purchase.Purchase.get_by_id(id)
    return render_template('facility.html', one_gift = one_gift)

@app.route('/update/<int:id>')
def updatepage(id):
    if session['role'] != 'Admin':
        return redirect ('/')
    one_purchase = purchase.Purchase.get_by_id(id)
    return render_template('update_item.html', one_purchase = one_purchase)
    

@app.route('/updateitem/<int:id>', methods=['POST', 'GET'])
def updating(id):
    if 'id' not in session:
        return redirect ('/')
    if not purchase.Purchase.validate_purchase(request.form):
        return redirect(f'/update/{id}')
    data = {
        'item_name' : request.form['item_name'],
        "category": request.form['category'],
        "facility": request.form['facility'],
        "city": request.form['city'],
        "quantity": request.form['quantity'],
        'id' : id
    }
    purchase.Purchase.update(data)
    return redirect('/my_gifts')

#DELETE
@app.route("/cancel/<int:id>", methods=['POST', 'GET'])
def deletePurchase(id):
    if 'id' not in session:
        return redirect ('/')
    purchase.Purchase.deletePurchase(id)
    return redirect('/my_gifts')