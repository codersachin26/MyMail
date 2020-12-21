
from flask import Flask
from db_connect import make_db_connection

app = Flask(__name__)
app.secret_key = 'flaskISAwesome'


if __name__ == '__main__':
    app.run(debug=True)
