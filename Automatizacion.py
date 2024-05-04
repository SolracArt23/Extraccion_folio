import os
import pandas as pd
import numpy as np
import shutil

def Crear_registro():
    #variables
    try:
        excel_dt = pd.read_excel('Plantillas/datos.xlsx',sheet_name=None)
    except:
        excel_dt = []
    excel = pd.ExcelWriter('Plantillas/datos.xlsx')
    #leer los csv
    for directorio,_,archivos in os.walk('Resultados_apriori'):
        for archivo in archivos:
            nombre_hoja = archivo.split('_')[0]
            dataframe = pd.read_csv(directorio+'/'+archivo)
            #crear hojas en el archvio excel
            if len(excel_dt) <=1:
                dataframe.to_excel(excel,sheet_name=nombre_hoja,index=False)

            else:#agregar nuevos datos
                dataframe_result = pd.concat([dataframe,excel_dt[nombre_hoja]],ignore_index=True)

                dataframe_result.to_excel(excel,sheet_name=nombre_hoja,index=False)


        excel._save()

    #eliminar las tablas de la carpeta priori
    shutil.rmtree('Resultados_apriori')
    os.mkdir('Resultados_apriori')

