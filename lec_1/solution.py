#write your answer here
#Q3.T1
Computers ={
  "Laptop1" : {"brand" : "DELL","OS" : "Windows"},
  "Laptop2" : {"brand" : "HP", "OS" : "Linux"},
  "Desktop" : {"brand" : "Apple","OS" : "Mac-OS"}
}
Brand=[]
os=[]
for laptop, key in Computers.items():
   Brand.append(key["brand"])
   os.append(key["OS"])
   print(Brand)
   print(os)

#Q1.T1
x=input("Enter a number: ")
print(x)
count=0
n=int(x)
while(n!=0): 
    n //= 10
    count+=1
print(count)