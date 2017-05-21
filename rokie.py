#!/bin/python

import sys
import time
import copy


n, m = raw_input().strip().split(' ')
n, m = [int(n), int(m)]
route = []
for route_i in xrange(m):
    route_temp = map(int,raw_input().strip().split(' '))
    route.append(route_temp)
# Write Your Code Here
prifor = copy.deepcopy(time.time())
temp_route = copy.copy(route)
for rote in range(0,len(route)):
    verdade = False
    temp_list = copy.copy(route[0])
    route.pop(0)
    index = -1
    # # secfor = copy.deepcopy(time.time())
    #
    for ele in temp_list:
    #     terfor = copy.deepcopy(time.time())
    #
        for linha in range(0, len(route)):
            try:
                route[linha].index(ele)
                verdade = True
                index = linha

            except:
                pass

            if (index != -1):

                route[index] = list(set(route[index] + temp_list))
                break
        if (verdade):
            break
        else:
            route.append(temp_list)
        # fimterfor = copy.deepcopy(time.time())
        # print 'terceiro for ' + str(fimterfor - terfor)

#     fimsecfor = copy.deepcopy(time.time())
#     print 'segundo for ' + str(fimsecfor - secfor)
fimprifor = copy.deepcopy(time.time())

num = 0
print route
for quant in route:

    if(len(quant) > num):
        num = len(quant)
print num
print 'primeiro for '+str(fimprifor-prifor)