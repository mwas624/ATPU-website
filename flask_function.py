from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os
from werkzeug.wsgi import DispatcherMiddleware

# Initialize Flask app
app = Flask(__name__)

# Configure database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///visitors.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define Visitor model
class Visitor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    tag_no = db.Column(db.String(50), nullable=False)
    vehicle_reg_no = db.Column(db.String(50), nullable=False)
    id_no = db.Column(db.String(50), nullable=False)
    time_in = db.Column(db.String(20), nullable=False)
    time_out = db.Column(db.String(20), nullable=False)
    visiting_office = db.Column(db.String(100), nullable=False)
    signature = db.Column(db.String(200), nullable=False)

# Set up routes for Flask app
@app.route('/')
def index():
    return render_template("home.html")

@app.route('/submit', methods=["POST"])
def submit():
    # Handle form submission
    name = request.form['name']
    phone = request.form['phone']
    tag_no = request.form['tag_no']
    vehicle_reg_no = request.form['vehicle_reg_no']
    id_no = request.form['id_no']
    time_in = request.form['time_in']
    time_out = request.form['time_out']
    visiting_office = request.form['visiting_office']
    signature = request.form['signature']

    # Save the visitor to the database
    new_visitor = Visitor(name=name, phone=phone, tag_no=tag_no, vehicle_reg_no=vehicle_reg_no, 
                          id_no=id_no, time_in=time_in, time_out=time_out, 
                          visiting_office=visiting_office, signature=signature)

    db.session.add(new_visitor)
    db.session.commit()
    
    return "Visitor data has been submitted successfully!"

# Wrap Flask app for Netlify serverless function
def handler(event, context):
    with app.app_context():
        return DispatcherMiddleware(app.wsgi_app, {
            '/.netlify/functions/flask_function': app
        })(event, context)
