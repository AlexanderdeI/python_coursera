import argparse
import json
import os
import tempfile


storage_path = os.path.join(tempfile.gettempdir(), 'storage_data')
json_file = open("storage.json")
storage = json.load(json_file)

with open(storage_path, 'w') as f:
    for key, value in storage.items():
        f.write("{}: {},\n".format(key, value))


def find_key(storage_path, keys_list):
    items = []
    with open(storage_path, 'r') as f:
        text = (f.read().strip()).split(",\n")
        for x in text:
            items.append(x.split(':'))
    storage = {k:v for k,v in items}
    result = []
    for key in keys_list:
        prepared_key = key.strip(' ,.!').lower()
        result.append(storage.get(prepared_key))
    return ", ".join(result)

parser = argparse.ArgumentParser()
parser.add_argument("keys",  nargs='*')
parser.add_argument("-k", "--key", action="store_true",
                    help="returns value of key or None",)
args = parser.parse_args()

if __name__ == "__main__":
    print(find_key(storage_path, args.keys))
