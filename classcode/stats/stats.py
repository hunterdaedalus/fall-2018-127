import time

import random

def build_random_list(num_items, max_value):
    l=[]

    for i in range(num_items):
        l = l + [ random.randrange(0,max_value) ]
    return l

def index_largest(l):
    li = 0
    for i in range(1,len(l)):
        if l[i] > l[li]:
            li = i
    return li
def freq(l,item):
    count = 0
    for i in l:
        if i==item:
            count = count + 1
    return count

def freq2(l,item):
    count = 0
    for i in range(len(l)):
        if l[i] == item:
            count = count + 1
    return count

def mode(l):
    msf_value = l[0]
    msf_freq = freq(l,l[0])
    msf_index = 0
    for i in range(len(l)):
        test_freq = freq(l,l[i])
        if test_freq >= msf_freq:
            #print("Found new possible mode:")
            #print("old mode: ",msf_value, " old_freq: " , msf_freq, "old location: ",msf_index)
            #print("new mode: ",l[i], " new freq:" , test_freq, "new location: ",i)
            #print("-------------------------------------------\n")
            msf_value = l[i]
            msf_index = i
            msf_freq = test_freq
    return msf_value

def fast_mode(l,max_value):
    tallies = []
    for i in range(max_value):
        tallies.append(0)
    for item in l:
        tallies[item] = tallies[item] + 1

    li = index_largest(tallies)
    return li

# l = build_random_list(30,100)
# li = index_largest(l)
# print(l)
# print(li,l[li])
# l[20]=5000
# l[25]=5000
# li = index_largest(l)
# print(li,l[li])

# mode_test_list = [9,12,31,3,3,8,2,8,6,7,8,4,8,15]
# print(mode(mode_test_list))

# base_size = 10000;
# for i in range(1,7):
#     l = build_random_list(base_size * i,100)
#     start_time = int(round(time.time() * 1000))
#     li = index_largest(l)
#     running_time = int(round(time.time() * 1000)) - start_time
#     print("Len: ",len(l), " largest: ",l[li], "milliseconds: ", running_time)
base_size = 10000
for i in range(1,7):
     l = build_random_list(base_size * i,100)
     #start_time = int(round(time.time() * 1000))
     #m = mode(l)
     #running_time = int(round(time.time() * 1000)) - start_time
     #print("Len: ",len(l), " mode: ",m, "milliseconds: ", running_time)
     start_time = int(round(time.time() * 1000))
     m = fast_mode(l,100)
     running_time = int(round(time.time() * 1000)) - start_time
     print("Len: ",len(l), " mode: ",m, "milliseconds: ", running_time)
    
