from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
   return 'my app!'


if __name__ == "__main__":
  app.run(debug=True,host='localhost',port=8080) 
