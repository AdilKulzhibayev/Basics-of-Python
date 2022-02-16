from itertools import cycle, count
from functools import reduce, partial

#
# my_func = partial(sum,5)
# result = my_func(4)
# print(result)























# for el in count(1,5):
#     print(el)
#     if el > 100:
#         break
i = 0
my_list = [1,2,3]
print(sum(my_list))
my_func = lambda a,b: a + b
result = reduce(my_func, my_list)

# print(result)











# for el in cycle(my_list):
#     print(el)
#     i +=1
#     if i > 100:
#         break



















# from random import randint, random, randrange
# # result = randint(-2,9)
# # result = randrange(0,1)
# result = random()
# print(result)
#
#
#
#
#
#
#
#
#
#
#
#
# #
# # my_list = []
# # for i in range(10):
# #     my_list.append(i)
# # print(my_list)
# #
# # my_list2 = [el for el in range(10)]
# #
# # print(my_list2)
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# # # import random as r
# # # # from random import randint
# # #
# # # print(r.randint(1,5))
# #
# # # from sys import argv
# # # print(argv)
# # # name = argv[1]
# # #
# # # result = f'Hello {name}'
# # #
# # # print(result)
