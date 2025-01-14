import requests

# Replace these with your Habitica UID and API Token
UID = "bf285827-bd8b-4bd7-a3dc-bd06e1fc9b8f"
API_KEY = "3332bcd4-8330-48ab-a7bd-f0fc2e441f29"

# gets habitica TASKS and returns them as a list
def get_all_habitica_tasks(uid, api_key):
    url = "https://habitica.com/api/v3/tasks/user"
    headers = {
        "x-client": f"{uid}-HabitJournal",
        "x-api-user": uid,
        "x-api-key": api_key
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        tasks = response.json()["data"]
        return tasks
    except requests.exceptions.RequestException as e:
        print(f"Error retrieving tasks: {e}")
        return []

# Retrieves user's Habitica dailies
# returns a list of habit objects
def get_habitica_habits(uid, api_key):
    url = "https://habitica.com/api/v3/tasks/user"
    headers = {
        "x-client": f"{uid}-HabitJournal",
        "x-api-user": uid,
        "x-api-key": api_key
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        tasks = response.json()["data"]
        
        # Filter for only habits, modify for other types
        habits = [task for task in tasks if task["type"] == "habit"]
        return habits
    except requests.exceptions.RequestException as e:
        print(f"Error retrieving tasks: {e}")
        return []

def get_habitica_dailies(uid, api_key):
    url = "https://habitica.com/api/v3/tasks/user"
    # Request headers for courtesy
    headers = {
        "x-client": f"{uid}-HabitJournal",
        "x-api-user": uid,
        "x-api-key": api_key
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        tasks = response.json()["data"]
        
        # Filter for only dailies, modify for other types
        dailies = [task for task in tasks if task["type"] == "daily"]
        return dailies
    except requests.exceptions.RequestException as e:
        print(f"Error retrieving tasks: {e}")
        return []
    
def get_task_id_name(tasks_list, task_name):
    for task in tasks_list:
        if task["text"] == task_name:
            return task["id"]
    print(f"Task {task_name} not found")
    return "failed ID retrieval"

def get_task_id_index(tasks_list, task_index):
    if task_index < len(tasks_list):
        return tasks_list[task_index]["id"]
    print(f"Task index {task_index} out of range")
    return "failed ID retrieval"

def complete_habitica_task_ID(uid, api_key, task_id):
    url = f"https://habitica.com/api/v3/tasks/{task_id}/score/up"
    headers = {
        "x-client": f"{uid}-HabitJournal",
        "x-api-user": uid,
        "x-api-key": api_key
    }

    try:
        response = requests.post(url, headers=headers)
        response.raise_for_status()
        return True
    except requests.exceptions.RequestException as e:
        print(f"Error completing task: {e}")
        return

def display_tasks(tasks):
    if not tasks:
        print("No tasks found? Add some! :0")
        return

    print("Tasks:")
    i = 0
    for task in tasks:
        title = task["text"]
        # check for due date
        if "date" in task and task["date"] is not None:
            date = task["date"]
            title += f" (Due: {date})"
        print(f"{i} - {title}")

# prints daily tasks and their completion status
def display_dailies(dailies):
    if not dailies:
        print("No dailies found? Add some! :0")
        return

    print("Foes To Conquer:")
    i = 0
    for daily in dailies:
        title = daily["text"]
        completed = daily["completed"]
        status = "✅ Completed! ^u^" if completed else "❌ Not Completed. >:("
        print(f"{i} - {title}: {status}")
        i+=1

def display_habits(habits):
    if not habits:
        print("No habits found? Add some! :0")
        return

    print("Habits:")
    i = 0
    for habit in habits:
        title = habit["text"]
        print(f"{i} - {title}")
        i+=1

if __name__ == "__main__":
    tasks = get_habitica_habits(UID, API_KEY)
    display_habits(tasks)


    

    # Complete a daily task
