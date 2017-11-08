import argparse, json, os, tempfile


storage_path = os.path.join(tempfile.gettempdir(), 'storage_data')
json_file = open("storage.json")
storage = json.load(json_file)

with open(storage_path, 'w') as f:
    for key, value in storage.items():
        f.write("{}: {},\n".format(key, value))

parser = argparse.ArgumentParser()
parser.add_argument("key")
parser.add_argument("val")
