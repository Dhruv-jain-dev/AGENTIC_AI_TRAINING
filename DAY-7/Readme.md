# Day 7 – Recursion, Searching & Sorting Techniques in Python

**Date:** 2 July 2026

## Overview

The seventh day of the Agentic AI Training focused on understanding **recursion**, one of the most important problem-solving techniques in programming. We explored how recursive functions are executed in memory through the Call Stack and revisited the roles of Stack and Heap memory during function execution. The session also introduced fundamental searching and sorting algorithms, including Linear Search, Binary Search, Bubble Sort, and Filtering algorithms. Along with learning their working principles, we compared their efficiencies using time complexity and implemented recursion-based solutions for common programming problems.

---

## Learning Highlights

### Topics Covered

* Recursion and Recursive Functions
* Base Case and Recursive Case
* Call Stack and Memory Management
* Stack Memory and Heap Memory
* Linear Search
* Binary Search
* Bubble Sort
* Filtering Algorithm
* Recursive Problem Solving
* Time Complexity Analysis

---

## 1. Understanding Recursion

* Learned that **recursion** is a technique where a function repeatedly calls itself to solve a problem.
* Understood that large problems can be divided into smaller, similar subproblems until a stopping condition is reached.
* Studied the two essential components of every recursive function:

  * **Base Case** – Terminates the recursion.
  * **Recursive Case** – Continues the recursive calls.
* Discussed the importance of recursion in solving mathematical problems, tree structures, graph traversal, and divide-and-conquer algorithms.

---

## 2. Execution of Recursive Functions

* Learned how Python handles recursive function calls internally.
* Understood that every function call creates a separate **stack frame** in the Call Stack.
* Observed that each recursive call waits until the next call finishes execution.
* Once the base condition is met, function calls return one after another in reverse order.
* Learned that the Call Stack follows the **Last In, First Out (LIFO)** principle.

---

## 3. Stack Memory

* Revised the purpose of Stack Memory during program execution.
* Learned that Stack Memory stores:

  * Function calls
  * Local variables
  * Function parameters
  * Return addresses
* Understood that every recursive call creates a new stack frame.
* Discussed why Stack Memory provides fast access and is automatically managed by Python.

---

## 4. Heap Memory

* Understood that Heap Memory stores dynamically allocated objects.
* Learned that complex data structures such as lists, dictionaries, strings, tuples, sets, and objects are stored in the Heap.
* Discussed how Heap Memory is shared among different functions.
* Learned about Python's automatic memory management through the Garbage Collector.

---

## 5. Linear Search

* Studied the Linear Search algorithm for finding an element in a collection.
* Learned that it examines elements one by one until the required value is found.
* Understood that it can be used on both sorted and unsorted datasets.
* Discussed its simplicity and suitability for smaller datasets.

### Time Complexity

* **Best Case:** O(1)
* **Average Case:** O(n)
* **Worst Case:** O(n)

---

## 6. Binary Search

* Learned that Binary Search works efficiently on **sorted data**.
* Understood how the algorithm repeatedly divides the search space into two halves.
* Compared the target value with the middle element to determine the next search range.
* Discussed why Binary Search is significantly faster than Linear Search for large datasets.

### Time Complexity

* **Best Case:** O(1)
* **Average Case:** O(log n)
* **Worst Case:** O(log n)

---

## 7. Bubble Sort

* Learned the working of the Bubble Sort algorithm.
* Understood that adjacent elements are repeatedly compared and swapped whenever they are in the wrong order.
* Observed that after every iteration, the largest unsorted element reaches its correct position.
* Discussed its advantages, limitations, and practical applications.

### Time Complexity

* **Best Case:** O(n)
* **Average Case:** O(n²)
* **Worst Case:** O(n²)

---

## 8. Filtering Algorithm

* Explored the concept of filtering data based on specific conditions.
* Learned how filtering helps extract only the required information while ignoring unwanted data.
* Discussed practical applications in data analysis, searching, and processing large datasets.

### Common Applications

* Selecting records that satisfy given conditions.
* Filtering even or odd numbers.
* Extracting relevant information from large collections of data.

### Time Complexity

* **Best Case:** O(n)
* **Average Case:** O(n)
* **Worst Case:** O(n)

---

## 9. Problem Solving Using Recursion

Applied recursion to solve various programming problems, including:

* Finding the product of multiple numbers.
* Determining the maximum value from a collection.
* Breaking larger problems into smaller recursive tasks.
* Returning the final solution after reaching the base case.

---

## Key Takeaways

* Built a strong understanding of recursion and recursive thinking.
* Learned how recursive functions are managed using the Call Stack.
* Revised the responsibilities of Stack Memory and Heap Memory during execution.
* Understood the implementation and efficiency of Linear Search, Binary Search, Bubble Sort, and Filtering algorithms.
* Compared algorithm performance using time complexity analysis.
* Strengthened logical reasoning and problem-solving skills through recursion-based programming exercises.

---

## Reflection

Today's session introduced some of the most important concepts in algorithm design and problem solving. Understanding recursion and memory management provided valuable insight into how Python executes functions internally, while learning different searching and sorting algorithms highlighted the importance of choosing efficient solutions for different scenarios. These concepts form a solid foundation for advanced data structures, algorithms, and future Agentic AI development.
