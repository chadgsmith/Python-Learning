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
			return True # Got 4 connected
			
#################
#################
def check_blocks(x,rnge,board,player,tmp):
	block = ''
	for y in rnge:
		block+=board[x][y]
	if get_winner(player,tmp,block) == True:
		#print block,'(%s,%s)' % (str(x),str(y))
		import sys
		print 'Player %s WON!!!!!' % str(player)
		sys.exit()

def check_horizon(matrix,player,row=6):
	if player == 1: exempt = 2
	elif player == 2: exempt = 1 
	for x in range(row):
		rows = 5 - x
		check_blocks(rows,range(0,4),matrix,player,exempt)
		check_blocks(rows,range(1,5),matrix,player,exempt)
		check_blocks(rows,range(2,6),matrix,player,exempt)
		check_blocks(rows,range(3,7),matrix,player,exempt)
################		
def check_vblocks(rnge,y,board,player,tmp):
	block = ''
	for x in rnge:
		block+=board[x][y]
	if get_winner(player,tmp,block) == True:
		#print block,'(%s,%s)' % (str(x),str(y))
		import sys
		print 'Player %s WON!!!!!' % str(player)
		sys.exit()

def check_vertical(matrix,player,col=7):
	if player == 1: exempt = 2
	elif player == 2: exempt = 1
	for y in range(col):
		check_vblocks(range(0,4),y,matrix,player,exempt)
		check_vblocks(range(1,5),y,matrix,player,exempt)
		check_vblocks(range(2,6),y,matrix,player,exempt)
###############
###############


def get_row2(matrix):
	filled = 0
	for col in range(7):
		if matrix[2][col] != '0':
			filled +=1
	return filled


'''
#Horizontal
for start in range(3):
	start = 5 - start
	block = ''
	for y in range(0,4):
		for k in range(4):
			block+=board[start][k+y]
		if get_winner(player,tmp,block) == True:
		print '\n'

#Vertical
for y in range(0,7):
	for start in range(0,3):
		start = 5-start
			for x in range(4):
				print start-x,y
			print '\n'
		
#DIAGONAL Lup
for start in range(0,3):
	start = 5 - start
	for y in range(4):
		for x in range(4):
			print start-x,x+y
		print '\n set of blocks'

#DIAGONAL Ldown, start at row 2 then 1 then 0
for start in range(0,3):
	start = 2-start
	for y in range(4):      
		for x in range(4):
			print start+x,x+y
		print '\n set of blocks'

'''
