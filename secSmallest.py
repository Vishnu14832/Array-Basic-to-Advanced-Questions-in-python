#second smallest element in the array

marks = [40,30,45,68,95,80,35]
min = marks[0]
secSmall = marks[0]

for i in range(len(marks)):
  if(marks[i] < min):
    min = marks[i]

for num in range(len(marks)):
  if(marks[num] != min and  marks[num] < secSmall):
    secSmall = marks[num]

print(f"{min} first smallest array element")
print(f"{secSmall} second smallest array element")