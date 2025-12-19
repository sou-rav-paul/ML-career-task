import time
n=100000
user_list=list(range(n))
user_set=set(range(n))
target=-1
start=time.time()
time_for_list = target in user_list
end = time.time()
print('Time for list :',(end-start)*1000000)

start=time.time()
time_for_list = target in user_set
end = time.time()
print('Time for set :',(end-start)*1000000)




