import yaml
import pprint

with open(r"C:\Users\Rudra\Desktop\Data Manipulation with Python\007_YML_Files\learn.yml", "r") as f:
    try:
        pprint.pprint(yaml.safe_load(f))
    except yaml.YAMLError as exc:
        print(exc)