from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import login_user,logout_user,login_required
from flask import jsonify,request
from . import auth
from .. import db,login_manager
from models import User



@auth.route('/login',methods=['POST'])
def login():

    """login into app

    Returns:
        user: object
    """
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        remember = True if request.form['remember'] else False

    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({"error":"User Does Not Exists"})


    if not (check_password_hash(user.password,password)):
        return({"error":"Incorrect Username or/and Password"})
    delattr(user,"password")
    login_user(user,remember=remember)
    return jsonify({"data":user})



@auth.route('/signup',methods=['POST'])
def signup():

    """signup into app

    Returns:
        _type_: _description_
    """

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        username = request.form['username']
        fav_artist = request.form['fav_artist']
        fav_style = request.form['fav_style']

    user = User.query.filter_by(email = email).first()
    if not user:
         user = User.query.filter_by(username = username).first()
    if user:
        return jsonify({"error":"User already exists"})

    password = generate_password_hash(password, method='sha256')

    new_user = User(name,username,email,password,fav_artist,fav_style)
    db.session.add(new_user)
    db.session.commit()
    new_user.password = "null"
    return jsonify({"data":new_user})

@auth.route('/logout', methods=['GET'])
def logout():

    """logout from app

    Returns:
        _type_: _description_
    """
    logout_user()
    return ({"Success":"Log Out Successful"})

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
