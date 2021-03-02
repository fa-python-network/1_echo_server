import yaml
from typing import Dict

def get_data() -> Dict:
    with open("./users.yml", "r") as stream:
        return yaml.safe_load(stream)