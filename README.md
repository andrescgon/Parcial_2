# README para el proyecto de ANTLR con Python

Este documento te guiará a través de la instalación de ANTLR, la configuración de alias necesarios y cómo ejecutar un programa que evalúa expresiones con números racionales.

## Requisitos previos

- Python instalado en tu sistema.
- Java JDK instalado en tu sistema.

## Instalación de ANTLR

1. **Descargar ANTLR:**
   - sudo wget https://www.antlr.org/download/antlr-4.13.2-complete.jar -O /usr/local/lib/antlr-4.13.2-complete.jar
2. **Crear un alias para ANTLR:**
   - Abre tu terminal y edita el archivo de configuración de tu shell (por ejemplo, `~/.bashrc` o `~/.zshrc`).
   - Añade la siguiente línea:
     ```bash
     alias antlr4='java -jar ~/antlr/antlr-4.x-complete.jar'
     ```
   - Guarda y cierra el archivo.
   - Ejecuta `source ~/.bashrc` o `source ~/.zshrc` para aplicar los cambios.

## Instalación de Python y dependencias

1. **Instalar pip (si aún no lo tienes):**
   ```bash
   sudo apt-get install python3-pip  # Para sistemas basados en Debian
   ```

2. **Instalar el paquete `antlr4-python3-runtime`:**
   ```bash
   pip install antlr4-python3-runtime
   ```

## Ejecución del programa

1. **Ejecuta el programa:**
   Asegúrate de que estás en el mismo directorio donde se encuentran `main.py` y los archivos generados por ANTLR. Luego ejecuta:
   ```bash
   python main.py
   ```
2. **Ingresa una expresión racional:**
   Cuando se te pida, ingresa una expresión como `(1/3 + 2/3)` y observa cómo se procesa.


