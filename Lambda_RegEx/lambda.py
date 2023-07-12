

# Created on Wed Apr  3 15:53:10 2019

# def plus_two(num):
#     return num+2
# print(plus_two(5))
#
# lambda_plus_two = lambda num: num+2
# print(lambda_plus_two(5))
#
# lambda_mul_3 = lambda num : num*3
# print(lambda_mul_3(5))


# # Example 2 - USING LAMBDA WITH A MAP
# numbers = [1,2,3,4,5,6,7,8,9,10]
# print(numbers)
#
# def add_five(num):
#     return num+5
#
#
#
# new_list_A = list(map(add_five, numbers))
# print(new_list_A)
#
#
# new_list_B = list(map(lambda num: num+5, numbers))
# print(new_list_B)



# Example 3 - Lambda with filter

numbers = [1, 4, 5, 10, 20, 30]
print(numbers)

def greater_than_five(number):
    if number > 5:
        return True
    else:
        return False



number_filter_A = list(filter(greater_than_five,numbers))
print(number_filter_A)

number_filter_B = list(filter(lambda num: num > 5, numbers))
print(number_filter_B)




# Example 4 - Lambda with reduce
from functools import reduce

numbers = [0, 5, 10, 20, 30, 40]
print(numbers)


def sum_up(a, b):
    return a + b

result_A = reduce(sum_up, numbers)
print(result_A)

result_B = reduce(lambda a,b : a+b, numbers)
print(result_B)















































