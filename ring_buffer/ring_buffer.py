class RingBuffer:
	def __init__(self, capacity):
		self.capacity = capacity
		self.current = 0
		self.storage = [None]*capacity

	def append(self, item):
		self.storage[self.current] = item
		self.current += 1
		if self.current > self.capacity-1:
			self.current = 0

	def get(self):
		if None in self.storage:
			return [item for item in self.storage if item is not None]
		else:
			return self.storage