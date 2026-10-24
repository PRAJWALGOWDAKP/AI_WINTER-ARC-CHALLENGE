# l=[1,7,8,4,5,6,9,2]
# def selection_sort_asc(l):
#   n=len(l)
#   for i in range(0,n):
#     min_index=i
#     for j in range(i+1,n):
#       if l[j]<l[min_index]:
#         min_index=j
#     l[i],l[min_index]=l[min_index],l[i]
#   return l
# def selection_sort_desc(l):
#   n=len(l)
#   for i in range(0,n):
#     max_index=i
#     for j in range(i+1,n):
#       if l[j]>l[max_index]:
#         max_index=j
#     l[i],l[max_index]=l[max_index],l[i]
#   return l

  
# res1=selection_sort_asc(l)
# print(res1)
# res2=selection_sort_desc(l)
# print(res2)

nums=[5,8,1,6,9,2,4]
def bubblesort_asc(nums):
  is_swap=False
  n=len(nums)
  for i in range(n-2,-1,-1):
    for j in range(0,i+1):
      if nums[j]>nums[j+1]:
        nums[j],nums[j+1]=nums[j+1],nums[j]
        is_swap=True
    if is_swap==False:
      break
  return nums
def bubblesort_desc(nums):
  is_swap=False
  n=len(nums)
  for i in range(n-2,-1,-1):
    for j in range(0,i+1):
      if nums[j]<nums[j+1]:
        nums[j],nums[j+1]=nums[j+1],nums[j]
        is_swap=True
    if is_swap==False:
      break
  return nums
res1=bubblesort_asc(nums)
res2=bubblesort_desc(nums)
print(res1)
print(res2)        
  