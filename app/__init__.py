from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__, static_folder="uploads")
bootstrap = Bootstrap(app)



from app.main import routes, errors