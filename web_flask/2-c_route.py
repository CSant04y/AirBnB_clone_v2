#!/usr/bin/python3
"""[This Starts the Flask Application]
"""

if __name__ == '__main__':
    from flask import Flask

    app = Flask(__name__)
    app.url_map.strict_slashes = False

    @app.route('/')
    def hello_HBNB():
        """[This stes the route for hello_hbnb]
        """
        return "Hello HBNB!"

    @app.route('/hbnb')
    def HBNB():
        """[This route displays HBHB]
        """
        return "HBNB"

    @app.route('/c/<text>')
    def print_C(text):
        """[/c/<text> Displays C followed by the value of the text]
        """
        new_str = text.replace('_', ' ')
        return "C {}".format(new_str)

    app.run(host='0.0.0.0', port='5000')
