print '\nClass based board'
#####################################################################################################
class Board:
	def __init__(self,col,row): #self is shared with everyone
		self.col = col
		self.row = row
		self.matrix = []

	def initBoard(self):
		self.matrix = [[' +']*self.col for i in range(self.row)]
	
	def printBoard(self):
		print ' ','  '.join(str(x) for x in xrange(1,self.col+1))
		for rows in range(self.row):	
			tmp = ''
			for columns in range(self.col):
				tmp += ' ' + str(self.matrix[rows][columns])
			print tmp
#main

# Game is 7 cols by 6 rows
column = 5
row = 4
board = Board(column,row) #the __init__ func runs here
board.initBoard()
board.printBoard()

print '\nFunction based board'
#####################################################################################################
def initBoard(rows,col):
	matrix = [[' +']*col for i in range(rows)]
	return matrix

def printBoard(row,col,matrix):
	print ' ','  '.join(str(x) for x in xrange(1,col+1))
	for rows in range(row):	
		tmp = ''
		for columns in range(col):
			tmp += ' ' + str(matrix[rows][columns])
		print tmp
#main
column = 5
row = 4

board = initBoard(row,column)
printBoard(row,column,board)

print '\nRaw based board'
#####################################################################################################
col = 5
row = 4
matrix = [[' +']*col for i in range(row)]
print ' ','  '.join(str(x) for x in xrange(1,col+1))
for rows in range(row):	
	tmp = ''
	for columns in range(col):
		tmp += ' ' + str(matrix[rows][columns])
	print tmp

#end of file

'''
:~:$ python board.py 

Class based board
  1  2  3  4  5
  +  +  +  +  +
  +  +  +  +  +
  +  +  +  +  +
  +  +  +  +  +

Function based board
  1  2  3  4  5
  +  +  +  +  +
  +  +  +  +  +
  +  +  +  +  +
  +  +  +  +  +

Raw based board
  1  2  3  4  5
  +  +  +  +  +
  +  +  +  +  +
  +  +  +  +  +
  +  +  +  +  +

'''
