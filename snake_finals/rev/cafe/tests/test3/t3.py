from hashlib import md5

class magic:
	def __init__(self, h, m, s):
		self.magic = f'{h},{m:o},{s}'

	def __hash__(self):
		return int(md5(str(self.magic).encode()).hexdigest(), 16)

	def __eq__(self, other):
		return str(hash(self)) == other


N = 32399973301113656

for h in range(24):
	for m in range(60):
		for s in range(62):
			mag = magic(h, m, s)
			hd = hash(mag)

			if hd == N:
				print(hd)
				print(h, m, s)
				print(f'magic: |{mag.magic}|')


