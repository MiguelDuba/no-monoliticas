import sys, os
from api.consumer.check_companies import *
from core.service.companies_service import seed_companies_db

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