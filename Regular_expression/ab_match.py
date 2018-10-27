#!/usr/bin/env python3
import re
m = re.search("(((AB)+)C)","ABABABCDED")
if m:
    print("Group 0",m.group(0))
    print("Group 1",m.group(1))
    print("Group 2",m.group(2))
    print("Group 3",m.group(3))

print("==")
m = re.search("((AB)+).+","ABABABCDED")
if m:
    print("Group 0",m.group(0))
    print("Group 1",m.group(1))
    print("Group 2",m.group(2))
    #print("Group 3",m.group(3))

nums = ["3","40","90","99","100","101","200","10100"]
print("==")
for n in nums:
    m = re.search("^(\d{1,2}|100)$",n)
    if m:
        print("string",n,"matches")
        print(m.group(0))
    else:
        print("string",n,"does not match")
