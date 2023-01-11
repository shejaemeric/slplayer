from werkzeug.security import generate_password_hash,check_password_hash
from flask import jsonify,request
from . import auth
from .. import db
from models import User
import jwt
import json


@auth.route('/login',methods=['POST'])
def login():

    """login into app

    Returns:
        user: object
    """

    username = request.form['username']
    password = request.form['password']


    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({"error":"User Does Not Exists"}),401


    if not (check_password_hash(user.password,password)):
        return({"error":"Incorrect Username or/and Password"}),401

    token = jwt.encode({'user_id':user.user_id,"user_name":user.name,"fav_artist":user.fav_artist,},"secretkey051!",algorithm='HS256')
    decoded_token = jwt.decode(token,"secretkey051!",algorithms='HS256')
    result = {"token":token,"name":user.name,"fav_artist":user.fav_artist,"username":user.username}
    print(result)
    return jsonify(result),200



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
        fav_style = "null"


    user = User.query.filter_by(email = email).first()
    if not user:
         user = User.query.filter_by(username = username).first()
    if user:
        return jsonify({"error":"Username already exists"}),401

    password = generate_password_hash(password, method='sha256')

    new_user = User(name,username,email,password,fav_artist)
    db.session.add(new_user)
    db.session.commit()
    token = jwt.encode({'user_id':new_user.user_id,"user_name":new_user.name,"fav_artist":new_user.fav_artist,},"secretkey051!",algorithm='HS256')
    decoded_token = jwt.decode(token,"secretkey051!",algorithms='HS256')
    return jsonify({"token":token,"name":new_user['name'],"fav_artist":new_user['fav_artist'],"username":['new_user.username']}),201

@auth.route('/logout', methods=['GET'])
def logout():

    """logout from app

    Returns:
        _type_: _description_
    """
    return ({"Success":"Log Out Successful"}),200


# def auth_required(func):
#     def wrapper(*args,**kwargs):
#         """get JWT from request header"""
#         token = request.headers.get('Authorization')

#         if not token:
#             return jsonify({"error":"Token is required"}),401

#         try:
#             user = jwt.decode(token,"secretkey051!",algorithms='HS256')
#         except jwt.InvalidTokenError:
#             return jsonify({"error":"Invalid Token"}),401
