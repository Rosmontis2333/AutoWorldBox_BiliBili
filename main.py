
import json
from misaka import MisakaII

if __name__ == '__main__':

    with open("config.json") as json_file:
        config = json.load(json_file)
        MisakaII(config)
