from neo4j import GraphDatabase


driver = GraphDatabase.driver(uri="bolt://localhost:7687")   
session = driver.session()

query = """
    MATCH (f:Factura)
    RETURN f
    ORDER BY f.fecha ASC;
    """

neo_query_result = session.run(query)

print(f"{'id'.ljust(10)} | {'fecha'.ljust(12)} | {'iva'.ljust(6)} | {'total con iva'.ljust(15)} | {'total sin iva'.ljust(15)}")
print("--------------------------------------------------------------------------")
for record in neo_query_result:
    factura_node = record["f"]

    print(f"{str(factura_node['nro_factura']).ljust(10)} | " +
        f"{str(factura_node['fecha']).ljust(12)} | " +
        f"{str(factura_node['iva']).ljust(6)} | " +
        f"{str(factura_node['total_con_iva']).ljust(15)} | " +
        f"{str(factura_node['total_sin_iva']).ljust(15)}")

session.close()