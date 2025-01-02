from bytecode import Instr, Bytecode
import os, string
import dill

lambdacode = lambda x: (((x & 192) >> 4 | (x & 48) << 2 | (x & 12) << 2 | (x & 3) << 6) ^ 170)

b = Bytecode([
	Instr('LOAD_GLOBAL', (True, 'list')),
	Instr('LOAD_CONST', lambdacode.__code__),
	Instr('MAKE_FUNCTION'),
	Instr('STORE_FAST', 'l'),
	Instr('LOAD_GLOBAL', (False, 'os')),
	Instr('LOAD_ATTR', (False, 'environ')),
	Instr('LOAD_ATTR', (True, 'get')),
	Instr('LOAD_CONST', 'NOTHING_TO_SEE_HERE'),
	Instr('LOAD_CONST', '0xdeadbeef'),
	Instr('CALL', 2),
	Instr('COPY', 1),
	Instr('STORE_FAST', 'r'),
	Instr('LOAD_ATTR', (True, 'translate')),
	Instr('LOAD_GLOBAL', (False, 'str')),
	Instr('LOAD_ATTR', (True, 'maketrans')),
	Instr('LOAD_GLOBAL', (False, 'string')),
	Instr('LOAD_ATTR', (False, 'printable')),
	Instr('LOAD_GLOBAL', (False, 'string')),
	Instr('LOAD_ATTR', (False, 'printable')),
	Instr('LOAD_CONST', None),
	Instr('LOAD_CONST', None),
	Instr('LOAD_CONST', -1),
	Instr('BUILD_SLICE', 3),
	Instr('BINARY_SUBSCR'),
	Instr('CALL', 2),
	Instr('CALL', 1),
	Instr('STORE_FAST', 'v'),
	Instr('LOAD_GLOBAL', (True, 'map')),
	Instr('LOAD_FAST_LOAD_FAST', ('l', 'v')),
	Instr('LOAD_ATTR', (True, 'encode')),
	Instr('CALL', 0),
	Instr('CALL', 2),
	Instr('CALL', 1),
	Instr('LOAD_FAST', 'r'),
	Instr('BUILD_TUPLE', 2),
	Instr('RETURN_VALUE')
])

code = b.to_code()
m, v = eval(code)

# b = dill._dill._create_function(b)

def b():
	for v in m:
		yield (v ^ 225)

tmp = ''.join(map(hex, b()))
if tmp != '0x1f0xf0xf0x5f0xaf0xf0xcb0x9f0xcb0x8f0x8f0xcb':
	print((False, ''))
else:
	print((True, v))


