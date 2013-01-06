import unittest
import cookie

class TestCookie(unittest.TestCase):
    def setUp(self):
        pass

    def test_create_cookie(self):
        value = 'my cookie'
        my_cookie = cookie.create_cookie(value)
        self.assertIn(value, my_cookie)

    def test_is_valid_cookie(self):
        value = 'my cookie'
        my_cookie = cookie.create_cookie(value)
        self.assertTrue(cookie.is_valid_cookie(my_cookie))

    def test_is_valid_cookie_with_colon(self):
        value = 'my:cookie'
        my_cookie = cookie.create_cookie(value)
        self.assertTrue(cookie.is_valid_cookie(my_cookie))

    def test_is_valid_cookie_fake(self):
        import hashlib
        import random
        hasher = hashlib.new(cookie.HASH_ALGORITHM)
        value = 'my cookie'
        hasher.update(value + str(random.getrandbits(64)))
        fake_cookie = '%s:%s' % (value, hasher.hexdigest())
        self.assertFalse(cookie.is_valid_cookie(fake_cookie))

if __name__ == '__main__':
    unittest.main()
