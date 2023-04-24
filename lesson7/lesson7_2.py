dict = {
    123456: ("Bil", 24),
    234567: ("Bob", 25),
    345678: ("Nik", 31),
    456789: ("Amanda", 26),
    567890: ("Mary", 27),
    987654: ("Sam", 32)
}

import json

with open("data_file.json", "w") as write_file:
    json.dump(dict, write_file)
