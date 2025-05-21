## TASK 1:

- Threading and Multiprocessing libraries in python.

### Threads v/s Processes:

#### Process:

- Process are basically programs that are dispatched into CPU execution.

- Works independently (own nmemory, secure & no interference).

#### Thread:

- "lightweight process".
- Threads donot isolate unlike process.
- These are smaller and faster.
- 3 States: Running, Ready, and Blocked.

### 1. Python - multithreading:

- Python library used: `threading`
- New thread creation: `threading.Thread(func-target, args-params)`
- Start the thread:
  `.start()`
- End the thread execution:
  `.join()` - program will wait for completion of this thread...

### 2. Python - multiprocessing:

- Python library used: `multiprocessing`.
- It contains `Process`, `Pool` (data parallelism), `mp` (Shared Memory Objects), `Pipe` (2-way connection objs - send() / recv()), `Lock` (.acquire() / .release())
- Data Stored in Shared Memory: `Value`, `Array`
- & many more...
- This is used when there is requirements of performing complex tasks that utilizes or requires the high resource allocation as well as if there requires the efficient data parallelism. For instance: 10k units of data to be stored into the data warehouse but doing this with single process will take too much of time and memory allocation by single process if not optimized properly. Hence we divide the this into multiple workers using multiprocessing so that it divides the resources parallely.
- Single Process can have multiple threads...
