from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
   return 'This is Home!'

@app.route('/service/healthy')
def healthCheck():
   return '', 200

if __name__ == '__main__':  
   app.run('0.0.0.0',port=8080,debug=True)