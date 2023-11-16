from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User
from flask_app.models.member import Member
from flask_app.models.contact import Contact
from flask_app.models.facility import Facility





@app.route("/facility/create" , methods=['POST'])
def create_facility():    
    
    data={ 
        'facility_id'  : request.form["facility_id"],        
        'facility_name' : request.form["facility_name"],
        'organization' : request.form["organization"],
        'address1' : request.form["address1"],
        'address2' : request.form["address2"],
        'phone' : request.form["phone"],
        'city' : request.form["city"]        
        }
  
    bin_id = Facility.create_facility(data)
    
# does this need to return or render_template?


@app.route('/facilities')
def edit_select_bins():
    bins = Bin.get_all_bins()    
    print(bins[0].member_id)
    return render_template("edit-bin-selection.html",bins=bins)
# the classmethod is commented out in the model



@app.route("/bin/<int:id>/edit")
def edit_bin(id):

    data={
        'bin_id':id
    }    
    
    bin = Bin.get_one_bin(data)
    if 'id' in session:       
            return render_template("edit-bin.html",bin=bin)
    return redirect('/')
# the classmethod is commented out in the model




