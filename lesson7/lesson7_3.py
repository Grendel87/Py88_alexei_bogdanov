dict = {
    123456: ("Bil", 24, "10-12-14"),
    234567: ("Bob", 25, "12-14-16"),
    345678: ("Nik", 31, "14-16-18"),
    456789: ("Amanda", 26, "16-18-20"),
    567890: ("Mary", 27, "18-20-22"),
    987654: ("Sam", 32, "20-22-24")
}

import json

with open("data_file.json", "w") as write_file:
    json.dump(dict, write_file, indent=4)

import csv

with open("data_file.json", "r") as f_json:
    data = json.load(f_json)
with open("some.csv", 'w') as f_csv:
    writer = csv.writer(f_csv, delimiter=",")
    headers = ['             '] + [f'person {i}' for i in range(1, len(data) + 1)]
    writer.writerow(headers)
    _id = ['id           ']
    names = ['name         ']
    ages = ['age          ']
    phone = ['Phone Number ']
    for k, (username, age, numeros) in data.items():
        _id.append(k)
        names.append(username)
        ages.append(age)
        phone.append(numeros)
    headers2 = [_id, names, ages]
    writer.writerows(headers2)
    writer.writerow(phone)
