# coding = utf-8
"""
@author: lichao
@time:202511/24 20:08
"""

from flask import Blueprint

chatbot = Blueprint('chatbot', __name__)

from . import views
