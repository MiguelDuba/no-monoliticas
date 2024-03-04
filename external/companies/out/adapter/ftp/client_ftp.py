from ftplib import FTP
import sys, os, json


def get_files_names(config):
    ftp = FTP(
        host=config.host
    )
    ftp.login(user=config.user, passwd=config.password)
    ftp.cwd("companies")
    return ftp.nlst()

def get_file_data(config, file_name):
    ftp = FTP(
        host=config.host
    )
    ftp.login(user=config.user, passwd=config.password)
    ftp.cwd("companies")
    # Read and store file from FTP
    with open(f'temp/{file_name}', 'wb') as fp:
        ftp.retrbinary(f'RETR {file_name}', fp.write)
    ftp.quit()
    # Read file
    temp_file = open(f'temp/{file_name}')
    data = json.load(temp_file)
    temp_file.close()
    os.remove(f'temp/{file_name}')
    print(data)
    return data