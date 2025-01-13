import requests

# Replace these with your Habitica UID and API Token
UID = "bf285827-bd8b-4bd7-a3dc-bd06e1fc9b8f"
API_KEY = "3332bcd4-8330-48ab-a7bd-f0fc2e441f29"

# Retrieves user's Habitica dailies
# returns a list of daily tasks objects
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

# prints daily tasks and their completion status
def display_dailies(dailies):
    if not dailies:
        print("No dailies found? Add some! :0")
        return

    print("Foes To Conquer:")
    for daily in dailies:
        title = daily["text"]
        completed = daily["completed"]
        status = "✅ Completed! ^u^" if completed else "❌ Not Completed. >:("
        print(f"- {title}: {status}")

if __name__ == "__main__":
    dailies = get_habitica_dailies(UID, API_KEY)
    display_dailies(dailies)
