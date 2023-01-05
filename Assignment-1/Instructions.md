# Assignment 1

## Due: October 18

### This assignment is worth 10% of your final grade

### Late penalties

* up to 1 week late - 10%
* 10% per day there after to a maximum of 50%

### Assignment Completion

In order to for this assignment to be considered completed you must submit:

* a successful push of your code for part B that passes testing on github.


Note: Assignment completion is the minimum requirement for your assignment to be considered complete.  It does not mean you will receive full marks.

Assignment completion is mandatory to pass dsa456


## Assignment Objectives

In this assignment we will:

*  draw diagrams of your implementation in order to gain a better insight as to how this is accomplished.
*  implement a sorted linked list
*  analyze the code that we write

NOTE: **as this assignment is about implementing data structures, you are not allowed to make use of any python libraries or use builtin python data structures and functions such as lists and the sort() function**

## Repo Creation:

In this assignment you can choose to work on your own or you can have ONE(1) teammate (work in pairs).  It is entirely your choice to work individually or in pairs.  Decide what you want to do then use the instructions below to create your repo.  Follow the instructions carefully.

* [Repo Creation for 1 person](individual-repo-creation.md)
* [Repo Creation for teams of 2](group-repo-creation.md)

Your team will last for only 1 assignment.  If you decide that you were not able to work together after assignment 1, you can find a new partner or work on your own for the other assignments.

## Part A: Drawings (5 marks)


In your repository you will find two pdf files with diagrams of linked lists. Each diagram has a label indicating the operation to be performed to the linked list.  The specification details of what each function does is listed in part B. 

Decide if you will implement the list with our without the use of sentinel nodes.

Use the appropriate diagram file for your chosen implementation. If you plan to implement part B using sentinels, then your diagrams should use sentinels. If you plan to implement part B without sentinels then your diagrams should be done using the file without sentinels.  Thus, your drawings should match your intended implementation.  If you change your mind on how you want to do your implementation, you will need to redraw the diagrams to match your implementation

Read through the specs.  Modify the list to show what the result of the operation is.  Be clear about what is changing and how.  The diagrams do not need to be neat.. but they need to be understandable.  The idea is to think through what you need to change to achieve your goals.


## Part B: Implementing a Sorted Linked list (15 marks)

The class declarations has been created in the a1.py starter file.  The data member names are provided (but not initialized so code will not compile).

Aside from the class declaration you will find two functions called __iter__

There are two versions because one is for sentinel linked lists while the other is for non-sentinel linked lists.  Please remove the version that does not apply for you leaving only the version that matches your implementation


You are allowed to add data members to both Node and Linked list.
You are also allowed to rename your data members BUT, if you do this, you will need to alter the __iter__ function to match your new data member names.

***


A sorted linked list is a linked list where values stay sorted from smallest to biggest.  That is the smallest value is at the front of the list while the largest is in the back.

When a doubly linked sorted list is first created it is empty.

The sorted list has the following member functions

```python
def insert(self,data)
```
this function inserts data into the list such that the list stays sorted. You may assume that the data being added can be compared using comparison operators

```python
def remove(self,data)
```
this function finds and removes node containing data from the list.  If a node containing data was found and removed, function returns True.  If no such node was found (data was not in list), function returns False

```python
def is_present(self, data)
```
This function returns true, if data is in the list, false otherwise

```python
def __len__(self)
```
This function returns the number of values stored in the list




## Part C Analysis: (5 marks)

Perform an analysis of the 4 functions you wrote with respect to the number of nodes in your list.


## Part D Reflection: (5 marks)

Tell us what you found most challenging when implementing your assignment.  What helped you overcome your challenges, what was most useful?


## Submitting your assignment

* Push your diagram into your repo (remember you can always use the file upload button).  Make the commit message clear that it is the version you you want us to mark.

* Push your code into your repo and ensure it passes testing by checking the actions tab

* Push your updated a1.md file into your repo with your analysis and reflections



## Rubrics:



This sections describes how your assignment will be graded:


### Drawing Rubric:

| Criteria | Level 0 | Level 1 | Level 2 | Level 3 | Level 4 |
|---|---|---|---|---|---|
| Drawing completion | No diagrams present | Less than half the diagrams are completed without flaws | At least Half the diagrams are completed without flaws, but a signficant number are missing or has flaws  | Missing a diagram or one of the diagrams have flaws | All diagrams present and correctly drawn with clear changes to the list|


### Coding Rubric:

| Criteria | Level 0 | Level 1 | Level 2 | Level 3 | Level 4 |
|---|---|---|---|---|---|
| **Documentation - 20%** - Documentation is about Intention.  "This function is suppose to do" X.  It doesn't state HOW "we loop, then there is an if, then ..." - this is an example of what not to do.  It doesn't repeat code.  For each function ensure that it describe what it does (at a high level), what it accepts as arguments and any sort of restrictions (number must be positive for example) and what the function should return under what condition (returns true if found for example) |Almost no documentation of any type |only a few functions got documented and documentation tends to be code description as opposed to code intention. | many function documentation missing or severe lack of details for function description or documentation is done only at code level (within the code) and not as an overall intention| a few functions documentation missing. or function description comments lack some detail.  Over documentation.  documenting every line of code is not a good... let the code speak | For all functions state what parameters are (and any limitations, what return value is, what it does. |
| **Code Styling - 10%** Consistent styling is key.  This category describes things like indentation, consistent naming strategies, good variable names, not adding public member functions etc. | more than 5 cases of inconsistent or bad styling | 3 to 5 cases of inconsistent  or bad styling | 2 to 3 cases of inconsistent or bad styling functions | 1 case of inconsistent  or bad styling | Consistency is key. same variable name styling (camel case pref), same data member styling, correct and consistent indentation, good variable names | 
|**Correctness and Completeness of Code - 35%**.  This category generally describes errors in logic or missing functionality that may occur only in some cases.  This category also includes using things you are not suppose to use or not following specifications correctly | 4 or more errors | 3 errors | 2 errors - using something you are not suppose to use will count as two errors right away as it is a spec violation | 1 errors | all functions completed and correct |
| **Efficiency - 35%** - Anything that is completely off from optimal run time will always count as an instance of inefficiency.. thus if runtime can be O(n) and your code is written to O(n^2). Writing unnecessary code will also be counted as inefficient even if runtime is same.. for example copying array more than 1 time during a grow() operation | 4 or more instance of inefficiency | 3 instance of inefficiency | 2 instance of inefficiency| 1 instance of inefficiency | Function is as efficient as possible |


### Analysis Rubric

 Criteria | Level 0 | Level 1 | Level 2 | Level 3 | Level 4 |
|---|---|---|---|---|---|
| Analysis | No analysis completed | Little to no explanation in analysis... arrives at final result as if by magic  | Lacks a significant component to analysis has one or more major errors or miscalculation within the analysis | Has minor errors or some minor missing steps in analysis  | Clearly laid out analysis with correct flow that shows how all mathematical expressions are obtained.  Clear and consistent usage of mathematical symbols.  Complete and clear count of operations |


### Reflection Rubric

 Criteria | Level 0 | Level 1 | Level 2 | Level 3 | Level 4 |
|---|---|---|---|---|---|
| Analysis | No reflection written | Reflection has no specifics with generic statements that can apply to anything | Reflection lacks depth, only a brief description without any details | Reflection shows some depth with some descriptions.  It does not go far beyond the basic requirements | A clearly written reflection with clear thought that shows depth|

