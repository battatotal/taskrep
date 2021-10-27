from sys import argv

with open(argv[1]) as file:
    argls = [int(x) for x in file.readlines()]


res = sorted(argls)

m = res[len(res) // 2]

count = 0

for i in res:
    while i != m:
        if i == m:
            continue
        if i < m: i += 1
        if i > m: i -= 1
        count += 1

print(count)



