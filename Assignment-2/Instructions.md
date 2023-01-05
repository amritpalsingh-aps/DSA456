## Due: November 22, 2021

### This assignment is worth 12% of your final grade.

### Late penalties

* up to 1 week late - 10%
* 10% per day there after to a maximum of 50%

## Assignment Completion

In order to for this assignment to be considered completed you must submit:

* a completed analysis of functions listed for (part A)
* a successful run for part C (green check for part C in actions)

Note: Assignment completion is the minimum requirements for your assignment.  It does not mean you will receive full marks.


## Assignment Objectives:

In this assignment, you will:

* Complete an analysis of multiple related functions for a class
* Implement hash tables

## Repository Setup

* [Repo Creation for 1 person](individual-repo-creation.md)
* [Repo Creation for teams of 2](group-repo-creation.md)

For this assignment you can choose to work entirely on your own or with one partner.  The choice is entirely yours and it will have no effect on your mark for this assignment.  Any mark received will be given to every member of your team.  You do not have to keep your team beyond one assignment (so if you find you are not working well with your partner, you don't have to stay with them for the entire course).

No matter which option you choose, you need to set up a repository for your assignment, even if you are working by yourself. You cannot just use your lab repository. The starter files and tester will be in the repo you create.

If you are working with a partner, we would like you to work such that for each item, if one person did the writing (the author), the other person would verify and check the work (the checker).   The authoring of the work should be split approximately equally.  Work needs to be split so that each person authors parts of the programming and non-programming components.  In other words, each person needs to write some code and do some analysis/reflection.

## Restrictions

**As this assignment is about implementing data structures, you are not allowed to make use of any python libraries or use builtin python data structures and functions unless otherwise stated.**


## Overview


In this assignment you will look at several implementations of a Table.  There are three tasks:

1. Analyze the member functions of the class SortedTable (code for this is provided below).  This table is created using a sorted list.  It is not necessarily implemented well.  You will analyze the listed functions.
2. Offer suggestions on how to make the SortedTable more efficient.  After analyzing the functions, look at how it is done and come up with some changes that will make the code more efficient
3. Implement a Hash table
	* using chaining for collision resolution
	* using linear probing for collision resolution

## Table functions overview

We will explore 3 ways to implement a Table.  Each method will have a different internal structure but the functionality will be the same.  A table stores a set of key-value pairs which are also referred to as ***records***

The following specification describes an overview of the general functionalities of the table but it does not specify any specifics in terms of implementation.  In otherwords, it describes what it can do but doesn't specify any internal data strctures

---

```python
	def __init__(self, capacity=32):
```
The initializer for the table defaults the initial table capacity to 32.  It creates a list with capacity elements all initialized to None.

---

```python
	def insert(self, key, value):
```
This function adds a new key-value pair into the table. If a record with matching key already exists in the table, the function does not add the new key-value pair and returns False. Otherwise, function adds the new key-value pair into the table and returns True.  If adding a record will cause the table to be "too small" (defined in each class), the function will grow to acommodate the new record.

---

```python
	def modify(self, key, value):
```

This function modifies an existing key-value pair into the table. If no record with matching key exists in the table, the function does nothing and returns False. Otherwise, function modifies the existing value into the one passed into the function and returns True.

---


```python
	def remove(self, key):
```

This function removes the key-value pair with the matching key.  If no record with matching key exists in the table, the function does nothing and returns False.  Otherwise, record with matching key is removed and returns True

---

```python
	def search(self, key):
```

This function returns the value of the record with the matching key.  If no record with matching key exists in the table, function returns None

---

```python
	def capacity(self):
```

This function returns the number of spots in the table.  This consists of spots available in the table.  

---

```python
	def __len__(self):
```
This function returns the number of Records stored in the table.

---


## Part A: Analyze the listed member functions of the SortedTable (12 marks)



Analyze the following functions with respect to the number of Records stored in the SortedTable

```python
	def insert(self, key, value):
	def modify(self, key, value):
	def remove(self, key):
	def search(self, key):
	def capacity(self):
	def __len__(self):

```


**Note: the code below is not necessarily the best way to write a table using a sorted array.  Outside of syntactic constructs, do not actually use this code for anything... its has a lot of inefficiencies.**

```python

class SortedTable:

	# packaging the key-value pair into one object
	class Record:
		def __init__(self, key, value):
			self.key = key
			self.value = value


	def __init__(self, cap=32):
		# this initializes a list of of capacity length with None
		self.the_table = [None for i in range(cap)]
		self.cap = cap

	def insert(self, key, value):
		if (self.search(key)!=None):
			return False

		if(len(self) == self.cap):
			# increase the capacity if list is full
			new_table = [None for i in range(self.cap*2)]
			for i in range(self.cap):
				new_table[i]=self.the_table[i]
			self.the_table = new_table
			self.cap *= 2


		self.the_table[len(self)]=self.Record(key,value)
		size = len(self)
		for i in range (0,size-1):
			for j in range(0,size-1-i):
				if(self.the_table[j].key>self.the_table[j+1].key):
					tmp=self.the_table[j]
					self.the_table[j]=self.the_table[j+1]
					self.the_table[j+1]=tmp
		return True

	def modify(self, key, value):
		i = 0
		while (i < len(self) and self.the_table[i].key != key):
			i+=1
		if(i==len(self)):
			return False
		else:
			self.the_table[i].value = value
			return True

	def remove(self, key):
		i = 0
		size = len(self)
		while (i < size and self.the_table[i].key != key):
			i+=1
		if(i==size):
			return False
		while(i+1 < size):
			self.the_table[i]=self.the_table[i+1]
			i+=1
		self.the_table[i] = None
		return True

	def search(self, key):
		i = 0
		size = len(self)
		while  i < size and self.the_table[i].key != key :
			i+=1
		if i==size:
			return None
		else:
			return self.the_table[i].value

	def capacity(self):
		return self.cap

	def __len__(self):
		i =0
		count = 0
		while(i < len(self.the_table)):
			if(self.the_table[i]!=None):
				count+=1
			i+=1
		return count

``` 

## Part B: Suggestions (4 marks)

Suggest 2 improvements you could make to the code that will improve its efficiency. State which function(s) would be improved by the suggested improvement.  Write up your suggestion into a2.md.   This is not a coding question.  You do not need to implement your suggestion.  A clear description of what you want to do is good enough.

**Which improvements counts and which do not**:
* You can't change the underlying data structure.  For example, "make it a hash table" would make it something different so that won't count.  Fundamentally it must use a sorted python list as the underlying data structure
* A change only counts once: "Do a selection sort instead of what is written in the __len__() function" and "Do a selection sort instead of what is written in the capacity() function" is just one suggestion not two. (note this suggestion is silly, and just used as an example)

## Part C Implementation of ChainingTable and LinearProbingTable (24 marks)


When doing this coding portion of the assignment you can use:
* python lists
* your assignment 1 linked list
* python hash() function - don't write your own



A hash table places records based on a hash value that you get from a hash function.  We will use the built in hash function in python for this part of the assignment.  A hash function will return a really big number when given something to hash.  We will use this function to hash the key of our key-value pair (not the value, just the key).

Example usage:

```python
x = hash("hello world")     # x will be a number with many digits, possibly negative.
cap = 32	
idx = x % cap               # idx is guaranteed to be a value between 0 and 31 inclusive 
                            # because the mod operator guarantees that when you say x % n
                            # the result is always between 0 and n-1 inclusive
```

You will implement two hash tables for this assignment.  One will use linear probing for collision resolution, the other will use chaining.  You can use your assingment 1 linked list for chaining table if you wish.

### ChainingTable:

A ChainingTable is a hash table which uses chaining as its collision resolution method.

```python
	def __init__(self, capacity=32):
```
The initializer for the table defaults the initial table capacity to 32.  It creates a list with capacity elements all initialized to None.


```python
	def insert(self, key, value):
```
This function adds a new key-value pair into the table. If a record with matching key already exists in the table, the function does not add the new key-value pair and returns False. Otherwise, function adds the new key-value pair into the table and returns True.  If adding the new record causes the load factor to exceed 1.0, you must grow your table by doubling its capacity

---

```python
	def modify(self, key, value):
```
This function modifies an existing key-value pair into the table. If no record with matching key exists in the table, the function does nothing and returns False. Otherwise, function modifies the changes the existing value into the one passed into the function and returns True

---


```python
	def remove(self, key):
```
This function removes the key-value pair with the matching key.  If no record with matching key exists in the table, the function does nothing and returns False.  Otherwise, record with matching key is removed and returns True

---

```python
	def search(self, key):
```

This function returns the value of the record with the matching key.  If no reocrd with matching key exists in the table, function returns None

---

```python
	def capacity(self):
```
This function returns the number of spots in the table.  This consists of spots available in the table.  

---

```python
	def __len__(self):
```
This function returns the number of Records stored in the table.

---



### LinearProbingTable:

A LinearProbingTable is a hash table which uses linear probing as its collision resolution method.  You can either use the tombstone method or the non-tombstone method.  The choice is yours.

```python
	def __init__(self, capacity=32):
```
The initializer for the table defaults the initial table capacity to 32.  It creates a list with capacity elements all initialized to None.

---


```python
	def insert(self, key, value):
```
This function adds a new key-value pair into the table. If a record with matching key already exists in the table, the function does not add the new key-value pair and returns False. Otherwise, function adds the new key-value pair into the table and returns True. If adding the new record causes the load factor to exceed 0.7, you must grow your table by doubling its capacity

---

```python
	def modify(self, key, value):
```
This function modifies an existing key-value pair into the table. If no record with matching key exists in the table, the function does nothing and returns False. Otherwise, function modifies the changes the existing value into the one passed into the function and returns True

---

```python
	def remove(self, key):
```

This function removes the key-value pair with the matching key.  If no record with matching key exists in the table, the function does nothing and returns False.  Otherwise, record with matching key is removed and returns True

---

```python
	def search(self, key):
```

This function returns the value of the record with the matching key.  If no reocrd with matching key exists in the table, function returns None

---

```python
	def capacity(self):
```
This function returns the number of spots in the table.  This consists of spots available in the table.  

---

```python
	def __len__(self):
```

This function returns the number of Records stored in the table.

---



## Submission:

In order to for this assignment to be considered completed you must submit:
* the analysis for part A (placed in the a2.md)
* a successful run for part C (green check for part C in actions)

Part B is optional for completion but failure to complete it will result in 0 for part B

Please make sure you follow the steps listed below fully

### What/How to submit

For part A to be considered complete, you must submit an updated a2.md with analysis of the listed functions. (part A is mandatory)

For part B, please place answers into a2.md

For part C to be considered completed, you must submit your a2.py into the main branch of your a2 repository.  Your assignment is not complete unless it passes testing (look in the action tab for) a greencheckmark for assignment 2. (part C is mandatory)


### Resubmissions

* With the test verification there is very rarely a need to have you resubmit your program.  However, if there are many errors in your program or it misses the point entirely (you simply copied the sortedTable code into your hash table), you may be asked to resubmit your work.  Any work that is resubmitted, will receive a 50% penalty

## Grading Breaking

### Part A (analysis)

There are 6 functions/scenarios you are asked to analyze for part A and it is worth 12 marks.  The rubric for grading analysis is as follows:

 Criteria | Level 0 | Level 1 | Level 2 | Level 3 | Level 4 |
|---|---|---|---|---|---|
| Analysis | No analysis completed | Little to no explanation in analysis... arrives at final result as if by magic  | Lacks a significant component to analysis has one or more major errors or miscalculation within the analysis | Has minor errors or some minor missing steps in analysis  | Clearly laid out analysis with correct flow that shows how all mathematical expressions are obtained.  Clear and consistent usage of mathematical symbols.  Complete and clear count of operations |

Each function is judged independently.

### Part B (Improvements)

You get two marks for each improvement suggestion that isn't saying the same thing... so if you suggest doing one thing and that results in 3 function being faster, that isn't 3 different suggestions.  that is just one suggestion.  Make sure you have 2 distinct suggestions for improvements.  Improvements also cannot fundamentally change the data structure (it must stay a sorted array)

### Part C (Implementation)

| Criteria | Level 0 | Level 1 | Level 2 | Level 3 | Level 4 |
|---|---|---|---|---|---|
| **Documentation - 20%** - Documentation is about Intention.  "This function is suppose to do" X.  It doesn't state HOW "we loop, then there is an if, then ..." - this is an example of what not to do.  It doesn't repeat code.  For each function ensure that it describe what it does (at a high level), what it accepts as arguments and any sort of restrictions (number must be positive for example) and what the function should return under what condition (returns true if found for example) |Almost no documentation of any type |only a few functions got documented and documentation tends to be code description as opposed to code intention. | many function documentation missing or severe lack of details for function description or documentation is done only at code level (within the code) and not as an overall intention| a few functions documentation missing. or function description comments lack some detail.  Over documentation.  documenting every line of code is not a good... let the code speak | For all functions state what parameters are (and any limitations, what return value is, what it does. |
| **Code Styling - 10%** Consistent styling is key.  This category describes things like indentation, consistent naming strategies, good variable names, not adding public member functions etc. | more than 5 cases of inconsistent or bad styling | 3 to 5 cases of inconsistent  or bad styling | 2 to 3 cases of inconsistent or bad styling functions | 1 case of inconsistent  or bad styling | Consistency is key. same variable name styling (camel case pref), same data member styling, same curly bracket positioning, correct and consistent indentation, good variable names | 
|**Correctness and Completeness of Code - 35%**.  This category generally describes errors in logic or missing functionality that may occur only in some cases.  This category also includes using things you are not suppose to use or not following specifications correctly | 4 or more errors | 3 errors | 2 errors - using something you are not suppose to use will count as two errors right away as it is a spec violation | 1 errors | all functions completed and correct |
| **Efficiency - 35%** - Anything that is completely off from optimal run time will always count as an instance of inefficiency.. thus if runtime can be O(n) and your code is written to O(n^2). Writing unnecessary code will also be counted as inefficient even if runtime is same.. for example copying array more than 1 time during a grow() operation | 4 or more instance of inefficiency | 3 instance of inefficiency | 2 instance of inefficiency| 1 instance of inefficiency | Function is as efficient as possible |

