from flask import Flask,render_template,flash
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired
from datetime import datetime, timezone


#Create a flask instance
app = Flask(__name__)

#csrf token #hide when uploading to github
app.config['SECRET_KEY'] = "my super secret key"

#Create a User Class
class UserForm(FlaskForm):
    name = StringField("Name",validators=[DataRequired()])
    email = StringField("Email",validators=[DataRequired()])
    submit = SubmitField("Submit")

#Create a Form Class
class NamerForm(FlaskForm):
    name = StringField("Whats your Name",validators=[DataRequired()])
    submit = SubmitField("Submit")

@app.route('/')
def index():
    return render_template("index.html")

# localhost:5000/user/pullak
@app.route('/blog')
def blog(name):
    return render_template("blog.html",user_name=name)

@app.route('/projects')
def projects(name):
    return render_template("projects.html",user_name=name)

@app.route('/contact',methods=['GET','POST'])
def contact():
    name = None
    form = NamerForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        #flash msg
        flash("Form Submitted Succesfully")

    return render_template('contact.html',name = name,form = form)


#Custom Error Page

#invalid Url
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"),404

#Internal Server Error
@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"),500
