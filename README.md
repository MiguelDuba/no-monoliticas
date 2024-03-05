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
 
        Para iniciar el microservicio ejecutamos el siguiente comando.
 
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
 
 
        HTTP://127.0.0.1:3005/api/house/create
 
        Adjunto el ejemplo del postman utilizado para el experimento.
 
                {
                        "id": "1",
                        "direccion": "Esta es la direccion",
                        "habitaciones":"5",
                        "banos": "2",
                        "descripcion": "casa ultimo modelo 2025"
                }







## Aqui trabajamos con el atributo de calidad 2 : DISPONIBILIDAD.

    El envío de información de los sistemas hacia PDA puede varias, a pesar de tener contratos y tiempos establecidos, pero al depender de sistemas externo, se puede tener la posibilidad de entrar en una operación concurrente cuando las empresas coincidentemente envían información hacia nuestra aplicación, por tanto, el sistema debe está disponible para recibir dicha información y ser capaz de procesarla, por eso aplica el patrón CQRS, con el fin dejar los comandos que afectan la base de datos separado de las consultas.


A continuación, presentamos el paso a paso para desplegar la aplicación desarrollado y obtener un despliegue como el que se presenta en la imagen a continuación:

## 1. Descargar el repositorio desde github en la siguiente URL: 
        (https://github.com/MiguelDuba/no-monoliticas.)

## 2. Levantar los docker con el siguiente comando: 
        
        docker-compose up -d db-company rabbitmq
        

## 3. Pasarse a la carpeta del microservicio.
        
        cd  no-monoliticas/centralizacion_procesamiento
        

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
            * Running on http://127.0.0.1:5000
            * Running on http://192.168.11.3:5000
            Press CTRL+C to quit
			
			
## 7. Pasarse a la carpeta del microservicio.
        
        cd  no-monoliticas/extraccion_automatizada
        

## 8. Crear el entorno virtual.
        
        
        python -m venv venv
        
        
        Una vez creado se debe activar el entorno.

        
        venv\Scripts\activate
        

## 9. Instalar los requerimientos del proyecto.
        
        pip install -r requirements.txt
        

## 10. Iniciar el microservicio.
        python main.py

        Se debe ver asi >

			[*] Waiting for messages from company. To exit press CTRL+C

## 11. Luego desde postman se crear una informacion.

        http://127.0.0.1:5000/api/company/add

		{
			"name":"x compania",
			"age": "16",
			"description":"Hola Mundo",
			"address":{
					"address1":"Calle 11",
					"address2":"Calle 11A",
					"address3":"Norte 24",
					"contry":"Colombia",
					"zip_code":"110821",
					"city":"Bopgota"
			}
		}



## Aqui trabajamos con el atributo de calidad 3 : INTEROPERABILIDAD.

Es necesario validar que el sistema puede conectarse con otros servidores por medio del protocolo HTTP con el fin de obtener información de ellos, inicialmente se empieza con HTTP ya que es el protocolo de comunicación mas usado y que de ser exitoso puede entregar más valor al necio.

A continuación, presentamos el paso a paso para desplegar la aplicación desarrollado y obtener un despliegue como el que se presenta en la imagen a continuación:

## 1. Descargar el repositorio desde github en la siguiente URL: 
        (https://github.com/MiguelDuba/no-monoliticas.)

## 2. Levantar los docker con el siguiente comando: 
        
        docker-compose up -d db-company-report rabbitmq
        

## 3. Pasarse a la carpeta del microservicio.
        
        cd  no-monoliticas/external/companies
        

## 4. Crear el entorno virtual.
        
        
        python -m venv venv
        
        
        Una vez creado se debe activar el entorno.

        
        venv\Scripts\activate
        

## 5. Instalar los requerimientos del proyecto.
        
        pip install -r requirements.txt
        

## 6. Iniciar el microservicio.
        python main.py

        Se debe ver asi >

        [*] Waiting for messages from company. To exit press CTRL+C
			
			
## 07. Luego desde postman se crear una informacion.

Luego nos posicionamos en la carpeta:

cd  no-monoliticas/external/companies/out/adapter/producer

Aquí ejecutamos 

python trigger.py

Se genera un mensaje como el siguiente:

        [x] Sent 'start check companies
