from flask import jsonify,request
import jwt
def auth_required(func):
    def wrapper(*args,**kwargs):
        """get JWT from request header"""
        token = request.headers.get('Authorization')
        token = (token.split(" "))[1]

        if not token:
            print("Token is required")
            return jsonify({"error":"Token is required"}),404

        try:

            user = jwt.decode(token,"secretkey051!",algorithms=['HS256'])

            print(user)
        except jwt.InvalidTokenError:
            print("Invalid Token")
            return jsonify({"error":"Invalid Token"}),401

        return func(*args,user=user,**kwargs)
    return wrapper
