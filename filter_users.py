import json

def filter_users_by_name(name):
    """Filters the user list by name and prints results"""
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["name"].lower() == name.lower()]

    for user in filtered_users:
        print(user)


def filter_users_by_age(age_to_search):
    """Filters the user list by age and prints results"""
    with open("users.json", "r") as file:
        users = json.load(file)
    filtered_users_by_age = [user for user in users if user["age"] == age_to_search]

    for user in filtered_users_by_age:
        print(user)


def filter_users_by_email(email_to_search):
    """Filters the user list by email address and prints results"""
    with open("users.json", "r") as file:
        users = json.load(file)
    filtered_users_by_email = [user for user in users if user["email"] == email_to_search]

    for user in filtered_users_by_email:
        print(user)


if __name__ == "__main__":
    filter_option = input("What would you like to filter by? (Currently, only 'name' is supported): ").strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search)
    elif filter_option == "age":
        age_to_search = input("Enter an age to filter users: ").strip()
        filter_users_by_age(age_to_search)
    elif filter_option == "email":
        email_to_search = input("Enter an email to filter users: ").strip()
        filter_users_by_email(email_to_search)
    else:
        print("Filtering by that option is not yet supported.")
