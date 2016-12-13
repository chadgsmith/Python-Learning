#Game

#CREATE A BOARD
def set_board(col = 7, row = 6):
    matrix = [['__']*col for i in range(row)]
    return matrix

#CREATES A BOARD FOR DECISION MAKING    
def set_memBoard(col = 7, row = 6):
    matrix = [['0']*col for i in range(row)]
    return matrix

#ASK PLAYER FOR COLUMN    
def get_column(num):
	cols = ['1','2','3','4','5','6','7']
	prompt = 'Player %s select columns 1-7 : ' % str(num)
	col = raw_input(prompt)
	if col.upper() == 'EXIT':
		import sys
		print 'Player %s QUIT' % str(num)
		sys.exit()
	if col in cols:
		return col
	else:
		print "wrong number"
		return get_column(num)

#PRINTS BOARD GIVEN WITH COLUMN HEADER
def print_board(matrix,col = 7, row = 6):
    print ' ','  '.join(str(x) for x in xrange(1,col+1))
    for rows in range(row):	
        tmp = ''
        for columns in range(col):
            tmp += '|' + str(matrix[rows][columns])
        print tmp+'|'

#
def get_row(matrix,column,row = 6):
	#print column
	for rows in range(row):
		rows = 5 - rows
		if matrix[rows][column] == '0':
			return rows
		else:
			continue
