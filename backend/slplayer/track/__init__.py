from flask import Blueprint
print("track init")
track = Blueprint('track',__name__)

from . import views
