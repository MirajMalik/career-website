from flask import Flask     #import Flask Class

app = Flask(__name__)       # create app object

@app.route('/')              #create a page on the first url

def hello_world():
  return "Hello, Miraj"

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug = True)