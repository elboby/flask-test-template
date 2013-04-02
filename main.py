from app import create_app


if __name__ == "__main__":
    app = create_app('AU/templates/')
    app.run(debug=True)