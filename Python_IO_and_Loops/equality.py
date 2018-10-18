#!/usr/bin/env python3

a="fiat"
b="".join(['f','i','a','t'])
c="fiat"
if a is b:
   print("strings are same")
if a == b:
   print("these are the same string: %s %s"%(a,b))

if a is c:
   print("c is a: %s %s"%(a,c))
