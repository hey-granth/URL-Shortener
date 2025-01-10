import qrcode
import os
from flask import url_for

os.makedirs("static/qr_codes", exist_ok=True)


def generate_qr_code(small_url):
    path = os.path.join("static/qr_codes", f"{small_url}.png")
    qr = qrcode.make(url_for("main.redirect", small_url=small_url, _external=True))
    # here, the url_for() function is used to generate the URL for the redirect endpoint. The _external=True argument is used to generate an absolute URL. This is necessary because the QR code will be displayed on a different domain than the one where the application is running.
    # qrcode.make function is used to generate the QR code image.
    # 'api.redirect' is the endpoint that will redirect the user to the original URL when the QR code is scanned.

    qr.save(path)
    return url_for("static", filename=f"qr_codes/{small_url}.png", _external=True)
    # This returns the URL for the QR code image. The _external=True argument is used to generate an absolute URL. This is necessary because the QR code will be displayed on a different domain than the one where the application is running.
