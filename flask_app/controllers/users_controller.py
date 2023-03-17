from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.users_model import User

@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def users():
    return render_template("users.html",users=User.get_all())

@app.route('/users/edit/<int:id>')
def edit(id):
    data = {
        "id":id
    }
    return render_template("edit_user.html",users=User.get_one(data))

@app.route('/users/show/<int:id>')
def show(id):
    data = {
        "id":id
    }
    return render_template("show_user.html",users=User.get_one(data))

@app.route('/user/new')
def new():
    return render_template("new_user.html")

@app.route('/user/create',methods=['POST'])
def create():
    print(request.form)
    User.save(request.form)
    return redirect('/users')

@app.route('/user/update/<int:id>',methods=['POST'])
def update(id):
    user = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email'],
        'id' : id
    }
    User.update(user)
    return redirect('/users')

@app.route('/user/destroy/<int:id>')
def destroy(id):
    data ={
        'id': id
    }
    User.destroy(data)
    return redirect('/users')
