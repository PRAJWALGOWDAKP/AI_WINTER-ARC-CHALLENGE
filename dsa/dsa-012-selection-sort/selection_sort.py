l=[1,7,8,4,5,6,9,2]
def selection_sort_asc(l):
  n=len(l)
  for i in range(0,n):
    min_index=i
    for j in range(i+1,n):
      if l[j]<l[min_index]:
        min_index=j
    l[i],l[min_index]=l[min_index],l[i]
  return l
def selection_sort_desc(l):
  n=len(l)
  for i in range(0,n):
    max_index=i
    for j in range(i+1,n):
      if l[j]>l[max_index]:
        max_index=j
    l[i],l[max_index]=l[max_index],l[i]
  return l
res1=selection_sort_asc(l)
print(res1)
res2=selection_sort_desc(l)
print(res2)