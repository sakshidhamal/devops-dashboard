from flask import Flask, render_template, jsonify
import psutil

app = Flask(__name__)

def get_system_stats():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    return {
        "cpu": cpu,
        "memory": memory,
        "disk": disk
    }

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/stats')
def stats():
    return jsonify(get_system_stats())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)