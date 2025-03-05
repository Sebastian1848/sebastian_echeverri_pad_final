import json
import requests
import os

class Actividad1: 
    def __init__(self):
        self.ruta_static = "src/pad/static/"  # Ruta base
        self.ruta_json = os.path.join(self.ruta_static, "Json")  # Carpeta donde se guardarán los JSON

        # Verifica si las carpetas existen, si no, las crea
        os.makedirs(self.ruta_json, exist_ok=True)

    def leer_api(self, url):
        """
        Realiza una solicitud GET a una API y devuelve los datos en formato JSON.
        Si la solicitud falla, devuelve un diccionario con el error.
        """
        try:
            response = requests.get(url)
            response.raise_for_status()  # Verifica si hay errores en la solicitud (404, 500, etc.)
            return response.json()  # Retorna el JSON si la solicitud fue exitosa
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}  # Retorna un mensaje de error en formato JSON

    def escribir_json(self, datos, nombre_archivo):
        """
        Escribe los datos en un archivo JSON dentro de la carpeta especificada.
        Si el archivo ya existe, lo sobrescribe.
        """
        ruta_completa = os.path.join(self.ruta_json, f"{nombre_archivo}.json")

        try:
            with open(ruta_completa, "w", encoding="utf-8") as archivo:
                json.dump(datos, archivo, indent=4, ensure_ascii=False)
            print(f"✅ Archivo JSON guardado en: {ruta_completa}")
        except Exception as e:
            print(f"❌ Error al escribir el archivo JSON: {e}")

    def leer_json(self, nombre_archivo):
        """
        Lee un archivo JSON si existe, de lo contrario, devuelve un mensaje de error.
        """
        ruta_completa = os.path.join(self.ruta_json, f"{nombre_archivo}.json")

        if os.path.exists(ruta_completa):
            try:
                with open(ruta_completa, "r", encoding="utf-8") as archivo:
                    datos = json.load(archivo)
                print(f"📂 Datos leídos correctamente desde: {ruta_completa}")
                return datos
            except Exception as e:
                print(f"❌ Error al leer el archivo JSON: {e}")
                return None
        else:
            print(f"⚠️ El archivo {ruta_completa} no existe.")
            return None

# Crear una instancia de la clase Actividad1
actividad = Actividad1()

# Endpoint corregido para obtener datos en JSON
url_api = "https://www.abibliadigital.com.br/api/books"

# Obtener datos de la API
datos_json = actividad.leer_api(url_api)

# Mostrar resultados en consola
print("📌 Esta es la ruta estática:", actividad.ruta_static)
print("📊 Datos JSON obtenidos:", json.dumps(datos_json, indent=4, ensure_ascii=False))  # Formatear salida

# Guardar los datos en un archivo JSON
actividad.escribir_json(datos_json, "libros_api")

# Leer el JSON guardado para verificar que se almacenó correctamente
datos_cargados = actividad.leer_json("libros_api")

if datos_cargados:
    print("✅ Los datos fueron leídos")
