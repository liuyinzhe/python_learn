import psutil
print(psutil.cpu_count())  # 12

# 或者使用 multiprocessing
import multiprocessing
print(multiprocessing.cpu_count())  # 12


# 获取 CPU 的物理核心数量
print(psutil.cpu_count(logical=False))  # 6

# 统计 CPU 的用户／系统／空闲时间
print(psutil.cpu_times())
"""
scputimes(user=84732.10937499999, 
          system=37132.85937500023, 
          idle=2003964.1249999998, 
          interrupt=3500.765625, 
          dpc=1089.6875)
"""
# 还有一个 psutil.cpu_times_percent() 
# 功能与之类似, 只不过返回的是比例

# 查看 CPU 的使用率
for x in range(3):
    # interval：表示每隔 0.5s 刷新一次
    # percpu：为 True 表示查看所有的 cpu 使用率
    print(psutil.cpu_percent(interval=0.5, percpu=True))
"""
[9.1, 3.1, 12.5, 3.1, 15.6, 0.0, 6.2, 0.0, 12.5, 50.0, 9.4, 3.1]
[9.1, 6.2, 12.5, 6.2, 3.1, 0.0, 0.0, 3.1, 0.0, 15.6, 3.1, 0.0]
[0.0, 0.0, 15.6, 0.0, 6.2, 0.0, 6.2, 25.0, 3.1, 9.4, 6.2, 0.0]
"""
# 这里 cpu 的逻辑数量是 12
# 所以每个列表里面有 12 个元素


# 查看 CPU 的统计信息
print(psutil.cpu_stats())
"""
scpustats(ctx_switches=3346512902, 
          interrupts=2288572793, 
          soft_interrupts=0, 
          syscalls=3324041552)
"""

# 查看 CPU 的频率
print(psutil.cpu_freq())
"""
scpufreq(current=2208.0, min=0.0, max=2208.0)
"""

