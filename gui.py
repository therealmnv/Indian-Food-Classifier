import neural
import basundi

# importing Flask and other modules

# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
# flask used Web Application Framework or simply Web Framework represents a collection of libraries and modules that enables a web application developer to write applications without having to bother about low-level details such as protocols, thread management etc.

from flask import Flask, redirect, url_for, request
app = Flask(__name__)
 
@app.route('/success/<name>')
def success(name):
    
    return f"<h1>{name}</h1>"
 #what this does is maps url to function that is localhost/hello
 #post Used to send HTML form data to server. Data received by POST method is not cached by server.
 #Sends data in unencrypted form to the server. Most common method.default
 #http://localhost/login is mapped to the login() function. 
@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']#getting the string value from nm
      inp=neural.predict(user)
      key=inp.lower()
      lis=basundi.db
      for d in lis:
          if d["name"]==key:
              n=d["name"]
              h=d["history"]
              c=d["calories"]
              l=d["recipe"]
              info=n+h+str(c)+l
              return f"<h1>THE NAME OF THE FOOD IS:{n} <br/> HISTORY:{h} <br/> CALORIES(BEWARE):{c} <br/> RECIPE:{l} </h1>"#returns html file
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))
 
if __name__ == '__main__':
   app.run(debug = True)