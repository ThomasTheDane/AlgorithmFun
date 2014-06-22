def multiplyMatrix(X, Y):
	print X, Y
	if(len(X) == 1):
		print 'root root bitches'
		return X * Y
	if(len(X) == 2):
		print 'almost root'
		print X, Y
		return X[0][0] * Y[0][0]

	X1 = [X[:len(X)/2][0][:len(X)/2], X[:len(X)/2][1][:len(X)/2]]
	X2 = [X[:len(X)/2][0][len(X)/2:], X[:len(X)/2][1][len(X)/2:]]
	X3 = [X[len(X)/2:][0][:len(X)/2], X[len(X)/2:][1][:len(X)/2]]
	X4 = [X[len(X)/2:][0][len(X)/2:], X[len(X)/2:][1][len(X)/2:]]
	
	Y1 = [Y[:len(Y)/2][0][:len(Y)/2], Y[:len(Y)/2][1][:len(Y)/2]]
	Y2 = [Y[:len(Y)/2][0][len(Y)/2:], Y[:len(Y)/2][1][len(Y)/2:]]
	Y3 = [Y[len(Y)/2:][0][:len(Y)/2], Y[len(Y)/2:][1][:len(Y)/2]]
	Y4 = [Y[len(Y)/2:][0][len(Y)/2:], Y[len(Y)/2:][1][len(Y)/2:]]

	return [[multiplyMatrix(X1, Y1)]]

	# return multiplyMatrixPiece(x, y)

def multiplyMatrixPiece(X, Y):
	print 'hi'



def main():
	count = 0
	# print countInversions([8,7,6,5,4,3,2,1], count) # 5 inversions
	print multiplyMatrix([[1,2,3,4],
						  [5,6,7,8],
						  [9,10,11,12],
						  [13,14,15,16]], [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])

if __name__ == '__main__':
	main()





