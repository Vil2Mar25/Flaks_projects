from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Aplicativo Web com Python Flask!'
@app.route('/index')
def aa():
    #name='Rosalia'
    #return render_template('index.html',title='Welcome', username=name)

    users = ['Rosalia', 'Adrianna', 'Victoria']
    return render_template('index.html', title='Welcome', members=users)
app.run()