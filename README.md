# Plantilla FastAPI SOLID con MySQL

Proyecto de ejemplo que expone una API REST con FastAPI usando principios SOLID, inyección de dependencias y separación clara entre interfaces y sus implementaciones. Incluye despliegue vía Docker Compose y MySQL.

## Arquitectura y patrones

El código sigue un enfoque de capas inspirado en DDD y principios SOLID:

- **Dominio (`app/domain`)**: modelos inmutables y servicios de negocio. Define interfaces (p. ej. `UserRepository`) para desacoplar reglas de negocio de la infraestructura.
- **Infraestructura (`app/infrastructure`)**: implementaciones concretas de las interfaces, como `SqlAlchemyUserRepository`, y configuración de base de datos.
- **API (`app/api`)**: controladores FastAPI que reciben y validan requests, delegando la lógica en servicios de dominio a través de dependencias.
- **Esquemas (`app/schemas`)**: modelos Pydantic que definen contratos de entrada y salida.
- **Configuración (`app/core/config.py`)**: `Settings` centraliza variables de entorno.

Este diseño permite intercambiar implementaciones (por ejemplo, otro repositorio) sin tocar la lógica de negocio, cumpliendo con inversión de dependencias y responsabilidad única.

### Flujo de dependencias
1. Los routers solicitan servicios mediante dependencias (`app/api/deps.py`).
2. Los servicios dependen de interfaces; las implementaciones se inyectan en tiempo de ejecución.
3. Las operaciones de infraestructura usan SQLAlchemy Async con MySQL.

## Requisitos previos
- Docker y Docker Compose
- Make (opcional pero recomendado)

## Variables de entorno
Copia `.env.example` a `.env` y ajusta si es necesario:

```
APP_NAME=FastAPI SOLID Template
ENVIRONMENT=development
DB_USER=app_user
DB_PASSWORD=app_password
DB_HOST=db
DB_PORT=3306
DB_NAME=app_db
```

## Puesta en marcha

```bash
# Construir contenedores
make build

# Levantar servicios en segundo plano
make up

# Ver logs de la app
make logs

# Detener y limpiar
make down
```

La API quedará disponible en `http://localhost:8000`. La UI interactiva de documentación está en `http://localhost:8000/docs`.

## Endpoints principales

- **Health**: `GET /api/health`
- **Cálculos**: `GET /api/calculate?expression=5+3`
- **Texto**: `POST /api/process-text` con `{"text": "hello world"}`
- **Usuarios (CRUD)**:
  - `GET /api/users`
  - `POST /api/users`
  - `GET /api/users/{id}`
  - `PUT /api/users/{id}`
  - `DELETE /api/users/{id}`
- **Stats (procedimientos almacenados)**:
  - `GET /api/stats/user-count`
  - `GET /api/stats/user-stats/{id}`

## Base de datos y procedimientos almacenados

`docker-compose` monta `sql/init/001_init.sql`, que:
- Crea la tabla `users`.
- Define `get_user_count()` (sin parámetros) y `get_user_stats(user_id_param INT)`.

El servicio `StatsService` ejecuta `CALL` sobre estos SPs para los endpoints de estadísticas.

## Desarrollo local sin Docker (opcional)

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Asegúrate de tener un MySQL accesible con las variables configuradas.

## Notas de diseño

- El módulo `CalculationService` usa `ast` para evaluar expresiones aritméticas simples de forma segura (solo operadores permitidos).
- `TextService` concentra la lógica de transformación y métricas de texto.
- `UserService` aplica reglas de negocio y valida duplicidad vía el repositorio.
- La configuración y creación de sesiones de base de datos están centralizadas en `app/infrastructure/db/session.py`, favoreciendo la reutilización y prueba.

## Pruebas

Incluye objetivo `make test` para ejecutar `pytest` si se añaden pruebas unitarias.
