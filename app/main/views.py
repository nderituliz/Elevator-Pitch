from . import main
from flask import render_template,request,redirect,url_for,abort
from flask_login import login_required,current_user
from ..models import User, PitchCategory, Pitch, Comments, Votes
# from .forms import UpdateProfile
from .forms import PitchForm, CommentForm, CategoryForm
from .. import db
