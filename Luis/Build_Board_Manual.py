import time

# This section of code shows how to drop a piece in the first column

for x in range(0,20):
    print "\n"

col = 5
row = 4
matrix = [['__']*col for i in range(row)]
#matrix[3][0] = '\033[1;37;44m%s\033[1;m' % ('__')
#matrix[0][0] = 'x '

#time.sleep(.75)
for x in range(0,20):
    print "\n"
matrix[0][0] = '\033[1;37;41m%s\033[1;m' % ('__')
print ' ','  '.join(str(x) for x in xrange(1,col+1))
for rows in range(row):	
	tmp = ' '
	for columns in range(col):
		tmp += '|' + str(matrix[rows][columns])
	print tmp+'|'



for y in range(0,3):
	time.sleep(.75)
	for x in range(0,20):
	    print "\n"
	matrix[0+y][0] = '__'
	matrix[1+y][0] = '\033[1;37;41m%s\033[1;m' % ('__')
	print ' ','  '.join(str(x) for x in xrange(1,col+1))
	for rows in range(row):	
		tmp = ' '
		for columns in range(col):
			tmp += '|' + str(matrix[rows][columns])
		print tmp+'|'






'''
# Hard coding 
print ' ','  '.join(str(x) for x in xrange(1,col+1))
for rows in range(row):	
	tmp = ' '
	for columns in range(col):
		tmp += '|' + str(matrix[rows][columns])
	print tmp+'|'

	
time.sleep(.75)
for x in range(0,20):
    print "\n"
matrix[0][0] = '__'
matrix[1][0] = 'x '
print ' ','  '.join(str(x) for x in xrange(1,col+1))
for rows in range(row):	
	tmp = ' '
	for columns in range(col):
		tmp += '|' + str(matrix[rows][columns])
	print tmp+'|'



time.sleep(.75)
for x in range(0,20):
    print "\n"
matrix[1][0] = '__'
matrix[2][0] = 'x '
print ' ','  '.join(str(x) for x in xrange(1,col+1))
for rows in range(row):	
	tmp = ' '
	for columns in range(col):
		tmp += '|' + str(matrix[rows][columns])
	print tmp+'|'



time.sleep(.75)
for x in range(0,20):
    print "\n"
matrix[2][0] = '__'
matrix[3][0] = 'x '
print ' ','  '.join(str(x) for x in xrange(1,col+1))
for rows in range(row):	
	tmp = ' '
	for columns in range(col):
		tmp += '|' + str(matrix[rows][columns])
	print tmp+'|'
'''
