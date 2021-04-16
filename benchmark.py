# imported necessary python libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time

# defined bubble sort function 
def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr

# defined heapify function
def heapify(arr, n, i): 
    largest = i 
    left = 2 * i + 1     
    right = 2 * i + 2     
  
    
    if left < n and arr[i] < arr[left]: 
        largest = left 
  
    
    if right < n and arr[largest] < arr[right]: 
        largest = right 
  
    
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i]   
  
         
        heapify(arr, n, largest) 

# defined heap sort function         
def heapSort(arr): 
    n = len(arr) 
   
    for i in range(n, -1, -1): 
        heapify(arr, n, i) 
        
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    
    return arr

# defined count sort function    
def countSort(arr):
    m = len(arr) + 1
    count = [0 for i in range(m)]
    
    for a in arr:
    # count occurences
        count[a] += 1             
    i = 0
    for a in range(m):            
        for c in range(count[a]):  
            arr[i] = a
            i += 1
    return arr
    
# defined insertion sort function    
def insertionSort(arr): 
  
    for i in range(1, len(arr)): 
  
        key = arr[i] 
   
        j = i-1
        while j >= 0 and key < arr[j] : 
                arr[j + 1] = arr[j] 
                j -= 1
        arr[j + 1] = key 
        
    return arr

# defined selection sort function    
def selectSort(arr):
    n = len(arr)
    
    for i in range(n):
        
        min_index = i
        
        for j in range(i+1, n):
            
            if arr[j] < arr[min_index]:
                min_index = j
        
        arr[i], arr[min_index] = arr[min_index], arr[i]
        
    return arr




# created empty pandas DataFrame
columnNames = ['Input Size', 'Bubble Sort', 'Insertion Sort', 'Counting Sort', 'Heap Sort', 'Selection Sort']
d = {'Input Size': [100, 250, 500, 750, 1000, 1250, 2500, 3750, 5000, 6250]}
df = pd.DataFrame(d, columns = columnNames).set_index('Input Size')




# bubble sort benchmarking
bub_sort = []
num_runs = 10 
results = []
# n = 100
for r in range(num_runs):
    testOne = np.random.randint(100, size=100)
    
    start_time = time.time()
    
    bubbleSort(testOne)
    
    end_time = time.time()
    
    time_elapsed = end_time - start_time
    
    results.append(time_elapsed)
    
firstRun = np.average(results)
bub_sort.append(firstRun)


results = []

# n = 250
for r in range(num_runs):
    
    testTwo = np.random.randint(250, size=250)
    
    start_time = time.time()
    
    bubbleSort(testTwo)
    
    end_time = time.time()
    
    time_elapsed = end_time - start_time
    
    results.append(time_elapsed)
    
secondRun = np.average(results)
bub_sort.append(secondRun)


results = []
# n = 500
for r in range(num_runs):
    
    testThree = np.random.randint(500, size=500)
    
    start_time = time.time()
    
    bubbleSort(testThree)
    
    end_time = time.time()
    
    time_elapsed = end_time - start_time
    
    results.append(time_elapsed)
    
thirdRun = np.average(results)
bub_sort.append(thirdRun)


results = []
# n = 750
for r in range(num_runs):
    
    testFour = np.random.randint(750, size=750)
    
    start_time = time.time()
    
    bubbleSort(testFour)
    
    end_time = time.time()
    
    time_elapsed = end_time - start_time
    
    results.append(time_elapsed)
    
fourthRun = np.average(results)
bub_sort.append(fourthRun)

results = []
# n = 1000
for r in range(num_runs):
    
    testFive = np.random.randint(1000, size=1000)
    
    start_time = time.time()
    
    bubbleSort(testFive)
    
    end_time = time.time()
    
    time_elapsed = end_time - start_time
    
    results.append(time_elapsed)
    
fifthRun = np.average(results)
bub_sort.append(fifthRun)


results = []
# n = 1250 
for r in range(num_runs):
    
    testSix = np.random.randint(1250, size=1250)
    
    start_time = time.time()

    bubbleSort(testSix)
    
    end_time = time.time()
    
    time_elapsed = end_time - start_time
    
    results.append(time_elapsed)
    
sixthRun = np.average(results)
bub_sort.append(sixthRun)

results = []
# n = 2500
for r in range(num_runs):
    
    testSeven = np.random.randint(2500, size=2500)
    
    start_time = time.time()

    bubbleSort(testSeven)
    
    end_time = time.time()
    
    time_elapsed = end_time - start_time
    
    results.append(time_elapsed)
    
seventhRun = np.average(results)
bub_sort.append(seventhRun)


results = []
# n = 3750
for r in range(num_runs):
    
    testEight = np.random.randint(3750, size=3750)
    
    start_time = time.time()
    
    bubbleSort(testEight)
    
    end_time = time.time()
    
    time_elapsed = end_time - start_time
    
    results.append(time_elapsed)
    
eighthRun = np.average(results)
bub_sort.append(eighthRun)

results= []
# n = 5000
for r in range(num_runs):
    
    testNine = np.random.randint(5000, size=5000)
    
    start_time = time.time()
    
    bubbleSort(testNine)
    
    end_time = time.time()
    
    time_elapsed = end_time - start_time
    
    results.append(time_elapsed)
    
ninthRun = np.average(results)
bub_sort.append(ninthRun)

results = []
# n = 6250 
for r in range(num_runs):
    
    testTen = np.random.randint(6250, size=6250)
    
    start_time = time.time()

    bubbleSort(testTen)
    
    end_time = time.time()
    
    time_elapsed = end_time - start_time
    
    results.append(time_elapsed)
    
tenthRun = np.average(results)
bub_sort.append(tenthRun)




# insertion sort benchmarking
insert_sort = []
num_runs = 10 

results = []
# n = 100
for r in range(num_runs):
    
    testOne = np.random.randint(100, size=100)
    
    start_time = time.time()
    
    insertionSort(testOne)
    
    end_time = time.time()
    
    time_elapsed = end_time - start_time
    
    results.append(time_elapsed)
    
firstRun = np.average(results)
insert_sort.append(firstRun)

results =[]
# n = 250
for r in range(num_runs):
    
    testTwo = np.random.randint(250, size=250)
    
    start_time = time.time()
    
    insertionSort(testTwo)
    
    end_time = time.time()
    
    time_elapsed = end_time - start_time
    
    results.append(time_elapsed)
    
secondRun = np.average(results)
insert_sort.append(secondRun)

results =[]
# n = 500
for r in range(num_runs):
    
    testThree = np.random.randint(500, size=500)
    
    start_time = time.time()
    
    insertionSort(testThree)
    
    end_time = time.time()
    
    time_elapsed = end_time - start_time
    
    results.append(time_elapsed)
    
thirdRun = np.average(results)
insert_sort.append(thirdRun)

results = []
# n = 750
for r in range(num_runs):
    
    testFour = np.random.randint(750, size=750)
    
    start_time = time.time()
    
    insertionSort(testFour)
    
    end_time = time.time()
    
    time_elapsed = end_time - start_time
    
    results.append(time_elapsed)
    
fourthRun = np.average(results)
insert_sort.append(fourthRun)

results = []
# n = 1000
for r in range(num_runs):
    
    testFive = np.random.randint(1000, size=1000)
    
    start_time = time.time()
    
    insertionSort(testFive)
    
    end_time = time.time()
    
    time_elapsed = end_time - start_time
    
    results.append(time_elapsed)
    
fifthRun = np.average(results)
insert_sort.append(fifthRun)

results = []
# n = 1250 
for r in range(num_runs):
    
    testSix = np.random.randint(1250, size=1250)
    
    start_time = time.time()

    insertionSort(testSix)
    
    end_time = time.time()
    
    time_elapsed = end_time - start_time
    
    results.append(time_elapsed)
    
sixthRun = np.average(results)
insert_sort.append(sixthRun)

results = []
# n = 2500
for r in range(num_runs):
    
    testSeven = np.random.randint(2500, size=2500)
    
    start_time = time.time()

    insertionSort(testSeven)
    
    end_time = time.time()
    
    time_elapsed = end_time - start_time
    
    results.append(time_elapsed)
    
seventhRun = np.average(results)
insert_sort.append(seventhRun)

results = []
# n = 3750
for r in range(num_runs):
    
    testEight = np.random.randint(3750, size=3750)
    
    start_time = time.time()
    
    insertionSort(testEight)
    
    end_time = time.time()
    
    time_elapsed = end_time - start_time
    
    results.append(time_elapsed)
    
eighthRun = np.average(results)
insert_sort.append(eighthRun)

results =[]
# n = 5000
for r in range(num_runs):
    
    testNine = np.random.randint(5000, size=5000)
    
    start_time = time.time()
    
    insertionSort(testNine)
    
    end_time = time.time()
    
    time_elapsed = end_time - start_time
    
    results.append(time_elapsed)
    
ninthRun = np.average(results)
insert_sort.append(ninthRun)

results = []
# n = 6250 
for r in range(num_runs):
    
    testTen = np.random.randint(6250, size=6250)
    
    start_time = time.time()

    insertionSort(testTen)
    
    end_time = time.time()
    
    time_elapsed = end_time - start_time
    
    results.append(time_elapsed)
    
tenthRun = np.average(results)
insert_sort.append(tenthRun)




# counting sort benchmarking
count_sort = []
num_runs = 10 

results = [] 
# n = 100
for r in range(num_runs):
    
    testOne = np.random.randint(100, size=100)
    
    start_time = time.time()
    
    countSort(testOne)
    
    end_time = time.time()
    
    time_elapsed = end_time - start_time
    
    results.append(time_elapsed)
    
firstRun = np.average(results)
count_sort.append(firstRun)

results = []
# n = 250
for r in range(num_runs):
    
    testTwo = np.random.randint(250, size=250)
    
    start_time = time.time()
    
    countSort(testTwo)
    
    end_time = time.time()
    
    time_elapsed = end_time - start_time
    
    results.append(time_elapsed)
    
secondRun = np.average(results)
count_sort.append(secondRun)

results = []
# n = 500
for r in range(num_runs):
    
    testThree = np.random.randint(500, size=500)
    
    start_time = time.time()
    
    countSort(testThree)
    
    end_time = time.time()
    
    time_elapsed = end_time - start_time
    
    results.append(time_elapsed)
    
thirdRun = np.average(results)
count_sort.append(thirdRun)

results = []
# n = 750
for r in range(num_runs):
    
    testFour = np.random.randint(750, size=750)
    
    start_time = time.time()
    
    countSort(testFour)
    
    end_time = time.time()
    
    time_elapsed = end_time - start_time
    
    results.append(time_elapsed)
    
fourthRun = np.average(results)
count_sort.append(fourthRun)

results = []
# n = 1000
for r in range(num_runs):
    
    testFive = np.random.randint(1000, size=1000)
    
    start_time = time.time()
    
    countSort(testFive)
    
    end_time = time.time()
    
    time_elapsed = end_time - start_time
    
    results.append(time_elapsed)
    
fifthRun = np.average(results)
count_sort.append(fifthRun)

results = []
# n = 1250 
for r in range(num_runs):
    
    testSix = np.random.randint(1250, size=1250)
    
    start_time = time.time()

    countSort(testSix)
    
    end_time = time.time()
    
    time_elapsed = end_time - start_time
    
    results.append(time_elapsed)
    
sixthRun = np.average(results)
count_sort.append(sixthRun)

results = []
# n = 2500
for r in range(num_runs):
    
    testSeven = np.random.randint(2500, size=2500)
    
    start_time = time.time()

    countSort(testSeven)
    
    end_time = time.time()
    
    time_elapsed = end_time - start_time
    
    results.append(time_elapsed)
    
seventhRun = np.average(results)
count_sort.append(seventhRun)

results = []
# n = 3750
for r in range(num_runs):
    
    testEight = np.random.randint(3750, size=3750)
    
    start_time = time.time()
    
    countSort(testEight)
    
    end_time = time.time()
    
    time_elapsed = end_time - start_time
    
    results.append(time_elapsed)
    
eighthRun = np.average(results)
count_sort.append(eighthRun)

results = []
# n = 5000
for r in range(num_runs):
    
    testNine = np.random.randint(5000, size=5000)
    
    start_time = time.time()
    
    countSort(testNine)
    
    end_time = time.time()
    
    time_elapsed = end_time - start_time
    
    results.append(time_elapsed)
    
ninthRun = np.average(results)
count_sort.append(ninthRun)

results = []
# n = 6250 
for r in range(num_runs):
    
    testTen = np.random.randint(6250, size=6250)
    
    start_time = time.time()

    countSort(testTen)
    
    end_time = time.time()
    
    time_elapsed = end_time - start_time
    
    results.append(time_elapsed)
    
tenthRun = np.average(results)
count_sort.append(tenthRun)




# heap sort benchmarking
heap_sort = []
num_runs = 10 

results = []
# n = 100
for r in range(num_runs):
    
    testOne = np.random.randint(100, size=100)
    
    start_time = time.time()
    
    heapSort(testOne)
    
    end_time = time.time()
    
    time_elapsed = end_time - start_time
    
    results.append(time_elapsed)
    
firstRun = np.average(results)
heap_sort.append(firstRun)

results = []
# n = 250
for r in range(num_runs):
    
    testTwo = np.random.randint(250, size=250)
    
    start_time = time.time()
    
    heapSort(testTwo)
    
    end_time = time.time()
    
    time_elapsed = end_time - start_time
    
    results.append(time_elapsed)
    
secondRun = np.average(results)
heap_sort.append(secondRun)

results = []
# n = 500
for r in range(num_runs):
    
    testThree = np.random.randint(500, size=500)
    
    start_time = time.time()
    
    heapSort(testThree)
    
    end_time = time.time()
    
    time_elapsed = end_time - start_time
    
    results.append(time_elapsed)
    
thirdRun = np.average(results)
heap_sort.append(thirdRun)

results = []
# n = 750
for r in range(num_runs):
    
    testFour = np.random.randint(750, size=750)
    
    start_time = time.time()
    
    heapSort(testFour)
    
    end_time = time.time()
    
    time_elapsed = end_time - start_time
    
    results.append(time_elapsed)
    
fourthRun = np.average(results)
heap_sort.append(fourthRun)

results = []
# n = 1000
for r in range(num_runs):
    
    testFive = np.random.randint(1000, size=1000)
    
    start_time = time.time()
    
    heapSort(testFive)
    
    end_time = time.time()
    
    time_elapsed = end_time - start_time
    
    results.append(time_elapsed)
    
fifthRun = np.average(results)
heap_sort.append(fifthRun)

results = []
# n = 1250 
for r in range(num_runs):
    
    testSix = np.random.randint(1250, size=1250)
    
    start_time = time.time()

    heapSort(testSix)
    
    end_time = time.time()
    
    time_elapsed = end_time - start_time
    
    results.append(time_elapsed)
    
sixthRun = np.average(results)
heap_sort.append(sixthRun)

results = []
# n = 2500
for r in range(num_runs):
    
    testSeven = np.random.randint(2500, size=2500)
    
    start_time = time.time()

    heapSort(testSeven)
    
    end_time = time.time()
    
    time_elapsed = end_time - start_time
    
    results.append(time_elapsed)
    
seventhRun = np.average(results)
heap_sort.append(seventhRun)

results = [] 
# n = 3750
for r in range(num_runs):
    
    testEight = np.random.randint(3750, size=3750)
    
    start_time = time.time()
    
    heapSort(testEight)
    
    end_time = time.time()
    
    time_elapsed = end_time - start_time
    
    results.append(time_elapsed)
    
eighthRun = np.average(results)
heap_sort.append(eighthRun)

results = []
# n = 5000
for r in range(num_runs):
    
    testNine = np.random.randint(5000, size=5000)
    
    start_time = time.time()
    
    heapSort(testNine)
    
    end_time = time.time()
    
    time_elapsed = end_time - start_time
    
    results.append(time_elapsed)
    
ninthRun = np.average(results)
heap_sort.append(ninthRun)

results = []
# n = 6250 
for r in range(num_runs):
    
    testTen = np.random.randint(6250, size=6250)
    
    start_time = time.time()

    heapSort(testTen)
    
    end_time = time.time()
    
    time_elapsed = end_time - start_time
    
    results.append(time_elapsed)
    
tenthRun = np.average(results)
heap_sort.append(tenthRun)




# selection sort benchmarking 
select_sort = []

num_runs = 10 

results = []
# n = 100
for r in range(num_runs):
    
    testOne = np.random.randint(100, size=100)
    
    start_time = time.time()

    selectSort(testOne)
    
    end_time = time.time()
    
    time_elapsed = end_time - start_time
    
    results.append(time_elapsed)
    
firstRun = np.average(results)
select_sort.append(firstRun)

results = [] 
# n = 250
for r in range(num_runs):
    
    testTwo = np.random.randint(250, size=250)
    
    start_time = time.time()

    selectSort(testTwo)
    
    end_time = time.time()
    
    time_elapsed = end_time - start_time
    
    results.append(time_elapsed)
    
secondRun = np.average(results)
select_sort.append(secondRun)

results = []
# n = 500
for r in range(num_runs):
    
    testThree = np.random.randint(500, size=500)
    
    start_time = time.time()

    selectSort(testThree)
    
    end_time = time.time()
    
    time_elapsed = end_time - start_time
    
    results.append(time_elapsed)
    
thirdRun = np.average(results)
select_sort.append(thirdRun)

results = []
# n = 750 
for r in range(num_runs):
    
    testFour = np.random.randint(750, size=750)
    
    start_time = time.time()

    selectSort(testFour)
    
    end_time = time.time()
    
    time_elapsed = end_time - start_time
    
    results.append(time_elapsed)
    
fourthRun = np.average(results)
select_sort.append(fourthRun)

results = []
# n = 1000 
for r in range(num_runs):
    
    testFive = np.random.randint(1000, size=1000)
    
    start_time = time.time()

    selectSort(testFive)
    
    end_time = time.time()
    
    time_elapsed = end_time - start_time
    
    results.append(time_elapsed)
    
fifthRun = np.average(results)
select_sort.append(fifthRun)

results = []
# n = 1250
for r in range(num_runs):
    
    testSix = np.random.randint(1250, size=1250)
    
    start_time = time.time()

    selectSort(testSix)
    
    end_time = time.time()
    
    time_elapsed = end_time - start_time
    
    results.append(time_elapsed)
    
sixthRun = np.average(results)
select_sort.append(sixthRun)

results = []
# n = 2500
for r in range(num_runs):
    
    testSeven = np.random.randint(2500, size=2500)
    
    start_time = time.time()

    selectSort(testSeven)
    
    end_time = time.time()
    
    time_elapsed = end_time - start_time
    
    results.append(time_elapsed)
    
seventhRun = np.average(results)
select_sort.append(seventhRun)

results = []
# n = 3750
for r in range(num_runs):
    
    testEight = np.random.randint(3750, size=3750)
    
    start_time = time.time()

    selectSort(testEight)
    
    end_time = time.time()
    
    time_elapsed = end_time - start_time
    
    results.append(time_elapsed)
    
eighthRun = np.average(results)
select_sort.append(eighthRun)

results = []
# n = 5000
for r in range(num_runs):
    
    testNine = np.random.randint(5000, size=5000)
    
    start_time = time.time()

    selectSort(testNine)
    
    end_time = time.time()
    
    time_elapsed = end_time - start_time
    
    results.append(time_elapsed)
    
ninthRun = np.average(results)
select_sort.append(ninthRun)


results = []
# n = 6250
for r in range(num_runs):
    
    testTen = np.random.randint(6250, size=6250)
    
    start_time = time.time()

    selectSort(testTen)
    
    end_time = time.time()
    
    time_elapsed = end_time - start_time
    
    results.append(time_elapsed)
    
tenthRun = np.average(results)
select_sort.append(tenthRun)




# set decimal places to 5
bub_sort = np.around(bub_sort, 5)
insert_sort = np.around(insert_sort, 5)
count_sort = np.around(count_sort, 5)
heap_sort = np.around(heap_sort, 5)
select_sort = np.around(select_sort, 5)

# added bubble sort results to pandas datadrame 
df['Bubble Sort'] = bub_sort
df['Insertion Sort'] = insert_sort
df['Counting Sort'] = count_sort
df['Heap Sort'] = heap_sort
df['Selection Sort'] = select_sort