x=input("Enter a number: ")
print(x)
count=0
n=int(x)
while(n!=0): 
    n //= 10
    count+=1
print(count)