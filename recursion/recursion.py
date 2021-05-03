# A function that calls the itself but with a different input everytime. It also has a base case.
# How does it work?
# A method calls itself.
# Exit from an infinite loop which is the base case
# For example
# def firstMethod():
#     secondMethod()
#     print('I am the first method.')


# def secondMethod():
#     thirdMethod()
#     print('I am the second method.')


# def thirdMethod():
#     fourthMethod()
#     print('I am the third method.')


# def fourthMethod():
#     print('I am the fourth method.')


# # IF we represent this in a call stack we would see something like:
# firstMethod()


# At first the first method is pushed on to the top of the stack, which then calls the second method which inturn calls the third one and so on.
# Then when the last in method is executed it gets popped.
# import pdb


# def recursiveFunction(n):
#     if n < 1:
#         print(f"{n} is less than 1")
#     else:

#         recursiveFunction(n-1)
#         print(f'this is {n} and is getting called')


# recursiveFunction(5)

#  A recursive function the find the sum of all the numbers up to a given number would be like
# def fun1(x, y):
#     if(x == 0):
#         return y
#     else:
#         return fun1(x-1, x+y)

# The function fu1 calculates and returns (1+2....x-1+x)+y which is  x(x+1)/2 + y

# print(fun1(1, 2))
# def sum(x):
#     if(x < 1):
#         return 0
#     else:
#         return x + sum(x-1)
# print(sum(2))


# Recursive vs iterative


# def powerOfTwo(n):
#     # Iterative solution
#     # i = 0
#     # power = 1
#     # while i < n:
#     #     power = power * 2
#     #     i += 1
#     # return power

#     # recursive solution
#     if n == 0:
#         return 1
#     else:
#         power = powerOfTwo(n-1)
#         return power * 2


# print(powerOfTwo(4))

# in recursive function, infinite recursion results in system crash but infinite iteration consumes CPU cycles.
# Space efficient => Iteration because no stack memory is required in case of iteration
# Time efficient => Iteration because no popping and pushing into the stack which makes recursion less time efficient
# Easy to code? => Recursion (if you know what you are doing.) We especially use it when we know the problem can be divided into similar sub problems.


# where should you use recursion?
# If we can easily break a problem into similar subproblem
# when we are fine with extra overhead both time and space that comes with it.
# When we need a quick working solution instead of efficient one.
# when we use memoization in recursion
# Using recursion is useful while traversing a tree.

# when to avoid it?
# if time and space complexity matter to us.
# example for mobile applications where memory is low we should avoid using recursion.
# or like in airbag situations where time matters, we avoid recursion.

# How to write recursion?
# Factorial
# import sys
# sys.setrecursionlimit(10000)


# def fact(num):
#     assert num >= 0 and int(
#         num) == num, 'The number must be positive integer only!'
#     if num in [0, 1]:
#         return 1
#     else:
#         return num * fact(num-1)


# print(fact(10))
#  fibonacci
# def fibonacci(n):
#     if n in [0, 1]:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)


# print(fibonacci(7))

# def fact(n):
#     if(n == 0):
#         return 1
#     else:
#         return n * fact(n-1)


# print(fact(5))

# Write a recursive function which takes an integer and computes the cumulative sum of 0 to that integer

# def cumulativeSum(n):
#     if n == 0:
#         return 1
#     else:

#         # print(result)
#         return n + cumulativeSum(n)


# print(cumulativeSum(4))
# def cumsum(n):
#     if n == 0:
#         return 0
#     else:
#         return n % 10 + cumsum(int(n/10))


# print(cumsum(54321))


def test(n):
    if n == 0:
        return 'hey'
    else:
        return 'this ' + test(n-1)


print(test(2))
