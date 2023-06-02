# from csv import reader
# with open("fighters.csv") as f:
#     csv_reader = reader(f) #an iterator
#     we can next(csv_reader )
#     for row in csv_reader:
#         print(row)

# result:
# ['name', 'country', 'height']
# ['Alan', 'USA', '1.56']
# ['Bill', 'Japan', '1.99']
# ['Garen', 'UK', '1.59']

# from csv import DictReader
# with open("fighters.csv") as f:
#     csv_DictReader = DictReader(f)
#     print(csv_DictReader)
#     for row in csv_DictReader:
#         print(row)

# result:
# {'name': 'Alan', 'country': 'USA', 'height': '1.56'}
# {'name': 'Bill', 'country': 'Japan', 'height': '1.99'}
# {'name': 'Garen', 'country': 'UK', 'height': '1.59'}


# csv_reader = reader(f, delimiter = "|") if the csv file does not use ','

# ====== WRITTING FILE CSV =========
# from csv import writer
# with open("cats.csv", "w") as f:
#     csv_writer = writer(f) #an object
#     csv_writer.writerow(["Name", "Age"])
#     csv_writer.writerow(["Blue", 3])
#     csv_writer.writerow(["Kitty", 1])

# it create file and overwritten the content

#======EXAMPLE====
# from csv import reader, writer
# with open('fighters.csv') as file:
#     csv_reader = reader(file) #an iterator of string
#     fighters = [[s.upper() for s in row] for row in csv_reader]
#     #["Hoang", "Harry"] => ["HOANG", "HARRY"]

# with open('sreamming_fighters.csv', 'w') as file:
#     csv_writer = writer(file)
#     for fighter in fighters:
#         csv_writer.writerow(fighter)

#OTHER WAY
# with open('fighters.csv') as file:
#     csv_reader = reader(file)
#     with open('screaming_fighters.csv', 'w') as f:
#         csv_writer = writer(file)
#         for fighter in csv_reader:
#             csv_writer.writerow([s.upper() for s in fighter])

#======DictWriter====
from csv import writer, DictWriter

with open("dogs.csv", "w") as file:
    headers = ["Name", "Breed", "Age"]
    csv_writer = DictWriter(file, fieldnames=headers) #an object
    csv_writer.writeheader() #write headers at the head of the file
    csv_writer.writerow({
        "Name": "Garfield",
        "Breed": "Orange Tabby",
        "Age": 10
    })
    csv_writer.writerow({
        "Name": "Blue",
        "Breed": "Red Tabby",
        "Age": 11
    })


"""
việc gì mình cần làm tốt bây giờ nhỉ
    sắp tới thi cho tốt
    làm một lập trình viên giỏi
    mình đang thấy hơi lủng củng về cái lộ trình của mình học
    chắc là mình nên kiếm một cái project để tự làm roief apply vào công ty thực tập
    mình sợ là sau này mình chỉ mong tới cuối tuần rồi đi về trong mệt mỏi
    cả ngày phải code (sợ không?) không sợ lắm
    code là việc mình khá giỏi nên cx không lo lắm
    

"""












