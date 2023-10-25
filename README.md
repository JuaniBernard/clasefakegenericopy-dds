# Rest Fake - Python

## Deploy en Render:
1. Forkear repositorio https://github.com/JuaniBernard/clasefakegenericopy-dds para tener su propia versión.
2. Crear una cuenta en render.com si no se posee una.
3. Seleccionar el botón **New +** y a continuación seleccionar **Web Service**.
4. Hacer click en **Build and deploy from a Git repository** (deberá conectar su cuenta si no lo ha hecho antes).
5. Buscar el repositorio forkeado y tocar **Connect**.
6. Elegir una región, la branch **main** y **Docker** en la selección de runtime.
7. Hacer click en **Create Web Service** y esperar a que se levante el servicio.

## Prueba de Consultas:
En la raíz del proyecto se encuentra el archivo **restfakepy(queries).postman_collection.json**, el mismo contiene
distintos métodos (POST, GET, PUT, etc.) que pueden usarse para probar el funcionamiento de la REST API.