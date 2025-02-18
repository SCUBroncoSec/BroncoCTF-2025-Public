from flask import Flask, jsonify, send_from_directory
import os

app = Flask(__name__, static_folder="dist")

@app.route("/mary/<sequence>")
def mary(sequence):
    if sequence == "32123332223993212333322321":
        return jsonify({"message": "bronco{W0ah_y0u_f0und_m4rys_1itt1e_1amb}"})
    return jsonify({"message": "WRONG"})

@app.route("/health")
def health():
    return "ok"

@app.route("/users")
def users():
    return "respond with a resource"

# Serve frontend
@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")

@app.route("/<path:path>")
def static_files(path):
    return send_from_directory(app.static_folder, path)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=False)
