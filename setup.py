from setuptools import setup, find_packages

setup(
    name="pad",
    version="0.0.1",
    author="Sebastián Echeverri",
    author_email="",
    description="Módulo para manejar la ingestión y almacenamiento de datos JSON",
    py_modules=["actividad_1"],  # Asegura que el módulo sea reconocido
    install_requires=[
        "pandas",
        "matplotlib",
        "requests"
    ],
)
