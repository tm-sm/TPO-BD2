from pymongo import MongoClient
from neo4j import GraphDatabase

class ClientInvoiceQuery:
    def __init__(self, mongo_uri, neo4j_uri, neo4j_user, neo4j_password):
        self.mongo_client = MongoClient(mongo_uri)
        self.neo4j_driver = GraphDatabase.driver(neo4j_uri, auth=(neo4j_user, neo4j_password))

    def close(self):
        self.mongo_client.close()
        self.neo4j_driver.close()

    def get_client_total_spent(self):
        db = self.mongo_client['Negocio']
        clients_collection = db['Clientes']

        clients = list(clients_collection.find({}))

        results = []

        with self.neo4j_driver.session() as session:
            for client in clients:
                nro_cliente = client.get("nro_cliente")
                if nro_cliente:
                    query = """
                    MATCH (f:Factura {nro_cliente: $nro_cliente})
                    RETURN SUM(f.total_con_iva) AS total_gastado
                    """
                    neo4j_result = session.run(query, nro_cliente=nro_cliente)
                    total_gastado = next(neo4j_result, {}).get("total_gastado", 0.0)
                    results.append({
                        "nombre": client.get("nombre"),
                        "apellido": client.get("apellido"),
                        "total_gastado": total_gastado or 0.0
                    })
        return results

MONGO_URI = "mongodb://mongo:27017/"
NEO4J_URI = "bolt://neo4j:7687"
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "test"

query_handler = ClientInvoiceQuery(MONGO_URI, NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD)

try:
    client_expenses = query_handler.get_client_total_spent()

    print(f"{'Nombre'.ljust(15)} | {'Apellido'.ljust(15)} | {'Total Gastado'.ljust(20)}")
    print("-" * 55)
    for entry in client_expenses:
        print(f"{entry['nombre'].ljust(15)} | {entry['apellido'].ljust(15)} | {str(entry['total_gastado']).ljust(20)}")
finally:
    query_handler.close()
