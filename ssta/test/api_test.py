import unittest

from ssta.collect.twitter.api import API


class APITestCase(unittest.TestCase):
    def test_instance(self):
        api = API()
        self.assertIsInstance(api, API)

    def test_get_user(self):
        api = API()
        scr_name = 'eLVasiunyk'
        self.assertEqual(scr_name, api.get_user(screen_name=scr_name, id=None).screen_name)


if __name__ == '__main__':
    unittest.main()
