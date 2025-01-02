from hashlib import md5

fingerprint = '\' ro:Lu63--nix_-tgb.\'\'sm E\'\'ls:Lu63--ni,Pcs\'\'64 sne π,M ds:91442OVsn ix..0gec86whlc4,St\'\'O,Ree ix..0gec reo:x_\'\'ea\'\'r AArs 2818}Sei\'\'n-109er-64i-i20 ye:GS ea\'\'n-109er\'\'osr 86,Urm:e\'\'Cde\'37992'
n = len(fingerprint)
f = [None] * n

for i in range(n // 3 + 1):
	f[i*3] = fingerprint[i]
for i in range(n // 3+1):
	f[i*3+1] = fingerprint[n//3+1+i]
for i in range(n // 3):
	f[i*3+2] = fingerprint[n//3+1+n//3+1+i]

f = '{' + ''.join(f)

digest = md5(f.encode()).hexdigest()
print(digest)
