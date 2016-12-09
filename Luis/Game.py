#Game

def get_column(num):
	cols = ['1','2','3','4','5','6','7']
	prompt = 'Player %s select colomns 1-7 : ' % str(num)
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
