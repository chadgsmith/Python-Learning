def init_board():
	col = 7
	row = 6
	matrix = [['__']*col for i in range(row)]
	print ' ','  '.join(str(x) for x in xrange(1,col+1))
	for rows in range(row):	
		tmp = ''
		for columns in range(col):
			tmp += '|' + str(matrix[rows][columns])
		print tmp+'|'
	print '#'.join('#' for x in xrange(1,13))
	print "  Lets Play 4 Square"
	print '#'.join('#' for x in xrange(1,13))

def get_player1():
	player1 = raw_input('\nType in Player 1 name: ')
	player1 = player1.strip()
	if not player1.isupper() : player1 = player1.upper()
	return player1

def get_player2():
	player2 = raw_input('\nType in Player 2 name: ')
	player2 = player2.strip()
	if not player2.isupper() : player2 = player2.upper()
	return player2

if __name__ == '__main__':
	init_board()
	player1 = get_player1()
	player2 = get_player2()
	print player1, player2
