from flask import Flask, render_template, request, flash, redirect, url_for
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

    if request.method == "POST":
        select = "SELECT cCodigoGenero FROM Genero"
        cursor = conexion.cursor()
        cursor.execute(select)

        valores = cursor.fetchall()
        codGenero=request.form['codGenero'].capitalize()
        desGenero=request.form['desGenero'].capitalize()

        if valores.__len__==0:
            cursor = conexion.cursor()

            insert="INSERT INTO Genero(cCodigoGenero, cDescripcionGenero) VALUES('{}','{}')".format(codGenero, desGenero)
            cursor.execute(insert)
            cursor.commit()
            return redirect(url_for('Genero'))
        else:
            flash("Ya existe el Codigo")
            return redirect(url_for('Genero'))
        
    return render_template("genero.html")

@app.route('/estadoCivil',methods=["GET","POST"])
def EstadoCivil():
    
    if request.method == "POST":
        codEstado=request.form['codEstado'].capitalize()
        desEstado=request.form['desEstado'].capitalize()
        print(codEstado, desEstado)
        cursor = conexion.cursor()
        insert="INSERT INTO Genero(cCodigoGenero, cDescripcionGenero) VALUES('{}','{}')".format(codEstado, desEstado)
        cursor.execute(insert)
        cursor.commit()
        return redirect(url_for('EstadoCivil'))
    
    return render_template("estadoCivil.html")

@app.route('/estrato', methods=["GET","POST"])
def Estrato():
    
    if request.method == "POST":
        codGenero=request.form['codGenero'].capitalize()
        desGenero=request.form['desGenero'].capitalize()
        print(codGenero, desGenero)
        cursor = conexion.cursor()
        insert="INSERT INTO Genero(cCodigoGenero, cDescripcionGenero) VALUES('{}','{}')".format(codGenero, desGenero)
        cursor.execute(insert)
        cursor.commit()
        return redirect(url_for('Genero'))
    
    return render_template("estrato.html")

@app.route('/formaDePago', methods=["GET","POST"])
def FormaDePago():
    
    if request.method == "POST":
        codGenero=request.form['codGenero'].capitalize()
        desGenero=request.form['desGenero'].capitalize()
        print(codGenero, desGenero)
        cursor = conexion.cursor()
        insert="INSERT INTO Genero(cCodigoGenero, cDescripcionGenero) VALUES('{}','{}')".format(codGenero, desGenero)
        cursor.execute(insert)
        cursor.commit()
        return redirect(url_for('Genero'))
    
    return render_template("formaDePago.html")

@app.route('/tiposDeID', methods=["GET","POST"])
def TiposID():
    
    if request.method == "POST":
        codGenero=request.form['codGenero'].capitalize()
        desGenero=request.form['desGenero'].capitalize()
        print(codGenero, desGenero)
        cursor = conexion.cursor()
        insert="INSERT INTO Genero(cCodigoGenero, cDescripcionGenero) VALUES('{}','{}')".format(codGenero, desGenero)
        cursor.execute(insert)
        cursor.commit()
        return redirect(url_for('Genero'))
    
    return render_template("tiposDeID.html")

    
if __name__=='__main__':
    app.run(port=5500, debug=True)