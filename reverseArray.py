def rev_list(items, start, end):
    while start < end:
        items[start], items[end] = items[end], items[start]  # proper swap
        
        start += 1
        end -= 1

items = [10, 20, 30, 40, 50]
rev_list(items, 0, len(items)-1)
print(items)
