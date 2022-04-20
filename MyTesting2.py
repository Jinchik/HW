# def fun(a):
#     if a > 30:
#         return 5
#
#     else:
#         print(a)
#         return a + fun(a + 3)
#
#
# print(fun(25))


def fib(n):
    if n < 1:
        return None
    if n < 3:
        print("Another",n)
        return 1
    print(n)
    return fib(n - 1) + fib(n - 2)
print(fib(6))
