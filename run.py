from backend_server import app

import constants

if __name__ == "__main__":
    app.run(debug=constants.DEBUG_MODE)
