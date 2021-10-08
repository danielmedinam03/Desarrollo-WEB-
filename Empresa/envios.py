from flask import Flask, render_template, request

#instancia de flask
app = Flask(__name__)


@app.route('/')
def genero():
    
   return render_template("genero.html")

@app.route('/genero', methods=['POST'])
def Enviogenero():
    if request.method == "POST":
        
        genero = request.form['codGenero'] 
    
        print(genero)
        return "REcibido"
    
if __name__=='__main__':
    app.run(port=5000, debug=True)