boardCounts = 0

class Board(object):
	def __init__(self):
		self.tiles = []
		for i in range(0, 9):
			aRow = []
			for j in range(0, 9):
				aRow += [0]
			self.tiles += [aRow]

	def setTile(self, x, y, val):
		print boardCounts
		self.tiles[x][y] = val

	def checkBoard(self):
		fullRowCount = 0
		# check rows:
		for aRow in self.tiles:
			checkedIn = []
			for aTile in aRow:
				if aTile != 0:
					if aTile in checkedIn:
						return False
					else:
						checkedIn += [aTile]
			if len(checkedIn) == 9:
				fullRowCount += 1

		# check colums 
		for i in range(0, 9):
			checkedIn = []
			for j in range(0, 9):
				if self.tiles[j][i] != 0:
					if self.tiles[j][i] in checkedIn:
						return False
					else:
						checkedIn += [self.tiles[j][i]]

		# check boxes 
		for i in [0, 3, 6]:
			for j in [0, 3, 6]:
				checkedIn = []
				for a in range(3):
					x = i+a
					for b in range(3):
						y = j+b
						if self.tiles[y][x] != 0:
							if self.tiles[y][x] in checkedIn:
								return False
							else:
								checkedIn += [self.tiles[y][x]]
		if fullRowCount == 9:
			global boardCounts
			boardCounts += 1
			if boardCounts % 100 == 0:
				print boardCounts
				self.printBoard()
				
		return True

	def printBoard(self):
		print "-" * 17
		for aRow in self.tiles:
			for aTile in aRow:
				print aTile,
			print ""
		print "-" * 17

def recursiveStep(board, x, y):
	if x > 8:
		x = 0
		y = y + 1
		if y > 8:
			# Got to end of board, fallback
			return False
	
	for i in range(board.tiles[y][x] + 1, 10):
		board.tiles[y][x] = i
		if board.checkBoard():
			recursiveStep(board, x+1, y)

	board.tiles[y][x] = 0
	return False

def makeRecursiveBoards():
	aBoard = Board()
	recursiveStep(aBoard, 0, 0)

def makeValidBoard1():
	aBoard = Board()
	aBoard.setTile(0, 0, 1)
	aBoard.setTile(0, 1, 2)
	aBoard.setTile(0, 2, 3)
	aBoard.setTile(0, 3, 4)
	aBoard.setTile(0, 4, 5)
	aBoard.setTile(0, 5, 6)
	aBoard.setTile(0, 6, 7)
	aBoard.setTile(0, 7, 8)
	aBoard.setTile(0, 8, 9)

	aBoard.setTile(1, 0, 4)
	aBoard.setTile(1, 1, 5)
	aBoard.setTile(1, 2, 6)
	aBoard.setTile(1, 3, 7)
	aBoard.setTile(1, 4, 8)
	aBoard.setTile(1, 5, 9)
	aBoard.setTile(1, 6, 1)
	aBoard.setTile(1, 7, 2)
	aBoard.setTile(1, 8, 3)

	aBoard.setTile(2, 0, 7)
	aBoard.setTile(2, 1, 8)
	aBoard.setTile(2, 2, 9)
	aBoard.setTile(2, 3, 1)
	aBoard.setTile(2, 4, 2)
	aBoard.setTile(2, 5, 3)
	aBoard.setTile(2, 6, 4)
	aBoard.setTile(2, 7, 5)
	aBoard.setTile(2, 8, 6)

	# aBoard.setTile(3, 0, 1)
	# aBoard.setTile(3, 1, 2)
	# aBoard.setTile(3, 2, 3)
	# aBoard.setTile(3, 3, 4)
	# aBoard.setTile(3, 4, 5)
	# aBoard.setTile(3, 5, 6)
	# aBoard.setTile(3, 6, 7)
	# aBoard.setTile(3, 7, 8)
	# aBoard.setTile(3, 8, 9)

	# aBoard.setTile(4, 0, 1)
	# aBoard.setTile(4, 1, 2)
	# aBoard.setTile(4, 2, 3)
	# aBoard.setTile(4, 3, 4)
	# aBoard.setTile(4, 4, 5)
	# aBoard.setTile(4, 5, 6)
	# aBoard.setTile(4, 6, 7)
	# aBoard.setTile(4, 7, 8)
	# aBoard.setTile(4, 8, 9)

	return aBoard

if __name__ == '__main__':
	print boardCounts
	makeRecursiveBoards()
	print boardCounts












	