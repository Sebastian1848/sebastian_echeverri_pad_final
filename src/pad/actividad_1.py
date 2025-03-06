import json
import requests
import os

class Ingestiones: 
    def __init__(self):
        self.ruta_static = "src/pad/static/Json/"  # Ruta donde se guardarán los archivos JSON

        # Crear la carpeta si no existe
        if not os.path.exists(self.ruta_static):
            os.makedirs(self.ruta_static)

    def leer_api(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()  # Verifica si hay errores en la solicitud (404, 500, etc.)
            return response.json()  # Retorna el JSON si la solicitud fue exitosa
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}  # Retorna un mensaje de error en formato JSON

    def escribir_json(self, datos, nombre_archivo):
        ruta_completa = f"{self.ruta_static}{nombre_archivo}.json"
        try:
            with open(ruta_completa, "w", encoding="utf-8") as archivo:
                json.dump(datos, archivo, indent=4, ensure_ascii=False)
            print(f"✅ Archivo JSON guardado en: {ruta_completa}")
        except Exception as e:
            print(f"❌ Error al escribir el archivo JSON: {e}")

    def leer_json(self, nombre_archivo):
        ruta_completa = f"{self.ruta_static}{nombre_archivo}.json"
        try:
            with open(ruta_completa, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
            print(f"✅ Datos leídos correctamente desde: {ruta_completa}")
            return datos
        except FileNotFoundError:
            print(f"⚠️ El archivo {ruta_completa} no existe. Se creará json.txt con un mensaje de error.")
            self.crear_json_txt()
            return None
        except Exception as e:
            print(f"❌ Error al leer el archivo JSON: {e}")
            return None

    def crear_json_txt(self):
        ruta_txt = f"{self.ruta_static}json.txt"
        mensaje_error = "El archivo JSON no existe o no se ha generado correctamente."

        try:
            with open(ruta_txt, "w", encoding="utf-8") as archivo:
                archivo.write(mensaje_error)
            print(f"📝 Archivo 'json.txt' creado en {ruta_txt}")
        except Exception as e:
            print(f"❌ Error al crear json.txt: {e}")

# Crear una instancia de la clase Ingestiones
actividad = Ingestiones()

# URL de la API
url_api = "https://www.abibliadigital.com.br/api/books"

# Obtener datos de la API
datos_json = actividad.leer_api(url_api)

# Mostrar resultados en consola
print("📌 Esta es la ruta estática:", actividad.ruta_static)
print("📥 Datos JSON obtenidos:\n", json.dumps(datos_json, indent=4, ensure_ascii=False))  # Formatear salida

# Guardar los datos en un archivo JSON
actividad.escribir_json(datos_json, "libros_api")

# Leer el JSON guardado para verificar que se almacenó correctamente
datos_cargados = actividad.leer_json("libros_api")

if datos_cargados:
    print("✅ Los datos fueron leídos correctamente.")
