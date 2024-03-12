import requests

def get_cadastral(config):
    api_url = config.host
    response = requests.get(f"{api_url}/cadastral")
    return response.json()
