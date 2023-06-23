import time
'''
没带参数、没带返回值
没用@
'''
def time_counting(func_):
    def wrapper():
        start = time.time()
        func_()
        end = time.time()
        print(end - start)
    return wrapper


def func():
    start = 0
    
    end = 10000000

    for i in range(start,end):
        a = 1
        pass
dec = time_counting(func)
dec()

'''
没带参数、没带返回值
用@
'''
def time_counting(func_):
    def wrapper():
        start = time.time()
        func_()
        end = time.time()
        print(end - start)
    return wrapper

@time_counting
def func():
    start = 0
    
    end = 10000000

    for i in range(start,end):
        a = 1
        pass
func()

'''
带参数、没带返回值
用@
'''
def time_counting(func_):
    def wrapper(*args,**kwargs):
        start = time.time()
        func_(*args,**kwargs)
        end = time.time()
        print(f"执行{func_}花费：{end - start}秒")
    return wrapper

@time_counting
def func(a,b):
    start = a
    
    end = b

    for i in range(start,end):
        a = 1
        pass
func(a = 0,b = 10000000)

'''
带参数、带返回值
用@
'''
import time
def time_counting(func_):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func_(*args,**kwargs)
        end = time.time()
        print(f"执行{func_}花费：,输入：{kwargs}，{end - start}秒")
        return result
    return wrapper

@time_counting
def func(a,b):
    start = a
    
    end = b

    for i in range(start,end):
        a = 1
        pass
    return "I am func"
print(func(a = 0,b = 10000000))



from functools import lru_cache


@lru_cache(maxsize=10)
@time_counting
def func2(x:int) -> int:
    time.sleep(1)
    return x + 1

func2(x = 1)
print(func2.cache_info())
func2(x = 2)
print(func2.cache_info())
func2(x = 3)
print(func2.cache_info())
func2(x = 4)
print(func2.cache_info())
func2(x = 5)
print(func2.cache_info())
func2(x = 2)
print(func2.cache_info())
func2(x = 1)
print(func2.cache_info())
'''
执行<function func2 at 0x000001BA35B778B0>花费：,输入：{'x': 1}，1.0144031047821045秒
CacheInfo(hits=0, misses=1, maxsize=10, currsize=1)
执行<function func2 at 0x000001BA35B778B0>花费：,输入：{'x': 2}，1.0083935260772705秒
CacheInfo(hits=0, misses=2, maxsize=10, currsize=2)
执行<function func2 at 0x000001BA35B778B0>花费：,输入：{'x': 3}，1.006730079650879秒
CacheInfo(hits=0, misses=3, maxsize=10, currsize=3)
执行<function func2 at 0x000001BA35B778B0>花费：,输入：{'x': 4}，1.0102896690368652秒
CacheInfo(hits=0, misses=4, maxsize=10, currsize=4)
执行<function func2 at 0x000001BA35B778B0>花费：,输入：{'x': 5}，1.0026702880859375秒
CacheInfo(hits=0, misses=5, maxsize=10, currsize=5)
CacheInfo(hits=1, misses=5, maxsize=10, currsize=5)
CacheInfo(hits=2, misses=5, maxsize=10, currsize=5)

hits表示缓存命中的次数，misses表示缓存未命中的次数，maxsize表示缓存的最大大小，currsize表示当前缓存的大小。
'''