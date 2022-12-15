from flask import jsonify, request
from . import user
from .. import db
from models import User

@user.route('/<int:id>',methods=['GET'])
def getUser(id):

    """Get user from database by id

    Args:
        id (int): id of user

    Returns:
        obj: returns user object
    """
    user = User.query.get(id)
    if not user:
        return jsonify({"error":"User does not exist"})
    delattr(user,"password")
    return jsonify({"data":user})



@user.route('/<int:id>',methods=['PUT'])
def updateUser(id):
    """update user in database

    Args:
        id (int): user id
    """
    user = User.query.get(id)


    if "name" in request.form:
        user.name = request.form['name']
    if "fav_artist" in request.form:
        user.fav_artist = request.form['fav_artist']
    if "fav_style" in request.form:
        user.fav_style = request.form['fav_style']

    db.session.commit()
    user.password = "null"
    return jsonify({"data":user})



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
    return jsonify({"Success":"User Successfull Deleted"})
