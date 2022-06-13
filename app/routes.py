from flask import render_template, flash, redirect
from app import app
from app.forms import EmailForm
from flask import request
from app.email import send_email




@app.route('/')

@app.route('/index', methods=['GET', 'POST'])
def index():
    form=EmailForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            send_email(form.subject.data, form.name.data, form.email.data, form.message.data)
            return render_template('index.html', title='Home', form=form, success=True)
    else:
        return render_template('index.html', title='Home', form=form)
