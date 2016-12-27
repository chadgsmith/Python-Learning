col = 7
row = 6
matrix = [['__']*col for i in range(row)]
matrix[5][0] = '\033[1;37;41m%s\033[1;m' % ('__')
print ' ','  '.join(str(x) for x in xrange(1,col+1))
for rows in range(row):	
	tmp = ''
	for columns in range(col):
		tmp += '|' + str(matrix[rows][columns])
	print tmp+'|'
