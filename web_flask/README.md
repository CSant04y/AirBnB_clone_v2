# web_flask

# 0x04. AirBnB clone - Web framework
## What is a Web Framework?
* A web Framework is a piece of software that offers a way to create and run web applications. These web applications are meant to support web services, web resources, and web API’s(Application Programing Interface).

## How to define routes in Flask
To define a route in Flask you can use the **route()** decorator to bind a function to a URL.
Ex.
```
@app.route('/')
def index():
	return 'Index Page'
@app.route('/hello')
def hello():
	return 'Hello, World'
```
* You can do a lot more with routes such as making parts of the URL dynamic and attach multiple rules to a function.
## What is a route
A route is used to map a Specific URL with its Associated Function which is intended to preform some task.
## How to handle variables in a route
* You can add variable sections to a URL by making the sections with **<variable_name>**.  The function receives the **<variable_name>** as a keyword argument. Optionally you can used a converter to specify the type of argument **<converter:variable_name>**
```
@app.route('/user/<username>')
def show_user_profile(username):
	# Show the user profile for that user
	return 'User %s' % escape(username)
@app.route('/post/<int:post_id>')
def show_post(post_id):
	# Show the post with the given id, the id is an integer
	return 'Post %d' % post_id
@app.route('/path/<path:subpath>')
def show_subpath(subpath):
	# show the subpath after /path/
	return 'Subpath %s' % escape(subpath)
```
## What is a template?
Templates are files that contain static data. They also contain placeholders for dynamic data.  A template is rendered with specific data to produce a final document. Flask uses the Jinja template library to render templates. An example of this would be rendering HTML to display on the users browser. 
* To Render a template you want to use the **render_template()** method.  All you have to do is provide the name to the template and variables that you want to pass to the template engine as keyword arguments.
```
from flask import render_template

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
	return render_template('hello.html', name=name)
```

## How to create a HTML response in Flask by using a template

## How to create a dynamic template (loops, conditions…)
## How to display in HTML data from a MySQL database
