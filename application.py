from flask import Flask
 
application = Flask(__name__)

#Set application.debug=true to enable tracebacks on Beanstalk log output. 
#Make sure to remove this line before deploying to production.
application.debug=True
 
@application.route('/')
def hello():
    return "Hello again world!"
 
if __name__ == "__main__":
    application.run(host='0.0.0.0')