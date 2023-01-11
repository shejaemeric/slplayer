from flask import jsonify, request
from . import user
from .. import db
from models import User

@user.route('/<username>',methods=['GET'])
def getUser(username):

    """Get user from database by id

    Args:
        id (int): id of user

    Returns:
        obj: returns user object
    """
    user = User.query.filter_by(username = username).first()
    if not user:
        return jsonify({"error":"User does not exist"})
    delattr(user,"password")
    return jsonify({"user":user}),200



@user.route('/<username>',methods=['PUT'])
def updateUser(username):
    """update user in database

    Args:
        id (int): user id
    """
    print("updating")
    user = User.query.filter_by(username = username).first()
    if "name" in request.form:
        user.name = request.form['name']
    if "fav_artist" in request.form:
        user.fav_artist = request.form['fav_artist']
    if "email" in request.form:
        user.email= request.form['email']
    if "username" in request.form:
        user.username = request.form['username']

    print(user.fav_artist)
    db.session.commit()
    user.password = "null"
    return jsonify({"updatedUser":user}),200



@user.route('/<int:id>',methods=['DELETE'])
def deleteUser(id):
    """_summary_

    Args:
        id (int): user id
    """
    user = User.query.get(id)
    if not user:
        return jsonify({"error":"User does not exist"})
    db.session.delete(user)
    db.session.commit()
    return jsonify({"Success":"User Successfull Deleted"}),200
