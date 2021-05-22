# Computational Thinking With Algorithms

This repositiory contains an investigation into sorting algorithms and a benchmarked comparison between them.

# Algorithms 

Five sorting algorithms are examined, Bubble, Heap, Counting, Insertion, and Selection sort. These algorithms encompass simple comparison-based sorting(Bubble, Insertion, and Selection), efficient comarison-based sorting(Heap), and  non comparison-based sorting(Counting). A full explanation of each of these algorithms is available in the Jupyter Notebook.

# Benchmarking 

This code will be run 10 times for each test case. The average result of each test case will be appended to an array corresponding to the algorithm used. A python script containing the benchmarking code is saved in the same folder as this notebook.

### Example of benchmark code
```
import time

num_runs = 10 
example = []

# create an array to contain results of test
results = []

for r in range(num_runs):
    # generate a random array to be sorted
    testOne = np.random.randint(100, size=100)
    
    # record start time
    start_time = time.time()
    
    # call sorting algorithm
    bubbleSort(testOne)
    
    # record end time
    end_time = time.time()
    
    # get total running time
    time_elapsed = end_time - start_time
    
    # append running time to array
    results.append(time_elapsed)

# calculate average of 10 runs    
first_test = np.average(results)

# append average to new array which continues benchmark results for all test cases
example.append(first_test)

example
```

# Required Software
[Python](https://www.python.org/downloads/)

## Required Python Packages
- [Matplotlib](https://matplotlib.org/)
- [Pandas](https://pandas.pydata.org/)
- [Numpy](https://numpy.org)
- [Jupyter](https://jupyter.org/install.html)

## References
- https://www.geeksforgeeks.org/bubble-sort/
- https://www.geeksforgeeks.org/counting-sort/
- https://www.geeksforgeeks.org/heap-sort/
- https://www.geeksforgeeks.org/insertion-sort/
- https://www.geeksforgeeks.org/selection-sort/
- https://www.geeksforgeeks.org/sorting-terminology/
- https://www.geeksforgeeks.org/stability-in-sorting-algorithms/
- https://learnonline.gmit.ie/pluginfile.php/191466/mod_resource/content/0/07%20Sorting%20Algorithms%20Part%201.pdf
- https://learnonline.gmit.ie/pluginfile.php/191471/mod_resource/content/0/08%20Sorting%20Algorithms%20Part%202.pdf
- https://learnonline.gmit.ie/pluginfile.php/191472/mod_resource/content/0/09%20Sorting%20Algorithms%20Part%203.pdf
- https://learnonline.gmit.ie/pluginfile.php/191481/mod_resource/content/0/11%20Benchmarking%20in%20Python.pdf
