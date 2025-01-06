# Notes

## Hashids
- Hashids is a small open-source library that generates short, unique, non-sequential ids from numbers.
- It converts numbers like 347 into strings like “yr8”, or array of numbers like [27, 986] into “3kTMd”.
- You can also decode those ids back. This is useful in bundling several parameters into one or simply using them as short UIDs.
- Hashids is great for use in URL shortening, tracking stuff, validating accounts, and making pages private.
- Salt is used to make the hashids unique. It is a secret string that will be used to generate the hashids.
- You can find its documentation at [hashids.org](https://hashids.org/python/)

---
## qrcode
- qrcode is a python library that generates QR codes.
- It is a simple library that can be used to generate QR codes.
- You can find its documentation at [pypi.org](https://pypi.org/project/qrcode/)
- It provides the following functions:
    - `qrcode.make(data)`: This function generates a QR code for the given data.
    - `qrcode.make(data).show()`: This function displays the QR code.
    - `qrcode.make(data).save('filename.png')`: This function saves the QR code as a png file.

---