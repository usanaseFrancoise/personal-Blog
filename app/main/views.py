from flask import render_template,url_for,abort,redirect,request
from . import main
from flask_login import login_user,login_required,current_user
# from .forms import RegistrationForm,LoginForm
from ..models import User,Post,Comment,Quotes
from .. import db,photos
from .forms import UpdateProfile,PostForm,CommentForm
import requests
from ..requests import getQuotes

@main.route('/')
def index():
    Postes=Post.query.all()
    job=Post.query.filter_by(category='Job').all()
    music=Post.query.filter_by(category='Music').all()
    news=Post.query.filter_by(category='News').all()
    quotes=getQuotes()

    return render_template('index.html'job=job,music=music,Postes=Postes,news=news,quotes=quotes)
    

@main.route('/create_new',methods=['GET','POST'])
@login_required
def new_post():
    form=PostForm()
    if form.validate_on_submit():
        title=form.title.data
        post=form.post.data
        category=form.category.data
        user_id=current_user
        new_post_object=Post(post=post,user_id=current_user._get_current_object().id,category=category,title=title)
        new_post_object.save_p()
        return redirect(url_for('main.index'))
    return render_template('create.html',form=form)