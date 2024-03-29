from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
from send import send_mail


app=Flask(__name__)
ENV='prod'
if ENV =='dev':
    app.debug=True
    app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:Nautilus5he!@localhost/lexus'
else:
    app.debug=False
    app.config['SQLALCHEMY_DATABASE_URI']='postgres://yqktxyhkkzobit:c7417227b47d269763b592d5306a1892f26f4cd8fe4a240d3d3f23a5899618b4@ec2-52-200-68-5.compute-1.amazonaws.com:5432/d9njthj75kk1ab'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)
class Feedback(db.Model):
    __tablename__='feedback'
    id=db.Column(db.Integer,primary_key=True)
    customer=db.Column(db.String(211),unique=True)
    dealer=db.Column(db.String(211))
    rating=db.Column(db.Integer)

    def __init__(self,customer,dealer,rating):
        self.customer=customer
        self.dealer=dealer
        self.rating=rating







@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit',methods=['POST'])
def submit():
    if request.method=="POST":
        customer=request.form['customer']
        dealer=request.form['dealer']
        rating=request.form['rating']
        if customer == '' or dealer == '':
            return render_template('index.html',message='please enter something')
        if Feedback.query.filter_by(customer=customer).count() == 0:
            data=Feedback(customer=customer,dealer=dealer,rating=rating)
            db.session.add(data)
            db.session.commit()
            send_mail(customer,dealer,rating)
            return render_template('success.html')
        
        return render_template('index.html',message='please enter something')

        








if __name__=="__main__":
    app.debug=True
    app.run()