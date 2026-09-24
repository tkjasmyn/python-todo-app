# To-Do CLI Application

A command-line task manager written in Python. Tasks are saved locally in a JSON file and persist between sessions.

## Features

- Add, edit, and delete tasks
- Mark tasks as done
- Assign priority and due dates
- Filter by priority or status
- Automatic save and load via JSON

## Requirements

Python 3.6+. No external libraries.

## Run

`python3 main.py`

## Menu

1. Add task

2. View tasks

3. Complete task

4. Edit task

5. Delete task

6. Filter tasks

7. Exit

## Task fields

| Field    | Notes                              |
| -------- | ---------------------------------- |
| id       | Auto-incremented                   |
| task     | Task name                          |
| status   | `Pending` or `Done`                |
| priority | `High`, `Medium`, `Low`, or `None` |
| due      | `YYYY-MM-DD` or `None`             |
| time     | Last modified time                 |
