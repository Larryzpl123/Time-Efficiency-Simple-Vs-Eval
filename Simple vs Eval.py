import timeit

# 测试 a + b
setup = "a = 1; b = 2"
direct_add = "a + b"
eval_add = "eval('a + b')"

direct_time = timeit.timeit(direct_add, setup=setup, number=1000000)
eval_time = timeit.timeit(eval_add, setup=setup, number=1000000)

print(f"直接加法 (a + b): {direct_time:.6f} 秒")
print(f"eval('a + b'): {eval_time:.6f} 秒")
