from flask import Flask,render_template    #import Flask Class

app = Flask(__name__)       # create app object

@app.route('/')              #create a page on the first url

def hello_world():
  return render_template('home.html')

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug = True)