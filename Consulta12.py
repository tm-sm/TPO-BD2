from neo4j import GraphDatabase


driver = GraphDatabase.driver(uri="bolt://localhost:7687")   
session = driver.session()

# Update the label
session.run("""
    MATCH (p:Producto)
    WHERE NOT EXISTS {
        MATCH (:DetalleFactura)-[:REFERS_TO]->(p)
    }
    SET p:producto_no_facturado;
    """)

query = """
    MATCH (p:producto_no_facturado)
    RETURN p;
    """

neo_query_result = session.run(query)

print(f"{'codigo'.ljust(10)} | {'marca'.ljust(12)} | {'nombre'.ljust(10)} | {'descripcion'.ljust(20)} | {'precio'.ljust(15)} | {'stock'.ljust(15)}")
print("--------------------------------------------------------------------------")

for record in neo_query_result:
    producto = record["p"]

    print(f"{str(producto['codigo_producto']).ljust(10)} | " +
        f"{str(producto['marca']).ljust(12)} | " +
        f"{str(producto['nombre']).ljust(6)} | " +
        f"{str(producto['descripcion']).ljust(15)} | " +
        f"{str(producto['precio']).ljust(15)} | " +
        f"{str(producto['stock']).ljust(15)}")


session.close()