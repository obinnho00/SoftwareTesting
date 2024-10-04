
# Library Management System

## Overview
In this project, I created a **Library Management System** using Python to simulate adding, searching, and removing books from a structured database. The system organizes books by **category** and **subfield**, allowing users to manage their library collection programmatically.

After building the core functionality, I applied **Test-Driven Development (TDD)** to ensure the code works correctly. This process involved writing unit tests for the system's different components, including edge cases, boundary value analysis, and equivalence partitioning.

## Features of the System
The Library Management System includes the following key features:
1. **Add Books**: Add a book to a specific category and subfield.
2. **Search for Books**: Search for a book by name and return its category and subfield if found.
3. **Remove Books**: Remove a book from the system by its name, ensuring it is deleted from the relevant subfield and category.

Each book in the system has attributes like:
- `Book Name`
- `Author`
- `ID`
- `Date Added`

## Approach
### Code Implementation
I structured the code around two main classes:
1. **DATABASE**: This class initializes the structure of the library. It contains predefined categories and subfields, which act as placeholders for the books.
   
2. **LibraryManagementSystem**: This class contains all the core functionalities of the system, such as adding, searching, and removing books. The methods in this class interact with the `DATABASE` class to manipulate the collection of books.

### Logging
I implemented **logging** to track various actions performed by the user, such as adding, searching, and removing books. Instead of using `print` statements, I relied on the `logging` module to log information and errors. This logging is crucial for monitoring the system's behavior during testing.

### Test-Driven Development (TDD)
My approach was heavily focused on TDD. I wrote unit tests before implementing some functionality and refined the system based on test outcomes. I covered the following scenarios in my tests:

1. **Valid Inputs**:
   - Adding a valid book to the library.
   - Searching for a book that exists.
   - Removing a book that exists.

2. **Invalid Inputs and Edge Cases**:
   - Attempting to add a book to a nonexistent category or subfield.
   - Adding books with empty names or authors.
   - Searching for a nonexistent book.
   - Removing a book that doesn’t exist.
   - Testing extremely long and short book names.
   
By using this approach, I ensured that the system could handle a wide range of inputs, both valid and invalid, and responded correctly.

### Testing Strategy
The testing was conducted using Python's built-in `unittest` framework. Here’s what I focused on during testing:

- **Equivalence Partitioning**: I divided the input data into valid and invalid partitions. For example, valid categories like `"Fiction"` and `"Non-Fiction"` versus invalid ones like `"Sci-Fi"`. Similarly, I tested valid book names against empty or overly long names.
  
- **Boundary Value Analysis**: I tested boundary cases, such as adding books with very short names (e.g., 1 character) and very long names (e.g., 1000 characters).

- **Assertions and Logging**: For each test, I checked whether the system logged the expected messages using `assertLogs()`. This approach ensured that all actions were properly logged, making the system more robust and easier to debug.

### Tests Conducted
I wrote test cases for the following actions:
1. **Adding Books**: 
   - Testing valid inputs and valid categories/subfields.
   - Handling invalid categories, subfields, and empty book names.
   - Adding extremely long and short book names.

2. **Searching for Books**: 
   - Successfully finding a book.
   - Handling cases where the book does not exist.
   - Testing with invalid categories and empty book names.

3. **Removing Books**:
   - Successfully removing a book.
   - Handling cases where the book does not exist.
   - Testing with invalid categories and empty book names.

## How to Run the Tests
To run the tests, make sure you have Python installed. You can execute the tests using Python's `unittest` module. Simply navigate to the project directory and run:

```bash
python -m unittest <test_file_name>.py
```

This will execute all test cases and display the results in the terminal. The logging messages will also be captured during test execution, verifying that the system is logging the correct information at each step.

## Conclusion
This Library Management System showcases the power of TDD in ensuring code reliability. By writing tests first and following a structured approach to input validation and logging, I was able to build a system that can handle various edge cases and boundary values while maintaining accurate logging. The tests provide confidence that the system behaves as expected in both normal and abnormal conditions.
