# app/controllers/botpost_controller.py

from flask import render_template, request, redirect, url_for, flash, Blueprint, json 
from app import app, db
from app.models import BotPost
from app.forms import BotPostForm, BulkCreateForm
from app.models.botpost_model import BotPost

bp = Blueprint('botpost', __name__)

@app.route('/')
def home():
    return render_template('home/index.html')


@app.route('/botpost/create', methods=['GET', 'POST'])
def create_botpost():
    form = BotPostForm()

    if form.validate_on_submit():
        part_one = form.part_one.data
        part_two = form.part_two.data
        body = {'part_one': part_one, 'part_two': part_two}

        new_botpost = BotPost(body=body)
        db.session.add(new_botpost)
        db.session.commit()

        # Redirect to the show page of the newly created BotPost
        return redirect(url_for('show_botpost', botpost_id=new_botpost.id))

    return render_template('botpost/create.html', form=form)


@app.route('/botpost/update/<int:botpost_id>')
def update_botpost(botpost_id):
    botpost = BotPost.query.get(botpost_id)
    return render_template('botpost/update.html', botpost=botpost)


@app.route('/botpost/show/<int:botpost_id>')
def show_botpost(botpost_id):
    botpost = BotPost.query.get_or_404(botpost_id)
    return render_template('botpost/show.html', botpost=botpost)


@app.route('/botpost/index')
def index_botposts():
    botposts = BotPost.query.all()
    return render_template('botpost/index.html', botposts=botposts)


@bp.route('/botpost/bulk_create', methods=['POST'])
def bulk_create_botposts():
    try:
        json_data = request.get_json()
        botposts_data = json_data.get('data', [])

        for entry in botposts_data:
            body_data = entry.get('body', {})
            BotPost.create(body_data)

        flash('BotPosts created successfully!', 'success')

    except ValueError:
        flash('Invalid JSON format for botposts.', 'error')

    return redirect(url_for('index_botposts'))