from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Aplicativo Web com Python Flask!'
app.run()