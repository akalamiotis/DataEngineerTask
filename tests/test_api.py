import unittest
from scripts.utils import get_data


class TestGetData(unittest.TestCase):
    def test_correct(self):
        api_data = get_data('https://jsonplaceholder.typicode.com/posts')
        assert api_data.status_code == 200
        assert api_data.headers['Content-Type'] == 'application/json; charset=utf-8'

    def test_incorrect_url(self):
        self.assertRaises(RuntimeError, lambda: get_data('https://jsonplaceholder.typicode.com/postsdata'))


if __name__ == '__main__':
    unittest.main()
