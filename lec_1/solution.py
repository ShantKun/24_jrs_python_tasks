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