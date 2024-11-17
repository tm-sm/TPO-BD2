from pymongo import MongoClient
from neo4j import GraphDatabase

mongo_client = MongoClient("mongodb://localhost:27017/")
db = mongo_client['Negocio']
collection = db['Clientes']

driver = GraphDatabase.driver(uri="bolt://localhost:7687", auth=("neo4j", "test"))
session = driver.session()

clients = list(db.Clientes.find({}, {"_id": 0}))

result = []
for client in clients:
    nro_cliente = client['nro_cliente']
    query = """
    MATCH (f:Factura {nro_cliente: $nro_cliente})-[:HAS_ITEM]->(:DetalleFactura)-[:REFERS_TO]->(p:Producto)
    WHERE p.marca CONTAINS 'Ipsum'
    RETURN DISTINCT f.nro_factura AS numero_factura,
                    f.fecha AS fecha,
                    f.total_con_iva AS total_con_iva,
                    f.total_sin_iva AS total_sin_iva,
                    p.nombre AS producto,
                    p.marca AS marca
    """
    neo_query_result = session.run(query, nro_cliente=nro_cliente)
    for record in neo_query_result:
        result.append({
            "numero_factura": record["numero_factura"],
            "fecha": record["fecha"],
            "total_con_iva": record["total_con_iva"],
            "total_sin_iva": record["total_sin_iva"],
            "producto": record["producto"],
            "marca": record["marca"]
        })

print(f"{'Número Factura'.ljust(15)} | {'Fecha'.ljust(12)} | {'Total con IVA'.ljust(15)} | {'Total sin IVA'.ljust(15)} | {'Producto'.ljust(20)} | {'Marca'.ljust(15)}")
print("-" * 100)
for factura in result:
    print(f"{str(factura['numero_factura']).ljust(15)} | " +
          f"{str(factura['fecha']).ljust(12)} | " +
          f"{str(factura['total_con_iva']).ljust(15)} | " +
          f"{str(factura['total_sin_iva']).ljust(15)} | " +
          f"{factura['producto'].ljust(20)} | " +
          f"{factura['marca'].ljust(15)}")

session.close()