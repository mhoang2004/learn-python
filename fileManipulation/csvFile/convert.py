from csv import DictReader, DictWriter

def cm_to_inch(cm):
    return float(cm) * 0.393701

with open("fighters.csv") as file:
    csv_reader = DictReader(file)
    fighters = list(csv_reader)
    # print(fighters)

with open("inches_fighters.csv", "w") as file:
    headers = ("Name", "Country", "Height")
    csv_writer = DictWriter(file, fieldnames=headers)
    csv_writer.writeheader()
    for fighter in fighters:
        csv_writer.writerow({
            "Name": fighter['name'],
            "Country": fighter['country'],
            "Height": cm_to_inch(fighter['height'])
        })
