from pymongo import MongoClient
from neo4j import GraphDatabase


client = MongoClient("mongodb://mongo:27017/")  
db = client['Negocio']
collection = db['Clientes']

driver=GraphDatabase.driver(uri="bolt://neo4j:7687")   
session=driver.session()

clients= list(db.Clientes.find({},{"_id":0}))

result=[]
for client in clients:
    query="""MATCH (f:Factura {nro_cliente:$nro_cliente})
    return f
    """
    neo_query_result=session.run(query,nro_cliente=client['nro_cliente'])
    if neo_query_result.peek() is not None:
        result.append(client)
for client in result:
    print(client)