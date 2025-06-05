
# FaceID

*Impulsando la seguridad a través de tecnología de reconocimiento facial sin interrupciones.*

![Lenguaje principal del repositorio](https://img.shields.io/github/languages/top/S-mazo/FaceID?style=flat&color=0080ff)
![Cantidad de lenguajes](https://img.shields.io/github/languages/count/S-mazo/FaceID?style=flat&color=0080ff)

**Desarrollado con:**

![Python](https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white)

---

## Tabla de Contenidos

- [Descripción general](#descripción-general)
- [Primeros pasos](#primeros-pasos)
  - [Requisitos previos](#requisitos-previos)
  - [Instalación](#instalación)
  - [Uso](#uso)
  - [Pruebas](#pruebas)

---

## Descripción general

**FaceID** es una herramienta de reconocimiento biométrico diseñada para mejorar la seguridad y facilitar la gestión de asistencia en entornos controlados.

### ¿Por qué FaceID?

Este proyecto busca ofrecer una solución simple y efectiva para el reconocimiento facial y el registro automático de asistencia. Sus características principales incluyen:

- **📊 Registro de asistencia:** Actualiza automáticamente los registros de asistencia en un archivo CSV, facilitando las tareas administrativas.
- **🖥️ Interfaz amigable:** Simplifica la interacción, haciéndola accesible incluso para personal no técnico.
- **🔒 Comparación biométrica:** Usa librerías avanzadas para garantizar una identificación precisa.
- **💾 Integración con base de datos local:** Aumenta la seguridad al mantener los datos sensibles en un entorno controlado.

---

## Primeros pasos

### Requisitos previos

Este proyecto requiere:

- **Lenguaje de programación:** Python 3.12.x 
- **[Cmake](https://cmake.org/download/)**
- **[Visual Studio](https://visualstudio.com/download)**
> **IMPORTANTE:** para el visual studio descargar las herramientas de *Desarrollo para el escritorio con C++*


Librerías adicionales:
- **setuptools**
```sh
pip install --upgrade setuptools
```
- **cv2**
```sh
pip install opencv-python
```
- **face_recognition**
```sh
pip install face_recognition
```
- **numpy** (se instala con el face_recognition)

- **dlib** (también se instala con el face_recognition)

### Instalación

Construye FaceID desde el código fuente:

1. **Clona el repositorio:**

```sh
git clone https://github.com/S-mazo/FaceID
```

2. **Entra al directorio del proyecto:**

```sh
cd FaceID
```

3. **Crea la carpeta donde irá a la base de datos de rostros:**
```sh
mkdir database
```


---

### Uso

Ejecuta el proyecto con:

```sh
python main.py
```

---

[Volver al inicio](#faceid)
