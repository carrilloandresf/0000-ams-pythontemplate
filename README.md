# API REST con FastAPI y MySQL

Proyecto de ejemplo que implementa una API REST con FastAPI y MySQL, pensada para ser levantada rápidamente en contenedores Docker. Incluye endpoints de cálculo, procesamiento de texto, CRUD de usuarios, procedimientos almacenados y health check.

## Requisitos
- Docker y Docker Compose
- Make

## Configuración
1. Copia el archivo de variables de entorno y ajusta valores según tu entorno:
   ```bash
   cp .env.example .env
   ```
2. Dentro de `.env` ajusta `DATABASE_URL` si necesitas otro host, usuario o nombre de base de datos.

## Cómo levantar el proyecto
Con Docker y Make:
```bash
make up
```
Esto construye las imágenes y levanta dos contenedores:
- `api`: aplicación FastAPI expuesta en el puerto 8000.
- `db`: MySQL 8 con inicialización automática (tabla `users` y procedimientos `user_count` y `user_stats`).

Para apagar los servicios:
```bash
make down
```

### Ejecución local sin Docker
Instala dependencias y ejecuta Uvicorn:
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```
Asegúrate de tener MySQL corriendo y que `DATABASE_URL` apunte a tu instancia.

## Endpoints principales
Todos los endpoints están bajo el prefijo `/api`.

### Cálculos
- `GET /api/calculate?expression=5+3`

### Texto
- `POST /api/process-text`
  ```json
  {"text": "hello world"}
  ```

### CRUD de Usuarios
- `GET /api/users` – Listar
- `POST /api/users` – Crear
- `GET /api/users/{id}` – Obtener
- `PUT /api/users/{id}` – Actualizar
- `DELETE /api/users/{id}` – Eliminar

### Estadísticas (Procedimientos almacenados)
- `GET /api/stats/user-count`
- `GET /api/stats/user-stats/{id}`

### Health Check
- `GET /api/health`

## Estructura del proyecto
```
app/
├── database.py        # Conexión a MySQL y sesión de SQLAlchemy
├── main.py            # Instancia de FastAPI y registro de routers
├── models.py          # Modelos ORM
├── routers/           # Routers organizados por dominio
│   ├── stats.py
│   ├── users.py
│   └── utility.py
├── schemas.py         # Esquemas Pydantic
└── utils.py           # Utilidades para cálculos y texto
mysql/
└── initdb/init_db.sql # Script de inicialización de la base
```

## Notas adicionales
- El script `mysql/initdb/init_db.sql` crea la base `app_db`, la tabla `users` y define los procedimientos `user_count` y `user_stats`.
- El proyecto usa `SQLAlchemy` con el driver `pymysql` (cadena de conexión `mysql+pymysql://...`).
- La documentación interactiva de la API estará disponible en `http://localhost:8000/docs` cuando el servicio esté corriendo.
