from multiprocessing import Process
import time

def tm():
    for i in range(3):
        print(time.ctime())
        time.sleep(2)

p=Process(target=tm,name='godessxin')
p.daemon=True
p.start()
print("NAME:",p.name)
print("PID:",p.pid)
print("is alive",p.is_alive())
