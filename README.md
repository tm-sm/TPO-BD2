# TPO-BD2

## Descripción del Proyecto
Este proyecto es un sistema de **Facturación** diseñado para gestionar el control de productos comprados por los clientes. Las principales funcionalidades incluyen:

- **Chequeo de Stock:** Verifica la disponibilidad de productos antes de realizar la venta.
- **Actualización de Inventario:** Decrementa la cantidad de productos vendidos del stock.
- **Cálculo de Factura:** Calcula el monto total considerando el IVA y aplica descuentos basados en el volumen de compra.

El sistema permite optimizar el proceso de facturación y asegurar la consistencia del inventario.
---

## **Requisitos de Instalación**
Para ejecutar este proyecto, asegúrate de tener instalados los siguientes componentes:

- **Python 3**: Lenguaje de programación utilizado.
- **Librerías de Python**:
  - `neo4j`
  - `pymongo` (librería para MongoDB)
  - `pandas`
- **Bases de datos**:
  - **Neo4j**
  - **MongoDB**
- **Docker**: Para manejar los entornos de las bases de datos mediante contenedores.

---

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
   *(Asegúrate de tener un archivo `requirements.txt` con las librerías necesarias, como `neo4j`, `pymongo` y `pandas`.)*

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

---

## **Resolución de Problemas**
- Asegúrate de que los contenedores de **MongoDB** y **Neo4j** estén en ejecución:
  - Usa `docker ps` para verificar los contenedores activos.
  - Revisa los logs de `docker-compose` para confirmar que no haya errores en la configuración.
- Si un script falla, verifica que los datos hayan sido importados correctamente en las bases de datos.

---
