from flask import Flask, request, jsonify, abort

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({"message": "Hello from Flask app!"})

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

@app.route("/add", methods=["GET"])
def add():
    # example: /add?a=2&b=3
    try:
        a = request.args.get("a", type=float)
        b = request.args.get("b", type=float)
        if a is None or b is None:
            return jsonify({"error": "missing a or b"}), 400
        return jsonify({"a": a, "b": b, "sum": a + b})
    except Exception:
        abort(400)
