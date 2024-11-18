# TPO-BD2

## Descripción del Proyecto
Este proyecto, desarrollado como parte de un Trabajo Práctico, tiene como objetivo la implementación de un sistema de facturación para gestionar el control de productos comprados por los clientes. El sistema debe cumplir con las siguientes funcionalidades esenciales:

Gestión del stock: Verificar la disponibilidad de los productos antes de procesar la venta.
Actualización de inventario: Reducir la cantidad en stock de los productos vendidos.
Cálculo de facturación: Determinar el monto total de la factura, incluyendo el IVA y los descuentos aplicables según el volumen de productos adquiridos.

El desarrollo integra el uso de bases de datos NoSQL, MongoDB y Neo4j, para almacenar y consultar los datos necesarios de manera eficiente. Las consultas y operaciones se implementaron utilizando Python y sus bibliotecas especializadas, lo que permite centralizar el manejo de datos y garantizar un funcionamiento confiable del sistema.


## **Instrucciones de Configuración**
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

## **Importación de Datos**
Antes de ejecutar las consultas, importa los datos a las bases de datos:

1. Ejecuta el script de importación para **MongoDB**:
   ```bash
   python3 ./importMongoDB.py
   ```

2. Ejecuta el script de importación para **Neo4j**:
   ```bash
   python3 ./importNeo4j.py
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

