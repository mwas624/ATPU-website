from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///visitors.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Visitor model
class Visitor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(20), nullable=False)  # Add the date field
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    tag_no = db.Column(db.String(50), nullable=False)
    vehicle_reg_no = db.Column(db.String(50), nullable=False)
    id_no = db.Column(db.String(50), nullable=False)
    time_in = db.Column(db.String(20), nullable=False)
    time_out = db.Column(db.String(20), nullable=False)
    visiting_office = db.Column(db.String(100), nullable=False)
    officer_on_duty = db.Column(db.String(100), nullable=False)
    signature = db.Column(db.String(200), nullable=False)

# Create the database and tables inside an application context
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/submit', methods=["POST"])
def submit():
    # Get data from form fields
    date = request.form['date']
    name = request.form['name']
    phone = request.form['phone']
    tag_no = request.form.get('tag_no', '')  # Optional field
    vehicle_reg_no = request.form['vehicle_reg_no']
    id_no = request.form['id_no']
    time_in = request.form['time_in']
    time_out = request.form['time_out']
    visiting_office = request.form['visiting_office']
    officer_on_duty = request.form['officer_on_duty']
    signature = request.form['signature']

    # Create a new Visitor record
    new_visitor = Visitor(
        date=date,
        name=name,
        phone=phone,
        tag_no=tag_no,
        vehicle_reg_no=vehicle_reg_no,
        id_no=id_no,
        time_in=time_in,
        time_out=time_out,
        visiting_office=visiting_office,
        officer_on_duty=officer_on_duty,
        signature=signature
    )

    # Add the record to the database
    db.session.add(new_visitor)
    db.session.commit()

    return "Visitor data has been submitted successfully!"

if __name__ == "__main__":
    app.run(debug=True)
