with open('OGUUIER.pcap', 'rb') as f:
	data = f.read()

print('start')

o = data.find(b'JFIF') - 6

# binwalk -e -o 2478498430 OGUUIER.pcap

print(o)

l = 15529655

with open('OGUUIER.jpg', 'wb') as f:
	f.write(data[o:o+l])

print('done')

# snakeCTF{0p3nwebn3t_ag4in_4nd_ag4in}
