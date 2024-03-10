
# from threading import *
# def show():
#     for x in range(1,11):
#         print("Child Thread")

# t=Thread (target=show)
# t.start()
# for x in range(1,11):
#     print("Main Thread")

# ===========================================

# from threading import *
# class Mythread:
#     def show(self):
#         for x in range(1,11):
#             print("child thread")
# m=Mythread()
# t=Thread(target=m.show())
# t.start()
# for x in range (1,11):
#     print("main thread")

# ==========================================

# from threading import *
# class Mythread(Thread):
#     def show(self):
#         for x in range(1,11):
#             print("child thread")
# m=Mythread()
# t.start()
# for x in range (1,11):
#     print("main thread")

# ============================================

# from threading import *
# print(current_thread().getName())
# current_thread().setName("RCPIT Thread")
# print(current_thread().getName())

# =============================================

# from threading import *
# class Mythread:
#     def run(self):
#         for x in range(1,11):
#             print("child thread")
# m=Mythread()
# t=Thread(target = m.run)
# t.start()
# t.join()
# for x in range (1,11):
#     print("main thread")

#=========================

# from threading import *
# class Mythread:
#     def run(self):
#         for x in range(1,11):
#             print("child thread")
# m=Mythread()
# t=Thread(target = m.run)
#t.setDaemon(True):
# t.start()
# for x in range (1,11):
#     print("main thread")

#======================================

# from threading import *
# import time
# l=Semaphore(2)
# def play(name):
#   l.acquire()
#   for i in range(10):
#     print("Batting :",name)
#     time.sleep()
#   l.release()

# t1=Thread(target = play,args=("sachin"))
# t2=Thread(target = play,args=("Yuvraj"))
# t3=Thread(target = play,args=("kohli"))
# t1.start()
# t2.start()
# t3.start()







