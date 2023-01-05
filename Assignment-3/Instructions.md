# Assignment 3

## Due: December 6, 2022

### This assignment is worth 8% of your final grade

### Late penalties

* up to 1 week late - 10%
* 10% per day thereafter to a maximum of 50%
* **Assignment must be submittted by December 14**

### Assignment Completion

In order to for this assignment to be considered completed you must submit:

* a successful push of your code for part A that passes testing on github.

Note: Assignment completion is the minimum requirement for your assignment to be considered complete.  It does not mean you will receive full marks.

Assignment completion is mandatory to pass dsa456


## Assignment Objectives

In this assignment we will:

*  Create a Tree based data structure

## Repo Creation:

In this assignment you can choose to work on your own or you can have ONE(1) teammate (work in pairs).  It is entirely your choice to work individually or in pairs.  Decide what you want to do then use the instructions below to create your repo.  Follow the instructions carefully.

* [Repo Creation for 1 person](individual-repo-creation.md)
* [Repo Creation for teams of 2](group-repo-creation.md)

## Part A: Implement Trie (15 marks)

A Trie (pronounced "Try") is a Tree based data structure that helps implement functionalities such as autocomplete. It is used to provide a lookups for words in a dictionary.  However instead of storing the words as words, a Trie will store each of the characters of the words into nodes with a terminal marker to indicate the completion of a word.  Any word with the same prefix will share the nodes of the prefix.

For example, suppose I wanted to store the following words into a Trie

"yellow", "yell", "yeti","yes","red","redraw", and "ran".  The Trie that will store all of these words will look like this:
![trie1](https://user-images.githubusercontent.com/1699186/203019929-30843803-b3ec-4224-be4a-f1ff04c93e2e.png)

The astericks in some of the nodes in the drawing indicate that the node is a terminal node. That is, the nodes starting from the first lettered node down to the terminal form a word.  For example, the word "yell" is stored in the Trie using the highlighted nodes.  Also note how there is no astericks on the "o" node as yello is not a word in this particular Trie

![trie2](https://user-images.githubusercontent.com/1699186/203019974-d26bd528-ff90-4661-95f1-299e655c7c53.png)


You are to implement a Trie class. The class declarations are found in the file a3.py

Aside from a skeleton class declaration, you will find a function that will return a number that maps a character to a number from 0 to 25.  Thus the function will return:

  * 'a' or 'A' returns 0
  * 'b' or 'B' returns 1
  * 'c' or 'C' returns 2
  ...
 
**Note the drawing and the above function suggest that one way to implement a Trie is to have each TrieNode contain a list of 26 pointers to other TrieNodes.  This is is only one way to do this.  You do not have to do it exactly this way but it is offered as a suggestion of one possibility.**  As long as it is a Trie structure it will be valid.

***

  A Trie has the following member functions


```python
def insert(self,word)
```
This function adds ***word*** to the Trie
  
***
  
```python
def search(self, word)
```
function returns True if ***word*** is in the Trie, False otherwise.

***
  
```python
def begins_with(self, prefix)
```
function returns a list of words that begin with ***prefix*** in alphabetical order

***  

```python
def get_all(self):
```
function returns a list of all the words in a trie in alphabetical order
 
 
## Reflection (5 marks)

Over the course of the term, you have been exposed to a variety of data structures.  Considering the functionality of a Trie, pick **two** other data structure we have studied and discuss the following:

* How efficient is the creation Trie vs your chosen data structures.
* How good will that data structure be at the main look up tasks of a Trie(search and begins_with).
* How can each of the chosen data structures support the two look up tasks (can you use the exist functionality or do you need to do something extra to what is typically returned?)
    
    
To get full marks on this discussion, please provide details about the data structure you are comparing with the Trie, its features, and how well is it able to handle each of the three tasks of the Trie.
  

## Submitting your assignment

* Push your code into your repo and ensure it passes testing by checking the actions tab
* Push your updated a3.md file into your repo with your reflections

## Rubrics:

This sections describes how your assignment will be graded:


### Coding Rubric:

| Criteria | Level 0 | Level 1 | Level 2 | Level 3 | Level 4 |
|---|---|---|---|---|---|
| **Documentation - 20%** - Documentation is about Intention.  "This function is suppose to do" X.  It doesn't state HOW "we loop, then there is an if, then ..." - this is an example of what not to do.  It doesn't repeat code.  For each function ensure that it describe what it does (at a high level), what it accepts as arguments and any sort of restrictions (number must be positive for example) and what the function should return under what condition (returns true if found for example) |Almost no documentation of any type |only a few functions got documented and documentation tends to be code description as opposed to code intention. | many function documentation missing or severe lack of details for function description or documentation is done only at code level (within the code) and not as an overall intention| a few functions documentation missing. or function description comments lack some detail.  Over documentation.  documenting every line of code is not a good... let the code speak | For all functions state what parameters are (and any limitations, what return value is, what it does. |
| **Code Styling - 10%** Consistent styling is key.  This category describes things like indentation, consistent naming strategies, good variable names, not adding public member functions etc. | more than 5 cases of inconsistent or bad styling | 3 to 5 cases of inconsistent  or bad styling | 2 to 3 cases of inconsistent or bad styling functions | 1 case of inconsistent  or bad styling | Consistency is key. same variable name styling (snake_case pref), same data member styling, same curly bracket positioning, correct and consistent indentation, good variable names | 
|**Correctness and Completeness of Code - 35%**.  This category generally describes errors in logic or missing functionality that may occur only in some cases.  This category also includes using things you are not suppose to use or not following specifications correctly | 4 or more errors | 3 errors | 2 errors - using something you are not suppose to use will count as two errors right away as it is a spec violation | 1 errors | all functions completed and correct |
| **Efficiency - 35%** - Anything that is completely off from optimal run time will always count as an instance of inefficiency.. thus if runtime can be O(n) and your code is written to O(n^2). Writing unnecessary code will also be counted as inefficient even if runtime is same.. for example copying array more than 1 time during a grow() operation | 4 or more instance of inefficiency | 3 instance of inefficiency | 2 instance of inefficiency| 1 instance of inefficiency | Function is as efficient as possible |


### Reflection Rubric

 Criteria | Level 0 | Level 1 | Level 2 | Level 3 | Level 4 |
|---|---|---|---|---|---|
| Analysis | No reflection written | Reflection has no specifics with generic statements that can apply to anything | Reflection lacks depth, only a brief description without any details | Reflection shows some depth but still has missing info.| A thorough reflection that shows knowledge of subject matter and connects ideas |

