## **Technical Test**

Este repositorio contiene dos proyectos distintos que se ejecutan en contenedores Docker. El primer proyecto es una cola de tareas con Celery que consume datos de una API. El segundo es una API desarrollada con FastAPI que implementa endpoints CRUD y postea sobre una base de datos PostgreSQL.


## **Projectos**

1. ## **Celery Task Queue**

Este proyecto consiste en una cola de tareas con Celery que consume datos de una API. Utiliza Redis como backend y broker para Celery.

## Estructura del Proyecto

    celery_tasks/app: Contiene la configuración y tareas de Celery.
    docker-compose.yml: Configuración de Docker Compose para iniciar los contenedores necesarios.

## Instalación y ejecución

1. **Clonar el repositorio**

    git clone https://github.com/lotjulieta/technical-test.git
    cd technical-test/celery_tasks

2. **Levanta los contenedores con Docker Compose:**

    docker compose up --build

3. **Para ejecutar la tarea ingresamos al contenedor de Docker**

    docker exec -it celery_tasks-celery_worker-1 bash

4. **UNa vez dentro corremos el script de prueba**

    python main.py

5. **Las tareas de Celery comenzarán a ejecutarse y consumirán datos de la API especificada.**.


1. ## **FastAPI CRUD API**

Este proyecto es una API desarrollada con FastAPI que implementa endpoints CRUD para interactuar con una base de datos PostgreSQL. Utiliza SQLAlchemy para la gestión de la base de datos y Alembic para las migraciones.

## Estructura del Proyecto

    fastapi/app: Contiene la aplicación FastAPI, modelos, y rutas.
    docker-compose.yml: Configuración de Docker Compose para iniciar los contenedores necesarios.

## Instalación y ejecución

1. **Clonar el repositorio**

    git clone https://github.com/lotjulieta/technical-test.git
    cd technical-test/fastapi

2. **Levanta los contenedores con Docker Compose:**

    docker compose up --build

3. **Ingresa al contenedor de la aplicación FastAPI:**

    docker compose exec fastapi-web-1 bash

4. **Ejecuta las migraciones de la base de datos:**

    alembic upgrade head

5. **La API estará disponible en http://localhost:8000**

6. **Endpoints Disponibles**

    GET /cars: Obtiene todos los autos.
    GET /cars?brand={brand}&subsidiary_name={subsidiary_name}: Filtra autos por marca y nombre de subsidiaria.
    POST /cars: Agrega un nuevo auto.
