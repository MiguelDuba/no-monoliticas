import requests

def get_companies_info(config):
    api_url = config.host
    response = requests.get(api_url)
    return response.json()
