import io
import sys
import requests
import base64
from PIL import Image
from addict import Dict


class Nida(object):
    def __init__(self):
        self.BASE_URL = 'https://ors.brela.go.tz/um/load/load_nida/{}'
        # self.user_json = {}

    @staticmethod
    def get_headers():
        """
        Construct headers for be used while making requests 

        Returns:
            [type]: [description]
        """
        return {
            'Content-Type': 'application/json',
            'Content-Length': '0'
        }

    @staticmethod
    def bytes_to_img(image_str: str) -> Image:
        try:
            decoded_img = base64.b64decode(image_str)
            image_buffer = io.BytesIO(decoded_img)
            return Image.open(image_buffer)
        except Exception as bug:
            print(bug)
            return None

    def pythonize_images(self, user_data: dict) -> dict:
        user_data['PHOTO'] = self.bytes_to_img(user_data['PHOTO'])
        user_data['SIGNATURE'] = self.bytes_to_img(user_data['SIGNATURE'])
        return user_data

    @staticmethod
    def capitalize_keys(user_data):
        new_user_data = {}
        for key in user_data.keys():
            capitalized_key = key.capitalize()
            new_user_data[capitalized_key] = user_data[key]
        return new_user_data

    def preprocess_user_data(self, user_data: dict) -> dict:
        user_data = self.pythonize_images(user_data)
        user_data = self.capitalize_keys(user_data)
        user_data = Dict(user_data)
        return user_data

    def load_user(self, national_id: str, json: bool = False):
        try:
            user_data = self.load_user_information(national_id)
            if not json:
                user_data = self.preprocess_user_data(user_data)
                return user_data
            return user_data
        except Exception as bug:
            print(bug)
            return None

    def load_user_information(self, national_id: str):
        try:
            user_information = requests.post(
                self.BASE_URL.format(national_id),
                headers=self.get_headers()
            ).json()

            if user_information['obj'].get('result'):
                user_data = user_information['obj'].get('result')
                return user_data
            if user_information['obj'].get('error'):
                return None
        except (requests.ConnectionError, requests.ConnectTimeout):
            raise ConnectionError(
                "Can't load user information probably connection issues")


sys.modules[__name__] = Nida()
