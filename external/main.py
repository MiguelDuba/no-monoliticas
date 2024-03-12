import sys, os
from config.postgres import create_tables
from multiprocessing import Process
from modulos.companies.infraestructura.consumidores import suscribirse_a_consultar_servidor_compania
from modulos.cadastral.infraestructura.consumidores import suscribirse_a_consultar_servidor_catrastal
from modulos.saga.infraestructura.consumidores import suscribirse_a_consultar_masiva_servers



if __name__ == '__main__':
    try:
        create_tables()
        a = Process(target=suscribirse_a_consultar_servidor_compania)
        b = Process(target=suscribirse_a_consultar_servidor_catrastal)
        c = Process(target=suscribirse_a_consultar_masiva_servers)
        a.start()
        b.start()
        c.start()
        a.join()
        b.join()
        c.join()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)