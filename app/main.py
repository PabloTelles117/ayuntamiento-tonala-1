from app import app
from utils.db import mysql


mysql.init_app(app)


if __name__ == '__main__':
	app.run(debug=True, host="0.0.0.0")
