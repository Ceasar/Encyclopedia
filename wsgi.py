import os

from app import create_app


application = create_app(os.environ['ACCESS_TOKEN'])


if __name__ == "__main__":
    application.run(debug=True, port=5001)
