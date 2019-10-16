
class Stack:

	def __init__(self):
		self._stack = []

	def push(self, x):
		self._stack.append(x)

	def pop(self):
		self._stack.pop()

	def __str__(self):
		return str(self._stack)

	def isEmpty(self):
		return self.size()==0

	def size(self):
		return len(self._stack)

if __name__ == "__main__":
	s = Stack()
	s.push(1)
	s.push(2)
