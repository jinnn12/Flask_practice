from flask import Flask, jsonify

from Controllers.hello_controller import hello_bp

app = Flask(__name__)

# 127.0.0.1:5000/ping 으로 Get 요청
@app.get("/ping")
def ping():
    return jsonify(ok=True)

# 127.0.0.1:5000 으로 Get 요청 -> Hello future
# @app.get("/")
# def root():
#     return "Hello future"

app.register_blueprint(hello_bp)

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)