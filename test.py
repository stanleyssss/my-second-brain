from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    notes = "Hello, My knowledge Base!"
    return render_template('index.html', notes=notes)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)