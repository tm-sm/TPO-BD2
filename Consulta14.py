from neo4j import GraphDatabase
import argparse

driver = GraphDatabase.driver(uri="bolt://neo4j:7687")   
session = driver.session()

parser = argparse.ArgumentParser(description="Add a client to Neo4j.")
operation = parser.add_mutually_exclusive_group(required=True)
operation.add_argument("-a","-agregar",action="store_true", help="Agrega un producto")
operation.add_argument("-m","-modificar",action="store_true", help="Modifica un producto")

parser.add_argument("-desc",type=str,help="Descripcion del producto")
parser.add_argument("-stock",type=int,help="Stock del producto")
parser.add_argument("-precio",type=float,help="Precio del producto")
parser.add_argument("-marca",type=str,help="Marca del producto")
parser.add_argument("-nombre",type=str,help="Nombre del producto")
parser.add_argument("-codigo",type=int,required=True,help="Codigo del producto")

try:
    args=parser.parse_args()

    if args.a:
        session.run("""CREATE (p:Producto {marca:$marca, codigo_producto:$codigo_producto,
        marca:$marca, nombre:$nombre, descripcion:$descripcion,precio:$precio,stock:$stock })"""
        ,marca=args.marca, precio=args.precio,nombre=args.nombre,stock=args.stock,
        codigo_producto=args.codigo, descripcion=args.desc)
    elif args.m:
        neo_query_result=session.run("MATCH (p:Producto {codigo_producto:$codigo}) return (p)",codigo=args.codigo)
        if neo_query_result.peek() is None:
            print("No se encuentra el producto con codigo especificado")
            exit()
        neo_query_result=neo_query_result.single()
        stock=args.stock if args.stock is not None else neo_query_result['stock']
        precio=args.precio if args.precio is not None else neo_query_result['precio']
        desc=args.desc if args.desc is not None else neo_query_result['descripcion']
        session.run("""MATCH (p:Producto {codigo_producto:$codigo_producto})
                    SET p.stock=$stock, p.precio=$precio, p.descripcion=$desc
                    return p""",codigo_producto=args.codigo,stock=stock,precio=precio,desc=desc)
finally:
    session.close()
