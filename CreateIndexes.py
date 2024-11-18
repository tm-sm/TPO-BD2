from neo4j import GraphDatabase

uri = "bolt://neo4j:7687"
driver = GraphDatabase.driver(uri)

with driver.session() as session:
    
    session.run("""
    CREATE INDEX ProductoNoFacturadoIndex IF NOT EXISTS 
    FOR (p:producto_no_facturado) 
    ON (p.codigo_producto);
    """)

    session.run("""
    CREATE INDEX IF NOT EXISTS 
    FOR (f:Factura)
    ON (f.fecha);   
    """)