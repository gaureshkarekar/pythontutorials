arr = (i for i in range(100) if i%2==0)

for i in range(8):
    print(next(arr))

