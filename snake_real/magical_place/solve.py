flag = 'speqmM5T[@B[%bCf7aK67@t=$}:yuv( -PqL?:hp.Wn8'
al = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789{}_!@#$%^&*()-+=[]:;'<>?./ "
for i, c in enumerate(flag):
	print(al[(al.index(c) - i*2) % 89], end='')
print()

# snakeCTF{Wh4T_a_B3auty_FunC710nAl_L4nguAg3s}
