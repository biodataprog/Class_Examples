#!/usr/bin/env python3
list = (11, 20, 2, 7, 20,)
i = 0

print("list before is", list)
list = sorted(list)
for item in sorted(list):
   print("i-th [%d] item is %s"%(i,item))
   i += 1

print("list after is", list)

list_len = len(list)
print(range(list_len))

for n in range(list_len):
   print("n is ",n)
   print("item is ",list[n])
