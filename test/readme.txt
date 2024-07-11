Prueba Técnica

Este proyecto está realizado con el Framework Django, para poder ejecutarlo se debe tener instalado Python y seguir los siguientes pasos dentro de la terminal:
Desde la carpeta test
1-Ejecutar el comando "python -m venv nombre_entorno_virtual" para crear el entorno virtual cambiando nombre_entorno_virtual por el nombre deseado.
2-Activar el entorno virtual con el comando ".\activate" desde la ruta : nombre_entorno_virtual\Scripts\
3-Instalar los requirements con el comando: "pip install -r requirements.txt" desde la ruta: test\
4-Para verficar que fueron isntalados bien los requirements se puede ejecutar el comando "pip freeze"
4-Ejecutar el proyecto con el comando: "python manage.py runserver" desde la carpeta test que es la que contiene el manage.py 
5-Verificar en la terminal si el proyecto se ejecutó correctamente e ir al navegador a las siguientes urls:

http://127.0.0.1:8000/users/   (para ver el resultado del primer endpoint)
http://127.0.0.1:8000/user/fewest_followers/   (para ver el resultado del segundo endpoint)

Información adicional:
Los datos de los usuarios están en la carpeta static\data