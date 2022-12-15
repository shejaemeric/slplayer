from flask import Blueprint

track = Blueprint('track',__name__)

from . import views
