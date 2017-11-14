
from flask import render_template, request, redirect, url_for, make_response
import uuid
from project import app, db
from .models import Story

HOURS_LIVE_COOKIES = 24
MAX_AGE_LIVE_COOKIES = HOURS_LIVE_COOKIES * 60 * 60


def get_slug(item_form_title):
    slug = item_form_title.replace(' ', '_')
    return slug


def update_text(edit_text):
    stories = db.session.query(Story)
    text_update = stories.filter_by(slug=edit_text['slug'])
    text_update.update(edit_text)
    db.session.commit()


@app.route('/', methods=['GET', 'POST'])
def add_story():
    if request.method == 'POST':
        author_id = request.cookies.get('cookie')
        if not author_id:
            author_id = str(uuid.uuid4())
        story_uuid = str(uuid.uuid4())
        story_title = request.form.get('header')
        story_signature = request.form.get('signature')
        story_body = request.form.get('body')
        slug = get_slug(story_title)
        db.session.add(Story(slug=slug,
                             story_title=story_title,
                             story_signature=story_signature,
                             story_body=story_body,
                             story_uuid=story_uuid,
                             author_id=author_id))
        db.session.commit()
        new_story = make_response(redirect(url_for('view_text',
                                                       slug=slug)))
        new_story.set_cookie('author_id', author_id,
                             max_age=MAX_AGE_LIVE_COOKIES)
        return new_story
    else:
        return render_template('form.html')


@app.route('/<slug>')
def view_text(slug):
    author_id = request.cookies.get('author_id')
    story = db.session.query(Story).get_or_404(slug)
    return render_template('story.html',
                           story=story,
                           author_id=author_id)


@app.route('/edit/<slug>', methods=['GET', 'POST'])
def edit_text(slug):
    author_id = request.cookies.get('author_id')
    story = db.session.query(Story).get_or_404(slug)
    if author_id == story.author_id:
        if request.method == 'POST':
            story_title = request.form.get('header')
            story_signature = request.form.get('signature')
            story_body = request.form.get('body')
            edit_text = {'story_title':story_title,
                         'story_signature':story_signature,
                         'story_body':story_body,
                         'slug':slug}
            update_text(edit_text)
        return render_template('form.html', story=story)
    else:
        return "Access is denied! Create your own story!"