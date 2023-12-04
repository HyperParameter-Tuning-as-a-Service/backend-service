from backend_server import app

import constants

if __name__ == "__main__":
    app.run(ssl_context="adhoc", debug=constants.DEBUG_MODE)
