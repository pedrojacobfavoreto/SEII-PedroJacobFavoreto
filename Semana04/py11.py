#File objects

#with open('test.txt', 'r') as f:
#	pass
#	print(f.read())

#if = open('test.txt', 'r')

#print(f.name)
#print(f.mode)

#f.close()
################################################
#with open('test.txt', 'r') as f:
#
#	for line in f:
#		print(line, end='')
#
#size_to_read = 100
#
#
#	f_content = f.read(100)
#	print(f_contents, end='')
#
#	f_content = f.readline()
#	print(f_contents, end='')
###############################################
#with open('test.txt', 'r') as f:
#
#	size_to_read = 10
#
#	f_contents = f.read(size_to_read)
#	print(f_contents, end='')
#	f.seek(0)
#
#	f_contents = f.read(size_to_read)
#	print(f_contents)
#
#while len(f_contents) > 0:
#	print(f_contents, end='')
#	f_contents = f.read(size_to_read)
###############################################
#with open('test2.txt', 'w') as f:
#	f.write('Test')
#	f.seek(0)
#	f.write('R')
################################################
#with open('test.txt', 'r') as rf:
#	with open('test_copy.txt', 'w') as wf:
#		for line in rf:
#			wf.write(line)
################################################
with open('bronx.jpg', 'rb') as rf:
	with open('bronx_copy.jpg', 'wb') as wf:
	chunk_size = 4096
	rf_chunk = rf.read(chunk_size)
	while len(rf_chunk) > 0:
		wf.write(rf_chunk)
		rf_chunk = rf.read(chunk_size)
