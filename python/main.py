from flask import Flask, request
app = Flask(__name__)

def areArgsSet(args):
	return all(arg in request.args for arg in args)

@app.route('/user')
def user():
	if request.method == 'GET':
		if areArgsSet(['name', 'school']):
			return 'Hello World!'
	return 'Invalid request to endpoints'

if __name__ == '__main__':
	app.debug = True
	app.run()
