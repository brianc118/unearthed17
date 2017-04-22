from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def root(name=None):
    return render_template('hello.html', name=name)

app.run()