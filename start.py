from wsgiref.simple_server import make_server

from api import main

if __name__ == "__main__":
    """If start.py is called directly, start up the api."""
    server = make_server("0.0.0.0", 6543, main({}))
    server.serve_forever()
