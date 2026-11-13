from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Real-Time Jenkins CI/CD Pipeline Project",
        "status": "Application Running",
        "version": "1.0.0"
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "UP"
    }), 200

@app.route("/api/info")
def info():
    return jsonify({
        "application": "DevOps CI/CD Demo",
        "technology": "Python Flask",
        "deployment": "Jenkins + Docker + Kubernetes"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
