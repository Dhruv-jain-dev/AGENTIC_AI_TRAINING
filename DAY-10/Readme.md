# Day 10 – Stack, Queue, OOP Modeling, and String Manipulation in Python

**Date:** 7 July 2026

---

## Overview

The tenth day of the Agentic AI Training focused on integrating **Data Structures**, **Object-Oriented Programming (OOP)**, and **Python String Manipulation** to build practical applications. We began by understanding the concepts of **Stack** and **Queue**, followed by designing a **Toll Plaza Management System** using OOP. The session also covered the implementation of a **Queue using a Circular Doubly Linked List**, establishing relationships between `Vehicle` and `FASTag` objects, and automating toll deduction. Towards the end, we explored Python string formatting techniques along with commonly used string operations and built-in methods for efficient text processing.

---

## Learning Highlights

### Topics Covered

* Stack and Queue
* Stack vs Queue
* Queue Operations
* Object-Oriented Modeling
* Vehicle and FASTag Relationship
* Circular Doubly Linked List
* Toll Plaza Management System
* Automatic FASTag Toll Deduction
* Python String Formatting
* String Manipulation and Built-in Methods

---

## 1. Stack and Queue

* Learned the concepts of **Stack** and **Queue**, two fundamental linear data structures.
* Understood that a **Stack** follows the **LIFO (Last In, First Out)** principle.
* Studied the primary stack operations:

  * Push
  * Pop
  * Peek
* Learned that a **Queue** follows the **FIFO (First In, First Out)** principle.
* Explored queue operations including:

  * Enqueue
  * Dequeue
  * Traversal
* Compared Stack and Queue based on their working principles and practical applications.
* Discussed their use in browser history, task scheduling, memory management, and process execution.

---

## 2. Toll Plaza Management System using OOP

* Designed a Toll Plaza Management System using Object-Oriented Programming.
* Created separate classes for **Vehicle** and **FASTag**.
* Learned how OOP principles help represent real-world entities in software.
* Applied encapsulation by organizing data and methods within classes.
* Understood how modular design improves code readability and reusability.

---

## 3. Vehicle and FASTag Association

* Learned how different objects interact with each other in an application.
* Established an association between Vehicle and FASTag objects.
* Assigned a unique FASTag to each vehicle.
* Retrieved FASTag information during toll processing.
* Understood how object relationships simplify real-world system modeling.

---

## 4. Queue using Circular Doubly Linked List

* Implemented the vehicle queue using a **Circular Doubly Linked List**.
* Learned how nodes maintain references to both previous and next nodes.
* Understood circular linking for continuous traversal.
* Studied efficient insertion and deletion operations without breaking the queue structure.
* Learned how dynamic memory allocation supports flexible queue management.

---

## 5. Queue Operations

Implemented and practiced the following queue operations:

* **Enqueue** – Added a vehicle to the rear of the queue.
* **Dequeue** – Removed the vehicle from the front after toll payment.
* **Traversal** – Displayed all vehicles waiting in the queue.
* **Display Queue** – Viewed the complete queue status.
* **Empty Queue Check** – Verified whether the queue contained any vehicles.

---

## 6. Automatic FASTag Toll Deduction

* Developed the logic for an automated FASTag toll deduction system.
* Identified the vehicle type before calculating the toll.
* Verified the available FASTag balance.
* Automatically deducted the toll amount from the account.
* Updated the remaining balance after each transaction.
* Handled insufficient balance situations using conditional validation.

---

## 7. Python String Formatting

Learned different methods of formatting strings to produce clean and readable output.

The techniques covered included:

* Formatted String Literals (**f-Strings**)
* `format()`
* `format_map()`

These methods help create dynamic strings while improving code readability.

---

## 8. Python String Operations

Explored several important concepts related to Python strings, including:

* String Immutability
* Indexing
* Negative Indexing
* Slicing
* Reverse Slicing
* Concatenation
* Splitting Strings
* Trimming Whitespaces

These concepts demonstrated how Python stores and manipulates textual data efficiently.

---

## 9. Built-in String Methods

Practiced commonly used string methods, including:

* `upper()`
* `lower()`
* `title()`
* `capitalize()`
* `strip()`
* `lstrip()`
* `rstrip()`
* `split()`
* `replace()`
* `find()`

These methods simplify everyday string manipulation tasks and improve code efficiency.

---

## Practical Implementation

During the practical session, I worked on implementing several concepts learned throughout the day.

The implementation included:

* Creating `Vehicle` and `FASTag` classes.
* Establishing relationships between objects.
* Simulating a Toll Plaza Management System.
* Implementing a Queue using a Circular Doubly Linked List.
* Performing enqueue, dequeue, and traversal operations.
* Developing an automatic FASTag toll deduction mechanism.
* Practicing Python string formatting and manipulation techniques through coding examples.

---

## Key Takeaways

* Developed a clear understanding of Stack and Queue data structures.
* Learned how Queue can be implemented efficiently using a Circular Doubly Linked List.
* Strengthened Object-Oriented Programming concepts through a real-world Toll Plaza Management System.
* Understood object associations using Vehicle and FASTag classes.
* Applied logical thinking to automate FASTag toll deduction.
* Improved Python string handling using formatting techniques and built-in methods.
* Enhanced problem-solving skills by integrating data structures, OOP, and string manipulation into practical applications.

---

## Reflection

Today's session combined multiple programming concepts into a single real-world application, making it one of the most practical sessions of the training so far. Building the Toll Plaza Management System helped me understand how data structures and object-oriented programming work together to solve real-world problems. Additionally, learning string formatting and manipulation techniques improved my ability to write cleaner, more readable, and efficient Python code. The session significantly strengthened both my theoretical understanding and hands-on programming skills.
