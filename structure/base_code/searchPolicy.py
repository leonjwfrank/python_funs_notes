"""
~~~ 查找策略
    顺序（无序，有序）
    二分查找(有序)，迭代和非迭代实现
"""


def binarySearch(alist, item):
    """二分查找的非递归实现"""
    first = 0
    last = len(alist) - 1
    found = False
    iter_t = 0
    while first <= last and not found:
        iter_t += 1

        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    print(f'search times:{iter_t}')
    return found


def recursionSearch(alist, item, rec_t=0):
    """二分查找的递归实现"""
    rec_t += 1
    if len(alist) == 0:
        return False  # 结束条件
    else:
        midpoint = len(alist) // 2
        if alist[midpoint] == item:
            return True
        else:
            if item < alist[midpoint]:  # 缩小规模
                print('now search rec_t:{}'.format(rec_t))
                return recursionSearch(alist[:midpoint], item)  # 调用自身
            else:
                print('now search rec_t:{}'.format(rec_t))
                return recursionSearch(alist[midpoint + 1:], item)  # 调用自身


def bubbleSort(alist, x=0):
    """冒泡排序"""
    exchange = True  # 用于检测冒泡排序是否发生交换
    for passnum in range(len(alist) - 1, 0, -1):
        if exchange:
            exchange = False
            for i in range(passnum):  # n-1 趟
                x += 1
                if alist[i] > alist[i + 1]:
                    exchange = True
                    print(f'是否发生交换:{exchange}')
                    """
                    # 序错，交换开始
                    temp = alist[i]
                    alist[i] = alist[i+1]
                    alist[i+1] = temp
                    # 序错，交换结束
                    """
                    alist[i], alist[i + 1] = alist[i + 1], alist[i]
    print('sort times:{}'.format(x))
    return alist


def shortBubbleSort(alist, n=0):
    """冒泡性能改进
    """
    exchanges = True
    passnum = len(alist) - 1
    while passnum > 0 and exchanges:
        exchanges = False

        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                n += 1  # 排序多少次
                exchanges = True
                # temp = alist[i]
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
        passnum = passnum - 1
    print(f'共排序{n}次')
    return alist


def selectionSorting(alist, n=0):
    """选择排序"""
    for fill in range(len(alist) - 1, 0, -1):
        positionOfMax = 0
        for local in range(1, fill + 1):

            if alist[local] > alist[positionOfMax]:
                n += 1
                positionOfMax = local

        # 选择排序是在每一次内存循环完成后才进行的
        alist[fill], alist[positionOfMax] = alist[positionOfMax], alist[fill]  # 交换位置
    print(f'select sort n:{n}')
    return alist


def insertionSort(alist, n=0):
    """插入排序
    移动操作仅包含一次赋值，是交换操作的1/3，所以插入排序性能会好一些"""
    for index in range(1, len(alist)):
        currentvalue = alist[index]  # 新项/插入项
        position = index
        while position > 0 and alist[position - 1] > currentvalue:  # 如果大于当前项进入循环
            n += 1
            alist[position] = alist[position - 1]  # 对比，移动
            position = position - 1

        alist[position] = currentvalue  # 插入新项
    print('插入排序比对次数{}'.format(n))
    return alist


def shellSort(alist):
    """谢尔排序, gap 取值1，3，5，7，9... 2k-1
    O(N**(3/2))"""
    sublistcount = len(alist) // 2  # 间隔设定
    while sublistcount > 0:
        for startposition in range(sublistcount):  # 子列表排序
            gapInsertionSort(alist, startposition, sublistcount)
        print("After increment of size:{}, \n The list:{} ".format(sublistcount, alist))

        sublistcount = sublistcount // 2  # 间隔缩小

    return alist

def gapInsertionSort(alist, start, gap):
    """间隔插入排序"""
    for i in range(start + gap, len(alist), gap):
        currentvalue = alist[i]
        position = 1

        while position >= gap and alist[position - gap] > currentvalue:
            alist[position] = alist[position - gap]
            position = position - gap
    pass

def mergeSort(alist, n=0):
    """归并排序"""
    print('split:{}'.format(alist))
    if len(alist) > 1:
        mid = len(alist) // 2   # 基本结束条件
        lefthalf = alist[:mid]
        rightalf = alist[mid:]

        mergeSort(lefthalf) #递归调用左半部分,排序左部分
        mergeSort(rightalf) #递归调用右半部分，排序右部分
        print(f'left{lefthalf}')
        print(f'right{rightalf}')

        i=j=k=0
        while i<len(lefthalf) and j>len(rightalf):

            if lefthalf[i]<rightalf[j]:
                # 交错把左右半部从小到大归并到结果列表中
                alist[k]=lefthalf[i]
                i+=1
                print(f"merga times:i{i},j{j},k{k}, alist:{alist}")
            else:
                alist[k] = rightalf[j]
                j+=1
                print(f"merga times:i{i},j{j},k{k}, alist:{alist}")
            k+=1

        while i<len(lefthalf):
            # 归并左半部
            alist[k]=lefthalf[i]
            i+=1
            k+=1
            print(f"merga times:i{i},j{j},k{k}, alist:{alist}")
        while j<len(rightalf):
            # 归并右半部
            alist[k]=rightalf[j]
            j+=1
            k+=1
            print(f"merga times:i{i},j{j},k{k}, alist:{alist}")
        # return alist


def merge_sort(lst, n=0):
    """pythonic 的归并排序"""
    if len(lst) <= 1:
        return lst
    # 分解问题，递归调用解决
    midd = len(lst) // 2
    left = merge_sort(lst[:midd])   # 左部排好序
    right = merge_sort(lst[midd:]) # 右部排好序

    # 合并左右半部，完成排序
    merged = []
    while left and right:
        n+= 1
        if left[0] <= right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))
    merged.extend(right if right else left)
    print(f'pythonic 归并排序{n}次:{merged}')
    return merged

class QuickSort(object):

    @staticmethod
    def quickSort(alist):
        QuickSort.quickSortHelper(alist, 0, len(alist)-1)
        return alist

    @staticmethod
    def quickSortHelper(alist, first,last, n=0):
        if first<last:  # 基本结束条件，如果first 还大于等于last，则继续分裂
            n+=1
            splitpoint = QuickSort.partition(alist,first,last)  # 分裂

            QuickSort.quickSortHelper(alist,first,splitpoint-1)  # 递归调用快速排序
            QuickSort.quickSortHelper(alist,splitpoint+1,last)

            print(f"快速排序{n}次，{alist}")
        return alist

    @staticmethod
    def partition(alist,first,last):
        """快速排序的分裂函数"""
        pivotvalue = alist[first]  # 选择中值
        leftmark = first + 1
        rightmark = last        # 左右标初值

        done = False
        while not done:
            while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
                # 左标向右移
                leftmark = leftmark + 1
            while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
                # 右标向左移
                rightmark = rightmark - 1
            if rightmark < leftmark:
                # 左右标相错则结束
                done = True
            else:

                # # 左右标值交换
                alist[leftmark], alist[rightmark] = alist[rightmark], alist[leftmark]
                """
                #或者经典写法:
                temp = alist[leftmark]
                alist[leftmark] = alist[rightmark]
                alist[rightmark] = temp
                #"""
        # 中值就位
        temp = alist[first]
        alist[first] = alist[rightmark]
        alist[rightmark] = temp

        return rightmark  # 返回中值点，分裂点

if __name__ == '__main__':
    import time

    """
    testlist = [0,1,2,3,7,8,13,25,258,1992,]
    t0 = time.clock()
    print(binarySearch(testlist, 258))
    print('timeit:{}'.format(time.clock() - t0))

    t1 = time.clock()
    print(binarySearch(testlist, 125))
    print('timeit2:{}'.format(time.clock() - t1))

    t2 = time.clock()
    print(recursionSearch(testlist, 258))
    print('timeit3:{}'.format(time.clock() - t2))
    """

    t3 = time.clock()
    alist = [1, 3, 45, 3, 43434, 3, 2, 3, 43, 23, 534]
    print(bubbleSort([1, 3, 45, 3, 43434, 3, 2, 3, 43, 23, 534]))
    print('timeit3:{}'.format(time.clock() - t3))

    t4 = time.clock()
    print(shortBubbleSort(alist))
    print('timeit4:{}'.format(time.clock() - t3))

    t5 = time.clock()
    print(selectionSorting(alist))
    print('timeit5:{}'.format(time.clock() - t5))

    t6 = time.clock()
    print(f"插入排序:{insertionSort(alist)}")
    print('timeit6:{}'.format(time.clock() - t6))

    t7 = time.clock()
    print(f"shellSort: {shellSort(alist)}")
    print('timeit7:{}'.format(time.clock() - t7))


    t8 = time.time()
    alist = [1, 3, 45, 3, 43434, 3, 2, 3, 43, 23, 534]
    print(f'归并排序:{merge_sort(alist)}')
    print('timeit8:{}'.format(time.clock() - t8))


    t9=time.time()
    alist = [54,26,93,17,77,31,44,55,20]
    print(f'快速排序:{QuickSort.quickSort(alist)}')
    print('timeit9:{}'.format(time.clock() - t9))