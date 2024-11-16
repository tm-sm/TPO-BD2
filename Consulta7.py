from pymongo import MongoClient
from neo4j import GraphDatabase

mongo_client = MongoClient("mongodb://localhost:27017/")  
db = mongo_client['Negocio']
collection = db['Clientes']

driver = GraphDatabase.driver(uri="bolt://localhost:7687")   
session = driver.session()

client = collection.find_one({"nombre": "Kai", "apellido": "Bullock"})

if client:
    nro_cliente = client["nro_cliente"]

    query = """
    MATCH (f:Factura)
    WHERE f.nro_cliente = $nro_cliente
    RETURN f;
    """
    
    neo_query_result = session.run(query, nro_cliente=nro_cliente)

    print(f"{'id'.ljust(10)} | {'fecha'.ljust(12)} | {'iva'.ljust(6)} | {'total con iva'.ljust(15)} | {'total sin iva'.ljust(15)}")
    print("--------------------------------------------------------------------------")

    for record in neo_query_result:
        factura_node = record["f"]

        print(f"{str(factura_node['nro_factura']).ljust(10)} | " +
            f"{str(factura_node['fecha']).ljust(12)} | " +
            f"{str(factura_node['iva']).ljust(6)} | " +
            f"{str(factura_node['total_con_iva']).ljust(15)} | " +
            f"{str(factura_node['total_sin_iva']).ljust(15)}")
else:
    print("Client not found.")

session.close()