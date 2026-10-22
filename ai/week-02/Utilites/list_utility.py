n=[1,2,3,4,5,6]

even=[x for x in n if x%2==0 ]
squares=[x*x for x in n]
last_three=n[-3:]

print(f"Complete numbers: {n}")
print(f"Even numbers: {even}")
print(f"Square of the numbers: {squares}")
print(f"Last three numbers: {last_three}")