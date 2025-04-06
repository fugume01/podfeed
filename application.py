# from flask import Flask
# application = Flask(__name__)

# replace above with podfeed app. This should pull in the podfeed specific stuff
from server import app as application

@application.route('/')
def hello_elastic_beanstalk():
        return 'Hello Elastic Beanstalk, from steveo!'
