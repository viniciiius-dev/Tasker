# Tasker

Tasker is a lightweight CLI interface that allows users to manage tasks efficiently.  
Built as a solution for the [Task Tracker Challenge](https://roadmap.sh/backend/projects) from [roadmap.sh](https://roadmap.sh), it allows users to add, delete, modify and list tasks directly from their terminal.

# Features
 * **Add a task**: Add a new task with a description
 * **Update a task**: Modify the description of a task
 * **Marking a task as done or in progress:** Allows users to change the current condition of the task
 * **Delete a task**: Delete a task using its ID
 * **List tasks**: List tasks by status  
    * **Status**: Todo, in progress, done or all

# Installation

**1. Clone the repository**:  
```
git clone https://github.com/viniciiius-dev/Tasker.git
cd Tasker
```
**2. Run the main.py file through python**:
```
py main.py
```

# Usage
```
Welcome to Tasker. Type help to see available commands.

# Add new task
Tasker add Buy groceries
# Output: Task added successfully (ID: 1)

# Updating a task
Tasker update 1 Buy groceries and cook dinner
# Output: Task updated successfully (ID: 1)

# Deleting a task
Tasker delete 1
# Output: Task deleted successfully (ID: 1)

# Marking as in progress
Tasker mark_in_progress 1
# Output: Task marked as in progress (ID: 1)

# Marking as done
Tasker mark_done 1
# Output: Task marked as done (ID: 1)

# List all tasks
Tasker list

# Listing by status
Tasker list todo
Tasker list in_progress
Tasker list done
```
