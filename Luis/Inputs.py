def init_board(col = 7, row = 6):
	matrix = [['__']*col for i in range(row)]
	matrix[5][4] = '\033[1;37;41m%s\033[1;m' % ('__')
	matrix[4][4] = '\033[1;37;41m%s\033[1;m' % ('__')
	matrix[3][4] = '\033[1;37;41m%s\033[1;m' % ('__')
	matrix[2][4] = '\033[1;37;41m%s\033[1;m' % ('__')
	matrix[1][4] = '\033[1;37;41m%s\033[1;m' % ('__')
	matrix[0][4] = '\033[1;37;41m%s\033[1;m' % ('__')
	matrix[1][3] = '\033[1;37;41m%s\033[1;m' % ('__')
	matrix[2][2] = '\033[1;37;41m%s\033[1;m' % ('__')
	matrix[3][1] = '\033[1;37;41m%s\033[1;m' % ('__')
	matrix[3][2] = '\033[1;37;41m%s\033[1;m' % ('__')
	matrix[3][3] = '\033[1;37;41m%s\033[1;m' % ('__')
	matrix[3][5] = '\033[1;37;41m%s\033[1;m' % ('__')
	print ' ','  '.join(str(x) for x in xrange(1,col+1))
	for rows in range(row):	
		tmp = ''
		for columns in range(col):
			tmp += '|' + str(matrix[rows][columns])
		print tmp+'|'
	print '#'.join('#' for x in xrange(1,13))
	print "  Lets Play 4 Square"
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
