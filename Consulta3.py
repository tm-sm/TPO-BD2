# -*- coding: utf-8 -*-

from pymongo import MongoClient
import pandas as pd

client = MongoClient("mongodb://localhost:27017/")  
db = client['Negocio']
collection = db['Telefonos']  

pipeline = [
    {
        "$lookup": {
            "from": "Clientes",        
            "localField": "nro_cliente", 
            "foreignField": "nro_cliente", 
            "as": "cliente"             
        }
    },
    {
        "$unwind": {
            "path": "$cliente",  
            "preserveNullAndEmptyArrays": True  
        }
    }
]

result = list(db.Telefonos.aggregate(pipeline))

df = pd.DataFrame(result)

df['telefono'] = df['codigo_area'].astype(str) + '-' + df['nro_telefono'].astype(str)

cliente_df = df['cliente'].apply(pd.Series)

df = pd.concat([df, cliente_df], axis=1)

df = df[['telefono', 'nombre', 'apellido', 'direccion', 'activo']]
for result in df.values:
    print(result)
