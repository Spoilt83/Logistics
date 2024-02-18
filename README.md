# Logistics
Aplicación desarrollada con Django para logística de paquetería


## Requisitos

- Python (3.12.1)
- Django (5.0.2)

## Configuración

1. Clona este repositorio en tu máquina local:

    ```
    git clone https://github.com/Spoilt83/Logistics.git
    ```

2. Navega al directorio de tu proyecto:

    ```
    cd tu_aplicacion_django
    ```

3. Crea y activa un entorno virtual (opcional pero recomendado):

    ```
    python -m venv env
    source env/bin/activate   # Linux/Mac
    env\Scripts\activate      # Windows
    ```

4. Instala las dependencias del proyecto:

    ```
    pip install -r requirements.txt
    ```

5. Realiza las migraciones de la base de datos:

    ```
    python manage.py migrate
    ```
6. Crea un usario para gestionar los datos desde el admin de la aplicación.

    ```
    python manage.py createsuperuser
 
    ```
    Este te solicitara un username, email y password para crear el usuario.

7. Ejecuta el servidor de desarrollo:

    ```
    python manage.py runserver
    ```

8. Abre tu navegador web y ve a http://localhost:8000 para ver tu aplicación en funcionamiento.

9. Abre tu navegador web y ve a http://localhost:8000/admin.   
     - Se solicitara username y password configurado previamente.
     - Registra datos para las tablas Clients y Transportists.
     - Para agregar un envío en la tabla Packages, puedes hacerlo desde admin o desde página de creación de la aplicación.


## Estructura del Proyecto

- El proyecto se encuntra conformado por 3 modelos para representar los datos de clientes, transportistas y paquetes. 

- Támbien se crearon templates para representar los datos de los modelos al usuario.

- Mediante el manejo de views se implementa la logica para hacer uso de los datos y poder manipularlos y representarlos representarlos.

- En las vistas se encuentran implementadas funciones para: 

        - listar los paquetes de un usuario 
        - listar los paquetes asignados a un         transportista
        - crear un envio con los datos de un paquete y asignarle un cliente y un transportista
        - actualizar un envio
        - borrar un envio

- Las distintas rutas implementadas fueron configurdas mediante el archivo urls.py



