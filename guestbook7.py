from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Date

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://webadmin:SPYatb32373@node1247-rachpython.th.app.ruk-com.cloud:5432/testdb'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://webadmin:DKBmmx00859@node17334-patsakon.app.ruk-com.cloud:5432/mydb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Comments(db.Model):
    __tablename__ = 'comments'
    #id = Column(Integer, primary_key=True)
    name = Column(String, primary_key=True)
    comment = Column(String)


@app.route('/')
def index():
    result = Comments.query.all()
    return render_template('index7.html', result=result)


@app.route('/sign')
def sign():
    return render_template('sign7.html')


@app.route('/process', methods=['POST'])
def process():
    name = request.form['name']
    comment = request.form['comment']
    signature = Comments(name=name, comment=comment)
    db.session.add(signature)
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80)