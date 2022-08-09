# def square(x):
#     return x*x

# print(square(3)) # >> 9

# f=square

# print(f)   # >> <function square at 0x1029a0a60>
# print(f(5)) # >> 25

# def logger(msg):
#     def log_message():  # 1
#         print('Log: ', msg)

#     return log_message

# log_hi = logger('Hi')
# print(log_hi)  # log_message 오브젝트가 출력됩니다.
# log_hi()  # "Log: Hi"가 출력됩니다.

def decorate(func):
    def func_wrapper():
        print("welcome to")
        func()
        print("with python")
        return func_wrapper
        
@decorate
def function2():
    print("hello world")
    return

# function2()
print('f')