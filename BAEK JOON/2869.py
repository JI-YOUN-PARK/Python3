A, B, V = map(int, input().split())
go = (V-B)/(A-B)
if (go == int(go)):
    print(int(go))
else:
    print(int(go) + 1)
