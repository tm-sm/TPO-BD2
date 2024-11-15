# -*- coding: utf-8 -*-

from pymongo import MongoClient
import pandas as pd

client = MongoClient("mongodb://localhost:27017/")  
db = client['Negocio']
collection = db['Clientes']

pipeline = [
    {
        "$match": {
            "nombre": "Jacob",       
            "apellido": "Cooper"     
        }
    },
    {
        "$lookup": {
            "from": "Telefonos",        
            "localField": "nro_cliente", 
            "foreignField": "nro_cliente", 
            "as": "telefonos"             
        }
    }
]

result = list(db.Clientes.aggregate(pipeline))

df = pd.DataFrame(result)

df['telefonos'] = df['telefonos'].apply(lambda x: [f"{item['codigo_area']}-{item['nro_telefono']}" for item in x] if isinstance(x, list) else [])

df = df[['nombre', 'apellido', 'telefonos']]


