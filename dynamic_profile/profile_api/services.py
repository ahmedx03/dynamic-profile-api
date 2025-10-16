import requests
from django.conf import settings
from django.utils import timezone

class CatFactService:
    @staticmethod
    def get_random_fact():
        try:
            response = requests.get(
                'https://catfact.ninja/fact',
                timeout=10
            )
            response.raise_for_status()
            data = response.json()
            return data.get('fact')
        except:
            return "Temporarily unavailable: Could not fetch cat fact"

class ProfileService:
    @staticmethod
    def get_profile_data():
        return {
            'status': 'success',
            'user': {
                'email': 'ameeahmedy@gmail.com',  
                'name': 'Ahmed Anwar',
                'stack': 'Python/Django',
            },
            'timestamp': timezone.now().isoformat(),
            'fact': CatFactService.get_random_fact(),
        }