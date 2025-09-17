marks_list = [20,30,45,12,9,13,78]
low = marks_list[0]

for num in range(len(marks_list)):
  if(marks_list[num] < low):
    low = marks_list[num]

print(f"the lowest element of an array in the list is {low}")