from flask_app import app
from flask_app.controllers import pages
from flask_app.controllers import actions
from flask_app.controllers import actions_user

if __name__=="__main__":
	app.run(debug=True)