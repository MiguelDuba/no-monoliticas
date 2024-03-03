import sys, os
from api.consumer.check_companies import *

if __name__ == '__main__':
    try:
        start_listen_for_companies()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)