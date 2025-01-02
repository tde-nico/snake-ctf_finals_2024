import hashlib

class cafe:
	def __init__(self):
		self.agent = bytes.fromhex('f5b209498bfad650')

	def check(self, nonce):
		self.magic = self.agent + bytes.fromhex('eb000b') + nonce
		n = int.from_bytes(hashlib.sha256(self.magic).digest(), 'little')

		return n < 2 ** 160
