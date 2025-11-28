#Arthematic operators

a=int(input("Enter Number:"))
b=int(input("Enter Number:"))

print(a+b) #20+30=50
print(a-b) #20-30=-10
print(a*b) #20*30=600
print(a/b) #20/30=0.6666666666
print(a//b) #20//30=0
print(a%b)  #20%30=20

#Logical Operator

print(a&b) #20&30=20
print(a|b) #20|30=30
print(not a) #not a=False
print(not b) #not b=False

#relational Operator

print(a<b) #20<30=True
print(a>b) #20>30=False
print(a<=b) #20<=30=True
print(a>=b) #20>=30=False
print(a==b) #20==30=False

#Special Operator
#Membership Operator

li=["madhu","gnanesh","Srinithi","chandu"]
print('madhu' not in li) #false 
print('Srinithi' in li) #True
print('sunil' in li) #False

#Identity operator

print(a is b) #20 is 30=False
print(a is not b) # 20 is not=True

# Assignment operator 
a=b
print(a) #20=30=30

a=10
a += 5 #15 (a=a+5)
print(a)

a-= 5
print(a) #10 (a=a-5)

a*= 5
print(a) #50 (a=a*5)

a/=5
print(a)  #10.0 

a//=5
print(a)  #2.0


a%=5
print(a) #2.0

#Bitwise Operator

x=5
x &= 3   #ans:1
print(x)  #bitwise
            #5->  8  4  2   1
            #     0  1   0  1
            # 3-> 0  0   1  1 
            #        0   0  1   

m=10      # 1010 
m |= 3    # 0011
print (m) # 1011
          # ans: 11

s=8       # 1000
s ^= 5    # 0101
print (s) # 1101 
          #ans:13

ab=15      #15/2/2
ab >>=2    #ans: 3
print(ab)  
 

bw=25
bw <<=2    # 25*2*2
print(bw)  # 100

         





