def init_board(col = 7, row = 6):
	matrix = [['__']*col for i in range(row)]
	#Color in the number 4
	for a in range(0,6): #vertical
		matrix[a][4] = '\033[1;37;41m%s\033[1;m' % ('__')
	for b in range(1,4): # diagonal
		matrix[b][4-b] = '\033[1;37;41m%s\033[1;m' % ('__')
	for c in range(2,6): #horizontal
		matrix[3][c] = '\033[1;37;41m%s\033[1;m' % ('__')
	#Print the BOARD
	print ' ','  '.join(str(x) for x in xrange(1,col+1))
	for rows in range(row):	
		tmp = ''
		for columns in range(col):
			tmp += '|' + str(matrix[rows][columns])
		print tmp+'|'
	#Print game message
	print '#'.join('#' for x in xrange(1,13))
	print '  \033[1;31m%s\033[1;m' % ("Lets Play connect 4")
	print '#'.join('#' for x in xrange(1,13))

def get_players(num):
	prompt = '\nType in Player %s name: ' % str(num)
	player = raw_input(prompt)
	player = player.strip()
	if not player.isupper() : player = player.upper()
	return player

if __name__ == '__main__':
	init_board()
	player1 = get_players(1)
	player2 = get_players(2)
	print player1, player2
	print '\033[1;37;41m%s\033[1;m' % 'GAME OVER'
