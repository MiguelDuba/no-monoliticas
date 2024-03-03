import requests

def get_companies_info():
    api_url = "http://localhost:8888/companies"
    response = requests.get(api_url)
    return response.json()
