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
	player = player.strip().lower().capitalize()
	return player

def check_color(clr,num,p1clr):
	grid = ['Red', 'Green', 'Yellow','Blue']
	color = clr.strip().lower().capitalize()
	if color in grid:
		#print color,'2'
		if (p1clr == None) or (color != p1clr):
			return color, grid.index(color)+1
		elif p1clr == color:
			print "pick a diff color"
			return get_color(num,p1clr)
	else:
	    print "color is mispelled"
	    return get_color(num,p1clr)			
	

def get_color(num,p1c=None):
	prompt = 'Type in Player %s color, [Red, Green, Yellow or Blue]: ' % (str(num))
	color = raw_input(prompt)
	if color.strip().upper() == 'EXIT' : 
	    import sys
	    sys.exit()
	color,typ = check_color(color,num,p1c)
	#print typ
	return color,typ

if __name__ == '__main__':
	init_board()
	player1 = get_players(1)
	p1c,clr1 = get_color(1)
	player2 = get_players(2)
	p2c,clr2 = get_color(2,p1c)

	print '\nP1 : %s : \033[1;37;4%sm%s\033[1;m \nP2 : %s : \033[1;37;4%sm%s\033[1;m' % (player1,clr1,p1c, player2,clr2, p2c)
	print '\n\033[1;37;41m%s\033[1;m' % 'GAME OVER'
	
