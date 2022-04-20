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


# def fib(n):
#     if n < 1:
#         return None
#     if n < 3:
#         print("Another",n)
#         return 1
#     print(n)
#     return fib(n - 1) + fib(n - 2)
# print(fib(6))

# school_class = {}
#
# while True:
#     name = input("Enter the student's name: ")
#     if name == '':
#         break
#
#     score = int(input("Enter the student's score (0-10): "))
#     if score not in range(0, 11):
#         break
#
#     if name in school_class:
#         school_class[name] += (score,)
#     else:
#         school_class[name] = (score,)
#
# for name in sorted(school_class.keys()):
#     adding = 0
#     counter = 0
#     for score in school_class[name]:
#         adding += score
#         print(adding)
#         counter += 1
#     print(name, ":", adding / counter)



# def f(x):
#     if x == 0:
#         return 0
#     return x + f(x - 1)
# print(f(3))


# def any():
#    print(var + 1, end ='')
# var = 1
# print(var)
# any()
# print(var)


# tup = (1, 2, 4, 8)
# tup = tup[1:-1]
# print(tup)
# tup = tup[0]
# print(tup)

dictionary = {}
my_list = ['a', 'b', 'c', 'd']
for i in range(len(my_list) - 1):
      dictionary[my_list[i]] = (my_list[i], )
for i in sorted(dictionary.keys()):
    k = dictionary[i]
    print(k[0])