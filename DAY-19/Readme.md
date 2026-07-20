# Day 19 – Regular Expressions and Agentic AI Dashboard

**Date:** 20th July 2026

---
## Overview
The nineteenth day of the Agentic AI with Python Training Program focused on Regular Expressions (Regex) for efficient text processing and the enhancement of an AI-powered multi-page Streamlit application using OpenAI Function Calling with MongoDB Atlas. The session covered pattern matching techniques for searching, validating, and extracting text, followed by integrating conversational AI with cloud database operations to manage tasks through natural language. Overall, the session demonstrated how Regex, Streamlit, OpenAI Function Calling, and MongoDB Atlas can be combined to build intelligent, interactive, and scalable AI applications.

---

## Learning Highlights

### Topics Covered

* Regular Expressions (Regex)
* Pattern Matching using Python `re` Module
* Data Extraction and Validation
* Multi-Page Streamlit Applications
* Streamlit Navigation
* OpenAI Responses API
* OpenAI Function Calling
* JSON Tool Schemas
* MongoDB Atlas Integration
* AI-Powered Task Management

---

### 1. Regular Expressions (Regex)

The session introduced Python's **re** module, which provides a powerful mechanism for searching, matching, extracting, and validating text using predefined patterns.

The following Regex functions were explored:

| Function         | Purpose                                                        |
| ---------------- | -------------------------------------------------------------- |
| `re.search()`    | Finds the first occurrence of a matching pattern               |
| `re.findall()`   | Retrieves every occurrence that matches the pattern            |
| `re.fullmatch()` | Ensures that the complete string matches the specified pattern |

Regular Expressions simplify text-processing tasks, making programs more efficient, readable, and easier to maintain while reducing the need for complex string manipulation.

---

### 2. Data Extraction and Validation

Through practical demonstrations, we learned how Regular Expressions can efficiently identify and extract structured information from unstructured text.

Examples included:

* Indian Mobile Numbers
* Email Addresses
* Vehicle Registration Numbers
* PAN Card Numbers
* Numeric Values
* Alphanumeric Patterns

The trainer also demonstrated how multiple patterns can be merged into a single Regular Expression, allowing different types of information to be extracted simultaneously from the same input. These techniques are extensively used in web development, form validation, automation scripts, data preprocessing, and information extraction systems.

---

### 3. Multi-Page Streamlit Applications

The session introduced Streamlit's navigation framework for building well-structured multi-page applications.

The application was organized into multiple functional modules, including:

* Dashboard
* AI Chat Interface
* Patient Management

Several Streamlit features were utilized to build an interactive user interface, including:

* Metrics
* Columns
* Charts
* DataFrames
* Session State
* Cached Resources
* Sidebar Navigation
* Interactive Widgets
* Responsive Layout

The modular design allowed each page to manage a specific functionality independently while sharing application resources effectively. Streamlit's navigation features helped organize the project into logical sections, improving code maintainability, scalability, and the overall user experience.

---

### 4. AI-Powered Agentic Task Manager

The primary objective of the practical session was to enhance the existing Agentic AI application using the **OpenAI Responses API**.

Instead of relying on manually written conditional statements, the application enabled a **Large Language Model (LLM)** to interpret user requests and determine the appropriate backend function automatically.

The application supported the following features:

* Creating Tasks
* Viewing Tasks
* Updating Tasks
* Deleting Tasks

This implementation demonstrated how AI can intelligently understand user intent and automate backend operations through natural language interactions.

---

### 5. OpenAI Function Calling

A major concept introduced during the session was **OpenAI Function Calling**, which enables AI models to interact directly with backend functions.

JSON Tool Schemas were created by defining:

* Function Name
* Description
* Parameters
* Required Fields

#### Workflow

1. The user submits a request in natural language.
2. The OpenAI model analyzes the request.
3. The appropriate backend function is identified.
4. Required parameters are generated automatically.
5. The corresponding Python function is executed.
6. MongoDB Atlas performs the required database operation.
7. The processed result is returned through the Streamlit interface.

This workflow illustrated how AI can intelligently coordinate backend operations while maintaining a clean, modular, and scalable application architecture.

---

### 6. MongoDB Integration

MongoDB Atlas served as the cloud database responsible for storing and managing task information.

The reusable **DBHelper** class managed database operations such as:

* Document Insertion
* Data Retrieval
* Record Updates
* Record Deletion

Additional task information, including timestamps and task status, was generated automatically before each document was stored.

Separating database functionality into reusable helper methods improved maintainability, code organization, and overall software architecture.

---

### 7. Class Activity

During the hands-on session, we successfully built and tested a complete AI-powered Task Management application.

The application performed the following operations:

* Task Creation
* Task Listing
* Task Updating
* Task Deletion

using:

* Streamlit
* OpenAI Function Calling
* MongoDB Atlas

The project also incorporated advanced Streamlit features such as Session State, Chat Interface, Typing Animation, Cached Resources, and Multi-Page Navigation, resulting in a responsive and user-friendly application.

---

### Technologies Used

| Technology                 | Purpose                                 |
| -------------------------- | --------------------------------------- |
| Python                     | Core Programming Language               |
| Regular Expressions (`re`) | Pattern Matching & Validation           |
| Streamlit                  | Interactive Web Application Development |
| OpenAI Responses API       | Natural Language Understanding          |
| Function Calling           | Intelligent Backend Automation          |
| MongoDB Atlas              | Cloud Database                          |
| DBHelper                   | Database CRUD Operations                |
| JSON                       | Tool Schema Definition                  |

---

## Key Takeways

By the end of this session, I was able to:

* Understand the fundamentals of Python Regular Expressions.
* Perform searching, extraction, and validation using the `re` module.
* Extract meaningful information from textual data using Regex patterns.
* Validate structured inputs such as phone numbers, email addresses, PAN cards, and vehicle registration numbers.
* Design and develop a professional multi-page Streamlit application.
* Build interactive dashboards using various Streamlit components.
* Implement OpenAI Function Calling for AI-driven backend automation.
* Connect MongoDB Atlas through a reusable DBHelper class to perform CRUD operations.
* Understand the role of JSON Tool Schemas in enabling intelligent AI workflows.
* Develop an AI-powered Task Management application capable of responding to natural language commands.

---

## Reflection

Day 19 was one of the most insightful sessions of the Agentic AI with Python Training Program, combining Regular Expressions (Regex), OpenAI Function Calling, Streamlit, and MongoDB Atlas into a practical AI application. Learning Regex enhanced my ability to efficiently validate, search, and extract structured information from text, while OpenAI Function Calling demonstrated how Large Language Models can understand user requests and perform backend operations intelligently. Integrating Streamlit with MongoDB Atlas further strengthened my understanding of building interactive, scalable, and production-ready AI applications. Overall, the session provided valuable hands-on experience in developing intelligent software systems that seamlessly combine text processing, AI, cloud databases, and modern web technologies.
