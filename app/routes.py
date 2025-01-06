from flask import request, Blueprint, jsonify
from .shortener import shorten_url, get_original_url
from .qr_code import generate_qr_code

main = Blueprint("main", __name__)


@main.route("/api/shorten/<url>", methods=["POST"])
def shorten(url):
    data = request.get_json
    # get_json() is a method that returns the JSON payload of the request as a Python dictionary. Hence, data basically stores the JSON payload of the request as a Python dictionary.

    original_url = data["url"]
    # This is the original URL that the user wants to shorten

    if not original_url:
        return jsonify({"error": "URL is required"}), 400

    small_url = shorten_url(original_url)
    # This will return the shortened URL
    qr_code_url = generate_qr_code(small_url)
    # This will return the URL for the QR code image

    return jsonify({"small_url": small_url, "qr_code_url": qr_code_url}), 201
    # 201 is the status code for created. This is used to indicate that the resource has been created successfully.

@main.route('/<small_url>', methods=['GET'])
def redirect(small_url):
    original_url = get_original_url(small_url)
    # This will return the original URL for the shortened URL
    if not original_url:
        return jsonify({"error": "URL not found"}), 404
    # 404 is the status code for not found. This is used to indicate that the requested resource could not be found.

    return jsonify({"original_url": original_url}), 200
    # 200 is the status code for OK. This is used to indicate that the request has succeeded.
