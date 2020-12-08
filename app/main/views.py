from . import main
from flask import render_template,request,redirect,url_for,abort
from flask_login import login_required,current_user
from ..models import User, PitchCategory, Pitch, Comments, Votes
# from .forms import UpdateProfile
from .forms import PitchForm, CommentForm, CategoryForm
from .. import db

@main.route('/')
def index():
    """
    View root page function that returns index page
    """

    all_category = PitchCategory.get_categories()
    all_pitches = Pitch.query.order_by('id').all()
    print(all_pitches)

    title = 'Home- Welcome'
    return render_template('index.html', title = title, categories=all_category, all_pitches=all_pitches)

