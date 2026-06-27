# Day 3 – Hashing, Memory Management & Python Data Structures

**Date:** 27 June 2026

## Overview

The third day of the Agentic AI Training focused on understanding how data is stored and managed in memory. We learned the fundamentals of hashing, explored how single-valued and multi-valued data are stored in Stack and Heap memory, discussed the challenges associated with memory allocation, compared Python's List and Set data structures, and received practical assignments to strengthen these concepts.

---

## Topics Covered

### 1. Introduction to Hashing

* Learned the basic concept of **Hashing**.
* Understood how hashing maps data to unique memory locations using hash functions.
* Discussed how hashing enables faster data retrieval and efficient searching.

### 2. Storage of Data in Memory

* Explored how **Single-Valued Data** and **Multi-Valued Data** are stored in memory.
* Understood the role of:

  * **Stack Memory** for storing local variables and function execution data.
  * **Heap Memory** for storing dynamically allocated objects and complex data structures.
* Learned how Python manages different types of data internally.

### 3. Memory Allocation Challenges

* Discussed the problems that can arise during memory allocation and variable assignment.
* Learned how improper memory management may lead to inefficiencies.
* Understood how Python manages memory dynamically to overcome these challenges.

### 4. Difference Between List and Set

Learned the key differences between Python's **List** and **Set** data structures.

| List                                  | Set                                    |
| ------------------------------------- | -------------------------------------- |
| Maintains insertion order             | Does not guarantee order               |
| Allows duplicate elements             | Stores only unique elements            |
| Indexed and ordered                   | Unindexed                              |
| Mutable                               | Mutable                                |
| Suitable when duplicates are required | Suitable when unique values are needed |

---

## Assignments

### Assignment 1: Flight Information Management

Created a **List** to store details of multiple flights. Each flight record included relevant information such as:

* Flight Number
* Airline Name
* Source
* Destination
* Departure Time
* Arrival Time
* Ticket Price

This assignment helped in understanding how multi-valued data can be organized using Python Lists.

### Assignment 2: Cinema Seat Booking System

Created a **Dictionary containing Lists of Dictionaries** to represent the seat availability of a cinema hall during movie ticket booking.

The structure stored information such as:

* Screen or Hall
* Seat Number
* Seat Type
* Booking Status (Available/Booked)

This assignment demonstrated how nested data structures can be used to model real-world applications efficiently.

---

## Key Takeaways

* Gained a foundational understanding of hashing and its applications.
* Learned how different types of data are stored in Stack and Heap memory.
* Understood common memory allocation challenges and how Python handles them.
* Differentiated between Python Lists and Sets based on their characteristics and use cases.
* Applied the concepts by designing real-world data structures for a flight management system and a cinema seat booking system.

---

## Reflection

Today's session focused on practical aspects of data organization and memory management in Python. Learning about hashing and memory allocation strengthened my understanding of Python's internal working, while the assignments provided hands-on experience in designing structured data models for real-world scenarios. These concepts will be valuable when developing scalable Agentic AI applications.
