#write your answer here
#Q1.T1
x=input("Enter a number: ")
print(x)
count=0
n=int(x)
while(n!=0): 
    n //= 10
    count+=1
print(count)


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


#Leetcode
class TWONUM(object):
    def twoSum(self, nums, target):
        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        return[]