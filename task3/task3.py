from sys import argv
import pickle
import json

t = argv[1]
v = argv[2]

with open(t, encoding="UTF-8") as file:
    te = file.read()

with open(v, encoding="UTF-8") as file:
    va = file.read()

tests = json.loads(te)
values = json.loads(va)

tes = tests.values()
vals = values.values()
vnorm = []
for i in vals:
    for j in i:
        vnorm.append(list(j.values()))

vnorm = dict(vnorm)

def shift(dict):
    if list(dict.values())[0] in vnorm:
        dict['value'] = vnorm[dict['id']]
    if dict.get('values'):
        for i in range(len(dict.get('values'))):
            shift(dict.get('values')[i])

for i in tes:
    for j in i:
        shift(j)


with open('report.json', 'w') as f:
    json.dump(tests, f)





