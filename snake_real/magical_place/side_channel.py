

import subprocess
import string

cmd = "valgrind --trace-children=yes --tool=callgrind mit-scheme < flag.txt 2>&1 | grep refs | cut -d ' ' -f11"
# cmd = "valgrind --trace-children=yes --tool=callgrind mit-scheme < flag.txt"

flag = """(define (mod a b) (remainder a b))
(load "challenge.bin")
%s
"""

# for char in string.ascii_lowercase:
# for char in string.digits:
for char in string.printable[:-6]:
	tmp = flag % (f'speqm{char}'.ljust(44, 'Z'))

	with open('./flag.txt', 'w') as f:
		f.write(tmp)

	p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
	res = p.communicate()[0].strip().decode()
	# res = int(res.replace(',', ''))

	print(char, res)



# flag = ''

# for i in range(64):
# 	for char in string.printable:
# 		with open('./flag.txt', 'w') as f:
# 			f.write(flag + char)
# 		p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
# 		res = p.communicate()[0].strip().decode()
# 		res = int(res.replace(',', ''))
	
# 		print(flag, char, res)
# 		if char == string.printable[0]:
# 			last = res
# 		else:
# 			if res > last + 100:
# 				flag += char
# 				break
# 			elif last > res + 100:
# 				flag += string.printable[0]
# 				break
# 	else:
# 		print('BRUH')
# else:
# 	print('BRUH pt.2')

# print(flag)

