import sqlite3 as db

# Conectar a la base de datos
conexion = db.connect("usuarios.db")
cursor = conexion.cursor()

# Crear tabla USERS
cursor.execute("""
CREATE TABLE USERS (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    display_name TEXT,
    role_id INTEGER NOT NULL,
    date_of_birth TEXT NOT NULL,
    sex TEXT NOT NULL,
    height_cm INTEGER,
    weight_kg REAL,
    metadata TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP,
    deleted_at TIMESTAMP
)
""")

# Insertar un usuario
cursor.execute("""
INSERT INTO USERS (
    full_name, email, password_hash, display_name, role_id,
    date_of_birth, sex, height_cm, weight_kg
) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
""", (
    "Juan Perez",
    "juan@example.com",
    "123456hash",
    "Juan",
    1,
    "2000-05-10",
    "Masculino",
    175,
    70.5
))

# Guardar cambios
conexion.commit()

# Consultar datos
cursor.execute("SELECT * FROM USERS")
usuarios = cursor.fetchall()

for usuario in usuarios:
    print(usuario)

# Cerrar conexión
conexion.close()