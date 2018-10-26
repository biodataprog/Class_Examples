#!/usr/bin/env python3

# expect to use subroutine like this:
# sum = sum_list_numbers([2,3,4,5])
# list_o_nums = [10,20,30,40]
# sum = sum_list_numbers(list_o_nums)
# print("sum is ",sum)

def sum_list_numbers(input_numbers):
    # this is the subroutine code
    running_total = 0
    for num in input_numbers:
        running_total += num
#    print(running_total)
    return running_total

def average(input_numbers):
    avg = sum_list_numbers(input_numbers) / len(input_numbers)
    return avg

# here we are actually using the subroutine
list_o_nums = [10,20,30,40]
sum = sum_list_numbers(list_o_nums)
print("sum of", list_o_nums,"is",sum)
print("avg of",list_o_nums,"is",average(list_o_nums))
