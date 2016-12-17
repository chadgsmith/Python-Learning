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

def get_winner(chckr,xmpt,block):
	chckr = str(chckr)
	xmpt = str(xmpt)
	if xmpt not in block and '0' not in block:
		if block.count(chckr) == 4:
		    import sys
		    print block
		    print 'Player %s WON!!!!!' % (chckr)
		    sys.exit()
			#return True # Got 4 connected

def get_row2(matrix):
	filled = 0
	for col in range(7):
		if matrix[2][col] != '0':
			filled +=1
	return filled

#Horizontal
def horizontal(matrix,player):
    if player == 1: tmp = 2
    elif player == 2: tmp = 1
    for start in range(3):
    	start = 5 - start
    	for y in range(0,4):
    	    blockh = ''
    	    for k in range(4):
    	        #print start,k+y
    	        blockh+=matrix[start][k+y]
            #print blockh
            get_winner(player,tmp,blockh)
#Vertical
def vertical(matrix,player):
    if player == 1: tmp = 2
    elif player == 2: tmp = 1
    for y in range(0,7):
        blockv = ''
        for start in range(0,3):
            start = 5 - start
            for x in range(4):
                blockv+=matrix[start-x][y]
            get_winner(player,tmp,blockv)
#DIAGONAL Lup
def diagonal_up(matrix,player):
    if player == 1: tmp = 2
    elif player ==2: tmp = 1
    for start in range(0,3):
        start = 5 - start
        for y in range(4):
            blocku = ''
            for x in range(4):
                blocku+=matrix[start-x][x+y]
            #print blocku
            get_winner(player,tmp,blocku)

#DIAGONAL Ldown, start at row 2 then 1 then 0
def diagonal_down(matrix,player):
    if player ==1 : tmp = 2
    elif player ==2: tmp = 1
    for start in range(0,3):
        start = 2-start
        for y in range(4):
            blockd = ''
            for x in range(4):
                blockd+=matrix[start+x][x+y]
            get_winner(player,tmp,blockd)
            












