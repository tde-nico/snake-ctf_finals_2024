import time
from hashlib import md5

def test_3():
    class magic:
        def __init__(self):
            x = time.localtime().tm_hour
            self.magic = f'{x},{time.localtime().tm_min:o},{time.localtime().tm_sec}'

        def __hash__(self):
            if time.altzone is not None and time.altzone!= (-7200):
                return int(md5(str(self.magic).encode()).hexdigest(), 16)
            return None

        def __eq__(self, other):
            return str(hash(self)) == other
    m = magic()
    return (m == '32399973301113656', m.magic)
