from flask import Flask, render_template
#python backend file - flask server -

# we are just configuring backend for our wesite in a simple way.


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/prices')
def pricing():
    return render_template('pricing.html')

@app.route('/team')
def team():
    return render_template('team.html')

if __name__ == '__main__':
    app.run(debug=True)


  
 
