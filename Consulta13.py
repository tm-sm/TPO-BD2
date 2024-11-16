from pymongo import MongoClient
import pandas as pd
import argparse

client = MongoClient("mongodb://localhost:27017/")  
db = client['Negocio']
collection = db['Clientes']

parser = argparse.ArgumentParser(description="Add a client to Neo4j.")
operation = parser.add_mutually_exclusive_group(required=True)
operation.add_argument("--a","--agregar",action="store_true", help="Agrega un cliente")
operation.add_argument("--m","--modificar",action="store_true", help="Modifica un cliente")
operation.add_argument("--e","--eliminar",action="store_true", help="Elimina un cliente")


parser.add_argument("--nro_cliente", type=int, required=True, help="Numero de Cliente")
parser.add_argument("--nombre", type=str, help="Nombre Cliente")
parser.add_argument("--apellido", type=str, help="Apellido Cliente")
parser.add_argument("--direccion", type=str, help="Direccion del Cliente")
parser.add_argument("--activo", type=int,  help="Activo de Cliente")

args=parser.parse_args()


if args.a:
        collection.insert_one({"nro_cliente":args.nro_cliente,"nombre":args.nombre,
                            "apellido":args.apellido,"direccion":args.direccion,"activo":args.activo})
elif args.m:
        collection.update_one({"nro_cliente":args.nro_cliente},{"$set":{"direccion":args.direccion}})
elif args.e:
        collection.delete_one({"nro_cliente":args.nro_cliente})
