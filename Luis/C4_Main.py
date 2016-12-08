import Inputs as In

if __name__ == '__main__':
	######### Init ###############
	In.init_board()
	player1 = In.get_players(1)
	p1c,clr1 = In.get_color(1)
	player2 = In.get_players(2)
	p2c,clr2 = In.get_color(2,p1c)

	print '\nP1 : %s : \033[1;37;4%sm%s\033[1;m' % (player1,clr1,p1c) 
	print 'P2 : %s : \033[1;37;4%sm%s\033[1;m\n' % (player2,clr2,p2c)
	#print '\n\033[1;37;41m%s\033[1;m' % 'GAME OVER'
	
	######### Game ###############
