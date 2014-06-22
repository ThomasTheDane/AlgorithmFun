def countInversions(start, count):
	print "top ", count
	if(len(start) == 1):
		return start, count
	X, c1 = countInversions(start[:len(start)/2], count)
	Y, c2 = countInversions(start[len(start)/2 :], count)
	return countSplitInversions(X, Y, c1+c2)

def countSplitInversions(A, B, count):
	C = list()
	n = len(A) + len(B)
	i, j = 0, 0
	for k in range(0, n):
		if((A[i] if i < len(A) else float('inf')) < (B[j] if j < len(B) else float('inf'))):
			C.append(A[i])
			i+=1
		else:
			count += len(A) - i
			C.append(B[j])
			j+=1
	print count
	return C, count

def multiplyMatrix(A, B):
	

def main():
	count = 0
	print countInversions([8,7,6,5,4,3,2,1], count) # 5 inversions

if __name__ == '__main__':
	main()





