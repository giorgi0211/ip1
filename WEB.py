# from flask import Flask, redirect, url_for
# app = Flask(__name__)
#
# @app.route('/')
# def home():
#     return 'Home page'
#
# @app.route('/GER-POR')
# def GER_POR():
#     return '<h1>POR2-1GER</h1>'
#
# @app.route('/<country>')
# def euro(country):
#     return f'I am with {country} on euro21'
#
# @app.route('/<country>/<bitch>')
# def europe(country,bitch):
#     return f'I am with {country} on euro21, fuck {bitch}'
#
# @app.route('/messiiii')
# def messiiii():
#     return redirect('https://www.google.com/search?q=loria&tbm=isch&ved=2ahUKEwiF3O7qiaTxAhUnMuwKHbErAAkQ2-cCegQIABAA&oq=loria&gs_lcp=CgNpbWcQAzICCAAyAggAMgIIADICCAAyAggAMgIIADICCAAyAggAMgIIADICCAA6BwgAELEDEEM6BAgAEEM6BQgAELEDUMYiWNRCYLFGaAZwAHgAgAGFAYgB2QqSAQQwLjEymAEAoAEBqgELZ3dzLXdpei1pbWewAQDAAQE&sclient=img&ei=4RXOYMXnDKfksAex14BI&bih=657&biw=1366')
#
#
# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, render_template, redirect, url_for, request, session
from flask_sqlalchemy import SQLAlchemy
import requests
import json
import sqlite3
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lookup_db.sqlite'
app.config['SECRET_KEY'] = 'Python'
db = SQLAlchemy(app)

class IP_address(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    ip = db.Column(db.String,nullable=False)
    def __str__(self):
        return f'{self.id},ip-{self.ip}'


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        username = request.form['username']
        session['username']=username
        return redirect(url_for('user', name=username))

    return render_template('login.html')


@app.route('/<name>')
def user(name):
    return f"Hello {name}"

@app.route('/iplookup', methods=['POST', 'GET'])

def iplookup():
    if request.method=='POST':
        ip = request.form['ip']
    # token = '2c7863a34f2f06'
    # url = f"https://ipinfo.io/{ip}?token={token}"
    # req = requests.get(url)
        db.session.add(ip=ip)
        db.session.commit()
        return 'done'

    return render_template('iplookup.html')



@app.route('/logout')
def logout():
    session.pop('username', None)
    return 'you are logged out'


# @app.route('/books', methods=['GET', 'POST'])
# def books():
#     return render_template('books.html')


if __name__=='__main__':
    app.run(debug=True)