import Inputs as I
import Game 

if __name__ == '__main__':
	######### Init ###############
	name = {}
	color = {}
	chips = {}
	
	I.init_board()
	grid = I.set_colors()
	
	#Player1
	name[1] = I.get_players(1)
	color[1] = I.get_color(1)
	chips[1] = grid[color[1]].replace(color[1],'__')
	
	#Player2
	name[2] = I.get_players(2)
	color[2] = I.get_color(2,color[1])
	chips[2] = grid[color[2]].replace(color[2],'__')

	print '\nP1 : %s : %s' % (name[1],grid[color[1]]) 
	print 'P2 : %s : %s' % (name[2],grid[color[2]])
	#print '\n\033[1;37;41m%s\033[1;m' % 'GAME OVER'
	
	#str.replace("is", "was")
	#In.init_board(grid[color[1]].replace(color[1],'__'))
	#In.init_board(grid[color[2]].replace(color[2],'__'))
	
	######### Game ###############
	pos = {}
	board = Game.set_board()
	memBoard = Game.set_memBoard()
	Game.print_board(board)
	
	while 1:
		#play player1
		pos['c1'] = int(Game.get_column(1))-1
		pos['r1'] = Game.get_row(memBoard,pos['c1'])
		if pos['r1'] == None:
			print "Pick a new column"
			continue
		board[pos['r1']][pos['c1']] = chips[1]
		memBoard[pos['r1']][pos['c1']] = '1'
		Game.print_board(board)
			
		#play player2
		pos['c2'] = int(Game.get_column(2))-1
		pos['r2'] = Game.get_row(memBoard,pos['c2'])
		if pos['r2'] == None:
			print "Pick a new column"
			continue
		board[pos['r2']][pos['c2']] = chips[2]	
		memBoard[pos['r2']][pos['c2']] = '2'
		Game.print_board(board)
	
		#Game.print_board(memBoard)
	
	print pos
	
