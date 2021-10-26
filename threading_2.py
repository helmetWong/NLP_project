import concurrent.futures 
import time

#https://github.com/CoreyMSchafer/code_snippets/tree/master/Python/Threading

start = time.perf_counter()


def do_something(second):
    print (f'Sleeping {second} second(s)...')
    time.sleep(second)
    return f'Done Sleeping....{second}'

#with concurrent.futures.ThreadPoolExecutor() as executor:
#    f1 = executor.submit(do_something, 1)
#    f2 = executor.submit(do_something, 1)
#    print (f1.result())
#    print (f2.result())

#finish = time.perf_counter()

#print (f'Finished in {round(finish-start, 2)} second(s)')

#####################################################################
#with concurrent.futures.ThreadPoolExecutor() as executor:
#    secs = [5, 4, 3, 2, 1]
#    results = [executor.submit (do_something, sec) for sec in secs]
#    for f in concurrent.futures.as_completed(results):
#        print (f.result())

#####################################################################
with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    results = executor.map (do_something, secs)

for result in results:
    print (result)