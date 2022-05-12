
from flask import render_template,request,redirect,url_for,abort, flash
from . import main
from flask_login import login_required, current_user
from ..models import Pitch, User,Comment,Upvote,Downvote
from .forms import PitchForm, CommentForm, UpvoteForm
from flask.views import View,MethodView
from .. import db 



# @main.route('/', methods = ['GET','POST'])
# def home():

#     '''
#     Root page functions that return the home page and its data
#     '''
#     pitch = Pitch.query.all()
#     title = 'Home'
#     upvotes = Upvote.get_all_upvotes(pitch_id=Pitch.id)
#     return render_template('index.html', title = title, pitch = pitch)
    


# @main.route('/music', methods = ['GET','POST'])
# def music():

#     '''
#     this method filters music pitches
#     '''
    
#     title = 'Music'
#     music = Pitch.query.filter_by(category="music")
#     return render_template('music.html', title = title,music=music)

# @main.route('/art', methods = ['GET','POST'])
# def art():

#     '''
#     this method filters music pitches
#     '''
    
#     title = 'Art'
#     art = Pitch.query.filter_by(category ="art")
#     return render_template('art.html', title = title,art=art)

# @main.route('/movies', methods = ['GET','POST'])
# def movies():

#     '''
#     this method filters music pitches
#     '''
    
#     title = 'movies'
#     movies = Pitch.query.filter_by(category ="movies")
#     return render_template('movies.html', title = title,movies=movies)

# @main.route('/general', methods = ['GET','POST'])
# def general():

#     '''
#     this method filters music pitches
#     '''
    
#     title = 'general'
#     general = Pitch.query.filter_by(category ="general")
#     return render_template('movies.html', title = title,general=general)

@main.route('/', methods = ['GET','POST'])
def index():

    '''
    Root page functions that return the home page and its data
    '''
    pitch = Pitch.query.filter_by().first()
    title = 'Pitch'
    music = Pitch.query.filter_by(category="music")
    movies = Pitch.query.filter_by(category ="movies")
    art = Pitch.query.filter_by(category ="art")
    general = Pitch.query.filter_by(category ="general")

    upvotes = Upvote.get_all_upvotes(pitch_id=Pitch.id)
    

    return render_template('home.html', title = title, pitch = pitch, movies=movies, music=music, art=art, general=general, upvotes=upvotes)
  
@main.route('/pitches/new/', methods = ['GET','POST'])
@login_required
def new_pitch():
    form = PitchForm()
    my_upvotes = Upvote.query.filter_by(pitch_id = Pitch.id)
    if form.validate_on_submit():
        description = form.description.data
        title = form.title.data
        owner_id = current_user
        category = form.category.data
        print(current_user._get_current_object().id)
        new_pitch = Pitch(owner_id =current_user._get_current_object().id, title = title,description=description,category=category)
        db.session.add(new_pitch)
        db.session.commit()
        
        
        return redirect(url_for('main.index'))
    return render_template('pitches.html',form=form)



@main.route('/comment/new/<int:pitch_id>', methods = ['GET','POST'])
@login_required
def new_comment(pitch_id):
    form = CommentForm()
    pitch=Pitch.query.get(pitch_id)
    if form.validate_on_submit():
        description = form.description.data

        new_comment = Comment(description = description, user_id = current_user._get_current_object().id, pitch_id = pitch_id)
        db.session.add(new_comment)
        db.session.commit()

        return redirect(url_for('.new_comment', pitch_id= pitch_id))

    all_comments = Comment.query.filter_by(pitch_id = pitch_id).all()
    return render_template('comments.html', form = form, comment = all_comments, pitch= pitch )

   
@main.route('/pitch/upvote/<int:pitch_id>/upvote', methods = ['GET', 'POST'])
@login_required
def upvote(pitch_id):
    pitch = Pitch.query.get(pitch_id)
    user = current_user
    pitch_upvotes = Upvote.query.filter_by(pitch_id= pitch_id)
    
    if Upvote.query.filter(Upvote.user_id==user.id,Upvote.pitch_id==pitch_id).first():
        return  redirect(url_for('main.index'))


    new_upvote = Upvote(pitch_id=pitch_id, user = current_user)
    new_upvote.save_upvotes()
    return redirect(url_for('main.index'))


@main.route('/pitch/downvote/<int:pitch_id>/downvote', methods = ['GET', 'POST'])
@login_required
def downvote(pitch_id):
    pitch = Pitch.query.get(pitch_id)
    user = current_user
    pitch_downvotes = Downvote.query.filter_by(pitch_id= pitch_id)
    
    if Downvote.query.filter(Downvote.user_id==user.id,Downvote.pitch_id==pitch_id).first():
        return  redirect(url_for('main.index'))


    new_downvote = Downvote(pitch_id=pitch_id, user = current_user)
    new_downvote.save_downvotes()
    return redirect(url_for('main.index'))