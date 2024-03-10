#method overloading
# class test:
#     def func(self):
#         print("No argument method")
#     def func(self,a):
#         print("No argument method",a)
#     def func(self,a,b):
#         print("No argument method",(a+b))

# t=test()
# t.func()
# t.func(10)
# t.func(10,20)

#solution

# class mypython:
#     def sum(self,*n):
#         total=0
#         for x in n:
#             total=total+x
#         print("sum = ",total)

# m=mypython()
# m.sum(10,20)
# m.sum(10,30,40,50)


