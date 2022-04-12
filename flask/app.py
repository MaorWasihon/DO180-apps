from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
   return render_template('index.html')


@app.route("/who")
def who():
   return "My name is TONY MONTOYA !"


@app.route("/health")
def health():
   return "{ health : ok }"






if __name__ == "__main__":
  app.run(debug=True,host='127.0.0.1',port=80) 
