from concurrent import futures


def printer(data):
    for i in data:
        return (i)

data = [1,2,3,4,5,6,7,8,10]
with futures.ProcessPoolExecutor(max_workers = 4) as executor:
    go_printer = executor.submit(printer,data)
    for f in futures.as_completed(go_printer):
        print(f.result)
# from concurrent import futures
#
# def test(num):
#     import time
#     return time.ctime(), num
#
#
# def muti_exec(m, n):
#     # m 并发次数
#     # n 运行次数
#
#     with futures.ProcessPoolExecutor(max_workers=m) as executor:  # 多进程
#         # with futures.ThreadPoolExecutor(max_workers=m) as executor: #多线程
#         executor_dict = dict((executor.submit(test, times), times) for times in range(m * n))
#
#     for future in futures.as_completed(executor_dict):
#         times = executor_dict[future]
#         if future.exception() is not None:
#             print('%r generated an exception: %s' % (times, future.exception()))
#         else:
#             print('RunTimes:%d,Res:%s' % (times, future.result()))
#
#
# if __name__ == '__main__':
#     muti_exec(5, 1)