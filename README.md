# Performance Optimization and Parallel Computing Exercise

## Objective

The goal of this exercise is to evaluate your understanding of performance optimization, parallel computing, and memory management in high-performance computing (HPC). You will need to analyze a given problem, optimize it, and parallelize it to achieve the best possible performance. You will also need to document your process and provide a brief report on the results.

## Problem Statement

You are given a Python program that performs a large-scale simulation of a physical system. The program involves intensive matrix operations, including matrix multiplication, element-wise operations, and solving linear equations. The current implementation is slow and not optimized for running on multi-core systems.

## Part 1: Initial Profiling and Analysis

### Profiling the Code

> - Profile the given code using cProfile or any other profiling tool of your choice to identify the most time-consuming parts of the program
> - Record the functions or parts of the code that are taking the most time
>   When profiling my script these were my results:

```
5376 function calls (5185 primitive calls) in 0.051 seconds

   Ordered by: cumulative time
   List reduced from 291 to 10 due to restriction <10>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.021    0.021    0.051    0.051 /Users/danielkumlin/Desktop/University/high-performance-computing/hw-3/q1.py:6(simulate_physical_system)
        1    0.000    0.000    0.022    0.022 /Users/danielkumlin/.pyenv/versions/hpc-3/lib/python3.12/site-packages/numpy/__init__.py:326(__getattr__)
     25/1    0.000    0.000    0.022    0.022 <frozen importlib._bootstrap>:1349(_find_and_load)
     25/1    0.000    0.000    0.022    0.022 <frozen importlib._bootstrap>:1304(_find_and_load_unlocked)
     24/1    0.000    0.000    0.022    0.022 <frozen importlib._bootstrap>:911(_load_unlocked)
      9/1    0.000    0.000    0.022    0.022 <frozen importlib._bootstrap_external>:989(exec_module)
     65/2    0.000    0.000    0.022    0.011 <frozen importlib._bootstrap>:480(_call_with_frames_removed)
      9/1    0.000    0.000    0.022    0.022 {built-in method builtins.exec}
        1    0.000    0.000    0.022    0.022 /Users/danielkumlin/.pyenv/versions/hpc-3/lib/python3.12/site-packages/numpy/random/__init__.py:1(<module>)
      4/3    0.000    0.000    0.022    0.007 <frozen importlib._bootstrap>:1390(_handle_fromlist)



Detailed information about numpy operations:
   Ordered by: cumulative time
   List reduced from 291 to 1 due to restriction <'dot'>

Function                                                                                                   was called by...
                                                                                                               ncalls  tottime  cumtime
/Users/danielkumlin/.pyenv/versions/hpc-3/lib/python3.12/site-packages/numpy/_core/multiarray.py:757(dot)  <-       1    0.000    0.000  /Users/danielkumlin/Desktop/University/high-performance-computing/hw-3/q1.py:6(simulate_physical_system)


   Ordered by: cumulative time
   List reduced from 291 to 1 due to restriction <'dot'>

Function                                                                                                   called...
                                                                                                               ncalls  tottime  cumtime
/Users/danielkumlin/.pyenv/versions/hpc-3/lib/python3.12/site-packages/numpy/_core/multiarray.py:757(dot)  ->



Sorted by total time:
         5376 function calls (5185 primitive calls) in 0.051 seconds

   Ordered by: internal time
   List reduced from 291 to 10 due to restriction <10>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.021    0.021    0.051    0.051 /Users/danielkumlin/Desktop/University/high-performance-computing/hw-3/q1.py:6(simulate_physical_system)
       15    0.012    0.001    0.012    0.001 {built-in method _imp.create_dynamic}
        1    0.008    0.008    0.008    0.008 /Users/danielkumlin/.pyenv/versions/hpc-3/lib/python3.12/site-packages/numpy/linalg/_linalg.py:320(solve)
     15/6    0.004    0.000    0.017    0.003 {built-in method _imp.exec_dynamic}
        9    0.003    0.000    0.003    0.000 {method 'read' of '_io.BufferedReader' objects}
        9    0.000    0.000    0.000    0.000 {built-in method marshal.loads}
       85    0.000    0.000    0.000    0.000 {built-in method posix.stat}
        9    0.000    0.000    0.000    0.000 {built-in method _io.open_code}
       47    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:1593(find_spec)
       14    0.000    0.000    0.000    0.000 {built-in method builtins.__build_class__}



Stats for numpy operations only:
         5376 function calls (5185 primitive calls) in 0.051 seconds

   Ordered by: internal time
   List reduced from 291 to 28 due to restriction <'numpy'>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.008    0.008    0.008    0.008 /Users/danielkumlin/.pyenv/versions/hpc-3/lib/python3.12/site-packages/numpy/linalg/_linalg.py:320(solve)
        1    0.000    0.000    0.000    0.000 /Users/danielkumlin/.pyenv/versions/hpc-3/lib/python3.12/site-packages/numpy/_core/_ufunc_config.py:465(inner)
        1    0.000    0.000    0.000    0.000 /Users/danielkumlin/.pyenv/versions/hpc-3/lib/python3.12/site-packages/numpy/_core/numeric.py:144(ones)
        1    0.000    0.000    0.022    0.022 /Users/danielkumlin/.pyenv/versions/hpc-3/lib/python3.12/site-packages/numpy/random/__init__.py:1(<module>)
        1    0.000    0.000    0.000    0.000 {built-in method numpy.empty}
        1    0.000    0.000    0.000    0.000 /Users/danielkumlin/.pyenv/versions/hpc-3/lib/python3.12/site-packages/numpy/linalg/_linalg.py:148(_commonType)
        1    0.000    0.000    0.021    0.021 /Users/danielkumlin/.pyenv/versions/hpc-3/lib/python3.12/site-packages/numpy/random/_pickle.py:1(<module>)
        2    0.000    0.000    0.000    0.000 /Users/danielkumlin/.pyenv/versions/hpc-3/lib/python3.12/site-packages/numpy/linalg/_linalg.py:123(_makearray)
        4    0.000    0.000    0.000    0.000 /Users/danielkumlin/.pyenv/versions/hpc-3/lib/python3.12/site-packages/numpy/_core/getlimits.py:692(__init__)
        1    0.000    0.000    0.000    0.000 /Users/danielkumlin/.pyenv/versions/hpc-3/lib/python3.12/site-packages/numpy/_core/_ufunc_config.py:441(__enter__)
        1    0.000    0.000    0.000    0.000 /Users/danielkumlin/.pyenv/versions/hpc-3/lib/python3.12/site-packages/numpy/linalg/_linalg.py:198(_assert_stacked_square)
        1    0.000    0.000    0.022    0.022 /Users/danielkumlin/.pyenv/versions/hpc-3/lib/python3.12/site-packages/numpy/__init__.py:326(__getattr__)
        4    0.000    0.000    0.000    0.000 /Users/danielkumlin/.pyenv/versions/hpc-3/lib/python3.12/site-packages/numpy/_core/getlimits.py:716(max)
        2    0.000    0.000    0.000    0.000 {built-in method numpy._core._multiarray_umath._make_extobj}
        1    0.000    0.000    0.000    0.000 /Users/danielkumlin/.pyenv/versions/hpc-3/lib/python3.12/site-packages/numpy/_core/_ufunc_config.py:460(__call__)
        1    0.000    0.000    0.000    0.000 /Users/danielkumlin/.pyenv/versions/hpc-3/lib/python3.12/site-packages/numpy/linalg/_linalg.py:192(_assert_stacked_2d)
        1    0.000    0.000    0.000    0.000 {method 'astype' of 'numpy.ndarray' objects}
        2    0.000    0.000    0.000    0.000 /Users/danielkumlin/.pyenv/versions/hpc-3/lib/python3.12/site-packages/numpy/linalg/_linalg.py:142(_realType)
        1    0.000    0.000    0.000    0.000 /Users/danielkumlin/.pyenv/versions/hpc-3/lib/python3.12/site-packages/numpy/_core/_ufunc_config.py:457(__exit__)
        2    0.000    0.000    0.000    0.000 {built-in method numpy.asarray}
        3    0.000    0.000    0.000    0.000 /Users/danielkumlin/.pyenv/versions/hpc-3/lib/python3.12/site-packages/numpy/linalg/_linalg.py:128(isComplexType)
        1    0.000    0.000    0.000    0.000 {method '__array_wrap__' of 'numpy.ndarray' objects}
        2    0.000    0.000    0.000    0.000 /Users/danielkumlin/.pyenv/versions/hpc-3/lib/python3.12/site-packages/numpy/_core/_ufunc_config.py:431(__init__)
        1    0.000    0.000    0.000    0.000 /Users/danielkumlin/.pyenv/versions/hpc-3/lib/python3.12/site-packages/numpy/_core/multiarray.py:1101(copyto)
        1    0.000    0.000    0.000    0.000 /Users/danielkumlin/.pyenv/versions/hpc-3/lib/python3.12/site-packages/numpy/_core/multiarray.py:161(concatenate)
        1    0.000    0.000    0.000    0.000 /Users/danielkumlin/.pyenv/versions/hpc-3/lib/python3.12/site-packages/numpy/_pytesttester.py:75(__init__)
        1    0.000    0.000    0.000    0.000 /Users/danielkumlin/.pyenv/versions/hpc-3/lib/python3.12/site-packages/numpy/linalg/_linalg.py:316(_solve_dispatcher)
        1    0.000    0.000    0.000    0.000 /Users/danielkumlin/.pyenv/versions/hpc-3/lib/python3.12/site-packages/numpy/_core/multiarray.py:757(dot)
```

Total execution time: 0.051 seconds with 5376 function calls

The Most time-consuming operations (sorted by cumulative time):

- `simulate_physical_system`: 0.021s total time (main function)
- `numpy.__getattr__`: 0.022s cumulative time
- `numpy.linalg.solve`: 0.008s total time
- Various import operations taking the rest of the time

The fact that `numpy.__getattr__` and imports are taking significant time suggests this is the first run where Python is loading the NumPy modules.

### Memory Usage Analysis

> - Analyze the memory usage of the program. Identify any inefficiencies in memory usage, such as redundant data storage, large temporary arrays, or inefficient memory access patterns

When analysing the memory I used the `memory_profiler` package and got the following result:

| Line # | Mem usage | Increment | Occurrences | Line Contents                      |
| ------ | --------- | --------- | ----------- | ---------------------------------- |
| 7      | 30.0 MiB  | 30.0 MiB  | 1           | @profile                           |
| 8      |           |           |             | def simulate_physical_system(n):   |
| 9      |           |           |             | # Create input matrices            |
| 10     | 42.0 MiB  | 12.1 MiB  | 1           | A = np.random.rand(n, n)           |
| 11     | 49.7 MiB  | 7.6 MiB   | 1           | B = np.random.rand(n, n)           |
| 12     | 57.3 MiB  | 7.6 MiB   | 1           | C = np.random.rand(n, n)           |
| 13     |           |           |             |                                    |
| 14     |           |           |             | # Perform matrix multiplication    |
| 15     | 73.1 MiB  | 15.8 MiB  | 1           | D = np.dot(A, B)                   |
| 16     |           |           |             |                                    |
| 17     |           |           |             | # Element-wise operations          |
| 18     | 80.7 MiB  | 7.6 MiB   | 1           | E = D \* C                         |
| 19     |           |           |             |                                    |
| 20     |           |           |             | # Solve a linear system            |
| 21     | 88.5 MiB  | 7.8 MiB   | 1           | x = np.linalg.solve(E, np.ones(n)) |
| 22     | 88.5 MiB  | 0.0 MiB   | 1           | return x                           |

Looking at the memory profiling results, the following can be inferred:

Memory Usage Analysis:

1. Initial Memory Allocation (Lines 9-12):

- Starting memory: 30.0 MiB (baseline)
- Matrix A takes 12.1 MiB
- Matrices B and C each take 7.6 MiB
- Each new matrix allocation adds significant memory overhead

2. Matrix Multiplication (Line 15):

- Creates temporary array D requiring 15.8 MiB
- Largest single memory increase in the program
- Represents temporary storage that could potentially be optimized

3. Element-wise Operations (Line 18):

- Creates another temporary array E using 7.6 MiB
- Additional memory allocation for intermediate result

4. Linear System Solution (Line 21):

- Final memory increase of 7.8 MiB
- Total program memory reaches 88.5 MiB

Identified Inefficiencies:

1. Redundant Data Storage:

- Multiple temporary arrays (D and E) storing intermediate results
- Each operation creates new memory allocations

2. Large Temporary Arrays:

- Matrix multiplication result (D) creates large temporary storage
- Element-wise multiplication result (E) creates another large array

3. Memory Access Patterns:

- Sequential creation of matrices might affect memory locality
- No indication of memory layout optimization (contiguous vs non-contiguous)

4. Data Type Usage:

- Default data type might be using more memory than necessary
- No explicit control over precision requirements

This analysis points to several areas where memory usage could be optimized. Would you like me to focus on any specific aspect of the analysis?

## Part 2: Optimization

### Code Optimization

> - Optimize the identified bottlenecks. You may consider:
>   - Using high-performance libraries like NumPy, SciPy, or BLAS for matrix operations
>   - Refactoring code to reduce unnecessary computations or memory usage
>   - Improving memory access patterns to reduce cache misses

1. Memory Layout: Used `ascontiguousarray` for contiguous memory blocks

   - Improves cache utilization
   - Reduces cache misses
   - Optimizes BLAS operations

2. BLAS Integration: Leveraged NumPy's automatic BLAS/LAPACK implementation

   - Hardware-optimized matrix operations
   - Efficient memory handling

3. Data Types: Explicit `dtype=np.float64` specification
   - Consistent precision
   - Avoids type conversions

### Memory Management

> - Optimize the memory usage by eliminating unnecessary memory allocations, using views instead of copies where possible, and reducing the memory footprint of large data structures

To optimise the memory I used the following techniques

1. Single Memory Block

   - `data = np.random.rand(3, n, n)`: One allocation instead of three
   - Views (A, B, C) share memory with `data`

2. In-place Operations

   - `np.dot(..., out=A)`: Reuses A's memory
   - `A *= C`: In-place element-wise multiplication
   - Eliminates D and E temporary arrays

3. Memory Reduction
   - Reduced from 6 arrays to 2 main arrays (data and x)
   - Uses views instead of copies
   - Minimizes temporary allocations

## Part 3: Parallelization

### Parallelizing the Code

> - Parallelize the most computationally expensive parts of the code using either Python's multiprocessing module or OpenMP in C/C++ (if applicable). If you choose to use Python, consider using mpi4py or Joblib for parallelism
> - Ensure that the parallel implementation is efficient and scales well with the number of cores or processes

The following parallelising techinques were used:

1. BLAS/LAPACK Level

   - Utilizes built-in parallel implementations
   - Optimized for matrix operations

2. Data-Level Parallelism

   - Splits input into chunks
   - Processes chunks concurrently
   - Combines results

3. Resource Utilization
   - Uses available CPU cores
   - Balanced workload distribution
   - Minimizes communication overhead

### Handling Race Conditions and Synchronization

> - If your parallel code involves shared resources or data, ensure that you handle synchronization issues such as race conditions. Use appropriate locking mechanisms or atomic operations to prevent these issues

Race conditions are prevented by:

1. Random State Isolation

   - Separate `RandomState` per process
   - Seed-based initialization

2. Resource Protection

   - Lock for shared operations
   - Local memory allocation
   - Controlled result combination

3. Thread Safety
   - Independent process execution
   - Synchronized critical sections
   - Atomic operations for data combination

## Part 4: Testing and Reporting

### Testing

> - Test the optimized and parallelized code on different input sizes and record the performance improvements. Ensure that the output remains correct and consistent with the original implementation

### Documentation and Report

> - Write a brief report (1-2 pages) that includes:
>   - A summary of your profiling results
>   - A description of the optimizations you applied and why you chose them
>   - An explanation of your parallelization strategy and any challenges you faced
>   - Performance metrics before and after optimization, including execution time and memory usage
>   - A discussion on the scalability of your solution

## Deliverables

> - **Optimized and Parallelized Code**: Submit the final version of your Python (or C/C++) code, with comments explaining the changes you made
> - **Profiling Output**: Submit the output from the profiling tool showing the original and optimized performance
> - **Report**: Submit a brief report summarizing your approach, optimizations, parallelization, and results

## Evaluation Criteria

> - **Correctness (20%)**: Does the optimized and parallelized code produce correct results?
> - **Performance Improvement (30%)**: How much did the performance improve after optimization and parallelization?
> - **Code Quality (20%)**: Is the code well-organized, properly commented, and free of race conditions or other parallel programming issues?
> - **Scalability (10%)**: Does the parallelized code scale well with the number of cores or processes?
> - **Report Quality (20%)**: Is the report clear, well-organized, and does it adequately explain the steps taken and the results obtained?
