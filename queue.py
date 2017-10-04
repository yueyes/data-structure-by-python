#FIFO -first insert-> first take out

class Queue:

	def __init__(self):
		self.queue =[]

	def isEmpty(self):
		return self.queue ==[]

	def enqueue(self,data):
		self.queue.append(data)

	def dequeue(self):
		data = self.queue[0]
		del self.queue[0]
		return data

	def peek(self):
		return self.queue[0]

	def get_size(self):
		return len(self.queue)

q = Queue()

q.enqueue(7) 
q.enqueue(5) 
q.enqueue(9)

print q.get_size()
print q.queue
print 'peek : {}'.format(q.peek())
print 'popped data : {}'.format(q.dequeue())
print q.queue
print 'popped data :{}'.format(q.dequeue())
print q.get_size()
print q.queue
print 