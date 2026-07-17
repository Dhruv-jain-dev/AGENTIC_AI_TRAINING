# Day 17 – Advanced Python Programming: Iterators, Generators, Decorators & Functional Programming

**Date:** 16 July 2026

---

## Overview

The seventeenth day of the **Agentic AI with Python Training Program** introduced advanced Python programming concepts used to develop efficient, reusable, and maintainable applications. The session explored **Iterators, Generators, Decorators, Lambda Functions**, and **Functional Programming** with `map()`, `filter()`, and `reduce()`. Through practical implementations such as tax computation, subscription plan calculations, and flight data processing, the session strengthened both theoretical understanding and real-world programming skills.


## Topics Covered

- Iterators and Iteration Protocol
- Iterators on Lists, Tuples, Sets, Strings, and Dictionaries
- Generators and the `yield` Keyword
- Decorators
- Lambda Functions
- Functional Programming (`map()`, `filter()`, `reduce()`)
- `functools` Module
- Flight Dictionary Assignment

---

### 1. Iterators

An **Iterator** is an object that enables sequential access to the elements of an iterable **one at a time** using the `iter()` and `next()` functions. It follows Python's iteration protocol and allows efficient traversal of data without loading all elements into memory at once.

- Created iterators using the `iter()` function.
- Retrieved elements sequentially using the `next()` function.
- Understood Python's iteration protocol and how loops work internally.
- Explored iterator behavior on lists, tuples, sets, strings, and dictionaries.
- Learned how iterators improve memory efficiency by processing one element at a time.

---

### 2. Iterators on Different Data Structures
Python collections support iteration, but the way elements are traversed depends on the characteristics of each collection, such as whether it is ordered, unordered, mutable, or immutable.

- **List** – Iterates through elements in insertion order (ordered and mutable).
- **Tuple** – Traverses elements in order (ordered and immutable).
- **Set** – Iterates through unique elements in an unordered manner.
- **String** – Accesses one character at a time.
- **Dictionary** – Iterates over keys by default, while values can be accessed using their corresponding keys.

---
---

### 3. Generators
A **Generator** is a special type of function that uses the `yield` keyword to produce values **one at a time** instead of returning them all at once. It pauses execution after each `yield` statement and resumes from the same point when the next value is requested, making it memory efficient.

- Learned the difference between `return` and `yield`.
- Understood the concept of lazy evaluation.
- Explored memory-efficient programming using generators.
- Learned how generators process large datasets efficiently by generating values on demand.

---

### 4. Decorators
A **Decorator** adds extra functionality to a function without modifying its original code.

- Used the `@decorator` syntax.
- Learned function wrapping.
- Improved code reusability and maintainability.
- Explored applications such as logging, authentication, validation, and performance monitoring.

---

### 5. Lambda Functions

A **Lambda Function** is a small **anonymous (unnamed) function** created using the `lambda` keyword. It is commonly used to write short, single-expression functions without defining them using `def`, making the code more concise and readable.

```python
lambda arguments: expression
```

#### Applications

- Arithmetic operations
- Employee tax calculation
- Monthly subscription calculation
- Half-yearly subscription calculation
- Yearly subscription calculation

---

### 6. Functional Programming

**Functional Programming** is a programming paradigm that processes data by applying functions to iterables instead of relying on explicit loops. It helps write cleaner, more concise, and efficient code.

#### `map()`
Applies a specified function to every element of an iterable and returns a new iterable with the transformed values.

**Uses:**
- Performs data transformation.
- Reduces the need for explicit loops.
- Produces cleaner and more readable code.

#### `filter()`
 Selects only those elements from an iterable that satisfy a specified condition.

**Uses:**
- Filters data based on conditions.
- Simplifies conditional data extraction.
- Improves code readability.

#### `reduce()`
Repeatedly applies a function to the elements of an iterable until a single cumulative result is obtained. It is available in Python's `functools` module.

**Uses:**
- Calculates totals and cumulative values.
- Performs aggregation operations.
- Simplifies computations on collections.

---

### 7. Flight Dictionary Assignment

#### Objective

Applied functional programming concepts to process a list of flight dictionaries.

#### Tasks Performed

- Extracted flight details using `map()`.
- Filtered flight records using `filter()`.
- Calculated cumulative values using `reduce()`.
- Used lambda expressions throughout the solution.

---

### Practical Implementation

- Implemented iterators on lists, tuples, sets, strings, and dictionaries.
- Created generators using `yield`.
- Implemented decorators.
- Used lambda functions for tax and subscription calculations.
- Applied `map()`, `filter()`, and `reduce()` for data processing.
- Completed the Flight Dictionary Assignment.

---

## Key Takeaways

- Developed a strong understanding of Python's iteration mechanism using `iter()` and `next()`.
- Learned how generators enable memory-efficient programming through lazy evaluation with the `yield` keyword.
- Understood how decorators enhance function behavior while promoting code reusability and maintainability.
- Gained practical experience using lambda functions for concise and efficient function definitions.
- Applied functional programming concepts using `map()`, `filter()`, and `reduce()` for data transformation, filtering, and aggregation.
- Strengthened problem-solving skills by implementing these concepts in real-world scenarios, including tax calculation, subscription planning, and flight data processing.
- Improved my ability to write clean, optimized, and modular Python programs using advanced programming techniques.

---

## Reflection

Today's session significantly enhanced my understanding of advanced Python programming and its practical applications. Learning about **Iterators**, **Generators**, **Decorators**, **Lambda Functions**, and **Functional Programming** provided valuable insights into writing cleaner, more efficient, reusable, and memory-optimized code. The hands-on exercises, particularly the **Flight Dictionary Assignment**, reinforced these concepts by demonstrating how they can be applied to solve real-world data processing problems. Overall, this session strengthened my confidence in using advanced Python features and laid a solid foundation for building scalable and efficient Python applications.
