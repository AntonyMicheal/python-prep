import time

def my_func():
    start_time = time.time()
    s = 0
    for i in range(10):
        s+=i

    end_time = time.time()

    return s, float(end_time - start_time)

x, y = my_func()
print("sum = ", x, "time = ", y)