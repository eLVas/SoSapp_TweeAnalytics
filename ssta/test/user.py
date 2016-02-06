import unittest

from ssta.collect.user import User


class UserTestCase(unittest.TestCase):
    def test_create(self):
        screen_name = 'eLVasiunyk'
        user = User(screen_name=screen_name, sync=True)
        self.assertEqual(user.screen_name, user._raw.screen_name)
        self.assertEqual(user.screen_name, user._node['screen_name'])


if __name__ == '__main__':
    unittest.main()
