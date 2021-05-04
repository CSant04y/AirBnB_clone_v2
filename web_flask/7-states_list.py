#!/usr/bin/python3
"""[This is a script that starts a Flask web application]
"""

from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list')
def states_list():
    """[Sets the route for states_list]
    """
    state = storage.all(State)
    return render_template('7-states_list.html', States=state)


@app.teardown_appcontext
def teardown(context):
    """[This closes the file storage mehtod]
    """
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
