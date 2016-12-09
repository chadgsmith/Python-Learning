import Inputs as I
import Game 

if __name__ == '__main__':
	######### Init ###############
	'''
	I.init_board()
	grid = I.set_colors()
	name = {}
	color = {}
	name[1] = I.get_players(1)
	color[1] = I.get_color(1)
	name[2] = I.get_players(2)
	color[2] = I.get_color(2,color[1])

	print '\nP1 : %s : %s' % (name[1],grid[color[1]]) 
	print 'P2 : %s : %s' % (name[2],grid[color[2]])
	#print '\n\033[1;37;41m%s\033[1;m' % 'GAME OVER'
	
	#str.replace("is", "was")
	#In.init_board(grid[color[1]].replace(color[1],'__'))
	#In.init_board(grid[color[2]].replace(color[2],'__'))
	'''
	######### Game ###############
	pos = {}
	pos[1] = Game.get_column(1)
	pos[2] = Game.get_column(2)
	print pos
