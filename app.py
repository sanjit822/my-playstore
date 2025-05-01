from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home page route
@app.route('/')
def index():
    return render_template('index.html')

# Apps page route
@app.route('/apps')
def apps():
    return render_template('apps.html')

# Games page route
@app.route('/games')
def games():
    return render_template('games.html')

# Downloads page route
@app.route('/downloads')
def downloads():
    return render_template('downloads.html')

# Search page route
@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        query = request.form.get('search-query')
        # Dummy search results
        search_results = ['Sky Racer', 'Photo Editor Pro', 'Jungle Escape']
        return render_template('search.html', query=query, results=search_results)
    return render_template('search.html', query=None, results=None)

# About page route
@app.route('/about')
def about():
    return render_template('about.html')

# Admin page route
@app.route('/admin')
def admin():
    return render_template('admin.html')

# Details page route
@app.route('/details')
def details():
    return render_template('details.html')

# Login page route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        # Authentication logic would go here
        return redirect(url_for('profile'))
    return render_template('login.html')

# Profile page route
@app.route('/profile')
def profile():
    return render_template('profile.html')

# Register page route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        # Save to database logic goes here
        return redirect(url_for('login'))
    return render_template('register.html')

# Thank You page route
@app.route('/thank_you', methods=['GET', 'POST'])
def thank_you():
    if request.method == 'POST':
        name = request.form.get('feedback-name')
        message = request.form.get('feedback-message')
        print(f"Feedback received from {name}: {message}")
        return render_template('thank_you.html', success_message="Thank you for your feedback!")
    return render_template('thank_you.html')

# Contact page route
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        print(f"Contact form received from {name} ({email}): {message}")
        return redirect(url_for('thank_you'))
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
