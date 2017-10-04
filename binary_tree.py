class Node(object):

	def __init__(self,data):
		self.data = data
		self.leftChild = None
		self.rightChild = None


class BinarySearchTree(object):

	def __init__(self):
		self.root = None

	def insert(self,data):
		if not self.root:
			self.root = Node(data)
		else:
			self.insertNode(data,self.root)

	def insertNode(self,data,node):

		if data < node.data:
			if node.leftChild:
				self.insertNode(data,node.leftChild)
			else:
				node.leftChild = Node(data)
		else:
			if node.rightChild:
				self.insertNode(data,node.rightChild)
			else:
				node.rightChild = Node(data)

	def remove(self,data):
		if self.root: #is not none
			self.root = self.removeNode(data,self.root) # Replace the root by the removeNode with data
			###Input the root to removeNode

					#6
			#3					#8
		#2		#4			#7
		   #2.2			#5


	def removeNode(self,data,node): #4,root5  case I-> data 4, (node 3) ->4, node 4 ( <- return tempNode)
									#2,root5 case II ->data 2, (node 3) -> 2, node 2 ( <- return None)
									#3,root5 case III -> data 3 ,(node3) ()
		if not node: #if the node is none 
			return node

		if data < node.data: #1. 如果輸入的data 比root小 
			node.leftChild = self.removeNode(data,node.leftChild) # case I : data 2 node 3 --> 3.leftchild = Node
		elif data > node.data:
			node.rightChild = self.removeNode(data,node.rightChild) #
		else:
			if not node.leftChild and not node.rightChild:
				print 'removing a left node...'
				del node
				return None
			if not node.leftChild:
				print 'Removing a node with single right child'
				tempNode = node.rightChild
				del node
				return tempNode
			elif not node.rightChild:
				print 'Removing a node with single left child'
				tempNode = node.leftChild
				del node
				return tempNode
			print 'Removing node with two children....'
			tempNode = self.getPredeccor(node.leftChild) #(2) -> get 2.2
			node.data = tempNode.data #3 become 2.2
			node.leftChild = self.removeNode(tempNode.data,node.leftChild)#2.2,2
	
		return node
	def getPredecessor(self,node):

		if node.rightChild:
			return self.getPredecessor(node.rightChild)

		return node


	def getMinValue(self):
		if self.root:
			return self.getMin(self.root)

	def getMin(self,node):
		if node.leftChild:
			return self.getMin(node.leftChild)

		return node.data

	def getMaxValue(self,node):
		if self.root:
			return self.getMax(self.root)

	def getMax(self,node):
		if node.rightChild:
			return self.getMax(node.rightChild)
		return node.data

	def traverse(self):
		if self.root:
			self.traverseInOrder(self.root)

	def traverseInOrder(self,node):
		if node.leftChild:
			self.traverseInOrder(node.leftChild)

		print '{} '.format(node.data)

		if node.rightChild:
			self.traverseInOrder(node.rightChild)



bat =  BinarySearchTree()
bat.insert(10)
bat.insert(13)
bat.insert(7)
bat.insert(6)
bat.remove(5)

print bat.traverse()
