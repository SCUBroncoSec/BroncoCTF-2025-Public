from flask import Flask, request, jsonify, render_template_string
import jwt
import datetime
import random

app = Flask(__name__)

FLAG_PATH = "flag.txt"

if not os.path.exists(FLAG_PATH):
    with open(FLAG_PATH, "w") as f:
        f.write("error-reading-flag-from-file-contact-an-admin-asap")

def get_flag():
    with open(FLAG_PATH, "r") as f:
        return f.read().strip()

FLAG = get_flag()

# For JWT Signing
SECRET_KEY = "MIKU_SUPER_SECRET_39YZ_MIKU_SUPER_SECRET_39YZ_MIKU_SUPER_SECRET_39YZ_MIKU_SUPER_SECRET_39YZ_MIKU_SUPER_SECRET_39YZ_MIKU_SUPER_SECRET_39YZ_MIKU_SUPER_SECRET_39YZ_MIKU_SUPER_SECRET_39YZ_MIKU_SUPER_SECRET_39YZ_MIKU_SUPER_SECRET_39YZ_MIKU_SUPER_SECRET_39YZ_MIKU_SUPER_SECRET_39YZ_MIKU_SUPER_SECRET_39YZ_MIKU_SUPER_SECRET_39YZ_MIKU_SUPER_SECRET_39YZ_MIKU_SUPER_SECRET_39YZ_MIKU_SUPER_SECRET_39YZ_MIKU_SUPER_SECRET_39YZ_MIKU_SUPER_SECRET_39YZ_MIKU_SUPER_SECRET_39YZ_MIKU_SUPER_SECRET_39YZ_MIKU_SUPER_SECRET_39YZ_MIKU_SUPER_SECRET_39YZ_MIKU_SUPER_SECRET_39YZ_MIKU_SUPER_SECRET_39YZ_"

# List of YouTube video URLs
YOUTUBE_VIDEOS = [
    "https://www.youtube.com/watch?v=NocXEwsJGOQ",
    "https://www.youtube.com/watch?v=OuLZlZ18APQ",
    "https://www.youtube.com/watch?v=jhl5afLEKdo",
    "https://www.youtube.com/watch?v=LaEgpNBt-bQ",
    "https://www.youtube.com/watch?v=yPuI4l0jK7s",
]

# Function to extract YouTube video ID from URL
def get_random_video_id():
    url = random.choice(YOUTUBE_VIDEOS)
    return url.split("v=")[-1].split("&")[0]  # Extract video ID

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Hatsune Miku Fan Club</title>
    <style>
        body { 
            font-family: Arial, sans-serif; 
            text-align: center; 
            background-color: #87CEFA; 
        }
        h1 { color: #00AEEF; }
        img { width: 300px; }
        .container { 
            background: white; 
            padding: 20px; 
            border-radius: 10px; 
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); 
            display: inline-block;
            margin-top: 20px;
        }
        button {
            margin-top: 20px;
            padding: 10px 20px;
            font-size: 16px;
            background-color: #00AEEF;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        iframe {
            margin-top: 20px;
            width: 560px;
            height: 315px;
            border: none;
        }
    </style>
    <script>
        function magicMikuLogin() {
            fetch('/get_token')
            .then(response => response.json())
            .then(data => {
                let token = data.your_token;
                fetch('/login', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
                    body: 'magic_token=' + encodeURIComponent(token)
                })
                .then(response => response.text())
                .then(result => document.body.innerHTML = result);
            });
        }
    </script>
</head>
<body>
    <h1>Welcome to Hatsune Miku's Fan Club</h1>
    
    <h3>Registered Users: miku_user & miku_admin</h3>
    <div class="container">
       <button onclick="magicMikuLogin()">✨ Magic Miku Login ✨</button>
    </div>
    <br>
    <div class="container">
    {% if video_id %}
        <iframe src="https://www.youtube.com/embed/{{ video_id }}" allowfullscreen></iframe>
    {% endif %}
    </div>
    <br>
    <div class="container">
        <h3>{{ message }} </h3>
    </div>
</body>
</html>
"""

@app.route("/")
def index():
    video_id = get_random_video_id()
    return render_template_string(HTML_TEMPLATE, message="Not logged in", video_id=video_id)

@app.route("/get_token")
def get_token():
    token = jwt.encode(
        {"sub": "miku_user", "exp": datetime.datetime.now(datetime.UTC) + datetime.timedelta(minutes=10)},
        SECRET_KEY,
        algorithm="HS256"
    )
    return jsonify({"your_token": token})

@app.route("/login", methods=["POST"])
def login():
    token = request.form.get("magic_token")

    try:
        # Decode the token WITHOUT verifying the signature if 'none' is used
        header = jwt.get_unverified_header(token)

        if header["alg"] == "none":
            decoded = jwt.decode(token, options={"verify_signature": False})
        else:
            decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])

        user = decoded.get("sub", "")

        if user == "miku_admin":
            return f"<h2>Welcome, Miku Admin! Here's your flag: {FLAG}</h2>"
        else:
            return render_template_string(HTML_TEMPLATE, message="Access Denied: You are not miku_admin!", video_id=get_random_video_id())

    except Exception as e:
        return render_template_string(HTML_TEMPLATE, message="Invalid Magic Login!", video_id=get_random_video_id())

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=80)
