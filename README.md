# Telegraph Clone

App to anonymously record your stories, notes and articles. Just click [Telegraph clone](https://telegraph-story.herokuapp.com/)

The ability to edit a post within 24 hours.

# What's inside

The application is deployed on [heroku](https://heroku.com) using Flask framework.

# Run locally

Use Venv or virtualenv for insulation project. Virtualenv example:

```
$ python virtualevn myenv
$ source myenv/bin/activate
```

Install requirements:

```
pip install -r requirements.txt
```
Run gunicorn:

At the root of the project
```
gunicorn server:app
```
and simple [click](http://localhost:8000)


# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
