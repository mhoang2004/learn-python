
from csv import DictReader, DictWriter

def update_users(old_first_name, old_last_name, new_first_name, new_last_name):
    count = 0
    with open("users.csv") as file:
        csv_reader = DictReader(file)
        users = list(csv_reader)
        
    with open("users.csv", "w", newline='') as file:
        header = ["First Name", "Last Name"]
        csv_writer = DictWriter(file, fieldnames=header)
        csv_writer.writeheader()
        for user in users:
            print(user['First Name'], user['Last Name'])
            if user['First Name'] == old_first_name and user['Last Name'] == old_last_name:
                count += 1
                user['First Name'] = new_first_name
                user['Last Name'] = new_last_name
            
            csv_writer.writerow(user)
            
    return f'Users updated: {count}.'

        
        
    