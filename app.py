from flask import Flask, render_template, request, redirect, session, url_for
from models import db, User, Ride
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db.init_app(app)
bcrypt = Bcrypt(app)


@app.route('/')
def home():
    return redirect(url_for('register'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        hashed = bcrypt.generate_password_hash(request.form['password']).decode('utf-8')
        user = User(username=request.form['username'], password=hashed, role=request.form['role'])
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if user and bcrypt.check_password_hash(user.password, request.form['password']):
            session['user_id'] = user.id
            session['username'] = user.username
            session['role'] = user.role
            return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    if session['role'] == 'Passenger':
        rides = Ride.query.filter_by(passenger_id=session['user_id']).all()
        return render_template('passenger_dashboard.html', rides=rides)
    else:
        rides = Ride.query.filter_by(status='Pending').all()
        return render_template('driver_dashboard.html', rides=rides)

@app.route('/request_ride', methods=['POST'])
def request_ride():
    if session['role'] != 'Passenger':
        return redirect(url_for('dashboard'))
    ride = Ride(
        pickup=request.form['pickup'],
        destination=request.form['destination'],
        passenger_id=session['user_id']
    )
    db.session.add(ride)
    db.session.commit()
    return redirect(url_for('dashboard'))

@app.route('/accept_ride/<int:ride_id>')
def accept_ride(ride_id):
    if session['role'] != 'Driver':
        return redirect(url_for('dashboard'))
    ride = Ride.query.get(ride_id)
    if ride and ride.status == 'Pending':
        ride.status = f'Accepted by {session["username"]}'
        ride.driver_id = session['user_id']
        db.session.commit()
    return redirect(url_for('dashboard'))

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))




if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
