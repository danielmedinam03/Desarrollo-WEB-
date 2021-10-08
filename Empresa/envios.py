from flask import Flask, render_template, request

#instancia de flask
app = Flask(__name__)


@app.route('/')
def Index():
   return render_template("index.html")

@app.route('/tablas')
def Tablas():
   return render_template("tablas.html")

@app.route('/genero')
def Genero():
   return render_template("genero.html")

@app.route('/estadoCivil')
def EstadoCivil():
   return render_template("estadoCivil.html")

@app.route('/estrato')
def Estrato():
   return render_template("estrato.html")

@app.route('/formaDePago')
def FormaDePago():
   return render_template("formaDePago.html")

@app.route('/tiposDeID')
def TiposID():
   return render_template("tiposDeID.html")

    
if __name__=='__main__':
    app.run(port=5500, debug=True)