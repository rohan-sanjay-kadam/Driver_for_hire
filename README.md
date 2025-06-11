# 🚖 Driver-For-Hire 

A simple ride-matching web application built using Flask, SQLAlchemy, and Jinja2. Users can register as a "Passenger" or a "Driver", request rides, and accept them in real time.

# 📦 Features

- 🧍 Passenger:
  - Register and log in.
  - Request a ride (pickup → destination).
  - View current ride request status (e.g., Accepted by Driver X).

- 🚗 Driver:
  - Register and log in.
  - View pending ride requests.
  - Accept a ride and assign yourself as the driver.

- 🔐 Passwords hashed with Bcrypt.

# 🛠️ Tech Stack

- **Backend**: Flask, SQLAlchemy
- **Frontend**: HTML, CSS 
- **Database**: SQLite
- **Auth**: Flask Sessions, Bcrypt


# 🏁 Getting Started

 1. Clone the Repository

git clone https://github.com/rohan-sanjay-kadam/Driver_for_hire.git
cd Driver_for_hire

2. Setup A Virtual Environment
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install Dependencies
   pip install -r requirements.txt
   OR
   pip install Flask Flask-Bcrypt Flask-SQLAlchemy

4. Run The App
   python app.py
