import csv


def find_user(first_name, last_name):
    with open('users.csv') as file:
        users = csv.reader(file)
        for (index, user) in enumerate(users):
            first_name_match = user[0] == first_name
            last_name_match = user[1] == last_name
            if first_name_match and last_name_match:
                return index
        return f"{first_name} {last_name} not found."
