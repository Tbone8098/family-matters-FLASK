from flask_app import app
from flask_app.controllers import controller_routes, controller_user, controller_category, controller_page, controller_block

if __name__=='__main__':
    app.run(debug=True)