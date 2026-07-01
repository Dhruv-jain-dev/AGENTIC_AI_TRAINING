# Day 6 – Functions and Memory Management in Python

**Date:** 1 July 2026

## Overview

The sixth day of the Agentic AI Training focused on one of the most fundamental concepts in programming—**Functions**. We learned how functions help organize code into reusable and modular blocks, making programs easier to read, maintain, and debug. The session also covered how Python handles function calls internally, the concept of reference copy, different ways of passing arguments to functions, and how single-valued and multi-valued variables behave in Stack and Heap memory during function execution.

---

## Topics Covered

### 1. Functions in Python

* Learned the concept and purpose of functions in Python.
* Understood how functions help break large programs into smaller, reusable modules.
* Studied the syntax for defining and calling functions.
* Learned the advantages of using functions, such as code reusability, modularity, and improved readability.

---

### 2. Reference Copy in Functions

* Learned how Python passes objects to functions using **reference copying**.
* Understood that instead of creating a completely new object, Python passes a reference to the existing object.
* Discussed how changes to mutable objects inside a function can affect the original object outside the function.
* Explored examples to understand the behavior of reference copying during function calls.

---

### 3. Function Arguments

Studied different ways of passing data to functions.

* **Positional Arguments:** Arguments passed according to their position.
* **Variable-Length Arguments (`*args`):** Allows a function to accept any number of positional arguments.
* **Keyword Arguments (`**kwargs`):** Allows arguments to be passed using parameter names, making function calls more flexible and readable.
* Learned when each type of argument is most useful while designing functions.

---

### 4. Memory Management Inside Functions

* Understood how function calls create a new **stack frame** in Stack memory.
* Learned how **single-valued variables** (such as integers and strings) are managed during function execution.
* Studied how **multi-valued variables** (such as lists and dictionaries) are stored in Heap memory while their references are maintained in the Stack.
* Explored the difference in behavior of immutable and mutable objects when passed to functions.
* Discussed how memory allocation and reference handling influence the output of a program.

---

## Key Takeaways

* Developed a strong understanding of Python functions and their importance in writing modular programs.
* Learned how Python handles function calls through reference copying.
* Explored different methods of passing arguments, including positional, variable-length, and keyword arguments.
* Strengthened understanding of Stack and Heap memory during function execution.
* Gained insight into how mutable and immutable objects behave when passed to functions.

---

## Reflection

Today's session deepened my understanding of Python functions and the way memory is managed during program execution. Learning about reference copying and different types of function arguments helped me understand how data is passed and modified inside functions. These concepts are essential for writing efficient, modular, and maintainable Python programs and will be valuable while developing more advanced Agentic AI applications in the coming weeks.
