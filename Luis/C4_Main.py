import Inputs as I
import Game 

def Main(player):
	column = 'c%s' % str(player)
	row = 'r%s' % str(player)
	pos[column] = int(Game.get_column(player))-1
	pos[row] = Game.get_row(memBoard,pos[column])
	if pos[row] == None:
		print "Pick a new column"
		Main(player)
	board[pos[row]][pos[column]] = chips[player]
	memBoard[pos[row]][pos[column]] = str(player)
	Game.print_board(board)

		
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
	
	######### Game ###############
	pos = {}
	board = Game.set_board()
	memBoard = Game.set_memBoard()
	Game.print_board(board)
	move = 0
	player = 1
	while True:
		#play player
		Main(player)
		move +=1	
		if move > 6:
		    Game.horizontal(memBoard,player)
		    if Game.get_row2(memBoard) > 0:
		        Game.vertical(memBoard,player)
		        Game.diagonal_up(memBoard,player)
		        Game.diagonal_down(memBoard,player)
		if player == 1 : player = 2
		elif player == 2: player = 1
	#end of code
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
