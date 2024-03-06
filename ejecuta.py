import subprocess
import time

def ejecutar_xampp_control():
    try:
        # Ruta al ejecutable de XAMPP Control
        ruta_xampp_control = r"C:\xampp\xampp-control.exe"

        # Ejecutar XAMPP Control
        subprocess.Popen([ruta_xampp_control], shell=True)
        print("XAMPP Control ejecutado correctamente.")
    except subprocess.CalledProcessError as error:
        print(f"Error al ejecutar XAMPP Control: {error}")

def ejecutar_archivos_bat():
    try:
        # Rutas a los archivos bat
        ruta_mysql_start = r"C:\xampp\mysql_start.bat"
        ruta_apache_start = r"C:\xampp\apache_start.bat"
        
        # Ejecutar ambos archivos bat en paralelo
        proceso_mysql = subprocess.Popen([ruta_mysql_start], shell=True)
        proceso_apache = subprocess.Popen([ruta_apache_start], shell=True)
        
        # Esperar a que ambos procesos finalicen
        proceso_mysql.wait()
        proceso_apache.wait()

        print("Ambos archivos bat ejecutados correctamente.")
    except subprocess.CalledProcessError as error:
        print(f"Error al ejecutar los archivos bat: {error}")

if __name__ == "__main__":
    ejecutar_xampp_control()
    time.sleep(5)  # Esperar 5 segundos para que XAMPP Control se abra completamente
    ejecutar_archivos_bat()
