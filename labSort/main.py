# 5, б, е, ж:
# Массив данных о преподавателях: ФИО преподавателя, факультет,
# ученое звание, ученая степень (сравнение по  полям - факультет, ФИО, степень, звание)
# Сортировка пузырьком, Быстрая сортировка, Сортировка слиянием
# https://www.kaggle.com/datasets/zusmani/pakistanintellectualcapitalcs
import pandas as pd
import time
import matplotlib.pyplot as plt


# Перегрузка операторов >, <, >=, <=, ==
class teacher:
    def __init__(self, name:str, department:str, designation:str, degree:str):
        self.name = name
        self.department = department
        self.designation = designation
        self.degree = degree
    # <
    def __lt__(self, other):
        if self.department < other.department:
            return True
        elif self.department > other.department:
            return False
        else:
            if self.name < other.name:
                return True
            elif self.name > other.name:
                return False
            else:
                if self.degree < other.degree:
                    return True
                elif self.degree > other.degree:
                    return False
                else:
                    if self.designation < other.designation:
                        return True
                    else:
                        return False
    # <=
    def __le__(self, other):
        if self.department < other.department:
            return True
        elif self.department > other.department:
            return False
        else:
            if self.name < other.name:
                return True
            elif self.name > other.name:
                return False
            else:
                if self.degree < other.degree:
                    return True
                elif self.degree > other.degree:
                    return False
                else:
                    if self.designation < other.designation:
                        return True
                    elif self.designation < other.designation:
                        return False
                    else:
                        return True

    # >
    def __gt__(self, other):
        if self.department > other.department:
            return True
        elif self.department < other.department:
            return False
        else:
            if self.name > other.name:
                return True
            elif self.name < other.name:
                return False
            else:
                if self.degree > other.degree:
                    return True
                elif self.degree < other.degree:
                    return False
                else:
                    if self.designation > other.designation:
                        return True
                    else:
                        return False
    # >=
    def __ge__(self, other):
        if self.department > other.department:
            return True
        elif self.department < other.department:
            return False
        else:
            if self.name > other.name:
                return True
            elif self.name < other.name:
                return False
            else:
                if self.degree > other.degree:
                    return True
                elif self.degree < other.degree:
                    return False
                else:
                    if self.designation > other.designation:
                        return True
                    elif self.designation < other.designation:
                        return False
                    else:
                        return True
    #  ==
    def __eq__(self, other):
        if self.department != other.department:
            return False
        if self.name != other.name:
            return False
        if self.degree != other.degree:
            return False
        if self.designation != other.designation:
            return False
        return True

def bubble_sort(mas):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(mas) - 1):
            if mas[i] > mas[i + 1]:
                mas[i], mas[i + 1] = mas[i + 1], mas[i]
                swapped = True
    return mas


def partition(array, start, end):
    pivot = array[(start + end) // 2]
    i = start
    j = end
    while i <= j:
        while array[i] < pivot:
            i += 1
        while array[j] > pivot:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]

            i += 1
            j -= 1
    return i
def quick_sort (array, start, end):
    if start < end:
        temp = partition(array, start, end)
        quick_sort(array, start, temp - 1)
        quick_sort(array, temp, end)


def merge_sort(mas, start, end):
    if end - start > 1:
        mid = (start + end) // 2
        merge_sort(mas, start, mid)
        merge_sort(mas, mid, end)
        merge(mas, start, mid, end)


def merge(mas, start, mid, end):
    left = mas[start:mid]
    right = mas[mid:end]
    k = start
    i = 0
    j = 0
    while (start + i < mid and mid + j < end):
        if (left[i] <= right[j]):
            mas[k] = left[i]
            i = i + 1
        else:
            mas[k] = right[j]
            j = j + 1
        k = k + 1
    if start + i < mid:
        while k < end:
            mas[k] = left[i]
            i = i + 1
            k = k + 1
    else:
        while k < end:
            mas[k] = right[j]
            j = j + 1
            k = k + 1

df = pd.read_csv('/Users/tanushk1ns/PycharmProjects/labSort/Teachers.csv',on_bad_lines='skip', delimiter=';')

df1 = df[:100]
df1.to_csv("data1.csv")
df1 = pd.read_csv('data1.csv')
#print(df1.head(10))
arr1 = []
for i in range(len(df1)):
    arr1.append(teacher(df1['Teacher Name'][i], df1['Department'][i], df1['Designation'][i], df1['Terminal Degree'][i]))

df2 = df[100:250]
df2.to_csv("data2.csv")
df2 = pd.read_csv('data2.csv')
arr2 = []
for i in range(len(df2)):
    arr2.append(teacher(df2['Teacher Name'][i], df2['Department'][i], df2['Designation'][i], df2['Terminal Degree'][i]))

df3 = df[250:450]
df3.to_csv("data3.csv")
df3 = pd.read_csv('data3.csv')
arr3 = []
for i in range(len(df3)):
    arr3.append(teacher(df3['Teacher Name'][i], df3['Department'][i], df3['Designation'][i], df3['Terminal Degree'][i]))

df4 = df[450:700]
df4.to_csv("data4.csv")
df4 = pd.read_csv('data4.csv')
arr4 = []
for i in range(len(df4)):
    arr4.append(teacher(df4['Teacher Name'][i], df4['Department'][i], df4['Designation'][i], df4['Terminal Degree'][i]))

df5 = df[700:1000]
df5.to_csv("data5.csv")
df5 = pd.read_csv('data5.csv')
arr5 = []
for i in range(len(df5)):
    arr5.append(teacher(df5['Teacher Name'][i], df5['Department'][i], df5['Designation'][i], df5['Terminal Degree'][i]))

df6 = df[1000:1350]
df6.to_csv("data6.csv")
df6 = pd.read_csv('data6.csv')
arr6 = []
for i in range(len(df6)):
    arr6.append(teacher(df6['Teacher Name'][i], df6['Department'][i], df6['Designation'][i], df6['Terminal Degree'][i]))

df7 = df[1350:]
df7.to_csv("data7.csv")
df7 = pd.read_csv('data7.csv')
arr7 = []
for i in range(len(df7)):
    arr7.append(teacher(df7['Teacher Name'][i], df7['Department'][i], df7['Designation'][i], str(df7['Terminal Degree'][i])))

arr = [arr1, arr2, arr3, arr4, arr5, arr6, arr7]

x = [len(el) for el in arr]

# Сортировка пузырьком
arr_bubble = arr.copy()
time_bubble = []
for (i, el_arr) in enumerate(arr_bubble):
    tmp = el_arr[:]
    start = time.time()
    bubble_sort(tmp)
    time_bubble.append(time.time() - start)
    with open(f'bubble_{i+1}.txt', 'w') as f:
        for el in tmp:
            f.write(f'{el.name} {el.department} {el.designation} {el.degree}\n')
print(time_bubble)
plt.plot(x, time_bubble)

# Быстрая сортировка
arr_quick = arr.copy()
time_quick = []
for (i, el_arr) in enumerate(arr_quick):
    tmp = el_arr[:]
    start = time.time()
    quick_sort(tmp,0,len(tmp)-1)
    time_quick.append(time.time() - start)
    with open(f'quick_{i+1}.txt', 'w') as f:
        for el in tmp:
            f.write(f'{el.name} {el.department} {el.designation} {el.degree}\n')
print(time_quick)
plt.plot(x, time_quick)

# Сортировка слиянием
arr_merge = arr.copy()
time_merge = []
for (i, el_arr) in enumerate(arr_merge):
    tmp = el_arr[:]
    start = time.time()
    merge_sort(tmp,0,len(tmp)-1)
    time_merge.append(time.time() - start)
    with open(f'merge_{i+1}.txt', 'w') as f:
        for el in tmp:
            f.write(f'{el.name} {el.department} {el.designation} {el.degree}\n')
print(time_merge)
plt.plot(x, time_merge)

plt.legend(('Bubble', 'Quick', 'Merge'))
plt.show()
