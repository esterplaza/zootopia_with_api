import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')


def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary:
    {
    'name': ...,
    'taxonomy': {
      ...
    },
    'locations': [
      ...
    ],
    'characteristics': {
      ...
    }
    },
    """
    api_url = f"https://api.api-ninjas.com/v1/animals?name={animal_name}"
    try:
        response = requests.get(api_url, headers={"X-Api-Key": API_KEY}, timeout=10)
        if response.status_code == requests.codes.ok:
            data = response.json()
            if not data:
                print(f"The animal with the name {animal_name} was not found.")
            return response.json()
        print("Error:", response.status_code, response.text)
        return None
    except requests.exceptions.Timeout:
        print("Timed out")
        return None
