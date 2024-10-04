
# LMS (List Management System)

## Overview

I developed a **List Management System (LMS)** in Python to manage tasks effectively through a **Todo** list and a **Complete** list. The system allows users to:
- Add tasks to a Todo list.
- Mark tasks as complete, which moves them from the Todo list to the Complete list.
- Remove tasks from either list.
- Display the current Todo and Completed tasks in a tabular format.

After building the core functionality, I used **Test-Driven Development (TDD)** to ensure that each feature works as expected. This involved writing test cases for various functionalities, including edge cases and boundary value testing.

## Features

### Task Management
- **Add Tasks**: Add a task to the Todo list, which automatically generates a unique 6-character alphanumeric ID for each task.
- **Complete Tasks**: Mark tasks as complete, which transfers them from the Todo list to the Complete list with the completion timestamp.
- **Remove Tasks**: Delete tasks from either the Todo or the Complete list.
- **Display Tasks**: View the tasks in both the Todo and Complete lists in a formatted table.

Each task has the following attributes:
- **ID**: A unique identifier generated for each task.
- **Task**: The name of the task.
- **Date Added**: The date the task was added to the Todo list.
- **Completed At**: The date the task was marked as completed (for tasks in the Complete list).

## My Approach

I structured the **LMS** around two main lists:
1. **Todo List**: Stores tasks that need to be completed.
2. **Complete List**: Stores tasks that have been completed.

The system allows users to move tasks between these lists, and it provides methods for adding, completing, removing, and displaying tasks. I also used the `tabulate` module to display tasks in a clear table format.

### Why I Chose TDD

Using **Test-Driven Development (TDD)** allowed me to focus on ensuring that my code worked as intended before implementation. By writing tests first and then building the system to pass those tests, I was able to handle errors and edge cases early in development. This made the system more reliable and saved me time in the long run, as I could detect and fix problems as soon as they appeared.

## Test-Driven Development (TDD)

### Testing Process

The tests cover the system’s main functionalities:
1. **Add Tasks**:
   - I tested adding tasks with valid inputs, such as a typical task name.
   - I also tested boundary values, including tasks with empty names, single-character names, and extremely long names (up to 1000 characters).

2. **Complete Tasks**:
   - I tested marking tasks as complete and moving them to the Complete list.
   - I also tested case insensitivity to ensure that a task can be marked complete regardless of how the case was entered (e.g., "Finish biology project" vs "FINISH BIOLOGY PROJECT").

3. **Remove Tasks**:
   - I wrote tests to ensure that tasks could be removed from both the Todo and Complete lists.
   - I also tested the behavior when trying to remove a non-existent task to ensure proper error handling.

4. **Display Tasks**:
   - I tested the display function to ensure tasks are shown in a readable table format.
   - I verified that the system properly handles both empty and non-empty lists when displaying tasks.

### Boundary Value Testing

In addition to regular test cases, I performed boundary value analysis to check how the system behaves at its limits:
- **Minimum Task Length**: I tested adding tasks with only a single character.
- **Empty Task**: I tested adding an empty task to see how the system would handle it.
- **Maximum Task Length**: I tested adding a task with 1000 characters to ensure the system handles large inputs.
- **Case Insensitivity**: I ensured that tasks could be completed regardless of whether the case matched exactly.

### Running the Tests

I used Python's `unittest` framework to write and run the tests. To run the tests yourself, use the following command:

```bash
python -m unittest <test_file_name>.py
```

This command will execute all the test cases, and the results will be displayed in the terminal. The tests ensure that the core functionality and boundary conditions are handled correctly by the system.

## Conclusion

By using TDD, I was able to build a reliable and robust **List Management System (LMS)** that can handle a wide variety of tasks. The system successfully adds, completes, removes, and displays tasks, all while managing edge cases like empty or excessively long task names. I’m confident that this system will manage tasks efficiently, and the tests provide assurance that it behaves as expected in both typical and boundary cases.

Feel free to use the LMS to manage your tasks, and you can rely on the system to handle them efficiently!

