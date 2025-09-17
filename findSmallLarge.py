#find the smallest and largest element of an array

list_marks = [99,90,100,89,78,88,97]
max = list_marks[0]
min = list_marks[0]

for num in range(len(list_marks)):
  if(list_marks[num] > max):
    max = list_marks[num]
  if(list_marks[num] < min):
    min = list_marks[num]

print(f"{max} the largest array element")
print(f"{min} the smallest array element")