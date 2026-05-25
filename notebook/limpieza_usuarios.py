import pandas as pd

def limpiar_datos_usuarios(data_frame_sucio):

    data_frame_limpio = data_frame_sucio.copy()
    # print(data_frame_limpio)

    # 1. Limpiar columnas tipo string
    columnas_texto = [
        "fullName",
        "email",
        "displayName",
        "sex",
        "metadata"
    ]

    for columna in columnas_texto:
        data_frame_limpio[columna] = (
            data_frame_limpio[columna]
            .astype("string")
            .str.strip()
        )

    # 1.1 Definir valores válidos
    valores_validos_sex = ["M", "F"]

    data_frame_limpio["sex"] = data_frame_limpio["sex"].where(
        data_frame_limpio["sex"].isin(valores_validos_sex),
        pd.NA
    )
    # print(data_frame_limpio)
    # 2. Limpiar columnas numéricas
    data_frame_limpio["id"] = pd.to_numeric(
        data_frame_limpio["id"],
        errors="coerce"
    )

    data_frame_limpio["role"] = pd.to_numeric(
        data_frame_limpio["role"],
        errors="coerce"
    )

    data_frame_limpio["heightCm"] = pd.to_numeric(
        data_frame_limpio["heightCm"],
        errors="coerce"
    )

    data_frame_limpio["weightKg"] = pd.to_numeric(
        data_frame_limpio["weightKg"],
        errors="coerce"
    )

    # 2.1 Validar números correctos
    data_frame_limpio = data_frame_limpio[
        data_frame_limpio["id"] > 0
    ]

    data_frame_limpio = data_frame_limpio[
        data_frame_limpio["role"] > 0
    ]

    data_frame_limpio = data_frame_limpio[
        data_frame_limpio["heightCm"] > 0
    ]

    data_frame_limpio = data_frame_limpio[
        data_frame_limpio["weightKg"] > 0
    ]

    # 3. Organizar columnas fecha
    columnas_fecha = [
        "dateOfBirth",
        "createdAt",
        "updatedAt"
    ]

    for columna in columnas_fecha:
        data_frame_limpio[columna] = pd.to_datetime(
            data_frame_limpio[columna],
            errors="coerce"
        )

    # 3.1 Reemplazar fechas vacías
    fecha_default = pd.to_datetime("2023-01-01")

    for columna in columnas_fecha:
        data_frame_limpio[columna] = (
            data_frame_limpio[columna]
            .fillna(fecha_default)
        )

    # 4. Eliminar registros con datos obligatorios vacíos
    columnas_obligatorias = [
        "id",
        "email",
        "weightKg",
        "heightCm",
        "fullName",
        "sex"
    ]

    data_frame_limpio = data_frame_limpio.dropna(
        subset=columnas_obligatorias
    )

    # 5. Eliminar registros duplicados
    data_frame_limpio = data_frame_limpio.drop_duplicates()

    return data_frame_limpio