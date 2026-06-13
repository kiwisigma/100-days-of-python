from datetime import datetime
def get_time_of_day():
    hour = datetime.now().hour
    if hour < 12:
        return "morning"
    elif hour < 17:
        return "afternoon"
    else:
        return "evening"

def full_greeting(name, time_of_day):
    print(f"Hello {name}!\nIt is {time_of_day}")

full_greeting("Angela", get_time_of_day())