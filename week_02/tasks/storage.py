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


def find_key(storage_path, *args):
    items = []
    with open(storage_path, 'r') as f:
        text = (f.read().strip()).split(",\n")
        for x in text:
            items.append(x.split(':'))
    storage = {k:v for k,v in items}
    for key in args:
        return storage.get(key)


parser = argparse.ArgumentParser()
parser.add_argument("keys")
parser.add_argument("-k", "--key", action="store_true",
                    help="returns value of key or None")
args = parser.parse_args()


if __name__ == "__main__":
    print(find_key(storage_path, args.keys))
