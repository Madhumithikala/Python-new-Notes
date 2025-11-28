""" n=10
for i in range(n,0,-1):
    print(i) """


""" for i in range(5):
    print("*",end="") """


""" n=5
a=0
for i in range(n,0,-1):
    a +=1
    for j in range(1,i+1):
        print(a,end='')
    print() """


n=int(input("Enter rows:"))
skip=int(input("Enter skip value:"))
a=1
for i in range(n,0,-1):
    if skip !=a:
        for i in range(1,i+1):
            print(a,end='')
        print()
    a+=1 


n = int(input("Enter number: "))
for i in range(1, n+1): 
    for j in range(i):
        print("*", end="")
    print()

for i in range(n,0,-1): 
    for j in range(i):
        print("*", end="")
    print()

for i in range(n,0,-1): 
    for j in range(n):
        print("*", end="")
    print()
