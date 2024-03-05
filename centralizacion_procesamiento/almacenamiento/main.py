import sys, os
from core.services.companies_services import seed_companies_db
from api.companies import start_listen_for_companies

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