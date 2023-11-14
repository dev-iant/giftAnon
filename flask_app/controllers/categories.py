from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User
from flask_app.models.category import Categories





@app.route("/category/create" , methods=['POST'])
def create_category():    
    
    data={ 
        'category_id'  : request.form["category_id"],        
        'category_name' : request.form["category_name"]
        }
  
    bin_id = Categories.create_category(data)
    










# @app.route('/facilities')
# def edit_select_bins():
#     bins = Bin.get_all_bins()    
#     print(bins[0].member_id)
#     return render_template("edit-bin-selection.html",bins=bins)



# @app.route("/bin/<int:id>/edit")
# def edit_bin(id):

#     data={
#         'bin_id':id
#     }    
    
#     bin = Bin.get_one_bin(data)
#     if 'id' in session:       
#             return render_template("edit-bin.html",bin=bin)
#     return redirect('/')




