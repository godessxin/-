from multiprocessing import Process,Queue
from time import sleep
#消息队列
q=Queue(3)

def request():
    print("使用wx登录？")
    q.put("请求用户名密码")
    data=q.get()
    print("获取信息",data)

def handle():
    data =q.get()
    print("收到请求：",data)
    sleep(3)
    q.put({'name':'zhang','passwd':'123'})

p1=Process(target=request)
p2=Process(target=handle)
p1.start()
p2.start()
p1.join()
p2.join()