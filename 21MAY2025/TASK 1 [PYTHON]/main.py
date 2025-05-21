import os
import time
from threading import Thread, current_thread
from multiprocessing import Process, current_process

CNT = 200000000
SLEEP = 10

def io_bound(sec):
    
    p_id = os.getpid()
    
    thread_name = current_thread().name
    process_name = current_process().name
    
    
    print(f"""Started>>>>>>>>>>>>>>>>>>>>>>>>>
          Process id: {p_id}
          Process NAME: {process_name}
          Thread Name: {thread_name}""")
    
    time.sleep(sec)
    print(f"""<<<<<<<<<<<<<<<<<<<<<<<Completed!
          Process id: {p_id}
          Process NAME: {process_name}
          Thread Name: {thread_name}""")


def cpu_bound(n):

    p_id = os.getpid()
    
    thread_name = current_thread().name
    process_name = current_process().name
    
    print(f"""COUNTING Started>>>>>>>>>>>>>>>>>>>>>>>>>
          Process id: {p_id}
          Process NAME: {process_name}
          Thread Name: {thread_name}""")
    
    while n > 0:
        n -= 1
    print(f"""<<<<<<<<<<<<<<<<<<<<<<<COUNTING COMPLETED!
          Process id: {p_id}
          Process NAME: {process_name}
          Thread Name: {thread_name}""")
    

if __name__ == "__main__":
    
    st =  time.time()
    # Same Process Multiple threads [concept of multithreading...]
    # t1 = Thread(target=io_bound, args = (SLEEP,))
    # t2 = Thread(target=cpu_bound, args = (CNT,))
    
    # t1.start()
    # t2.start()
    # t1.join()
    # t2.join()
    
    # Concept of Multiprocessing:
    
    p1 = Process(target=io_bound, args=(SLEEP,))
    p2 = Process(target=cpu_bound, args=(CNT,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print(p1.pid)
    print(p2.pid)

    et = time.time()
    print(f"Execution Time: {et-st} seconds")

    
    