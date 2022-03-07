from flask_app import app
from flask_app.controllers import controller_user, controller_category, controller_page, controller_block, controller_post, controller_routes, controller_refit_page, controller_playlist, controller_song

if __name__=='__main__':
    app.run(debug=True, host="0.0.0.0")