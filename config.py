import os
import quandl

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    quandl.ApiConfig.api_key = os.environ.get('API_KEY') or "coMpzT82DE4TQXC8y_kG"