class SortedList:
	class Node:
		# Node is internal.  Feel free to add
		# to the argument list for its init function if you want
		# you can add additonal data members if you like
		def __init__(self, data):
			self.data = data
			self.next = None
			self.prev = None

	# Sorted list is external, do not change its prototype.
	# you can add additional data members if you like
	def __init__(self):
		self.front = None
		self.back = None
		self.count = 0

	def insert(self, data):
		new_node = self.Node(data)
		self.count += 1

		# If first node is inserted to empty list
		if self.front == None:
			self.front = new_node
			self.back = new_node
			self.front.prev = None
			return

		# if the data of new node is less than front data, inserting it to the front
		# and making front as new node
		if new_node.data < self.front.data:
			self.front.prev = new_node
			new_node.next = self.front
			self.front = new_node
			return

		# if the data inserted has a value greater than the back node, insert it to the last
		# and make back as new node
		if new_node.data > self.back.data:

			new_node.prev = self.back
			self.back.next = new_node
			self.back = new_node
			return

		# Find the node before which we need to insert new_node.
		temp = self.front
		while temp.data < new_node.data:
			temp = temp.next

		# Insert new node before temp
		temp.prev.next = new_node
		new_node.prev = temp.prev
		temp.prev = new_node
		new_node.next = temp

	def remove(self, data):
		current = self.front
		node_deleted = False

		if current is None:
			node_deleted = False
		elif current.data == data:
			self.front = current.next
			if self.front:
				self.front.prev = None
			node_deleted = True
		elif self.back.data == data:
			self.back = self.back.prev
			self.back.next = None
			node_deleted = True
		else:
			while current:
				if current.data == data:
					current.prev.next = current.next
					current.next.prev = current.prev
					node_deleted = True
				current = current.next

		if node_deleted:
			self.count -= 1
			if self.count == 0:
				self.front = None
				self.back = None
			return True
		return False

	def is_present(self, data):
		for node_val in self.__iter__():
			if data == node_val:
				return True
		return False

	def __len__(self):
		return self.count

	# The functions below called __iter__ and __reversed__
	# allows an external function to
	# iterate through your list.
	#
	# myll = SortedList()
	#
	# for i in myll:
	#     print(i)
	#
	# for i in reversed(myll):
	# 	  print(i)
	#
	# with each iteration, curr goes through only one step of the while loop
	# (ie you don't run it all at once..)
	# there are two versions of these function as sentinels nodes do
	# make a difference in terms of where you start and end
	# keep only the version you are using and erase the version you are
	# not using (or comment it out...)

	# NOTE: if you change the names of your data members, you need
	# to change them in the functions below or your tests won't pass.

	# This is the version you need if you do not use sentinels:
	def __iter__(self):
		curr = self.front
		while curr:
			yield curr.data
			curr = curr.next

	def __reversed__(self):
		curr = self.back
		while curr:
			yield curr.data
			curr = curr.prev

	# This is the version you need if you used sentinels:
	# def __iter__(self):
	#     curr = self.front.next
	#     while curr != self.back:
	#         yield curr.data
	#         curr = curr.next
	# 
	# def __reversed__(self):
	#     curr = self.back.prev
	#     while curr != self.front:
	#         yield curr.data
	#         curr = curr.prev
