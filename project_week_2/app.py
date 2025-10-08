from flask import Flask, render_template

app = Flask(__name__)

# Simple in-memory "database"
user_profile = {
    "name": "Stanley",
    "goals": [
        "Learn Python for AI",
        "Build a 'Second Brain' app",
        "Master Git and GitHub",
        "Understand web development basics"
    ]
}

@app.route('/')
def home():
    """Renders the home page."""
    return render_template('index.html')

@app.route('/about')
def about():
    """Renders the about page with user's name."""
    return render_template('about.html', username=user_profile['name'])

@app.route('/goals')
def goals():
    """Renders the goals page with a list of goals."""
    return render_template('goal.html', goals=user_profile['goals'])

if __name__ == '__main__':
    app.run(debug=True, port=5002)