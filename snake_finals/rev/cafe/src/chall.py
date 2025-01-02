# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: challenge.py
# Bytecode version: 3.13.0rc3 (3571)
# Source timestamp: 1970-01-01 00:00:00 UTC (0)

import asyncio
import os
import platform
import random
import socket
import string
import time
import uuid
from hashlib import md5, sha256
import aiofiles
import dill
import numpy as np

async def support_1(id):
    await asyncio.sleep(os.urandom(1)[0] / 8)
    async with aiofiles.open(get_file('static/secrets.bin'), 'rb+') as f:
        await f.seek(0)
        matrix1 = np.frombuffer(await f.read(100), dtype=np.uint8).reshape((10, 10))
        await f.seek((id + 1) * 100)
        matrix2 = np.frombuffer(await f.read(100), dtype=np.uint8).reshape((10, 10))
        result_matrix = matrix1
        for i in range(10):
            result_matrix = np.dot(result_matrix, matrix2)
        await f.seek(0)
        await f.write(result_matrix.astype(np.uint8).tobytes())

def test_1():
    try:
        open(get_file('static/secrets.bin'), 'rb+').write(bytes(range(100)))
        loop = asyncio.new_event_loop()
        tasks = [loop.create_task(support_1(i)) for i in range(10)]
            loop.run_until_complete(asyncio.wait(tasks))
            with open(get_file('static/secrets.bin'), 'rb+') as f:
                f.seek(0)
                matrix = np.frombuffer(f.read(100), dtype=np.uint8).reshape((10, 10))
                    assert [136, 199, 97, 79, 174, 233, 70, 25, 66, 64] == list(map(int, matrix[0]))
    except Exception as e:
        return (False, '')

def test_2():
    try:
        fingerprint = {'OS Version': platform.platform(), 'System': platform.system(), 'Release': platform.release(), 'Machine': platform.machine(), 'Processor': platform.processor(), 'Username': os.getlogin(), 'MAC Address': uuid.getnode()}
        del fingerprint['Machine']
    fingerprint = str(fingerprint)
    if fingerprint[1::3] + fingerprint[2::3] + fingerprint[3::3]!= '\' ro:Lu63--nix_-tgb.\'\'sm E\'\'ls:Lu63--ni,Pcs\'\'64 sne π,M ds:91442OVsn ix..0gec86whlc4,St\'\'O,Ree ix..0gec reo:x_\'\'ea\'\'r AArs 2818}Sei\'\'n-109er-64i-i20 ye:GS ea\'\'n-109er\'\'osr 86,Urm:e\'\'Cde\'37992':
        pass  # postinserted
    return (False, '')
    else:  # inserted
        pass  # postinserted
    case [] as OSError:
        fingerprint = ''
        pass

def test_3():
    class magic:
        def __init__(self):
            x = time.localtime().tm_hour
            self.magic = f'{x},{time.localtime().tm_min:o},{time.localtime().tm_sec}'

        def __hash__(self):
            if time.altzone is not None and time.altzone!= (-7200):
                pass  # postinserted
            return

        def __eq__(self, other):
            return str(hash(self)) == other
    m = magic()
    return (m == '32399973301113656', m.magic)

def test_4() -> (bool, str):
    from bytecode import Instr, Bytecode
    lambdacode = (lambda x: (x & 192) >> 4 | (x & 48) << 2 | (x & 12) << 2 | (x & 3) << 6) ^ 170

    b = [
        Instr('LOAD_GLOBAL', (True, 'list')),
        Instr('LOAD_CONST', lambdacode),
        Instr('MAKE_FUNCTION'),
        Instr('STORE_FAST', 'l'),
        
		Instr('LOAD_GLOBAL', (False, 'os')),
		Instr('LOAD_ATTR', (False, 'environ')),
		Instr('LOAD_ATTR', (False, 'get')),
		Instr('LOAD_CONST', ('NOTHING_TO_SEE_HERE')),
		Instr('LOAD_CONST', ('0xdeadbeef')),
		Instr('CALL', (2)),
		Instr('COPY', (1)),
		Instr('STORE_FAST', ('r')),
		Instr('LOAD_ATTR', (True, 'translate')),
		Instr('LOAD_GLOGAL', (False, 'str')),
		Instr('LOAD_ATTR', (True, 'maketrans')),
		Instr('LOAD_GLOBAL', (False, 'string')),
		Instr('LOAD_ATTR', (False, 'printable')),
		Instr('LOAD_GLOBAL', (False, 'string')),
		Instr('LOAD_ATTR', (False, 'printable')),
		Instr('LOAD_CONST', (None)),
		Instr('LOAD_CONST', (None)),
		Instr('LOAD_CONST', (-1)),
		Instr('BUILD_SLICE', (3)),
		Instr('BINARY_SUBSCR'),
		Instr('CALL', (2)),
		Instr('CALL', (1)),
		Instr('STORE_FAST', ('v')),
		Instr('LOAD_GLOBAL', (True, 'map')),
		Instr('LOAD_FAST_LOAD_FAST', ('l', 'v')),
		Instr('LOAD_ATTR', (True, 'encode')),
		Instr('CALL', (0)),
		Instr('CALL', (2)),
		Instr('CALL', (1)),
		Instr('LOAD_FAST', ('r')),
		Instr('BUILD_TUPLE', (2)),
		Instr('RETURN_VALUE'),
	]
		
		# Instr('LOAD_ATTR', (False, 'os')),
		# Instr('LOAD_ATTR', (False, 'environ')),
		# Instr('LOAD_ATTR', (False, 'maketrans')),
		# Instr('LOAD_GLOBAL', (False, 'string')),
		# Instr('LOAD_CONST', None),
		# Instr('CALL', 2),
		# Instr('CALL', 1),
		# Instr('CALL', 2),
		# Instr('LOAD_FAST', 'r'),
		# Instr('BUILD_TUPLE', 2),
		# Instr('RETURN_VALUE'),
		# Instr('b'),
		# Instr('<module>'),
		# Instr('<mask_38>'),
		# Instr('<mask_39>'),
		# Instr('8'),
		# Instr('<mask_41>'),
		# Instr('<mask_42>'),
		# Instr('
    code = b.to_code()
    m, v = eval(code)

    def b():
        for v in m:
            yield (v ^ 225)
    if ''.join(map(hex, b()))!= '0x1f0xf0xf0x5f0xaf0xf0xcb0x9f0xcb0x8f0x8f0xcb':
        pass  # postinserted
    return (False, '')

def test_5():
    try:
        a = b
        c = f
    if not os.path.exists('./challenge.py'):
        pass  # postinserted
    return (False, '')
    except NameError:
        pass

def test_6():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('cafe.challs.snakectf.org', 5875))
    request = 'GET check HTTP/1.1\r\nHost: cafe.challs.snakectf.org\r\nConnection: close\r\nUser-Agent: õ²\tIúÖP\r\nAccept-Encoding: gzip, deflate\r\n\r\n'
    client_socket.sendall(request.encode('latin'))
    response = b''
    pass
    chunk = client_socket.recv(4096)
    if not chunk:
        pass  # postinserted
    break
    client_socket.close()
    headers, body = response.split(b'\r\n\r\n', 1)
    l, body = body.split(b'\r\n', 1)
    l = int(l.decode(), 16)
    p = b''
    if l!= 0:
        p += body[:l]
        body = body[l + 2:]
        l, body = body.split(b'\r\n', 1)
        l = int(l.decode(), 16)
    x = dill.loads(p)
    nonce = random.randbytes(42)
    if not x.__check__(nonce):
        nonce = random.randbytes(42)
    return (True, x.magic.hex())

def get_file(relative_path):
    import sys
    try:
        base_path = sys._MEIPASS
    return os.path.join(base_path, relative_path)
    except Exception:
        base_path = os.path.abspath('.')

def get_flag(passwords):
    from Crypto.Cipher import AES
    from Crypto.Util.Padding import unpad
    hashed_key = md5(passwords.encode('utf-8')).digest()
    ciphertext = open(get_file('static/flag.bin'), 'rb').read()
    cipher = AES.new(hashed_key, AES.MODE_ECB)
    decrypted = unpad(cipher.decrypt(ciphertext), 16)
    return decrypted.decode('utf-8')