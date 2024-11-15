# -*- coding: utf-8 -*-

from pymongo import MongoClient
import pandas as pd

client = MongoClient('mongodb://localhost:27017/')

# clientes
db = client['Negocio']
collection = db['Clientes']
data = pd.read_csv('Data/e01_cliente.csv', encoding = 'ANSI', delimiter=';')
records = data.to_dict(orient='records')
collection.insert_many(records)

#telefonos
collection = db['Telefonos']
data = pd.read_csv('Data/e01_telefono.csv', encoding = 'ANSI', delimiter=';')
records = data.to_dict(orient='records')
collection.insert_many(records)