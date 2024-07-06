##Q1.
def getlistlol():
  l1=[]
  n=int(input())
  print("Enter The Numbers")
  while n != 0:
    a = int(input())
    if(a % 2 == 0):
      l1.append(a)
      n-=1
  return l1
print(getlistlol())

##Q2.
def vowcon9(str):
    str = input("Enter a string: ")
    vow=0
    cons=0
    bs=0
    str1=str.lower()
    for i in str:
        if(i == "a" or i == "e" or i == "o" or i == "u" or i == "i"):
            vow+=1
        elif(i == " "):
            bs+=1
        else:
            cons+=1
    print("Number of vowells is:",vow)
    print("No of consonents=",cons)
    print("The no of blank spaces is: ",bs)
vowcon9(str)

##leetcode1
class Solution(object):
    def majorElement(self, nums):
        nums = {}

        for n in nums:
            if n not in nums:
                nums[n] = 1
            else:
                nums[n] += 1
            if nums[n] > len(nums) / 2:
                return n

##leetcodde2

class Solution(object):
    def constr(self, ransomNote, magazine):
        if len(ransomNote) > len(magazine):
            return False
        res={}
        for char in magazine:
            if char in res:
                res[i]+=1
            else:
                 res[i]=1
        for char in ransomNote:
            if char in res and res[char]>0:
                 res[char]-=1
            else:
                return False
        return True

##lc3

str="Shantanoo"
dic={}
f=0
unique=""
for i in str:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
for key,value in enumerate(str):
    if dic[value]==1:
        f=1
        unique=value
        index=key
        break
if f==1:
     print("The unique char is:",unique," ",index)
else:
        print(-1)
