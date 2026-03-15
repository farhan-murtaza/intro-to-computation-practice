import threading
import time


num_threads = 5
iterations_in_one_thread = 100

counter = 0

def f():
    global counter

    for i in range(iterations_in_one_thread):
        v = counter
        time.sleep(0.00000000001)  # Simulate some processing
        v += 1
        counter = v

def run_experiment():
    global counter

    counter = 0
    threads = []
    for i in range(num_threads):
        t = threading.Thread(target=f)
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()
    
    print("Calculated value: %d" % counter)
    print("Expected value: %d" % (num_threads * iterations_in_one_thread))


run_experiment()





print("\nNow with synchronization:\n")

# Synchronization 
# What we need is some way of ensuring that critical sections are executed all in one go,
lock = threading.Lock()

def f():
    global counter

    for i in range(iterations_in_one_thread):
        lock.acquire()   # begin critical section
        v = counter
        time.sleep(0.00000000001)  # Simulate some processing
        v += 1
        counter = v
        lock.release()   # end critical section

run_experiment()



# But we will sure forget to release the lock .. just as we would forget 
# to close open files. Well, context managers to the rescue!

print("\nNow with synchronization using context manager:\n")
def f():
    global counter

    for i in range(iterations_in_one_thread):
        with lock:   # begin critical section
            v = counter
            time.sleep(0.00000000001)  # Simulate some processing
            v += 1
            counter = v
        # end critical section

run_experiment()
