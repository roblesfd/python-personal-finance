# 🧾 Personal Finance CLI

Un sistema de **gestión de finanzas personales** desarrollado en **Python**, diseñado con una arquitectura flexible y modular que permite cambiar fácilmente entre distintos métodos de almacenamiento de datos (archivos JSON o base de datos SQLite) sin modificar la lógica de negocio.

---

## 🚀 Características principales

- 📂 **Gestión de categorías** (crear, listar, eliminar)
- 💸 **Gestión de transacciones** (registro, visualización, eliminación)
- 💰 **Cálculo automático de balances**
- 🔄 **Arquitectura desacoplada** mediante clases abstractas (repositorios)
- 🧱 **Soporte intercambiable de almacenamiento**:
  - `JsonCategoryRepository` / `JsonTransactionRepository`
  - `SqliteCategoryRepository` / `SqliteTransactionRepository`
- 🧪 **Pruebas unitarias** con `pytest`
- 🕒 **Decoradores de logging y medición de tiempo**
- 🧾 **Interfaz CLI** simple y extensible


---

## ⚙️ Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/roblesfd/python-personal-finance.git
   cd personal-finance
    ```

2. Crea y activa un entorno virtual:

```bash
    python -m venv venv
    source venv/bin/activate   # En Linux / macOS
    venv\Scripts\activate      # En Windows
```

3. Instala dependencias:

```bash
    pip install -r requirements.txt
```

## 🧠 Uso del CLI

Ejecuta el programa principal desde la terminal:

```bash
    python main.py
```


## Ejemplos de comandos


### Registrar un movimiento

```bash
    python main.py add gasto 2900 --categoria alimentos --descripcion "Comida del mes"
    python main.py add ingreso 10500 -c salario -d "Salario mensual"
```

### Devolver una lista de movimientos
```bash
    python main.py list 
```

### Mostrar movimientos en una tabla
```bash
    python main.py display --tipo ingreso --categoria salario --desde 2025-06-10 --hasta 2025-10-09

    python main.py display -t ingreso -c salario -start 2025-06-10 -end 2025-10-09
```

### Exportar movimientos en un archivo pdf o csv
```bash
    python main.py export pdf
    python main.py export csv
```

### Eliminar un movimiento por ID
```bash
    python main.py delete 10 
```

### Listar categorías
```bash
    python main.py listcat
```

### Mostrar categorías en una tabla
```bash
    python main.py displaycat
```

### Eliminar una categoría por nombre
```bash
    python main.py deletecat salario
```

### Mostrar la documentación del proyecto
```bash
    python main.py opendocs
```

## 🧪 Pruebas

Ejecuta los tests con Pytest o Pytest Watch:

Pytest watch:
```bash
    ptw -vv
```

Pytest:

```bash
    python -m pytest -vv
```