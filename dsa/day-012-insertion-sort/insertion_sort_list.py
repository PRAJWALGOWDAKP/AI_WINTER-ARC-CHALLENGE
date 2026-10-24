nums=[3,5,6,4,8,9,10,7,1]
def insertion_sort_asc(nums):
  n=len(nums)
  for i in range(1,n):
    key=nums[i]
    j=i-1
    while j>=0 and nums[j]>key:
      nums[j+1]=nums[j]
      j=j-1
    nums[j+1]=key
  return nums
def insertion_sort_desc(nums):
  n=len(nums)
  for i in range(1,n):
    key=nums[i]
    j=i-1
    while j>=0 and nums[j]<key:
      nums[j+1]=nums[j]
      j=j-1
    nums[j+1]=key
  return nums
res1=insertion_sort_asc(nums)
print(res1)
res2=insertion_sort_desc(nums)
print(res2)