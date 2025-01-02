from pwn import xor

k = 0x5A

f = b")4;1?\x19\x0E\x1C!mcklo??b?'"

print(xor(f, k))

# snakeCTF{79165ee8e}

