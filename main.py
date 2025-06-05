import face_recognition as fr
import cv2
import os
from pathlib import Path
import numpy as np
from datetime import datetime
from time import sleep 
dir_ruta = Path(os.getcwd())


print("Ajustando la cámara, por favor espera")

for i in range(3, 0, -1):
    print(f"Tomando foto en {i}")
    sleep(1)

# Leer imagen de la cámara
captura = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# Descartar los dos primeros frames de la cámara (permitir el autoajuste de la cámara)
for _ in range(10):
    captura.read()
exito, imagen = captura.read()
captura.release()
print("Foto capturada correctamente")

# Crear base de datos
ruta = Path(dir_ruta, "database")
if not os.path.exists(ruta):
    os.makedirs(ruta, exist_ok=True)
mis_imagenes = []
nombres_empleados = []
lista_empleados = os.listdir(ruta)

print(f"{"="*50}\n")

for nombre in lista_empleados:
    print(f"Cargando {nombre}")
    imagen_actual = fr.load_image_file(Path(ruta, nombre))
    mis_imagenes.append(imagen_actual)
    nombres_empleados.append(os.path.splitext(nombre)[0])
print(f"\n{"="*50}")
# print(nombres_empleados)

# Codificar nombres empleados
def codificar(imagenes: list) -> list:
    # Crear lista nueva
    lista_codificada = []

    # Pasar todas las imágenes a rgb
    for imagen in imagenes:
        imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
        
        # Codificar
        codificacion = fr.face_encodings(imagen)[0] if len(fr.face_encodings(imagen)) > 0 else None

        # Agregar a la lista
        if codificacion is not None:
            lista_codificada.append(codificacion)
    # Devolver lista
    return lista_codificada

""" def registrar_ingresos(persona):
    try:
        with open(Path(dir_ruta, "registro.csv"), "r+", encoding="utf-8") as f:
            lista_datos = f.readlines()
            nombres_registro = {}
            for linea in lista_datos:
                ingreso = linea.strip().split(",")
                nombres_registro[ingreso[0]] = ingreso[1]

            # Si la persona no está en el registro, agregarla
            if persona not in nombres_registro:
                ahora = datetime.now().strftime("%H:%M:%S")
                f.writelines(f"\n{persona}, {ahora}")

    except FileNotFoundError:
        with open(Path(dir_ruta, "registro.csv"), "w", encoding="utf-8") as f:
            f.writelines("Persona, Hora\n")
            ahora = datetime.now().strftime("%H:%M:%S")
            f.writelines(f"{persona}, {ahora}") """

def registrar_ingresos(persona):
    try:
        # Leer el archivo y almacenar las líneas
        with open(Path(dir_ruta, "registro.csv"), "r+", encoding="utf-8") as f:
            lista_datos = f.readlines()
            nombres_registro = {}
            
            # Crear un diccionario con los nombres y sus horas de ingreso
            for linea in lista_datos:
                ingreso = linea.strip().split(",")
                nombres_registro[ingreso[0]] = ingreso[1]  # Almacena el nombre y la hora
            
            # Actualizar o agregar la persona
            ahora = datetime.now().strftime("%H:%M:%S")
            nombres_registro[persona] = ahora  # Actualiza la hora de ingreso
            # Escribir de nuevo en el archivo
            f.seek(0)  # Regresar al inicio del archivo
            f.truncate()  # Limpiar el archivo
            for nombre, hora in nombres_registro.items():
                f.write(f"{nombre}, {hora}\n")  # Escribir cada entrada
                
    except FileNotFoundError:
        with open(Path(dir_ruta, "registro.csv"), "w", encoding="utf-8") as f:
            f.writelines("Persona, Hora\n")
            ahora = datetime.now().strftime("%H:%M:%S")
            f.writelines(f"{persona}, {ahora}")
            
    except Exception as e:
        print(f"Error al registrar ingresos: {e}")
            
lista_empleados_codificada = codificar(mis_imagenes)

if not exito:
    print("No se pudo tomar la captura.")
else:
    # Reconocer caras en la captura
    cara_captura = fr.face_locations(imagen)
    # Codificar todas las caras capturadas
    codificacion_cara = fr.face_encodings(imagen, cara_captura)

    # Iterar sobre todas las caras detectadas
    for caracodif, caraubic in zip(codificacion_cara, cara_captura):
        # Buscar coincidencias en la base de datos
        coincidencias = fr.compare_faces(lista_empleados_codificada, caracodif)
        distancias = fr.face_distance(lista_empleados_codificada, caracodif)

        print(distancias)

        # Mostrar coincidencias si las hay
        try:
            indice_coincidencia = np.argmin(distancias)
            if distancias[indice_coincidencia] > 0.6:
                n = "Desconocido"
                print("No coincide con nadie en la base de datos de rostro")
            else:
                n = nombres_empleados[indice_coincidencia]
                print(f"Hola, bienvenido {n}")
                # Mostrar la imagen de la persona reconocida (comentar línea de abajo para evitar mostrar la imagen)
                # cv2.imshow(f"Foto de {n}", cv2.cvtColor(mis_imagenes[indice_coincidencia], cv2.COLOR_BGR2RGB))
                registrar_ingresos(n)
        except Exception as e:
            n = "Desconocido"
            print(f"Error al procesar las imágenes: {e}")
            print(f"Quizás la ruta ({ruta}) está vacía. Por favor, verifica que en la ruta hayan imágenes (con el nombre de la persona como nombre de archivo) y que no haya imágenes duplicadas.")
            
        # Dibujar rectángulo alrededor de la cara detectada
        y1, x2, y2, x1 = caraubic
        imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
        cv2.rectangle(imagen, (x1, y1), (x2, y2), (183, 19, 0), 2)
        
        # Solo el primer nombre
        # texto = n.split(" ")[0]
        texto = n

        # Calcula el tamaño del texto
        (font_width, font_height), _ = cv2.getTextSize(texto, cv2.FONT_HERSHEY_COMPLEX, 1, 2)
        # Ajusta el tamaño del rectángulo para que se ajuste al texto
        rect_width = font_width + 80  # Se añade un margen extra para que el texto no quede pegado al borde
        rect_height = font_height + 20  # Margen vertical para el texto
        cv2.rectangle(imagen, (x1-40, y2), (x1-40 + rect_width, y2 + rect_height), (183, 19, 0), cv2.FILLED)
        # Calcula la posición del texto para que se ajuste dentro del rectángulo
        text_x = x1 - 16  # Puedes ajustar este valor si es necesario
        text_y = y2 + font_height + 8  # Centra verticalmente el texto
        # Dibuja el texto sobre el rectángulo
        cv2.putText(imagen, texto, (text_x, text_y), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255))
        
        
        imagen = cv2.cvtColor(imagen, cv2.COLOR_RGB2BGR)
        

    # Mostrar la imagen final con las caras reconocidas
    cv2.imshow(f"Foto capturada", imagen)
    cv2.waitKey(0)
