from hashlib import sha256, md5

passwords = ''.join([
	'59951918239556537679872',
	'77e6e4a259339933630b54fe365c5833',
	'11,41,54',
	'ILLY>LAVAZZA', # 'HLLY9LA&A**A',
	'2575c7781734f11a305fb78cdc0f1d6bfae5df385ba5b517e442ba3ab28863ec',
	'f5b209498bfad650eb000b1917fc119b601e799c18c00b6e562e71300ed1cc93',
])

from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
hashed_key = md5(passwords.encode('utf-8')).digest()
ciphertext = open('./flag.bin', 'rb').read()
cipher = AES.new(hashed_key, AES.MODE_ECB)
decrypted = cipher.decrypt(ciphertext)
print(decrypted)


# snakeCTF{0xc0ffeeBaB3_f284d72db2c03569}
