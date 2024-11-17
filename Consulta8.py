from neo4j import GraphDatabase

class ProductQuery:
    def __init__(self, uri, username, password):
        self.driver = GraphDatabase.driver(uri, auth=(username, password))

    def close(self):
        self.driver.close()

    def get_factured_products(self):
        query = """
        MATCH (:Factura)-[:HAS_ITEM]->(:DetalleFactura)-[:REFERS_TO]->(p:Producto)
        RETURN p.codigo_producto AS codigo_producto,
               p.nombre AS nombre,
               p.marca AS marca,
               p.precio AS precio,
               COUNT(*) AS times_factured
        """
        with self.driver.session() as session:
            results = session.run(query)
            return [
                {
                    "codigo_producto": record["codigo_producto"],
                    "nombre": record["nombre"],
                    "marca": record["marca"],
                    "precio": record["precio"],
                    "times_factured": record["times_factured"]
                }
                for record in results
            ]

URI = "neo4j://localhost:7687"
USERNAME = "neo4j"
PASSWORD = "test"

product_query = ProductQuery(URI, USERNAME, PASSWORD)

try:
    factured_products = product_query.get_factured_products()

    print(f"{'Código Producto'.ljust(15)} | {'Nombre'.ljust(20)} | {'Marca'.ljust(15)} | {'Precio'.ljust(10)} | {'Veces Facturada'.ljust(15)}")
    print("-" * 80)
    for product in factured_products:
        print(f"{str(product['codigo_producto']).ljust(15)} | {product['nombre'].ljust(20)} | {product['marca'].ljust(15)} | {str(product['precio']).ljust(10)} | {str(product['times_factured']).ljust(15)}")
finally:
    product_query.close()
