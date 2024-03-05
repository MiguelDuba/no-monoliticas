# Grupo 33 - Aplicaciones No Monoliticas


## Aqui trabajamos con el atributo de calidad 1 : INTEGRIDAD.

    Desacoplamiento del sistema en sistemas más pequeños que permiten aislamiento del fallo.

A continuación, presentamos el paso a paso para desplegar la aplicación desarrollado y obtener un despliegue como el que se presenta en la imagen a continuación:

## 1. Descargar el repositorio desde github en la siguiente URL: 
        (https://github.com/MiguelDuba/no-monoliticas.)

## 2. Levantar los docker con el siguiente comando: 
        
        docker-compose up -d db-house rabbitmq
        

## 3. Pasarse a la carpeta del microservicio.
        
        cd  no-monoliticas/captura_informacion_manual
        

## 4. Crear el entorno virtual.
        
        
        python -m venv venv
        
        
        Una vez creado se debe activar el entorno.

        
        venv\Scripts\activate
        

## 5. Instalar los requerimientos del proyecto.
        
        pip install -r requirements.txt
        

## 6. Iniciar el microservicio.
        python main.py

        Se debe ver asi >

            * Serving Flask app 'main'
            * Debug mode: off
            WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
            * Running on all addresses (0.0.0.0)
            * Running on http://127.0.0.1:3005
            * Running on http://192.168.1.7:3005
            Press CTRL+C to quit

## 7. Luego desde postman se crear una informacion.



