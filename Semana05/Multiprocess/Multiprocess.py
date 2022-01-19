"""
import time
start = time.perf_counter()
def do_something():
	print('Sleeping for 01 second...')
	time.sleep(1)
	print('Done sleeping...')
do_something()
finished = time.perf_counter()
print(f'Finished in {round(finished - start, 2)} second(s)')
"""
"""
import time
import multiprocessing
start = time.perf_counter()
def do_something():
	print('Sleeping for 01 second...')
	time.sleep(1)
	print('Done sleeping...')
p1 = multiprocessing.Process(target= do_something)
p2 = multiprocessing.Process(target= do_something)
p1.start()
p2.start()
p1.join()
p2.join()
finished = time.perf_counter()
print(f'Finished in {round(finished - start, 2)} second(s)')
"""
"""
import time
import multiprocessing
start = time.perf_counter()
def do_something():
	print('Sleeping for 01 second...')
	time.sleep(1)
	print('Done sleeping...')
processes = []
for _ in range(10):
	p = multiprocessing.Process(target= do_something)
	p.start()
	processes.append(p)
for process in processes:
	process.join()
finished = time.perf_counter()
print(f'Finished in {round(finished - start, 2)} second(s)')
"""
"""
import time
import multiprocessing
start = time.perf_counter()
def do_something(seconds):
	print(f'Sleeping for {seconds} second(s)...')
	time.sleep(seconds)
	print('Done sleeping...')
processes = []
for _ in range(10):
	p = multiprocessing.Process(target= do_something, args =[1.5])
	p.start()
	processes.append(p)
for process in processes:
	process.join()
finished = time.perf_counter()
print(f'Finished in {round(finished - start, 2)} second(s)')
"""
"""
import time
import concurrent.futures
start = time.perf_counter()
def do_something(seconds):
	print(f'Sleeping for {seconds} second(s)...')
	time.sleep(seconds)
	return 'Done sleeping...'
with concurrent.futures.ProcessPoolExecutor() as executor:
	f1 = executor.submit(do_something, 1)
	print(f1.result())
finished = time.perf_counter()
print(f'Finished in {round(finished - start, 2)} second(s)')
"""
"""
import time
import concurrent.futures
start = time.perf_counter()
def do_something(seconds):
	print(f'Sleeping for {seconds} second(s)...')
	time.sleep(seconds)
	return 'Done sleeping...'
with concurrent.futures.ProcessPoolExecutor() as executor:
	f1 = executor.submit(do_something, 1)
	f2 = executor.submit(do_something, 1)
	print(f1.result())
	print(f2.result())
finished = time.perf_counter()
print(f'Finished in {round(finished - start, 2)} second(s)')
"""
"""
import time
import concurrent.futures
start = time.perf_counter()
def do_something(seconds):
	print(f'Sleeping for {seconds} second(s)...')
	time.sleep(seconds)
	return 'Done sleeping...'
with concurrent.futures.ProcessPoolExecutor() as executor:
	results = [executor.submit(do_something, 1) for _ in range(10)] 
	
	for f in concurrent.futures.as_completed(results):
		print(f.result())
finished = time.perf_counter()
print(f'Finished in {round(finished - start, 2)} second(s)')
"""
"""
import time
import concurrent.futures
start = time.perf_counter()
def do_something(seconds):
	print(f'Sleeping for {seconds} second(s)...')
	time.sleep(seconds)
	return (f'Done sleeping {seconds}...')
with concurrent.futures.ProcessPoolExecutor() as executor:
	secs = [5, 4, 3, 2, 1]
	results = [executor.submit(do_something, sec) for sec in secs] 
	
	for f in concurrent.futures.as_completed(results):
		print(f.result())
finished = time.perf_counter()
print(f'Finished in {round(finished - start, 2)} second(s)')
"""
"""
import time
import concurrent.futures
start = time.perf_counter()
def do_something(seconds):
	print(f'Sleeping for {seconds} second(s)...')
	time.sleep(seconds)
	return (f'Done sleeping {seconds}...')
with concurrent.futures.ThreadPoolExecutor() as executor:
	secs = [5, 4, 3, 2, 1]
	results = executor.map(do_something, secs)
	
	for result in results:
		print(result)
finished = time.perf_counter()
print(f'Finished in {round(finished - start, 2)} second(s)')
"""
"""
import time
import concurrent.futures

start = time.perf_counter()

def do_something(seconds):
	print(f'Sleeping for {seconds} second(s)...')
	time.sleep(seconds)
	return (f'Done sleeping {seconds}...')

with concurrent.futures.ThreadPoolExecutor() as executor:
	secs = [5, 4, 3, 2, 1]
	results = executor.map(do_something, secs)


finished = time.perf_counter()

print(f'Finished in {round(finished - start, 2)} second(s)')