import os
import time
from typing import List, Optional
import multiprocessing
from multiprocessing import Process




class Worker:
    
    @staticmethod
    def run():
        print(f"Worker Started it's work")
        print(f"{multiprocessing.current_process()}")
        time.sleep(15)
        print(f"Worker completed it's work...")


if __name__ == "__main__":
    print(f"Number of CPUs: {multiprocessing.cpu_count()}")
    st = time.time()
    
    processes: List[multiprocessing.Process] = []

    num_of_workers = range(1000)

    for worker in num_of_workers:
        p = Process(target = Worker.run, name=f'worker-{worker}')
        processes.append(p)
    
    # Starting the processes...
    for p in processes:
        p.start()

        # p1.start()
        # p2.start()
    print(f"{multiprocessing.current_process()}")
    et = time.time()


    print(f"Executed in {et-st} seconds")
