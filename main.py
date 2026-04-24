import cmd

from datetime import datetime
from logging import exception
from functions import *

class myCLI(cmd.Cmd):
    prompt = ('task-cli ' )
    intro = 'Welcome to Tasker. Type "help" to see available commands.'


    def do_add(self, line):
        # check description of the task
        if line == '':
            print("""You need to input the description of the task after the add command.
Example: """)
            return
        print(line)
        """add new task"""
        global task_info
        global highest_id
        task_desc = line
        task_id = update_highest_id("add")
        task_info = {
            "id": task_id,
            "desc": task_desc,
            "status": "todo",
            "createdAt": datetime.now().strftime("%d %b %Y, %I:%M%p"),
            "updatedAt": datetime.now().strftime("%d %b %Y, %I:%M%p")
        }

        try:
            json_file = open("task_data.json")
            add_task_to_file(task_info)

        except FileNotFoundError, JSONDecodeError:
            create_json_file()
            add_task_to_file(task_info)

        print(f"Task added successfully (ID: {task_id})")

    def do_update(self, line):
        try:
            id = int(line[0:line.index(" ")])
            new_task_desc = line[line.index(" ") + 1:]
        except ValueError:
            print("""You need to input the Task ID and the new description of the task
Example: update 6 "Wash dishes". 
To see tasks and IDs, type list.""")
            return None

        tasks = json_to_list()
        if tasks == None or tasks == []:
            return None
        list_ids = []

        try:
            for index in range(1, len(tasks)):
                list_ids.append(list(tasks[index].values())[0])
        except TypeError:
            print("""Couldn't find any tasks. To create one, use the command add and the task name.           
Example: add Wash dishes.""")
            return None
        index = list_ids.index(id) + 1
        if id in list_ids:
            tasks[index]["desc"] = new_task_desc
            tasks[index]["updatedAt"] = datetime.now().strftime("%d %b %Y, %I:%M%p")
            modify_json(tasks)
        else:
            print("The ID doesn't match a task. To see IDs and tasks, type list.")


    def do_delete(self, line):
        # Deletes the task using ID
        try:
            id = int(line)
        except ValueError:
            print("""To delete a task, you need to place an ID after the command
Example: delete 1
To see tasks and IDs, type list. """)
            return None

        # If the file is empty or there is no file, the function returns None and tells the user it didn't find any tasks.
        # Asks the user to add tasks through the add command.
        tasks = json_to_list()
        if tasks == None:
            return None

        list_ids = []

        # Creates a list of all the IDs
        try:
            for index in range(1, len(tasks)):
                list_ids.append(list(tasks[index].values())[0])
        except TypeError:
            print("""Couldn't find any tasks. To create one, use the command add and the task name.
        Example: add Wash dishes.""")
            return None

        # Verify if the ID is in the list, if True: removes the task that matches the ID from the tasks variable  (tasks list taken from the JSON file)
        # and updates the JSON with the updated task list  (tasks variable)
        if id in list_ids:
            tasks.pop(list_ids.index(id) + 1)
            modify_json(tasks)
        else:
            print("The ID doesn't match a task. To see tasks and IDs, type list.")

        # If the removed ID is the highest one, updates the highest ID in the JSON file
        if id == list_ids[-1]:
            update_highest_id("remove")




    # Mark task in progress or done
    def do_mark_in_progress(self, line):
        tasks = json_to_list()
        try:
            id = int(line)
        except ValueError:
            print("""To mark a task as in progress, you need to put a ID after the command.
Example: mark_in_progress 1
To see tasks and IDs, type list. """)
            return None
        list_ids = []

        for tarefa in range(1, len(tasks)):
            list_ids.append(list(tasks[tarefa].values())[0])

        if id in list_ids:
            index = list_ids.index(id) + 1
            tasks[index]["status"] = "in_progress"
            tasks[index]["updatedAt"] =  datetime.now().strftime("%d %b %Y, %I:%M%p")
            modify_json(tasks)
        else:
            print("The ID doesn't match a task. To show tasks and IDs, type list.")
            return None

    def do_mark_done(self, line):
        tasks = json_to_list()
        try:
            id = int(line)
        except ValueError:
            print("""To mark a task as completed, you need to place a ID after the command.
        Example: mark_done 1
        To see tasks and IDs, type list. """)
            return None
        list_ids = []

        for task in range(1, len(tasks)):
            list_ids.append(list(tasks[task].values())[0])

        if id in list_ids:
            index = list_ids.index(id) + 1
            tasks[index]["status"] = "done"
            tasks[index]["updatedAt"] =  datetime.now().strftime("%d %b %Y, %I:%M%p")
            modify_json(tasks)
        else:
            print("The ID doesn't match a task. To show tasks and IDs, type list.")
            return None

    # Show list of tasks
    def do_list(self, line):
        status = line
        tasks = json_to_list()
        if tasks == None:
            return None

        match line:
            case "todo":
                for index in range(1, len(tasks)):
                    if tasks[index]["status"] == "todo":
                        print(f"""TASK ID: {tasks[index]["id"]}
DESCRIPTION: {tasks[index]["desc"]}
STATUS: {tasks[index]["status"]}\n""")

            case "done":
                for index in range(1, len(tasks)):
                    if tasks[index]["status"] == "completado":
                        print(f"""TASK ID: {tasks[index]["id"]}
DESCRIPTION: {tasks[index]["desc"]}
STATUS: {tasks[index]["status"]}\n""")

            case "in_progress":
                for index in range(1, len(tasks)):
                    if tasks[index]["status"] == "em_progresso":
                        print(f"""TASK ID: {tasks[index]["id"]}
DESCRIPTION: {tasks[index]["desc"]}
STATUS: {tasks[index]["status"]}\n""")
            case "":
                for index in range(1, len(tasks)):
                    print(f"""TASK ID: {tasks[index]["id"]}
DESCRIPTION: {tasks[index]["desc"]}
STATUS: {tasks[index]["status"]}\n""")

            case _:
                print("""To see all tasks type list
To see done tasks, in progress, or todo, use list done, list in_progress or list todo""")


    pass


if __name__ == '__main__':
    myCLI().cmdloop()