# You don't have to use these classes, but we recommend them as a good place to start!



from dotenv import load_dotenv
import os
load_dotenv()

class WeatherGetter():
    def __init__(self):
        # Let's set our secrets and keys from the .env file
        # as environment variables.
        self.BASE_URL = 'https://api.darksky.net'
        self.token = os.getenv('DARKSKY')
        if len(self.token) == 0:
            raise ValueError('Missing API key!')

class MongoHandler():
    pass