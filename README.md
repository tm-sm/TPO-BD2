# TPO-BD2

## Descripción del Proyecto
Este proyecto tiene como objetivo la implementación de un sistema de facturación para gestionar el control de productos comprados por los clientes a través de bases de datos NoSQL. 

## **Instruciones de uso** ##

### **Codespaces** ###
1. Ingresar a [Codespaces](https://codespaces.new/tm-sm/TPO-BD2)
2. Esperar a que se terminen de instalar las bases de datos y requisitos


### **Local** ###
1. Clona el repositorio del proyecto:
   ```bash
   git clone https://github.com/tm-sm/TPO-BD2.git
   cd TPO-BD2
   ```

2. Navega a la carpeta `.devcontainer`:
   ```bash
   cd .devcontainer
   ```

3. Construye y levanta los contenedores de Docker:
   ```bash
   docker-compose up --build
   ```
   - Asegúrate de que los contenedores de **MongoDB** y **Neo4j** estén en ejecución.

4. Instala las librerías necesarias para Python:
   ```bash
   pip install -r requirements.txt
   ```

---

## **Antes de ejecutar las consultas**
Es necesario importar los .csv necesarios, al igual que preparar índices:

1. Ejecutar el script de importación para **MongoDB**:
   ```bash
   python3 ./importMongoDB.py
   ```

2. Ejecutar el script de importación para **Neo4j**:
   ```bash
   python3 ./importNeo4j.py
   ```
   
3. Ejecutar el script de índices **Neo4j**:
   ```bash
   python3 ./CreateIndexes.py
   ```

---

## **Ejecución de Consultas**
Para ejecutar cualquier script de consulta:

1. Ejecuta el archivo de consulta deseado en la terminal:
   ```bash
   python3 ./ConsultaX.py
   ```
   Reemplaza `ConsultaX.py` con el nombre del script de consulta que deseas ejecutar.

   Para las consultas 13 y 14 que contienen operaciones de escrituras, se requieren parametros de entrada. Para ambos se necesita especificar una de las siguientes:
   
- -a, -agregar: Indica que se debe agregar los parametros indicados de la base de datos
- -m, -modificar: Indica que se debe modificar los parametros indicados de la base de datos
- -e, -eliminar: Indica que se debe eliminar los parametros indicados de la base de datos (no disponible para los productos))
   
Luego, cada consulta pueden recibir parametros especificos a sus dominios.

###  Consulta13
- -nro_cliente: Numero del cliente. Requerido para la ejecucion.
- -nombre: Nombre del cliente.
- -apellido: Apellido del cliente.
- -direccion: Direccion del cliente.
- -activo: Indica el campo activo del cliente.
- -telefono: Telefono del cliente.
- -tipo: Tipo del telefono del cliente.
- -codigo_area: Codigo de area del telefono del cliente  

Por ejemplo, se puede agregar un cliente de la siguiente forma:
``` bash
python3 Consulta13.py -a -nro_cliente 116 -nombre NOMBRECLIENTE -apellido APELLIDOCLIENTE -direccion DIRECCIONCLIENTE -activo 1 -telefono 11547325 -tipo M -codigo_area 11
```
Para la modificacion, el script solo toma los parametros de direccion, telefono, activo, tipo y codigo de area.

### Consulta 14
- -desc: Descripcion del producto
- -stock: Stock del producto
- -precio: Precio del producto
- -marca: Marca del producto
- -nombre: Nombre del producto
- -codigo: Codigo del producto 

Siguiendo el ejemplo anterior, se puede agregar un producto de la siguiente forma:
```bash 
python3 Consulta14.py -a -codigo 104 -marca MARCAPRODUCTO -nombre NOMBREPRODUCTO -precio 1400.6 -desc DESCRIPCIONPRODUCTO -stock 4
```
Para la modificacion, el script solo toma los parametros de stock, precio y descripcion.

