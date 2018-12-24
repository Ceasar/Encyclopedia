import os

from app import create_app


app = create_app(os.environ['ACCESS_TOKEN'])


if __name__ == "__main__":
    app.run(debug=True, port=5001)
