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

#Q2.T1
num = input("Enter: ")
if num.isdigit():
    num = int(num)
    fact = 1
    for i in range(1,num+1):
        fact = fact*i
    print("Factorial: ")
    print(fact)
else:
    print("Enter a Valid Input !!")


#Q3.T1
Computers ={
  "Laptop1" : {"brand" : "DELL","OS" : "Windows"},
  "Laptop2" : {"brand" : "HP", "OS" : "Linux"},
  "Desktop" : {"brand" : "Apple","OS" : "Mac-OS"}
}
Brand=[Computers["Laptop1"]["brand"],Computers["Laptop2"]["brand"],Computers["Desktop"]["brand"]]
os=[Computers["Laptop1"]["OS"],computers["Laptop2"]["OS"],Computers["Desktop"]["OS"]]
print(Brand)
print(os)


#Leetcode.T2
class TWONUM(object):
    def twoSum(self, nums, target):
        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        return[]
