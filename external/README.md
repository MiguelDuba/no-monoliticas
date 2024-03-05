#How to star the appliaction
## Create python env
```
python -m venv venv
```
## Install requirements
```
pip install -r requirements.txt
```
## Start infrastructure tools
## Posgrest, Rabbitmq, ftp-server
```
docker compose up -d db, rabbitmq, ftp
```
## Start service
