from pymongo import MongoClient
from neo4j import GraphDatabase

mongo_client = MongoClient("mongodb://localhost:27017/")  
db = mongo_client['Negocio']
collection = db['Clientes']

driver = GraphDatabase.driver(uri="bolt://localhost:7687")   
session = driver.session()

clients = list(collection.find())

query = """
    MATCH (f:Factura)
    WHERE f.nro_cliente = $nro_cliente
    RETURN COUNT(f) AS factura_count;
"""

for client in clients:
    nro_cliente = client["nro_cliente"]
    neo_query_result = session.run(query, nro_cliente=nro_cliente)
    
    factura_count = neo_query_result.single()["factura_count"]
    
    print(client["nombre"] + " " + client["apellido"] + " -> " + str(factura_count) + " factura(s)")


session.close()