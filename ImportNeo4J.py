import os
from neo4j import GraphDatabase

class Neo4jImporter:
    def __init__(self, uri):
        self.driver = GraphDatabase.driver(uri)

    def close(self):
        self.driver.close()

    def run_query(self, query, parameters=None):
        with self.driver.session() as session:
            session.run(query, parameters)

    def import_csv(self, file_path, query):
        absolute_path = os.path.abspath(file_path)
        if not os.path.exists(absolute_path):
            raise FileNotFoundError(f"File not found: {absolute_path}")
        
        with open(absolute_path, "r", encoding="utf-8") as file:
            csv_data = file.read()
        
        with self.driver.session() as session:
            session.run(query, parameters={"data": csv_data})

# Cypher query to parse CSV data in Neo4j
FACTURA_QUERY = """
LOAD CSV WITH HEADERS FROM 'file:///e01_factura.csv' AS row
CREATE (:Factura {
    nro_factura: toInteger(row.nro_factura),
    fecha: date(row.fecha),
    total_sin_iva: toFloat(row.total_sin_iva),
    iva: toFloat(row.iva),
    total_con_iva: toFloat(row.total_con_iva),
    nro_cliente: toInteger(row.nro_cliente)
});
"""

PRODUCTO_QUERY = """
LOAD CSV WITH HEADERS FROM 'file:///e01_producto.csv' AS row
CREATE (:Producto {
    codigo_producto: toInteger(row.codigo_producto),
    marca: row.marca,
    nombre: row.nombre,
    descripcion: row.descripcion,
    precio: toFloat(row.precio),
    stock: toInteger(row.stock)
});
"""

DETALLE_FACTURA_QUERY = """
LOAD CSV WITH HEADERS FROM 'file:///e01_detalle_factura.csv' AS row
MATCH (f:Factura {nro_factura: toInteger(row.nro_factura)})
MATCH (p:Producto {codigo_producto: toInteger(row.codigo_producto)})
CREATE (df:DetalleFactura {
    nro_item: toInteger(row.nro_item),
    cantidad: toFloat(row.cantidad)
})
MERGE (f)-[:HAS_ITEM]->(df)
MERGE (df)-[:REFERS_TO]->(p);
"""

# Main script
if __name__ == "__main__":
    URI = "neo4j://localhost:7687"
    importer = Neo4jImporter(URI)

    try:
        importer.import_csv("Data/e01_factura.csv", FACTURA_QUERY)

        importer.import_csv("Data/e01_producto.csv", PRODUCTO_QUERY)

        importer.import_csv("Data/e01_detalle_factura.csv", DETALLE_FACTURA_QUERY)
        importer.driver.session().run("CREATE CONSTRAINT FOR (p:Producto) REQUIRE p.codigo_producto IS UNIQUE;")

        print("Data import completed successfully.")
    except Exception as e:
        print(f"Failed to import .csv files into Neo4J @ {URI}: {e}")
    finally:
        importer.close()
