import requests

URL = "https://api.freecurrencyapi.com/v1/latest?apikey="
API_KEY = "fca_live_VwM4HMSqi04e36YiIDOTyNtQSxiK8NH6frVaiI9V"


def get_actual_currencies():
    response = requests.get(URL + API_KEY)
    actual_currencies = response.json().get('data')
    return actual_currencies
