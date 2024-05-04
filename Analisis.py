from bs4 import BeautifulSoup
import requests
import json
import pandas as pd
import numpy as np
from Automatizacion import Crear_registro

def Assessment_extract(jsondata,folio):
    #variables
    try:
        data = pd.DataFrame(jsondata['Assessment']['AssessmentInfos'])
        data['folio'] = [ folio for x in range(len(jsondata['Assessment']['AssessmentInfos']))]

        #Guardar Assessment
        data.to_csv(f'Resultados_apriori/aseessment_{folio}.csv',index=False)
    except:pass
    
def Benefit_extract(jsondata,folio):
    #variables
    try:
        data = pd.DataFrame(jsondata['Benefit']['BenefitInfos'])
        data['folio'] = [ folio for x in range(len(jsondata['Benefit']['BenefitInfos']))]

        #eliminar columnas no deseadas
        listas_impotrtantes =['folio','Description','TaxYear','Type']
        data_objetivo = data[listas_impotrtantes]
        data_objetivo.to_csv(f'Resultados_apriori/benefit_{folio}.csv',index=False)
    except:pass


def Building_extract(jsondata,folio):
    #variables
    try:
        data = pd.DataFrame(jsondata['Building']['BuildingInfos'])
        data['folio'] = [ folio for x in range(len(jsondata['Building']['BuildingInfos']))]

        #buscar columnas de interes
        lista_importante =['folio','Actual','ActualArea','DepreciatedValue','BuildingNo']
        data_objetivo = data[lista_importante]
        data_objetivo.to_csv(f'Resultados_apriori/building_{folio}.csv',index=False)
    except:pass

def Land_extract(jsondata,folio):
    #variables
    try:
        data = pd.DataFrame(jsondata['Land']['Landlines'])
        data['folio'] = [ folio for x in range(len(jsondata['Land']['Landlines']))]

        #buscar columnas de interes
        lista_importante =['folio','LandUse','LandlineType','MuniZone','PAZoneDescription','UnitType','Units','UseCode','Zone','RollYear']
        data_objetivo = data[lista_importante]
        data_objetivo.to_csv(f'Resultados_apriori/Land_{folio}.csv',index=False)
    except:pass

def Mailing_extract(jsondata,folio):
     #variables
    try:
        data = pd.DataFrame([jsondata['MailingAddress']])
        data['folio'] =folio

        #buscar columnas de interes
        lista_importante =['folio','Address1','City','ZipCode']
        data_objetivo = data[lista_importante]
        data_objetivo.to_csv(f'Resultados_apriori/Mailing_{folio}.csv',index=False)
    except:pass

def Owner_extract(jsondata,folio):
     #variables
    try:
        data = pd.DataFrame([*jsondata['OwnerInfos']])
        data['folio'] =folio
        #buscar columnas de interes
        lista_importante =['folio','MarriedFlag','Name']
        data_objetivo = data[lista_importante]
        data_objetivo.to_csv(f'Resultados_apriori/OwnerInfos_{folio}.csv',index=False)
    except:pass

def Propirety_extract(jsondata,folio):
     #variables
    try:
        data = pd.DataFrame([jsondata['PropertyInfo']])
        data['folio'] =folio
        #buscar columnas de interes
        lista_importante = [
        'folio','BathroomCount', 'BedroomCount', 'BuildingActualArea', 'BuildingBaseArea',
        'BuildingEffectiveArea', 'DORCode', 'DORDescription', 'FolioNumber', 'HxBaseYear',
        'LotSize', 'Municipality', 'ParentFolio', 'PercentHomesteadCapped', 'PlatBook',
        'PlatPage', 'PrimaryZone', 'PrimaryZoneDescription', 'Status', 'Subdivision',
        'SubdivisionDescription', 'UnitCount', 'YearBuilt']
        data_objetivo = data[lista_importante]
        data_objetivo.to_csv(f'Resultados_apriori/Properity_{folio}.csv',index=False)
    except:pass


def Sales_extract(jsondata,folio):
     #variables
    try:
        data = pd.DataFrame(jsondata['SalesInfos'])
        data['folio'] =[folio for x in range(len(jsondata['SalesInfos']))]
        #buscar columnas de interes
        lista_importante = [
            "folio","DateOfSale", "GranteeName1", "GrantorName1", "GrantorName2",
            "OfficialRecordBook", "OfficialRecordPage", "QualificationDescription", 
            "QualifiedFlag", "ReasonCode", "SaleId", "SaleInstrument", "SalePrice", 
            
        ]
        data_objetivo = data[lista_importante]
        data_objetivo.to_csv(f'Resultados_apriori/Sales_{folio}.csv',index=False)
    except:pass
def Site_extract(jsondata,folio):
    #variables
    try:
        data = pd.DataFrame(jsondata['SiteAddress'])
        data['folio'] =[folio for x in range(len(jsondata['SiteAddress']))]
        #buscar columnas de interes
        lista_importante = [
            "folio","StreetName","StreetNumber","StreetPrefix","StreetSuffix","Zip",
            "Address"]
        data_objetivo = data[lista_importante]
        data_objetivo.to_csv(f'Resultados_apriori/Site_{folio}.csv',index=False)
    except:pass

def Taxable_extract(jsondata,folio):
    #Variable
    try:
        data = pd.DataFrame(jsondata['Taxable']['TaxableInfos'])
        data['folio'] =[folio for x in range(len(jsondata['Taxable']['TaxableInfos']))]
        #buscar columnas de interes
        lista_importante = [
        "folio","CityExemptionValue", "CityTaxableValue", "CountyExemptionValue", 
        "CountyTaxableValue", "RegionalExemptionValue", "RegionalTaxableValue", 
        "SchoolExemptionValue", "SchoolTaxableValue"]

        data_objetivo = data[lista_importante]
        data_objetivo.to_csv(f'Resultados_apriori/Taxes_{folio}.csv',index=False)
    except:pass

def  Other_extract(jsondata,folio):
    #values 
    try:
        dicc = {"folio":folio,"Legal_description":jsondata['LegalDescription']['Description'],"District":jsondata['District']}
        data = pd.DataFrame([dicc])
        data.to_csv(f'Resultados_apriori/main_{folio}.csv',index=False)
    except:pass

# extraer la informacion 
def Extract_info(folio):
    #extraer infomracion del folio
    contenido = requests.get(f'https://www.miamidade.gov/Apps/PA/PApublicServiceProxy/PaServicesProxy.ashx?Operation=GetPropertySearchByFolio&clientAppName=PropertySearch&folioNumber={folio}')
    jsondata=json.loads(contenido.text)
    print(jsondata.keys()) 

    #deteccion de la existencia del folio
    if  jsondata['Message'] =="":
        #extraccion de datos
        Assessment_extract(jsondata=jsondata,folio=folio)
        Benefit_extract(jsondata=jsondata,folio=folio)
        Building_extract(jsondata=jsondata,folio=folio)
        Land_extract(jsondata,folio)
        Mailing_extract(jsondata,folio)
        Owner_extract(jsondata,folio)
        Propirety_extract(jsondata,folio)
        Sales_extract(jsondata,folio)
        Site_extract(jsondata,folio)
        Taxable_extract(jsondata,folio)
        Other_extract(jsondata,folio)

            #Agrupar los datos
        Crear_registro()
        return 'folio encontrado'
    #En caso de no encontrar el folio
    else:
        return "folio no encontrado" 




# Extract_info('3040090730050')
# Extract_info('0530240010410')