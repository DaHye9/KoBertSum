import json
import sys

with open(sys.argv[1], 'r', encoding='utf-8') as j:
    with open(sys.argv[1]+'l', 'w', encoding='utf-8') as out:
#        json_list = json.load(j)
        for entry in j:
            json.dump(entry, out)
            out.write('\n')


