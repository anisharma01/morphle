from flask import Flask
import os
import datetime
import subprocess

app = Flask(__name__)

def get_top_output():
    return subprocess.getoutput("top -b -n 1 | head -10")

@app.route('/htop')
def htop():
    name = "Anish Sharma"
    username = os.getenv("USER", "user_anish")
    server_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S IST")
    top_output = get_top_output().replace("\n", "<br>")

    return f"""
    <h1>System Info</h1>
    <p><b>Name:</b> {name}</p>
    <p><b>Username:</b> {username}</p>
    <p><b>Server Time (IST):</b> {server_time}</p>
    <h2>Top Output:</h2>
    <pre>{top_output}</pre>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
