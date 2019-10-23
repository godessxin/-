from  multiprocessing import Process
from time import sleep

def worker(sec,name):
    for i  in range(3):
        sleep(sec)
        print("I'M%s"%name)
        print("I'm working...")

# p=Process(target=worker,args=(2,'LEVI0'))
p=Process(target=worker,kwargs={'na me':'Abby'})
p.start()
p.join()
print('==========')