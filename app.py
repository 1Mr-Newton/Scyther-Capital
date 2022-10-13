from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/',methods=['POST', 'GET'])
def homepage():
  return render_template('index.html')


@app.route('/signup',methods=['POST', 'GET'])
def signup():
  return render_template('signup.html')


@app.route('/login',methods=['POST', 'GET'])
def login():
  return render_template('login.html')

@app.route('/forgotpassword',methods=['POST', 'GET'])
def forgotPassword():
  return render_template('forgotpassword.html')





@app.route('/dashboard',methods=['POST', 'GET'])
def dashboard():
  return render_template('dashboard.html')








if __name__ == "__main__":app.run(debug=True)
  