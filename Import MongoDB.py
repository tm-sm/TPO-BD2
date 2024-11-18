# -*- coding: utf-8 -*-

from pymongo import MongoClient
import pandas as pd

client = MongoClient('mongodb://localhost:27017/')

# clientes
db = client['Negocio']
collection = db['Clientes']
data = pd.read_csv('Data/e01_cliente.csv', encoding="iso-8859-1" ,delimiter=';')
records = data.to_dict(orient='records')
collection.create_index("nro_cliente",unique=True)
collection.insert_many(records)

#telefonos
collection = db['Telefonos']
data = pd.read_csv('Data/e01_telefono.csv', encoding="ascii", delimiter=';')
records = data.to_dict(orient='records')
collection.insert_many(records)