from flask import Blueprint, jsonify

hello_bp = Blueprint(
    "hello",
    __name__,
    url_prefix="/hello"
)

@hello_bp.get("")
def hello():
    return jsonify(message="hello blueprint")
