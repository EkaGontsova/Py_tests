import requests
import os
import unittest
from dotenv import load_dotenv

load_dotenv()


class TestYandexDiskAPI(unittest.TestCase):
    def setUp(self):
        self.base_url = 'https://cloud-api.yandex.net/v1/disk/resources'
        self.token = os.getenv('YA_TOKEN')
        self.headers = {'Authorization': f'OAuth {self.token}'}
        self.folder_name = 'test'

    def test_create_folder(self):
        # Проверяем, существует ли папка
        response = requests.get(f'{self.base_url}?path={self.folder_name}', headers=self.headers)
        if response.status_code == 200:
            self.fail(f'Папка "{self.folder_name}" уже существует')
        elif response.status_code == 404:
            response = requests.put(f'{self.base_url}?path={self.folder_name}', headers=self.headers)
            self.assertEqual(response.status_code, 201, 'Ошибка {response.status_code}')
        else:
            self.fail(f'При попытке создать папку возникла ошибка: {response.status_code}')

    def test_create_folder_without_auth(self):
        response = requests.put(f'{self.base_url}?path={self.folder_name}')
        self.assertEqual(response.status_code, 401, 'Невозможно создать папку без авторизации')


if __name__ == '__main__':
    unittest.main()
