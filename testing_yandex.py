import requests
import unittest


class Yandex_test(unittest.TestCase):

    def setUp(self):
        # Инициализация параметров yandex Disc
        self.yd_token = ''
        self.yd_headers = {'Authorization': 'OAuth ' + self.yd_token}
        self.dir_name =  'test_folder'
        self.put_dir = requests.put(url='https://cloud-api.yandex.net/v1/disk/resources/?path=' + self.dir_name,
                                    headers=self.yd_headers)

    def tearDown(self):
        self.yd_token = ''
        self.yd_headers = {'Authorization': 'OAuth ' + self.yd_token}
        self.dir_name =  'test_folder'
        requests.delete(url='https://cloud-api.yandex.net/v1/disk/resources/?path=' + self.dir_name,
                                       headers=self.yd_headers)


    def test_put_folder(self):


        self.get_dir = requests.get(url='https://cloud-api.yandex.net/v1/disk/resources/?path=' + self.dir_name,
                                    headers=self.yd_headers)

        self.assertEqual('<Response [200]>', str(self.get_dir), 'папка появилась в списке файлов')


if __name__ == '__main__':
    Yandex_test()
