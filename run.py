from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)

# after creation and structuring of package, do `python3 run.py`
