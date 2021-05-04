#!/usr/bin/python3
"""[This is a script that starts a Flask web application]
"""

from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/cities_by_states')
def states_list():
    """[Sets the route for cities by states]
    """
    state = storage.all(State)
    return render_template('8-cities_by_states.html', States=state)


@app.teardown_appcontext
def teardown(context):
    """[This closes the file storage mehtod]
    """
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
