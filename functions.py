from json import JSONDecodeError
import json
from inspect import stack


def modify_json(new_json):
    with open("task_data.json", "w") as write_file:
        json.dump(new_json, write_file, indent=4)

def json_to_list():
    try:
        with open("task_data.json", "r") as read_file:
            list_json = json.load(read_file)
            return list_json
    except FileNotFoundError, JSONDecodeError:
        caller_frame = stack()[1]
        caller_name = caller_frame.function
        if not caller_name in ["check_highest_id", "get_list_of_ids"]:
            print("""Couldn't find any task. To create one, use the command add and the description of the task.
Example: add Wash dishes.""")
            return None

def add_task_to_file(task_info):
    with open("task_data.json", "r") as read_file:
        list_json = json.load(read_file)
        list_json.append(task_info)
    with open("task_data.json", "w") as write_file:
        json.dump(list_json, write_file, indent=4)

def create_json_file():
    ## Creates the file and updates it to have the highest_id data in it
    task_id = 1
    list_json = [{"highest_id": task_id}]
    with open("task_data.json", mode="w") as write_file:
        json.dump(list_json, write_file)

def check_highest_id():
    tasks = json_to_list()
    try:
        if len(tasks) == 1:
            return 0
        else:
            highest_idvav = list(tasks[-1].values())[0]
    except TypeError:
        return 0
    except FileNotFoundError:
        return 0
    except JSONDecodeError:
        return 0

    return highest_idvav


def update_highest_id(action):
    try:
        # Uses the function check_highest_id to get current highest id, add 1 to it
        if action == "add":
            highest_id = check_highest_id()
            highest_id += 1
        elif action == "remove":
            highest_id = check_highest_id()


        # Reads the file task_data.json, Returns as list, updates the dictionary {"highest_id": int} to
        # {"highest_id": highest_id} (it was added or subtracted 1 to the variable highest_id before)

        with open("task_data.json", "r") as read_file:
            list = json.load(read_file)
            list[0] = {"highest_id": highest_id}

        with open("task_data.json", "w") as write_file:
            json.dump(list, write_file, indent=4)
    except FileNotFoundError, JSONDecodeError:
        pass
    return highest_id

def get_list_of_ids():
    json_list = json_to_list()
    list_ids = [tarefa.get("id") for tarefa in json_list[1:]]
    return list_ids