# if you wish to use your sorted list from a1, copy and paste it here
# this is not the best way to do this but the test scripts are not
# designed to pick up an extra file. 

class ChainingHash:

	# This is a single record in a chaining hash table.  You can
	# change this in any way you wish (including not using it at all)
	class Record:
		def __init__(self, key = None, value=None):
			self.key=key
			self.value=value


	# You cannot change the function prototypes below.  Other than that
	# how you implement the class is your choice (but it must be a hash
	# table that use chaining for collision resolution
	def __init__(self, cap=32):
		self.cap = cap
		self.the_table = [[] for i in range(self.cap)]
		self.length=0
	def insert(self,key, value):
		self.length+=1
		h = hash(key) % self.cap
		for kv in self.the_table[h]:
			if(kv[0]==key):
				self.length-=1
				return False
		if ((1.0* (self.length) / self.cap) >1):
			self.rehash()
		self.the_table[h].append((key,value))
		return True
	def modify(self, key, value):
		h=hash(key)%self.cap
		for index, kv in enumerate(self.the_table[h]):
			if (kv[0] == key):
				self.the_table[h][index]=(key,value)
				return True
		return False
	def remove(self, key):
		h = hash(key) % self.cap
		for index,kv in enumerate(self.the_table[h]):
			if(kv[0]==key):
				del self.the_table[h][index]
				self.length-=1
				return True
		return False
	def search(self, key):
		h = hash(key) % self.cap
		for kv in self.the_table[h]:
			if(kv[0]==key):
				return kv[1]
		return None
	def capacity(self):
		return self.cap
	def __len__(self):
		return self.length
	def rehash(self):
		self.length=1
		self.cap=self.cap*2
		oldTable=self.the_table
		self.the_table=[[] for i in range(self.cap)]
		for item in oldTable:
			for pop in item:
					self.insert(pop[0],pop[1])

class LinearProbingHash:

	# This is a single record in a chaining hash table.  You can
	# change this in anyway you wish (including not using it at all)
	class Record:
		def __init__(self, key = None, value=None):
			self.key=key
			self.the_table=value


	# You cannot change the function prototypes below.  Other than that
	# how you implement the class is your choice (but it must be a hash
	# table that use linear probing for collision resolution)

	def __init__(self, cap=32):
		self.cap=cap
		self.the_table = [None] * self.cap
		self.length = 0
		self.max_load_factor = 0.70
	def insert(self,key, value):
		self.length += 1
		hashed_key = hash(key) % self.cap
		while self.the_table[hashed_key] is not None:
			if self.the_table[hashed_key][0] == key:
				self.length -= 1
				return False
			hashed_key = self._increment_key(hashed_key)
		if self.length / float(self.cap) >= self.max_load_factor:
			self.rehash()
		tuple = (key, value)
		self.the_table[hashed_key] = tuple
		return True
	def modify(self, key, value):
		h = hash(key) % self.cap
		k=h
		while self.the_table[h] is not None and h!=k-1:
			if(self.the_table[h][0]==key and self.the_table[h][0]!=None):
				self.the_table[h]=(key,value)
				return True
			h = self._increment_key(h)
		return False
	def remove(self, key):
		count=0
		for item in self.the_table:
			if(item is not None):
				if(item[0]==key):
					self.the_table[count]=None
					self.length-=1
					return True
			count+=1
		return False
	def search(self, key):
		for item in self.the_table:
			if(item is not None):
				if(item[0]==key):
					return item[1]
		return None
	def capacity(self):
		return self.cap
	def __len__(self):
		if(self.length>self.cap):
			self.length-=1
		return self.length
	def rehash(self):
		self.cap *= 2
		self.length = 1
		old_table = self.the_table
		self.the_table = [None] * self.cap
		for tuple in old_table:
			if tuple is not None:
				self.insert(tuple[0],tuple[1])

	def _increment_key(self, key):
		return (key + 1) % self.cap