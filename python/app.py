from flask import Flask, redirect, url_for, request, render_template
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient()
db = client.HackMann

def hasParams(fields):
	return all(x in request.form for x in fields)
def getSubParams(fields):
	return {k:request.form[k] for k in fields if k in request.form}
def storeFormInDB(collection, requiredFields, uniqueFields):
	print(request.form)
	if hasParams(requiredFields):
		collectionData = getSubParams(requiredFields)

		# Check that there are no documents with equal values for a set of unique keys 
		if uniqueFields != None:
			for field in uniqueFields:
				if collection.find_one({field: collectionData[field]}) != None:
					return "Non unique submission"

		collection.insert_one(collectionData)
		return "Success"
	else:
		return "Bad request"

@app.route('/user', methods=['POST'])
def user():
	return storeFormInDB(db.user, ['firstName', 'lastName', 'school', 'email'], ['email'])

@app.route('/mentor', methods=['POST'])
def mentor():
	return storeFormInDB(db.user, ['firstName', 'lastName', 'organization', 'email'], ['email'])

@app.route('/sponsor', methods=['POST'])
def sponsor():
	return storeFormInDB(db.user, ['firstName', 'lastName', 'organization', 'email'], ['email'])

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)