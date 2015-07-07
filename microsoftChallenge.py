class Node():
	def __init__(self, value, left, right):
		self.value = value
		self.left = left
		self.right = right
	def __str__():
		return self.value

n1 = Node("1", None, None)
n2 = Node("2", None, None)
n3 = Node("3", n1, n2)
n4 = Node("4", None, None)
n5 = Node("5", n3, n4)

def printBreath(startNode):
	stack = [startNode]
	while stack:
		for node in stack:
			print node.value,
		print ""
		aNode = stack.pop()
		if(aNode):
			print aNode.value
			stack += [aNode.left]
			stack += [aNode.right]

printBreath(n5)
#should print 5, 3, 4, 1, 2
