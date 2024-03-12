import requests

def get_companies(config):
    api_url = config.host
    response = requests.get(f"{api_url}/companies")
    return response.json()
