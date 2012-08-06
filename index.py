from bottle import Bottle, run, route, static_file, view, template, post, request, get_url, SimpleTemplate
SimpleTemplate.defaults["get_url"]=get_url		#pass the get_url object to all the templates - don't mess with this.
#handler to serve static files - don't mess.
@route(/'/static/<filename>', name='static')		#the handler is named 'static' so you can pass the handler to get_url
def server_static(filename):
	return static_file(filename, root="static")
	
@route('/')
def index():
	return template('index')	

run(host='0.0.0.0', port=8080)
