from flask import Flask, request, make_response, render_template_string, redirect
import os
import hashlib

app = Flask(__name__)
FLAG_PATH = "flag.txt"

if not os.path.exists(FLAG_PATH):
    with open(FLAG_PATH, "w") as f:
        f.write("error-reading-flag-from-file-contact-an-admin-asap")

def get_flag():
    with open(FLAG_PATH, "r") as f:
        return f.read().strip()

TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Grandma's Bakery</title>
    <style>
        body { font-family: 'Comic Sans MS', cursive, sans-serif; background-color: #ffe5b4; text-align: center; }
        .container { margin-top: 50px; padding: 20px; background: #fff8dc; border-radius: 10px; display: inline-block; box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1); }
        .flag { font-weight: bold; color: green; }
        .btn { display: inline-block; padding: 10px 20px; margin: 10px; background-color: #d2691e; color: white; text-decoration: none; border-radius: 5px; }
        h1 { color: #8b0000; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Welcome to Grandma's Bakery!</h1>
        <p>{{ message }}</p>
        {% if flag %}<p class="flag">Flag: {{ flag }}</p>{% endif %}
        <br>
        <a class="btn" href="/login">Login</a>
        <a class="btn" href="/logout">Logout</a>
        <a class="btn" href="/grandma">Grandma's Pantry</a>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    role = request.cookies.get('role', 'kitchen helper')  # Default role is "kitchen helper"
    checksum = hashlib.md5(role.encode()).hexdigest()
    if role == 'grandma' and request.cookies.get('checksum') == checksum:
        return render_template_string(TEMPLATE, message="Welcome, Grandma! I know you have been struggling with your memory lately, so here is your secret recipe:", flag=get_flag())
    else:
        resp = make_response(render_template_string(TEMPLATE, message="You are logged in as a kitchen helper. Only Grandma can view the secret recipe!"))
        if 'role' not in request.cookies:
            resp.set_cookie('role', 'kitchen helper', httponly=True, secure=True)  # Secure and HttpOnly to add realism
            resp.set_cookie('checksum', hashlib.md5("kitchen helper".encode()).hexdigest(), httponly=True, secure=True)
        return resp

@app.route('/login')
def login():
    resp = make_response(render_template_string(TEMPLATE, message="Welcome to Grandma's kitchen! You are now a 'kitchen helper'. Hun, can you pleae go grab the sugar?"))
    resp.set_cookie('role', 'kitchen helper', httponly=True, secure=True)
    resp.set_cookie('checksum', hashlib.md5("kitchen helper".encode()).hexdigest(), httponly=True, secure=True)
    return resp

@app.route('/logout')
def logout():
    resp = make_response(render_template_string(TEMPLATE, message="You've been kicked out of Grandma's kitchen!"))
    resp.set_cookie('role', '', expires=0)
    resp.set_cookie('checksum', '', expires=0)
    return resp

@app.route('/grandma')
def grandma():
    role = request.cookies.get('role', 'kitchen helper')
    checksum = request.cookies.get('checksum', '')
    if role == 'grandma' and checksum == hashlib.md5(role.encode()).hexdigest():
        return render_template_string(TEMPLATE, message="Grandma's Secret Recipe: ", flag=get_flag())
    return render_template_string(TEMPLATE, message="You are not Grandma! Only Grandma can access this page.")

@app.route('/<path:invalid_path>')
def catch_all(invalid_path):
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=80)
