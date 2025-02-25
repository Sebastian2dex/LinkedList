class LinkedList:
	class Node:
		def __init__(self, data: int):
			self.data = data
			self.next = None

	def __init__(self):
		self.head = None
		self.count = 0

	def addfirst(self, data):
		node = self.Node(data)
		self.count += 1
		if self.head is None:
			self.head = node
			return

		node.next = self.head
		self.head = node

	def addlast(self, data):
		node = self.Node(data)
		self.count += 1
		if self.head is None:
			self.head = node
			return

		copy = self.head
		while copy.next is not None:
			copy = copy.next

		copy.next = node


	def addall(self, a: list):
		for var in a:
			self.addlast(var)
			self.count += 1
	
	def deletefirst(self):
		if self.head is None:
			return
		self.head = self.head.next
		self.count -= 1

	def deletelast(self):
		if self.head is None:
			return
		copy = self.head
		while copy.next.next is not None:
			copy = copy.next
		copy.next = None
		self.count -= 1

		
	def deleteall(self):
		self.head = None
		self.count = 0

	def printlist(self):
		copy = self.head
		while copy is not None:
			print(copy.data, end=" ")
			copy = copy.next
		print()


if __name__ == '__main__':
	pass