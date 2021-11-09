from threading import Thread

def work(id, start, end, result):
    total = 0
    for i in range(start, end):
        total += i
    result.append(total)
    print("work1")
    return

def work2(id, start, end, result):
    total = 0
    for i in range(start, end):
        total += i
    result.append(total)
    print("work2")
    return


START, END = 0, 10000
result = list()
th1 = Thread(target = work(1,START,END,result))
th1 = Thread(target = work2(1,START,END,result))

th1.start()
th1.join()

print(f"Result:{sum(result)}")