marks = [40,30,45,68,95,80]
max = marks[0]

for  num in range(0,len(marks)):
  if(marks[num] > max):
    max = marks[num]

print(f"the largest element of array is {max}")