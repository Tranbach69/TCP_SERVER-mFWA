import threading
import time
import psutil
import os
def get_mem_usage():
    PROCESS = psutil.Process(os.getpid())
    return PROCESS.memory_info().rss // 1024


def mythread():
    print ("Total number of threads", threading.activeCount())
    # mem_after_threads = get_mem_usage()
    # global MAX_MEMORY
    PROCESS = psutil.Process(os.getpid())
    mem=PROCESS.memory_info().rss // 1024
    # mem = get_mem_usage()
    print(f"Currently used memory={mem} KB")
    # MAX_MEMORY = max(mem, MAX_MEMORY)
    

def main():
    threads = 0     #thread counter
    y = 1000000     #a MILLION of 'em!
    for i in range(y):
        try:
            x = threading.Thread(target=mythread, daemon=True)
            threads += 1    #thread counter
            x.start()  #start each thread
            time.sleep(0.2)         
        except RuntimeError:    #too many throws a RuntimeError
            break
    print("{} threads created.\n".format(threads))

if __name__ == "__main__":
    main()
