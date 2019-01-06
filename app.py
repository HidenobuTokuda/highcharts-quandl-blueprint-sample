from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config.from_object(Config)
bootstrap = Bootstrap(app)
app.jinja_env.filters['zip'] = zip

#from app import routes
from app.routes import app1
modules_define = [app1]
for app1 in modules_define:
    app.register_blueprint(app1)

if __name__ == '__main__':
    app.run()