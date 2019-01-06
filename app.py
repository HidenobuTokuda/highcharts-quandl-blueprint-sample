from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config.from_object(Config)
bootstrap = Bootstrap(app)
app.jinja_env.filters['zip'] = zip

#from app import routes
from app_chart.routes import app_chart
modules_define = [app_chart]
for module in modules_define:
    app.register_blueprint(module)

if __name__ == '__main__':
    app.run()