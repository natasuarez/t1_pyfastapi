# T1 - Proyecto Python con FastAPI

## 📌 Descripción

Este proyecto consiste en el desarrollo de una API utilizando **Python y FastAPI**, como parte del proceso de aprendizaje de desarrollo de software.

El proyecto permite trabajar con la estructura de una API, la organización del código, la gestión de dependencias y la ejecución de un servidor local.

## 🛠️ Tecnologías utilizadas

- **Python:** lenguaje de programación.
- **FastAPI:** framework para el desarrollo de APIs.
- **Uvicorn:** servidor para ejecutar la aplicación.
- **Git y GitHub:** control de versiones y almacenamiento del proyecto.

## 📂 Estructura del proyecto

```text
t1_pyfastapi/
├── src/
│   └── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

*Nota: la estructura puede variar según la organización actual del proyecto.*

## ⚙️ Instalación y configuración

### 1. Clonar el repositorio

```bash
git clone https://github.com/natasuarez/t1_pyfastapi.git
```

### 2. Ingresar a la carpeta

```bash
cd t1_pyfastapi
```

### 3. Crear el entorno virtual

```bash
python -m venv venv
```

### 4. Activar el entorno virtual

En Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Instalar las dependencias

```bash
pip install -r requirements.txt
```

## ▶️ Ejecución del proyecto

Con el entorno virtual activado, ejecutar:

```bash
uvicorn src.main:app --reload
```

Si el archivo principal se encuentra en otra ubicación o utiliza una instancia con otro nombre, será necesario ajustar el comando.

Una vez iniciado el servidor, acceder a:

- **Aplicación local:** http://127.0.0.1:8000
- **Documentación interactiva:** http://127.0.0.1:8000/docs
- **Documentación alternativa:** http://127.0.0.1:8000/redoc

## 🎯 Objetivos de aprendizaje

- Comprender el funcionamiento de FastAPI.
- Crear y organizar la estructura de un proyecto en Python.
- Gestionar las dependencias mediante `requirements.txt`.
- Utilizar entornos virtuales.
- Ejecutar y probar una API localmente.
- Aplicar Git y GitHub para el control de versiones.

## 👩‍💻 Autora

**Natalia Suárez**

Proyecto académico de desarrollo de software.

## 🔗 Enlaces

- **Repositorio:** https://github.com/natasuarez/t1_pyfastapi
- **Proyecto publicado:** https://natasuarez.github.io/t1_pyfastapi/

---

Desarrollado como parte del proceso de formación en desarrollo de software.
