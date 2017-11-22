import threading

local_school = threading.local()

def process_student():

    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))

def process_thread(name):
    # 先执行传入绑定student,创建实例，name='Alica'：
    local_school.student = name
    #调用process_student()，线程name为'Thread-A'
    process_student()

t1 = threading.Thread(target=process_thread, args=('Alica',), name='Thread-A')
t2 = threading.Thread(target=process_thread, args=('Bob',), name ='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()