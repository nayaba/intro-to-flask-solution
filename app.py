from flask import Flask
app = Flask(__name__)

personnel = {
    "rachel": "Executive Vice President of Managerial Functions",
    "wallace": "Senior Vice President of Managerial Functions",
    "rosie": "Staff Vice President of Managerial Functions",
    "james": "Vice Vice President of Managerial Functions",
    "henri": "Junior Vice President of Managerial Functions"
}

@app.route('/')
def index():
    return 'Hello Flask!'

@app.route('/information') 
def info():
    return 'Flask is the micro-framework of choice for building Machine Learning API endpoints'

@app.route('/profile/<name>')
def profile(name):
    return f"This is the profile information for {name.upper()}"

@app.route('/personnel/<name>')
def personnel_query(name):
    return personnel[name]

if __name__ == '__main__':
    app.run()