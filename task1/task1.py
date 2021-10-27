from sys import argv


n = int(argv[1])
m = int(argv[2])

lstor = [x + 1 for x in range(n)]
index = lstor.copy()[:m]
mem = lstor * 2
path = []
point = 0
while True:
    path.append(index[0])
    point = index[-2]
    index = mem[point:point + m]
    if index[-1] == lstor[0]:
        path.append(index[0])
        break

for i in path:
    print(i, end='')



    
