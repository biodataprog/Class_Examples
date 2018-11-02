#!/usr/bin/env python3

months = {'Dec': 12, 'Jan': 1, 'Feb': 2, 'Mar': 3}

print("unsorted months")
print(months)
for m in months:
    print(m, months[m])

monthsalpha = sorted(months)

print("alpha sorted months")
print(monthsalpha)
for m in monthsalpha:
    print(m, months[m])

months_lookupsorted = sorted(months, key=months.__getitem__, reverse=True)

print("numeric lookup sorted months")
print(months_lookupsorted)
for m in months_lookupsorted:
    print(m, months[m])

