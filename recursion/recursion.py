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


# Recursice vs iterative

def powerOfTwo(n):
    # recursive approach
    # if num == 0:
    #     return 1
    # else:
    #     power = powerOfTwo(num-1)
    #     return power*2
    # iterative approach
    i = 0
    power = 1
    while i < n:
        power = power * 2
        i += 1
    return power


print(powerOfTwo(3))
