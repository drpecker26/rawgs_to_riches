"""cookie methods"""

import hashlib
import random

HASH_ALGORITHM = 'sha1'
_SECRET = str(random.getrandbits(64)) # this is not actually secret...

def hash_value(value):
    hasher = hashlib.new(HASH_ALGORITHM)
    hasher.update(value + _SECRET)
    return hasher.hexdigest()

def create_cookie(value):
    return '%s:%s' % (value, hash_value(value))

def is_valid_cookie(cookie):
    value, hashed = cookie.rsplit(':', 1)
    return hashed == hash_value(value)
