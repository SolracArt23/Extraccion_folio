from flask import Flask,render_template,request,flash,session,jsonify,send_file
import os
from Analisis import Extract_info
import numpy as np
import time

#creacion de la aplicacion
app = Flask(__name__)
informacion = 0
app.secret_key = '12345'


@app.route('/')
def main():
    return render_template('index.html')

@app.route('/extracting',methods=['POST'])
def Statring_folio():
    if request.method =='POST':
        #extracccion de los datos
        folio = request.get_json('folio')['folio']
        cantidad = request.get_json('folio')['cant']
        print(request.get_json('folio'))

        #pruebas previa 
        if int(folio) and len(folio) == 13:
            #retorno de mensaje previo
            flash('Comenzando analisis')

            respuesta = Extract_info(folio)

            informacion = []
            for x in range(int(cantidad)):
                 folio=generar_folio(folio)

                 respuesta=Extract_info(folio)
                 
                 informacion.append({'id':x,'N folio':folio,'estado':respuesta})
                 time.sleep(3)
                 


            return jsonify(informacion)
        #en caso de que el folio no exista
        return 'error datos no estan bien'


@app.route('/descargar')
def descargar_archivo():
    # Ruta al archivo que deseas descargar
    ruta_archivo = 'Plantillas/datos.xlsx'
    # Nombre que se utilizará para el archivo descargado
    nombre_descarga = 'resultado.xlsx'
    # Devolver el archivo como respuesta a la solicitud
    return send_file(ruta_archivo, as_attachment=True)



def generar_folio(pre_folio):
    new_folio = int(pre_folio) +10
    return str(new_folio)
    



# Iniciar aplicacion
if __name__ =='__main__':
    app.run(port=500,host='0.0.0.0',debug=True)