# n=5
# a=0
# for i in range(n,0,-1):
#     a +=1
#     for j in range(1,i+1):
#         print(a,end='')
#     print() 


# n=int(input("Enter rows:"))
# skip=int(input("Enter skip value:"))
# a=1
# for i in range(n,0,-1):
#     if skip !=a:
#         for i in range(1,i+1):
#             print(a,end='')
#         print()
#     a+=1 


# n = int(input("Enter number: "))
# for i in range(1, n+1): 
#     for j in range(i):
#         print("*", end="")
#     print()

#  for i in range(n,0,-1): 
#     for j in range(i):
#         print("*", end="")
#     print()

# for i in range(n,0,-1): 
#     for j in range(n):
#         print("*", end="")
#     print() 



n=int(input("Enter number of rows:"))
for i in range(n,0,-1):
    print("")
    for j in range(i):
        print(" *", i,end='')
    print()
# output:
# Enter number of rows:5

#  * 5 * 5 * 5 * 5 * 5

#  * 4 * 4 * 4 * 4

#  * 3 * 3 * 3

#  * 2 * 2

#  * 1