from flask import Blueprint, jsonify, send_from_directory, current_app
import os

api_bp = Blueprint("api", __name__)

@api_bp.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "ok"}), 200

@api_bp.route("/swagger.json", methods=["GET"])
def swagger_spec():
    folder = os.path.dirname(os.path.abspath(__file__))
    return send_from_directory(folder, "swagger.json")