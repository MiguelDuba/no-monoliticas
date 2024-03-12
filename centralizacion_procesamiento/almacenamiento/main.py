import sys, os
from ..almacenamiento.modulos.companies.infraestructura.companies_services import seed_companies_db
from ..almacenamiento.modulos.companies.aplicacion.comandos.add_company_command import start_listen_for_companies

if __name__ == '__main__':
    try:
        seed_companies_db()
        start_listen_for_companies()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)