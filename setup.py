from setuptools import setup, find_packages

setup(
    name="url-shortener",
    version="0.1.0",
    author="Granth Agarwal",
    author_email="heygranth@gmail.com",
    description="",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    python_requires=">=3.12,<4.0",
    install_requires=[
        "blinker==1.9.0",
        "click==8.1.8",
        "flask==3.1.0",
        "greenlet==3.1.1",
        "hashids==1.3.1",
        "itsdangerous==2.2.0",
        "jinja2==3.1.5",
        "markupsafe==3.0.2",
        "python-dotenv==1.0.1",
        "qrcode==8.0",
        "sqlalchemy==2.0.36",
        "typing-extensions==4.12.2",
        "werkzeug==3.1.3",
        "requests==2.32.3",
    ]
)