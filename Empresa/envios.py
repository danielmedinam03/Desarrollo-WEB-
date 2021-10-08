from flask import Flask, render_template, request
import os
import pyodbc

#instancia de flask
app = Flask(__name__)

# Ruta actual de la carpeta donde se esta trabajando
# Conexion a la BD
ruta = os.getcwd()

cadenaRutaBD = ruta + '\BD\EmpresaBD.accdb;'
driver = "Microsoft Access Driver (*.mdb, *.accdb)"
cadena = (r'DRIVER={};DBQ={}').format(driver, cadenaRutaBD)

conexion = pyodbc.connect(cadena)

@app.route('/', methods=["GET","POST"])
def Index():
    return render_template("index.html")

@app.route('/tablas', methods=["GET","POST"])
def Tablas():
    return render_template("tablas.html")

@app.route('/genero', methods=["GET","POST"])
def Genero():
    
    codGenero = request.args.get("codGenero")
    desGenero = request.args.get("desGenero")

    #codGenero=(request.form['codGenero'])
    #desGenero=(request.form['desGenero'])
    print(codGenero, desGenero)
    
    insert="INSERT INTO Genero(cCodigoGenero, cDescripcionGenero) VALUES('{}','{}')".format(codGenero, desGenero)
    cursor = conexion.cursor()
    cursor.execute(insert)
    cursor.commit()
    
    if request.method == "POST":
        return render_template("genero.html")
    return render_template("genero.html")

@app.route('/estadoCivil',methods=["GET","POST"])
def EstadoCivil():
    return render_template("estadoCivil.html")

@app.route('/estrato', methods=["GET","POST"])
def Estrato():
    return render_template("estrato.html")

@app.route('/formaDePago', methods=["GET","POST"])
def FormaDePago():
    return render_template("formaDePago.html")

@app.route('/tiposDeID', methods=["GET","POST"])
def TiposID():
    return render_template("tiposDeID.html")

    
if __name__=='__main__':
    app.run(port=5500, debug=True)