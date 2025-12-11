# Course: Slides

## Lecture: output\algorithm_design\page_001\algorithm_design_page_001\auto

# Parallel Programming

Principles of Parallel Algorithm Design

Slides adapted from the lecture notes of the text “Introduction to Parallel Computing”.

---

## Lecture: output\algorithm_design\page_002\algorithm_design_page_002\auto

# Overview

• Tools for Parallel Algorithm Design • Decomposition Techniques • Task Generation and Interactions • Mapping Techniques • Parallel Algorithm Design Models

---

## Lecture: output\algorithm_design\page_003\algorithm_design_page_003\auto

# Dependency Graphs

The first step in developing a parallel algorithm is to decompose the problem into tasks that can be executed concurrently

• A given problem may be decomposed into tasks in many different ways.

• Tasks may be of the same or different sizes.

A decomposition can be illustrated in the form of a directed graph with nodes corresponding to tasks and edges indicating that the result of one task is required for processing the other. Such a graph is called a task dependency graph.

---

## Lecture: output\algorithm_design\page_004\algorithm_design_page_004\auto

# Example: Multiplying a Dense Matrix with a Vector

![](images/4236e9c898927e4a7e14c37f9b410725419daccc7c290cc3ba02ce29cff5b0cd.jpg)

Computation of each element of output vector y is independent of other elements. Based on this, a dense matrix-vector product can be decomposed into n tasks. The figure highlights the portion of the matrix and vector accessed by Task 1.

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\algorithm_design\page_004\algorithm_design_page_004\auto\images\4236e9c898927e4a7e14c37f9b410725419daccc7c290cc3ba02ce29cff5b0cd.jpg

---

## Lecture: output\algorithm_design\page_005\algorithm_design_page_005\auto

# Example: Database Query Processing Consider the execution of the query:

MODEL = \`\`CIVIC'' AND YEAR = 2001 AND (COLOR = \`\`GREEN'' OR COLOR $=$ \`\`WHITE)

on the following database:   

<table><tr><td>ID# Model</td><td></td><td>Year</td><td>Color</td><td>Dealer</td><td>Price</td></tr><tr><td>4523</td><td>Civic</td><td>2002</td><td>Blue</td><td>MN</td><td>$18,000</td></tr><tr><td>3476</td><td>Corolla</td><td>1999</td><td>White</td><td>IL</td><td>$15,000</td></tr><tr><td>7623</td><td>Camry</td><td>2001</td><td>Green</td><td>NY</td><td>$21,000</td></tr><tr><td>9834</td><td>Prius</td><td>2001</td><td>Green</td><td>CA</td><td>$18,000</td></tr><tr><td>6734</td><td>Civic</td><td>2001</td><td>White</td><td>OR</td><td>$17,000</td></tr><tr><td>5342</td><td>Altima</td><td>2001</td><td>Green</td><td>FL</td><td>$19,000</td></tr><tr><td>3845</td><td>Maxima</td><td>2001</td><td>Blue</td><td>NY</td><td>$22,000</td></tr><tr><td>8354</td><td>Accord</td><td>2000</td><td>Green</td><td>VT</td><td>$18,000</td></tr><tr><td>4395</td><td>Civic</td><td>2001</td><td>Red</td><td>CA</td><td>$17,000</td></tr><tr><td>7352</td><td>Civic</td><td>2002</td><td>Red</td><td>WA</td><td>$18,000</td></tr></table>

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\algorithm_design\page_005\algorithm_design_page_005\auto\images\b074c0fe20a8cf27c4f5b3d78baf478f0680e196ab013aad09f6a810a69b7114.jpg

---

## Lecture: output\algorithm_design\page_006\algorithm_design_page_006\auto

# Example: Database Query Processing

The execution of the query can be divided into subtasks in various ways. Each task can be thought of as generating an intermediate table of entries that satisfy a particular clause.

<table><tr><td>ID#</td><td>Model</td></tr><tr><td>4523 6734</td><td>Civic Civic</td></tr><tr><td>4395</td><td>Civic</td></tr><tr><td>7352</td><td>Civic</td></tr></table>

<table><tr><td rowspan=1 colspan=1>ID#</td><td rowspan=1 colspan=1>Year</td></tr><tr><td rowspan=1 colspan=1>76236734</td><td rowspan=3 colspan=1>20012001200120012001</td></tr><tr><td rowspan=1 colspan=1>5342</td></tr><tr><td rowspan=1 colspan=1>38454395</td></tr></table>

<table><tr><td>ID#</td><td>Color</td></tr><tr><td>3476 6734</td><td>White White</td></tr></table>

<table><tr><td>ID#</td><td>Color</td></tr><tr><td>7623 9834 5342</td><td>Green Green Green</td></tr></table>

![](images/031b8aa6343e58cd64487bd64685f447ce63e2a2c059be6a194d199c1ad90789.jpg)

<table><tr><td rowspan=1 colspan=1>ID#</td><td rowspan=1 colspan=1>Color</td></tr><tr><td rowspan=1 colspan=1>34767623</td><td rowspan=1 colspan=1>WhiteGreen</td></tr><tr><td rowspan=1 colspan=1>9834</td><td rowspan=1 colspan=1>Green</td></tr><tr><td rowspan=1 colspan=1>6734</td><td rowspan=3 colspan=1>WhiteGreenGreen</td></tr><tr><td rowspan=1 colspan=1>5342</td></tr><tr><td rowspan=1 colspan=1>8354</td></tr></table>

<table><tr><td rowspan=1 colspan=1>ID#</td><td rowspan=1 colspan=1>Model</td><td rowspan=1 colspan=1>Year</td><td rowspan=1 colspan=1>Color</td></tr><tr><td rowspan=1 colspan=1>6734</td><td rowspan=1 colspan=1>Civic</td><td rowspan=1 colspan=1>2001</td><td rowspan=1 colspan=1>White</td></tr></table>

Decomposing the given query into a number of tasks. Edges in this graph denote that the output of one task is needed to accomplish the next.

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\algorithm_design\page_006\algorithm_design_page_006\auto\images\031b8aa6343e58cd64487bd64685f447ce63e2a2c059be6a194d199c1ad90789.jpg
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\algorithm_design\page_006\algorithm_design_page_006\auto\images\31e2918c48b1cf0f33599a9a02a69d44f64e41affef237010c82cb2e63277c35.jpg
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\algorithm_design\page_006\algorithm_design_page_006\auto\images\3b8d43dfa7c9243a7837abdb0e08159d563e34a67e45332f7ea0b6601a34da04.jpg
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\algorithm_design\page_006\algorithm_design_page_006\auto\images\7f993b2741921ad49d4ff89751cf59c59007496c16a62ef9c952b3c2618e06af.jpg
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\algorithm_design\page_006\algorithm_design_page_006\auto\images\b29ee2b69a9761148aa5b089b5259d3cb728707d07f04dab97dfe6a0785d24dd.jpg
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\algorithm_design\page_006\algorithm_design_page_006\auto\images\c544cc74cf1945ce8be3a9719f4529f39656a207865de4c3b48bea47c9f954f9.jpg
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\algorithm_design\page_006\algorithm_design_page_006\auto\images\f1989778e68aa12e805c1383d7755d95e3c11469306b6fc517072eb1db449459.jpg

---

## Lecture: output\algorithm_design\page_007\algorithm_design_page_007\auto

# Example: Database Query Processing

Note that the same problem can be decomposed into subtasks in other ways as well.

<table><tr><td>ID#</td><td>Model</td></tr><tr><td>4523</td><td>Civic</td></tr><tr><td>6734</td><td>Civic</td></tr><tr><td>4395 7352</td><td>Civic Civic</td></tr></table>

<table><tr><td>ID#</td><td>Year</td></tr><tr><td>7623 6734</td><td>2001 2001 2001</td></tr></table>

<table><tr><td>ID#</td><td>Color</td></tr><tr><td>3476 6734</td><td>White White</td></tr></table>

<table><tr><td>ID#</td><td>Color</td></tr><tr><td>7623</td><td>Green</td></tr><tr><td>9834 5342</td><td>Green Green</td></tr><tr><td>8354</td><td>Green</td></tr></table>

![](images/91381a76280087df1a89ad0b6d983f5177aa2e31a15072f7f63b33e777a2adab.jpg)

<table><tr><td rowspan=1 colspan=1>ID#</td><td rowspan=1 colspan=1>Model</td><td rowspan=1 colspan=1>Year</td><td rowspan=1 colspan=1>Color</td></tr><tr><td rowspan=1 colspan=1>6734</td><td rowspan=1 colspan=1>Civic</td><td rowspan=1 colspan=1>2001</td><td rowspan=1 colspan=1>white</td></tr></table>

An alternate decomposition of the given problem into subtasks, along with their data dependencies.

Different task decompositions may lead to significant differences with respect to their eventual parallel performance.

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\algorithm_design\page_007\algorithm_design_page_007\auto\images\4f9ae6f2479d50477c156c1834178960cdb222e0ff2a902e963367b5b1f3f328.jpg
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\algorithm_design\page_007\algorithm_design_page_007\auto\images\91381a76280087df1a89ad0b6d983f5177aa2e31a15072f7f63b33e777a2adab.jpg
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\algorithm_design\page_007\algorithm_design_page_007\auto\images\a9ef2285db6597189ad7b771c7bb735ae9e0def3feef2f649e5d5ddb6edf75c8.jpg
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\algorithm_design\page_007\algorithm_design_page_007\auto\images\b952a188519c9a049514ba283359eb91de8b7b2fe4d7c767a7672367bc1a1885.jpg
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\algorithm_design\page_007\algorithm_design_page_007\auto\images\c4e9cd68fffc55bce8472d8cbf581063dca23bdd100782091207a8adebc973cf.jpg
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\algorithm_design\page_007\algorithm_design_page_007\auto\images\cbf21ec9c6619983a13d1d56494757ea1132630e05ca027560d62f075f30a0fe.jpg

---

## Lecture: output\algorithm_design\page_008\algorithm_design_page_008\auto

# Granularity of Task Decompositions

The number of tasks into which a problem is decomposed determines its granularity.

Decomposition into a large number of tasks results in finegrained decomposition and that into a small number of tasks results in a coarse grained decomposition.

![](images/9dc1eaf8ac60add003fa05e50b0103ba7bfac3c07bbf28fb9b1f25ff486d1ae4.jpg)

A coarse grained counterpart to the dense matrix-vector product example. Each task in this example corresponds to the computation of three elements of the result vector.

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\algorithm_design\page_008\algorithm_design_page_008\auto\images\9dc1eaf8ac60add003fa05e50b0103ba7bfac3c07bbf28fb9b1f25ff486d1ae4.jpg

---

## Lecture: output\algorithm_design\page_009\algorithm_design_page_009\auto

# Degree of Concurrency

The number of tasks that can be executed in parallel is the degree of concurrency of a decomposition.

Since the number of tasks that can be executed in parallel may change over program execution, the maximum degree of concurrency is the maximum number of such tasks at any point during execution. What is the maximum degree of concurrency of the database query examples?

The average degree of concurrency is the average number of tasks that can be processed in parallel over the execution of the program. Assuming that each task in the database example takes identical processing time, what is the average degree of concurrency in each decomposition?

• The degree of concurrency increases as the decomposition becomes finer in granularity and vice versa.

---

## Lecture: output\algorithm_design\page_010\algorithm_design_page_010\auto

# Critical Path Length

• A directed path in the task dependency graph represents a sequence of tasks that must be processed one after the other.

• The longest such path determines the shortest time in which the program can be executed in parallel.

• The length of the longest path in a task dependency graph is called the critical path length.

---

## Lecture: output\algorithm_design\page_011\algorithm_design_page_011\auto

# Critical Path Length

Consider the task dependency graphs of the two database query decompositions:

![](images/d3c7e4f87b85b58a9ffb6da3df8b8ea828ba9efc5b7821319afb05aacdc5b630.jpg)

What are the critical path lengths for the two task dependency graphs? What is the shortest parallel execution time for each decomposition?

How many processors are needed in each case to achieve this minimum parallel execution time? What is the maximum degree of concurrency? What is the average degree of concurrency?

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\algorithm_design\page_011\algorithm_design_page_011\auto\images\d3c7e4f87b85b58a9ffb6da3df8b8ea828ba9efc5b7821319afb05aacdc5b630.jpg

---

## Lecture: output\algorithm_design\page_012\algorithm_design_page_012\auto

# Limits on Parallel Performance

It would appear that the parallel time can be made arbitrarily small by making the decomposition finer in granularity.

There is an inherent bound on how fine the granularity of a computation can be. For example, in the case of multiplying a dense matrix with a vector, there can be no more than (n2) concurrent tasks.

Concurrent tasks may also have to exchange data with other tasks. This results in communication overhead. The tradeoff between the granularity of a decomposition and associated overheads often determines performance bounds.

---

## Lecture: output\algorithm_design\page_013\algorithm_design_page_013\auto

# Task Interaction Graphs

• Subtasks generally exchange data with others in a decomposition. For example, even in the trivial decomposition of the dense matrix-vector product, if the vector is not replicated across all tasks, they will have to communicate elements of the vector.

The graph of tasks (nodes) and their interactions/data exchange (edges) is referred to as a task interaction graph.

Note that task interaction graphs represent data dependencies, whereas task dependency graphs represent control dependencies.

---

## Lecture: output\algorithm_design\page_014\algorithm_design_page_014\auto

# Task Interaction Graphs: An Example

Consider the problem of multiplying a sparse matrix A with a vector b. The following observations can be made:

As before, the computation of each element of the result vector can be viewed as an independent task. Unlike a dense matrix-vector product though, only non-zero elements of matrix A participate in the computation. • If, for memory optimality, we also partition b across tasks, then one can see that the task interaction graph of the computation is identical to the graph of the matrix A (the graph for which A represents the adjacency structure).

![](images/29a122b467d7483d540bae1938afe39aaa37efd0d833b629a7347649dbf16660.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\algorithm_design\page_014\algorithm_design_page_014\auto\images\29a122b467d7483d540bae1938afe39aaa37efd0d833b629a7347649dbf16660.jpg

---

## Lecture: output\algorithm_design\page_015\algorithm_design_page_015\auto

# Task Interaction Graphs, Granularity, and Communication

In general, if the granularity of a decomposition is finer, the associated overhead (as a ratio of useful work associated with a task) increases.

Example: Consider the sparse matrix-vector product example from previous slide. Assume that each node takes unit time to process and each interaction (edge) causes an overhead of a unit time.

Viewing node 0 as an independent task involves a useful computation of one time unit and overhead (communication) of three time units.

Now, if we consider nodes 0, 4, and 8 as one task, then the task has useful computation totaling to three time units and communication corresponding to four time units (four edges). Clearly, this is a more favorable ratio than the former case.

---

## Lecture: output\algorithm_design\page_016\algorithm_design_page_016\auto

# Processes and Mapping

• In general, the number of tasks in a decomposition exceeds the number of processing elements available.

• For this reason, a parallel algorithm must also provide a mapping of tasks to processes.

Note: We refer to the mapping as being from tasks to processes, as opposed to processors. This is because typical programming APIs, as we shall see, do not allow easy binding of tasks to physical processors. Rather, we aggregate tasks into processes and rely on the system to map these processes to physical processors. We use processes, not in the UNIX sense of a process, rather, simply as a collection of tasks and associated data.

---

## Lecture: output\algorithm_design\page_017\algorithm_design_page_017\auto

# Processes and Mapping

• Appropriate mapping of tasks to processes is critical to the parallel performance of an algorithm.

Mappings are determined by both the task dependency and task interaction graphs.

Task dependency graphs can be used to ensure that work is equally spread across all processes at any point (minimum idling and optimal load balance).

• Task interaction graphs can be used to make sure that processes need minimum interaction with other processes (minimum communication).

---

## Lecture: output\algorithm_design\page_018\algorithm_design_page_018\auto

# Processes and Mapping

An appropriate mapping must minimize parallel execution time by:

• Mapping independent tasks to different processes.

Assigning tasks on critical path to processes as soon as they become available.

Minimizing interaction between processes by mapping tasks with dense interactions to the same process.

Note: These criteria often conflict eith each other. For example, a decomposition into one task (or no decomposition at all) minimizes interaction but does not result in a speedup at all! Can you think of other such conflicting cases?

---

## Lecture: output\algorithm_design\page_019\algorithm_design_page_019\auto

# Processes and Mapping: Example

![](images/ac481229254f405f273455d0032514c5765fef40e1c0c7d6e32f3f7e19d16550.jpg)

Mapping tasks in the database query decomposition to processes. These mappings were arrived at by viewing the dependency graph in terms of levels (no two nodes in a level have dependencies). Tasks within a single level are then assigned to different processes.

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\algorithm_design\page_019\algorithm_design_page_019\auto\images\ac481229254f405f273455d0032514c5765fef40e1c0c7d6e32f3f7e19d16550.jpg

---

## Lecture: output\algorithm_design\page_020\algorithm_design_page_020\auto

# Decomposition Techniques

So how does one decompose a task into various subtasks?

While there is no single recipe that works for all problems, we present a set of commonly used techniques that apply to broad classes of problems. These include:

recursive decomposition data decomposition exploratory decomposition speculative decomposition

---

## Lecture: output\algorithm_design\page_021\algorithm_design_page_021\auto

# Recursive Decomposition

Generally suited to problems that are solved using the divide-and-conquer strategy.

• A given problem is first decomposed into a set of sub-problems.

• These sub-problems are recursively decomposed further until a desired granularity is reached.

---

## Lecture: output\algorithm_design\page_022\algorithm_design_page_022\auto

# Recursive Decomposition: Example

A classic example of a divide-and-conquer algorithm on which we can apply recursive decomposition is Quicksort.

![](images/cebd33750eb352e25ac6ba90819a813283665a2563f43daa4365a71eda8b2338.jpg)

In this example, once the list has been partitioned around the pivot, each sublist can be processed concurrently (i.e., each sublist represents an independent subtask). This can be repeated recursively.

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\algorithm_design\page_022\algorithm_design_page_022\auto\images\cebd33750eb352e25ac6ba90819a813283665a2563f43daa4365a71eda8b2338.jpg

---

## Lecture: output\algorithm_design\page_023\algorithm_design_page_023\auto

# Recursive Decomposition: Example

The problem of finding the minimum number in a given list (or indeed any other associative operation such as sum, AND, etc.) can be fashioned as a divide-and-conquer algorithm. The following algorithm illustrates this.

We first start with a simple serial loop for computing the minimum entry in a given list:

1. procedure SERIAL_MIN (A, n)   
2. begin   
3. $m i n = \mathsf { A } [ 0 ] .$ ;   
4. for $i : = 1$ to $n - 1$ do   
5. if $( A [ i ] < m i n ) \ : m i n : = A [ i ] ;$   
6. endfor;   
7. return min;   
8. end SERIAL_MIN

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\algorithm_design\page_023\algorithm_design_page_023\auto\images\3c538b91ddf7bbbbed15c62b58e65177a660fdffdec38be4c9d69de230235c49.jpg

---

## Lecture: output\algorithm_design\page_024\algorithm_design_page_024\auto

Recursive Decomposition: Example We can rewrite the loop as follows:

1. procedure RECURSIVE_MIN (A, n)   
2. begin   
3. if ( $n = 1 )$ then   
4. $m i n : = \pmb { A } \left[ 0 \right]$ ;   
5. else   
6. lmin := RECURSIVE_MIN ( A, n/2 );   
7. rmin := RECURSIVE_MIN ( &(A[n/2]), n - n/2 );   
8. if (lmin $<$ rmin) then   
9. min := lmin;   
10. else   
11. min := rmin;   
12. endelse;   
13. endelse;   
14. return min;   
15. end RECURSIVE_MIN

---

## Lecture: output\algorithm_design\page_025\algorithm_design_page_025\auto

# Recursive Decomposition: Example

The code in the previous slide can be decomposed naturally using a recursive decomposition strategy. We illustrate this with the following example of finding the minimum number in the set {4, 9, 1, 7, 8, 11, 2, 12}. The task dependency graph associated with this computation is as follows:

![](images/1138fdc7ac8c68c66d53ae455473c80ddc128b005d2f6f5a80305834646b7e1e.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\algorithm_design\page_025\algorithm_design_page_025\auto\images\1138fdc7ac8c68c66d53ae455473c80ddc128b005d2f6f5a80305834646b7e1e.jpg

---

## Lecture: output\algorithm_design\page_026\algorithm_design_page_026\auto

# Data Decomposition

• Identify the data on which computations are performed.   
Partition this data across various tasks.   
• This partitioning induces a decomposition of the problem.   
• Data can be partitioned in various ways - this critically impacts performance of a parallel algorithm.

---

## Lecture: output\algorithm_design\page_027\algorithm_design_page_027\auto

# Data Decomposition: Output Data Decomposition

• Often, each element of the output can be computed independently of others (but simply as a function of the input).

• A partition of the output across tasks decomposes the problem naturally.

---

## Lecture: output\algorithm_design\page_028\algorithm_design_page_028\auto

# Output Data Decomposition: Example

Consider the problem of multiplying two n x n matrices A and B to yield matrix C. The output matrix C can be partitioned into four tasks as follows:

(A_ A ${ \mathrm { , 2 } } \atop \int \cdot ( \begin{array} { l l } { { B _ { 1 , 1 } } } & { { B _ { 1 , 2 } } } \\ { { B _ { 2 , 1 } } } & { { B _ { 2 , 2 } } } \end{array} )  ( \begin{array} { l } { { C _ { 1 } } } \\ { { C _ { 2 } } } \end{array} $

Task 1:

Task 2:

$$
\begin{array} { r } { C _ { 1 , 1 } = A _ { 1 , 1 } B _ { 1 , 1 } + A _ { 1 , 2 } B _ { 2 , 1 } } \\ { C _ { 1 , 2 } = A _ { 1 , 1 } B _ { 1 , 2 } + A _ { 1 , 2 } B _ { 2 , 2 } } \\ { C _ { 2 , 1 } = A _ { 2 , 1 } B _ { 1 , 1 } + A _ { 2 , 2 } B _ { 2 , 1 } } \\ { C _ { 2 , 2 } = A _ { 2 , 1 } B _ { 1 , 2 } + A _ { 2 , 2 } B _ { 2 , 2 } } \end{array}
$$

Task 3:

Task 4:

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\algorithm_design\page_028\algorithm_design_page_028\auto\images\b393e4613e079a6eac4501311745c48f708f9fb043ab9e190c36e596eb213425.jpg
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\algorithm_design\page_028\algorithm_design_page_028\auto\images\cb04d29d082da22e8a8d8ba80b24fe6247a9d25de493340adaeb8e5a0d3fd7f8.jpg

---

## Lecture: output\algorithm_design\page_029\algorithm_design_page_029\auto

# Output Data Decomposition: Example

A partitioning of output data does not result in a unique decomposition into tasks. For example, for the same problem as in previous slide, with identical output data distribution, we can derive the following two (other) decompositions:

<table><tr><td>Decomposition I</td><td>Decomposition II</td></tr><tr><td>Task 1: C1,1 = A1,1 B1,1 Task 2: C1,1 = C1,1 + A1,2 B2,1</td><td>Task 1: C1,1 = A1,1 B1,1 Task 2: C1,1 = C1,1 + A1,2 B2,1</td></tr><tr><td>Task 3: C1,2 = A1,1 B1,2</td><td>Task 3: C1,2 = A1,2 B2,2</td></tr><tr><td>Task 4: C1,2 = C1,2 + A1,2 B2,2</td><td>Task 4: C1,2 = C1,2 + A1,1 B1,2</td></tr><tr><td>Task 5: C2,1 = A2,1 B1,1</td><td>Task 5: C2,1 = A2,2 B2,1</td></tr><tr><td>Task 6: C2,1 = C2,1 + A2,2 B2,1</td><td>Task 6: C2,1 = C2,1 + A2,1 B1,1</td></tr><tr><td>Task 7: C2,2 = A2,1 B1,2</td><td>Task 7: C2,2 = A2,1 B1,2</td></tr><tr><td></td><td></td></tr><tr><td>Task 8: C2,2 = C2,2 + A2,2 B2,2</td><td>Task 8: C2,2 = C2,2 + A2,2 B2,2</td></tr></table>

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\algorithm_design\page_029\algorithm_design_page_029\auto\images\505063a46f2a4c4edfb7c0c662a1e47ab4e831673698ec6825bd5af598262a9d.jpg

---

## Lecture: output\algorithm_design\page_030\algorithm_design_page_030\auto

# Output Data Decomposition: Example

Consider the problem of counting the instances of given itemsets in a database of transactions. In this case, the output (itemset frequencies) can be partitioned across tasks.

# (a) Transactions (input), temsets (input), and frequencies (output)

![](images/a34b10cdc4900f9d421bfb1b202a5e85d999d6aff9bf2de69920678b29825d2a.jpg)

# (b) Partitioning the frequencies (and itemsets) among the tasks

![](images/075ed4f2343216ccc1d4ba84b202c0417720a4427bb4651d11611a4b3c553839.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\algorithm_design\page_030\algorithm_design_page_030\auto\images\075ed4f2343216ccc1d4ba84b202c0417720a4427bb4651d11611a4b3c553839.jpg
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\algorithm_design\page_030\algorithm_design_page_030\auto\images\a34b10cdc4900f9d421bfb1b202a5e85d999d6aff9bf2de69920678b29825d2a.jpg

---

## Lecture: output\algorithm_design\page_031\algorithm_design_page_031\auto

# Output Data Decomposition: Example

From the previous example, the following observations can be made:

• If the database of transactions is replicated across the processes, each task can be independently accomplished with no communication.

• If the database is partitioned across processes as well (for reasons of memory utilization), each task first computes partial counts. These counts are then aggregated at the appropriate task.

---

## Lecture: output\algorithm_design\page_032\algorithm_design_page_032\auto

# Input Data Partitioning

Generally applicable if each output can be naturally computed as a function of the input.

In many cases, this is the only natural decomposition because the output is not clearly known a-priori (e.g., the problem of finding the minimum in a list, sorting a given list, etc.).

• A task is associated with each input data partition. The task performs as much of the computation with its part of the data. Subsequent processing combines these partial results.

---

## Lecture: output\algorithm_design\page_033\algorithm_design_page_033\auto

# Input Data Partitioning: Example

In the database counting example, the input (i.e., the transaction set) can be partitioned. This induces a task decomposition in which each task generates partial counts for all itemsets. These are combined subsequently for aggregate counts.

# Partitioning the transactions among the tasks

![](images/73fd128d5c91257770fbc2a1848b59a794d6c26ea73c88463834c78ac80bf9d2.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\algorithm_design\page_033\algorithm_design_page_033\auto\images\73fd128d5c91257770fbc2a1848b59a794d6c26ea73c88463834c78ac80bf9d2.jpg

---

## Lecture: output\algorithm_design\page_034\algorithm_design_page_034\auto

# Partitioning Input and Output Data

Often input and output data decomposition can be combined for a higher degree of concurrency. For the itemset counting example, the transaction set (input) and itemset counts (output) can both be decomposed as follows:

![](images/9b76962e15712dfbb05f722b7903a458ed214b75eb230776685421ab71a26890.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\algorithm_design\page_034\algorithm_design_page_034\auto\images\9b76962e15712dfbb05f722b7903a458ed214b75eb230776685421ab71a26890.jpg

---

## Lecture: output\algorithm_design\page_035\algorithm_design_page_035\auto

# Intermediate Data Partitioning

• Computation can often be viewed as a sequence of transformation from the input to the output data.

• In these cases, it is often beneficial to use one of the intermediate stages as a basis for decomposition.

---

## Lecture: output\algorithm_design\page_036\algorithm_design_page_036\auto

# Intermediate Data Partitioning: Example

Let us revisit the example of dense matrix multiplication. We first show how we can visualize this computation in terms of intermediate matrices D.

![](images/26293c12d54a18a6d17b494354547b29704ee9e395f5e7c4c3f8c99007f1ff96.jpg)

<table><tr><td>C1,1</td><td>C1,2</td></tr><tr><td>C2,1</td><td>C2.2</td></tr></table>

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\algorithm_design\page_036\algorithm_design_page_036\auto\images\26293c12d54a18a6d17b494354547b29704ee9e395f5e7c4c3f8c99007f1ff96.jpg
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\algorithm_design\page_036\algorithm_design_page_036\auto\images\812512a1dacbf5ba6d4086eb28876df1928fb33be0dad7189a41edfbca8bdfec.jpg

---

## Lecture: output\algorithm_design\page_037\algorithm_design_page_037\auto

# ntermediate Data Partitioning: Example

A decomposition of intermediate data structure leads to the following decomposition into $8 + 4$ tasks:

$$
A _ { 1 , 2 } \atop A _ { 2 , 2 } \atop A \cdot ( \begin{array} { c c } { { B _ { 1 , 1 } } } & { { B _ { 1 , 2 } } } \\ { { B _ { 2 , 1 } } } & { { B _ { 2 , 2 } } } \end{array} )  ( \begin{array} { c c } { { ( \begin{array} { c c } { { D _ { 1 , 1 , 1 } } } & { { I } } \\ { { D _ { 1 , 2 , 2 } } } & { { I } } \end{array} ) } } & { { } } \\ { { ( \begin{array} { c c } { { D _ { 2 , 1 , 1 } } } & { { I } } \\ { { D _ { 2 , 2 , 2 } } } & { { I } } \end{array} ) } } & { { } } \end{array} )
$$

# Stage II

( 1 $\begin{array}{c} \begin{array} { r } { \iota , \iota , D _ { 1 , 1 , 2 } } \\ { \iota , 2 , D _ { 1 , 2 , 2 } } \end{array} \bigg ) + ( \begin{array} { l l } { D _ { 2 , 1 , 1 } } & { D _ { 2 , 1 , 2 } } \\ { D _ { 2 , 2 , 2 } } & { D _ { 2 , 2 , 2 } } \end{array} )  ( \begin{array} { l } { C _ { 1 , 2 , 2 } } \\ { C _ { 2 , 2 , 2 } } \end{array} )  \end{array}$ C2,1 C1,2) \$C2,2

Task 01: $D _ { 1 , 1 , 1 } { = } A _ { 1 , 1 } B _ { 1 , 1 }$

Task 03: $D _ { 1 , 1 , 2 } \mathbf { \equiv } A _ { 1 , 1 } B _ { 1 , 2 }$

Task 05: $\pmb { D } _ { 1 , 2 , 1 } \pmb { = A } _ { 2 , 1 } \pmb { B } _ { 1 , 1 } ,$ 1

Task 07: $\pmb { D } _ { 1 , 2 , 2 } \mathbf { = } A _ { 2 , 1 } \pmb { B } _ { 1 , 2 }$

Task 09: $\pmb { C } _ { 1 , 1 } = \pmb { D } _ { 1 , 1 , 1 } + \pmb { D } _ { 2 , 1 , 1 }$

Task 11: $\pmb { C } _ { 2 , 1 } = \pmb { D } _ { 1 , 2 , 1 } + \pmb { D } _ { 2 , 2 , 1 }$

Task 02: $D _ { 2 , 1 , 1 } { = } A _ { 1 , 2 } B _ { 2 , 1 }$

Task 04: $D _ { 2 , 1 , 2 } \mathrm { = } A _ { 1 , 2 } B _ { 2 , 2 }$

Task 06: $D _ { 2 , 2 , 1 } \mathrm { = } A _ { 2 , 2 } B _ { 2 , 1 }$

Task 08: $D _ { 2 , 2 , 2 } { = } A _ { 2 , 2 } B _ { 2 , 2 }$

Task 10: $\pmb { C } _ { 1 , 2 } = \pmb { D } _ { 1 , 1 , 2 } + \pmb { D } _ { 2 , 1 , 2 }$

Task 12: $\pmb { C } _ { 2 , 2 } = \pmb { D } _ { 1 , 2 , 2 } + \pmb { D } _ { 2 , 2 , 2 }$

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\algorithm_design\page_037\algorithm_design_page_037\auto\images\2304adf8d1f8f2c60bfcd23db02307a536975ac2252f59eeceb54326d43bc423.jpg
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\algorithm_design\page_037\algorithm_design_page_037\auto\images\b181f3dcb149a298880360d417c85702b0d11a88f61a612cfe58206ad3239c3e.jpg

---

## Lecture: output\algorithm_design\page_038\algorithm_design_page_038\auto

# Intermediate Data Partitioning: Example

The task dependency graph for the decomposition (shown in previous foil) into 12 tasks is as follows:

![](images/e7992db61b1352e1008bd516912acc3b23dbed9bd6e9a3b868e85f52e06a70d2.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\algorithm_design\page_038\algorithm_design_page_038\auto\images\e7992db61b1352e1008bd516912acc3b23dbed9bd6e9a3b868e85f52e06a70d2.jpg

---

## Lecture: output\algorithm_design\page_039\algorithm_design_page_039\auto

# The Owner Computes Rule

The Owner Computes Rule generally states that the process assigned a particular data item is responsible for all computation associated with it.

• In the case of input data decomposition, the owner computes rule implies that all computations that use the input data are performed by the process.

• In the case of output data decomposition, the owner computes rule implies that the output is computed by the process to which the output data is assigned.

---

## Lecture: output\algorithm_design\page_040\algorithm_design_page_040\auto

# Exploratory Decomposition

• In many cases, the decomposition of the problem goes hand-in-hand with its execution.

• These problems typically involve the exploration (search) of a state space of solutions.

• Problems in this class include a variety of discrete optimization problems (e.g., integer programming), theorem proving, game playing, etc.

---

## Lecture: output\algorithm_design\page_041\algorithm_design_page_041\auto

# Exploratory Decomposition: Example

A simple application of exploratory decomposition is in the solution to a 15 puzzle (a tile puzzle). We show a sequence of three moves that transform a given initial state (a) to desired final state (d).

![](images/74db17259102d135c92aa017ba21657ff34123f638352ad4ac2f9a51ae7c8f66.jpg)

Of-course, the problem of computing the solution, in general, is much more difficult than in this simple example.

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\algorithm_design\page_041\algorithm_design_page_041\auto\images\74db17259102d135c92aa017ba21657ff34123f638352ad4ac2f9a51ae7c8f66.jpg

---

## Lecture: output\algorithm_design\page_042\algorithm_design_page_042\auto

Exploratory Decomposition: Example The state space can be explored by generating various successor states of the current state and to view them as independent tasks.

![](images/19cf69b6fd1513b28057c8a2efd63502c99875dc0696ae9672e8e4de2c524bbd.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\algorithm_design\page_042\algorithm_design_page_042\auto\images\19cf69b6fd1513b28057c8a2efd63502c99875dc0696ae9672e8e4de2c524bbd.jpg

---

## Lecture: output\algorithm_design\page_043\algorithm_design_page_043\auto

# Exploratory Decomposition:

# Anomalous Computations

• In many instances of exploratory decomposition, the decomposition technique may change the amount of work done by the parallel formulation.

• This change results in super- or sub-linear speedups.

![](images/c09155bb91db9a71ab438d7808cd332aa69a34ba1d359f30d30a6ac5c7c2c250.jpg)

Total serial work: 2m+1   
Total parallel work: 1

Total serial work: m Total parallel work: 4m

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\algorithm_design\page_043\algorithm_design_page_043\auto\images\c09155bb91db9a71ab438d7808cd332aa69a34ba1d359f30d30a6ac5c7c2c250.jpg

---

## Lecture: output\algorithm_design\page_044\algorithm_design_page_044\auto

# Speculative Decomposition

• In some applications, dependencies between tasks are not known a-priori.

• For such applications, it is impossible to identify independent tasks.

There are generally two approaches to dealing with such applications: conservative approaches, which identify independent tasks only when they are guaranteed to not have dependencies, and, optimistic approaches, which schedule tasks even when they may potentially be erroneous.

Conservative approaches may yield little concurrency and optimistic approaches may require roll-back mechanism in the case of an error.

---

## Lecture: output\algorithm_design\page_045\algorithm_design_page_045\auto

# Speculative Decomposition: Example

A classic example of speculative decomposition is in discrete event simulation.

• The central data structure in a discrete event simulation is a timeordered event list.

Events are extracted precisely in time order, processed, and if required, resulting events are inserted back into the event list.

Consider a bus terminal as a discrete event system – each bus comes in, drops off passengers, gets new passengers, and departs.

Each of these events may be processed independently, however, if some buses are stuck in a traffic jam and not get to the bus terminal, then the schedule will have to change for those buses.

• Therefore, an optimistic scheduling of other events will have to be rolled back.

---

## Lecture: output\algorithm_design\page_046\algorithm_design_page_046\auto

# Hybrid Decompositions

Often, a mix of decomposition techniques is necessary for decomposing a problem. Consider the following examples:

In quicksort, recursive decomposition alone limits concurrency (Why?). A mix of data and recursive decompositions is more desirable. In discrete event simulation, there might be concurrency in task processing. A mix of speculative decomposition and data decomposition may work well. • Even for simple problems like finding a minimum of a list of numbers, a mix of data and recursive decomposition works well.

![](images/f0bca833d59f8149395c473459ae45d8c60a24e38e6d12beaf80a9acb9cef7c6.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\algorithm_design\page_046\algorithm_design_page_046\auto\images\f0bca833d59f8149395c473459ae45d8c60a24e38e6d12beaf80a9acb9cef7c6.jpg

---

## Lecture: output\algorithm_design\page_047\algorithm_design_page_047\auto

# Characteristics of Tasks

Once a problem has been decomposed into independent tasks, the characteristics of these tasks critically impact choice and performance of parallel algorithms. Relevant task characteristics include:

• Task generation (static/dynamic) • Task sizes. • Size of data associated with tasks.

---

## Lecture: output\algorithm_design\page_048\algorithm_design_page_048\auto

# Task Generation

• Static task generation: Concurrent tasks can be identified a-priori. Typical matrix operations, graph algorithms, image processing applications, and other regularly structured problems fall in this class. These can typically be decomposed using data or recursive decomposition techniques.

Dynamic task generation: Tasks are generated as we perform computation. A classic example of this is in game playing - each 15 puzzle board is generated from the previous one. These applications are typically decomposed using exploratory or speculative decompositions.

---

## Lecture: output\algorithm_design\page_049\algorithm_design_page_049\auto

# Task Sizes

• Task sizes may be uniform (i.e., all tasks are the same size) or non-uniform.

• Non-uniform task sizes may be such that they can be determined (or estimated) a-priori or not.

• Examples in this class include discrete optimization problems, in which it is difficult to estimate the effective size of a state space.

---

## Lecture: output\algorithm_design\page_050\algorithm_design_page_050\auto

# Size of Data Associated with Tasks

• The size of data associated with a task may be small or large when viewed in the context of the size of the task.

• A small context of a task implies that an algorithm can easily communicate this task to other processes dynamically (e.g., the 15 puzzle).

A large context ties the task to a process, or alternatively, an algorithm may attempt to reconstruct the context at another process as opposed to communicating the context of the task (e.g., integer programming).

---

## Lecture: output\algorithm_design\page_051\algorithm_design_page_051\auto

# Characteristics of Task Interactions

• Tasks may communicate with each other in various ways:

• Static interactions: The tasks and their interactions are known a-priori. These are relatively simpler to code into programs.

Dynamic interactions: The timing or interacting tasks cannot be determined apriori. These interactions are harder to code, especially if they use message passing APIs.

---

## Lecture: output\algorithm_design\page_052\algorithm_design_page_052\auto

# Characteristics of Task Interactions

• Regular interactions: There is a definite pattern in the interactions. These patterns can be exploited for efficient implementation.

• Irregular interactions: Interactions lack welldefined topologies.

---

## Lecture: output\algorithm_design\page_053\algorithm_design_page_053\auto

# Characteristics of Task Interactions: Example

A simple example of a regular static interaction pattern is in image dithering. The underlying communication pattern is a structured (2-D mesh) one as shown here:

![](images/76361eabd9e0db1ef54fbe1413ac81f4693604b23d90bda2af8ef8b9f792a0c5.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\algorithm_design\page_053\algorithm_design_page_053\auto\images\76361eabd9e0db1ef54fbe1413ac81f4693604b23d90bda2af8ef8b9f792a0c5.jpg

---

## Lecture: output\algorithm_design\page_054\algorithm_design_page_054\auto

# Characteristics of Task Interactions: Example

The multiplication of a sparse matrix with a vector is a good example of a static irregular interaction pattern. Here is an example of a sparse matrix and its associated interaction pattern.

![](images/9fba41584ff44f8f542423485a2f605c9350bb0944e85cb4d79c24b639c473d8.jpg)

![](images/327a60974c50d4a838c9f142e5e77418f7d54fc91032b22d27e770bb0b88bfa6.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\algorithm_design\page_054\algorithm_design_page_054\auto\images\327a60974c50d4a838c9f142e5e77418f7d54fc91032b22d27e770bb0b88bfa6.jpg
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\algorithm_design\page_054\algorithm_design_page_054\auto\images\9fba41584ff44f8f542423485a2f605c9350bb0944e85cb4d79c24b639c473d8.jpg

---

## Lecture: output\algorithm_design\page_055\algorithm_design_page_055\auto

Characteristics of Task Interactions

• Interactions may be read-only or read-write.   
In read-only interactions, tasks just read data items associated with other tasks.   
In read-write interactions tasks read, as well as modily data items associated with other tasks.   
In general, read-write interactions are harder to code, since they require additional synchronization primitives.

---

## Lecture: output\algorithm_design\page_056\algorithm_design_page_056\auto

# Characteristics of Task Interactions

• Interactions may be one-way or two-way.

• A one-way interaction can be initiated and accomplished by one of the two interacting tasks.

• A two-way interaction requires participation from both tasks involved in an interaction.

• One way interactions are somewhat harder to code in message passing APIs.

---

## Lecture: output\algorithm_design\page_057\algorithm_design_page_057\auto

# Mapping Techniques

• Once a problem has been decomposed into concurrent tasks, these must be mapped to processes (that can be executed on a parallel platform).

• Mappings must minimize overheads.

• Primary overheads are communication and idling.

Minimizing these overheads often represents contradicting objectives.

Assigning all work to one processor trivially minimizes communication at the expense of significant idling.

---

## Lecture: output\algorithm_design\page_058\algorithm_design_page_058\auto

# Mapping Techniques for Minimum Idling

Mapping must simultaneously minimize idling and load balance.   
Merely balancing load does not minimize idling.

![](images/9b86f7bc64f69182aa65709915b1dcb26cf6ead8d0d5c3bfb113db97729c7399.jpg)

![](images/70f408b1847f09824b5b147ad167957a58af22a285d1bf3715c944e2affdf330.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\algorithm_design\page_058\algorithm_design_page_058\auto\images\70f408b1847f09824b5b147ad167957a58af22a285d1bf3715c944e2affdf330.jpg
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\algorithm_design\page_058\algorithm_design_page_058\auto\images\9b86f7bc64f69182aa65709915b1dcb26cf6ead8d0d5c3bfb113db97729c7399.jpg

---

## Lecture: output\algorithm_design\page_059\algorithm_design_page_059\auto

# Mapping Techniques for Minimum Idling

Mapping techniques can be static or dynamic.

Static Mapping: Tasks are mapped to processes a-priori. For this to work, we must have a good estimate of the size of each task. Even in these cases, the problem may be NP complete.

Dynamic Mapping: Tasks are mapped to processes at runtime. This may be because the tasks are generated at runtime, or that their sizes are not known.

Other factors that determine the choice of techniques include the size of data associated with a task and the nature of underlying domain.

---

## Lecture: output\algorithm_design\page_060\algorithm_design_page_060\auto

# Schemes for Static Mapping

• Mappings based on data partitioning.   
• Mappings based on task graph partitioning.   
• Hybrid mappings.

---

## Lecture: output\algorithm_design\page_061\algorithm_design_page_061\auto

# Mappings Based on Data Partitioning

We can combine data partitioning with the \`\`owner-computes'' rule to partition the computation into subtasks. The simplest data decomposition schemes for dense matrices are 1-D block distribution schemes.

row-wise distribution   

<table><tr><td rowspan=1 colspan=1>P0</td></tr><tr><td rowspan=1 colspan=1>P1</td></tr><tr><td rowspan=1 colspan=1>P2</td></tr><tr><td rowspan=1 colspan=1>P3</td></tr><tr><td rowspan=1 colspan=1>P4</td></tr><tr><td rowspan=1 colspan=1>P $</td></tr><tr><td rowspan=1 colspan=1>P6</td></tr><tr><td rowspan=1 colspan=1>P7</td></tr></table>

column-wise distribution   

<table><tr><td></td><td></td><td></td><td>P0 P1 P2 P3 P4 P5 P6 P7</td><td></td><td></td><td></td><td></td></tr></table>

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\algorithm_design\page_061\algorithm_design_page_061\auto\images\1504dd4214e20a379938092cfcfa869999a99a528a471890bf5f82652dffd173.jpg
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\algorithm_design\page_061\algorithm_design_page_061\auto\images\2717541aded54a19858a305574f9322d28002413059512e05c3caf19b9080fa3.jpg

---

## Lecture: output\algorithm_design\page_062\algorithm_design_page_062\auto

# Block Array Distribution Schemes

Block distribution schemes can be generalized to higher dimensions as well.

<table><tr><td rowspan=1 colspan=1>Po</td><td rowspan=1 colspan=1>P1</td><td rowspan=1 colspan=1>P2$</td><td rowspan=1 colspan=1>P </td><td rowspan=4 colspan=1></td><td rowspan=2 colspan=1></td><td rowspan=2 colspan=1></td><td rowspan=2 colspan=1></td><td rowspan=2 colspan=1></td><td rowspan=2 colspan=1></td><td rowspan=2 colspan=1></td><td rowspan=2 colspan=1></td><td rowspan=2 colspan=1></td></tr><tr><td rowspan=1 colspan=1>P4</td><td rowspan=1 colspan=1>P5$</td><td rowspan=1 colspan=1>P6</td><td rowspan=1 colspan=1>Pr</td></tr><tr><td rowspan=1 colspan=1>P{$</td><td rowspan=1 colspan=1>Pg</td><td rowspan=1 colspan=1>P10</td><td rowspan=1 colspan=1>P11</td><td rowspan=2 colspan=1></td><td rowspan=2 colspan=1></td><td rowspan=2 colspan=1></td><td rowspan=2 colspan=1></td><td rowspan=2 colspan=1></td><td rowspan=2 colspan=1></td><td rowspan=2 colspan=1></td><td rowspan=2 colspan=1></td></tr><tr><td rowspan=1 colspan=1>P12</td><td rowspan=1 colspan=1>P13</td><td rowspan=1 colspan=1>P14</td><td rowspan=1 colspan=1>P15</td></tr><tr><td rowspan=1 colspan=13>(a)                                                                                      (b)</td></tr></table>

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\algorithm_design\page_062\algorithm_design_page_062\auto\images\d34f4a9d250e0d64b90887fcda2af413e48c2a9b872625a328db971c200b5c61.jpg

---

## Lecture: output\algorithm_design\page_063\algorithm_design_page_063\auto

# Block Array Distribution Schemes: Examples

For multiplying two dense matrices A and B, we can partition the output matrix C using a block decomposition.

For load balance, we give each task the same number of elements of C. (Note that each element of C corresponds to a single dot product.)

The choice of precise decomposition (1-D or 2-D) is determined by the associated communication overhead.

• In general, higher dimension decomposition allows the use of larger number of processes.

---

## Lecture: output\algorithm_design\page_064\algorithm_design_page_064\auto

# Data Sharing in Dense Matrix Multiplication

![](images/073455c6db37c2f761ff36272111dcc4660ff746b50154c768c87a69466aa188.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\algorithm_design\page_064\algorithm_design_page_064\auto\images\073455c6db37c2f761ff36272111dcc4660ff746b50154c768c87a69466aa188.jpg

---

## Lecture: output\algorithm_design\page_065\algorithm_design_page_065\auto

# Block Cyclic Distributions

• Variation of the block distribution scheme that can be used to alleviate the load-imbalance and idling problems.

• Partition an array into many more blocks than the number of available processes.

• Blocks are assigned to processes in a roundrobin manner so that each process gets several non-adjacent blocks.

---

## Lecture: output\algorithm_design\page_066\algorithm_design_page_066\auto

# Block-Cyclic Distribution

• A cyclic distribution is a special case in which block size is one. A block distribution is a special case in which block size is n/p , where n is the dimension of the matrix and $\pmb { p }$ is the number of processes.

![](images/cb6119d7bb75eb64297728de08361511fc050d4f530fcf859cf3d78baba44253.jpg)

![](images/d53e0ba3c921feb7506099ea967302528804e9f349c9752355f0aba2440550d4.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\algorithm_design\page_066\algorithm_design_page_066\auto\images\cb6119d7bb75eb64297728de08361511fc050d4f530fcf859cf3d78baba44253.jpg
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\algorithm_design\page_066\algorithm_design_page_066\auto\images\d53e0ba3c921feb7506099ea967302528804e9f349c9752355f0aba2440550d4.jpg

---

## Lecture: output\algorithm_design\page_067\algorithm_design_page_067\auto

# Graph Partitioning Dased Data Decomposition

• In case of sparse matrices, block decompositions are more complex.

• Consider the problem of multiplying a sparse matrix with a vector.

The graph of the matrix is a useful indicator of the work (number of nodes) and communication (the degree of each node).

• In this case, we would like to partition the graph so as to assign equal number of nodes to each process, while minimizing edge count of the graph partition.

---

## Lecture: output\algorithm_design\page_068\algorithm_design_page_068\auto

# Partitioning the Graph of Lake Superior

![](images/5750f6b5fc98941d02f585b6fc4722c72593ea0de07acdbb9ec884ed72263012.jpg)  
Random Partitioning

![](images/e0aed27d81f337d88ba6467fe1e00964917e7f7b96121260acfeffa103b96f98.jpg)

Partitioning for minimum edge-cut.

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\algorithm_design\page_068\algorithm_design_page_068\auto\images\5750f6b5fc98941d02f585b6fc4722c72593ea0de07acdbb9ec884ed72263012.jpg
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\algorithm_design\page_068\algorithm_design_page_068\auto\images\e0aed27d81f337d88ba6467fe1e00964917e7f7b96121260acfeffa103b96f98.jpg

---

## Lecture: output\algorithm_design\page_069\algorithm_design_page_069\auto

# Mappings Based on Task Paritioning

• Partitioning a given task-dependency graph across processes.

• Determining an optimal mapping for a general task-dependency graph is an NP-complete problem.

• Excellent heuristics exist for structured graphs.

---

## Lecture: output\algorithm_design\page_070\algorithm_design_page_070\auto

# Task Paritioning: Mapping a Binary Tree Dependency Graph

Example illustrates the dependency graph of one view of quick-sort and how it can be assigned to eight processes.

![](images/0e0f4ead5e0a3da832190926705a16bd5b7310b9bdee07dc278eac6669d47522.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\algorithm_design\page_070\algorithm_design_page_070\auto\images\0e0f4ead5e0a3da832190926705a16bd5b7310b9bdee07dc278eac6669d47522.jpg

---

## Lecture: output\algorithm_design\page_071\algorithm_design_page_071\auto

# Task Paritioning: Mapping a Sparse

Graph

Sparse graph for computing a sparse matrix-vector product and its mapping.

Process 0

![](images/44aa30a006635e1c9d5595021eb53b0e4b8c206234915909ed08973a972b429e.jpg)

Process 1

Process 2

List Ci contains the indices of b that Process i needs from other processes.

Partitioning the task-interaction graph

![](images/97d46b9377eb1b06adcbb23b0b931835980f2f12d1d49e225057c7165797c27b.jpg)  
Process 2

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\algorithm_design\page_071\algorithm_design_page_071\auto\images\44aa30a006635e1c9d5595021eb53b0e4b8c206234915909ed08973a972b429e.jpg
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\algorithm_design\page_071\algorithm_design_page_071\auto\images\97d46b9377eb1b06adcbb23b0b931835980f2f12d1d49e225057c7165797c27b.jpg
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\algorithm_design\page_071\algorithm_design_page_071\auto\images\feab4eaed5eb84a3745b2d032b7f023969eb9adc46b78af212058eff90d1ea32.jpg

---

## Lecture: output\algorithm_design\page_072\algorithm_design_page_072\auto

# Hierarchical Mappings

• Sometimes a single mapping technique is inadequate.

• For example, the task mapping of the binary tree (quicksort) cannot use a large number of processors.

• For this reason, task mapping can be used at the top level and data partitioning within each level.

---

## Lecture: output\algorithm_design\page_073\algorithm_design_page_073\auto

# An Example of Task Partitioning

An example of task partitioning at top level with data partitioning at the lower level.

![](images/7019c316b65b26fc52fbbc82f990b636cc26fdd97cb9be0fd24fb8012e81550d.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\algorithm_design\page_073\algorithm_design_page_073\auto\images\7019c316b65b26fc52fbbc82f990b636cc26fdd97cb9be0fd24fb8012e81550d.jpg

---

## Lecture: output\algorithm_design\page_074\algorithm_design_page_074\auto

# Schemes for Dynamic Mapping

• Dynamic mapping is sometimes also referr to as dynamic load balancing, since load balancing is the primary motivation for dynamic mapping.

• Dynamic mapping schemes can be centralized or distributed.

---

## Lecture: output\algorithm_design\page_075\algorithm_design_page_075\auto

# Centralized Dynamic Mapping

• Processes are designated as masters or slaves.

When a process runs out of work, it requests the master for more work.

When the number of processes increases, the master may become the bottleneck.

• To alleviate this, a process may pick up a number of tasks (a chunk) at one time. This is called Chunk scheduling.

• Selecting large chunk sizes may lead to significant load imbalances as well.

• A number of schemes have been used to gradually decrease chunk size as the computation progresses.

---

## Lecture: output\algorithm_design\page_076\algorithm_design_page_076\auto

# Distributed Dynamic Mapping

• Each process can send or receive work from other processes.

• This alleviates the bottleneck in centralized schemes.

There are four critical questions: how are sending and receiving processes paired together, who initiates work transfer, how much work is transferred, and when is a transfer triggered?

Answers to these questions are generally application specific.

---

## Lecture: output\algorithm_design\page_077\algorithm_design_page_077\auto

# Minimizing Interaction Overheads

Maximize data locality: Where possible, reuse intermediate data. Restructure computation so that data can be reused in smaller time windows.

• Minimize volume of data exchange: There is a cost associated with each word that is communicated. For this reason, we must minimize the volume of data communicated.

Minimize frequency of interactions: There is a startup cost associated with each interaction. Therefore, try to merge multiple interactions to one, where possible.

Minimize contention and hot-spots: Use decentralized techniques, replicate data where necessary.

---

## Lecture: output\algorithm_design\page_078\algorithm_design_page_078\auto

# Minimizing Interaction Overheads (continued)

• Overlapping computations with interactio Use non-blocking communications, multithreading, and prefetching to hide latencies.

• Replicating data or computations.

• Using group communications instead of pointto-point primitives.

• Overlap interactions with other interactions.

---

## Lecture: output\algorithm_design\page_079\algorithm_design_page_079\auto

# Parallel Algorithm Models

An algorithm model is a way of structuring a parallel algorithm by selecting a decomposition and mapping technique and applying the appropriate strategy to minimize interactions.

Data Parallel Model: Tasks are statically (or semistatically) mapped to processes and each task performs similar operations on different data.

Task Graph Model: Starting from a task dependency graph, the interrelationships among the tasks are utilized to promote locality or to reduce interaction costs.

---

## Lecture: output\algorithm_design\page_080\algorithm_design_page_080\auto

# Parallel Algorithm Models (continued)

Master-Slave Model: One or more processes generate work and allocate it to worker processes. This allocation may be static or dynamic.

Pipeline / Producer-Comsumer Model: A stream of data is passed through a succession of processes, each of which perform some task on it.

Hybrid Models: A hybrid model may be composed either of multiple models applied hierarchically or multiple models applied sequentially to different phases of a parallel algorithm.

---

## Lecture: output\algorithm_design\page_081\algorithm_design_page_081\auto

# Summary

• Parallel algorithm design involves decomposition, task generation, and task mapping considering data partitioning and task interactions.

• Parallel algorithm models include dataparallel, task parallel, and hybrid schemes.

---

## Lecture: output\communications\page_001\communications_page_001\auto

# Basic Communication Operations

# Ananth Grama, Anshul Gupta, George Karypis, and Vipin Kumar

Based on the text \`\`Introduction to Parallel Computing'', Addison Wesley, 2003

---

## Lecture: output\communications\page_002\communications_page_002\auto

# Topic Overview

One-to-All Broadcast and All-to-One Reduction All-to-All Broadcast and Reduction All-Reduce and Prefix-Sum Operations Scatter and Gather All-to-All Personalized Communication

---

## Lecture: output\communications\page_003\communications_page_003\auto

# Communication Operations in MPI

<table><tr><td>Operation</td><td>MPI Name</td></tr><tr><td>One-to-all broadcast All-to-one reduction All-to-all broadcast</td><td>MPI_Bcast MPI_Reduce MPI_Allgather</td></tr><tr><td>All-to-all reduction All-reduce</td><td>MPI_Reduce_scatter</td></tr><tr><td>Gather</td><td>MPI_Allreduce MPI_Gather</td></tr><tr><td>Scatter</td><td>MPI_Scatter</td></tr><tr><td>All-to-all personalized</td><td>MPI_Alltoall</td></tr></table>

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\communications\page_003\communications_page_003\auto\images\1c37201bd0e1945a82c8e63ae89e0f7757480d82b3c751fc226d67230fb8a12c.jpg

---

## Lecture: output\communications\page_004\communications_page_004\auto

# Basic Communication Operations: Introduction

• Many interactions in practical parallel programs occur in well-defined patterns involving groups of processors.

Efficient implementations of these operations can improve performance, reduce development effort and cost, and improve software quality.

• Efficient implementations must leverage underlying architecture.

• We select a descriptive set of architectures to illustrate the process of algorithm design.

– Ring (linear array), two-dimensional Mesh, Hypercube

---

## Lecture: output\communications\page_005\communications_page_005\auto

# Basic Communication Operations: Introduction

• Group communication operations are built using point-topoint messaging primitives.

Communicating a message of size m over an uncongested network takes time $t _ { s } + t _ { w } { ^ { \star } } m .$

Where necessary, we take congestion into account explicitly by scaling the $t _ { w }$ term.

We assume that the network is bidirectional and that communication is single-ported.

---

## Lecture: output\communications\page_006\communications_page_006\auto

# One-to-All Broadcast and All-to-One Reduction

• One processor has a piece of data (of size m) it needs to send to everyone.

• The dual of one-to-all broadcast is all-to-one reduction.

• In all-to-one reduction, each processor has m units of data. These data items must be combined piece-wise (using some associative operator, such as addition or min), and the result made available at a target processo

---

## Lecture: output\communications\page_007\communications_page_007\auto

# One-to-All Broadcast and All-to-One Reduction

![](images/3034b2a1c089b0d9e6f4e7c113b0b1a32ac67927e0b19d37225afa18752a2399.jpg)

One-to-all broadcast and all-to-one reduction among processors.

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\communications\page_007\communications_page_007\auto\images\3034b2a1c089b0d9e6f4e7c113b0b1a32ac67927e0b19d37225afa18752a2399.jpg

---

## Lecture: output\communications\page_008\communications_page_008\auto

# One-to-All Broadcast and All-to-One Reduction on Rings

• Simplest way is to send p-1 messages from the source to the other p-1 processors - this is not very efficient.

Use recursive doubling: source sends a message to a selected processor. We now have two independent problems each on one half of the machines.

Reduction can be performed by inverting the broadcasting process.

---

## Lecture: output\communications\page_009\communications_page_009\auto

# One-to-All Broadcast

![](images/fa86b6cf595c398c45957d99379e3149979626aa752045a34154c9eb28a5ec8e.jpg)

One-to-all broadcast on an eight-node ring. Node 0 is the source of the broadcast. Each message transfer step is shown by a numbered, dotted arrow from the source of the message to its destination. The number on an arrow indicates the time step during which the message is transferred.

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\communications\page_009\communications_page_009\auto\images\fa86b6cf595c398c45957d99379e3149979626aa752045a34154c9eb28a5ec8e.jpg

---

## Lecture: output\communications\page_010\communications_page_010\auto

# All-to-One Reduction

![](images/4195a9faa1184066f8d2a081fb50c61b8fcafabc08870915a2ac03a4ab0035c5.jpg)

Reduction on an eight-node ring with node 0 as the destination of the reduction.

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\communications\page_010\communications_page_010\auto\images\4195a9faa1184066f8d2a081fb50c61b8fcafabc08870915a2ac03a4ab0035c5.jpg

---

## Lecture: output\communications\page_011\communications_page_011\auto

# Broadcast and Reduction: Example

Consider the problem of multiplying a matrix with a vector.

The n x n matrix is assigned to an n x n (virtual) processor grid. The vector is assumed to be on the first row of processors. The first step of the product requires a one-to-all broadcast of the vector element along the corresponding column of processors. This can be done concurrently for all n columns. The processors compute local product of the vector element and the local matrix entry. In the final step, the results of these products are accumulated to the first processor of each row using n concurrent all-to-one reduction operations along the rows (using the sum operation).

---

## Lecture: output\communications\page_012\communications_page_012\auto

# Broadcast and Reduction: Matrix-Vector Multiplication Example

![](images/5169adcd31f4161450a3f89d3afec7063ad4f3e6411b3eb27bced263a7a10b73.jpg)

One-to-all broadcast and all-to-one reduction in the multiplication of a 4 x 4 matrix with a 4 x 1 vector.

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\communications\page_012\communications_page_012\auto\images\5169adcd31f4161450a3f89d3afec7063ad4f3e6411b3eb27bced263a7a10b73.jpg

---

## Lecture: output\communications\page_013\communications_page_013\auto

# Broadcast and Reduction on a Mesh

• We can view each row and column of a square mesh of p nodes as a linear array of $\surd p$ nodes.

• Broadcast and reduction operations can be performed in two steps - the first step does the operation along a row and the second step along each column concurrently.

• This process generalizes to higher dimensions as well.

---

## Lecture: output\communications\page_014\communications_page_014\auto

# Broadcast and Reduction on a Mesh: Example

![](images/84ed05a41e843fa78aeb12736601b673dd27f4237b1ae130fa0d7da34b85fa4b.jpg)

One-to-all broadcast on a 16-node mesh.

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\communications\page_014\communications_page_014\auto\images\84ed05a41e843fa78aeb12736601b673dd27f4237b1ae130fa0d7da34b85fa4b.jpg

---

## Lecture: output\communications\page_015\communications_page_015\auto

# Broadcast and Reduction on a Hypercube

• A hypercube with 2d nodes can be regarded as a ddimensional mesh with two nodes in each dimension.

• The mesh algorithm can be generalized to a hypercube and the operation is carried out in $d \left( = I o g p \right)$ steps.

---

## Lecture: output\communications\page_016\communications_page_016\auto

# Broadcast and Reduction on a Hypercube: Example

![](images/14a8be3ba7e24e8f0460077e9f032aba754985ca8b3db45ac2858c7d4181247f.jpg)

One-to-all broadcast on a three-dimensional hypercube. The binary representations of node labels are shown in parentheses.

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\communications\page_016\communications_page_016\auto\images\14a8be3ba7e24e8f0460077e9f032aba754985ca8b3db45ac2858c7d4181247f.jpg

---

## Lecture: output\communications\page_017\communications_page_017\auto

# Broadcast and Reduction Algorithms

We illustrate the algorithm for a hypercube, but the algorithm can be adapted to other architectures.

• The hypercube has 2d nodes and my_id is the label for a node.

• X is the message to be broadcast, which initially resides at the source node 0.

---

## Lecture: output\communications\page_018\communications_page_018\auto

# Broadcast and Reduction Algorithms

1. procedure GENERAL_ONE_TO_ALL_BC(d, my_id, source, X)   
2. begin   
3. 4. $\begin{array} { l } { { m y \mathrm { { } } _ { - } v i r t u a l \mathrm { { } } _ { - } i d : = m y \mathrm { { } } _ { - } i d \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathsf { { \times } } \mathrm { { O R \ s o u r c e ; } } } } \\ { { m a s k : = 2 ^ { d } - 1 \mathrm { { : } } } } \end{array}$   
5. for $i : = d - 1$ downto 0 do/\*Outer loop\*/   
6. mask := mask XOR 2:/\*Set bit iofmaskto0\*/   
7. if $( m y _ { - } v i r t u a l _ { - } i d \mathsf { A N D } m a s k ) = 0$ then   
8. $\mathsf { \Pi } ^ { \mathsf { i f } } \left( m y \mathrm { - } v i r t u a l \mathrm { - } i d \mathsf { A N D \ 2 ^ { i } } \right) = \mathrm { 0 }$ then   
9. $\begin{array} { r } { v i r t u a l \_ d e s t : = m y \_ v i r t u a l \_ i d \times \mathsf { O R \ 2 ^ { \iota } } ; } \end{array}$   
10. send $X$ to (virtual_dest XOR source):   
/\* Convert virtual_dest to the label of the physical destination \*/   
11. else   
12. virtual_source := my-virtual_id XOR 2:   
13. receive $X$ from (virtual_source XOR source):   
/\* Convert virtual_source to the label of the physical source \*/   
14. endelse;   
15. endfor;   
16. end GENERAL_ONE_TO_ALL_BC

One-to-all broadcast of a message X from source on a hypercube. 18

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\communications\page_018\communications_page_018\auto\images\9e7c2d4190fa1b0cd384807f90a9f463194e8fb67b3a6f0524c7ee758566c009.jpg

---

## Lecture: output\communications\page_019\communications_page_019\auto

# Broadcast and Reduction Algorithms

1. procedure ALL_TO_ONE_REDUCE(d, my_id, m, X, sum)   
2. begin   
3. for $j : = 0 \dag \circ m - 1 \dag \circ s u m [ j ] : = X [ j ] ;$   
4. $m a s k : = 0 ;$   
5. for $i : = 0$ to $d - 1$ do   
$/ ^ { * } \mathsf { S e l e c } ^ { + } \mathsf { n o d e s } \mathsf { w h o s e } \mathsf { l o w e r } i \mathsf { b i f s c a r e }$ 0\*/   
6. if $( m y _ { - } i d \mathsf { A N D } m a s k ) = 0$ then   
7. if $( m y _ { - } i d \mathsf { A N D 2 } ^ { i } ) \neq 0$ then   
8. msg_destination := my_id XOR 2:   
9. send sum to msg_destination;   
10. else   
11. $m s g \_ s o u r c e : = m y \_ i d \times \mathsf { O R \ 2 ^ { i } } ;$   
12. receive $X$ from msg_source;   
13. for $j : = 0$ to $m - 1$ do   
14. $s u m [ j ] : = s u m [ j ] + X [ j ] ;$   
15. endelse;   
16. mask:= mask XOR $2 ^ { i }$ ;/\*Set bitiofmaskto1 \*   
17. endfor;   
18. end ALL_TO_ONE_REDUCE

Single-node accumulation on a $d .$ -dimensional hypercube. Each node contributes a message X containing m words, and node 0 is the destination. 19

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\communications\page_019\communications_page_019\auto\images\4bb08059e18b44da7ed830f582143d5671ea5e193563e656bdbd66203f52c145.jpg
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\communications\page_019\communications_page_019\auto\images\b71d1c9505470bf6b0b6374c222def93a709c4f7ea0b7ec44e6caf260fb91430.jpg
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\communications\page_019\communications_page_019\auto\images\f6aef1178f3288856b24765ace080a4d7f3165ed2b7475383e1c335a6434b66f.jpg
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\communications\page_019\communications_page_019\auto\images\f85105ab0df201bfbe9addf9253dd6063e43715755f0da03a2cbd0eedfa44235.jpg

---

## Lecture: output\communications\page_020\communications_page_020\auto

# Cost Analysis

The broadcast or reduction procedure involves log p rounds of point-to-point simple message transfers, each at a time cost of $t _ { s } + t _ { w } m$ .

• The total time is therefore given by:

$$
T = \left( t _ { s } + t _ { w } m \right) \log p .
$$

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\communications\page_020\communications_page_020\auto\images\b0fbb566090d62d9a445d8e25f691fc87e8df8a6adcdeb6c42866a8e5b1e2845.jpg

---

## Lecture: output\communications\page_021\communications_page_021\auto

# All-to-All Broadcast and Reduction

Generalization of broadcast in which each processor is the source as well as destination.

• A process sends the same m-word message to every other process, but different processes may broadcast different messages.

---

## Lecture: output\communications\page_022\communications_page_022\auto

# All-to-All Broadcast and Reduction

![](images/c4bd5eac1e8f2a919898748113973d0731ea81c0cf927dee24f3aed48cb09f40.jpg)

All-to-all broadcast and all-to-all reduction.

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\communications\page_022\communications_page_022\auto\images\c4bd5eac1e8f2a919898748113973d0731ea81c0cf927dee24f3aed48cb09f40.jpg

---

## Lecture: output\communications\page_023\communications_page_023\auto

# All-to-All Broadcast and Reduction on a Ring

• Simplest approach: perform p one-to-all broadcasts. This is not the most efficient way, though. Better as follows:

• Each node first sends to one of its neighbors the data it needs to broadcast.

• In subsequent steps, it forwards the data received from one of its neighbors to its other neighbor.

• The algorithm terminates in p-1 steps.

---

## Lecture: output\communications\page_024\communications_page_024\auto

# All-to-All Broadcast and Reduction on a Ring

![](images/b04d160cc25081eddd81809bfed9379d6534d94f7460224358cb1241fb58f919.jpg)

All-to-all broadcast on an eight-node ring.

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\communications\page_024\communications_page_024\auto\images\b04d160cc25081eddd81809bfed9379d6534d94f7460224358cb1241fb58f919.jpg

---

## Lecture: output\communications\page_025\communications_page_025\auto

# All-to-All Broadcast on a Ring

1. procedure ALL_TO_ALL_BC_RING   
2. begin   
3. $\begin{array} { r } { I e f f : = \left( m y _ { - } i d - 1 \right) } \end{array}$ mod p;   
4. $r i g h t { : = } \left( m y _ { - } i d + 1 \right)$ mod p;   
5. $r e s u | t : = m y _ { - } m s g ;$   
6. $m s g : = r e s u / \hbar ;$   
7. for $i : = 1$ to $p - 1$ do   
8. send msg to right;   
9. receive msg from lefft;   
10. result:= result U msg;   
11. endfor;   
12. end ALL_TO_ALL_BC_RING

All-to-all broadcast on a p-node ring.

---

## Lecture: output\communications\page_026\communications_page_026\auto

# All-to-all Broadcast on a Mesh

Performed in two phases - in the first phase, each row of the mesh performs an all-to-all broadcast using the procedure for the linear array.

• In this phase, all nodes collect √p messages corresponding to the √p nodes of their respective rows. Each node consolidates this information into a single message of size m√p.

• The second communication phase is a columnwise allto-all broadcast of the consolidated messages.

---

## Lecture: output\communications\page_027\communications_page_027\auto

# All-to-all Broadcast on a Mesh

![](images/55af2b5ab3b62cad96a0b26e53d4b96861163bfef89e38334b49bf58756d7bad.jpg)  
(a) Initial data distribution

![](images/c96c63254de49a0e90d34e1c7a74a2c17dcd6816ab46014f167974c9ca3285c7.jpg)  
(b) Data distribution after rowwise broadcast

All-to-all broadcast on a 3 x 3 mesh. The groups of nodes communicating with each other in each phase are enclosed by dotted boundaries. By the end of the second phase, all nodes get (0,1,2,3,4,5,6,7) (that is, a message from each node).

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\communications\page_027\communications_page_027\auto\images\55af2b5ab3b62cad96a0b26e53d4b96861163bfef89e38334b49bf58756d7bad.jpg
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\communications\page_027\communications_page_027\auto\images\c96c63254de49a0e90d34e1c7a74a2c17dcd6816ab46014f167974c9ca3285c7.jpg

---

## Lecture: output\communications\page_028\communications_page_028\auto

# All-to-all Broadcast on a Mesh

1. procedure ALL_TO_ALL_BC_MESH(my_id, my_msg, p, resulf)   
2. begin   
/\*Communication along rows \*/   
3. $I \Theta \dot { H } : = m y _ { - } i d - ( m y _ { - } i d \ : \mathsf { m o d } \ : \sqrt { p } ) + ( m y _ { - } i d - 1 ) \mathsf { m o d } \sqrt { p } ;$   
4. $r i g h ^ { \dagger } { : = m y _ { - } i d - \left( m y _ { - } i d \mathsf { m o d } \sqrt { p } \right) + \left( m y _ { - } i d + 1 \right) \mathsf { m o d } } \ ,$ √p:   
5. result := my_msg;   
6. $m s g : = r e s u 1 7 :$   
7. for $i : = 1$ to $\sqrt { p } - 1$ do   
8. send msg to right:   
9. receive msg from left:   
10. $r e s u 1 7 : = r e s u 1 7 + m s y :$   
11. endfor;   
/\* Communication along columns $x _ { j }$   
12. $U { \boldsymbol { \mathcal { P } } } : = \left( m y _ { - } i d - { \sqrt { p } } \right) { \bmod { p } } ;$   
13. $d o w n : = ( m y _ { - } i d + \sqrt { p } ) \bmod p ;$   
14. $m s g : = r e s u 1 1 \cdot$   
15. for $i : = 1$ to $\sqrt { p } - 1$ do   
16. send msg to down;   
17. receive msg from up:   
18. result $: =$ result U msg:   
19. endfor;   
20. end ALL_TO_ALL_BC_MESH

All-to-all broadcast on a square mesh of p nodes.

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\communications\page_028\communications_page_028\auto\images\0818c212b4e04b3f03a885f78d2cb0288ca0746b32075df14dc56922a2be6a1e.jpg
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\communications\page_028\communications_page_028\auto\images\844b6e47c10a2d806c0d35ee80efffa0f720ea5be69dc4ca8b2150d7f138abff.jpg

---

## Lecture: output\communications\page_029\communications_page_029\auto

# All-to-all broadcast on a Hypercube

Generalization of the mesh algorithm to log p dimensions.

• Message size doubles at each of the log p steps.

---

## Lecture: output\communications\page_030\communications_page_030\auto

# All-to-all broadcast on a Hypercube

![](images/a069f0b4e1d389d0e27a1bc5b827f7a8a027e5eadfa8eb2e6de5dc00496277a6.jpg)

All-to-all broadcast on an eight-node hypercube.

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\communications\page_030\communications_page_030\auto\images\a069f0b4e1d389d0e27a1bc5b827f7a8a027e5eadfa8eb2e6de5dc00496277a6.jpg

---

## Lecture: output\communications\page_031\communications_page_031\auto

# All-to-all broadcast on a Hypercube

1. procedure ALL_TO_ALL_BC_HCUBE(r   
2. begin   
3. result $: = m y _ { - } m s g ;$   
4. for $i : = 0$ to $d - 1$ do   
5. $p a r t n e r : = m y \_ i d \times \bigcirc \mathbb { R } \ 2 ^ { i } ;$   
6. send resul to partner;   
7. receive msg from partner;   
8. result $\mid =$ result U msg:   
9. endfor;   
10. end ALL_TO_ALL_BC_HCUBE

---

## Lecture: output\communications\page_032\communications_page_032\auto

# All-to-all Reduction

• Similar communication pattern to all-to-all broadcast, except in the reverse order. C On receiving a message, a node must combine it with the local copy of the message that has the same destination as the received message before forwarding the combined message to the next neighbor.

---

## Lecture: output\communications\page_033\communications_page_033\auto

# Cost Analysis

• On a ring, the time is given by: $( t _ { s } + t _ { w } m ) ( p - 1 )$ .

• On a mesh, the time is given by: $2 t _ { s } ( \surd p - 1 ) + t _ { w } m ( p - 1 ) .$ – Phase 1: $: ( t _ { s } + t _ { w } m ) ( \surd p - 1 )$ – Phase $2 \colon ( t _ { s } + t _ { w } m \setminus p ) ( \setminus p - 1 )$ //each message sizes m√ p

On a hypercube, we have:

$$
T = \sum _ { i = 1 } ^ { \log p } ( t _ { s } + 2 ^ { i - 1 } t _ { w } m )
$$

$$
= t _ { s } \log p + t _ { w } m ( p - 1 ) .
$$

These times are asymptotically optimal in message size.

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\communications\page_033\communications_page_033\auto\images\14ce885ce50c08697d2feaaffe178a5706cf8e0c503997d34323fe742f0cdb8a.jpg
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\communications\page_033\communications_page_033\auto\images\4763eb1ab4fd2d8ca2e157a5a852ca489aa68301075ac7b6566549f55c349060.jpg

---

## Lecture: output\communications\page_034\communications_page_034\auto

# The All-Reduce Operation

In all-reduce, each node starts with a buffer of size m and the final results of the operation are identical buffers of size m on each node that are formed by combining the original $p$ buffers using an associative operator.

All-reduce is identical to all-to-one reduction followed by a one-to-all broadcast. This formulation is not the most efficient on hypercubes.

• A more efficient way is to use the pattern of all-to-all broadcast. The only difference is to sum up the numbers (reduce) instead of accumulating messages. Time for this All-Reduce on hypercubes is $( t _ { s } + t _ { w } m )$ log p.

---

## Lecture: output\communications\page_035\communications_page_035\auto

# The Prefix-Sum Operation

Given p numbers $n _ { o } , n _ { 1 } , . . . , n _ { p - 1 }$ (one on each node), the problem is to compute the sums $\begin{array} { r } { s _ { k } = \sum _ { i } ^ { k } = o \ : n _ { i } } \end{array}$ for all k between 0 and $p - 1$ .

Initially, $n _ { k }$ resides on the node labeled $k$ , and at the end of the procedure, the same node holds $S _ { k }$ .

---

## Lecture: output\communications\page_036\communications_page_036\auto

# The Prefix-Sum Operation

![](images/3246d5328d106f6c39be766cc09514ef6229697fce5bc265e799bc4f2b72b10a.jpg)

Computing prefix sums on an eight-node hypercube.

Square brackets show the local prefix sum accumulated in the result buffer.   
Parentheses enclose the outgoing message buffer for the next step.

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\communications\page_036\communications_page_036\auto\images\3246d5328d106f6c39be766cc09514ef6229697fce5bc265e799bc4f2b72b10a.jpg

---

## Lecture: output\communications\page_037\communications_page_037\auto

# The Prefix-Sum Operation

The operation can be implemented using the all-to-all broadcast kernel.

We must account for the fact that in prefix sums the node with label k uses information from only the k-node subset whose labels are less than or equal to k.

This is implemented using an additional result buffer. The content of an incoming message is added to the result buffer only if the message comes from a node with a smaller label than the recipient node.

The contents of the outgoing message (denoted by parentheses in the figure) are updated with every incoming message.

---

## Lecture: output\communications\page_038\communications_page_038\auto

# The Prefix-Sum Operation

procedure PREFIX_SUMS_HCUBE(my_id, my_number, d, resu   
2. begin   
3. result := my−number;   
4. msg := result;   
5. for $i : = 0$ to d − 1 do   
6. partner := my_id XOR 2i;   
7. send msg to partner;   
8. receive number from partner;   
9. $m s g : = m s g + n u m b e r ;$   
10. if $( p o r t n e r < m y _ { - } i d )$ then result:= result + number;   
11. endfor;   
12. end PREFIX_SUMS_HCUBE

Prefix sums on a d-dimensional hypercube.

---

## Lecture: output\communications\page_039\communications_page_039\auto

# Scatter and Gather

• In the scatter operation, a single node sends a unique message of size m to every other node (also called a one-to-all personalized communication). In other words, each node starts with $p$ unique messages, each destined for one of the p nodes.

• In the gather operation, a single node collects a unique message from each node.

While the scatter operation is fundamentally different from broadcast, the algorithmic structure is similar, except for differences in message sizes (messages get smaller in scatter and stay constant in broadcast).

• The gather operation is exactly the inverse of the scatter operation and can be executed as such.

---

## Lecture: output\communications\page_040\communications_page_040\auto

# Gather and Scatter Operations

![](images/9e05b6803bb718d3b4036b8bcf5d09c070ae48b2842371e82f6f3d6287a6052c.jpg)

Scatter and gather operations.

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\communications\page_040\communications_page_040\auto\images\9e05b6803bb718d3b4036b8bcf5d09c070ae48b2842371e82f6f3d6287a6052c.jpg

---

## Lecture: output\communications\page_041\communications_page_041\auto

# Example of the Scatter Operation

![](images/2290c1a4c5898286ad0c96f3e056b991af1bb13c8d9f6f3fcdb9e39f713bae2c.jpg)

The scatter operation on an eight-node hypercube.

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\communications\page_041\communications_page_041\auto\images\2290c1a4c5898286ad0c96f3e056b991af1bb13c8d9f6f3fcdb9e39f713bae2c.jpg

---

## Lecture: output\communications\page_042\communications_page_042\auto

# Cost of Scatter and Gather

• There are log p steps, in each step, the number of nodes halves and the data size halves.

• We have the time for this operation to be:

$$
T = t _ { s } \log p + t _ { w } m ( p - 1 ) .
$$

• This time holds for a linear array as well as a 2-D mesh.   
• These times are asymptotically optimal in message size.

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\communications\page_042\communications_page_042\auto\images\2009132ec0711ef9fd5b035972b5662858b581559722e24892b7dab10e68e80b.jpg

---

## Lecture: output\communications\page_043\communications_page_043\auto

# All-to-All Personalized Communication

• Each node has a distinct message of size m for every other node. This is unlike all-to-all broadcast, in which each node sends the same message to all other nodes. All-to-all personalized communication is also known as total exchange.

---

## Lecture: output\communications\page_044\communications_page_044\auto

# All-to-All Personalized Communication

Mp-1,11   
  
$\mathrm { M } _ { 1 , 0 }$   
M0,0 M10 $\mathrm { M _ { p - 1 , 0 } }$ A1-l-al ained M0,0 M0,1 M 0,p-1   
0 1 p-1) 0 ① p-1)

All-to-all personalized communication.

---

## Lecture: output\communications\page_045\communications_page_045\auto

# All-to-All Personalized Communication: Example

Consider the problem of transposing a matrix. Each processor contains one full row of the matrix. The transpose operation in this case is identical to an allto-all personalized communication operation.

---

## Lecture: output\communications\page_046\communications_page_046\auto

# All-to-All Personalized Communication: Example

![](images/21e703939b6ef1f5ce1ff7f2a9d43daf38ed3ce35976c2d3586c913f655a5183.jpg)

All-to-all personalized communication in transposing a 4 x 4 matrix using four processes.

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\communications\page_046\communications_page_046\auto\images\21e703939b6ef1f5ce1ff7f2a9d43daf38ed3ce35976c2d3586c913f655a5183.jpg

---

## Lecture: output\communications\page_047\communications_page_047\auto

# All-to-All Personalized Communication on a Ring

• Each node sends all pieces of data as one consolidated message of size $m ( p - 1 )$ to one of its neighbors.

• Each node extracts the information meant for it from the data received, and forwards the remaining $( p - 2 )$ pieces of size m each to the next node.

• The algorithm terminates in p – 1 steps.

• The size of the message reduces by m at each step.

---

## Lecture: output\communications\page_048\communications_page_048\auto

# All-to-All Personalized Communication on a Ring

![](images/3d738dfd492d01e10617d2051a8643b3c1b6527bd26602685a97f5ee65ab0a97.jpg)

All-to-all personalized communication on a six-node ring. The label of each   
message is of the form $\{ x , y \}$ , where $\pmb { \chi }$ is the label of the node that originally owned the message, and $y$ is the label of the node that is the final   
destination of the message. The label $( \{ x _ { 1 } , y _ { 1 } \} , \{ x _ { 2 } , y _ { 2 } \} , . . . , \{ x _ { n } , y _ { n } \}$ , indicates a message that is formed by concatenating $n$ individual messages. 48

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\communications\page_048\communications_page_048\auto\images\3d738dfd492d01e10617d2051a8643b3c1b6527bd26602685a97f5ee65ab0a97.jpg

---

## Lecture: output\communications\page_049\communications_page_049\auto

# All-to-All Personalized Communication on a Ring: Cost

• We have p – 1 steps in all.

• In step i, the message size is $m ( p - i )$ .

The total time is given by:

$$
\begin{array} { r c l } { { T } } & { { = } } & { { \displaystyle \sum _ { i = 1 } ^ { p - 1 } ( t _ { s } + t _ { w } m ( p - i ) ) } } \\ { { } } & { { } } & { { } } \\ { { } } & { { = } } & { { \displaystyle t _ { s } ( p - 1 ) + \sum _ { i = 1 } ^ { p - 1 } i t _ { w } m } } \\ { { } } & { { } } & { { } } \\ { { } } & { { = } } & { { ( t _ { s } + t _ { w } m p / 2 ) ( p - 1 ) . } } \end{array}
$$

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\communications\page_049\communications_page_049\auto\images\97b531abe528ccf57a54d54ae96fd7ba156b3e2e7968c3ffc09bcc7233822466.jpg

---

## Lecture: output\communications\page_050\communications_page_050\auto

# All-to-All Personalized Communication on a Mesh

• Each node first groups its p messages according to the columns of their destination nodes.

• All-to-all personalized communication is performed independently in each row with clustered messages of size m√p.

• Messages in each node are sorted again, this time according to the rows of their destination nodes.

All-to-all personalized communication is performed independently in each column with clustered messages of size m√p.

---

## Lecture: output\communications\page_051\communications_page_051\auto

# All-to-All Personalized Communication on a Mesh

![](images/80b973575f3135bd51170bf3b70a25c3a801e041600e8e712872cb183e860708.jpg)  
(b) Data distribution at the beginning of second phase

The distribution of messages at the beginning of each phase of all-to-all personalized communication on a $3 \times 3$ mesh. At the end of the second phase, node i has messages $( \{ 0 , I \} , . . . , \{ 8 , i \} )$ , where $\textstyle 0 \leq i \leq 8$ . The groups of nodes communicating together in each phase are enclosed in dotted boundaries.

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\communications\page_051\communications_page_051\auto\images\80b973575f3135bd51170bf3b70a25c3a801e041600e8e712872cb183e860708.jpg

---

## Lecture: output\communications\page_052\communications_page_052\auto

# All-to-All Personalized Communication on a Mesh: Cost

Time for the first phase is identical to that in a ring with √p processors, i.e., $( t _ { s } + t _ { w } m p / 2 ) ( \surd p - 1 ) .$ .

Time in the second phase is identical to the first phase. Therefore, total time is twice of this time, i.e.,

$$
T = ( 2 t _ { s } + t _ { w } m p ) ( \sqrt { p } - 1 ) .
$$

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\communications\page_052\communications_page_052\auto\images\f3398092e1648bc61aca0336e70b848ebad061b47515c3baf47845d764d042dd.jpg

---

## Lecture: output\communications\page_053\communications_page_053\auto

# All-to-All Personalized Communication on a Hypercube

• Generalize the mesh algorithm to log p steps.

• At any stage in all-to-all personalized communication, every node holds p packets of size m each.

While communicating in a particular dimension, every node sends p/2 of these packets (consolidated as one message).

• A node must rearrange its messages locally before each of the log p communication steps.

---

## Lecture: output\communications\page_054\communications_page_054\auto

# All-to-All Personalized Communication on a Hypercube

![](images/841e2cc9d924b9a542762f387a09cbfd6b65aa67e8e66a58835a7d83cd70709a.jpg)

![](images/fd87234f510e8364b88961f7b328d41fe182b4853321c38651fd34df39c2555a.jpg)  
An all-to-all personalized communication algorithm on a three-dimensional hypercube.

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\communications\page_054\communications_page_054\auto\images\841e2cc9d924b9a542762f387a09cbfd6b65aa67e8e66a58835a7d83cd70709a.jpg
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\communications\page_054\communications_page_054\auto\images\fd87234f510e8364b88961f7b328d41fe182b4853321c38651fd34df39c2555a.jpg

---

## Lecture: output\communications\page_055\communications_page_055\auto

# All-to-All Personalized Communication on a Hypercube: Cost

• We have log p iterations and mp/2 words are communicated in each iteration. Therefore, the cost is:

$$
\begin{array} { r } { T = ( t _ { s } + t _ { w } m p / 2 ) \log p . } \end{array}
$$

This is not optimal!

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\communications\page_055\communications_page_055\auto\images\0c275a655369f03f0a221436b8ffd860533a06be5fd14adbd982f6b71aa1fbd4.jpg

---

## Lecture: output\communications\page_056\communications_page_056\auto

# All-to-All Personalized Communication on a Hypercube: Optimal Algorithm

Each node simply performs p – 1 communication steps, exchanging m words of data with a different node in every step.

• A node must choose its communication partner in each step so that the hypercube links do not suffer congestion.

• In the j th communication step, node i exchanges data with node (i XOR j).

• In this schedule, all paths in every communication step are congestion-free, and none of the bidirectional links carry more than one message in the same direction.

• The routing scheme is called E-cube routing.

---

## Lecture: output\communications\page_057\communications_page_057\auto

# All-to-All Personalized Communication on a Hypercube: Optimal Algorithm

![](images/9a4d1bf840957416f2bd83b3ce0b18e071212f845c7928fe2bdb83086119d5b3.jpg)  
Seven steps in all-to-all personalized communication on an eight-node hypercube.

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\communications\page_057\communications_page_057\auto\images\9a4d1bf840957416f2bd83b3ce0b18e071212f845c7928fe2bdb83086119d5b3.jpg

---

## Lecture: output\communications\page_058\communications_page_058\auto

# All-to-All Personalized Communication on a Hypercube: Optimal Algorithm

1. procedure ALL_TO_ALL_PERSONAL(d, my _id)   
2. begin   
3. for $i : = 1$ to $2 ^ { d } - 1$ do   
4. begin   
5. partner := my_id XOR $i$   
6. send $M _ { m y \_ i d , p a r t n e r }$ to partner;   
7. receive $M _ { p a r t n e r , m y \_ i d }$ from partner;   
8. endfor;   
9. end ALL_TO_ALL_PERSONAL

A procedure to perform all-to-all personalized communication on a ddimensional hypercube. The message $M _ { i , j }$ initially resides on node i and is destined for node $j$ .

---

## Lecture: output\communications\page_059\communications_page_059\auto

# All-to-All Personalized Communication on a Hypercube: Cost Analysis of Optimal Algorithm

• There are p – 1 steps and each step involves noncongesting message transfer of m words.

We have:

$$
T _ { = } ( t _ { s } + t _ { w } m ) ( p - 1 ) .
$$

• This is asymptotically optimal in message size.

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\communications\page_059\communications_page_059\auto\images\74894e32a330528af99c06aef5c00072d4650693ec1138105d024556dbcbff99.jpg

---

## Lecture: output\communications\page_060\communications_page_060\auto

# Improving Performance of Operations

Splitting and routing messages into parts: If the message can be split into p parts, a one-to-all broadcast can be implemented as a scatter operation followed by an all-toall broadcast operation. The time for this is:

$$
\begin{array} { l c l } { { T } } & { { = } } & { { 2 \times ( t _ { s } \log p + t _ { w } ( p - 1 ) { \frac { m } { p } } ) } } \\ { { } } & { { } } & { { } } \\ { { } } & { { \approx } } & { { 2 \times ( t _ { s } \log p + t _ { w } m ) . } } \end{array}
$$

All-to-one reduction can be performed by performing allto-all reduction (dual of all-to-all broadcast) followed by a gather operation (dual of scatter).

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\communications\page_060\communications_page_060\auto\images\9825ac17e7ed81afd64fa01a2f9c2d5255c5efa5d92477fc99d7621442a3f548.jpg

---

## Lecture: output\communications\page_061\communications_page_061\auto

# Improving Performance of Operations

Since an all-reduce operation is semantically equivalent to an all-to-one reduction followed by a one-to-all broadcast, the asymptotically optimal algorithms for these two operations can be used to construct a similar algorithm for the all-reduce operation.

---

## Lecture: output\communications\page_062\communications_page_062\auto

# Summary

Assume the algorithm most suitable for the given message size is chosen. These time bounds are valid for any architecture with a θ(p) cross-section bandwidth.   

<table><tr><td>Operation</td><td>Hypercube Time</td><td>B/W Requirement</td></tr><tr><td>One-to-all broadcast, All-to-one reduction</td><td>min((ts + twm) log p, 2(ts log p + twm))</td><td>Θ(1)</td></tr><tr><td>All-to-all broadcast, All-to-all reduction</td><td>ts log p + twm (p − 1)</td><td>Θ(1)</td></tr><tr><td>All-reduce</td><td>min((ts + tw m) 1log p, 2(ts log p + twm))</td><td>Θ(1)</td></tr><tr><td>Scatter, Gather</td><td>ts log p + tωm (p − 1)</td><td>Θ(1)</td></tr><tr><td>All-to-all personalized</td><td>(ts + twm)(p − 1)</td><td>Θ(p)</td></tr><tr><td>Circular shift</td><td>ts + tw m</td><td>Θ(p)</td></tr></table>

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\communications\page_062\communications_page_062\auto\images\421bfc157c457b14593ed52048e3cf9e3955faf949e27ae1383352a39892be87.jpg

---

## Lecture: output\cuda_memory\page_001\cuda_memory_page_001\auto

# Parallel Programming

CUDA Memories and Optimizations

---

## Lecture: output\cuda_memory\page_002\cuda_memory_page_002\auto

# Overview

• CUDA Memories – Registers, shared memory, global memory

• Memory optimizations – General memory optimizations – Use of shared memory

---

## Lecture: output\cuda_memory\page_003\cuda_memory_page_003\auto

# Memory and Registers in the Von-Neumann Model

![](images/98a187a4220c9e5d5543ed235006f23cc3d1b398d39b439f593e5bbfa846dbf4.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\cuda_memory\page_003\cuda_memory_page_003\auto\images\98a187a4220c9e5d5543ed235006f23cc3d1b398d39b439f593e5bbfa846dbf4.jpg

---

## Lecture: output\cuda_memory\page_004\cuda_memory_page_004\auto

# CUDA Memories in a Similar Model

![](images/0fcb170bd87c4839a628278150bbde73767864c3a4b1d1056224ae1c0175d30f.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\cuda_memory\page_004\cuda_memory_page_004\auto\images\0fcb170bd87c4839a628278150bbde73767864c3a4b1d1056224ae1c0175d30f.jpg

---

## Lecture: output\cuda_memory\page_005\cuda_memory_page_005\auto

# Programmer’s View of CUDA Memories

![](images/e38911a07bb8bea6aeaee51946b4be17deab3b812746690c0077d926d2d39055.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\cuda_memory\page_005\cuda_memory_page_005\auto\images\e38911a07bb8bea6aeaee51946b4be17deab3b812746690c0077d926d2d39055.jpg

---

## Lecture: output\cuda_memory\page_006\cuda_memory_page_006\auto

# Type Qualifiers of Device Variables

<table><tr><td rowspan=1 colspan=1>Variable declaration</td><td rowspan=1 colspan=1>Memory</td><td rowspan=1 colspan=1>Scope</td><td rowspan=1 colspan=1>Lifetime</td></tr><tr><td rowspan=1 colspan=1>int LocalVar;</td><td rowspan=1 colspan=1>register</td><td rowspan=1 colspan=1>thread</td><td rowspan=1 colspan=1>thread</td></tr><tr><td rowspan=1 colspan=1>_device_  _shared       int SharedVar;</td><td rowspan=1 colspan=1>shared</td><td rowspan=1 colspan=1>block</td><td rowspan=1 colspan=1>block</td></tr><tr><td rowspan=1 colspan=1>_device_                 int GlobalVar;</td><td rowspan=1 colspan=1>global</td><td rowspan=1 colspan=1>grid</td><td rowspan=1 colspan=1>application</td></tr><tr><td rowspan=1 colspan=1>_device_        _constant_ int ConstantVar;</td><td rowspan=1 colspan=1>constant</td><td rowspan=1 colspan=1>grid</td><td rowspan=1 colspan=1>application</td></tr></table>

__device__ is optional when used with __shared__, or __constant__

Automatic variables (variables declared without any of these qualifiers) reside in a register except per-thread arrays that reside in global memory

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\cuda_memory\page_006\cuda_memory_page_006\auto\images\884be9e730803e42f97d23451d5eb13e85f3b86d7cb0879736c175065f08525b.jpg

---

## Lecture: output\cuda_memory\page_007\cuda_memory_page_007\auto

# Global Memory

• Resides in device memory (high latency + high bandwidth)

• Accessed via 32-, 64-, or 128-byte memory transactions

– Addresses in a transaction must be aligned to these sizes.

– Memory accesses of the threads within a warp are coalesced into one or more of memory transactions depending on the size of the word accessed by each thread and the distribution of the memory addresses across the threads.

---

## Lecture: output\cuda_memory\page_008\cuda_memory_page_008\auto

# Local Memory

• Resides in device memory – Same latency and bandwidth as global memory access – Same requirements for memory coalescing – Access cached same way as global memory acce

Organized such that consecutive 32-bit words are accessed by consecutive thread IDs

– Accesses are therefore fully coalesced as long as all threads in a warp follow the access pattern

---

## Lecture: output\cuda_memory\page_009\cuda_memory_page_009\auto

# Constant Memory

• Resides in device memory Cached in the constant cache   
Accesses are split into separate memory requests depending on the addresses. – Each request is serviced at the throughput of the constant cache in case of a cache hit, or at the throughput of device memory otherwise.

---

## Lecture: output\cuda_memory\page_010\cuda_memory_page_010\auto

# Shared Memory

• On-chip – Much higher bandwidth and much lower latency than local or global memory   
• Divided into equally-sized memory modules, called banks, which can be accessed simultaneously – If two addresses of a memory request fall in the same memory bank, there is a bank conflict and the access has to be serialized.

---

## Lecture: output\cuda_memory\page_011\cuda_memory_page_011\auto

# Texture and Surface Memory

• Reside in device memory   
• Cached in texture cache – A texture fetch or surface read costs one memory read from device memory only on a cache miss, otherwise it just costs one read from texture cache.

The texture cache is optimized for 2D spatial locality, so threads of the same warp that read texture or surface addresses that are close together in 2D will achieve best performance.

---

## Lecture: output\cuda_memory\page_012\cuda_memory_page_012\auto

# Details of CUDA Memories

<table><tr><td rowspan=1 colspan=1>Memory</td><td rowspan=1 colspan=1>Location</td><td rowspan=1 colspan=1>Cached</td><td rowspan=1 colspan=1>Access</td><td rowspan=1 colspan=1>Who</td><td rowspan=1 colspan=1>Latency</td></tr><tr><td rowspan=1 colspan=1>Register</td><td rowspan=1 colspan=1>On-chip</td><td rowspan=1 colspan=1>Resident</td><td rowspan=1 colspan=1>Read/write</td><td rowspan=1 colspan=1>One thread</td><td rowspan=1 colspan=1>0(1 cycle)</td></tr><tr><td rowspan=1 colspan=1>Shared</td><td rowspan=1 colspan=1>On-chip</td><td rowspan=1 colspan=1>Resident</td><td rowspan=1 colspan=1>Read/write</td><td rowspan=1 colspan=1>Threads in block</td><td rowspan=1 colspan=1>O(1 cycle) w/o conflict</td></tr><tr><td rowspan=1 colspan=1>Global</td><td rowspan=1 colspan=1>off-chip</td><td rowspan=1 colspan=1>No/Yes</td><td rowspan=1 colspan=1>Read/write</td><td rowspan=1 colspan=1>All threads + host</td><td rowspan=1 colspan=1>0(1)- O(100) cycles, depending on if cached</td></tr><tr><td rowspan=1 colspan=1>Local</td><td rowspan=1 colspan=1>off-chip</td><td rowspan=1 colspan=1>No/Yes</td><td rowspan=1 colspan=1>Read/write</td><td rowspan=1 colspan=1>One thread</td><td rowspan=1 colspan=1>O(1)- 0(100) cycles, depending on if cached</td></tr><tr><td rowspan=1 colspan=1>Constant</td><td rowspan=1 colspan=1>Off-chip</td><td rowspan=1 colspan=1>Yes</td><td rowspan=1 colspan=1>Read only</td><td rowspan=1 colspan=1>All threads + host(host may write)</td><td rowspan=1 colspan=1>0(1)-0(100) cycles, depending on if cached</td></tr><tr><td rowspan=1 colspan=1>Texture</td><td rowspan=1 colspan=1>Off-chip</td><td rowspan=1 colspan=1>Yes</td><td rowspan=1 colspan=1>Read only</td><td rowspan=1 colspan=1>All threads + host(host may write)</td><td rowspan=1 colspan=1>O(1)- O(100) cycles, depending on if cached</td></tr><tr><td rowspan=1 colspan=1>Surface</td><td rowspan=1 colspan=1>off-chip</td><td rowspan=1 colspan=1>Yes</td><td rowspan=1 colspan=1>Read/write</td><td rowspan=1 colspan=1>All threads+host</td><td rowspan=1 colspan=1>0(1)-0(100) cycles, depending on if cached</td></tr></table>

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\cuda_memory\page_012\cuda_memory_page_012\auto\images\60e6b4719f102d92d0417c1dc5d8754f06e769f2f5796b928b6b1132300400a9.jpg

---

## Lecture: output\cuda_memory\page_013\cuda_memory_page_013\auto

# Targets of Memory Optimizations

# Reduce memory latency

– The latency of a memory access is the time (usually in cycles) between a memory request and its completion

• Maximize memory bandwidth – Bandwidth is the amount of useful data that can be retrieved over a time interval

• Manage overhead – Cost of performing optimization (e.g., copying) should be less than anticipated gain

---

## Lecture: output\cuda_memory\page_014\cuda_memory_page_014\auto

# Reuse and Locality

• Consider how data is accessed

# – Data reuse:

• Same data used multiple times

• Intrinsic in computation

# – Data locality:

• Data is reused and is present in “fast memory”

• Same data or same data transfer

• If a computation has reuse, what can we do to get locality?

• Appropriate data placement and layout

• Code reordering transformations

---

## Lecture: output\cuda_memory\page_015\cuda_memory_page_015\auto

# Data Placement: Conceptual

Copies from host to device go to some part of global memory (possibly, constant or texture memory)

• How to use shared memory • Must construct or be copied from global memory by kernel program

• How to use constant or texture cache – Read-only “reused” data can be placed in constant & texture memory by host

• How to use registers – Most locally-allocated data is placed directly in registers – Even array variables can use registers if compiler understands access patterns – Can allocate vectors to registers, e.g., float4 Excessive use of registers will “spill” data to local memory

---

## Lecture: output\cuda_memory\page_016\cuda_memory_page_016\auto

# Data Placement: Syntax

• Through type qualifiers – __constant__, __shared__, __device__

• Through cudaMemcpy calls – Any directions between host and device memories

Implicit default behavior

– Device memory without other qualifier is global memory – Host by default copies to global memory

– Thread-local variables go into registers unless capacity exceeded, then local memory

---

## Lecture: output\cuda_memory\page_017\cuda_memory_page_017\auto

# Common Programming Pattern of Using Shared Memory

• Load data into shared memory   
• Synchronize (if necessary) Operate on data in shared memory   
• Synchronize (if necessary) Write intermediate results to global memory Repeat until done

![](images/d572fa624d7b8bc5013195292376757b145148d01d1b9f31814fc92d3c9d46f3.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\cuda_memory\page_017\cuda_memory_page_017\auto\images\d572fa624d7b8bc5013195292376757b145148d01d1b9f31814fc92d3c9d46f3.jpg

---

## Lecture: output\cuda_memory\page_018\cuda_memory_page_018\auto

# Mechanics of Using Shared Memory

__shared__ type qualifier required • Must be allocated from global/device function, or as “extern”

Examples:

extern __shared__ float d_s_array[];   
__host__ void outerCompute() { compute<<<gs,bs>>>();   
}   
__global__ void compute() { d_s_array[i] = …;   
}

__global__ void compute2() { __shared__ float d_s_array[M];

// create or copy from global memory   
d_s_array[j] $=$ …;   
//synchronize threads before use   
__syncthreads();   
… = d_s_array[x]; // now can use any eleme   
// more synchronization needed if updated __syncthreads(); // may write result back to global memory d_g_array[j] $=$ d_s_array[j];   
}

---

## Lecture: output\cuda_memory\page_019\cuda_memory_page_019\auto

# Tiling for Limited Capacity Storage

Tiling can be used hierarchically to compute partial results on a block of data wherever there are capacity limitations

– Between grids if total data exceeds global memory capacity   
– Across thread blocks if shared data exceeds shared memory capacity (also to partition computation across blocks and threads) Within threads if data in registers exceeds register capacity or data in shared memory for block still exceeds shared memory capacity

---

## Lecture: output\cuda_memory\page_020\cuda_memory_page_020\auto

# Summary

Device variables reside in the global memory, the shared memory, or registers.   
CUDA memories have different latency and bandwidth characteristics.   
• Memory optimizations can be done through data placement and reuse.   
Tiling for the shared memory is a common memory optimization in CUDA programming.

---

## Lecture: output\cuda_programming_model\page_001\cuda_programming_model_page_001\auto

# Parallel Programming

CUDA Programming Model

---

## Lecture: output\cuda_programming_model\page_002\cuda_programming_model_page_002\auto

# Overview

• CUDA programming model – Host code and device code (kernel) – CUDA Threads: Grids, Blocks – CUDA memory allocation and copy – Kernel programs and their invocation • Simple CUDA program examples

---

## Lecture: output\cuda_programming_model\page_003\cuda_programming_model_page_003\auto

# CUDA: Compute Unified Device Architecture

• A parallel computing architecture developed by NVIDIA.

– Hardware: NVIDIA GPUs, from embedded devices, graphics cards for laptops and desktops, to dedicated server products for computation.

– Software

• Tool kit, device drivers, and programming SDK.

• Support C, Fortran, Matlab, and other languages.

• We teach CUDA C programming in this course

---

## Lecture: output\cuda_programming_model\page_004\cuda_programming_model_page_004\auto

# Host and Device Code

• A CUDA program consists of two parts: host and device (or kernel) code.

• Host code: executed on the CPU – Memory copy between the GPU and the CPU – Computation on the CPU and call GPU kernel

• Device code: executed on the GPU – GPU-based computation

• A CUDA program always starts from the host code, and then invokes the GPU kernels.

---

## Lecture: output\cuda_programming_model\page_005\cuda_programming_model_page_005\auto

# Processing Flow of a CUDA Program

![](images/827c238f80857702c90a0ae21678875ee63ef0732e2006482496a7ab467fa338.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\cuda_programming_model\page_005\cuda_programming_model_page_005\auto\images\827c238f80857702c90a0ae21678875ee63ef0732e2006482496a7ab467fa338.jpg

---

## Lecture: output\cuda_programming_model\page_006\cuda_programming_model_page_006\auto

# Threads in a CUDA Kernel

Each kernel corresponds to a grid of threads. Each grid consists of multiple thread blocks. Each thread block contains multiple threads.

![](images/cb577c8767ac8c6bbbf15f3124c6540d2cf8fa29cf65049da957b28a3800a3bb.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\cuda_programming_model\page_006\cuda_programming_model_page_006\auto\images\cb577c8767ac8c6bbbf15f3124c6540d2cf8fa29cf65049da957b28a3800a3bb.jpg

---

## Lecture: output\cuda_programming_model\page_007\cuda_programming_model_page_007\auto

# Grid and Block Dimensions

A grid consists of i  
dimension $( \mathsf { i } = 1 , 2 , 3 )$ blocks. – gridDim.x, gridDim.y, gridDim.z

A thread block contains threads organized in 1-3 dimensions

blockDim.x, blockDim.y, blockDim.z.

Any unspecified dimension is set to size 1.

![](images/1f56a25f08e498e53088e57ddee7e3b67d57e1ea3620832c9d9655c043be53f6.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\cuda_programming_model\page_007\cuda_programming_model_page_007\auto\images\1f56a25f08e498e53088e57ddee7e3b67d57e1ea3620832c9d9655c043be53f6.jpg

---

## Lecture: output\cuda_programming_model\page_008\cuda_programming_model_page_008\auto

# Block and Thread IDs

Threads and blocks have built-in IDs

Block ID: (blockIdx.x,   
blockIdx.y, blockIdx.z)   
Thread ID: 1D, 2D, or   
3D within a block   
(threadIdx.x,   
threadIdx.y,   
threadIdx.z)

# Device

![](images/0282962c4ac29b8576fd1ead62a1b2a2b7a97deda1373bc8ead9705e0029b9ae.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\cuda_programming_model\page_008\cuda_programming_model_page_008\auto\images\0282962c4ac29b8576fd1ead62a1b2a2b7a97deda1373bc8ead9705e0029b9ae.jpg

---

## Lecture: output\cuda_programming_model\page_009\cuda_programming_model_page_009\auto

# Device Code (Kernel)

• The device code is the same for each thread.

• A kernel function has the prefix __global__, and has a void return type. __global__ void kernel1(param1, …)

Note: device code has no direct access to main memory.

---

## Lecture: output\cuda_programming_model\page_010\cuda_programming_model_page_010\auto

# Kernel Invocation in Host Code

kernelName<<<#block, #thread, shared_size, s>>> (param1, …)

#block: number of thread blocks in the grid #thread: number of threads per block shared_size: optional; size of shared memory per block, default 0.

s: optional; the associated stream, default 0.

---

## Lecture: output\cuda_programming_model\page_011\cuda_programming_model_page_011\auto

# Memory Management in Host Code

• GPU memory management functions – GPU memory allocation: cudaMalloc(devPtr, size) cudaFree(devPtr) – Memory copy: cudaMemcpy(dst, src, size, direction) direction: cudaMemcpyHostToDevice, cudaMemcpyDeviceToHost

Note: host code has no direct access to GPU memory.

---

## Lecture: output\cuda_programming_model\page_012\cuda_programming_model_page_012\auto

# CUDA Memory Hierarchy

![](images/c067460ab7b101001af9e1b92a55594a5f3566e9838c8b0532b1b52489acd151.jpg)

Registers: only available within a thread.

Shared memory: accessed by threads in the same thread block.

Global memory: can be accessed by all threads.

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\cuda_programming_model\page_012\cuda_programming_model_page_012\auto\images\c067460ab7b101001af9e1b92a55594a5f3566e9838c8b0532b1b52489acd151.jpg

---

## Lecture: output\cuda_programming_model\page_013\cuda_programming_model_page_013\auto

# A Simple Program on the CPU

int main() int+h_A,+h_B,+h_C; inti; int $\tt { N } = \tt { 4 0 9 6 }$ ; size_t size $=$ N \* sizeof(int); h_A $=$ (int\*)malloc(size); $\mathrm { ~ h ~ } \mathbb { B } =$ (int\*)malloc(size); hc $=$ (int\*)malloc(size); $\mathrm { ~ i ~ } = \mathrm { ~ 0 ~ }$ $\mathrm { ~ i ~ } < \mathbb { N }$ $\dot { 2 } + +$ ) h_c[i] $=$ h_A[i] $^ +$ h_B[i]; free(h_A); free(h_B); free(h_c); return 0; “d_”(device).

A recommended common practice is to name a host-resident structure with the prefix $\cdot$ (host), and a device-resident structure with

---

## Lecture: output\cuda_programming_model\page_014\cuda_programming_model_page_014\auto

# CUDA Program: Set Up on the Host

# Host code

int main()

int+h_A，+h_B，+h_C，d_A，d_B，+d_C;   
intN $=$ 4096;   
size_t size $=$ N \* sizeof(int); // Allocate input vectors h_A and h_B in host memory h_A $=$ (int\*)malloc(size);   
h_B $=$ (int\*)malloc(size);   
h_c $=$ (int\*)malloc(size);   
for (int i $\qquad = \quad 0$ ;i $<$ N;i++)   
{ h_A[i]=i, h_B[i]= i;   
}

// Allocate vectors in device memory cudaMalloc((void\*\*)&d_A,size); cudaMalloc((void\*\*)&dB,size); cudaMalloc((void\*\*)&dc, size);

// copy vectors from host memory to device memory cudaMemcpy(d_A, h_A, size, cudaMemcpyHostToDevice); cudaMemcpy(d_B,h_B, size, cudaMemcpyHostToDevice);

---

## Lecture: output\cuda_programming_model\page_015\cuda_programming_model_page_015\auto

# CUDA Program: Invoke the Kernel

# // Invoke kernel

int threadsPerBlock= 256;   
int blocksPerGrid = N / threadsPerBlock;   
VecAdd<<<blocksPerGrid,threadsPerBlock>>>(d_A,d_B,d_C);

---

## Lecture: output\cuda_programming_model\page_016\cuda_programming_model_page_016\auto

# CUDA Program: The Device Code

// Device code _global_void VecAdd(int\* A，int\*B,int+C) inti $=$ blockDim.x + blockIdx.x + threadIdx.x; C[i] = A[i] + B[i]; } Block1 Block2 Block3 1 it1 t2 t3 t4it1 t2 t3 t4 t1 t2 t3 t4！

---

## Lecture: output\cuda_programming_model\page_017\cuda_programming_model_page_017\auto

# CUDA Program: Wrap Up on the Host

![](images/136066faeab4de0bd67e1b6212fe3fb5a5cc168f8e09f4320bbca5252ad6a1bf.jpg)

// Copy result from device memory to host memory // h_C contains the result in host memory cudaMemcpy(h_C, d_C, size, cudaMemcpyDeviceToHost);

//Free host memory free(h_A) ;   
free(h_B);   
free(h_C);

//Eree device memory cudaFree(d_A); cudaFree(d_B); cudaFree(d_C);

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\cuda_programming_model\page_017\cuda_programming_model_page_017\auto\images\136066faeab4de0bd67e1b6212fe3fb5a5cc168f8e09f4320bbca5252ad6a1bf.jpg

---

## Lecture: output\cuda_programming_model\page_018\cuda_programming_model_page_018\auto

# Another Example

• Given an array of n elements, increment each element.

• A C program without CUDA

for(int i = 0; i < n; i++) { h data[i] += 1;

---

## Lecture: output\cuda_programming_model\page_019\cuda_programming_model_page_019\auto

# The Parallelization on the GPU

• Shall we still make one thread handle one element?

Maybe not…

– The numbers of blocks and threads for a kernel have a limit, e.g., up to 65535 blocks and 1024 threads per block.

– A suitable number of threads should balance the degree of parallelism and resource usage.

• We may need to make each thread handle multiple elements for a large number of elements.

---

## Lecture: output\cuda_programming_model\page_020\cuda_programming_model_page_020\auto

# Two Parallelization Methods

![](images/d483d7674bcff58fa06c2b9d41cdb596ff4f90fa252dd82c1f3e5f9c110ab08b.jpg)

![](images/e88090c5a78e62ea02b775f0ce8810929cf8802aed62ae378be313887b700bd7.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\cuda_programming_model\page_020\cuda_programming_model_page_020\auto\images\d483d7674bcff58fa06c2b9d41cdb596ff4f90fa252dd82c1f3e5f9c110ab08b.jpg
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\cuda_programming_model\page_020\cuda_programming_model_page_020\auto\images\e88090c5a78e62ea02b775f0ce8810929cf8802aed62ae378be313887b700bd7.jpg

---

## Lecture: output\cuda_programming_model\page_021\cuda_programming_model_page_021\auto

# Coalesced Access

• If memory addresses accessed by threads in the same thread block are consecutive, then these memory accesses are grouped into one memory transaction.

Non-coalesced

![](images/565ab6f08a6c84e52aa58307a59cfd1650e01413c2b469856f20a2e135790e2d.jpg)

Coalesced

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\cuda_programming_model\page_021\cuda_programming_model_page_021\auto\images\565ab6f08a6c84e52aa58307a59cfd1650e01413c2b469856f20a2e135790e2d.jpg

---

## Lecture: output\cuda_programming_model\page_022\cuda_programming_model_page_022\auto

# The GPU Kernel with Coalesced Access

void kernel2(int\* d data, const int numElement) { $=$

for(int i = tid; i < numElement; i += nthread) { d_data[i] += 1;

<table><tr><td>t1 ↓</td><td>t2</td><td>t3</td><td>t4</td><td>t1</td><td>t2</td><td>t3</td><td>t4</td><td>t1</td><td>t2</td><td>t3</td><td>t4 </td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\cuda_programming_model\page_022\cuda_programming_model_page_022\auto\images\7fc8e3e8e0bd9e51ec28d678f894eaf3e8cdd9143f5f583abb2c23ae115905cf.jpg

---

## Lecture: output\cuda_programming_model\page_023\cuda_programming_model_page_023\auto

# Performance Comparison

![](images/21dc32384941e09949b1ab7d7096e8c1935e44bf01781bcce565333135f3520d.jpg)

1. Coalesced access is crucial for utilizing the GPU memory bandwidth.   
2. A badly-written GPU program may be even slower than a CPU program!

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\cuda_programming_model\page_023\cuda_programming_model_page_023\auto\images\21dc32384941e09949b1ab7d7096e8c1935e44bf01781bcce565333135f3520d.jpg

---

## Lecture: output\cuda_programming_model\page_024\cuda_programming_model_page_024\auto

# Measure Kernel Execution Time

• Kernel execution is asynchronous.

• To measure the elapsed time of a kernel, we need a synchronization between the host and device.

cudaEvent_t start, stop;   
cudaEventCreate(&start);   
cudaEventCreate(&stop);   
cudaEventRecord(start, 0);   
kernel1<<<1024, 512>>>(d_data);   
cudaEventRecord(stop, 0);   
cudaEventSynchronize(stop);   
float elapsedTime;   
cudaEventElapsedTime(&elapsedTime, start, stop);   
printf("Kernel elapsed time: %.3f ms\n", elapsedTime)

---

## Lecture: output\cuda_programming_model\page_025\cuda_programming_model_page_025\auto

# Summary

• A CUDA program consists of host and device code.

• The host code is in charge of GPU memory allocation, data transfer between the GPU and the CPU, and kernel launching.

• A kernel program is executed by every thread in a grid structure.

• Coalesced access effectively utilizes GPU memory bandwidth.

---

## Lecture: output\cuda_threads\page_001\cuda_threads_page_001\auto

# Parallel Programming

CUDA Threads

---

## Lecture: output\cuda_threads\page_002\cuda_threads_page_002\auto

# Overview

Thread Mapping Warp Scheduling Control Divergence

---

## Lecture: output\cuda_threads\page_003\cuda_threads_page_003\auto

# A Multi-Dimensional Grid Example

![](images/88427415be91035e19ff0cf5fdeb677e83e34b823ccfcecc86cb372b55e0b424.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\cuda_threads\page_003\cuda_threads_page_003\auto\images\88427415be91035e19ff0cf5fdeb677e83e34b823ccfcecc86cb372b55e0b424.jpg

---

## Lecture: output\cuda_threads\page_004\cuda_threads_page_004\auto

# Transparent Scalability

![](images/514a7ce867b0fd57da098f2bb4b04dc8599396d3747a3dec68994d11ed6ecaf0.jpg)

• Each block can execute in any order relative to others. Hardware is free to assign blocks to any processor at any time – A kernel scales to any number of parallel processors

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\cuda_threads\page_004\cuda_threads_page_004\auto\images\514a7ce867b0fd57da098f2bb4b04dc8599396d3747a3dec68994d11ed6ecaf0.jpg

---

## Lecture: output\cuda_threads\page_005\cuda_threads_page_005\auto

# Example: Executing Thread Blocks

Threads are assigned to Streaming Multiprocessors (SM) in block granularity

– Up to 8 blocks to each SM as resource allows – Fermi SM can take up to 1536 threads

Could be 256 (threads/block) $\yen 6$ blocks • Or 512 (threads/block) $\yen 3$ blocks, etc.

SM maintains thread/block idx #s

SM manages/schedules thread execution

![](images/63bb8d17d89f7ddfabfbbf09040b4c21ea215c510e2be381857943ec0b29c59d.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\cuda_threads\page_005\cuda_threads_page_005\auto\images\63bb8d17d89f7ddfabfbbf09040b4c21ea215c510e2be381857943ec0b29c59d.jpg

---

## Lecture: output\cuda_threads\page_006\cuda_threads_page_006\auto

# Warps as Scheduling Units

![](images/38e1146ac14a0917394f6e8e6e98aca74d50ce945132b813db30ba778be3c58b.jpg)

• Each block is divided into 32-thread warps

– An implementation technique, not part of the CUDA programming mod   
– Warps are scheduling units in SM Threads in a warp execute in Single Instruction Multiple Data (SIMD) manner   
– The number of threads in a warp may vary in future generations

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\cuda_threads\page_006\cuda_threads_page_006\auto\images\38e1146ac14a0917394f6e8e6e98aca74d50ce945132b813db30ba778be3c58b.jpg

---

## Lecture: output\cuda_threads\page_007\cuda_threads_page_007\auto

# Warps in Multi-dimensional Thread Blocks

• The thread blocks are first linearized into 1D in row major order: x followed by y followed by z

![](images/6e76ffc008b12809af4306f2ef16f48d80094cb317a961d2dae1015b5a4b8d10.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\cuda_threads\page_007\cuda_threads_page_007\auto\images\6e76ffc008b12809af4306f2ef16f48d80094cb317a961d2dae1015b5a4b8d10.jpg

---

## Lecture: output\cuda_threads\page_008\cuda_threads_page_008\auto

# Blocks are partitioned after linearization

• Linearized thread blocks are partitioned – Thread indices within a warp are consecutive and increasing – Warp 0 starts with Thread 0

• Partitioning scheme is consistent across devices

– Thus you can use this knowledge in control flow – However, the exact size of warps may change from generation to generation

• DO NOT rely on any ordering within or between warps – If there are any dependencies between threads, you must __syncthreads() to get correct results.

---

## Lecture: output\cuda_threads\page_009\cuda_threads_page_009\auto

# SMs are SIMD Processors

Control unit for is shared among processing units

![](images/b316079b141df9c4c848e0d52088688ac282ec6a28732a8beeae99b76c430444.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\cuda_threads\page_009\cuda_threads_page_009\auto\images\b316079b141df9c4c848e0d52088688ac282ec6a28732a8beeae99b76c430444.jpg

---

## Lecture: output\cuda_threads\page_010\cuda_threads_page_010\auto

# SIMD Execution Among Threads in a Warp

• All threads in a warp must execute the same instruction at any point in time

This works efficiently if all threads follow the same control flow path

– All if-then-else statements make the same decision – All loops iterate the same number of times

---

## Lecture: output\cuda_threads\page_011\cuda_threads_page_011\auto

# Control Divergence

Control divergence occurs when threads in a warp take different control flow paths by making different control decisions

– Some take the then-path and others take the else-path of an ifstatement – Some threads take different number of loop iterations than others

The execution of threads taking different paths are serialized in current GPUs

– The control paths taken by the threads in a warp are traversed one at a time until there is no more. During the execution of each path, all threads taking that path will be executed in parallel The number of different paths can be large when considering nested control flow statements

---

## Lecture: output\cuda_threads\page_012\cuda_threads_page_012\auto

# Control Divergence Examples

Divergence can arise when branch or loop condition is a function of thread indices

Example kernel statement with divergence: – if (threadIdx.x > 2) { } – This creates two different control paths for threads in a block Decision granularity $<$ warp size; threads 0, 1 and 2 follow different path than the rest of the threads in the first warp • Example without divergence: – If (blockIdx.x > 2) { } Decision granularity is a multiple of blocks size; all threads in any given warp follow the same path

---

## Lecture: output\cuda_threads\page_013\cuda_threads_page_013\auto

# Example: Vector Addition Kernel

// Compute vector sum C = A + B // Each thread performs one pair-wise addition

# global

void vecAddKernel(float\* A, float\* B, float\* C, int n)   
{ int i = threadIdx.x + blockDim.x \* blockIdx.x;   
if(i<n) C[i] = A[i] + B[i];

---

## Lecture: output\cuda_threads\page_014\cuda_threads_page_014\auto

# Analysis for vector size of 1,000 elements

Assume that block size is 256 threads – 8 warps in each block

All threads in Blocks 0, 1, and 2 are within valid range – i values from 0 to 767 – There are 24 warps in these three blocks, none will have control divergen

• Most warps in Block 3 will not control divergence – Threads in the warps 0-6 are all within valid range, thus no control divergence

One warp in Block 3 will have control divergence

– Threads with i values 992-999 will all be within valid range – Threads with i values of 1000-1023 will be outside valid range

Effect of serialization on control divergence will be small

– 1 out of 32 warps has control divergence – The impact on performance will likely be less than 3%

---

## Lecture: output\cuda_threads\page_015\cuda_threads_page_015\auto

# Performance Impact of Control Divergence

Boundary condition checks are vital for complete functionality and robustness of parallel code

– The tiled matrix multiplication kernel has many boundary condition checks The concern is that these checks may cause significant performance degradation

if(Row < Width && t \* TILE_WIDTH+tx < Width) {

ds_M[ty][tx] $\underline { { \underline { { \mathbf { \delta \pi } } } } }$ M[Row \* Width $^ +$ t \* TILE_WIDTH + tx]; } else { ds_M[ty][tx] = 0.0; }

if (t\*TILE_WIDTH+ty < Width && Col < Width) {

ds_N[ty][tx] = N[(t\*TILE_WIDTH + ty) \* Width $^ +$ Col]; } else { ds_N[ty][tx] = 0.0; }

---

## Lecture: output\cuda_threads\page_016\cuda_threads_page_016\auto

# Two types of blocks in loading M Tiles

1. Blocks whose tiles are all within valid range until the last phase.

2. Blocks whose tiles are partially outside the valid range all the way

![](images/7ddedc88eaea706a627561f8b5c47f03f9bd360b22d32d9df51ef1b728bbae33.jpg)  
Type 1

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\cuda_threads\page_016\cuda_threads_page_016\auto\images\7ddedc88eaea706a627561f8b5c47f03f9bd360b22d32d9df51ef1b728bbae33.jpg

---

## Lecture: output\cuda_threads\page_017\cuda_threads_page_017\auto

# Analysis of Control Divergence Impact

• Assume 16x16 tiles and thread blocks

• Each thread block has 8 warps (256/32)

• Assume square matrices of 100x100

• Each thread will go through 7 phases (ceiling of 100/16)

• There are 49 thread blocks (7 in each dimension)

---

## Lecture: output\cuda_threads\page_018\cuda_threads_page_018\auto

# Control Divergence in Loading M Tiles

Assume 16x16 tiles and thread blocks

Each thread block has 8 warps (256/32)

Assume square matrices of 100x100

Each warp will go through 7 phases (ceiling of 100/16)

There are 42 $( 6 ^ { * } 7 )$ Type 1 blocks, with a total of 336 $( 8 ^ { * } 4 2 )$ warps

They all have 7 phases, so there are 2,352 $( 3 3 6 ^ { * } 7 )$ ) warp-phases

The warps have control divergence only in their last phase

336 warp-phases have control divergence

![](images/10ed1c4f1e514cc75396a1342bf361a90d9481e7a422e6344bad5c8716dea879.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\cuda_threads\page_018\cuda_threads_page_018\auto\images\10ed1c4f1e514cc75396a1342bf361a90d9481e7a422e6344bad5c8716dea879.jpg

---

## Lecture: output\cuda_threads\page_019\cuda_threads_page_019\auto

# Control Divergence in Loading M Tiles (Type 2)

Type 2: the 7 blocks assigned to load the bottom tiles, with a total of 56 (8\*7) warps They all have 7 phases, so there are 392 (56\*7) warpphases The first 2 warps in each Type 2 block will stay within the valid range until the last phase The 6 remaining warps stay outside the valid range So, only 14 $( 2 ^ { * } 7 )$ warp-phases have control divergence

![](images/58acc39e80d8cef01eb3b97090d10291beeeabd660cecc6931d0bdf515696bbe.jpg)  
Type 2

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\cuda_threads\page_019\cuda_threads_page_019\auto\images\58acc39e80d8cef01eb3b97090d10291beeeabd660cecc6931d0bdf515696bbe.jpg

---

## Lecture: output\cuda_threads\page_020\cuda_threads_page_020\auto

# Overall Impact of Control Divergence

• Type 1 Blocks: 336 out of 2,352 warp-phases have control divergence Type 2 Blocks: 14 out of 392 warp-phases have control divergence Type 1 The performance impact is expected to be less than 12% (350/2,944 or Type 2 (336+14)/(2352+14))

![](images/581204b51261f681149d41de9161a0a005cc39c5b45a3298bb962d0108a06a03.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\cuda_threads\page_020\cuda_threads_page_020\auto\images\581204b51261f681149d41de9161a0a005cc39c5b45a3298bb962d0108a06a03.jpg

---

## Lecture: output\cuda_threads\page_021\cuda_threads_page_021\auto

# Additional Comments

• The estimated performance impact is data dependent. – For larger matrices, the impact will be significantly smaller

In general, the impact of control divergence for boundary condition checking for large input data sets should be insignificant

– One should not hesitate to use boundary checks to ensure full functionality

The fact that a kernel is full of control flow constructs does not mean that there will be heavy occurrence of control divergence

---

## Lecture: output\cuda_threads\page_022\cuda_threads_page_022\auto

# Summary

• Threads are transparently mapped to processors.   
• Threads are scheduled in the unit of warps   
• Branch code does not necessarily cause control divergence.   
• Control divergence is data dependent.

---

## Lecture: output\gpu_architecture\page_001\gpu_architecture_page_001\auto

# Parallel Programming

GPU Architecture

Acknowledgement: Some graphics and examples are taken from various online resources, including NVIDIA web sites and lecture slides of Prof. Wen-mei Hwu.

---

## Lecture: output\gpu_architecture\page_002\gpu_architecture_page_002\auto

# Overview

• Modern GPUs have a massively parallel architecture.

– We use NVIDIA CUDA-enabled GPU as example.

• How are they different from CPUs?

• Where do GPUs fit in parallel architectures?

---

## Lecture: output\gpu_architecture\page_003\gpu_architecture_page_003\auto

# Von Neumann Machine (1947)

• Fetch-and-Execute cycle on the CPU: – Fetch instructions and data from memory – Execute instructions on ALU

![](images/15b254f0ed1305e5d01a288a6071f7cb617f578303104ab976bb188b4aa67514.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\gpu_architecture\page_003\gpu_architecture_page_003\auto\images\15b254f0ed1305e5d01a288a6071f7cb617f578303104ab976bb188b4aa67514.jpg

---

## Lecture: output\gpu_architecture\page_004\gpu_architecture_page_004\auto

# Modern CPU Architecture

![](images/f778fe4904190571b9d3c7ee42ccbcc795ef1b31bd279a54616018a596990b42.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\gpu_architecture\page_004\gpu_architecture_page_004\auto\images\f778fe4904190571b9d3c7ee42ccbcc795ef1b31bd279a54616018a596990b42.jpg

---

## Lecture: output\gpu_architecture\page_005\gpu_architecture_page_005\auto

# Parallelism in CPUs

• Multiple physical cores   
• Hyper Threading (HT) or Simultaneous Multithreading (SMT) – Map each physical core to two logical processors

• Instructional level parallelism (ILP) – Divide each instruction into stages and pipeline multiple independent instructions by stages

---

## Lecture: output\gpu_architecture\page_006\gpu_architecture_page_006\auto

# Graphics Processing Unit (GPU)

![](images/8fb58aeb22ad4ca39b3211c1bc52ef20563b1139a46890e85019398589ce494e.jpg)

Traditionally used for game (3D rendering) applications Currently major accelerators for general-purpose computing applications that exhibit data parallelism Work as co-processors, i.e., rely on the CPU for task control, memory allocation, data transfer, etc.

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\gpu_architecture\page_006\gpu_architecture_page_006\auto\images\8fb58aeb22ad4ca39b3211c1bc52ef20563b1139a46890e85019398589ce494e.jpg

---

## Lecture: output\gpu_architecture\page_007\gpu_architecture_page_007\auto

# Traditional GPU Pipeline

Input from CPU (geometry information)

![](images/9ff4e614435885de54c4c1fa6a997176453dcc152f50af93b1963beceeb9a407.jpg)

Traditional graphics hardware abstraction Limited programmability (only highlighted stages programmable)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\gpu_architecture\page_007\gpu_architecture_page_007\auto\images\9ff4e614435885de54c4c1fa6a997176453dcc152f50af93b1963beceeb9a407.jpg

---

## Lecture: output\gpu_architecture\page_008\gpu_architecture_page_008\auto

#

General  
purpose   
Fully   
programma   
ble   
Massively   
parallel

![](images/e483834e42e8ac51131ef4d2b0f804303cf6ddb95a6912c54d418066590b4e9c.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\gpu_architecture\page_008\gpu_architecture_page_008\auto\images\e483834e42e8ac51131ef4d2b0f804303cf6ddb95a6912c54d418066590b4e9c.jpg

---

## Lecture: output\gpu_architecture\page_009\gpu_architecture_page_009\auto

# Comparison of CPU and GPU

![](images/d375087d53404526a6227a49791c947fea2421a5c7814030fc918f957dbdf585.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\gpu_architecture\page_009\gpu_architecture_page_009\auto\images\d375087d53404526a6227a49791c947fea2421a5c7814030fc918f957dbdf585.jpg

---

## Lecture: output\gpu_architecture\page_010\gpu_architecture_page_010\auto

# GPU and CPU

![](images/549073970228d99301460bad339f8a454fb14b94bd6eaafbdb7c53777fd334cc.jpg)

Host

Device

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\gpu_architecture\page_010\gpu_architecture_page_010\auto\images\549073970228d99301460bad339f8a454fb14b94bd6eaafbdb7c53777fd334cc.jpg

---

## Lecture: output\gpu_architecture\page_011\gpu_architecture_page_011\auto

# Classification of Parallel Architecture

<table><tr><td>ＳIＳＤ Single Instruction, Single Data</td><td>ＳＩＭＤ Single Instruction, Multiple Data</td></tr><tr><td>A serial (non-parallel) computer Oldest type of computers</td><td>A type of parallel computer Synchronous execution Suitable for data-parallel applications Examples: GPUs</td></tr><tr><td>MＩＳD Multiple Instruction, Single Data</td><td>ＭＩＭＤ Multiple Instruction, Multiple Data</td></tr><tr><td>A type of parallel computer A single data stream is fed into multiple processing units. Few actual examples</td><td>most common type of parallel computer synchronous or asynchronous Examples: Supercomputers, clusters, multicore PCs</td></tr></table>

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\gpu_architecture\page_011\gpu_architecture_page_011\auto\images\384eab17436a0c4f667af503bcbd12de0e733dae99b114a539e1d37424dfc73c.jpg

---

## Lecture: output\gpu_architecture\page_012\gpu_architecture_page_012\auto

# Illustrations of Execution Flows

![](images/0344ae0a49f4869e0dc1a538b8aac358a5cfac4a5c1b6216fc6a7b0f2717819c.jpg)

Example adapted from https://computing.llnl.gov/tutorials/parallel_comp

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\gpu_architecture\page_012\gpu_architecture_page_012\auto\images\0344ae0a49f4869e0dc1a538b8aac358a5cfac4a5c1b6216fc6a7b0f2717819c.jpg

---

## Lecture: output\gpu_architecture\page_013\gpu_architecture_page_013\auto

# SIMT Architecture of NVIDIA GPU

• Single Instruction Multiple Threads – Instruction-level parallelism within a single thread – Thread-level parallelism through simultaneous hardware multithreading

• Each multiprocessor creates, manages, schedules, and executes CUDA threads in groups of 32, called warps. • Branch divergence occurs only within a warp; different warps execute independently regardless of whether they are executing common or disjoint code paths.

---

## Lecture: output\gpu_architecture\page_014\gpu_architecture_page_014\auto

# SIMT vs SIMD

• Similar: a single instruction controls multiple processing units.

Different:

– SIMD vector organizations expose the SIMD width to the software

• E.g., data items are required to aligned into vectors of a fixed size.

– SIMT instructions specify the execution and branching behavior of a single thread

• For simplicity, the programmer can ignore the SIMT behavior; however, substantial performance improvements can be realized by taking care of it.

---

## Lecture: output\gpu_architecture\page_015\gpu_architecture_page_015\auto

# CPU vs GPU Threads

CPU threads are much more heavyweight than GPU threads to create and maintain.

• Typically there are tens of concurrent CPU threads in a CPU program whereas there can be 1,000s to 10,000s of concurrent GPU threads in a GPU program.

• In a CPU program, threads may execute different code; in a GPU program, typically all threads execute the same piece of code (called a kernel).

---

## Lecture: output\gpu_architecture\page_016\gpu_architecture_page_016\auto

# NVIDIA GPU Memory Hierarchy

Registers:   
smallest, fastest on-chip memory On-chip shared memory: small, fast, software  
managed   
consistency   
Off-chip device memory: high  
bandwidth,   
high-latency

![](images/54a1aa7ecc6a4ef266f986f4e6f46997cb931642dd03bb10483970d8fb22d539.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\gpu_architecture\page_016\gpu_architecture_page_016\auto\images\54a1aa7ecc6a4ef266f986f4e6f46997cb931642dd03bb10483970d8fb22d539.jpg

---

## Lecture: output\gpu_architecture\page_017\gpu_architecture_page_017\auto

# Putting it Together

![](images/f0db345c2b32d14d521dc462e884e7e762cf5131f79a8d6ca56dd7b6ce4a697a.jpg)

• 10s\~100s of identical streaming multiprocessors (SMs) 10s of identical uniprocessors (cores) in a multiprocessor => Hundreds to thousands of cores, or thread processors

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\gpu_architecture\page_017\gpu_architecture_page_017\auto\images\f0db345c2b32d14d521dc462e884e7e762cf5131f79a8d6ca56dd7b6ce4a697a.jpg

---

## Lecture: output\gpu_architecture\page_018\gpu_architecture_page_018\auto

# GPU versus CPU: Performance Trend

![](images/9441a2685842824220557e62f8c1508e414fb4a415dc78ce7ad170af3fdce811.jpg)  
Peak Memory Bandwidth (GB/s)

![](images/c9e66404fff98d54612419d12e1b12cbe9312af46984dffdd4a63072f01f6e1b.jpg)  
Peak Double Precision (GFLOPs)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\gpu_architecture\page_018\gpu_architecture_page_018\auto\images\9441a2685842824220557e62f8c1508e414fb4a415dc78ce7ad170af3fdce811.jpg
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\gpu_architecture\page_018\gpu_architecture_page_018\auto\images\c9e66404fff98d54612419d12e1b12cbe9312af46984dffdd4a63072f01f6e1b.jpg

---

## Lecture: output\gpu_architecture\page_019\gpu_architecture_page_019\auto

# GPGPU Applications

• 3D real-time graphics   
• Weather and climate forecast and simulation   
• Molecular dynamics Computational finance Bioinformatics   
• Computational physics and chemistry

---

## Lecture: output\gpu_architecture\page_020\gpu_architecture_page_020\auto

# Issues about GPU Architecture

• Co-processor nature   
Bus transfer bandwidth   
• Suitable mainly for data-parallel applications   
Unusual memory hierarchy   
• Programmer-responsible correctness   
• Programmer-responsible optimizations   
• High power consumption

---

## Lecture: output\gpu_architecture\page_021\gpu_architecture_page_021\auto

# Summary

• GPUs are highly parallel architectures. – Single Instruction Multiple Thread – Support a massive number of threads – Threads scheduled in unit of warps

• They are suitable for many data-parallel, computation-intensive applications.

• Programming GPU requires architectural considerations.

---

## Lecture: output\hardwareOS\page_001\hardwareOS_page_001\auto

# Introduction to High-Performance and Parallel Computing

# are and

Slides adapted from the lecture notes by Peter Pacheco

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\hardwareOS\page_001\hardwareOS_page_001\auto\images\70fad6eee5b04dc1f58cc12d904ed967908bd8572f6fd838aa94280c1fab976d.jpg

---

## Lecture: output\hardwareOS\page_002\hardwareOS_page_002\auto

# Roadmap

• Some background • Modifications to the von Neumann model • Computer hardware and OS review

---

## Lecture: output\hardwareOS\page_003\hardwareOS_page_003\auto

SOME BACKGROUND

---

## Lecture: output\hardwareOS\page_004\hardwareOS_page_004\auto

Serial hardware and software

![](images/aba93d8940870dc15f70e7e328be88782eeecf8a429c25e6f6a154ee57119e56.jpg)

![](images/e3b96b56fba822ad499d5bab0c99369a749878798ab0056f4a5b9e7c0447f856.jpg)

output

Computer runs one program at a time.

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\hardwareOS\page_004\hardwareOS_page_004\auto\images\aba93d8940870dc15f70e7e328be88782eeecf8a429c25e6f6a154ee57119e56.jpg
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\hardwareOS\page_004\hardwareOS_page_004\auto\images\e3b96b56fba822ad499d5bab0c99369a749878798ab0056f4a5b9e7c0447f856.jpg

---

## Lecture: output\hardwareOS\page_005\hardwareOS_page_005\auto

# The von Neumann Architecture

![](images/1f389066a01a648bed4b0a6fb4ae2852f9423eb3738097b4e052dc3ff151ff28.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\hardwareOS\page_005\hardwareOS_page_005\auto\images\1f389066a01a648bed4b0a6fb4ae2852f9423eb3738097b4e052dc3ff151ff28.jpg

---

## Lecture: output\hardwareOS\page_006\hardwareOS_page_006\auto

# Main memory

• It is a collection of locations, each of which is capable of storing both instructions and data. Every location consists of an address, which is used to access the location, and the contents of the location.

![](images/2dcf16abb3edb850f91a78a631e5a53394a0903f5e0012eae7da32b9555549dd.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\hardwareOS\page_006\hardwareOS_page_006\auto\images\2dcf16abb3edb850f91a78a631e5a53394a0903f5e0012eae7da32b9555549dd.jpg

---

## Lecture: output\hardwareOS\page_007\hardwareOS_page_007\auto

# Central processing unit (CPU)

Two components:

• Control unit - responsible for deciding which instruction in a program should be executed. (the boss)

• Arithmetic and logic unit (ALU) - responsible for executing the actual instructions. (the worker)

---

## Lecture: output\hardwareOS\page_008\hardwareOS_page_008\auto

# Key terms

• Register – very fast storage, part of the CPU.

• Program counter – stores address of the next instruction to be executed.

• Bus – wires that connect the CPU and memory.

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\hardwareOS\page_008\hardwareOS_page_008\auto\images\dce828c9dd8fa7f0c18ac57e230517281603a5da7fa65a37433d32b41e3a79dc.jpg

---

## Lecture: output\hardwareOS\page_009\hardwareOS_page_009\auto

memory

![](images/9e9a5c472fb87a9a050788466bcd3f2479b1fde20d98adebeae48f2934e20890.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\hardwareOS\page_009\hardwareOS_page_009\auto\images\9e9a5c472fb87a9a050788466bcd3f2479b1fde20d98adebeae48f2934e20890.jpg

---

## Lecture: output\hardwareOS\page_010\hardwareOS_page_010\auto

![](images/0b678a1a75b1be9ada6be0e33e341301a2d1691736416c9118b5c362e0b2772d.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\hardwareOS\page_010\hardwareOS_page_010\auto\images\0b678a1a75b1be9ada6be0e33e341301a2d1691736416c9118b5c362e0b2772d.jpg

---

## Lecture: output\hardwareOS\page_011\hardwareOS_page_011\auto

# von Neumann bottleneck

The separation of memory and CPU

The limited storage capacity of the CPU means that large amounts of data and instructions must be transferred from the memory The interconnect determines the rate at which instructions and data can be accessed The CPU can execute instructions orders of magnitude faster than memory access

---

## Lecture: output\hardwareOS\page_012\hardwareOS_page_012\auto

# An operating system “Process”

• An instance of a computer program that is being executed.   
• Components of a process: – The executable machine language program. – A block of memory. – Descriptors of resources the OS has allocated t the process. – Security information. – Information about the state of the process.

---

## Lecture: output\hardwareOS\page_013\hardwareOS_page_013\auto

# Multitasking

• Gives the illusion that a single processor system is running multiple programs simultaneously.

• Each process takes turns running. (time slice)

• After its time is up, it waits until it has a turn again. (blocks)

---

## Lecture: output\hardwareOS\page_014\hardwareOS_page_014\auto

# Threading

• Threads are contained within processes. • They allow programmers to divide their programs into (more or less) independent tasks. • The hope is that when one thread blocks because it is waiting on a resource, another will have work to do and can run.

---

## Lecture: output\hardwareOS\page_015\hardwareOS_page_015\auto

# A process and two threads

the “master” thread

![](images/334e5e5d5ab68368a4ad428a88a54640b4cad67771b96d8c2de0d1aea555353d.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\hardwareOS\page_015\hardwareOS_page_015\auto\images\334e5e5d5ab68368a4ad428a88a54640b4cad67771b96d8c2de0d1aea555353d.jpg

---

## Lecture: output\hardwareOS\page_016\hardwareOS_page_016\auto

# MODIFICATIONS TO THE VON NEUMANN MODEL

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\hardwareOS\page_016\hardwareOS_page_016\auto\images\5b7272a8f5051841d20bc74860f12e38bc2e05f61021cb0d89932310e6a78cda.jpg

---

## Lecture: output\hardwareOS\page_017\hardwareOS_page_017\auto

# Caches

• A collection of memory locations that can be accessed in less time than some other memory locations.

• A CPU cache is typically located on the same chip, or one that can be accessed much faster than ordinary memory.

---

## Lecture: output\hardwareOS\page_018\hardwareOS_page_018\auto

# Locality

• The same or nearby locations are accessed frequently.

• Spatial locality – accessing a nearby location.

• Temporal locality – accessing in the near future.

---

## Lecture: output\hardwareOS\page_019\hardwareOS_page_019\auto

# Example of locality

float z[1000];  
$\mathsf { s u m } = 0 . 0$ ;  
for $( \mathfrak { i } = 0 ; \mathfrak { i } < 1 0 0 0 ; \mathfrak { i } + + )$ sum += z[i];

---

## Lecture: output\hardwareOS\page_020\hardwareOS_page_020\auto

# Levels of Cache

![](images/da3f87a636aa0417ed1a6a4e03d692e4a4d43b5d4f8700255f34b17d64d00d8a.jpg)

![](images/f04ea587d303821f79ca3ef54473d06368e931d0b10e0c9dd8c20a9e4eb2756c.jpg)

largest & slowest

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\hardwareOS\page_020\hardwareOS_page_020\auto\images\da3f87a636aa0417ed1a6a4e03d692e4a4d43b5d4f8700255f34b17d64d00d8a.jpg
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\hardwareOS\page_020\hardwareOS_page_020\auto\images\f04ea587d303821f79ca3ef54473d06368e931d0b10e0c9dd8c20a9e4eb2756c.jpg

---

## Lecture: output\hardwareOS\page_021\hardwareOS_page_021\auto

# Cache hit

L2

y z total

L3

A[ ] radius r1 center

---

## Lecture: output\hardwareOS\page_022\hardwareOS_page_022\auto

# Cache miss

L3

![](images/14491cf01f5c451961a449aa963b036a2651d5323d4846cf0fdf0734bf531bf2.jpg)

L2

r1 z total

A[ ] radius center

![](images/5a1e8751e59f372be615042963a42aa26ea8532de2fae69630fa9642e8657fef.jpg)

main memory

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\hardwareOS\page_022\hardwareOS_page_022\auto\images\14491cf01f5c451961a449aa963b036a2651d5323d4846cf0fdf0734bf531bf2.jpg
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\hardwareOS\page_022\hardwareOS_page_022\auto\images\5a1e8751e59f372be615042963a42aa26ea8532de2fae69630fa9642e8657fef.jpg

---

## Lecture: output\hardwareOS\page_023\hardwareOS_page_023\auto

# Issues with writes

• When a CPU writes data to cache, the value in cache may be inconsistent with the value in main memory.

– Write-through caches handle this by updating the data in main memory at the time it is written to cache.

– Write-back caches mark data in the cache as dirty When the cache line is replaced by a new cache line from memory, the dirty line is written to memory.

---

## Lecture: output\hardwareOS\page_024\hardwareOS_page_024\auto

# Cache mapping

• Full associative – a new line can be placed at any location in the cache.

Direct mapped – each cache line has a unique location in the cache to which it will be assigned.

• n-way set associative – each cache line can be place in one of n different locations in the cache.

---

## Lecture: output\hardwareOS\page_025\hardwareOS_page_025\auto

# Example

<table><tr><td rowspan=2 colspan=1>Memory Index</td><td rowspan=1 colspan=3>Cache Location</td></tr><tr><td rowspan=1 colspan=1>Fully Assoc</td><td rowspan=1 colspan=1>Direct Mapped</td><td rowspan=1 colspan=1>2-way</td></tr><tr><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0, 1, 2, or 3</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0 or 1</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0, 1, 2, or 3</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2or3</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>0, 1, 2, or 3</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>0 or 1</td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>0, 1, 2, or 3</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>2or 3</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>0, 1, 2, or 3</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0or1</td></tr><tr><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>0, 1, 2, or 3</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2or 3</td></tr><tr><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>0, 1, 2, or 3</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>0or1</td></tr><tr><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>0, 1, 2, or 3</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>2or3</td></tr><tr><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1>0, 1, 2, or 3</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0or1</td></tr><tr><td rowspan=1 colspan=1>9</td><td rowspan=1 colspan=1>0, 1, 2, or 3</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2or3</td></tr><tr><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>0, 1, 2, or 3</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>0or1</td></tr><tr><td rowspan=1 colspan=1>11</td><td rowspan=1 colspan=1>0, 1, 2, or 3</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>2 or 3</td></tr><tr><td rowspan=1 colspan=1>12</td><td rowspan=1 colspan=1>0, 1, 2, or 3</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0or1</td></tr><tr><td rowspan=1 colspan=1>13</td><td rowspan=1 colspan=1>0, 1, 2, or 3</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2or 3</td></tr><tr><td rowspan=1 colspan=1>14</td><td rowspan=1 colspan=1>0, 1, 2, or 3</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>0or1</td></tr><tr><td rowspan=1 colspan=1>15</td><td rowspan=1 colspan=1>0, 1, 2, or 3</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>2 or 3</td></tr></table>

Assignments of a 16-line main memory to a 4-line cache

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\hardwareOS\page_025\hardwareOS_page_025\auto\images\9f070f08a4d9544ad82a6ee9a30109eead48e6f9c372103f6ddf215e2c90338f.jpg

---

## Lecture: output\hardwareOS\page_026\hardwareOS_page_026\auto

# Cache Eviction

• Caches are much smaller than main memory.   
• When the cache is full, bringing a new line in memory needs to replace or evict a line in the cache. Common cache eviction policies include LRU/MRU (Least/Most Recently Used) and LFU (Least Frequently Used).

---

## Lecture: output\hardwareOS\page_027\hardwareOS_page_027\auto

# Caches and programs

double A[MAx ][MAx]，x[MAx],Y[MAx];   
/\* Initialize A and x, assigi   
/\* First pair of loops \*/   
for (i = 0; i < MAX; i++) for (j = 0;j< MAX;j++) y[i] += A[i][j]\*x[j];   
/\* Assign y = 0 \*/   
/\* Second pair of loops \*/   
for （j = 0;j< MAX；j++) for (i = 0; i < MAX; i++) y[i]+=A[i][j]\*x[j];

<table><tr><td rowspan=1 colspan=1>Cache Line</td><td rowspan=1 colspan=4>Elements of A</td></tr><tr><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>A[0][0]</td><td rowspan=1 colspan=1>A[0][1]</td><td rowspan=1 colspan=1>A[0] [2]</td><td rowspan=1 colspan=1>A[0][3]</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>A[1][0]</td><td rowspan=1 colspan=1>A[1] [1]</td><td rowspan=1 colspan=1>A[11 [2]</td><td rowspan=1 colspan=1>A[1][3]</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>A[2][0]</td><td rowspan=1 colspan=1>A[2][1]</td><td rowspan=1 colspan=1>A[2] [2]</td><td rowspan=1 colspan=1>A[2] [3]</td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>A[3] [0]</td><td rowspan=1 colspan=1>A[3][1]</td><td rowspan=1 colspan=1>A[3] [2]</td><td rowspan=1 colspan=1>A[3] [3]</td></tr></table>

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\hardwareOS\page_027\hardwareOS_page_027\auto\images\ff2234465bc353c3fdccd72a78468a763f42d84ddb08a7a033b86cd42ce18334.jpg

---

## Lecture: output\hardwareOS\page_028\hardwareOS_page_028\auto

# Virtual memory (1)

• If we run a very large program or a program that accesses very large data sets, all of the instructions and data may not fit into main memory.

• Virtual memory functions as a cache for secondary storage.

---

## Lecture: output\hardwareOS\page_029\hardwareOS_page_029\auto

# Virtual memory (2)

• It exploits the principle of spatial and temporal locality.

• It only keeps the active parts of running programs in main memory.

---

## Lecture: output\hardwareOS\page_030\hardwareOS_page_030\auto

# Virtual memory (3)

• Swap space – an area of secondary storage that keeps the inactive (parts of) running programs.

• Pages – blocks of data and instructions. – Most systems have a fixed page size that currently ranges from 4 to 16 kilobytes.

---

## Lecture: output\hardwareOS\page_031\hardwareOS_page_031\auto

# Virtual memory (4)

main memory

![](images/541bf3c3bfc9795734a7d1c92e8ee5a2b74b9e2f6a67e6ca074ea191c4407229.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\hardwareOS\page_031\hardwareOS_page_031\auto\images\541bf3c3bfc9795734a7d1c92e8ee5a2b74b9e2f6a67e6ca074ea191c4407229.jpg

---

## Lecture: output\hardwareOS\page_032\hardwareOS_page_032\auto

# Virtual page numbers

When a program is compiled its pages are assigned virtual page numbers.

• When the program is run, a table is created that maps the virtual page numbers to physical addresses.

• A page table is used to translate the virtual address into a physical address.

---

## Lecture: output\hardwareOS\page_033\hardwareOS_page_033\auto

# Virtual Address

<table><tr><td rowspan=1 colspan=11>Virtual Address</td></tr><tr><td rowspan=1 colspan=5>Virtual Page Number</td><td></td><td rowspan=1 colspan=5>Byte Offset</td></tr><tr><td rowspan=1 colspan=1>31</td><td rowspan=1 colspan=1>30</td><td rowspan=1 colspan=1>」」</td><td rowspan=1 colspan=1>13</td><td rowspan=1 colspan=1>12</td><td></td><td rowspan=1 colspan=1>11</td><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>」   」</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>」」-</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1</td><td></td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>ı 」」</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1</td></tr></table>

Virtual Address Divided into Virtual Page Number and Byte Offset

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\hardwareOS\page_033\hardwareOS_page_033\auto\images\a154afc8be8365285785b23f265e44bd1e79e9c83dc3ef1b053c755fcfcdd3d1.jpg

---

## Lecture: output\hardwareOS\page_034\hardwareOS_page_034\auto

# Translation-lookaside buffer (TLB)

• Using a page table has the potential to significantly increase each program’s overall run-time.

• TLB is a special address translation cache in the processor.

---

## Lecture: output\hardwareOS\page_035\hardwareOS_page_035\auto

# Translation-lookaside buffer (2)

• It caches a small number of entries (typically 16–512) from the page table in very fast memory.

• Page fault – attempting to access a valid physical address for a page in the page table but the page is only stored on disk.

---

## Lecture: output\hardwareOS\page_036\hardwareOS_page_036\auto

# Instruction Level Parallelism (ILP)

Attempts to improve processor performance by having multiple processor components or functional units simultaneously executing instructions.

---

## Lecture: output\hardwareOS\page_037\hardwareOS_page_037\auto

# Instruction Level Parallelism (2)

• Pipelining - functional units are arranged in stages.

Multiple issue - multiple instructions can be simultaneously initiated.

---

## Lecture: output\hardwareOS\page_038\hardwareOS_page_038\auto

![](images/d1cc0ffedab2978f31fe43bf46f6924cd3dc330ec16c50db8c290646597fcd6b.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\hardwareOS\page_038\hardwareOS_page_038\auto\images\d1cc0ffedab2978f31fe43bf46f6924cd3dc330ec16c50db8c290646597fcd6b.jpg

---

## Lecture: output\hardwareOS\page_039\hardwareOS_page_039\auto

# Pipelining example (1)

<table><tr><td rowspan=1 colspan=1>Time</td><td rowspan=1 colspan=1>Operation</td><td rowspan=1 colspan=1>Operand 1</td><td rowspan=1 colspan=1>Operand 2</td><td rowspan=1 colspan=1>Result</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>Fetch operands</td><td rowspan=1 colspan=1>9.87× 104</td><td rowspan=1 colspan=1>6.54× 103</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>Compare exponents</td><td rowspan=1 colspan=1>9.87 ×104</td><td rowspan=1 colspan=1>6.54× 103</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>Shift one operand</td><td rowspan=1 colspan=1>9.87 × 104</td><td rowspan=1 colspan=1>0.654× 104</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>Add</td><td rowspan=1 colspan=1>9.87× 104</td><td rowspan=1 colspan=1>0.654× 104</td><td rowspan=1 colspan=1>10.524× 104</td></tr><tr><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>Normalize result</td><td rowspan=1 colspan=1>9.87 × 104</td><td rowspan=1 colspan=1>0.654× 104</td><td rowspan=1 colspan=1>1.0524× 103</td></tr><tr><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>Round result</td><td rowspan=1 colspan=1>9.87 × 104</td><td rowspan=1 colspan=1>0.654× 104</td><td rowspan=1 colspan=1>1.05 × 105</td></tr><tr><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>Store result</td><td rowspan=1 colspan=1>9.87 × 104</td><td rowspan=1 colspan=1>0.654× 104</td><td rowspan=1 colspan=1>1.05 × 105</td></tr></table>

Add the floating point numbers 9.87×104 and 6.54×103

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\hardwareOS\page_039\hardwareOS_page_039\auto\images\027814227dbd7600f4e9b10e3c3bce936d244aea5b25e2b6ff391b8b59fcad75.jpg

---

## Lecture: output\hardwareOS\page_040\hardwareOS_page_040\auto

# Pipelining example (2)

float x[1000]， y[1000], z[1000]; for $l \dot { ~ } \dot { ~ } = ~ 0$ ;i<1000；i++) z [i] = x[i] + y [i];

• Assume each operation takes one nanosecond (10-9 seconds).

This for loop takes about 7000 nanoseconds.

---

## Lecture: output\hardwareOS\page_041\hardwareOS_page_041\auto

# Pipelining (3)

Divide the floating point adder into 7 separate pieces of hardware or functional units.   
First unit fetches two operands, second unit compares exponents, etc.   
Output of one functional unit is input to the next.

---

## Lecture: output\hardwareOS\page_042\hardwareOS_page_042\auto

# Pipelining (4)

<table><tr><td rowspan=1 colspan=1>Time</td><td rowspan=1 colspan=1>Fetch</td><td rowspan=1 colspan=1>Compare</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Add</td><td rowspan=1 colspan=1>Shift  Add  Normalize</td><td rowspan=1 colspan=1>Round</td><td rowspan=1 colspan=1>Store</td></tr><tr><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>:</td><td rowspan=1 colspan=1>:</td><td rowspan=1 colspan=1>:</td><td rowspan=1 colspan=1>:</td><td rowspan=1 colspan=1>:</td><td rowspan=1 colspan=1>:</td><td rowspan=1 colspan=1>:</td><td rowspan=1 colspan=1>:</td></tr><tr><td rowspan=1 colspan=1>999</td><td rowspan=1 colspan=1>999</td><td rowspan=1 colspan=1>998</td><td rowspan=1 colspan=1>997</td><td rowspan=1 colspan=1>996</td><td rowspan=1 colspan=1>995</td><td rowspan=1 colspan=1>994</td><td rowspan=1 colspan=1>993</td></tr><tr><td rowspan=1 colspan=1>1000</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>999</td><td rowspan=1 colspan=1>998</td><td rowspan=1 colspan=1>997</td><td rowspan=1 colspan=1>996</td><td rowspan=1 colspan=1>995</td><td rowspan=1 colspan=1>994</td></tr><tr><td rowspan=1 colspan=1>1001</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>999</td><td rowspan=1 colspan=1>998</td><td rowspan=1 colspan=1>997</td><td rowspan=1 colspan=1>996</td><td rowspan=1 colspan=1>995</td></tr><tr><td rowspan=1 colspan=1>1002</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>999</td><td rowspan=1 colspan=1>998</td><td rowspan=1 colspan=1>997</td><td rowspan=1 colspan=1>996</td></tr><tr><td rowspan=1 colspan=1>1003</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>999</td><td rowspan=1 colspan=1>998</td><td rowspan=1 colspan=1>997</td></tr><tr><td rowspan=1 colspan=1>1004</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>[</td><td rowspan=1 colspan=1>999</td><td rowspan=1 colspan=1>998</td></tr><tr><td rowspan=1 colspan=1>1005</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>999</td></tr></table>

Pipelined Addition.

Numbers in the table are subscripts of operands/results.

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\hardwareOS\page_042\hardwareOS_page_042\auto\images\cb7ec324c6f6957646bc9ee9747ec50f0d01a60adde63fb024d84ba3300a2923.jpg

---

## Lecture: output\hardwareOS\page_043\hardwareOS_page_043\auto

# Pipelining (5)

• One floating point addition still takes 7 nanoseconds.

• But 1000 floating point additions now takes 1006 nanoseconds!

---

## Lecture: output\hardwareOS\page_044\hardwareOS_page_044\auto

# Multiple Issue (1)

• Multiple issue processors replicate functional units and try to simultaneously execute different instructions in a program.

![](images/5d3b68dd28c1790e0de63ae3a13f9e3f299d4b4eb1f0a45a770e63ca45d6a306.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\hardwareOS\page_044\hardwareOS_page_044\auto\images\5d3b68dd28c1790e0de63ae3a13f9e3f299d4b4eb1f0a45a770e63ca45d6a306.jpg

---

## Lecture: output\hardwareOS\page_045\hardwareOS_page_045\auto

# Multiple Issue (2)

• static multiple issue - functional units are scheduled at compile time.

dynamic multiple issue – functional units are scheduled at run-time.

superscalar

---

## Lecture: output\hardwareOS\page_046\hardwareOS_page_046\auto

# Speculation (1)

• In order to make use of multiple issue, the system must find instructions that can be executed simultaneously.

![](images/8ec994678ed8c9bbb1e75a041ccd517e8281e742d2c97fe574e48e1bc090da15.jpg)

In speculation, the compiler or the processor makes a guess about an instruction, and then executes the instruction on the basis of the guess.

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\hardwareOS\page_046\hardwareOS_page_046\auto\images\8ec994678ed8c9bbb1e75a041ccd517e8281e742d2c97fe574e48e1bc090da15.jpg

---

## Lecture: output\hardwareOS\page_047\hardwareOS_page_047\auto

# Speculation (2)

z = x + y ;   
i f ( z > 0) w = x ;   
e l s e w = y ;

![](images/eba647d378e524d25179645d77767e67b6c80594782017dff972b122a9ecba03.jpg)

If the system speculates incorrectly, it must go back and recalculate $\mathsf { w } = \mathsf { y } .$ .

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\hardwareOS\page_047\hardwareOS_page_047\auto\images\eba647d378e524d25179645d77767e67b6c80594782017dff972b122a9ecba03.jpg

---

## Lecture: output\hardwareOS\page_048\hardwareOS_page_048\auto

# Hardware multithreading (1)

• There aren’t always good opportunities for simultaneous execution of different threads.

Hardware multithreading provides a means for systems to continue doing useful work when the task being currently executed has stalled.

– Ex., the current task has to wait for data to be loaded from memory.

---

## Lecture: output\hardwareOS\page_049\hardwareOS_page_049\auto

# Hardware multithreading (2)

• Fine-grained - the processor switches between threads after each instruction, skipping threads that are stalled.

– Pros: potential to avoid wasted machine time due to stalls.

– Cons: a thread that’s ready to execute a long sequence of instructions may have to wait to execute every instruction.

---

## Lecture: output\hardwareOS\page_050\hardwareOS_page_050\auto

# Hardware multithreading (3)

• Coarse-grained - only switches threads that are stalled waiting for a time-consuming operation to complete.

– Pros: switching threads doesn’t need to be nearly instantaneous.

– Cons: the processor can be idled on shorter stalls, and thread switching will also cause delays.

---

## Lecture: output\hardwareOS\page_051\hardwareOS_page_051\auto

Hardware multithreading (3)

• Simultaneous multithreading (SMT) - a variation on fine-grained multithreading.

• Allows multiple threads to make use of the multiple functional units.

---

## Lecture: output\interconnectionNetworks\page_001\interconnectionNetworks_page_001\auto

# Interconnection Networks

---

## Lecture: output\interconnectionNetworks\page_002\interconnectionNetworks_page_002\auto

# Architecture of an Ideal Parallel Computer

• A natural extension of the Random Access Machine (RAM) serial architecture is the Parallel Random Access Machine, or PRAM.

• PRAMs consist of $p$ processors and a global memory of unbounded size that is uniformly accessible to all processors.

• Processors share a common clock but may execute different instructions in each cycle.

---

## Lecture: output\interconnectionNetworks\page_003\interconnectionNetworks_page_003\auto

# Architecture of an Ideal Parallel Computer

• Depending on how simultaneous memory accesses are handled, PRAMs can be divided into four subclasses.

• Exclusive-read, exclusive-write (EREW) PRAM.   
Concurrent-read, exclusive-write (CREW) PRAM.   
Exclusive-read, concurrent-write (ERCW) PRAM.   
• Concurrent-read, concurrent-write (CRCW) PRAM.

---

## Lecture: output\interconnectionNetworks\page_004\interconnectionNetworks_page_004\auto

# Architecture of an Ideal Parallel Computer

• What does concurrent write mean, anyway?

• Common: write only if all values are identical.   
• Arbitrary: write the data from a randomly selected processor.   
• Priority: follow a predetermined priority order.   
• Sum: Write the sum of all data items.

---

## Lecture: output\interconnectionNetworks\page_005\interconnectionNetworks_page_005\auto

# Physical Complexity of an Ideal Parallel Computer

• Processors and memories are connected via switches.   
• Since these switches must operate in O(1) time at the level of words,   
for a system of $p$ processors and m words, the switch complexity is O(mp).   
• Clearly, for meaningful values of p and m, a true PRAM is not realizable.

---

## Lecture: output\interconnectionNetworks\page_006\interconnectionNetworks_page_006\auto

# Interconnection Networks for Parallel Computers

• Interconnection networks carry data between processors and to memory.

• Interconnects are made of switches and links (wires, fiber).

• Interconnects are classified as static or dynamic.

• Static networks consist of point-to-point communication links among processing nodes and are also referred to as direct networks.

• Dynamic networks are built using switches and communication links.   
Dynamic networks are also referred to as indirect networks.

---

## Lecture: output\interconnectionNetworks\page_007\interconnectionNetworks_page_007\auto

# Static and Dynamic Interconnection Networks

![](images/8435879b8f33e8d7f4e68db29fbbcbefb886189eb16223dc2aa84d0d15aa48ce.jpg)

Classification of interconnection networks: (a) a static network; and (b) a dynamic network.

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\interconnectionNetworks\page_007\interconnectionNetworks_page_007\auto\images\8435879b8f33e8d7f4e68db29fbbcbefb886189eb16223dc2aa84d0d15aa48ce.jpg

---

## Lecture: output\interconnectionNetworks\page_008\interconnectionNetworks_page_008\auto

# Interconnection Networks

• Switches map a fixed number of input ports to output ports. • The total number of ports on a switch is the degree of the switch. • The cost of a switch grows as the square of the degree of the switch, the peripheral hardware linearly as the degree, and the packaging costs linearly as the number of pins.

---

## Lecture: output\interconnectionNetworks\page_009\interconnectionNetworks_page_009\auto

# Interconnection Networks: Network Interfaces

• Processors talk to the network via a network interface.

• The network interface may hang off the I/O bus or the memory bus.

• In a physical sense, this distinguishes a cluster from a tightly coupled multicomputer.

• The relative speeds of the I/O and memory buses impact the performance of the network.

---

## Lecture: output\interconnectionNetworks\page_010\interconnectionNetworks_page_010\auto

# Network Topologies

• A variety of network topologies have been proposed and implemented.

• These topologies tradeoff performance for cost.

• Commercial machines often implement hybrids of multiple topologies for reasons of packaging, cost, and available components.

---

## Lecture: output\interconnectionNetworks\page_011\interconnectionNetworks_page_011\auto

# Network Topologies: Buses

Some of the simplest and earliest parallel machines used buses.

• All processors access a common bus for exchanging data.

• The distance between any two nodes is O(1) in a bus. The bus also provides a convenient broadcast media.

• However, the bandwidth of the shared bus is a major bottleneck.

• Typical bus based machines are limited to dozens of nodes. Sun Enterprise servers and Intel Pentium based shared-bus multiprocessors are examples of such architectures.

---

## Lecture: output\interconnectionNetworks\page_012\interconnectionNetworks_page_012\auto

# Network Topologies: Buses

![](images/6e297a6eed1a6c6569de5c6d2897b5976ca2accf5edf894579957e0a565af53a.jpg)

Bus-based interconnects (a) with no local caches; (b) with local memory/caches.

Since much of the data accessed by processors is local to the processor, a local memory can improve the performance of bus-based machines.

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\interconnectionNetworks\page_012\interconnectionNetworks_page_012\auto\images\6e297a6eed1a6c6569de5c6d2897b5976ca2accf5edf894579957e0a565af53a.jpg

---

## Lecture: output\interconnectionNetworks\page_013\interconnectionNetworks_page_013\auto

# Network Topologies: Crossbars A crossbar network uses a p×m grid of switches to connect $p$ input ports to m output ports in a non-blocking manner.

![](images/8d974a56713ff6dd4a7460725745c14f7d599227565ab91476fd0a8fb2227d07.jpg)

A completely non-blocking crossbar network connecting $p$ processors to b memory banks.

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\interconnectionNetworks\page_013\interconnectionNetworks_page_013\auto\images\8d974a56713ff6dd4a7460725745c14f7d599227565ab91476fd0a8fb2227d07.jpg

---

## Lecture: output\interconnectionNetworks\page_014\interconnectionNetworks_page_014\auto

# Network Topologies: Crossbars

• The cost of a crossbar network of $p$ processors grows as $O ( p ^ { 2 } )$ . • This is generally difficult to scale for large values of $p$ . • Examples of machines that employ crossbars include the Sun Ultra HPC 10000 and the Fujitsu VPP500.

---

## Lecture: output\interconnectionNetworks\page_015\interconnectionNetworks_page_015\auto

# Network Topologies: Multistage Networks

• Crossbars have excellent performance scalability but poor cost scalability.

• Buses have excellent cost scalability, but poor performance scalability.

• Multistage interconnects strike a compromise between these extremes.

---

## Lecture: output\interconnectionNetworks\page_016\interconnectionNetworks_page_016\auto

# Network Topologies: Multistage Networks

![](images/daede00721512c9de73dc2f4cc6d17efd0eeae8445ce7f22074b2f32a86b4fae.jpg)

The schematic of a typical multistage interconnection network.

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\interconnectionNetworks\page_016\interconnectionNetworks_page_016\auto\images\daede00721512c9de73dc2f4cc6d17efd0eeae8445ce7f22074b2f32a86b4fae.jpg

---

## Lecture: output\interconnectionNetworks\page_017\interconnectionNetworks_page_017\auto

# Network Topologies: Multistage Omega Network

• One of the most commonly used multistage interconnect networks is the Omega network.

• This network consists of log p stages, where p is the number of input ports/output ports.

• At each stage, input i is connected to output j if:

$$
j = \left\{ \begin{array} { l l } { 2 i , } & { 0 \leq i \leq p / 2 - 1 } \\ { 2 i + 1 - p , } & { p / 2 \leq i \leq p - 1 } \end{array} \right.
$$

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\interconnectionNetworks\page_017\interconnectionNetworks_page_017\auto\images\9ede8772db684eb918b6a3af2e91f156aeb0a04873d41be215d1f7b12c6ee435.jpg

---

## Lecture: output\interconnectionNetworks\page_018\interconnectionNetworks_page_018\auto

# Network Topologies: Multistage Omega Network

Each stage of the Omega network implements a perfect shuffle as follows:

![](images/455520939e2271106e141575b2de2e8602e0ea10d2afd63544a92d8f2f01c7ce.jpg)

A perfect shuffle interconnection for eight input ports and output ports.

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\interconnectionNetworks\page_018\interconnectionNetworks_page_018\auto\images\455520939e2271106e141575b2de2e8602e0ea10d2afd63544a92d8f2f01c7ce.jpg

---

## Lecture: output\interconnectionNetworks\page_019\interconnectionNetworks_page_019\auto

# Network Topologies:

# Multistage Omega Network

• The perfect shuffle patterns are connected using 2×2 switches.   
• The switches operate in two modes – crossover or passthrough.

![](images/4dcb791970de91ce95e0e3042bf1f8505a18373ca79b165f34e52052260524f7.jpg)

Two switching configurations of the $2 \times 2$ switch: (a) Pass-through; (b) Cross-over.

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\interconnectionNetworks\page_019\interconnectionNetworks_page_019\auto\images\4dcb791970de91ce95e0e3042bf1f8505a18373ca79b165f34e52052260524f7.jpg

---

## Lecture: output\interconnectionNetworks\page_020\interconnectionNetworks_page_020\auto

# Network Topologies: Multistage Omega Network

A complete Omega network with the perfect shuffle interconnects and switches can now be illustrated:

![](images/77055fef25636d7296bd12f437c893a4d10bdf79d59c41b6839d2a4bd391c32a.jpg)

A complete omega network connecting eight inputs and eight outputs.

An omega network has $p / 2 \times 1 0 g p$ switching nodes, and the cost of such a network grows as (p log p).

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\interconnectionNetworks\page_020\interconnectionNetworks_page_020\auto\images\77055fef25636d7296bd12f437c893a4d10bdf79d59c41b6839d2a4bd391c32a.jpg

---

## Lecture: output\interconnectionNetworks\page_021\interconnectionNetworks_page_021\auto

# Network Topologies:

# Multistage Omega Network – Routing

• Let s be the binary representation of the source and d be that of the destination processor.

• The data traverses the link to the first switching node. If the most significant bits of s and d are the same, then the data is routed in pass-through mode by the switch else, it switches to crossover.

• This process is repeated for each of the log p switching stages.

• Note that this is not a non-blocking switch.

---

## Lecture: output\interconnectionNetworks\page_022\interconnectionNetworks_page_022\auto

# Network Topologies: Multistage Omega Network – Routing

![](images/0304e3c211aca4f86a7de3d6e31ebec2876869ec115e434c8004ff295e10f64b.jpg)

An example of blocking in omega network: one of the messages (010 to 111 or 110 to 100) is blocked at link AB.

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\interconnectionNetworks\page_022\interconnectionNetworks_page_022\auto\images\0304e3c211aca4f86a7de3d6e31ebec2876869ec115e434c8004ff295e10f64b.jpg

---

## Lecture: output\interconnectionNetworks\page_023\interconnectionNetworks_page_023\auto

# Network Topologies: Completely Connected Network

• Each processor is connected to every other processor.   
• The number of links in the network scales as $O ( p ^ { 2 } )$ .   
• While the performance scales very well, the hardware complexity is not realizable for large values of $p$ .   
• In this sense, these networks are static counterparts of crossbars.

---

## Lecture: output\interconnectionNetworks\page_024\interconnectionNetworks_page_024\auto

# Network Topologies: Star Connected Network

• Every node is connected only to a common node at the center.

• Distance between any pair of nodes is O(1). However, the central node becomes a bottleneck.

• In this sense, star connected networks are static counterparts of buses.

---

## Lecture: output\interconnectionNetworks\page_025\interconnectionNetworks_page_025\auto

# Network Topologies: Completely Connected and Star Connected Networks

![](images/06dac38422a044d771c1d9d3d37ef6fc2db242d5b12a13ba76ced35cd9daf1e5.jpg)

(a) A completely-connected network of eight nodes; (b) a star connected network of nine nodes.

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\interconnectionNetworks\page_025\interconnectionNetworks_page_025\auto\images\06dac38422a044d771c1d9d3d37ef6fc2db242d5b12a13ba76ced35cd9daf1e5.jpg

---

## Lecture: output\interconnectionNetworks\page_026\interconnectionNetworks_page_026\auto

Network Topologies:

Linear Arrays, Meshes, and k-d Meshes

• In a linear array, each node has two neighbors, one to its left and one to its right. If the nodes at either end are connected, we refer to it as a 1-D torus or a ring.

• A generalization to 2 dimensions has nodes with 4 neighbors, to the north, south, east, and west.

• A further generalization to $d$ dimensions has nodes with $2 d$ neighbors.

• A k-d mesh consists of d dimensions with k nodes on each dimension.

• A special case of a $d .$ -dimensional mesh is a hypercube. Here, $d = 1 0 g$ p, where $p$ is the total number of nodes.

---

## Lecture: output\interconnectionNetworks\page_027\interconnectionNetworks_page_027\auto

# Network Topologies: Linear Arrays

![](images/3df52fa9121bfe366b056383e744b38bf666797e6c5ca8a5214e5a74dc1ba7a8.jpg)

Linear arrays: (a) with no wraparound links; (b) with wraparound link.

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\interconnectionNetworks\page_027\interconnectionNetworks_page_027\auto\images\3df52fa9121bfe366b056383e744b38bf666797e6c5ca8a5214e5a74dc1ba7a8.jpg

---

## Lecture: output\interconnectionNetworks\page_028\interconnectionNetworks_page_028\auto

# Network Topologies: Two- and Three Dimensional Meshes

![](images/083585504ea91e5ba198d9c6ac4efc092607c9cd7145f6c054e2874bbd1c1272.jpg)

Two and three dimensional meshes: (a) 2-D mesh with no wraparound; (b) 2-D mesh with wraparound link (2-D torus); and (c) a 3-D mesh with no wraparound.

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\interconnectionNetworks\page_028\interconnectionNetworks_page_028\auto\images\083585504ea91e5ba198d9c6ac4efc092607c9cd7145f6c054e2874bbd1c1272.jpg

---

## Lecture: output\interconnectionNetworks\page_029\interconnectionNetworks_page_029\auto

# Network Topologies: Hypercubes and their Construction

![](images/eed3e31d6eb788a257db4b1ede39aa9c754cb8b8ad90e5edf4079eef9fda0d15.jpg)

Construction of hypercubes from hypercubes of lower dimension.

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\interconnectionNetworks\page_029\interconnectionNetworks_page_029\auto\images\eed3e31d6eb788a257db4b1ede39aa9c754cb8b8ad90e5edf4079eef9fda0d15.jpg

---

## Lecture: output\interconnectionNetworks\page_030\interconnectionNetworks_page_030\auto

# Network Topologies: Properties of Hypercubes

• The distance between any two nodes is at most log p.   
• Each node has log p neighbors.   
• The distance between two nodes is given by the number of bit positions at which the two nodes differ.

---

## Lecture: output\interconnectionNetworks\page_031\interconnectionNetworks_page_031\auto

# Network Topologies: Tree-Based Networks

![](images/befb834002baf3b118630d560ad2fec54419fe347cec94a0d25a6fdcb6de6983.jpg)

Complete binary tree networks: (a) a static tree network; and (b) a dynamic tree network.

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\interconnectionNetworks\page_031\interconnectionNetworks_page_031\auto\images\befb834002baf3b118630d560ad2fec54419fe347cec94a0d25a6fdcb6de6983.jpg

---

## Lecture: output\interconnectionNetworks\page_032\interconnectionNetworks_page_032\auto

# Network Topologies: Tree Properties

• The distance between any two nodes is no more than 2logp.   
• Links higher up the tree potentially carry more traffic than those at the lower levels.   
• For this reason, a variant called a fat-tree, fattens the links as we go up the tree.   
• Trees can be laid out in 2D with no wire crossings. This is an attractive property of trees.

---

## Lecture: output\interconnectionNetworks\page_033\interconnectionNetworks_page_033\auto

# Network Topologies: Fat Trees

![](images/c50374ac804ad74b2ac312e8b434a5d7ad2ad7844ebe32cb5395c54f1a68e4b2.jpg)

A fat tree network of 16 processing nodes.

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\interconnectionNetworks\page_033\interconnectionNetworks_page_033\auto\images\c50374ac804ad74b2ac312e8b434a5d7ad2ad7844ebe32cb5395c54f1a68e4b2.jpg

---

## Lecture: output\interconnectionNetworks\page_034\interconnectionNetworks_page_034\auto

# Evaluating Static Interconnection Networks

• Diameter: The distance between the farthest two nodes in the network. The diameter of a linear array is $p - 1 .$ , that of a mesh is $2 ( { \sqrt { p } }$ − 1), that of a tree and hypercube is log $p$ , and that of a completely connected network is O(1).

• Arc Connectivity: The minimum number of links to remove to make the network into two disconnected networks.

Bisection Width: The minimum number of wires you must cut to divide the network into two equal parts. The bisection width of a linear array and tree is 1, that of a mesh $\mathsf { i s } \sqrt { p }$ , that of a hypercube is $p / 2$ and that of a completely connected network is $p ^ { 2 } / 4$ .

• Cost: The number of links or switches (whichever is asymptotically higher) is a meaningful measure of the cost. However, a number of other factors, such as the ability to layout the network, the length of wires, etc., also factor in to the cost.

---

## Lecture: output\interconnectionNetworks\page_035\interconnectionNetworks_page_035\auto

# Evaluating Static Interconnection Networks

<table><tr><td>Network</td><td>Diameter</td><td>Bisection Width</td><td>Arc Connectivity</td><td>Cost (No. of links)</td></tr><tr><td>Completely-connected</td><td>1</td><td>$p{2/4$</td><td>p-1</td><td>p(p − 1)/2</td></tr><tr><td>Star</td><td>2</td><td>1</td><td>1</td><td>p-1</td></tr><tr><td>Complete binary tree</td><td>21og((p + 1)/2)</td><td>1</td><td>1</td><td>p-1</td></tr><tr><td>Linear array</td><td>p-1</td><td>1</td><td>1</td><td>p-1</td></tr><tr><td>2-D mesh, no wraparound</td><td>2(√p − 1)</td><td>$√p}$</td><td>2</td><td>2(p − √p)</td></tr><tr><td>2-D wraparound mesh</td><td>2√p/2</td><td>2√p$</td><td>4</td><td>2p</td></tr><tr><td>Hypercube</td><td>logp</td><td>p/2</td><td>logp</td><td>(p log p)/2</td></tr><tr><td>Wraparound k-ary d-cube</td><td>d|k/2</td><td>2kd-1</td><td>2d</td><td>dp</td></tr></table>

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\interconnectionNetworks\page_035\interconnectionNetworks_page_035\auto\images\78ec64961a377c2dfc3c534a89406427e3bdfe1ac7c568c5351bb0677a447694.jpg

---

## Lecture: output\interconnectionNetworks\page_036\interconnectionNetworks_page_036\auto

# Evaluating Dynamic Interconnection Networks

<table><tr><td>Network</td><td>Diameter</td><td>Bisection Width</td><td>Arc Connectivity</td><td>Cost (No. of links)</td></tr><tr><td>Crossbar</td><td>1</td><td>P</td><td>1</td><td>D2</td></tr><tr><td>Omega Network</td><td>logp</td><td>P/2</td><td>2</td><td>p/2 × log p</td></tr><tr><td>Dynamic Tree</td><td>2logp</td><td>1</td><td>2</td><td>p-1</td></tr></table>

The nodes in dynamic networks contains both the processor nodes and the switching nodes.

The diameter is the maximum distance between any (processing or switching) pair of nodes.

The bisection width is the minimum number of edges that cross the two equal partitions of the processing nodes.

The arc connectivity is the minimum number of edges that must fail to fragment the network into two unreachable parts.

The cost of a dynamic network (number of links) is asymptotically the number of switches.

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\interconnectionNetworks\page_036\interconnectionNetworks_page_036\auto\images\db5d28d9d0b41f093e55b484a1dadb31eb100c159d2ad0db3e1644c5ba4128cb.jpg

---

## Lecture: output\lecture0\page_001\lecture0_page_001\auto

# Introduction to High-Performance and Parallel Computing

Course Introduction

---

## Lecture: output\lecture0\page_002\lecture0_page_002\auto

# Course Background

• A DSAA ELECTIVE – Assume C/C++ programming, Algorithms – Structured lectures based on reference books – Teach parallel programming knowledge – Practice parallel programming in two APIs – Workload • Three programming assignments + final exam

---

## Lecture: output\lecture0\page_003\lecture0_page_003\auto

# Course Topics

• Introduction to parallel computer architectures   
• Principles of parallel algorithm design   
• Shared-memory programming models   
• Message passing programming models   
Case studies of parallel algorithms, systems, and applications Hands-on experience with writing parallel programs for tasks of interest

---

## Lecture: output\lecture0\page_004\lecture0_page_004\auto

# Parallel Computer Architectures

Review on OS and Computer Architecture – The von Neumann architecture – Processes, multitasking, and threads – Modifications to the von Neumann Model

• Caches   
• Virtual memory   
• Instruction-level parallelism Hardware multithreading

Parallel Hardware

– SIMD systems   
– MIMD systems   
– Interconnection networks Cache coherence   
– Shared-memory versus distributed-memory

---

## Lecture: output\lecture0\page_005\lecture0_page_005\auto

# Principles of parallel algorithm design

Preliminaries

– Decomposition, Tasks, and Dependency Graphs – Granularity, Concurrency, and Task-Interaction – Processes and Mapping

• Decomposition Techniques

• Mapping Techniques for Load Balancing

• Methods for Containing Interaction Overheads • Parallel Algorithm Models

---

## Lecture: output\lecture0\page_006\lecture0_page_006\auto

# Shared-memory programming models

• OpenMP – Parallel directives – Variable scopes – Critical sections – Other synchronization mechanisms – Schedule types

---

## Lecture: output\lecture0\page_007\lecture0_page_007\auto

Message passing programming models

• Principles of Message-Passing Programming   
Building Blocks: Send and Receive Operations   
• MPI: the Message Passing Interface   
Collective Communication and Computation Operations – Gather, Scatter, Prefix, Reduction, Broadcast, Barrier, and so on

---

## Lecture: output\lecture0\page_008\lecture0_page_008\auto

# Reference Book 1

Introduction to

# Parallel Computing

Second Edition

Introduction to Parallel Computing 2nd edition

By Ananth Grama, Anshul Gupta, George Karypis, Vipin Kumar.

Addison Wesley, 2003.

https://www.cs.purdue.edu/h omes/ayg/book/index.html

GI PTA KARYPIS KUN MAR

---

## Lecture: output\lecture0\page_009\lecture0_page_009\auto

# Reference Book 2

![](images/1b1d53a739e68c97b1e28f00c78b754b46719769ea7789d4df075f5adb0fd9ec.jpg)

An Introduction to Parallel Programming. 2nd edition

By Peter Pacheco and

Matthew Malensek, 2022

Second Edition

# AN INTRODUCTION TO PARALLEL PROGRAMMING

https://www.cs.usfca.edu/ \~peter/ipp2/index.html

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\lecture0\page_009\lecture0_page_009\auto\images\1b1d53a739e68c97b1e28f00c78b754b46719769ea7789d4df075f5adb0fd9ec.jpg

---

## Lecture: output\lecture0\page_010\lecture0_page_010\auto

# Lecture Time and Venue

• 13 weeks of lectures on Mon/Wed at 12- 1:20pm – Sept 1-Dec 5 (No class on Oct 1-8 public holiday) – E1-148

• 13 weeks of labs on Friday at 10:30AM - 11:20AM, E1-227

---

## Lecture: output\lecture0\page_011\lecture0_page_011\auto

# Workload & Assessment

• Tentative plan – Three programming assignments 50%

• Week 4, 7, 10 on OpenMP and MPI

• All assignments on related topics (e.g., shortest path)

• Sequential version program given (a few hundred lines of code)

• Parallel program skeleton given

• Your task is to fill in a few parallel components (tens of lines of code)

– One final exam 50%

• Programming: fill in code, similar to assignments • Short answer questions on concepts from course material

---

## Lecture: output\lecture0\page_012\lecture0_page_012\auto

# Lab Facilities

• TA will guide you to set up access to – Cloud computers in the lab – Accounts on the HPC clusters

---

## Lecture: output\lecture0\page_013\lecture0_page_013\auto

# Academic Integrity

• You can discuss with others on ideas and bugs.

• Do not look up (e.g., using AI) solution code.

• Do not share or post your code.

• All code that you submit (other than skeleton code) should be written by you alone.

• Code plagiarism detection will be performed.

• Misconduct will be reported and penalized.

---

## Lecture: output\matrix_multiplicationCUDA\page_001\matrix_multiplicationCUDA_page_001\auto

# Parallel Programming

CUDA Example: Matrix Multiplication

---

## Lecture: output\matrix_multiplicationCUDA\page_002\matrix_multiplicationCUDA_page_002\auto

# Overview

• Matrix multiplication as an example in CUDA – Math operation review – Baseline implementation – Tiling for shared memory/blocking

---

## Lecture: output\matrix_multiplicationCUDA\page_003\matrix_multiplicationCUDA_page_003\auto

# Math Review: Matrix Multiplication

C[Row,Col] = A’s row at Row∙ B’s column at Col = A[Row,0] \* B[0, Col] + A[Row,1]\*B[1,Col] + …

+A[Row,n-1] \*B[n-1,Col]

![](images/494d66b73c87bc05449a29b733e2ac89831cbebc85c14ad7d558355079911794.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\matrix_multiplicationCUDA\page_003\matrix_multiplicationCUDA_page_003\auto\images\494d66b73c87bc05449a29b733e2ac89831cbebc85c14ad7d558355079911794.jpg

---

## Lecture: output\matrix_multiplicationCUDA\page_004\matrix_multiplicationCUDA_page_004\auto

# Sequential C code

void MatrixMulOnHost(int m, int n, int k, float\* A, float\* B, float\*   
for (int Row = 0; Row < m; ++Row) for (int Col = 0; Col < k; ++Col) { float sum = 0; B f $\mathsf { o r } ( \mathsf { i n t } \mathsf { i } = 0 ; \mathsf { i } < \mathsf { n } ; + + \mathsf { i } ) \{$ Col float $\mathsf { a } = \mathsf { A } [ \mathsf { R o w } ^ { \star } \mathsf { n } + \mathsf { i } ] ;$ n float ${ \sf b } = { \sf B } [ { \sf C o } | + \mathrm { i } ^ { \star } { \sf k } ] ;$ k sum $+ = a ^ { \star } b ;$ ; } C[Row\*k + Col] = sum; Row m m   
} k

---

## Lecture: output\matrix_multiplicationCUDA\page_005\matrix_multiplicationCUDA_page_005\auto

# Baseline Kernel

_ global__ void MatrixMulKernel(int m,int n,int k,float\* A,float\* B, float\* C) {

int Row $=$ blockIdx.y\*blockDim.y+threadIdx.y;   
int Col $=$ blockIdx.x\*blockDim.x+threadIdx.x;   
if $( \mathsf { R o w } < \mathsf { m } )$ && (Col < k)) {   
float $\mathsf { C v a l u e } = 0 . 0$ ;   
for $( \mathsf { i n t } \mathsf { i } = 0 ; \mathsf { i } < \mathsf { n } ; + + \mathsf { i } )$ /\* A[Row, i] and B[i, Col] \*/ Cvalue $+ = A [ R o w ^ { \star } \mathsf { n } + \mathsf { i } ] \ ^ { \star } \mathsf { B } [ \mathsf { C o l } + \mathsf { i } ^ { \star } \mathsf { k } ] ;$

$\mathsf { C } [ \mathsf { R o w } ^ { \star } \mathsf { k } + \mathsf { C o l } ] = \mathsf { C v a l u e } ;$ } }

![](images/09549ed20e38a9097feb4406b705990d0a74e427ef122a44749dadf3ff3a8add.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\matrix_multiplicationCUDA\page_005\matrix_multiplicationCUDA_page_005\auto\images\09549ed20e38a9097feb4406b705990d0a74e427ef122a44749dadf3ff3a8add.jpg

---

## Lecture: output\matrix_multiplicationCUDA\page_006\matrix_multiplicationCUDA_page_006\auto

# Memory Access Pattern

Global Memory

![](images/1372db639a49b6f088fdf7ddd9bb30e632e1f8fb96f7b1d399d556c606444770.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\matrix_multiplicationCUDA\page_006\matrix_multiplicationCUDA_page_006\auto\images\1372db639a49b6f088fdf7ddd9bb30e632e1f8fb96f7b1d399d556c606444770.jpg

---

## Lecture: output\matrix_multiplicationCUDA\page_007\matrix_multiplicationCUDA_page_007\auto

# Shared Memory Tiling/Blocking

Global Memory

![](images/820d5fcaa82fa78dfb84d942e04c152e509e3ace69a74f4b5270585279a2fcf5.jpg)

Divide the global memory content into tiles

Focus the computation of small number of tiles in multiple threads at each point in time

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\matrix_multiplicationCUDA\page_007\matrix_multiplicationCUDA_page_007\auto\images\820d5fcaa82fa78dfb84d942e04c152e509e3ace69a74f4b5270585279a2fcf5.jpg

---

## Lecture: output\matrix_multiplicationCUDA\page_008\matrix_multiplicationCUDA_page_008\auto

# Timing with Tiling

Good: when threads have similar access timing

![](images/30638f2e6b20bc01452d3dc0227523745fd442c64218c2071c5237672e87c2cb.jpg)

Bad: when threads have very different timing

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\matrix_multiplicationCUDA\page_008\matrix_multiplicationCUDA_page_008\auto\images\30638f2e6b20bc01452d3dc0227523745fd442c64218c2071c5237672e87c2cb.jpg

---

## Lecture: output\matrix_multiplicationCUDA\page_009\matrix_multiplicationCUDA_page_009\auto

# Barrier Synchronization for Tiling

![](images/f587f5386e5525cc49971c842189a0646cc75ab5424580b1095bba92614e6102.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\matrix_multiplicationCUDA\page_009\matrix_multiplicationCUDA_page_009\auto\images\f587f5386e5525cc49971c842189a0646cc75ab5424580b1095bba92614e6102.jpg

---

## Lecture: output\matrix_multiplicationCUDA\page_010\matrix_multiplicationCUDA_page_010\auto

# Barrier Synchronization

• Synchronize all threads in a thread block: __syncthreads()

All threads in the same block must reach the __syncthreads() before any of them can move on

• Best used to coordinate tiled algorithms

– To ensure that all elements of a tile are loaded at the beginning of a phase

– To ensure that all elements of a tile are consumed at the end of a phase

---

## Lecture: output\matrix_multiplicationCUDA\page_011\matrix_multiplicationCUDA_page_011\auto

# Outline of Tiling

• Identify a tile of global memory contents that are accessed by multiple threads

• Load the tile from global memory into on-chip memory

• Use barrier synchronization to make sure that all threads are ready to start the phase

• Have the multiple threads to access their data from the on-chip memory

Use barrier synchronization to make sure that all threads have completed the current phase

Move on to the next tile

---

## Lecture: output\matrix_multiplicationCUDA\page_012\matrix_multiplicationCUDA_page_012\auto

# Matrix Multiplication Tiled

Break up the execution of each thread into phases so that the data accessed by a thread block is contained in a block of A and a block of B.

![](images/d318463d2c87ef0d755317f79458c9ac7aac399a32b9f72f3ff65124faeea9f8.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\matrix_multiplicationCUDA\page_012\matrix_multiplicationCUDA_page_012\auto\images\d318463d2c87ef0d755317f79458c9ac7aac399a32b9f72f3ff65124faeea9f8.jpg

---

## Lecture: output\matrix_multiplicationCUDA\page_013\matrix_multiplicationCUDA_page_013\auto

# Loading a Tile

• All threads in a block participate – Each thread loads one A element and one B element in the tiled code

• Assign the loaded element to each thread such that the accesses within each warp are coalesced

---

## Lecture: output\matrix_multiplicationCUDA\page_014\matrix_multiplicationCUDA_page_014\auto

# Phase 0: Load for Block (0,0) of C

![](images/3f9561c0e0512d6502c0e477bf64ffed83c89c274c7acddb91df94c06aac196e.jpg)

![](images/9850aa7d16a37797b4d8fda5331d2c7669d297d16ae0d7a52029296748f96d62.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\matrix_multiplicationCUDA\page_014\matrix_multiplicationCUDA_page_014\auto\images\3f9561c0e0512d6502c0e477bf64ffed83c89c274c7acddb91df94c06aac196e.jpg
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\matrix_multiplicationCUDA\page_014\matrix_multiplicationCUDA_page_014\auto\images\9850aa7d16a37797b4d8fda5331d2c7669d297d16ae0d7a52029296748f96d62.jpg

---

## Lecture: output\matrix_multiplicationCUDA\page_015\matrix_multiplicationCUDA_page_015\auto

# Phase 0: Compute Block (0,0) Iteration 0

![](images/27fffa2b02aa8556cf3be0cae7bf598ae348478105ea378cbde5859271a43239.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\matrix_multiplicationCUDA\page_015\matrix_multiplicationCUDA_page_015\auto\images\27fffa2b02aa8556cf3be0cae7bf598ae348478105ea378cbde5859271a43239.jpg

---

## Lecture: output\matrix_multiplicationCUDA\page_016\matrix_multiplicationCUDA_page_016\auto

# Phase 0: Compute Block (0,0) Iteration 1

![](images/b1db045cefdba25236f37ea5082d403f0cc66b9b42184cc061fc7d683ffa0a00.jpg)

![](images/894b0d21ce8c88f2cabf57087b2e05f420f9ea441629f168c9e351cc1a7bdcf6.jpg)

![](images/feb3a996b4237b177f8398e40f31ed23a5bf22dbcf04a6de2d680fdbc7f99980.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\matrix_multiplicationCUDA\page_016\matrix_multiplicationCUDA_page_016\auto\images\894b0d21ce8c88f2cabf57087b2e05f420f9ea441629f168c9e351cc1a7bdcf6.jpg
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\matrix_multiplicationCUDA\page_016\matrix_multiplicationCUDA_page_016\auto\images\b1db045cefdba25236f37ea5082d403f0cc66b9b42184cc061fc7d683ffa0a00.jpg
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\matrix_multiplicationCUDA\page_016\matrix_multiplicationCUDA_page_016\auto\images\feb3a996b4237b177f8398e40f31ed23a5bf22dbcf04a6de2d680fdbc7f99980.jpg

---

## Lecture: output\matrix_multiplicationCUDA\page_017\matrix_multiplicationCUDA_page_017\auto

# Phase 1: Load for Block (0,0) of C

![](images/a8dd1c747e97bc9f73579e08e4ae5f3137f886f0f37ac2b852fbe5f601c41d4f.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\matrix_multiplicationCUDA\page_017\matrix_multiplicationCUDA_page_017\auto\images\a8dd1c747e97bc9f73579e08e4ae5f3137f886f0f37ac2b852fbe5f601c41d4f.jpg

---

## Lecture: output\matrix_multiplicationCUDA\page_018\matrix_multiplicationCUDA_page_018\auto

# Phase 1: Compute Block (0,0) Iteration 0

![](images/9f94443b99b9d0a03bd54384e008472877f968dceaa7b6f1171b32340cd395b2.jpg)

![](images/3b4520c8086823e7407fd09180ff572cc3447383e3d15083e2e3ee28fe847087.jpg)

![](images/de41db28881e1f1431ea56cc5b6a9d7630fdb219e5d3ef793a84302bfa1c5916.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\matrix_multiplicationCUDA\page_018\matrix_multiplicationCUDA_page_018\auto\images\3b4520c8086823e7407fd09180ff572cc3447383e3d15083e2e3ee28fe847087.jpg
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\matrix_multiplicationCUDA\page_018\matrix_multiplicationCUDA_page_018\auto\images\9f94443b99b9d0a03bd54384e008472877f968dceaa7b6f1171b32340cd395b2.jpg
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\matrix_multiplicationCUDA\page_018\matrix_multiplicationCUDA_page_018\auto\images\de41db28881e1f1431ea56cc5b6a9d7630fdb219e5d3ef793a84302bfa1c5916.jpg

---

## Lecture: output\matrix_multiplicationCUDA\page_019\matrix_multiplicationCUDA_page_019\auto

# Phase 1: Compute Block (0,0) Iteration 1

![](images/7970d81a9903cfc1ccbcd779dde1e2ae9bf3872da3742be4fd73f76c8d1b873f.jpg)

![](images/697b3ba22df5c84b009f554dbced39fc7360638554dd925e5b09509382d2332c.jpg)

![](images/fcf0ad964a462832859e6a0dca5adde7583d9a1a0c66e7c0f3822c7f28bd88da.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\matrix_multiplicationCUDA\page_019\matrix_multiplicationCUDA_page_019\auto\images\697b3ba22df5c84b009f554dbced39fc7360638554dd925e5b09509382d2332c.jpg
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\matrix_multiplicationCUDA\page_019\matrix_multiplicationCUDA_page_019\auto\images\7970d81a9903cfc1ccbcd779dde1e2ae9bf3872da3742be4fd73f76c8d1b873f.jpg
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\matrix_multiplicationCUDA\page_019\matrix_multiplicationCUDA_page_019\auto\images\fcf0ad964a462832859e6a0dca5adde7583d9a1a0c66e7c0f3822c7f28bd88da.jpg

---

## Lecture: output\matrix_multiplicationCUDA\page_020\matrix_multiplicationCUDA_page_020\auto

# Loading a Tile: 2D Element Index

Have each thread to load an A element and a B element at the same relative position as its C element.

![](images/a128e003052103c91d9388c3cf55aa6c6407a6bd131bdc981e593130fa293f9d.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\matrix_multiplicationCUDA\page_020\matrix_multiplicationCUDA_page_020\auto\images\a128e003052103c91d9388c3cf55aa6c6407a6bd131bdc981e593130fa293f9d.jpg

---

## Lecture: output\matrix_multiplicationCUDA\page_021\matrix_multiplicationCUDA_page_021\auto

# Loading a Tile: 2D Element Index (cont.)

![](images/5e1713790cd2faf6f168809bd8350e991ae1f226507f026d41c89ac97e60357b.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\matrix_multiplicationCUDA\page_021\matrix_multiplicationCUDA_page_021\auto\images\5e1713790cd2faf6f168809bd8350e991ae1f226507f026d41c89ac97e60357b.jpg

---

## Lecture: output\matrix_multiplicationCUDA\page_022\matrix_multiplicationCUDA_page_022\auto

# Loading a Tile: Element in 1D Index

A[Row][t\*TILE_WIDTH+tx]

A[Row\*n $^ +$ t\*TILE_WIDTH + tx]

B[t\*TILE_WIDTH+ty][Col]B[(t\*TILE_WIDTH+ty)\*k + Col]

where t is the tile sequence number of the current phase

![](images/4905ffac0718ec4a7a495195a1f4dd2784979cb7c35049be273533fbd800756c.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\matrix_multiplicationCUDA\page_022\matrix_multiplicationCUDA_page_022\auto\images\4905ffac0718ec4a7a495195a1f4dd2784979cb7c35049be273533fbd800756c.jpg

---

## Lecture: output\matrix_multiplicationCUDA\page_023\matrix_multiplicationCUDA_page_023\auto

# Tiled Matrix Multiplication Kernel

_global__ void MatrixMulKernel(int m, int n, int k, float\* A, float\* B, float\* C) {

1. __shared__ float ds_A[TILE_WIDTH][TILE_WIDTH];   
2. _shared float ds_B[TILE_WIDTH][TILE_WIDTH];   
3. int bx $=$ blockIdx.x; int by = blockIdx.y;   
4. int tx $=$ threadIdx.x; int $\begin{array} { r l } { \mathrm { \Delta t { } } _ { \Sigma } } & { { } = } \end{array}$ threadIdx.y;   
5. int $\mathtt { R o w } \ = \ \mathtt { b y }$ \* blockDim.y + ty;   
6. int $\mathsf { C o l } \ = \ \mathsf { b x }$ \* blockDim.x + tx;

7. float Cvalue $= 0$ ;

---

## Lecture: output\matrix_multiplicationCUDA\page_024\matrix_multiplicationCUDA_page_024\auto

# Tiled Matrix Multiplication Kernel (cont.)

//Loop over the A and B tiles as required to compute the C

8. for (int $\begin{array} { r l r } { \mathrm { t } = 0 ; \mathrm { t } } & { { } } & { < \mathsf { n } / \mathsf { T } | \mathsf { L } \mathsf { E } \_ { \mathsf { W } } | \mathsf { D } \mathsf { T } \mathsf { H } ; + + \mathrm { t } \left\{ \begin{array} { r l r } { \left\{ \begin{array} { r l r } \end{array} \right. } \end{array} \right. } \end{array}$

// Collaborative loading of A and B tiles into shared memory

$$
\mathsf { d } \mathsf { s \_ B } [ \mathsf { t y } ] [ \mathsf { t x } ] = \mathsf { B } [ ( \mathsf { t ^ { * } T } \mathsf { I L E \_ W } \mathsf { I D T } \mathsf { H } + \mathsf { t y } ) ^ { * } \mathsf { k } + \mathsf { C o l } ] ;
$$

11. syncthreads();

12. for (int $\dot { \mathsf { I } } = 0$ ; i < TILE_WIDTH; ++i) //compute the corresponding result   
13. Cvalue $+ =$ ds_A[ty][i] \* ds_B[i][tx];   
14. synchthreads();

15. }

16. $\mathsf { C } \left[ \mathsf { R o w } ^ { * } \mathsf { k } { + } \mathsf { C o l } \right] = \mathsf { C v a l u e } ;$ }

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\matrix_multiplicationCUDA\page_024\matrix_multiplicationCUDA_page_024\auto\images\5c48bf4db0b37610a37d1a12e9e1f5bc05bea71b10357961b1802505671d7c70.jpg
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\matrix_multiplicationCUDA\page_024\matrix_multiplicationCUDA_page_024\auto\images\f41e8140476587156d246093378fd09c0dd07153388d33491429b94e4dfc7806.jpg

---

## Lecture: output\matrix_multiplicationCUDA\page_025\matrix_multiplicationCUDA_page_025\auto

# Block Size Consideration

Each thread block should have many threads

TILE_WIDTH of 16 gives $1 6 ^ { * } 1 6 = ~ 2 5 6$ threads TILE_WIDTH of 32 gives $3 2 ^ { * } 3 2 = 1 0 2 4$ threads

For 16, each block performs $2 ^ { * } 2 5 6 = 5 1 2$ float loads from global memory for 256 \* (2\*16) = 8,192 mul/add operations. (memory traffic reduced by a factor of 16)

For 32, each block performs $2 ^ { * } 1 0 2 4 = 2 0 4 8$ float loads from global memory for 1024 \* (2\*32) = 65,536 mul/add operations. (memory traffic reduced by a factor of 32)

However, the thread count limitation of threads per SM in current generation GPUs will reduce the number of blocks per SM (e.g., with a limit of 1536 threads per SM, we have 1536/256 = 6 16\*16blocks, 1536/1024 = 1 block).

---

## Lecture: output\matrix_multiplicationCUDA\page_026\matrix_multiplicationCUDA_page_026\auto

# Shared Memory Size Consideration

For an SM with 16KB shared memory – For TILE_WIDTH = 16, each thread block uses 2\*256\*4B = 2KB of shared memory. We can have up to 8 thread blocks. This allows up to 8\*512 = 4,096 pending loads. (2 per thread, 256 threads per block) The next TILE_WIDTH 32 would lead to 2\*32\*32\*4 Byte= 8K Byte shared memory usage per thread block, allowing 2 thread blocks active at the same time.

• Each __syncthread() can reduce the number of active threads for a block – More thread blocks can be advantageous

---

## Lecture: output\matrix_multiplicationCUDA\page_027\matrix_multiplicationCUDA_page_027\auto

# What If Tiles Exceed Matrix Boundaries

When a thread is to load any input element,   
test if it is in the valid index range   
– If valid, proceed to load   
– Else, do not load, just write a 0

Rationale: a 0 value will ensure that the multiply-add step does not affect the final value of the output element

---

## Lecture: output\matrix_multiplicationCUDA\page_028\matrix_multiplicationCUDA_page_028\auto

# Compute Elements Exceeding Boundaries

• If a thread does not calculate a valid output element, it can still perform multiply-add into its register as long as it is not allowed to write to the global memory at the end of the kernel • This way, the thread does not need to be turned off by an if-statement as in the baseline kernel; it can participate in the tile loading process

---

## Lecture: output\matrix_multiplicationCUDA\page_029\matrix_multiplicationCUDA_page_029\auto

# Illustration

![](images/c12b689b5980b0fb00329758e855f39da9e4b0aa10767eecc9a375feea5bc69d.jpg)

The multiply-add will not affect the output due to 0’s.

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\matrix_multiplicationCUDA\page_029\matrix_multiplicationCUDA_page_029\auto\images\c12b689b5980b0fb00329758e855f39da9e4b0aa10767eecc9a375feea5bc69d.jpg

---

## Lecture: output\matrix_multiplicationCUDA\page_030\matrix_multiplicationCUDA_page_030\auto

# Testing Boundary Condition on A

Each thread loads

A[Row][t\*TILE_WIDTH+tx]A[Row\*n $^ +$ t\*TILE_WIDTH+tx]

Need to test • (Row $< \mathsf { m }$ ) && (t\*TILE_WIDTH+tx < n) If true, load A element Else , load 0

![](images/72fcce62da5d5a9bea0bef25132eaaa0c50b887474e120c1e9ff4d7bc03fc009.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\matrix_multiplicationCUDA\page_030\matrix_multiplicationCUDA_page_030\auto\images\72fcce62da5d5a9bea0bef25132eaaa0c50b887474e120c1e9ff4d7bc03fc009.jpg

---

## Lecture: output\matrix_multiplicationCUDA\page_031\matrix_multiplicationCUDA_page_031\auto

# Testing Boundary Condition on B

Each thread loads

B[t\*TILE_WIDTH+ty][Col]B[(t\*TILE_WIDTH+ty)\*k+ Col]

Need to test

(t\*TILE_WIDTH+ty < n) && (Col< k)   
If true, load B element   
Else , load 0

![](images/f3e6284ebd9e621f15d070ff7353f3727d51f5f3dd5d4453f39daba90ab86064.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\matrix_multiplicationCUDA\page_031\matrix_multiplicationCUDA_page_031\auto\images\f3e6284ebd9e621f15d070ff7353f3727d51f5f3dd5d4453f39daba90ab86064.jpg

---

## Lecture: output\matrix_multiplicationCUDA\page_032\matrix_multiplicationCUDA_page_032\auto

# Code: Loading A and B Tiles with Boundary Checks

for (int $\mathbf { t } = 0$ ; t < (n-1)/TILE_WIDTH + 1; ++t) {

$\mathsf { i f } \big ( \mathsf { R o w } < \mathsf { m \& } \mathsf { \& } \mathsf { T I L E \_ W I D T H + t x } < \mathsf { n } \big ) \left\{ \begin{array} { r l } \end{array} \right.$ $\mathsf { d } \mathsf { s \_ A } [ \mathsf { t y } ] [ \mathsf { t x } ] = \mathsf { A } [ \mathsf { R o w } ^ { \ast } \mathsf { n } + \mathsf { t } ^ { \ast } \mathsf { T } | \mathsf { L E \_ W } | \mathsf { D } \mathsf { T } \mathsf { H } + \mathsf { t x } ] ;$ } else { ds_A[ty][tx] = 0.0; } if $(  \sf t ^ { * } T I L E \_ W I D T H + t y < n \& \& C o l < k ) \left\{ \right.$ ds_B[ty][tx] $=$ B[(t\*TILE_WIDTH + ty)\*k+col]; } else { ds_B[ty][tx] = 0.0; } syncthreads();

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\matrix_multiplicationCUDA\page_032\matrix_multiplicationCUDA_page_032\auto\images\80390b27b0b370e6137041cfda268173536a6e2e2dc8f6a3fd7432368280e122.jpg
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\matrix_multiplicationCUDA\page_032\matrix_multiplicationCUDA_page_032\auto\images\966d187eafc62db38ed944a6a488544231684d55ab50018409c63e77b289049c.jpg
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\matrix_multiplicationCUDA\page_032\matrix_multiplicationCUDA_page_032\auto\images\bcb090b869585083d2efc8a30fecb40c6c2a8b7b76111e7574d3598c4675ef47.jpg

---

## Lecture: output\matrix_multiplicationCUDA\page_033\matrix_multiplicationCUDA_page_033\auto

# Code: Calculate C Values and Store

12 for (int $\dot { \mathsf { I } } = 0$ ; i $<$ TILE_WIDTH; ++i) {   
13 Cvalue $+ =$ ds_A[ty][i] \* ds_B[i][tx]; }   
14 syncthreads();   
15 $\} / { } ^ { * }$ end of outer for loop $^ * /$   
++ if $( \mathsf { R o w } < \mathsf { m } \ \& \ \mathsf { k } \ \mathsf { C o l } < \mathsf { k } )$   
16 $\mathsf { P } \big [ \mathsf { R o w } ^ { * } \mathsf { k } + \mathsf { C o l } \big ] = \mathsf { C v a l u e } ;$ } /\* end of kernel \*/

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\matrix_multiplicationCUDA\page_033\matrix_multiplicationCUDA_page_033\auto\images\1712fc64482f188dae2fcaeeaf295e7d8c7e8a9af4e806f2813dda0efd68804d.jpg

---

## Lecture: output\matrix_multiplicationCUDA\page_034\matrix_multiplicationCUDA_page_034\auto

# Summary

• Matrix multiplication is a common computation task in many applications.

Its parallelization in CUDA can be optimized by tiling and use of shared memory.

• When tiles exceed matrix boundaries, loading the input and storing the result needs to check the boundary conditions.

---

## Lecture: output\mpi1\page_001\mpi1_page_001\auto

# Parallel Programming

# Distributed Memory Programming with MPI (1)

Slides adapted from the lecture notes by Peter Pacheco

---

## Lecture: output\mpi1\page_002\mpi1_page_002\auto

# Roadmap

• Writing your first MPI program.   
• Using the common MPI functions.   
• The Trapezoidal Rule in MPI.   
• Collective communication.   
• MPI derived datatypes.   
Performance evaluation of MPI programs.   
Parallel sorting.   
• Safety in MPI programs.

---

## Lecture: output\mpi1\page_003\mpi1_page_003\auto

# A distributed memory system

![](images/9d9e838a3260e0fce4a9d72078d2f1cf743770c28b0be0e916f97bc398f027df.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\mpi1\page_003\mpi1_page_003\auto\images\9d9e838a3260e0fce4a9d72078d2f1cf743770c28b0be0e916f97bc398f027df.jpg

---

## Lecture: output\mpi1\page_004\mpi1_page_004\auto

# Hello World!

#include <stdio.h> $\begin{array} { r l } & { \mathbf { i n t } \quad \operatorname* { m a i n } \left( \mathbf { v o i d } \right) \quad \left\{ \begin{array} { l l } & \\ & { \mathrm { p r i n t } \boldsymbol { \mathrm { f } } \left( \mathbf { \ " } \operatorname { h e l l o } , \mathrm { \quad } \mathrm { w o r l d } \backslash \mathbf { n } \mathbf { \ " } \right) ; } \end{array} \right. } \\ & { \quad \quad \mathbf { r e t u r n } \quad 0 ; } \\ &  \quad \quad \} \end{array}$

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\mpi1\page_004\mpi1_page_004\auto\images\b2dcc1b0f3e3cccbd0767ff6155a5e4cb6f546b1dfee6281f8dded8a2ffde028.jpg

---

## Lecture: output\mpi1\page_005\mpi1_page_005\auto

# Identifying MPI processes

• Common practice to identify processes by nonnegative integer ranks.

• p processes are numbered 0, 1, 2, .. p-1

---

## Lecture: output\mpi1\page_006\mpi1_page_006\auto

# Our first MPI program

1 #include <stdio .h>   
2 #include <string .h> $^ { \prime * }$   
3 #include <mpi.h> /\* For MPI functions , etc \*/   
4   
5 const int MAX_STRING = 100;   
6   
7 int main(void) {   
8 char   
9 int   
10 int $^ { \prime * }$ My process rank   
112 $\mathrm { ~ ! = ~ } 0$ $\}$ for (int $\mathrm { ~ q ~ } = \mathrm { ~ 1 ~ }$ ${ \mathfrak { q } } + +$ } return 0; }

---

## Lecture: output\mpi1\page_007\mpi1_page_007\auto

# Compilation

wrapper script to compile

![](images/edca3aa7175396288aa9956484c004c69c809c87f8f59ded764925d5e51fb8f3.jpg)

source file

mpicc -g -Wall -o mpi_hello mpi_hello.c

produce debugging information

create this executable file name (as opposed to default a.out)

turns on all warnings

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\mpi1\page_007\mpi1_page_007\auto\images\edca3aa7175396288aa9956484c004c69c809c87f8f59ded764925d5e51fb8f3.jpg

---

## Lecture: output\mpi1\page_008\mpi1_page_008\auto

# Execution

mpiexec -n <number of processes> <executable>

mpiexec -n 1 ./mpi_hello

![](images/c52e5d3d74395c7af75a318b22af45ce5848726631679473eb9d1f11514313cb.jpg)

run with 1 process

mpiexec -n 4 ./mpi_hello

![](images/80408988f0f74227b3220a64ad6e0bcd97db6da9db64ebd8e7cf24b73950ad72.jpg)

run with 4 processes

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\mpi1\page_008\mpi1_page_008\auto\images\80408988f0f74227b3220a64ad6e0bcd97db6da9db64ebd8e7cf24b73950ad72.jpg
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\mpi1\page_008\mpi1_page_008\auto\images\c52e5d3d74395c7af75a318b22af45ce5848726631679473eb9d1f11514313cb.jpg

---

## Lecture: output\mpi1\page_009\mpi1_page_009\auto

# Execution

mpiexec -n 1 ./mpi_hello

Greetings from process 0 of 1 !

mpiexec -n 4 ./mpi_hello

Greetings from process 0 of 4 !

---

## Lecture: output\mpi1\page_010\mpi1_page_010\auto

# MPI Programs

Written in C.   
– Has main.   
– Uses stdio.h, string.h, etc.   
• Need to add mpi.h header file.   
• Identifiers defined by MPI start with “MPI_”.   
• First letter following underscore is uppercase. – For function names and MPI-defined types. – Helps to avoid confusion.

---

## Lecture: output\mpi1\page_011\mpi1_page_011\auto

# MPI Components

• MPI_Init – Tells MPI to do all the necessary setup.

int MPI_Init(int\* argc_p /\* in/out \*/,char\*\*\* argv_p /\* in/out \*/);

• MPI_Finalize – Tells MPI we’re done, so clean up anything allocated for this program.

int MPI_Finalize(void );

---

## Lecture: output\mpi1\page_012\mpi1_page_012\auto

# Basic Outline

#include <mpi.h>   
int main $1$ int argc , char\* argv [l) { /\* No MPI calls before this \*/ MPI_Init(&argc, &argv); MPI_Finalize（); /\* No MPI calls after this \*/ return 0;   
}

---

## Lecture: output\mpi1\page_013\mpi1_page_013\auto

# Communicators

• A collection of processes that can send messages to each other.

• MPI_Init defines a communicator that consists of all the processes created when the program is started.

• Called MPI_COMM_WORLD.

---

## Lecture: output\mpi1\page_014\mpi1_page_014\auto

# Communicators

int MPI_Comm_size(

MPI_Comm Comm /\*in \*/int\* comm_sz_p /\* out \*/);

![](images/7c5a795b8235ab3bb0a9d48d46a9d130e586c80d283fb4efac4b3bcc65459f45.jpg)

number of processes in the communicator

int MPI_Comm_rank(

MPI_Comm comm int\* my_rank_p

![](images/c8c7733d15b1c49674997cdbb09ceb9f77d56b7f28b19ae2c3d6f85d1b88c59d.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\mpi1\page_014\mpi1_page_014\auto\images\7c5a795b8235ab3bb0a9d48d46a9d130e586c80d283fb4efac4b3bcc65459f45.jpg
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\mpi1\page_014\mpi1_page_014\auto\images\c8c7733d15b1c49674997cdbb09ceb9f77d56b7f28b19ae2c3d6f85d1b88c59d.jpg

---

## Lecture: output\mpi1\page_015\mpi1_page_015\auto

# SPMD

• Single-Program Multiple-Data • We compile one program. • Process 0 does something different. – Receives messages and prints them while other processes do the work.

• The if-else construct makes our program SPMD.

---

## Lecture: output\mpi1\page_016\mpi1_page_016\auto

# Communication

int MPI_Send(

void\* msg_buf_p   
int msg_size /\* in \*/ MPI_Datatype msg_type /\* in \*/ int dest /\* in \*/ int tag /\* in \*/, MPI_Comm communicator

---

## Lecture: output\mpi1\page_017\mpi1_page_017\auto

# Data types

<table><tr><td rowspan=1 colspan=1>MPI datatype</td><td rowspan=1 colspan=1>C datatype</td></tr><tr><td rowspan=1 colspan=1>MPI CHARMPI SHORTMPI_INTMPI_LONG</td><td rowspan=7 colspan=1>signedcharsignedshort intsigned intsigned longimtsigned longlong intunsignedcharunsignedshort intunsignedintunsigned long intfloatdoublelongdouble</td></tr><tr><td rowspan=1 colspan=1>MPI_LONG_LONGMPI_UNSIGNED CHAR</td></tr><tr><td rowspan=1 colspan=1>MPI_UNSIGNED SHORT</td></tr><tr><td rowspan=1 colspan=1>MPI_UNSIGNED</td></tr><tr><td rowspan=1 colspan=1>MPI_UNSIGNED LONG</td></tr><tr><td rowspan=1 colspan=1>MPI_FLOAT</td></tr><tr><td rowspan=1 colspan=1>MPI_DOUBLEMPI_LONGDOUBLEMPI_BYTEMPIPACKED</td></tr></table>

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\mpi1\page_017\mpi1_page_017\auto\images\45259866e9196e926ce0aadd8d9fa79367ccc2b329c8f18926dd48cd5a5e6532.jpg

---

## Lecture: output\mpi1\page_018\mpi1_page_018\auto

# Communication

int MPI_Recv(

void\* msg_buf_p /\* 0ut \*/, int buf_size /\* in \*/ MPI_Datatype buf_type /\* in int source in \*/ int /\* in \*/ MPI_Comm communicator MPI_Status\* status_p /\* 0ut \*/);

---

## Lecture: output\mpi1\page_019\mpi1_page_019\auto

# Message matching

![](images/8cdca4301b5d758efd4b82e5bbcf72df686b68d26e92196e0ec4e58b7b0ed17e.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\mpi1\page_019\mpi1_page_019\auto\images\8cdca4301b5d758efd4b82e5bbcf72df686b68d26e92196e0ec4e58b7b0ed17e.jpg

---

## Lecture: output\mpi1\page_020\mpi1_page_020\auto

# Receiving messages

• A receiver can get a message without knowing:

– the amount of data in the message, – the sender of the message, – or the tag of the message.

MPI_Recv(result, result_sz, result_type, MPI_ANY_SOURCE, MPI_ANY_TAG, comm, MPI_STATUS_IGNORE);

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\mpi1\page_020\mpi1_page_020\auto\images\9c21acc3c2c499146c2b6ea28a859b3264f5ec3f187c75b60866b2bb25cb061d.jpg
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\mpi1\page_020\mpi1_page_020\auto\images\a44c0ccc81af86dd34be648b468aa72866abbabddf1a93aac7c3f5c07215f141.jpg

---

## Lecture: output\mpi1\page_021\mpi1_page_021\auto

# status_p argument

MPI_Recv(recv_buf_p, recv_buf_sz , recv_type , src, recv_tag, recv_comm , &status);

![](images/738d289d61e5ac3be96d67daabf0f72fe914f5eec31a1227cfef2e0550b397dd.jpg)

MPI_Status\* status;

status.MPI_SOURCE status.MPI_TAG

![](images/c44101d0fc3a770b592c0eb6a3ee9578da16f9acffe84073517750142e593e45.jpg)

MPI_SOURCE MPI_TAG MPI_ERROR

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\mpi1\page_021\mpi1_page_021\auto\images\738d289d61e5ac3be96d67daabf0f72fe914f5eec31a1227cfef2e0550b397dd.jpg
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\mpi1\page_021\mpi1_page_021\auto\images\c44101d0fc3a770b592c0eb6a3ee9578da16f9acffe84073517750142e593e45.jpg

---

## Lecture: output\mpi1\page_022\mpi1_page_022\auto

# How much data am I receiving?

int MPI_Get_count(

MPI_status\* status_p /\*in \*/, MPI_Datatype type /\* in int\* count_p

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\mpi1\page_022\mpi1_page_022\auto\images\0005310ede488befd7887dfd6f962f9636c1681941ad898960683c4f6c73680b.jpg

---

## Lecture: output\mpi1\page_023\mpi1_page_023\auto

# Issues with send and receive

• Exact behavior is determined by the MPI implementation.

• MPI_Send may behave differently with regard to buffer size, cutoffs and blocking.

• MPI_Recv always blocks until a matching message is received.

• Know your implementation; don’t make assumptions!

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\mpi1\page_023\mpi1_page_023\auto\images\405ad26b698e797ada2c8d16bfeae7a352e73d50321e627bff671e79b0ee097e.jpg

---

## Lecture: output\mpi1\page_024\mpi1_page_024\auto

TRAPEZOIDAL RULE IN MPI

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\mpi1\page_024\mpi1_page_024\auto\images\9f4914a7a576dad6de1dbc1665e8ed228c24986e35854fa179d29b1aaf5674e4.jpg

---

## Lecture: output\mpi1\page_025\mpi1_page_025\auto

# The Trapezoidal Rule

![](images/d9e1f5860d5af2296e3db6f9225bded0a783f4d899b8140f1bf3774ea8c81cb4.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\mpi1\page_025\mpi1_page_025\auto\images\d9e1f5860d5af2296e3db6f9225bded0a783f4d899b8140f1bf3774ea8c81cb4.jpg

---

## Lecture: output\mpi1\page_026\mpi1_page_026\auto

# The Trapezoidal Rule

$$
{ \mathrm { A r e a ~ o f ~ o n e ~ t r a p e z o i d } } = { \frac { h } { 2 } } [ f ( x _ { i } ) + f ( x _ { i + 1 } ) ]
$$

$$
h = { \frac { b - a } { n } }
$$

$$
+ h , x _ { 2 } = a + 2 h , . . . , x _ { n - 1 } = a + ( n - 1 ) h , x _ { n }
$$

Sum of trapezoid areas $= h [ f ( x _ { 0 } ) / 2 + f ( x _ { 1 } ) + f ( x _ { 2 } ) + \cdots + f ( x _ { n - 1 } ) +$ f (xn)/2]

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\mpi1\page_026\mpi1_page_026\auto\images\141f9c55e3827d2bafdb3d0a62f6a045f4fb5444e1c092942adec4631e998d57.jpg
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\mpi1\page_026\mpi1_page_026\auto\images\240fcf6240bc3582e7cd50678fa41d604db7a5a2797beaa90e5bd845c2aff628.jpg
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\mpi1\page_026\mpi1_page_026\auto\images\7a912316b0c83a3baa30e8a2731de2733fff7582fc1eec79b45072657156ec18.jpg
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\mpi1\page_026\mpi1_page_026\auto\images\9b3041cd0ecdaf74c82f03dd4514d0cfc1520adc22c83eb8f7cd6ff3a301a51b.jpg

---

## Lecture: output\mpi1\page_027\mpi1_page_027\auto

# One trapezoid

![](images/de761fdfd7960caea9a1c81fd528d2c8e9822a51d3645a8d1cd4afb48caefab9.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\mpi1\page_027\mpi1_page_027\auto\images\de761fdfd7960caea9a1c81fd528d2c8e9822a51d3645a8d1cd4afb48caefab9.jpg

---

## Lecture: output\mpi1\page_028\mpi1_page_028\auto

# Pseudo-code for a serial program

$\begin{array} { r l } & { \int _ { \mathbb { \Gamma } ^ { * } } { \small \textit { \textbf { I n p u t : } } } \ { a } , \ b , \ n \ \ast { \prime } } \\ & {  { \mathrm { \scriptsize ~ \hat { h } ~ = ~ \Gamma ( b - \hat { a } ~ ) / n } } ; } \\ & { \ a \mathbin { \ p p r o x \ } = \ \textup { \scriptsize ( f ( a ) \ + \ \Gamma ( b ) ) } } \\ & {  { \mathbf { f } } _ { 0 } { \ r { \Gamma } } \ ( \ \mathfrak { i } \ = \ 1 ; \ \textup { \scriptsize i } \ \ll \ \mathfrak { n } { - 1 } ; } \\ & { \qquad \times _ { - } \mathfrak { i } \ = \ \partial \ + \ \mathfrak { i } * \ h ; } \\ & { \qquad \mathrm { \scriptsize ~ a \ p p r o x \ + = \ \Gamma ( \ x _ { - } \dag \ ) } ; } \end{array}$ /2.0; i++) { $\begin{array} { l } { \displaystyle \mathsf { \partial } \mathsf { \partial } } \\ { \mathsf { \partial } \mathsf { \mathsf { p } } \mathsf { p } \mathsf { r } \mathsf { o } \mathsf { x } \ = \mathsf { \partial } \mathsf { h } \ast \mathsf { a } \mathsf { p } \mathsf { p } \mathsf { r } \mathsf { o } \mathsf { x } ; } \end{array}$

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\mpi1\page_028\mpi1_page_028\auto\images\e56112c9c811a8a204208e78232d37bfacf583c166a31db4ddecc846a1998e60.jpg
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\mpi1\page_028\mpi1_page_028\auto\images\f30d581e9dc078f1b214e0718244e76131c87df99b860b488b39ee5f3a451b2a.jpg

---

## Lecture: output\mpi1\page_029\mpi1_page_029\auto

# Parallelizing the Trapezoidal Rule

1. Partition problem solution into tasks.

2. Identify communication channels between tasks.

3. Aggregate tasks into composite tasks.

4. Map composite tasks to cores.

---

## Lecture: output\mpi1\page_030\mpi1_page_030\auto

# Parallel pseudo-code

1   
2   
3   
4   
5   
6 $=$   
7 if (my_rank $\mathrm { ~ : = ~ } \mathrm { ~ 0 ) }$   
8   
9 else /\* $m y \_ r a n k \ = = \ 0 \ * /$

---

## Lecture: output\mpi1\page_031\mpi1_page_031\auto

# Tasks and communications for Trapezoidal Rule

![](images/6350636fed3d2bb02d249a8d45b21712b7248ed94db91e2bab815a4c18a228fc.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\mpi1\page_031\mpi1_page_031\auto\images\6350636fed3d2bb02d249a8d45b21712b7248ed94db91e2bab815a4c18a228fc.jpg

---

## Lecture: output\mpi1\page_032\mpi1_page_032\auto

# First version (1)

![](images/1707c188d5d6ec3c5f19f4adcbaf2b125520d2a9e40b1f9707566a9371b72ace.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\mpi1\page_032\mpi1_page_032\auto\images\1707c188d5d6ec3c5f19f4adcbaf2b125520d2a9e40b1f9707566a9371b72ace.jpg

---

## Lecture: output\mpi1\page_033\mpi1_page_033\auto

# First version (2)

} else $=$ MPI_Recv(&local_int , l， MPI_DouBLE , source, 0, MPI_COMM_WORLD , MPI_STATUS_IGNORE ); $+ =$ $\}$ if (my_rank $\scriptstyle \mathbf { \mu = } 0$ $=$ printf("of the integral from %f to %f $=$ MPI_Finalize (); return 0; $\}$

---

## Lecture: output\mpi1\page_034\mpi1_page_034\auto

# First version (3)

double Trap( double left_endpt /\* in \*/, double right_endpt /\* in \*/ , int double base_len double estimate, x; int i; 89 estimate $=$ (f(left_endpt) + f(right_endpt ))/2.0; for $\mathrm { ~  ~ { ~ i ~ } ~ } = \mathrm { ~  ~ { ~ l ~ } ~ }$ $^ +$ $+ =$ $\}$ $=$ return estimate ; (cid:) $\}$

---

## Lecture: output\mpi1\page_035\mpi1_page_035\auto

# Dealing with I/O

#include <stdio .h> #include <mpi.h>

int main(void) { int my_rank, comm_sz;

Each process just prints a message.

MPI_Init(NULL , NULL );  
MPI_Comm_size(MPI_COMM_WORLD ， &comm_sz );  
MPI_Comm_rank(MPI_COMM_WORLD , &my_rank );

my_rank , comm_sz );

MPI_Finalize () ; return 0; $\}$

---

## Lecture: output\mpi1\page_036\mpi1_page_036\auto

# Running with 6 processes

$\it { ? }$ $\it { ? }$ $\it { ? }$ 6 $\it { ? }$ $\it { ? }$ $\it { ? }$

unpredictable output

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\mpi1\page_036\mpi1_page_036\auto\images\11973c4bd46e8c542f467dfea9975ff5ef72dca0a33fd0949dd0bd9e2d2bf590.jpg

---

## Lecture: output\mpi1\page_037\mpi1_page_037\auto

# Input

• Most MPI implementations only allow process 0 in MPI_COMM_WORLD access to stdin.

• Process 0 must read the data (scanf) and send to the other processes.

MPI_Comm_rank(MPI_COMM_WORLD , &my_rank );  
MPI_Comm_size(MPI_COMM_WORLD ，&comm_sz );

---

## Lecture: output\mpi1\page_038\mpi1_page_038\auto

# Function for reading user input

void Get_input(

int my_rank int comm_sz in double \* /\* out \*/, double\* b_p int\* n int dest;

$\scriptstyle = = \quad 0$ for (dest $\qquad = \quad 1$ $<$ $\}$ else { /\* my_rank != 0 \*/ MPI_STATUS_IGNORE ); MPI_STATUS_IGNORE ); MPI_STATUS_IGNORE); } /\* Get_input \*/

---

## Lecture: output\mpi2\page_001\mpi2_page_001\auto

# Parallel Programming

# Distributed Memory Programming With MPI (2)

Slides adapted from the lecture notes by Peter Pacheco

---

## Lecture: output\mpi2\page_002\mpi2_page_002\auto

# Roadmap

• Writing your first MPI program.   
• Using the common MPI functions.   
• The Trapezoidal Rule in MPI.   
• Collective communication.   
• MPI derived datatypes.   
Performance evaluation of MPI programs.   
• Parallel sorting.   
• Safety in MPI programs.

---

## Lecture: output\mpi2\page_003\mpi2_page_003\auto

# COLLECTIVE COMMUNICATION

---

## Lecture: output\mpi2\page_004\mpi2_page_004\auto

# A tree-structured global sum Processes

![](images/e66ec86a8b5e44ecbeaba9f994f34cda1ff791605ba147cbca61148f26d2097d.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\mpi2\page_004\mpi2_page_004\auto\images\e66ec86a8b5e44ecbeaba9f994f34cda1ff791605ba147cbca61148f26d2097d.jpg

---

## Lecture: output\mpi2\page_005\mpi2_page_005\auto

# Tree-structured communication

1. In the first phase:

(a) Process 1 sends to 0, 3 sends to 2, 5 sends to 4, and 7 sends to 6.   
(b) Processes 0, 2, 4, and 6 add in the received values.   
(c) Processes 2 and 6 send their new values to processes 0 and 4, respectively.   
(d) Processes 0 and 4 add the received values into their new values.

2. (a) Process 4 sends its newest value to process 0. (b) Process 0 adds the received value to its newest value.

---

## Lecture: output\mpi2\page_006\mpi2_page_006\auto

# An alternative tree-structured global sum

Processes

![](images/069d23d4dd8ebecf459dc33dd8d1766d93e8916ca627b82a73f86e5384846cc7.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\mpi2\page_006\mpi2_page_006\auto\images\069d23d4dd8ebecf459dc33dd8d1766d93e8916ca627b82a73f86e5384846cc7.jpg

---

## Lecture: output\mpi2\page_007\mpi2_page_007\auto

# MPI_Reduce

int MPI_Reduce(

void\*   
void\*   
int in   
MPI_Datatype datatype in operator in $^ { \ast / \cdot , }$   
int in $^ { * / }$   
MPI_Comm comm in

MPI_COMM_WORLD);

double local_x [N], sum[N];   
MPI_Reduce(local_x, sum , N, MPI_DouBLE, MPI_SUM, 0, MPI_COMM_WORLD);

---

## Lecture: output\mpi2\page_008\mpi2_page_008\auto

# Predefined reduction operators in MPI

<table><tr><td rowspan=1 colspan=1>Operation Value</td><td rowspan=1 colspan=1>Meaning</td></tr><tr><td rowspan=1 colspan=1>MPIMAX</td><td rowspan=1 colspan=1>Maximum</td></tr><tr><td rowspan=1 colspan=1>MPIMIN</td><td rowspan=1 colspan=1>Minimum</td></tr><tr><td rowspan=1 colspan=1>MPI_SUM</td><td rowspan=1 colspan=1>Sum</td></tr><tr><td rowspan=1 colspan=1>MPI_PROD</td><td rowspan=1 colspan=1>Product</td></tr><tr><td rowspan=1 colspan=1>MPI_LAND</td><td rowspan=1 colspan=1>Logical and</td></tr><tr><td rowspan=1 colspan=1>MPI_BAND</td><td rowspan=1 colspan=1>Bitwise and</td></tr><tr><td rowspan=1 colspan=1>MPI_LOR</td><td rowspan=1 colspan=1>Logical or</td></tr><tr><td rowspan=1 colspan=1>MPI_BOR</td><td rowspan=1 colspan=1>Bitwise or</td></tr><tr><td rowspan=1 colspan=1>MPI_LXOR</td><td rowspan=1 colspan=1>Logical exclusive or</td></tr><tr><td rowspan=1 colspan=1>MPI_BXOR</td><td rowspan=1 colspan=1>Bitwise exclusive or</td></tr><tr><td rowspan=1 colspan=1>MPIMAXLOC</td><td rowspan=1 colspan=1>Maximum and location of maximum</td></tr><tr><td rowspan=1 colspan=1>MPIMINLOC</td><td rowspan=1 colspan=1>Minimum and location of minimum</td></tr></table>

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\mpi2\page_008\mpi2_page_008\auto\images\b8f4221e1a30eca02d2c04b38fe75a2c6145d1f3ea3e37b475f6c85aa482b5ae.jpg

---

## Lecture: output\mpi2\page_009\mpi2_page_009\auto

# Collective vs. Point-to-Point Communications

All the processes in the communicator must call the same collective function.

For example, a program that attempts to match a call to MPI_Reduce on one process with a call to MPI_Recv on another process is erroneous, and, in all likelihood, the program will hang or crash.

---

## Lecture: output\mpi2\page_010\mpi2_page_010\auto

# Collective vs. Point-to-Point Communications

• The arguments passed by each process to an MPI collective communication must be “compatible.”

For example, if one process passes in 0 as the dest_process and another passes in 1, then the outcome of a call to MPI_Reduce is erroneous, and, once again, the program is likely to hang or crash.

---

## Lecture: output\mpi2\page_011\mpi2_page_011\auto

# Collective vs. Point-to-Point Communications

• The output_data_p argument is only used on dest_process.

• However, all of the processes still need to pass in an actual argument corresponding to output_data_p, even if it’s just NULL.

---

## Lecture: output\mpi2\page_012\mpi2_page_012\auto

# Collective vs. Point-to-Point Communications

• Point-to-point communications are matched on the basis of tags and communicators.

• Collective communications don’t use tags.

• They’re matched solely on the basis of the communicator and the order in which they’re called.

---

## Lecture: output\mpi2\page_013\mpi2_page_013\auto

# Example (1)

<table><tr><td rowspan=1 colspan=1>Time</td><td rowspan=1 colspan=1>Process 0</td><td rowspan=1 colspan=1>Process 1</td><td rowspan=1 colspan=1>Process 2</td></tr><tr><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>a = 1;c = 2</td><td rowspan=1 colspan=1>a = 1；c = 2</td><td rowspan=1 colspan=1>a = 1;c = 2</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>MPI_Reduce (&amp;a, &amp;b, . ..)</td><td rowspan=1 colspan=1>MPI_Reduce (&amp;c, &amp;d, ...)</td><td rowspan=1 colspan=1>MPI_Reduce (&amp;a, &amp;b, . ..)</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>MPI_Reduce (&amp;c, &amp;d, . ..)</td><td rowspan=1 colspan=1>MPI_Reduce (&amp;a, &amp;b, ...)</td><td rowspan=1 colspan=1>MPI_Reduce (&amp;c, &amp;d, . ..)</td></tr></table>

# Multiple calls to MPI_Reduce

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\mpi2\page_013\mpi2_page_013\auto\images\dc44f346d8c49fcffc433b72a95301aa0c398b2f885ae7ece4534c2c551b9c82.jpg

---

## Lecture: output\mpi2\page_014\mpi2_page_014\auto

# Example (2)

Suppose that each process calls MPI_Reduce with operator MPI_SUM, and destination process 0.

At first glance, it might seem that after the two calls to MPI_Reduce, the value of b will be 3, and the value of d will be 6.

---

## Lecture: output\mpi2\page_015\mpi2_page_015\auto

# Example (3)

• However, the names of the memory locations are irrelevant to the matching of the calls to MPI_Reduce.

• The order of the calls will determine the matching so the value stored in b will be 1+2+1 = 4, and the value stored in d will be 2+1+2 = 5.

---

## Lecture: output\mpi2\page_016\mpi2_page_016\auto

# MPI_Allreduce

• Useful in a situation in which all of the processes need the result of a global sum in order to complete some larger computation.

int MPI_Allreduce(

void \* input_data_p /\*in void\* output_data_p /\* out \*/, int count in MPI_Datatype datatype /\* in MPI_Op operator /\* in MPI_Comm comm /\* in

---

## Lecture: output\mpi2\page_017\mpi2_page_017\auto

Processes

![](images/a8fe99d7685655960349726e6184ebf6c7f6925cd28679bda6c615806d1a0ed0.jpg)

A global sum followed by distribution of the result.

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\mpi2\page_017\mpi2_page_017\auto\images\a8fe99d7685655960349726e6184ebf6c7f6925cd28679bda6c615806d1a0ed0.jpg

---

## Lecture: output\mpi2\page_018\mpi2_page_018\auto

Processes

![](images/697ab88da5837b8f06dcb65a94e5ca1d683794ef4a149d7645e6a7f988fb0cee.jpg)

A butterfly-structured global sum.

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\mpi2\page_018\mpi2_page_018\auto\images\697ab88da5837b8f06dcb65a94e5ca1d683794ef4a149d7645e6a7f988fb0cee.jpg

---

## Lecture: output\mpi2\page_019\mpi2_page_019\auto

# Broadcast

• Data belonging to a single process is sent to all of the processes in the communicator.

int MPI_Bcast(

void\* $\begin{array} { l l l } { { \nonumber / _ { * } } } & { { i n / o u t } } & { { * \nonumber , } } \\ { { \nonumber / _ { * } } } & { { i n } } & { { * \nonumber , } } \\ { { \nonumber / _ { * } } } & { { i n } } & { { * \nonumber , } } \\ { { \nonumber / _ { * } } } & { { i n } } & { { * \nonumber , } } \\ { { \nonumber / _ { * } } } & { { i n } } & { { * \nonumber , } } \end{array}$   
int   
MPI_Datatype datatype   
int source_proc   
MPI_Comm comm

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\mpi2\page_019\mpi2_page_019\auto\images\1ab9c015e5c2f5f661c4fec2ac3145cd3f506f0297bfb4aac0af98fee0b7e968.jpg

---

## Lecture: output\mpi2\page_020\mpi2_page_020\auto

![](images/654d82b1ad63346e271ba7bcd3553abb38dffdbb0afa28676eab911cf6979681.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\mpi2\page_020\mpi2_page_020\auto\images\654d82b1ad63346e271ba7bcd3553abb38dffdbb0afa28676eab911cf6979681.jpg

---

## Lecture: output\mpi2\page_021\mpi2_page_021\auto

# A version of Get_input that uses MPI_Bcast

void Get_input(

int my_rank int comm_sz double\* a_p out double \* b p out int\* n_p

MPI_Bcast(a_P, 1， MPI_DoUBLE ， O, MPI_COMM_wORLD );MPI_Bcast(b_p, 1, MPI_DoUBLE , O, MPI_COMM_WORLD );/\* Get_input \*/

---

## Lecture: output\mpi2\page_022\mpi2_page_022\auto

# Vector Addition Example

X+ ${ \begin{array} { l l l } { \mathbf { y } } & { = } & { ( x _ { 0 } , x _ { 1 } , \ldots , x _ { n - 1 } ) + ( y _ { 0 } , y _ { 1 } , . } \\ & { = } & { ( x _ { 0 } + y _ { 0 } , x _ { 1 } + y _ { 1 } , \ldots , x _ { n - 1 } + } \\ & { = } & { ( z _ { 0 } , z _ { 1 } , \ldots , z _ { n - 1 } ) } \\ & { = } & { \mathbf { z } } \end{array} }$ yn−1)

Compute a vector sum.

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\mpi2\page_022\mpi2_page_022\auto\images\8217b671747877bc6b9a37c69fcf6818beefb987902dc3fca8e137b97e29ee59.jpg

---

## Lecture: output\mpi2\page_023\mpi2_page_023\auto

# Serial implementation of vector addition

void Vector_sum(double x[l, double y[l , double z[l, int n) { inti;

$$
\begin{array} { l } { { \mathrm { { \bf ~ f o r } ~ \omega ~ ( \mathrm { ~ i ~ \omega ~ = ~ 0 } ; ~ \varepsilon ~ i ~ < ~ n ~ ; ~ \varepsilon ~ i + + ) } } } \\ { { \mathrm { { \bf ~ \varepsilon ~ } ~ } } } \\ { { \mathrm { { \bf ~ \varepsilon ~ } ~ } } } \\ { { \mathrm { { \bf ~ \varepsilon ~ } ~ } } } \\ { { \mathrm { { \bf ~ \varepsilon ~ } } / { * \mathrm { { \bf ~ \varepsilon ~ } } V e c t o r \_ s u m \mathrm { ~ \omega ~ * } } / } } \end{array}
$$

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\mpi2\page_023\mpi2_page_023\auto\images\60107601aa8fdfa1cb4ca96df7808fe701344aa76740ecdd4849ed32af8f590d.jpg

---

## Lecture: output\mpi2\page_024\mpi2_page_024\auto

# Different partitions of a 12-component vector among 3 processes

<table><tr><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>9</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>7</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>-S</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1>9</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1>9</td><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>11</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1>11</td><td rowspan=1 colspan=1>45</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>11</td></tr></table>

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\mpi2\page_024\mpi2_page_024\auto\images\02617a1ee79d9e75e690a45a27e56089a2766181bda95ebf77edb447ffd7f4f9.jpg

---

## Lecture: output\mpi2\page_025\mpi2_page_025\auto

# Partitioning options

• Block partitioning – Assign blocks of consecutive components to each process.

• Cyclic partitioning – Assign components in a round robin fashion.

• Block-cyclic partitioning – Use a cyclic distribution of blocks of components.

---

## Lecture: output\mpi2\page_026\mpi2_page_026\auto

# Parallel implementation of vector addition

void Parallel_vector_sum(

double local_x  ]   
double local_y [l ,   
double local_z[]   
int

int local_i;

$\}$ /\* Parallel_vector_sum \*/

---

## Lecture: output\mpi2\page_027\mpi2_page_027\auto

# Scatter

MPI_Scatter can be used in a function that reads in an entire vector on process 0 but only sends the needed components to each of the other processes.

int MPI_Scatter( void\* int send_count MPI_Datatype send_type /\* in void\* recv_buf_p /\* out \*/, int recv_count in MPI_Datatype recv_type 丿\* in int src_proc in MPI_Comm comm

---

## Lecture: output\mpi2\page_028\mpi2_page_028\auto

# Reading and distributing a vector

void Read_vector(

double int in int n \* in char vec_name [] /\* in int my_rank /\* in MPI_Comm comm in

double\* a = NULL;   
int i;

if (my_rank $\scriptstyle = = \atop \mathrm { 0 }$ $=$ malloc(n\*sizeof (double )); for( $ { \mathrm { ~  ~ \dot { ~ } { ~ 1 ~ } ~ } } = \mathrm { ~  ~ 0 ~ }$ $\mathrm { ~ i ~ } < \mathrm { ~ n ~ }$ $\dot { 1 } + + )$ (d) scanf("%lf", &a[i ]); $\}$ else { /\* Read_vector \*/

---

## Lecture: output\mpi2\page_029\mpi2_page_029\auto

# Gather

• Collect all of the components of the vector onto process dest_proc.

int MPI_Gather( void\* send_buf_p int send_count MPI_Datatype send_type in void\* \* int recv_count in MPI_Datatype recv_type in int dest_proc /\* in MPI_Comm comm

---

## Lecture: output\mpi2\page_030\mpi2_page_030\auto

# Print a distributed vector (1)

void Print_vector(

double local_b[]   
int local_n   
int n /\*in   
char title l]   
int my_rank   
MPI_Comm comm /\* in \*/) double\* b = NULL ;   
int i;

---

## Lecture: output\mpi2\page_031\mpi2_page_031\auto

# Print a distributed vector (2)

if (my_rank $\scriptstyle = { \begin{array} { l l } { \mathbf { - } } & { \mathbf { 0 } } \end{array} }$ b = malloc (n\*sizeof (double )); for( $\mathrm { ~  ~ { ~ i ~ } ~ } = \mathrm { ~ \ r ~ { ~ 0 ~ } ~ }$   
$\}$ else{   
1   
/\* Print_vector \*/

---

## Lecture: output\mpi2\page_032\mpi2_page_032\auto

# Allgather

Concatenates the contents of each process’ send_buf_p and stores this in each process’ recv_buf_p.

• As usual, recv_count is the amount of data being received from each process.

int MPI_Allgather( void $^ *$ int MPI_Datatype \* in void\* \* int recv_count in MPI_Datatype recv_type in MPI_Comm comm

---

## Lecture: output\mpi2\page_033\mpi2_page_033\auto

# Matrix-vector multiplication

1 = (aij) is an m × n matrix

![](images/03056f7ed6a128eebbb72c40f1cbfbf7d92cb7225bd5eab4f7283da7e786f2e1.jpg)

x is a vector with n components

y = Ax is a vector with m components

![](images/a6f5ff3f111cdb9d03537bdb29eccdbbf11dd7a0bb860de7d4318e99b89ef257.jpg)

yi = aiox0 + ai1x1 + ai2x2 + · · ai,n−1Xn−1

i-th component of y

Dot product of the ith row of A with x.

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\mpi2\page_033\mpi2_page_033\auto\images\03056f7ed6a128eebbb72c40f1cbfbf7d92cb7225bd5eab4f7283da7e786f2e1.jpg
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\mpi2\page_033\mpi2_page_033\auto\images\a6f5ff3f111cdb9d03537bdb29eccdbbf11dd7a0bb860de7d4318e99b89ef257.jpg

---

## Lecture: output\mpi2\page_034\mpi2_page_034\auto

# Matrix-vector multiplication

![](images/70d8f5adbd6eca34681fe51dd40ffee7349bacc6892ffb7ddec117cb9ccbb71f.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\mpi2\page_034\mpi2_page_034\auto\images\70d8f5adbd6eca34681fe51dd40ffee7349bacc6892ffb7ddec117cb9ccbb71f.jpg

---

## Lecture: output\mpi2\page_035\mpi2_page_035\auto

# Multiply a matrix by a vector

fo1 $\begin{array} { l } { { { \begin{array} { l } { { F o r } } \\ { { \mathrm {  ~ \Lambda ~ } ^ { \prime } ~ e a c h ~ r o w ~ } \ o f ~ A ~ * ^ { \prime } } \ \ } } \\ { { \mathrm {  ~ \Lambda ~ } ^ { \prime } ~ ( \ \perp ~ = ~ 0 ; ~ \ \mathrm {  ~ i ~ } < \ \mathrm {  ~ n } ; ~ \mathrm {  ~ i } + + ) ~ \left\{ \begin{array} { l } { { { \Lambda } } } \\ { { { \Lambda } } } \end{array} \right. } } \\ { { \mathrm {  ~ \Lambda ~ } ^ { \prime } * { \pmod { ~ d o t } } { \cal P } r o d u c t { \quad o f } { \quad i t h } \ \mathrm {  ~ \Lambda ~ } ^ { \prime } } } \\ { { \mathrm {  ~ \nabla ~ } [ \ \mathrm { i } \ ] { \bf \Lambda } { \bf \Sigma } { } = { \bf \Lambda } { } { } 0 . 0 ; } } \\ { { { \mathrm {  ~ { \cal ~ f } ~ o r ~ } } { \mathrm {  ~ { \Sigma ~ } } } ( \ \mathrm { j } { \bf \Lambda } { } = { \bf \Lambda } { } ) { } ; ~ \mathrm {  ~ j ~ } { < \mathrm {  ~ n } ; ~ \mathrm {  ~ j } + } { } + { } ) } \ \ } \\ { { \mathrm {  ~ \nabla ~ } [ \ \mathrm { i } \ ] { \bf \Lambda } { } + = { \bf \Lambda } { } { \tt } [ \ \mathrm { i } \ ] [ \ \mathrm { j } ] * { } { \bf x } [ { \bf \Lambda } { } ] { \bf \Lambda } { } ; } } \end{array} }  \end{array}$ row with x \*/

Serial pseudo-code

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\mpi2\page_035\mpi2_page_035\auto\images\7a6135a9a1b65b426d267df00939289b1a7916795e358e567d1eb260dd71c2df.jpg

---

## Lecture: output\mpi2\page_036\mpi2_page_036\auto

# C style arrays

![](images/ed67b4d956695c945e9faf306d75f1642306c8a2e8b63ad624fc48bc4f904b2f.jpg)

01234567891011

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\mpi2\page_036\mpi2_page_036\auto\images\ed67b4d956695c945e9faf306d75f1642306c8a2e8b63ad624fc48bc4f904b2f.jpg

---

## Lecture: output\mpi2\page_037\mpi2_page_037\auto

# Serial matrix-vector multiplication

voi $\begin{array} { r l }  \mathbf { d } \quad \mathrm { M a t \_ V e c t \_ m u l t } ( \begin{array} { l l l l l } & & & { } \\ & { } & { } & { } & { } \\ { \mathbf { d o u b l e } } & { \mathbb { A } [ \begin{array} { l l l l } & { } & { } & { } & { } \\ { } & { } & { } & { } & { } \end{array} ] , } & {  } \\ { \mathbf { d o u b l e } } & { } & { \times [ \begin{array} { l l l l } { } & { } & { } & { } \\ { } & { } & { } & { } \\ { } & { } & { } & { } \end{array} ] } & {  \begin{array} { l l l l } & { } & { } & { } \\ { } & { } & { } & { \mathrm { \ast \it ~ / ~ } } \end{array}  , } \\ { \mathbf { d o u b l e } } & { } & { \times [ \begin{array} { l l l l } { } & { } & { \mathord { / { \vphantom { ( | \begin{array} { l l l l l } { } & { } & { } & { } \\ { } & { } & { } & { } \end{ | } } & { } & {  } \end{array}  } } \\ { } & { } & { } & { } & { } \end{array} ] } & {  \begin{array} { l l l l } & { } & { } & { } \\ { } & { } & { } & { \mathrm { \ast \it ~ / ~ } } \end{array}  , } \\ { \mathbf { i n t \_ i n t } } & { } & { \mathrm { \nmid \ n } } & { } & { \mathrm { / ~ / \ast ~ } } & { i n } & { \mathrm { \ast \it / ~ } } \end{array} \} } \\ { \mathbf { i n t \_ i \cdot \ i \cdot \ j \cdot } } & { \times } & { } & { } \end{array}$ $\begin{array} { r l } { { \bf f o r } } & { ( \mathrm {  ~ i ~ } = \mathrm {  ~ 0 ~ } ; \mathrm {  ~ i ~ } < \mathrm {  ~ n ~ } ; \mathrm {  ~ i + } ) \mathrm {  ~ \left\{ ~ \right. ~ } }  \\ { \mathrm {  ~ \gamma ~ } [ \mathrm {  ~ i ~ } ] } & { = \mathrm {  ~ 0 ~ } . 0 ; } \\ & { { \bf f o r } } & { ( \mathrm {  ~ j ~ } = \mathrm {  ~ 0 } ; \mathrm {  ~ j ~ } < \mathrm {  ~ n ~ } ; \mathrm {  ~ j + } ) } \\ & { \mathrm {  ~ \gamma ~ } [ \mathrm {  ~ i ~ } ] } & { + = \mathrm {  ~ \ z ~ } [ \mathrm {  ~ i ~ } { \ast } \mathrm { n + } \mathrm { j } ] \ast \mathrm { x } [ \mathrm {  ~ j ~ } ] ; } \\ { \mathrm {  ~ \gamma ~ } } \\ { \mathrm {  ~ \gamma ~ } / \ast } & { M a t _ { - } \nu e c t _ { - } m u l t * / } \end{array}$

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\mpi2\page_037\mpi2_page_037\auto\images\16969e1e6306233ed4f5a890868642361005d25ded6112d6c71447dffc3721be.jpg
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\mpi2\page_037\mpi2_page_037\auto\images\8c61013726f1c776da448264c32e4e32e1a8eac9c2dd1a234ddcf15751be3c5a.jpg

---

## Lecture: output\mpi2\page_038\mpi2_page_038\auto

# An MPI matrix-vector multiplication function (1)

void Mat_vect_mult( double local_A[l /\* in \*/ double local_x[l /\* in \*/， double local_y Il /\* 0ut \*/ int local_m /\* in \*/ int n /\* in \*/ int local_n ノ\* in \*/ MPI_Comm comm /\*in

double \* x ; int local_i, j; int local_ok = 1:

---

## Lecture: output\mpi2\page_039\mpi2_page_039\auto

# An MPI matrix-vector multiplication function (2)

x = mal loc (n\* sizeof(double )); MPI_Allgather（local_x， local_n, MPI_DouBLE , $ \begin{array} { r l } & { [ \mathbf { o r } \quad ( \mathbf { \lambda } \mathrm { 1 } \circ \mathbf { c a l \_ i } \ \mathbf { \lambda } \ \mathrm { ~ \mathbf { i } } = \ 0 ; \ \mathbf { \lambda } \ \mathrm { ~ \lambda } \mathrm { ~ \lambda } \mathrm { ~ o c a l \_ i ~ } \ \mathrm { ~ \lambda } \mathrm { ~ \mathbf { i } ~ \lambda ~ } < \ \mathrm { ~ \lambda } \mathrm { ~ \lambda } \mathrm { ~ o c a l \_ ~ } } \\ & { \qquad \mathrm { ~ \lambda } \mathrm { ~ \lambda } \mathrm { ~ o c a l \_ y ~ } \ [ \mathrm { ~ \lambda } ] \circ \mathrm { c a l \_ i ~ } \ \mathrm { ~ \lambda } ] \ = \ \mathbf { \lambda } \ \mathrm { ~ \mathbf { 0 } . ~ \mathbf { 0 } ~ } ; } \\ & { \qquad \mathbf { f o r } \quad ( \mathbf { \lambda } \mathrm { ~ } \mathrm { ~ \mathbf { j } } \ \ \mathbf { \lambda } \mathrm { ~ = ~ \lambda } \ 0 ; \ \mathbf { \lambda } \mathrm { ~ \mathbf { j } } \ \textsf { < ~ n } ; \ \mathbf { j } + + ) } \\ & { \qquad \mathrm { ~ \lambda } \mathrm { ~ o c a l \_ y ~ } [ \mathrm { ~ \lambda } \mathrm { ~ } ] \circ \mathrm { c a l \_ i ~ } \ \mathrm { ~ \lambda } \mathrm { ~ \mathbf { i } ~ } + = \ \mathrm { ~ \lambda } \mathrm { ~ \lambda } \mathrm { ~ o c a l \_ { - } a l \_ { - } a l ~ } } \\ & { \qquad \ } \\ & { \qquad \mathrm { ~ \lambda } \mathrm { ~ \ } \mathrm { ~ \ } \mathrm { ~ \ } \mathrm { ~ \ } } \\ & { \qquad \mathrm { ~ \lambda } \mathrm { ~ \ } \mathrm { ~ \ } \mathrm { ~ \ } \mathrm { ~ \ } \mathrm { ~ \ } \mathrm { ~ \ } \mathrm { ~ \ } \mathrm { ~ \ } \mathrm { ~ \ } } \\ &  \qquad \mathrm { ~ \ } \mathrm { ~ \ } \mathrm { ~ \ } \mathrm { ~ \ } \mathrm { ~ \ } \mathrm { ~ \ } \mathrm { ~ \ } \mathrm { ~ \ } \mathrm { ~ \ } \mathrm { ~ \ } \mathrm { ~ \ } \mathrm { ~ \ } \mathrm { ~ \ } \mathrm { ~ \ } \mathrm { ~ \ } \mathrm { ~ \ } \mathrm { ~ \ } \ \end{array}$

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\mpi2\page_039\mpi2_page_039\auto\images\21d398d8ef73d974bef9b7d18720d2e2df470afae510b104084096b93b9bfed6.jpg

---

## Lecture: output\mpi3\page_001\mpi3_page_001\auto

# Parallel Programming

# Distributed Memory Programming with MPI (3)

Slides adapted from the lecture notes by Peter Pacheco

---

## Lecture: output\mpi3\page_002\mpi3_page_002\auto

# Roadmap

Writing your first MPI program.

Using the common MPI functions.

The Trapezoidal Rule in MPI.

Collective communication.

MPI derived datatypes.

• Performance evaluation of MPI programs.

Parallel sorting.

Safety in MPI programs.

---

## Lecture: output\mpi3\page_003\mpi3_page_003\auto

# MPI DERIVED DATATYPES

---

## Lecture: output\mpi3\page_004\mpi3_page_004\auto

# Derived datatypes

Used to represent any collection of data items in memory by storing both the types of the items and their relative locations in memory.

• The idea is that if a function that sends data knows this information about a collection of data items, it can collect the items from memory efficiently.

• Similarly, a function that receives data can distribute the items into their correct destinations in memory when they’re received.

---

## Lecture: output\mpi3\page_005\mpi3_page_005\auto

# Derived datatypes

• A derived datatype consists of a sequence of basic MPI data types together with a displacement for each of the data types.

• Trapezoidal Rule example:

{(MPI_DOUBLE, 0), (MPI_DOUBLE, 16), (MPI_INT, 24)}

<table><tr><td rowspan=1 colspan=1>Variable</td><td rowspan=1 colspan=1>Address</td></tr><tr><td rowspan=1 colspan=1>a</td><td rowspan=1 colspan=1>24</td></tr><tr><td rowspan=1 colspan=1>b</td><td rowspan=1 colspan=1>40</td></tr><tr><td rowspan=1 colspan=1>n</td><td rowspan=1 colspan=1>48</td></tr></table>

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\mpi3\page_005\mpi3_page_005\auto\images\0c5dbd73f73a71debcdf10e8c45914fd46438a1e3903c2577db03fed7f75ea3b.jpg

---

## Lecture: output\mpi3\page_006\mpi3_page_006\auto

# MPI_Type create_struct

• Builds a derived datatype that consists of individual elements that have different basic types.

int MPI_Type_create_struct( int in int array_of_blocklengths [] in MPI_Aint array_of_displacements [] in MPI_Datatype array_of_types [] in MPI_Datatype\* new_type_p

---

## Lecture: output\mpi3\page_007\mpi3_page_007\auto

# MPI_Get_address

• Returns the address of the memory location referenced by location_p.

The special type MPI_Aint is an integer type that is big enough to store an address on the system.

int MPI_Get_address ( void\* location_p MPI_Aint\* address_p

---

## Lecture: output\mpi3\page_008\mpi3_page_008\auto

# MPI_Type_commit

• Allows the MPI implementation to optimize its internal representation of the datatype for use in communication functions.

---

## Lecture: output\mpi3\page_009\mpi3_page_009\auto

# MPI_Type_free

• When we’re finished with our new type, this frees any additional storage used.

---

## Lecture: output\mpi3\page_010\mpi3_page_010\auto

# Get input function with a derived datatype (1)

void Build_mpi_type(

double\* a_p   
double\* b /\*in int $^ *$ n_p /\* in MPI_Datatype\*

MPI_Datatype array_of_types[3】 = {MPI_DoUBLE , MPI_DouBLE , MPI_INT $\}$ $[ 3 ] \ = \ \{ 0 \} ;$

---

## Lecture: output\mpi3\page_011\mpi3_page_011\auto

# Get input function with a derived datatype (2)

MPI_Get_address (a_p , &a_addr );   
MPI_Get_address (b_p , &b_addr );   
MPI_Get_address(n_P , &n_addr );

array_of_displacements [l] = b_addr-a_addr; array_of_displacements [2] = n_addr—a_addr; MPI_Type_create_struct(3, array_of_blocklengths ,

array_of_displacements , array_of_types input_mpi_t_p);

MPI_Type_commit (input_mpi_t_p ); /+ Build_mpi_type \*/

---

## Lecture: output\mpi3\page_012\mpi3_page_012\auto

# Get_input function with a derived datatype (3)

void Get_input(int my_rank, int comm_sz , double\* a_p, double\* b_p , int $^ *$ $\{$ $\}$ $^ 1$ $0$ ，MPI_COMM_WORLD); MPI_Type_free(&input_mpi_t );   
$\}$

---

## Lecture: output\mpi3\page_013\mpi3_page_013\auto

# PERFORMANCE EVALUATION

---

## Lecture: output\mpi3\page_014\mpi3_page_014\auto

# Elapsed parallel time

Returns the number of seconds that have elapsed since some time in the past.

double MP I_Wtime (void );

double start, finish; $=$ MPI_Wtime); $k$   
/\* Code to be timed \*/   
finish $=$ MPI_Wtime(; $=$

---

## Lecture: output\mpi3\page_015\mpi3_page_015\auto

# Elapsed serial time

• In this case, you don’t need to link in the MPI libraries. The POSIX library function gettimeofday returns time in microseconds elapsed from some point in the past.

• Pacheco book example code provides a GET_TIME macro, which records the number of seconds since some time in the past.

#include "timer.h" ı ı   
double now;   
  
GET_TIME(now);

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\mpi3\page_015\mpi3_page_015\auto\images\6c88ed6aa95eb53b96436b26b2e2d40b75a00edd864ac38f5c050dd271309905.jpg

---

## Lecture: output\mpi3\page_016\mpi3_page_016\auto

# Elapsed serial time

#include "timer.h" double start , finish; GET_TIME(start ); /\* Code to be timed \*/ GET_TIME(finish ); printf("Elapsed time

---

## Lecture: output\mpi3\page_017\mpi3_page_017\auto

# MPI_Barrier

• Ensures that no process will return from calling it until every process in the communicator has started calling it.

int MPI_Barrier(MPI_Comm Comm

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\mpi3\page_017\mpi3_page_017\auto\images\fbaf377670f2379e708102a102932eba7fed14e6fc1f1276f55f014480d3d852.jpg

---

## Lecture: output\mpi3\page_018\mpi3_page_018\auto

# MPI_Barrier

double local_start , local_finish, local_elapsed, elapsed;

/\* Code to be timed \*/

MPI_Reduce(&local_elapsed , &elapsed , 1, MPI_DouBLE ,

---

## Lecture: output\mpi3\page_019\mpi3_page_019\auto

# Run-times of serial and parallel matrixvector multiplication

<table><tr><td rowspan=2 colspan=1>comm.sZ</td><td rowspan=1 colspan=5>Order of Matrix</td></tr><tr><td rowspan=1 colspan=1>1024</td><td rowspan=1 colspan=1>2048</td><td rowspan=1 colspan=1>4096</td><td rowspan=1 colspan=1>8192</td><td rowspan=1 colspan=1>16,384</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>4.1</td><td rowspan=1 colspan=1>16.0</td><td rowspan=1 colspan=1>64.0</td><td rowspan=1 colspan=1>270</td><td rowspan=1 colspan=1>1100</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>2.3</td><td rowspan=1 colspan=1>8.5</td><td rowspan=1 colspan=1>33.0</td><td rowspan=1 colspan=1>140</td><td rowspan=1 colspan=1>560</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>2.0</td><td rowspan=1 colspan=1>5.1</td><td rowspan=1 colspan=1>18.0</td><td rowspan=1 colspan=1>70</td><td rowspan=1 colspan=1>280</td></tr><tr><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1>1.7</td><td rowspan=1 colspan=1>3.3</td><td rowspan=1 colspan=1>9.8</td><td rowspan=1 colspan=1>36</td><td rowspan=1 colspan=1>140</td></tr><tr><td rowspan=1 colspan=1>16</td><td rowspan=1 colspan=1>1.7</td><td rowspan=1 colspan=1>2.6</td><td rowspan=1 colspan=1>5.9</td><td rowspan=1 colspan=1>19</td><td rowspan=1 colspan=1>71</td></tr></table>

(Seconds)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\mpi3\page_019\mpi3_page_019\auto\images\febec1eb0ca41865a9106cc27fa5606eed920bf731fb89880553f2ffcd48ffc4.jpg

---

## Lecture: output\mpi3\page_020\mpi3_page_020\auto

# Speedups of Parallel Matrix-Vector Multiplication

<table><tr><td rowspan=2 colspan=1>comm_SZ</td><td rowspan=1 colspan=5>Order of Matrix</td></tr><tr><td rowspan=1 colspan=1>1024</td><td rowspan=1 colspan=1>2048</td><td rowspan=1 colspan=1>4096</td><td rowspan=1 colspan=1>8192</td><td rowspan=1 colspan=1>16,384</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1.0</td><td rowspan=1 colspan=1>1.0</td><td rowspan=1 colspan=1>1.0</td><td rowspan=1 colspan=1>1.0</td><td rowspan=1 colspan=1>1.0</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>1.8</td><td rowspan=1 colspan=1>1.9</td><td rowspan=1 colspan=1>1.9</td><td rowspan=1 colspan=1>1.9</td><td rowspan=1 colspan=1>2.0</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>2.1</td><td rowspan=1 colspan=1>3.1</td><td rowspan=1 colspan=1>3.6</td><td rowspan=1 colspan=1>3.9</td><td rowspan=1 colspan=1>3.9</td></tr><tr><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1>2.4</td><td rowspan=1 colspan=1>4.8</td><td rowspan=1 colspan=1>6.5</td><td rowspan=1 colspan=1>7.5</td><td rowspan=1 colspan=1>7.9</td></tr><tr><td rowspan=1 colspan=1>16</td><td rowspan=1 colspan=1>2.4</td><td rowspan=1 colspan=1>6.2</td><td rowspan=1 colspan=1>10.8</td><td rowspan=1 colspan=1>14.2</td><td rowspan=1 colspan=1>15.5</td></tr></table>

$$
S ( n , p ) = { \frac { T _ { \mathrm { S e r i a l } } ( n ) } { T _ { \mathrm { p a r a l l e l } } ( n , p ) } }
$$

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\mpi3\page_020\mpi3_page_020\auto\images\147216d6ff3689ab343e8e8a060e9f66553d29e58bd2f72c0acf966825d549a4.jpg
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\mpi3\page_020\mpi3_page_020\auto\images\8fc3e68b6c10d8d7240b08b3bacb438d27b700923e10e9837a4df35d86d28719.jpg

---

## Lecture: output\mpi3\page_021\mpi3_page_021\auto

# Efficiencies of Parallel Matrix-Vector Multiplication

<table><tr><td rowspan=2 colspan=1>comm.sZ</td><td rowspan=1 colspan=5>Order of Matrix</td></tr><tr><td rowspan=1 colspan=1>1024</td><td rowspan=1 colspan=1>2048</td><td rowspan=1 colspan=1>4096</td><td rowspan=1 colspan=1>8192</td><td rowspan=1 colspan=1>16,384</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1.00</td><td rowspan=1 colspan=1>1.00</td><td rowspan=1 colspan=1>1.00</td><td rowspan=1 colspan=1>1.00</td><td rowspan=1 colspan=1>1.00</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>0.89</td><td rowspan=1 colspan=1>0.94</td><td rowspan=1 colspan=1>0.97</td><td rowspan=1 colspan=1>0.96</td><td rowspan=1 colspan=1>0.98</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>0.51</td><td rowspan=1 colspan=1>0.78</td><td rowspan=1 colspan=1>0.89</td><td rowspan=1 colspan=1>0.96</td><td rowspan=1 colspan=1>0.98</td></tr><tr><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1>0.30</td><td rowspan=1 colspan=1>0.61</td><td rowspan=1 colspan=1>0.82</td><td rowspan=1 colspan=1>0.94</td><td rowspan=1 colspan=1>0.98</td></tr><tr><td rowspan=1 colspan=1>16</td><td rowspan=1 colspan=1>0.15</td><td rowspan=1 colspan=1>0.39</td><td rowspan=1 colspan=1>0.68</td><td rowspan=1 colspan=1>0.89</td><td rowspan=1 colspan=1>0.97</td></tr></table>

E( $n , p ) = { \frac { S ( n , p ) } { p } } = { \frac { T _ { \mathrm { S e r i a } } } { p \times T _ { \mathrm { p a r a } } } }$ 1(n) e1(n, p)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\mpi3\page_021\mpi3_page_021\auto\images\8cc32723a4f208896e2202e4e001a5e385f86d8c4ab8acfb28af6eb209dc9ca7.jpg
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\mpi3\page_021\mpi3_page_021\auto\images\8f9643c402ce25bc316cf39e201661addaa82824adb2720ad83a26db28b4bea7.jpg

---

## Lecture: output\mpi3\page_022\mpi3_page_022\auto

# A PARALLEL SORTING ALGORITHM

---

## Lecture: output\mpi3\page_023\mpi3_page_023\auto

# Sorting

n keys and p = # processes.

n/p keys assigned to each process.

• No restrictions on which keys are assigned to which processes.

• When the algorithm terminates:

– The keys assigned to each process should be sorted in order (we will use increasing order in the example).

– If $0 \leq \mathsf { q } < \mathsf { r } < \mathsf { p } ,$ , then each key assigned to process q should be less than or equal to every key assigned to process r.

---

## Lecture: output\mpi3\page_024\mpi3_page_024\auto

# Serial bubble sort

void Bubble_sort(

int aⅡint n

a[i] = a[i+1];

} /\* Bubble_sort \*/

![](images/c89cf590b6427c61abef99b1d6fc1c50422d1f0360bd80b89cdd6181ea82aa64.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\mpi3\page_024\mpi3_page_024\auto\images\c89cf590b6427c61abef99b1d6fc1c50422d1f0360bd80b89cdd6181ea82aa64.jpg

---

## Lecture: output\mpi3\page_025\mpi3_page_025\auto

Odd-even transposition sort

• A sequence of phases.

• Even phases, compare swaps:

$$
( a [ 0 ] , a [ 1 ] ) , ( a [ 2 ] , a [ 3 ] ) , ( a [ 4 ] , a [ 5 ] ) , . .
$$

• Odd phases, compare swaps:

$$
a [ 1 ] , a [ 2 ] ) , ( a [ 3 ] , a [ 4 ] ) , ( a [ 5 ] , a [ 6 ] ) , . .
$$

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\mpi3\page_025\mpi3_page_025\auto\images\0c64ae3affa49a4eca8f64d48b236aca42e17a6d5998ff700bd16c8a598f9fd1.jpg
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\mpi3\page_025\mpi3_page_025\auto\images\68ecb27658ddb5f1e117a4aa7dd0415abcf748ac284a2ead57aab0dcd8e1064e.jpg

---

## Lecture: output\mpi3\page_026\mpi3_page_026\auto

# Example

Start: 5, 9, 4, 3

Even phase: compare-swap (5,9) and (4,3) getting the list 5, 9, 3, 4   
Odd phase: compare-swap (9,3) getting the list 5, 3, 9, 4   
Even phase: compare-swap (5,3) and (9,4) getting the list 3, 5, 4, 9   
Odd phase: compare-swap (5,4) getting the list 3, 4, 5, 9

---

## Lecture: output\mpi3\page_027\mpi3_page_027\auto

# Serial odd-even transposition sort

void odd_even_sort( int a[] /\* in/out \*/,

int n for (phase $\begin{array}{c} \begin{array} { r l } & { \quad = \quad 0 ; \ \operatorname { p h a s e } < \ n ; \ \operatorname { p h a s e } + \ n ; } \\ & { \quad \le \ \operatorname { s e } \ \varphi _ { \varphi } \ 2 = \ 0 ; \quad \Big \{ \begin{array} { l } { \gamma + \ \ \xi \operatorname { E v e n } } \\ { \cdot \ \operatorname { E v e n } } \end{array} \ , \ D _ { \varphi } , \ \operatorname { p h a s e } \ \rho _ { \varphi } } \\ & { \quad \textrm { i } \ = \ 1 ; \ \textrm { i } < \ n ; \ \textrm { i } + \ 2 \ \textrm { p } } \\ & { \quad \textrm { f } \ ( \textrm { a l l } - 1 ) \ > \ \alpha [ \textrm { l i l } ] \ ; } \\ & { \quad \textrm { c e l p } = \ \alpha [ 1 ] \ < \ n ; \ | \ \textrm { i } \ \cdot | } \\ & { \quad \textrm { a l l i } - \ 1 } \end{array} \  \\ & { \quad \quad \textrm { a l l i } \ \textrm { i } - \ \tan { \ \ y s } ; } \\ & { \quad \quad \textrm { a l l i } - \ 1 } \\ & { \quad \quad \textrm { f } \ \cdot \ \textrm { o d d } \ p h a s e \ \textrm { s e } ^ { \prime } } \\ & { \quad \quad \textrm { ( i } \ = \ 1 \ ; \ \textrm { i } < \ n - 1 ; \ \textrm { i } + \ 2 \ \textrm { ) } } \\ & { \quad \textrm { f } \ \textrm { o } \ [ \textrm { i } \ > \ \textrm { s e l p } ] \ \textrm { ( a l l ) } \ \textrm { ( } } \\ & { \quad \textrm { c e l p } = \ \textrm { a l l i } ] \ . } \\ & { \quad \textrm { a l l i } + 1 + \ \tan { \ \ y s } . } \end{array}$ )d) if (pha hase \*/ for i $\}$ else for i } } /\* Odd_even_sort \*/

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\mpi3\page_027\mpi3_page_027\auto\images\fd33109e6d9e1aafa2866ebf124d03c337a3d9deeee976aef580adca53a3549a.jpg

---

## Lecture: output\mpi3\page_028\mpi3_page_028\auto

# Communications among tasks in oddeven sort

![](images/cb7f79d3df03d2db88f1f010a4586c9b2a7aaffe52636571f2c89c3f19507c52.jpg)  
Tasks determining a[i] are labeled with a[i].

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\mpi3\page_028\mpi3_page_028\auto\images\cb7f79d3df03d2db88f1f010a4586c9b2a7aaffe52636571f2c89c3f19507c52.jpg

---

## Lecture: output\mpi3\page_029\mpi3_page_029\auto

# Parallel odd-even transposition sort

<table><tr><td rowspan=2 colspan=1>Time</td><td rowspan=1 colspan=4>Process</td></tr><tr><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>3</td></tr><tr><td rowspan=1 colspan=1>Start</td><td rowspan=1 colspan=1>15, 11, 9, 16</td><td rowspan=1 colspan=1>3, 14, 8, 7</td><td rowspan=1 colspan=1>4, 6, 12, 10</td><td rowspan=1 colspan=1>5, 2, 13, 1</td></tr><tr><td rowspan=1 colspan=1>After Local Sort</td><td rowspan=1 colspan=1>9, 11, 15, 16</td><td rowspan=1 colspan=1>3, 7, 8, 14</td><td rowspan=1 colspan=1>4, 6, 10, 12</td><td rowspan=1 colspan=1>1, 2, 5, 13</td></tr><tr><td rowspan=1 colspan=1>After Phase 0</td><td rowspan=1 colspan=1>3,7, 8,9</td><td rowspan=1 colspan=1>11, 14, 15, 16</td><td rowspan=1 colspan=1>1,2,4,5</td><td rowspan=1 colspan=1>6, 10, 12, 13</td></tr><tr><td rowspan=1 colspan=1>After Phase 1</td><td rowspan=1 colspan=1>3,7, 8,9</td><td rowspan=1 colspan=1>1,2,4,5</td><td rowspan=1 colspan=1>11, 14, 15, 16</td><td rowspan=1 colspan=1>6, 10, 12, 13</td></tr><tr><td rowspan=1 colspan=1>After Phase 2</td><td rowspan=1 colspan=1>1,2,3,4</td><td rowspan=1 colspan=1>5, 7,8,9</td><td rowspan=1 colspan=1>6, 10, 11, 12</td><td rowspan=1 colspan=1>13, 14, 15, 16</td></tr><tr><td rowspan=1 colspan=1>After Phase 3</td><td rowspan=1 colspan=1>1, 2,3,4</td><td rowspan=1 colspan=1>5,6, 7, 8</td><td rowspan=1 colspan=1>9, 10, 11, 12</td><td rowspan=1 colspan=1>13, 14, 15, 16</td></tr></table>

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\mpi3\page_029\mpi3_page_029\auto\images\21b146ae68b92f4addb97c0c194563d7f49c11cc6eb4839304cdaed33c569c55.jpg

---

## Lecture: output\mpi3\page_030\mpi3_page_030\auto

# Pseudo-code

---

## Lecture: output\mpi3\page_031\mpi3_page_031\auto

# Compute_partner

if (phase % 2 == 0) /= Even phase \*/ if $\begin{array} { r c l } { { \mathrm { s e } } } & { { { \bf \bar { \alpha } } ^ { \prime } \ { \bf \bar { \alpha } } ^ { \prime } \ - \ { \bf \bar { \alpha } } ^ { \prime } \ { \bf \gamma } ^ { \prime } } } & { { { \bf \gamma } ^ { \prime } \ \cdot \stackrel { \bar { \alpha } } { \bf \gamma } ^ { \prime } \ \stackrel { \bar { \beta } \bar { \alpha } } } } & { { { \bf \bar \gamma } ^ { \prime } \cdot \ { \bf \sigma } \ { \bf \bar { \alpha } } ^ { \prime } \ { \bf \bar { \alpha } } ^ { \prime } \ } } \\ { { \mathrm { m i t y . \bar { \alpha } } ^ { \prime } \ \mathrm { z a n k } \ \ll \ { \bf \bar { \alpha } } ^ { \prime } \ { \bf \gamma } ^ { \prime } \ \mathrm { \bf \bar { \alpha } } ^ { \prime } \ \mathrm { \bf \bar { \alpha } } ^ { \prime } \ \mathrm { \bf \bar { \alpha } } ^ { \prime } \ \ \mathrm { \bf \bar { \alpha } } ^ { \prime } \ } } & { { \bf \gamma } ^ { \prime } \mathrm { \bf \bar { \alpha } } \cdot { \bf \sigma } \ { \bf \bar { \alpha } } \mathrm { d } { \bf \alpha } } \\ { { \mathrm { s t r a g . } \ \ \mathrm { \bar { \alpha } } } } & { { \bf \gamma } ^ { \prime } \ } & { { \bf \gamma } ^ { \prime } \mathrm { \bf \bar { \alpha } } \ } \\ { { \mathrm { s t r a g . } \ \ \mathrm { \bar { \alpha } } } } & { { \bf \gamma } ^ { \prime } \ - \bf \gamma } ^ { \prime } \ { \bf \alpha } \mathrm { \bar { \alpha } } \mathrm { \bf \bar { \alpha } } \mathrm { \bf \bar { \beta } } \mathrm { \bf \bar { \alpha } } ^ { \prime } \ + { \bf \gamma } \mathrm { \bf \alpha } \mathrm { \bf \bar { \alpha } } \mathrm { \bf \bar { \beta } } \mathrm { \bf \bar { \alpha } } \mathrm { \bf \bar { \beta } } \mathrm { \bf \bar { \alpha } } \mathrm { \bf \bar { \beta } } \mathrm  \bf \bar  \alpha \end{array}$ l rank \*/ else n rank \*/   
else if( l rank \*/ else n rank \*/ r   
if (par m_s z ) partner = MPI_PRoC_NuLL;

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\mpi3\page_031\mpi3_page_031\auto\images\eb61b10addcc73fd61ae642102014823dd46f82b5b874753a8714bb53b8c9353.jpg

---

## Lecture: output\mpi3\page_032\mpi3_page_032\auto

# Safety in MPI programs

• The MPI standard allows MPI_Send to behave in two different ways: – it can simply copy the message into an MPI managed buffer and return, – or it can block until the matching call to MPI_Recv starts.

---

## Lecture: output\mpi3\page_033\mpi3_page_033\auto

# Safety in MPI programs

• Many implementations of MPI set a threshold at which the system switches from buffering to blocking.

• Relatively small messages will be buffered by MPI_Send.

• Larger messages, will cause it to block.

---

## Lecture: output\mpi3\page_034\mpi3_page_034\auto

# Safety in MPI programs

• If the MPI_Send executed by each process blocks, no process will be able to start executing a call to MPI_Recv, and the program will hang or deadlock.

• Each process is blocked waiting for an event that will never happen.

---

## Lecture: output\mpi3\page_035\mpi3_page_035\auto

# Safety in MPI programs

• A program that relies on MPI provided buffering is said to be unsafe.

• Such a program may run without problems for various sets of input, but it may hang or crash with other sets.

---

## Lecture: output\mpi3\page_036\mpi3_page_036\auto

# MPI_Ssend

• An alternative to MPI_Send defined by the MPI standard.

• The extra “s” stands for synchronous and MPI_Ssend is guaranteed to block until the matching receive starts.

int MPI_Ssend( void\* msg_buf_p $\begin{array} { r l } { \mathrm { \ d ~ \nearrow ~ } i n } & { \ast \big / \mathrm { \ d ~ , } } \\ { \mathrm { \ d ~ \nearrow ~ } i n } & { \ast \big / \mathrm { \ d ~ , } } \\ { \mathrm { \ d ~ \nearrow ~ } i n } & { \ast \big / \mathrm { \ d ~ , } } \\ { \mathrm { \ d ~ \nearrow ~ } i n } & { \ast \big / \mathrm { \ d ~ , } } \\ { \mathrm { \ d ~ \nearrow ~ } i n } & { \ast \big / \mathrm { \ d ~ , } } \\ { \mathrm { \ d ~ \nearrow ~ } i n } & { \ast \big / \mathrm { \ d ~ , } } \end{array}$ int msg_size MPI_Datatype msg_type int int MPI_Comm communicator

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\mpi3\page_036\mpi3_page_036\auto\images\4f71fc82a506435edc87b9bf977823eac1d730db5d3b47d0a557092c43f478b7.jpg

---

## Lecture: output\mpi3\page_037\mpi3_page_037\auto

# Restructuring communication

$\%$ $\%$ 0, COmm , MPI_STATUS_IGNORE .

![](images/37fc861546de0f2538e9a0f7216dac59beb47abd922ec39b40c88444fdf06050.jpg)

if (my_rank $\%$ $2 \ = - \ 0$ $\%$ $\%$   
$\}$ else{0， Comm, MPI_STATUS_IGNORE.$\%$

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\mpi3\page_037\mpi3_page_037\auto\images\37fc861546de0f2538e9a0f7216dac59beb47abd922ec39b40c88444fdf06050.jpg

---

## Lecture: output\mpi3\page_038\mpi3_page_038\auto

# Safe communication with five processes

![](images/eaeeb761ab290eb61563e6757ab9e210e74dd9868690f86043537965584f4e1d.jpg)  
Time 0

![](images/2fcdac595298b00c66ee129ff7a6b7ff2d7ffc911724458dc03dd2e5e76bb6e5.jpg)  
Time 1

![](images/396f24f202df0f1a72464c075ea57994837c990bff25adb49b62023732789d81.jpg)  
Time 2

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\mpi3\page_038\mpi3_page_038\auto\images\2fcdac595298b00c66ee129ff7a6b7ff2d7ffc911724458dc03dd2e5e76bb6e5.jpg
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\mpi3\page_038\mpi3_page_038\auto\images\396f24f202df0f1a72464c075ea57994837c990bff25adb49b62023732789d81.jpg
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\mpi3\page_038\mpi3_page_038\auto\images\eaeeb761ab290eb61563e6757ab9e210e74dd9868690f86043537965584f4e1d.jpg

---

## Lecture: output\mpi3\page_039\mpi3_page_039\auto

# MPI_Sendrecv

• An alternative to scheduling the communications by ourselves.

• Carries out a blocking send and a receive in a single call.

• The destination and the source can be the same or different.

• Especially useful because MPI schedules the communications so that the program won’t hang or crash.

---

## Lecture: output\mpi3\page_040\mpi3_page_040\auto

# MPI_Sendrecv

int MPI_Sendrecv(

void\* send_buf_p in int send_buf_size /\* in MPI_Datatype send_buf_type /\* in int dest /\* in int send_tag /\* in void\* recv_buf_p /\* out \*/, int recv_buf_size /\* in MPI_Datatype recv_buf_type /\* in int source in int recv_tag in MPI_Comm communicator /\* in MPI_Status \* status_p /\* in

---

## Lecture: output\mpi3\page_041\mpi3_page_041\auto

# Parallel odd-even transposition sort

void Me i $\begin{array}{c} \begin{array} { l l l l l } { { \mathrm { r g e \_ l o w } (  } } & { { } } & { { } } & { { } } & { { } } \\ { { \mathrm { { \scriptsize ~ n t \_ } } } } & { { \mathrm { { \scriptsize ~ m y \_ k e y s [ ] ~ , } } } } & { { } } & { { } } & { { / * i n / o u t } } \\ { { \mathrm { { \scriptsize ~ n t \_ } } } } & { { \mathrm { { \scriptsize ~ r e c v \_ k e y s [ ] ~ , } } } } & { { } } & { { / * i n } } & { { * / } } \\ { { \mathrm { { \scriptsize ~ n t \_ } } } } & { { \mathrm { { \scriptsize ~ t e m p \_ k e y s [ ] ~ , } } } } & { { } } & { { / * s c r a t c h } } & { { * / } } \\ { { \mathrm { { \scriptsize ~ n t \_ } } } } & { { { \mathrm { \scriptsize ~ l \circ c a l \_ n r } } } } & { { \mathrm { { \scriptsize ~ \{ ~  ~ , } ~ } } }  & { { } } & { { / * =   { n / p , \begin{array} { l l l } { { \mathrm { { \scriptsize ~ { \scriptsize ~ { \it ~ i n } ~ } } } } } & { { * / } } \end{array} }  } } \\ { { \mathrm { { \scriptsize ~ m \_ i ~ , ~ \_ \tau . ~ \ i ~ , ~ \tau \_ { \tau } ~ { \ t \_ } } ~ } } } & { { } } & { { } } & { { } } \end{array} \{ \begin{array} { l l } { { } } & { { } } & { { } } \\ { { \mathrm { { \scriptsize ~  ~ c \_ i ~  } ~ } } } & { { } } & { { } } & { { } } \end{array} |   \end{array}$ i   
i   
i   
int   
$\mathfrak { m } _ { - } \dot { \mathrm { ~ i ~ } } = \mathfrak { r } _ { - } \dot { \mathrm { ~ i ~ } } = \dot { \mathrm { ~ t ~ } } _ { - } \dot { \mathrm { ~ i ~ } } = 0$   
while (t_i < local_n) {   
temp_keys [t_i ] = my_keys [m_i ];   
$\}$ else{   
}   
for $( \mathrm { ~ m ~ \_ ~ i ~ } = \mathrm { ~ 0 ~ }$   
my_keys [m_i ] = temp_keys [m_i ];   
$\}$ /\* Merge_low \*/

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\mpi3\page_041\mpi3_page_041\auto\images\87e16f819d696c67c1d951ce95571b7ad544b4a7fa2eff12bd590c2346ce787c.jpg

---

## Lecture: output\mpi3\page_042\mpi3_page_042\auto

# Run-time of parallel odd-even sort

<table><tr><td rowspan=2 colspan=1>Processes</td><td rowspan=1 colspan=5>Number of Keyss (in thousands)</td></tr><tr><td rowspan=1 colspan=1>200</td><td rowspan=1 colspan=1>400</td><td rowspan=1 colspan=1>800</td><td rowspan=1 colspan=1>1600</td><td rowspan=1 colspan=1>3200</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>88</td><td rowspan=1 colspan=1>190</td><td rowspan=1 colspan=1>390</td><td rowspan=1 colspan=1>830</td><td rowspan=1 colspan=1>1800</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>43</td><td rowspan=1 colspan=1>91</td><td rowspan=1 colspan=1>190</td><td rowspan=1 colspan=1>410</td><td rowspan=1 colspan=1>860</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>22</td><td rowspan=1 colspan=1>46</td><td rowspan=1 colspan=1>96</td><td rowspan=1 colspan=1>200</td><td rowspan=1 colspan=1>430</td></tr><tr><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1>12</td><td rowspan=1 colspan=1>24</td><td rowspan=1 colspan=1>51</td><td rowspan=1 colspan=1>110</td><td rowspan=1 colspan=1>220</td></tr><tr><td rowspan=1 colspan=1>16</td><td rowspan=1 colspan=1>7.5</td><td rowspan=1 colspan=1>14</td><td rowspan=1 colspan=1>29</td><td rowspan=1 colspan=1>60</td><td rowspan=1 colspan=1>130</td></tr></table>

(time is in milliseconds)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\mpi3\page_042\mpi3_page_042\auto\images\f19c31f63b8e3896e180b37af4c4719f67a9472816b7467a547c5975ec763a23.jpg

---

## Lecture: output\mpi3\page_043\mpi3_page_043\auto

# Concluding Remarks (1)

• MPI or the Message-Passing Interface is a library of functions that can be called from C, C++, or Fortran programs.

• A communicator is a collection of processes that can send messages to each other.

Many parallel programs use the singleprogram multiple data or SPMD approach.

---

## Lecture: output\mpi3\page_044\mpi3_page_044\auto

# Concluding Remarks (2)

• Most serial programs are deterministic: if we run the same program with the same input we’ll get the same output.

• Parallel programs often don’t possess this property.

• Collective communications involve all the processes in a communicator.

---

## Lecture: output\mpi3\page_045\mpi3_page_045\auto

# Concluding Remarks (3)

• When we time parallel programs, we’re usually interested in elapsed time or “wall clock time”.

• Speedup is the ratio of the serial run-time to the parallel run-time.

• Efficiency is the speedup divided by the number of parallel processes.

---

## Lecture: output\mpi3\page_046\mpi3_page_046\auto

# Concluding Remarks (4)

A parallel program is said to be strongly scalable if its efficiency can be kept constant with increase in number of processors; it is weakly scalable if its efficiency can be kept constant with both increase in number of processors and problem size at the same rate • An MPI program is unsafe if its correct behavior depends on the fact that MPI_Send is buffering its input.

---

## Lecture: output\nbodyMPI\page_001\nbodyMPI_page_001\auto

# Parallel Programming

Parallel N-Body Solvers on the CPU

---

## Lecture: output\nbodyMPI\page_002\nbodyMPI_page_002\auto

# Parallelizing the Basic Solver Using MPI

• Choices with respect to the data structures: – Each process stores the entire global array of particle masses. – Each process only uses a single n-element array for the positions. – Each process uses a pointer loc_pos that refers to the start of its block of pos. – So on process 0 local_pos = pos; on process 1 local_pos = pos + loc_n; and so on.

---

## Lecture: output\nbodyMPI\page_003\nbodyMPI_page_003\auto

# Pseudo-code for the MPI version of the basic nbody solver

for each timestep { if (timestep output)

---

## Lecture: output\nbodyMPI\page_004\nbodyMPI_page_004\auto

# Pseudo-code for output

if (my_r $\begin{array} { l } { \tt { \tt \tt { 2 1 0 c i t i e s ~ o n t o ~ p r o c e s s ~ 0 } ; } } \\ { \tt { \tt { u n k ~ \tt { = } = ~ 0 } ) ~ \Big \{ ~ \tt { 1 } ~ } } \\ { \tt { \tt { t i m e s t e p } ; } } \\ { \tt { \tt { i c h ~ p a r t i c l e } } } \\ { \tt { \tt { \tt { \tt { 1 } t ~ \tt { p o s } [ \tt { p a r t i c l e } ] ~ \tt { a n d ~ v e l } [ \tt { p a r t } ] } } } } \end{array}$ for ea cticle]

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\nbodyMPI\page_004\nbodyMPI_page_004\auto\images\51ab61597b9d18790cefe8df54b1843f7467d75e1cc8b222e96162e17e8e1876.jpg

---

## Lecture: output\nbodyMPI\page_005\nbodyMPI_page_005\auto

# Communication In A Possible MPI Implementation of the N-Body Solver (for a reduced solver)

![](images/558a711dbcc00460773912aeab5d2dcf8f37dc9aaeb46ab393108a6f860d67e8.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\nbodyMPI\page_005\nbodyMPI_page_005\auto\images\558a711dbcc00460773912aeab5d2dcf8f37dc9aaeb46ab393108a6f860d67e8.jpg

---

## Lecture: output\nbodyMPI\page_006\nbodyMPI_page_006\auto

# A Ring of Processes

![](images/85c0b0634d0a5175b72732e51e3b072b001bbe9155a9ff2e2cf071056088899b.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\nbodyMPI\page_006\nbodyMPI_page_006\auto\images\85c0b0634d0a5175b72732e51e3b072b001bbe9155a9ff2e2cf071056088899b.jpg

---

## Lecture: output\nbodyMPI\page_007\nbodyMPI_page_007\auto

# Ring Pass of Positions

![](images/73fd3a21a8de8dc1c050b06854d14655739d70267c6e93ab13a76fec319f2086.jpg)  
Phase 2   
Phase 3

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\nbodyMPI\page_007\nbodyMPI_page_007\auto\images\73fd3a21a8de8dc1c050b06854d14655739d70267c6e93ab13a76fec319f2086.jpg

---

## Lecture: output\nbodyMPI\page_008\nbodyMPI_page_008\auto

# Computation of Forces in Ring Pass (1)

<table><tr><td rowspan=1 colspan=1>Time</td><td rowspan=1 colspan=1>Variable</td><td rowspan=1 colspan=1>Process 0</td><td rowspan=1 colspan=1>Process 1</td></tr><tr><td rowspan=2 colspan=1>Start</td><td rowspan=2 colspan=1>loc_posloc_forcestmp-postmp_forces</td><td rowspan=1 colspan=1>S0,S2</td><td rowspan=2 colspan=1>S1,S30,0S1,S30,0</td></tr><tr><td rowspan=1 colspan=1>0,0S0,S20,0</td></tr><tr><td rowspan=2 colspan=1>AfterComp ofForces</td><td rowspan=2 colspan=1>loc_posloc_forcestmp-postmp_forces</td><td rowspan=1 colspan=1>S0,S2</td><td rowspan=2 colspan=1>S1,S3f13,0S1,S30, -f13</td></tr><tr><td rowspan=1 colspan=1>f02, 0S0,S20, -f02</td></tr><tr><td rowspan=1 colspan=1>AfterFirstComm</td><td rowspan=1 colspan=1>loc_posloc_forcestmp-postmp_forces</td><td rowspan=1 colspan=1>S0,S2f02,0S1,S30, -f13</td><td rowspan=1 colspan=1>S1,$3f13,0S0,S20, -f02</td></tr><tr><td rowspan=2 colspan=1>AfterComp ofForces</td><td rowspan=2 colspan=1>loc_posloc_forcestmp-postmp_forces</td><td rowspan=1 colspan=1>S0,$2f01 + f02 + f03, f23</td><td rowspan=2 colspan=1>S1,S3f12 + f13, 0S0,S20,−f02 -f12</td></tr><tr><td rowspan=1 colspan=1>S1,S3−f01, −f03 −f13 −f23</td></tr></table>

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\nbodyMPI\page_008\nbodyMPI_page_008\auto\images\e9e747d1a93c65aa67ec519565df19fc09d2c76c59b3a95900ca61c6920b758e.jpg

---

## Lecture: output\nbodyMPI\page_009\nbodyMPI_page_009\auto

# Computation of Forces in Ring Pass (2)

<table><tr><td rowspan=1 colspan=1>Time</td><td rowspan=1 colspan=1>Variable</td><td rowspan=1 colspan=1>Process 0</td><td rowspan=1 colspan=1>Process 1</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td></td><td></td></tr><tr><td rowspan=1 colspan=1>AfterSecondComm</td><td rowspan=1 colspan=1>loc_posloc_forcestmp-postmp_forces</td><td rowspan=1 colspan=1>S0,S2f01 + f02 + f03 , f23S0,S20, −f02-f12</td><td rowspan=1 colspan=1>S1,S3f12 + f13, 0S1,S3−f01, −f03 − f13 −f23</td></tr><tr><td rowspan=2 colspan=1>AfterComp ofForces</td><td rowspan=2 colspan=1>loc_posloc_forcestmp-postmp_forces</td><td rowspan=1 colspan=1>S0,S2f01 + f02 + f03, −f02 − f12 + f23</td><td rowspan=2 colspan=1>S1,S3−f01 + f12 + f13, −f03 − f13 − f23S1,S3−f01, −f03 − f13 − f23</td></tr><tr><td rowspan=1 colspan=1>S0,S20, −f02− f12</td></tr></table>

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\nbodyMPI\page_009\nbodyMPI_page_009\auto\images\8918dfb42619e45e1eeb6e63416089deba40e92660a5150f97ef8ab26b97a26f.jpg

---

## Lecture: output\nbodyMPI\page_010\nbodyMPI_page_010\auto

# Pseudo-code for the MPI implementation of the reduced n-body solver

$\%$ $=$ $=$

for (phase = l; phase < comm_sz ; phase++) { /\*Owner $o f$ the positions and forces we're receiving \*/ $=$ $\%$

---

## Lecture: output\nbodyMPI\page_011\nbodyMPI_page_011\auto

# Loops iterating through global particle indexes

$+ =$

---

## Lecture: output\nbodyMPI\page_012\nbodyMPI_page_012\auto

# Performance of the MPI n-body solvers

$$
\frac { \mathrm { P r o c e s s e s \ | | \ B a s i c \ | \ R e d u c e d } } { \frac { 1 } { 2 } } \frac { | | 1 7 . 3 0 | \ 8 . 6 8 } { | \begin{array} { l l l } { 8 . 6 5 } & { 4 . 4 5 } \\ { 4 . 3 5 } & { 2 . 3 0 } \\ { 8 } & { | \begin{array} { l l l } { 2 . 2 0 } & { 1 . 2 6 } \\ { 1 . 1 3 } & { 0 . 7 8 } \end{array} | } } \end{array}
$$

(in seconds)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\nbodyMPI\page_012\nbodyMPI_page_012\auto\images\f1e7fa7856f389fab503b5cdedf855038130d630f9cc93407e7e98e3533b01e6.jpg

---

## Lecture: output\nbodyMPI\page_013\nbodyMPI_page_013\auto

# Run-Times for OpenMP and MPI N-Body Solvers

<table><tr><td rowspan=2 colspan=1>Processes/Threads</td><td rowspan=1 colspan=2>OpenMP</td><td rowspan=1 colspan=2>MPI</td></tr><tr><td rowspan=1 colspan=1>Basic</td><td rowspan=1 colspan=1>Reduced</td><td rowspan=1 colspan=1>Basic</td><td rowspan=1 colspan=1>Reduced</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>15.13</td><td rowspan=1 colspan=1>8.77</td><td rowspan=1 colspan=1>17.30</td><td rowspan=1 colspan=1>8.68</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>7.62</td><td rowspan=1 colspan=1>4.42</td><td rowspan=1 colspan=1>8.65</td><td rowspan=1 colspan=1>4.45</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>3.85</td><td rowspan=1 colspan=1>2.26</td><td rowspan=1 colspan=1>4.35</td><td rowspan=1 colspan=1>2.30</td></tr></table>

(in seconds)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\nbodyMPI\page_013\nbodyMPI_page_013\auto\images\95170886ad8735f33dccc70cafbeb20e64174f1c87aa0ea073e1401159dd6584.jpg

---

## Lecture: output\nbodyMPI\page_014\nbodyMPI_page_014\auto

# Concluding Remarks (1)

• In developing the reduced MPI solution to the n-body problem, the “ring pass” algorithm proved to be much easier to implement and is probably more scalable.

• In a distributed memory environment in which processes send each other work, determining when to terminate is a nontrivial problem.

---

## Lecture: output\nbodyMPI\page_015\nbodyMPI_page_015\auto

# Concluding Remarks (2)

• When deciding which API to use, we should consider whether to use shared- or distributed-memory.

We should look at the memory requirements of the application and the amount of communication among the processes/threads.

---

## Lecture: output\nbodyMPI\page_016\nbodyMPI_page_016\auto

# Concluding Remarks (3)

• If the memory requirements are great or the distributed memory version can work mainly with cache, then a distributed memory program is likely to be much faster.

• On the other hand if there is considerable communication, a shared memory program will probably be faster.

---

## Lecture: output\nbodyOpenMP\page_001\nbodyOpenMP_page_001\auto

# Parallel Programming

Parallel N-Body Solvers on the CPU

---

## Lecture: output\nbodyOpenMP\page_002\nbodyOpenMP_page_002\auto

![](images/0d78285944af3800d97ca65cc429526da44b5243899c6ea925e26e679f65c455.jpg)

N-BODY SOLVERS

![](images/a8c3e255442b4de96de3987db4422dc0781471298c6b6fadbec8db8a9e8b31ca.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\nbodyOpenMP\page_002\nbodyOpenMP_page_002\auto\images\0d78285944af3800d97ca65cc429526da44b5243899c6ea925e26e679f65c455.jpg
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\nbodyOpenMP\page_002\nbodyOpenMP_page_002\auto\images\a8c3e255442b4de96de3987db4422dc0781471298c6b6fadbec8db8a9e8b31ca.jpg

---

## Lecture: output\nbodyOpenMP\page_003\nbodyOpenMP_page_003\auto

# The n-body problem

• Find the positions and velocities of a collection of interacting particles over a period of time.

• An n-body solver is a program that finds the solution to an n-body problem by simulating the behavior of the particles.

---

## Lecture: output\nbodyOpenMP\page_004\nbodyOpenMP_page_004\auto

![](images/ed453fc67f3fdf7c9b1ce9adf09ef9a4fa0b806fcb10526bfe1d62e4e354d57a.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\nbodyOpenMP\page_004\nbodyOpenMP_page_004\auto\images\ed453fc67f3fdf7c9b1ce9adf09ef9a4fa0b806fcb10526bfe1d62e4e354d57a.jpg

---

## Lecture: output\nbodyOpenMP\page_005\nbodyOpenMP_page_005\auto

# Simulating motion of planets

• Determine the positions and velocities: – Newton’s second law of motion. – Newton’s law of universal gravitation.

---

## Lecture: output\nbodyOpenMP\page_006\nbodyOpenMP_page_006\auto

# Forces

$$
\mathbf { \boldsymbol { \mathbf { \rho } } } _ { \ast } ( t ) = - \frac { G m _ { q } m _ { k } } {  \mathbf { \boldsymbol { s } } _ { q } ( t ) - \mathbf { \boldsymbol { s } } _ { k } ( t )  ^ { 3 } } [ \mathbf { \boldsymbol { s } } _ { q } ( t ) - \mathbf { \boldsymbol { s } } _ { }
$$

$$
= \sum _ { { k = 0 } \atop { k \ne q } } ^ { n - 1 } \mathbf { f } _ { q k } = - G m _ { q } \sum _ { { k = 0 } \atop { k \ne q } } ^ { n - 1 } { \frac { m _ { k } } { \left| \mathbf { s } _ { q } ( t ) - \mathbf { s } _ { k } \right. } }
$$

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\nbodyOpenMP\page_006\nbodyOpenMP_page_006\auto\images\2991bf771a53fc51f8f75fab25b9365a5f096919a70c1fb270c09d6db3aaf467.jpg
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\nbodyOpenMP\page_006\nbodyOpenMP_page_006\auto\images\6b5a4b03a951ec5be6228a3e28db59cebc17b709b7a2bf9dfa01464c9827f02e.jpg

---

## Lecture: output\nbodyOpenMP\page_007\nbodyOpenMP_page_007\auto

# Acceleration

${ \bf \omega } ^ { \prime } t ) = - G \sum _ { { j = 0 } \atop { j \ne q } } ^ { n - 1 } \frac { m _ { j } } { | { \bf s } _ { q } ( t ) - { \bf s } _ { j } ( t ) | ^ { 3 } } [ { \bf s } _ { q } ( t$

$$
t = 0 , \Delta t , 2 \Delta t , \ldots , T \Delta t
$$

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\nbodyOpenMP\page_007\nbodyOpenMP_page_007\auto\images\82c68bad85e3b3f3196a75182dc4648069c2e1c0355d91b89302cb1ab81dea27.jpg
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\nbodyOpenMP\page_007\nbodyOpenMP_page_007\auto\images\9b2ceb886244289da508c23629fdba5a37efba80f243292a36038eafbc4f4cc7.jpg

---

## Lecture: output\nbodyOpenMP\page_008\nbodyOpenMP_page_008\auto

# Serial pseudo-code

for each timestep $\{$ for each particle q

---

## Lecture: output\nbodyOpenMP\page_009\nbodyOpenMP_page_009\auto

# Computation of the forces

for each particle q { x_diff = pos [ql[x] − pos [k ][x ]; y_diff = pos [ql[y] − pos[k ][y ]; $=$ $=$ $] /$ $^ *$ forces [q]lY] —= G\*masses [q]\*masses [k $] /$ $^ *$   
}

---

## Lecture: output\nbodyOpenMP\page_010\nbodyOpenMP_page_010\auto

# A Reduced Algorithm for Computing NBody Forces

$[ \mathsf { q } ] ~ = ~ 0$ for each particle q { $=$ sqrt (x_diff\*x_diff + y_diff\*y_diff ); dist_cubed $=$ $] /$ $^ *$ force_qk [Y] = G\*masses [q]\*masses [k $] /$ $^ *$

forces [ql[x] += force_qk[x];   
forces[qly] += force_qk[y ];   
forces[k ][y] −= force_qk[y];

---

## Lecture: output\nbodyOpenMP\page_011\nbodyOpenMP_page_011\auto

# The individual forces

$\begin{array} { r } { { \left[ \begin{array} { l l l l l } { { \bf \Gamma } } & { 0 } & { { \bf f } _ { 0 1 } } & { { \bf f } _ { 0 2 } } & { \cdots . } \\ { - { \bf f } _ { 0 1 } } & { 0 } & { { \bf f } _ { 1 2 } } & { \cdots . } \\ { - { \bf f } _ { 0 2 } } & { - { \bf f } _ { 1 2 } } & { 0 } & { \cdots } \\ { ~ \vdots } & { ~ \vdots } & { ~ \vdots } & { \ddots } \\ { - { \bf f } _ { 0 , n - 1 } } & { - { \bf f } _ { 1 , n - 1 } } & { - { \bf f } _ { 2 , n - 1 } } & { \cdots } \end{array} \right] } } \end{array}$ f0,n−1   
f1,n−1   
f2,n−1

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\nbodyOpenMP\page_011\nbodyOpenMP_page_011\auto\images\65e2b71f07a48b0852ff930f550763b44db3b68faeb085a03e2630471a9bf72a.jpg

---

## Lecture: output\nbodyOpenMP\page_012\nbodyOpenMP_page_012\auto

# Using the Tangent Line to Approximate a Function

![](images/3f902211e17e2c508a06ce70fead5ad62092b33edba8031613191bf597f0f246.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\nbodyOpenMP\page_012\nbodyOpenMP_page_012\auto\images\3f902211e17e2c508a06ce70fead5ad62092b33edba8031613191bf597f0f246.jpg

---

## Lecture: output\nbodyOpenMP\page_013\nbodyOpenMP_page_013\auto

# Euler’s Method

![](images/5480622c7db0bf26c3eae9e0c2eae5b85eebdc38cd09765078f2b4b322b1d538.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\nbodyOpenMP\page_013\nbodyOpenMP_page_013\auto\images\5480622c7db0bf26c3eae9e0c2eae5b85eebdc38cd09765078f2b4b322b1d538.jpg

---

## Lecture: output\nbodyOpenMP\page_014\nbodyOpenMP_page_014\auto

# Parallelizing the N-Body Solvers

• Apply Foster’s methodology.   
Initially, we want a lot of tasks.   
Start by making our tasks the computations of the positions, the velocities, and the total forces at each timestep.

---

## Lecture: output\nbodyOpenMP\page_015\nbodyOpenMP_page_015\auto

# Communications Among Tasks in the Basic N-Body Solver

![](images/25a806246137121e70e6f989c2b11111455cfc85e74ae33e784f4ea95a834753.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\nbodyOpenMP\page_015\nbodyOpenMP_page_015\auto\images\25a806246137121e70e6f989c2b11111455cfc85e74ae33e784f4ea95a834753.jpg

---

## Lecture: output\nbodyOpenMP\page_016\nbodyOpenMP_page_016\auto

# Communications Among Agglomerated Tasks in the Basic N-Body Solver

![](images/8f0ad624dd3d62affcde9a46d4a990239d6bfb0aed65977cfb6ddb7c051c7263.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\nbodyOpenMP\page_016\nbodyOpenMP_page_016\auto\images\8f0ad624dd3d62affcde9a46d4a990239d6bfb0aed65977cfb6ddb7c051c7263.jpg

---

## Lecture: output\nbodyOpenMP\page_017\nbodyOpenMP_page_017\auto

# Communications Among Agglomerated Tasks in the Reduced N-Body Solver

![](images/d6a0a2ea037a68c01ff656d0f289b3555ec65140ff9371e3d574278586f65f25.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\nbodyOpenMP\page_017\nbodyOpenMP_page_017\auto\images\d6a0a2ea037a68c01ff656d0f289b3555ec65140ff9371e3d574278586f65f25.jpg

---

## Lecture: output\nbodyOpenMP\page_018\nbodyOpenMP_page_018\auto

# Computing the total force on particle q in the reduced algorithm

for $\begin{array} { r l } { \textsf { e a c h ~ p a r t i c l e ~ k > q } \left\{ \right. } & { } \\ { \textsf { x } _ { - } \mathrm { d i } \textsf { f f } \textsf { \textsf { \textsf { \textsf { X } } } } [ \textsf { \textsf { X } } ] \textsf { \textsf { X } } } & { } \\ { \textsf { y } _ { - } \mathrm { d i } \textsf { f f } \textsf { \textsf { \textsf { f } } } = \textsf { p o s } [ \mathrm { q } ] \left[ \textsf { Y } \right] \textsf { \textsf { \textsf { - } } } \textsf { p o s } [ \mathrm { k } ] \left[ \textsf { Y } \right] ; } & { } \\ { \textsf { d i s t } \textsf { \textsf { \textsf { = } } } \textsf { g c h } [ \textsf { x } _ { - } \mathrm { d i } \pounds { \textsf { f f } } \ll \_ { - } \mathsf { d i } \pounds { \textsf { f f } } \textsf { \textsf { \textsf { + } } } \textsf { y } _ { - } \mathrm { d i } \pounds { \textsf { f } } \bot } & { } \\ { \textsf { d i s t } _ { - } \mathsf { c u b e d } \textsf { \textsf { = } } \textsf { d i s t } \ast \mathsf { d i s t } \ast \mathsf { d i s t } ; } & { } \\ { \textsf { f o r c e } _ { - } \mathsf { q k } \left[ \textsf { X } \right] \textsf { \textsf { = } } \textsf { G } \ast \mathtt { m a s s e s } \left[ \mathsf { q } \right] \ast \mathsf { m a s s e s } \left[ \textsf { k } \right] } & { } \\ { \textsf { f o r c e } _ { - } \mathsf { q k } \left[ \textsf { Y } \right] \textsf { \textsf { = } } \textsf { G } \ast \mathtt { m a s s e s } \left[ \mathsf { q } \right] \ast \mathsf { m a s s e s } \left[ \textsf { k } \right] } & { } \end{array}$ ]/dist_cube

forces [ql[x] += force_qk [x];   
forces [ql[Y] += force_qk [Y];   
forces [k ][x] −= force_qk [x];   
forces [k ][Y] −= force_qk [Y ];

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\nbodyOpenMP\page_018\nbodyOpenMP_page_018\auto\images\bb8b32d8a47bbccfa5e4c837b9e6c994cce5b363ace893692b4465ea74e07f22.jpg

---

## Lecture: output\nbodyOpenMP\page_019\nbodyOpenMP_page_019\auto

# Serial pseudo-code

for each timestep $\{$

![](images/f3423a0560947f5ca808440067bd18b22db5b406993cfacf2ac7c63db8969e1c.jpg)

![](images/57f51ab0d95a2e7e44c261f470e0b00904c08f6fef3a14a20e6813c17d4c5482.jpg)

# iterating over particles

In principle, parallelizing the two inner for loops will map tasks/particles to cores.

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\nbodyOpenMP\page_019\nbodyOpenMP_page_019\auto\images\57f51ab0d95a2e7e44c261f470e0b00904c08f6fef3a14a20e6813c17d4c5482.jpg
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\nbodyOpenMP\page_019\nbodyOpenMP_page_019\auto\images\f3423a0560947f5ca808440067bd18b22db5b406993cfacf2ac7c63db8969e1c.jpg

---

## Lecture: output\nbodyOpenMP\page_020\nbodyOpenMP_page_020\auto

# First attempt

for each timestep { # pragma omp parallel for # pragma omp parallel for 1

Let’s check for race conditions caused by loop-carried dependences.

---

## Lecture: output\nbodyOpenMP\page_021\nbodyOpenMP_page_021\auto

# First loop

pragma omp parallel for   
for each particle q { forces [ql[x] = forces[ql[y] = 0; x_diff = pos[q][x] − pos[k ][x ]; $=$ dist_cubed $=$ forces [q][x] −= G\*masses [q]\*masses [k $] /$ $^ *$ forces [qlly] −= G\*masses [q]\*masses [k $] /$ $^ *$   
}

---

## Lecture: output\nbodyOpenMP\page_022\nbodyOpenMP_page_022\auto

# Second loop

# p1 ${ \begin{array} { r l } { \mathbf { a g m a ~ o m p ~ p ~ a r a l l e 1 ~ f o r } } & { } \\ { \mathbf { r } } & { \circ \mathbf { a } \operatorname { c h ~ \rho ~ p a r t i c l e ~ q ~ \operatorname { q } ~ \operatorname { f } ~ \rho ~ \operatorname { f } ~ \rho ~ } } \\ { \mathbf { p o s } [ \operatorname { q } ] [ \operatorname { X } ] } & { + = \operatorname { \ d e l t a \_ t * v e l } [ \operatorname { q } \operatorname { J } [ \operatorname { X } ] ] } \\ { \mathbf { p o s } [ \operatorname { q } ] [ \operatorname { Y } ] } & { + = \operatorname { \ d e l t a \_ t * v e l } [ \operatorname { q } \operatorname { J } [ \operatorname { Y } ] } \\ { \operatorname { v e l } [ \operatorname { q } ] [ \operatorname { X } ] } & { + = \operatorname { \ d e l t a \_ t } / \operatorname { m a s s e s } [ \operatorname { q }  } \\ { \operatorname { v e l } [ \operatorname { q } ] [ \operatorname { Y } ] } & { + = \operatorname { \ d e l t a \_ t - t } / \operatorname { m a s s e s } [ \operatorname { q }  } \end{array} }$   
fo ]\* forces [qllx]; ]\*forces [qllY];

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\nbodyOpenMP\page_022\nbodyOpenMP_page_022\auto\images\4a7aef0eec454c94de597a8039fa9a9aeb196b2f4da4c7448c57f49fe903e32a.jpg

---

## Lecture: output\nbodyOpenMP\page_023\nbodyOpenMP_page_023\auto

# Repeated forking and joining of threads

![](images/ad19b9b6b66f2aa31d99a22138a168895c30ba0ff61100115897d0d5576a109a.jpg)

# pragma omp p aralle1 for each timestep   
# pragma omp for for each particle q   
# pragma omp for for each particle q }

The same team of threads will be used in both loops and for every iteration of the outer loop.

But every thread will print all the positions and velocities.

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\nbodyOpenMP\page_023\nbodyOpenMP_page_023\auto\images\ad19b9b6b66f2aa31d99a22138a168895c30ba0ff61100115897d0d5576a109a.jpg

---

## Lecture: output\nbodyOpenMP\page_024\nbodyOpenMP_page_024\auto

# Adding the single directive

# pragma omp parallel for each timestep { $\{$   
# pragma omp single }   
# pragma omp for for each particle q   
# pragma omp for for each particle q

---

## Lecture: output\nbodyOpenMP\page_025\nbodyOpenMP_page_025\auto

# Parallelizing the Reduced Solver Using OpenMP

# pragma omp p arallel for each timestep {   
# pragma omp single }   
# pragma omp for for each particle q   
# pragma omp for for each particle q   
# pragma omp for for each particle q

---

## Lecture: output\nbodyOpenMP\page_026\nbodyOpenMP_page_026\auto

# Problems

$$
\mathbf { F } _ { 3 } = - \mathbf { f } _ { 0 3 } - \mathbf { f } _ { 1 3 } - \mathbf { f } _ { 2 3 }
$$

Updates to forces[3] create a race condition.

In fact, this is the case in general.

Updates to the elements of the forces array introduce race conditions into the code.

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\nbodyOpenMP\page_026\nbodyOpenMP_page_026\auto\images\634c364f0a7c83053914a806328bd986047f9a0645dd69dcef83b00986b470ef.jpg

---

## Lecture: output\nbodyOpenMP\page_027\nbodyOpenMP_page_027\auto

# First solution attempt

${ \begin{array} { r l } { \tt { r a g m a ~ o m p ~ c r i t i c a l } } & { } \\ { \tt { f o r c e s ~ [ \tt { q } ] [ \tt { X } ] ~ * = ~ f o r c e _ { - } \tt { c } } } \\ { \tt { f o r c e s ~ [ \tt { q } ] [ \tt { Y } ] ~ * = ~ f o r c e _ { - } \tt { c } } } \\ { \tt { f o r c e s ~ [ \tt { k } ] [ \tt { X } ] ~ * = ~ f o r c e _ { - } \tt { c } } } \\ { \tt { f o r c e s ~ [ \tt { k } ] [ \tt { X } ] ~ * = ~ f o r c e _ { - } \tt { c } } } \\ { \tt { f o r c e s ~ [ \tt { k } ] [ \tt { Y } ] ~ - = ~ f o r c e _ { - } \tt { c } } } \end{array} }$ es   
# p   
{ X ]; Y]; X ]; Y];   
} Access to the forces array will be effectively se

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\nbodyOpenMP\page_027\nbodyOpenMP_page_027\auto\images\01613bceaf173312374f6a3727b5b7c36e7771fe28239f89c72e90b977132f6e.jpg

---

## Lecture: output\nbodyOpenMP\page_028\nbodyOpenMP_page_028\auto

# Second solution attempt

omp_set_lock(locks [ql) ;

forces[ql[x] += force_qk [x];   
forces[ql[y] += force_qk[Y];   
omp_unset_lock(locks [ql); omp_set_lock(locks[k ]) ;   
forces [k ][x] —= force_qk [x ];   
forces[k ][y] —= force_qk[y];   
omp_unset_lock (locks [k l) ;

Use one lock for each particle.

---

## Lecture: output\nbodyOpenMP\page_029\nbodyOpenMP_page_029\auto

# First Phase Computations for Reduced Algorithm with Block Partition

<table><tr><td rowspan=1 colspan=2></td><td rowspan=1 colspan=3>Thread</td></tr><tr><td rowspan=1 colspan=1>Thread</td><td rowspan=1 colspan=1>Particle</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2</td></tr><tr><td rowspan=2 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>fo1 + f02 + f03 + f04 + f05</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>-f01 + f12 + f13 + f14 + f15</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=2 colspan=1>1</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>-f0_2--f12</td><td rowspan=1 colspan=1>f23 + f24 +f25</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>-f03  f13</td><td rowspan=1 colspan=1>-f23+f34+f35</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=2 colspan=1>2</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>-f04-f14</td><td rowspan=1 colspan=1>-f24-f34</td><td rowspan=1 colspan=1>f45</td></tr><tr><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>-f05-f15</td><td rowspan=1 colspan=1>-f25-f35</td><td rowspan=1 colspan=1>-f45</td></tr></table>

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\nbodyOpenMP\page_029\nbodyOpenMP_page_029\auto\images\36f26a9160cb1a7f4263a3adb4fc911100561e78528eaeb12caffa04b60bee7f.jpg

---

## Lecture: output\nbodyOpenMP\page_030\nbodyOpenMP_page_030\auto

# First Phase Computations for Reduced Algorithm with Cyclic Partition

<table><tr><td rowspan=1 colspan=2></td><td rowspan=1 colspan=3>Thread</td></tr><tr><td rowspan=1 colspan=1>Thread</td><td rowspan=1 colspan=1>Particle</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2</td></tr><tr><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>f01 + f02 + f03 + f04 + f05</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>-f01</td><td rowspan=1 colspan=1>f12 + f 13 + {14 + f15</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>-f02</td><td rowspan=1 colspan=1>-f12</td><td rowspan=1 colspan=1>f23 + f24 + f25</td></tr><tr><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>−f03 + f34 + f35</td><td rowspan=1 colspan=1>-f13</td><td rowspan=1 colspan=1>-{23</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>-f04-f34</td><td rowspan=1 colspan=1>−f14+f45</td><td rowspan=1 colspan=1>-f{24</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>-f05-f35</td><td rowspan=1 colspan=1>−f15-f45</td><td rowspan=1 colspan=1>-f25</td></tr></table>

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\nbodyOpenMP\page_030\nbodyOpenMP_page_030\auto\images\c819deeb0e53babb40fb26adfd7dce1d0643f1ec025e5d4288ff485498e055c5.jpg

---

## Lecture: output\nbodyOpenMP\page_031\nbodyOpenMP_page_031\auto

# Revised algorithm – phase I

pragma omp for   
for each particle q { x_dif f = pos [q l[x] − pos [k ][x ]; $=$ $=$ force_qk[x] = G\*masses [q] $^ *$ masses [k ]/dist_cubed force_qk[Y] = G\*masses [q] $^ *$ masses [k ]/dist_cubed

loc_forces [my_rank }[ql[y] += force_qk[Y ]; loc_forces [my_rank ] [ k l[x ] —= force_qk [x]; loc_forces [my_rank ][ k ][Y ]

---

## Lecture: output\nbodyOpenMP\page_032\nbodyOpenMP_page_032\auto

# Revised algorithm – phase II

pragma omp for   
fo $\begin{array} { r l } & { \mathrm { ~  ~ { \widetilde { \phi } } ~ } , \quad \mathrm { q ~ < ~ n ~ } ; \quad \mathrm { q } + + ) \quad \{ \mathrm { ~ }  { \widetilde { \phi } } \} } \\ & { \mathrm { ~  { \ f ~ o r ~ c e s ~ } [ \mathrm { ~ q ~ } ] [  { \ X } ] ~ = ~  { \widetilde { \phi } } ~ }  { \mathrm { T } } \circ  { \mathrm { e s } } \left[ \mathrm { ~ q ~ } \right] [ \mathrm { ~  { \mathbb { Y } } ~ } ] ~ = ~ 0 ; } \\ & { \mathrm { ~  ~ { \ f o r ~ \widetilde { \phi } } ~ } (  { \mathrm { t h } } \mathrm { ~  { r e a d } ~ = ~ 0 ~ } ;  { \mathrm { ~ t h r e e a d } } <  { \mathrm { ~ t h r e e a c } } } \\ & { \mathrm { ~  ~ { \widetilde { \phi } } ~ } \mathrm { ~ } \mathrm { f o r c e s ~ } [ \mathrm { ~ q ~ } ] [ \mathrm { ~  { X } } ] ~ + = ~ \mathrm { \lambda ~ l ~ o c \mathrm { ~  { \widetilde { \phi } } _ - }  { \widetilde { \phi } } ~ }  { \mathrm { r c e s } } \left[  { \mathrm { ~ t ~ h ~ } } \right] } \\ & { \mathrm { ~  ~ { \widetilde { \phi } } ~ } \mathrm { ~ } \mathrm { f ~ o r c e s ~ } [ \mathrm { ~ q ~ } ] [ \mathrm { ~  { Y } } ] ~ + = ~ \mathrm { \lambda ~ l ~ o c \mathrm { ~  { \widetilde { \phi } } _ - }  { \widetilde { \phi } } ~ }  { \mathrm { r c e s } } \left[  { \mathrm { ~ t ~ h ~ } } \right] } \\ & { \mathrm { ~  { \widetilde { \phi } } ~ } } \end{array}$ read ][ql[x ]; read  [q ll y ];   
}

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\nbodyOpenMP\page_032\nbodyOpenMP_page_032\auto\images\c2a8c389f1b2cbefd68b01c72547cc3f8e2d1f8f7fc2eaab607f3108e06d7b37.jpg

---

## Lecture: output\openmp\page_001\openmp_page_001\auto

# Introduction to High-Performance and Parallel Computing

# Shared Memory Programming with OpenMP

Slides adapted from the lecture notes by Peter Pacheco

---

## Lecture: output\openmp\page_002\openmp_page_002\auto

# Roadmap

• OpenMP basics.   
• Using OpenMP to parallelize for loops.   
• Task parallelism.   
• Explicit thread synchronization.   
• Standard problems in shared-memory programming.

---

## Lecture: output\openmp\page_003\openmp_page_003\auto

# OpenMP

• An API for shared-memory parallel programming.

MP = multiprocessing

Designed for systems in which each thread or process can potentially have access to all available memory.

• System is viewed as a collection of cores or CPU’s, all of which have access to main memory.

---

## Lecture: output\openmp\page_004\openmp_page_004\auto

# A shared memory system

![](images/a3ee9c803da3361ff4157add7dc9966b990ae1c48a888ab8bf2d3620045ba052.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\openmp\page_004\openmp_page_004\auto\images\a3ee9c803da3361ff4157add7dc9966b990ae1c48a888ab8bf2d3620045ba052.jpg

---

## Lecture: output\openmp\page_005\openmp_page_005\auto

# Pragmas

• Special preprocessor instructions.   
Typically added to a system to allow behaviors that are not part of the basic C specification.   
Compilers that do not support the pragmas ignore them.

---

## Lecture: output\openmp\page_006\openmp_page_006\auto

#include <stdio .h>   
#include <stdlib .h>   
#include <omp . h>   
void Hello(void ); /\* Thread function \*/   
int main(int argc , char\* argv[l) { /\* Get number of threads from command line \*/ int thread_count $=$ strtol(argv[1], NuLL , 10);   
# pragma omp parallel num_threads (thread _count ) Hello); return 0;   
} /\* main \*/   
void Hello(void) { int my_rank $=$ omp_get_thread_num (); int thread_count $=$ omp_get_num_threads (); printf("Hello from thread %d of %d\n", my_rank, thread_count);   
} /\* Hello \*/

---

## Lecture: output\openmp\page_007\openmp_page_007\auto

gcc −g −Wall −fopenmp −o omp_hello omp_hello . c

. / omp_hello 4 running with 4 threads

![](images/efa2bdf2ed00ae6d749bcbea645e4612aaa80101299e045c8a991cdcce813360.jpg)

Hello from thread 0 of 4   
Hello from thread 1 of 4   
Hello from thread 2 of 4   
Hello from thread 3 of 4   
Hello from thread 1 of 4   
Hello from thread 2 of 4   
Hello from thread 0 of 4   
Hello from thread 3 of 4   
Hello from thread 3 of 4   
Hello from thread 1 of 4   
Hello from thread 2 of 4   
Hello from thread 0 of 4

![](images/b16cbf9bf0f3ebbf7f8534b1e8d6e798e7784b5e97fe2cd987746f14c537637c.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\openmp\page_007\openmp_page_007\auto\images\b16cbf9bf0f3ebbf7f8534b1e8d6e798e7784b5e97fe2cd987746f14c537637c.jpg
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\openmp\page_007\openmp_page_007\auto\images\efa2bdf2ed00ae6d749bcbea645e4612aaa80101299e045c8a991cdcce813360.jpg

---

## Lecture: output\openmp\page_008\openmp_page_008\auto

# OpenMp pragmas

# # pragma omp parallel

– Most basic parallel directive.

– The number of threads that run the following structured block of code is determined by the run-time system.

---

## Lecture: output\openmp\page_009\openmp_page_009\auto

# clause

• Text that modifies a directive.   
• The num_threads clause can be added to a parallel directive.   
• It allows the programmer to specify the number of threads that should execute the following block.

# pragma omp parallel num_threads ( thread_count )

---

## Lecture: output\openmp\page_010\openmp_page_010\auto

# Notes about directives

• There may be system-defined limitations on the number of threads that a program can start.   
• The OpenMP standard doesn’t guarantee that it will actually start thread_count threads. Most current systems can start hundreds or even thousands of threads. Unless we’re trying to start a lot of threads, we will almost always get the desired number of threads.

---

## Lecture: output\openmp\page_011\openmp_page_011\auto

# Some terminology

In OpenMP the collection of threads executing the parallel block — the original thread and the new threads — is called a team, the original thread is called the master, and the additional threads are called slaves.

---

## Lecture: output\openmp\page_012\openmp_page_012\auto

# In case the compiler doesn’t support OpenMP

# include <omp.h>

#ifdef _OPENMP # include <omp.h> #endif

---

## Lecture: output\openmp\page_013\openmp_page_013\auto

# In case the compiler doesn’t support OpenMP

# ifdef _OPENMP

int my_rank = omp_get_thread_num ( ); int thread_count = omp_get_num_threads ( ); # else int my_rank = 0; int thread_count = 1; # endif

---

## Lecture: output\openmp\page_014\openmp_page_014\auto

# THE TRAPEZOIDAL RULE

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\openmp\page_014\openmp_page_014\auto\images\ed83719bf2c36f4294765044e031517c994b28f35f684c1af13cabe2ff3a9768.jpg

---

## Lecture: output\openmp\page_015\openmp_page_015\auto

# The trapezoidal rule

![](images/3fe991dba1847460735ba3c4f3a51c4ffacdc5ec0960834ad4cbd0a22607026a.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\openmp\page_015\openmp_page_015\auto\images\3fe991dba1847460735ba3c4f3a51c4ffacdc5ec0960834ad4cbd0a22607026a.jpg

---

## Lecture: output\openmp\page_016\openmp_page_016\auto

# Serial algorithm

$\begin{array} { r l } & { \gamma _ { * } \quad I n p u t : \quad a , b , n \quad * / } \\ & { \mathrm { ~ \hat { n } ~ = ~ ( \mathrm { b } { - } a ) / n ~ } ; } \\ & { \mathrm { a p p r o x ~ = ~ ( \mathrm { ~ f ~ } ( ~ a ~ ) ~ + ~ f ~ ( \mathrm { ~ b ~ } ) ~ ) ~ } / 2 . } \\ & { \mathrm { ~ \mathbf { f o r ~ } ~ ( ~ i ~ = ~ 1 ~ ; ~ i ~ < = ~ n { - } 1 ~ ; ~ i + } } \\ & { \mathrm { ~ \check { x } _ { - } { \mathrm { i } } ~ = ~ a ~ + ~ i ~ \mathrm { \hat { x } } * h ~ } ; } \\ & { \mathrm { a p p r o x ~ \hat { \xi } { + = } ~ \mathbf { f } ~ ( ~ x _ { - } { \mathrm { i } } ~ ) ~ } ; } \end{array}$ 0; } approx = h\*approx;

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\openmp\page_016\openmp_page_016\auto\images\e3496d36feaf13dc119b1c0b404a0dfb590fff7c8f9e096a175be6ef1f91d423.jpg

---

## Lecture: output\openmp\page_017\openmp_page_017\auto

# A First OpenMP Version

1) We identified two types of tasks:

a) computation of the areas of individual trapezoids, and   
b) adding the areas of trapezoids.

2) There is no communication among the tasks in the first collection, but each task in the first collection communicates with task 1b.

---

## Lecture: output\openmp\page_018\openmp_page_018\auto

# A First OpenMP Version

3) We assumed that there would be many more trapezoids than cores.

• So we aggregated tasks by assigning a contiguous block of trapezoids to each thread (and a single thread to each core).

---

## Lecture: output\openmp\page_019\openmp_page_019\auto

# Assignment of trapezoids to threads

![](images/dce25fdc2c2f2d38304df8401ae84f9c231d1a0a3300e0be0de69e2dfbdd93be.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\openmp\page_019\openmp_page_019\auto\images\dce25fdc2c2f2d38304df8401ae84f9c231d1a0a3300e0be0de69e2dfbdd93be.jpg

---

## Lecture: output\openmp\page_020\openmp_page_020\auto

<table><tr><td rowspan=1 colspan=1>Time</td><td rowspan=1 colspan=1>Thread 0</td><td rowspan=1 colspan=1>Thread 1</td></tr><tr><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>global_result = 0 to register</td><td rowspan=1 colspan=1>fi nish my_result</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>my_result = 1 to register</td><td rowspan=1 colspan=1>global_result = 0 to register</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>add my_result to global_result</td><td rowspan=1 colspan=1>my_result = 2 to register</td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>store global_result = 1</td><td rowspan=1 colspan=1>add my-result to global_result</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>store global_result = 2</td></tr></table>

Unpredictable results when two (or more) threads attempt to simultaneously execute:

global_result += my_result ;

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\openmp\page_020\openmp_page_020\auto\images\ed40931a4be9d11f2acb4aa06d478f5fc7b55b554098643e23852a5f2e121be8.jpg

---

## Lecture: output\openmp\page_021\openmp_page_021\auto

# Mutual exclusion

# pragma omp critical global_result += my_result ;

![](images/00e9fe51f1a78153ef3f07df816de71609348fca28d900bce8e14253239d9f1b.jpg)

only one thread can execute the following structured block at a time

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\openmp\page_021\openmp_page_021\auto\images\00e9fe51f1a78153ef3f07df816de71609348fca28d900bce8e14253239d9f1b.jpg

---

## Lecture: output\openmp\page_022\openmp_page_022\auto

#include <stdio .h> #include <stdlib .h> #include <omp. h>

void Trap(double a, double b, int n, double\* global_result_p );

int main(int arg double globa double a，b; int n; int thread_count;

$$
\begin{array} { r l r } { \mathrm { ~ c ~ , ~ } \ \mathbf { c h a r } * \ \mathrm { a r g v } \left[ \mathrm { 1 } \right] ) } & { \left\{ \begin{array} { l l } & { \mathrm { ~ } } \\ { \mathrm { ~ \textit ~ { ~ \beta ~ } ~ } _ { l \mathrm { ~ - } } \mathrm { r e ~ s u l t } \ i \mathrm { ~ \textit ~ { ~ i ~ n ~ } ~ } \ g l \ d r } \end{array} \right. } \\ { \mathrm { ~ l ~ - ~ r \in ~ s u l t } \ \mathrm { ~ \textit ~ { ~ a ~ x ~ g ~ y ~ } ~ } } & { / * \ \mathrm { ~ \textit ~ { ~ L ~ e ~ f t ~ } ~ } \ a n d \ r i \ g h t \ e n d _ { h } } \\ & { \textit { f * } \ L e f t \ a n d \ r i g h t \ e n d _ { h } } \\ & { \textit { f * } \ L e t a l \ h u m b e r \ o f \ t r a } \end{array}
$$

bal_result \*/ points \*/ ezoids \*/

thread_count $=$ strtol(argv[1l, NuLL, 10); printf("Enter a, b, and n\n"); scanf("%lf %lf %d", &a, &b, &n); # pragma omp parallel num_threads (thread _count) Trap(a, b, n, &global_result);

printf("with n $=$ %d trapezoids, our estimate\n", n);   
printf("of the integral from %f to %f = %.14e\n", a,b, global_result);   
return 0;   
/\* main \*/

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\openmp\page_022\openmp_page_022\auto\images\3640efedd7e77df7fba21c70081f6d349cc30a9ae60b84f6fd7b5eee90c981bd.jpg

---

## Lecture: output\openmp\page_023\openmp_page_023\auto

void Trap(double a, double b, int n, double\* double h, x, my_result; double local_a , local_b; int i, local_n; int my_rank $=$ omp_get_thread_num (); int thread_count = omp_get_num_threads ();

$\mathrm { ~ { ~ h ~ } ~ } = \mathrm { ~ \left( ~ b - a ~ \right) / ~ n ~ } ;$ (id:   
local_n = n/thread_count;   
local_a $=$ a + my_rank\*local_n\*h;   
local_b = local_a + local_n\*h;   
my_result $=$ (f(local_a) + f(local_b))/2.0;   
for ( $\mathrm { ~ \\ ~ { ~ i ~ } ~ } = \mathrm { ~ \Phi ~ } 1$ ; i <= local_n−1;i++) { x = local_a + i\*h; my_result += f(x);   
}   
my_result = my_result\*h;

# pragma omp critic al \*global_result_p += my_result; }.. ./\* .Trap. \*/

---

## Lecture: output\openmp\page_024\openmp_page_024\auto

![](images/fa27bce5b4eb41dd1bd925387eab602929dc61fb76f11727476cf6a5e20af59e.jpg)

SCOPE OF VARIABLES

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\openmp\page_024\openmp_page_024\auto\images\fa27bce5b4eb41dd1bd925387eab602929dc61fb76f11727476cf6a5e20af59e.jpg

---

## Lecture: output\openmp\page_025\openmp_page_025\auto

# Scope

• In serial programming, the scope of a variable consists of those parts of a program in which the variable can be used.

• In OpenMP, the scope of a variable refers to the set of threads that can access the variable in a parallel block.

---

## Lecture: output\openmp\page_026\openmp_page_026\auto

# Scope in OpenMP

• A variable that can be accessed by all the threads in the team has shared scope.

• A variable that can only be accessed by a single thread has private scope.

• The default scope for variables declared before a parallel block is shared.

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\openmp\page_026\openmp_page_026\auto\images\344743c0a12e4c1683c3c19561f7b7b94167013f1bf3dbd98be752405a66982f.jpg

---

## Lecture: output\openmp\page_027\openmp_page_027\auto

![](images/2f2e874b5a44f8612a05a86995b8395d6bfa2a0f6296a67b506380f6c896fc34.jpg)

THE REDUCTION CLAUSE

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\openmp\page_027\openmp_page_027\auto\images\2f2e874b5a44f8612a05a86995b8395d6bfa2a0f6296a67b506380f6c896fc34.jpg

---

## Lecture: output\openmp\page_028\openmp_page_028\auto

We have the following version to add each thread’s local calculation to get global_result.

void Trap(double a, double b, int n, double\* global_result_p);

How about simplifying it as the following?

double Trap(double a, double b, int n);

![](images/f0379fa6baa1dbfe9993e78984e2a8672274f14ccaefe07d1f20c8e070d71a9e.jpg)

If we use this, there’s race condition!

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\openmp\page_028\openmp_page_028\auto\images\f0379fa6baa1dbfe9993e78984e2a8672274f14ccaefe07d1f20c8e070d71a9e.jpg

---

## Lecture: output\openmp\page_029\openmp_page_029\auto

# If we fix it like this…

double Local_trap(double a, double b, int n ); global_result = 0.0;   
# pragma omp parallel num_threads (thread_count) {   
# pragma omp critical $+ =$ Local_trap(double a, double b, int n

… we force the threads to execute sequentially.

---

## Lecture: output\openmp\page_030\openmp_page_030\auto

We can avoid this problem by declaring a private variable inside the parallel block and moving the critical section after the function call.

global_result = 0.0;   
# pragma omp parallel num_threads (thread_count) double my_result = 0.0; /\* private \*/ my_result += Local_trap(double a, double b, int n);   
# pragma omp critical global_result += my_result; }

---

## Lecture: output\openmp\page_031\openmp_page_031\auto

# Reduction operators

• A reduction operator is a binary operation (such as addition or multiplication).

• A reduction is a computation that repeatedly applies the same reduction operator to a sequence of operands in order to get a single result.

• All of the intermediate results of the operation should be stored in the same variable: the reduction variable.

---

## Lecture: output\openmp\page_032\openmp_page_032\auto

# A reduction clause can be added to a parallel directive.

reduction(<operator>: <variable list>)

![](images/48d56531981d77e8ddc42f592f5f937c56b6e940f31b5d047900b21b7ad5b58d.jpg)

+, \*, -, &, |, ˆ, &&, ||

# pragma omp parallel num_threads(thread_count ) reduction(+: global_result) global_result += Local_trap(double a, double b, int

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\openmp\page_032\openmp_page_032\auto\images\48d56531981d77e8ddc42f592f5f937c56b6e940f31b5d047900b21b7ad5b58d.jpg

---

## Lecture: output\openmp\page_033\openmp_page_033\auto

![](images/ac21c008a310b367b20851f269cb56b6ace7f9fc464e14d4d8a598de7fd8bbaf.jpg)

THE “PARALLEL FOR” DIRECTIVE

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\openmp\page_033\openmp_page_033\auto\images\ac21c008a310b367b20851f269cb56b6ace7f9fc464e14d4d8a598de7fd8bbaf.jpg

---

## Lecture: output\openmp\page_034\openmp_page_034\auto

# Parallel for

• Forks a team of threads to execute the following structured block.

• However, the structured block following the parallel for directive must be a for loop.

• Furthermore, with the parallel for directive the system parallelizes the for loop by dividing the iterations of the loop among the threads.

---

## Lecture: output\openmp\page_035\openmp_page_035\auto

$\mathrm { ~ h ~ } = \mathrm { ~ ( ~ b { - a } ~ ) / ~ r ~ }$ ;   
approx = (f(a) + f(b ))/2.0;   
for( $\mathrm { ~ \\ ~ { ~ i ~ } ~ } = \mathrm { ~ \Phi ~ } 1$ ;i<= n−1；i++) approx $+ = \mathrm { ~ \underline { ~ } { ~ f ~ } ~ ( ~ a ~ \mathrm { ~ \ + ~ \mathrm { ~ i ~ } * h ~ } ) ~ }$ ;   
approx = h\*approx;

![](images/c659e500273ace40d03e2f9396469b8f2bf328ae21a23244de9d60fb02824604.jpg)

![](images/02fbacd127abbbc4b084def3b51c1edf25a1f5ab080b72769d064624137574cc.jpg)

(cid:) $\mathrm { ~ \texttt ~ { ~ h ~ } ~ } = \mathrm { ~ \texttt ~ { ~ ( ~ b ~ - a ~ ) ~ } ~ } / \mathrm { ~ n ~ } ;$ (cid:) $\mathsf { a p p r o x } \ = \ \mathsf { ( } \pounds ( \mathsf { a } ) + \pounds ( \mathsf { b } ) ) / 2 . 0$ ; # pragma omp parallel for num_threads(thread_count) i reduction(+: approx) for ( $\mathrm { ~ \ ~ { ~ i ~ } ~ } = \mathrm { ~  ~ { ~ 1 ~ } ~ }$ ; $\mathrm { ~ i ~ } < = \mathrm { ~ n - 1 ~ }$ ;i++) approx $+ = \mathrm { ~ \tt ~ f ~ } ( \mathrm { ~ a ~ } + \mathrm { ~ \tt ~ i ~ } * \mathrm { h } )$ ; approx $=$ h\*approx;

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\openmp\page_035\openmp_page_035\auto\images\02fbacd127abbbc4b084def3b51c1edf25a1f5ab080b72769d064624137574cc.jpg
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\openmp\page_035\openmp_page_035\auto\images\c659e500273ace40d03e2f9396469b8f2bf328ae21a23244de9d60fb02824604.jpg

---

## Lecture: output\openmp\page_036\openmp_page_036\auto

# Legal forms for parallelizable for statements

index++ ++index index $<$ end index $< =$ end --index for index $=$ $> =$ $+ =$ index $>$ end index $- =$ index $=$ index + incr index $=$ incr + index index $=$

---

## Lecture: output\openmp\page_037\openmp_page_037\auto

# Caveats

• The variable index must have integer or pointer type (e.g., it can’t be a float).

• The expressions start, end, and incr must have a compatible type. For example, if index is a pointer, then incr must have integer type.

---

## Lecture: output\openmp\page_038\openmp_page_038\auto

# Caveats

• The expressions start, end, and incr must not change during execution of the loop.

During execution of the loop, the variable index can only be modified by the “increment expression” in the for statement.

---

## Lecture: output\openmp\page_039\openmp_page_039\auto

# Data dependencies

$\mathbf { f i b o } [ \mathbf { \nabla } 0 \mathbf { ] } \ = \ \mathbf { f i b o } [ \mathbf { \nabla } 1 \mathbf { ] } \ = \ 1 ;$

for $\mathbf { ( i ~ = ~ 2 ; ~ i ~ < ~ n ; ~ i + + ) }$

fibo[ i ] = fibo[ i – 1 ] + fibo[ i – 2 ];

2 threads

fibo[ 0 ] = fibo[ 1 ] = 1;

# pragma omp parallel for num_threads(2)

but sometimes we get this

---

## Lecture: output\openmp\page_040\openmp_page_040\auto

# What happened?

![](images/42e0a33db3210b72e073840477a3f4071869e560374182d9fec0b2fbdd6a0197.jpg)

1. OpenMP compilers don’t check for dependences among iterations in a loop that’s being parallelized with a parallel for directive.

2. A loop in which the results of one or more iterations depend on other iterations cannot, in general, be correctly parallelized by OpenMP.

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\openmp\page_040\openmp_page_040\auto\images\42e0a33db3210b72e073840477a3f4071869e560374182d9fec0b2fbdd6a0197.jpg

---

## Lecture: output\openmp\page_041\openmp_page_041\auto

# Estimating π

$$
\left[ 1 - { \frac { 1 } { 3 } } + { \frac { 1 } { 5 } } - { \frac { 1 } { 7 } } + \cdots \right] = 4 \sum _ { k = 0 } ^ { \infty }  \frac  ( -
$$

$$
\begin{array} { r l } { \mathbf { d o u b l e } } & { \mathbf { f a c t o r ~ = ~ 1 . 0 ; } } \\ { \mathbf { d o u b l e } } & { \mathbf { s u m ~ = ~ 0 . 0 ; } } \\ { \mathbf { f o r ~ ( \lambda \mathbf { k } ~ = ~ 0 ; ~ \lambda \mathbf { k } ~ < ~ n ; ~ \lambda ~ k + + ) ~ } } \\ { \mathbf { s u m ~ + = ~ \mathbf { f } ~ a c t o r / ( 2 * \mathbf { k } + 1 ) ~ } } \\ { \mathbf { f a c t o r ~ = ~ - f a c t o r ; } } \\ { \mathbf { j } } \\ { \mathbf { p i _ { - } a p p r o x ~ = ~ 4 . 0 * { s u m } ; } } \end{array}
$$

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\openmp\page_041\openmp_page_041\auto\images\36a00582212e217ec19bd5c7a2eee23b458c8257a2cbd74c4067a09a7eb81244.jpg
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\openmp\page_041\openmp_page_041\auto\images\b154a69c9ef0b104b150e7524ea4c79759b569f6234816a4853cadab771a514d.jpg

---

## Lecture: output\openmp\page_042\openmp_page_042\auto

# Problem in OpenMP solution #1

![](images/7f5a1ee62dd2c9f91de5f7101167a5c3042266c64cde490c56710360f41531c7.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\openmp\page_042\openmp_page_042\auto\images\7f5a1ee62dd2c9f91de5f7101167a5c3042266c64cde490c56710360f41531c7.jpg

---

## Lecture: output\openmp\page_043\openmp_page_043\auto

# Fix in OpenMP solution #2

#

double sum = 0.0;   
pragma omp parallel for num_threads(thread_count) \ reduction(+: sum) private(factor)   
for ( $\mathrm { ~  ~ { ~ k ~ } ~ } = \mathrm { ~ \ r ~ { ~ 0 ~ } ~ }$ if(k $\%$ 2==0) factor = 1.0; else sum += factor/(2\*k +1);   
}

![](images/3444353e286a5caf6302e1aa1f5338acd5860077c8b00a8b29692c3811cc625f.jpg)

Ensures factor has private scope.

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\openmp\page_043\openmp_page_043\auto\images\3444353e286a5caf6302e1aa1f5338acd5860077c8b00a8b29692c3811cc625f.jpg

---

## Lecture: output\openmp\page_044\openmp_page_044\auto

# The default clause

• Let the programmer specify the scope of each variable in a block.

default (none)

With this clause the compiler will require that we specify the scope of each variable we use in the block and that has been declared outside the block.

---

## Lecture: output\openmp\page_045\openmp_page_045\auto

# The default clause

double $\mathsf { s u m } ~ = ~ 0 . 0$   
pragma omp parallel for num_threads(thread_count) i default(none) reduction(+:sum) private(k , factor) \ shared(n)   
for ( if $\begin{array} { r c l } { \mathrm { ~ : ~ } } & { \mathrm { ~ 0 ; ~ \ x ~ < ~ n ~ ; ~ \ x _ { + + } ) ~ } \left\{ \begin{array} { r c l } { \mathrm { ~ } } & { \mathrm { ~ } } & { \mathrm { ~ } } \\ { \mathrm { ~ ( ~ k ~ \mathcal { ~ } ~ \mathcal { { H } } ~ 2 ~ = ~ 0 ~ ) ~ } } & { \mathrm { ~ } } \end{array} \right. } \\ { \mathrm { ~ } } & { \mathrm { ~ f ~ a ~ c ~ t ~ o ~ r ~ = ~ 1 ~ . ~ } 0 ; } \\ { \mathrm { ~ } } & { \mathrm { ~ } } & { \mathrm { ~ } } \\ { \mathrm { ~ f ~ a ~ c ~ t ~ o ~ r ~ = ~ - ~ 1 ~ . ~ } 0 ; } \\ { \mathrm { ~ } } & { \mathrm { ~ : ~ } } & { \mathrm { ~ f ~ a ~ c ~ t ~ o ~ r ~ / ~ ( ~ 2 ~ * ~ k ~ + ~ 1 ~ ) ~ ; ~ } } \end{array}$ els sun   
}

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\openmp\page_045\openmp_page_045\auto\images\4f333e7dc2169d031e60b4fa40287c6cc465d23c2d010f3fd46695ccc8c6357a.jpg

---

## Lecture: output\openmp\page_046\openmp_page_046\auto

![](images/7cccadf55eef595f9898f7e9e77f8caf19c410f75e52c3d22bebd664c85927b5.jpg)

# MORE ABOUT LOOPS IN OPENMP: SORTING

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\openmp\page_046\openmp_page_046\auto\images\7cccadf55eef595f9898f7e9e77f8caf19c410f75e52c3d22bebd664c85927b5.jpg

---

## Lecture: output\openmp\page_047\openmp_page_047\auto

# Bubble Sort

for ( $\mathrm { ~  ~ { ~ i ~ } ~ } = \mathrm { ~ \ r ~ { ~ 0 ~ } ~ }$ a[i] = a[i +1];

![](images/ad7597d5869678a176b8eda7a217532b6de17fe2cc8543fe11e7e2533e78dbad.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\openmp\page_047\openmp_page_047\auto\images\ad7597d5869678a176b8eda7a217532b6de17fe2cc8543fe11e7e2533e78dbad.jpg

---

## Lecture: output\openmp\page_048\openmp_page_048\auto

# Serial Odd-Even Transposition Sort

or $\begin{array} { r l } & { \mathrm { ( ~ p h a s e ~ = ~ 0 ; ~ p h a s e ~ < ~ n ~ ; ~ p h a s e ~ + ~ \eta ~ } } \\ & { \textbf { f } \mathrm { ( ~ p h a s e ~ \% ~ 2 ~ = ~ 0 ) } } \\ & { \textbf { f o r } \mathrm { ( ~ i ~ = ~ 1 ~ ; ~ i ~ < ~ n ~ ; ~ i ~ + = ~ 2 ~ ) } } \\ & { \textbf { i f } \mathrm { ( ~ a [ \lambda - 1 ] ~ > ~ a [ \lambda ] ~ ) } \mathrm { S w a p } ( \mathfrak { e } } \\ & { \textbf { l s e } } \\ & { \textbf { f o r } \mathrm { ( ~ i ~ = ~ 1 ~ ; ~ i ~ < ~ n - 1 ~ ; ~ i ~ + = ~ 2 ~ ) } } \\ & { \textbf { i f } \mathrm { ( ~ a [ \lambda ] ~ > ~ a [ \lambda + 1 ] ) } \mathrm { S w a p } ( \mathfrak { e } } \end{array}$ +)  
i&a[i −1],&a[i ]) ;  
e&a[i ], &a[i + 1])

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\openmp\page_048\openmp_page_048\auto\images\1c6e29e257bb9a77d0aa98cc0d10293d5a9646bb0717e50d8ecaaf4e45045211.jpg

---

## Lecture: output\openmp\page_049\openmp_page_049\auto

# Serial Odd-Even Transposition Sort

<table><tr><td>Phase</td><td>Subscript in Array 0 1</td><td>2</td><td>3</td></tr><tr><td>0</td><td>9 7 一 7 9</td><td>8 1 6</td><td>6 8</td></tr><tr><td>1</td><td>7 7</td><td>9 1 6 6 9</td><td>8 8</td></tr><tr><td>2</td><td>7 1 6</td><td>6 9 7 8</td><td>1 8 9</td></tr><tr><td>3</td><td>6 6</td><td>7 8 1 7 8</td><td>9 9</td></tr></table>

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\openmp\page_049\openmp_page_049\auto\images\95bb4e8af36871f6510e6688e951a6fe0ea613c86fdff20d611a49dff668a0da.jpg

---

## Lecture: output\openmp\page_050\openmp_page_050\auto

# First OpenMP Odd-Even Sort

for (phase $\qquad = \quad 0$ if（phase $\%$ $2 \ \mathrm { ~ = ~ } \mathrm { ~ 0 ~ }$ )   
# pragma omp parallel for num_threads(thread_count) \ default(none) shared(a, n) private(i, tmp) for $\mathrm { ~  ~ \cdot ~ } \mathrm { ~  ~ i ~ } = \mathrm { ~  ~ 1 ~ }$ $\mathrm { ~ i ~ } < \mathrm { ~ n ~ }$ $\\mathrm { ~ i ~ } \ + = \ 2 )$ tmp = a[i−1]; $\mathrm { ~ a ~ } [ \mathrm { ~ i ~ } - 1 ] ~ = ~ \mathrm { ~ a ~ } [ \mathrm { ~ i ~ } ] $ $\mathsf { a } [ \mathrm { i } ] ~ = ~ \mathsf { t m p }$ } $\}$ else   
# pragma omp parallel for num_threads(thread_count) i default(none) shared(a, n) private(i, tmp) for $\mathrm { ~  ~ \mathcal ~ { ~ i ~ } ~ } = \mathrm { ~  ~ 1 ~ }$ $\mathrm { ~ i ~ } < \mathrm { ~ n - 1 ~ }$ $\\mathrm { ~ i ~ } \ + = \ 2 )$ if $\mathrm { ~ ( ~ a ~ [ ~ i ~ ] ~ > ~ \ a ~ [ ~ i + 1 ~ ] ~ ) ~ }$ $= \mathrm { ~ a ~ } [ \mathrm { ~ i ~ } + 1 ]$ $\mathsf { a } \left[ \mathrm { i } + 1 \right] \ = \ \mathsf { a } \left[ \mathrm { i } \ \right]$ $\mathsf { a } [ \mathrm { i } ] ~ = ~ \mathsf { t m p }$ 1 } 1

---

## Lecture: output\openmp\page_051\openmp_page_051\auto

# Second OpenMP Odd-Even Sort

# pragma omp parallel num_threads(thread _( default(none) shared(a, n) private(i for (phase $\qquad = \quad 0$ if (phase $\%$ $2 \ \mathrm { ~ = ~ } \mathrm { ~ 0 ~ }$ )   
# pragma omp for for $\begin{array} { r l } & { \mathrm {  ~ \hat { \mu } _ { i } ~ } = \mathrm {  ~ \hat { \mu } _ 1 ~ } ; \mathrm {  ~ i ~ } < \mathrm {  ~ n ~ } ; \mathrm {  ~ i ~ } + = \mathrm {  ~ \beta ~ } 2 ) \left\{ \begin{array} { r l } & { \{ \mu _ { \ell } = \mathrm {  ~ \hat { \mu } _ { \ell } ~ } } \\ & { \mathrm {  ~ \hat { \mu } _ { \ell } ~ } } \end{array} \right. } \\ &  \mathrm {  ~ \hat { \mu } _ { \ell } ~ } ( \mathrm {  ~ \hat { \mu } _ { i } - \mathrm {  ~ \hat { \mu } _ { \ell } ~ } } { \mathrm {  ~ \hat { \mu } _ { \ell } ~ } } ) > \mathrm {  ~ \hat { \mu } _ { a } [ \mathrm {  ~ i ~ } ] \} \quad \{ \begin{array} { r l } & { \{ \mu _ { \ell } = \mathrm {  ~ \hat { \mu } _ { \ell } ~ } } \\ & { \mathrm {  ~ \hat { \mu } _ { \ell } ~ } } \end{array} \} } \\ &  \mathrm {  ~ \hat { \mu } _ { a } [ \mathrm {  ~ i ~ } - 1 ] \mathrm {  ~ \hat { \mu } _ { \ell } = \mathrm {  ~ \hat { \mu } _ { a } [ \mathrm {  ~ i ~ } ] ~ } } ; } \\ &  \mathrm {  ~ \hat { \mu } _ { a } [ \mathrm {  ~ i ~ } ] ~ } = \mathrm {  ~ \hat { \mu } _ { \ell } \cdot \mathrm {  ~ \hat { \mu } _ { \ell } ~ } } \end{array}$ if else   
# pragma omp for for $\begin{array}{c} \begin{array} { r l } & { \mathrm { i ~ \gamma = ~ 1 ; ~ i ~ < ~ n { - } 1 ; ~ i ~ { \Sigma } + = ~ 2 ) ~ \left\{ \begin\right.} {array} { l l } \\ { ( { \mathrm { a } } [ \mathrm { ~ i } ] \mathrm { ~ > ~ \ a } [ \mathrm { ~ i { + } 1 } ] ) ~ \{ \phantom { { + } } } } \end{array}    \\ & { \mathrm { t m p ~ = ~ \mathsf { a } } \left[ \mathrm { ~ i { + } 1 } \right] ; } \\ & { \mathrm { a } \left[ \mathrm { ~ i { + } 1 } \right] ~ = ~ \mathsf { a } \left[ \mathrm { ~ i { } } \right] ; } \\ & { \mathrm { a } \left[ \mathrm { ~ i } \right] ~ = ~ \mathsf { t m p } ; } \end{array}$ if }

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\openmp\page_051\openmp_page_051\auto\images\3359bc63e83cfb6dddda103a8763bfd865bbc6027e11ca35e33d0c64f0fe1309.jpg
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\openmp\page_051\openmp_page_051\auto\images\ceec19ec26735a7c352196baf46532fa983d1ccd4f20f12ba3a05b8ff4e235ce.jpg

---

## Lecture: output\openmp\page_052\openmp_page_052\auto

# Odd-even sort with two parallel for directives and two for directives. (Times are in seconds.)

<table><tr><td rowspan=1 colspan=1>thread_count</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>4</td></tr><tr><td rowspan=1 colspan=1>Two parallel for directives</td><td rowspan=1 colspan=1>0.770</td><td rowspan=1 colspan=1>0.453</td><td rowspan=1 colspan=1>0.358</td><td rowspan=1 colspan=1>0.305</td></tr><tr><td rowspan=1 colspan=1>Two for directives</td><td rowspan=1 colspan=1>0.732</td><td rowspan=1 colspan=1>0.376</td><td rowspan=1 colspan=1>0.294</td><td rowspan=1 colspan=1>0.239</td></tr></table>

![](images/4e6883124bcec5a2bf332c32ea00209e4bf8e1b7f388efd39de70bcd294bc445.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\openmp\page_052\openmp_page_052\auto\images\0b51cbc2d8a5a57d5bddbd49b60471e86d2235c280e1ba7e188ae3f15df2b5cf.jpg
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\openmp\page_052\openmp_page_052\auto\images\4e6883124bcec5a2bf332c32ea00209e4bf8e1b7f388efd39de70bcd294bc445.jpg

---

## Lecture: output\openmp\page_053\openmp_page_053\auto

![](images/fbed765f0b75735a901a89c930b57b6021dc4904b8f5b64a27bbac36b0e5d8da.jpg)

SCHEDULING LOOPS

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\openmp\page_053\openmp_page_053\auto\images\fbed765f0b75735a901a89c930b57b6021dc4904b8f5b64a27bbac36b0e5d8da.jpg

---

## Lecture: output\openmp\page_054\openmp_page_054\auto

We want to parallelize this loop.

$$
\begin{array} { l } { { \mathrm { s u m ~ = ~ 0 . 0 ; } } } \\ { { \mathrm { f o r ~ \rho ( \mathrm { ~ i ~ = ~ 0 ; ~ \rho _ { i } ~ \leq ~ \eta _ { n } ~ ; ~ \rho _ { i } + + } ) ~ } } } \\ { { \mathrm { s u m ~ + = ~ \rho _ { f } ( \mathrm { ~ i ~ } ) ; } } } \end{array}
$$

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\openmp\page_054\openmp_page_054\auto\images\47b4eba6d8a019335bfa6673640304e817b03d90f5f6772c741f2b1352f91572.jpg

---

## Lecture: output\openmp\page_055\openmp_page_055\auto

double f(int i) { $=$ double return_val = 0.0; return_val += sin(j); } return return_val; $f$

Our definition of function f.

---

## Lecture: output\openmp\page_056\openmp_page_056\auto

# Results

• f(i) calls the sin function i times. Assume the time to execute f(2i) requires approximately twice as much time as the time to execute f(i).

• n = 10,000 – one thread – run-time = 3.67 seconds.

---

## Lecture: output\openmp\page_057\openmp_page_057\auto

# Results

• n = 10,000 – two threads – default assignment – run-time = 2.76 seconds – speedup = 1.33

n = 10,000 – two threads – cyclic assignment – run-time = 1.84 seconds – speedup = 1.99

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\openmp\page_057\openmp_page_057\auto\images\685b214ef142c8ec27f8c3f18d12b1f61ed116ff6ac48a4b89fb523e3e746a3d.jpg

---

## Lecture: output\openmp\page_058\openmp_page_058\auto

# The Schedule Clause

# Default schedule:

pragma omp parallel for num_threads(thread_count) \ for( $\mathrm { ~  ~ { ~ i ~ } ~ } = \mathrm { ~ \ r ~ { ~ 0 ~ } ~ }$

# Cyclic schedule:

#

pragma omp parallel for num_threads(thread_count) \ reduction(+: sum) schedule(static , 1) for( $\mathrm { ~  ~ { ~ i ~ } ~ } = \mathrm { ~ \ r ~ { ~ 0 ~ } ~ }$ $\mathrm { ~ i ~ } < = \mathrm { ~ n ~ }$

---

## Lecture: output\openmp\page_059\openmp_page_059\auto

# schedule ( type , chunksize )

• Type can be:

– static: the iterations can be assigned to the threads before the loop is executed.

– dynamic or guided: the iterations are assigned to the threads while the loop is executing.

– auto: the compiler and/or the run-time system determine the schedule.

– runtime: the schedule is determined at run-time by an environment variable.

• The chunksize is a positive integer.

---

## Lecture: output\openmp\page_060\openmp_page_060\auto

# The Static Schedule Type

twelve iterations, 0, 1, . . . , 11, and three threads

schedule (static, 1)

$$
\begin{array} { l l } { { \mathrm { T h r e a d ~ 0 : } } } & { { 0 , 3 , 6 , 9 } } \\ { { \mathrm { T h r e a d ~ 1 : } } } & { { 1 , 4 , 7 , 1 0 } } \\ { { \mathrm { T h r e a d ~ 2 : } } } & { { 2 , 5 , 8 , 1 1 } } \end{array}
$$

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\openmp\page_060\openmp_page_060\auto\images\6bcee8c35b94c506600a136d3517dc5c4e4f8f7838f61f9c3e10059e96206d54.jpg

---

## Lecture: output\openmp\page_061\openmp_page_061\auto

# The Static Schedule Type

twelve iterations, 0, 1, . . . , 11, and three threads schedule (static, 2)

$$
\begin{array} { l l } { { \mathrm { T h r e a d ~ 0 : } } } & { { 0 , 1 , 6 , 7 } } \\ { { \mathrm { T h r e a d ~ 1 : } } } & { { 2 , 3 , 8 , 9 } } \\ { { \mathrm { T h r e a d ~ 2 : } } } & { { 4 , 5 , 1 0 , 1 1 } } \end{array}
$$

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\openmp\page_061\openmp_page_061\auto\images\f35bbe1b6515512cee6be1ef19b0002319c2737d9a01b5914c7e9970ddf58e44.jpg

---

## Lecture: output\openmp\page_062\openmp_page_062\auto

# The Static Schedule Type

twelve iterations, 0, 1, . . . , 11, and three threads schedule (static, 4)

$$
\begin{array} { l l } { { \mathrm { T h r e a d ~ 0 : } } } & { { 0 , 1 , 2 , 3 } } \\ { { \mathrm { T h r e a d ~ 1 : } } } & { { 4 , 5 , 6 , 7 } } \\ { { \mathrm { T h r e a d ~ 2 : } } } & { { 8 , 9 , 1 0 , 1 1 } } \end{array}
$$

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\openmp\page_062\openmp_page_062\auto\images\4b15c48b48e5b8a1ee7469b74924ff198a73fa163f9d980995dc01418c29f724.jpg

---

## Lecture: output\openmp\page_063\openmp_page_063\auto

# The Dynamic Schedule Type

• The iterations are also broken up into chunks of chunksize consecutive iterations.

• Each thread executes a chunk, and when a thread finishes a chunk, it requests another one from the run-time system.

• This continues until all the iterations are completed.

• The chunksize can be omitted. When it is omitted, a chunksize of 1 is used.

---

## Lecture: output\openmp\page_064\openmp_page_064\auto

# The Guided Schedule Type

• Each thread also executes a chunk, and when a thread finishes a chunk, it requests another one. However, in a guided schedule, as chunks are completed the size of the new chunks decreases. • If no chunksize is specified, the size of the chunks decreases down to 1. • If chunksize is specified, it decreases down to chunksize, with the exception that the very last chunk can be smaller than chunksize.

---

## Lecture: output\openmp\page_065\openmp_page_065\auto

<table><tr><td rowspan=1 colspan=1>Thread</td><td rowspan=1 colspan=1>Chunk</td><td rowspan=1 colspan=1>Size of Chunk</td><td rowspan=1 colspan=1>Remaining Iterations</td></tr><tr><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>1-5000</td><td rowspan=1 colspan=1>5000</td><td rowspan=1 colspan=1>4999</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>5001-7500</td><td rowspan=1 colspan=1>2500</td><td rowspan=1 colspan=1>2499</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>7501-8750</td><td rowspan=1 colspan=1>1250</td><td rowspan=1 colspan=1>1249</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>8751-9375</td><td rowspan=1 colspan=1>625</td><td rowspan=1 colspan=1>624</td></tr><tr><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>9376-9687</td><td rowspan=1 colspan=1>312</td><td rowspan=1 colspan=1>312</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>9688 9843</td><td rowspan=1 colspan=1>156</td><td rowspan=1 colspan=1>156</td></tr><tr><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>9844一9921</td><td rowspan=1 colspan=1>78</td><td rowspan=1 colspan=1>78</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>9922-9960</td><td rowspan=1 colspan=1>39</td><td rowspan=1 colspan=1>39</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>9961—9980</td><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1>19</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>9981  9990</td><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>9</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>9991-9995</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>4</td></tr><tr><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>9996 -9997</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>2</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>9998 9998</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1</td></tr><tr><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>9999一9999</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td></tr></table>

Assignment of trapezoidal rule iterations 1–9999 using a guided schedule with two threads.

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\openmp\page_065\openmp_page_065\auto\images\0a2c8dc6b7572e1a3de1ee99f1449280f0d60f5a9f2b9bdbbf9d501e8635334a.jpg

---

## Lecture: output\openmp\page_066\openmp_page_066\auto

# The Runtime Schedule Type

• The system uses the environment variable OMP_SCHEDULE to determine at run-time how to schedule the loop.

• The OMP_SCHEDULE environment variable can take on any of the values that can be used for a static, dynamic, or guided schedule.

---

## Lecture: output\openmp\page_067\openmp_page_067\auto

PRODUCERS AND CONSUMERS

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\openmp\page_067\openmp_page_067\auto\images\3d42f2e14cb6a5d673174843eafe0f7269f2f92c042362488d184cf5a3e25eea.jpg

---

## Lecture: output\openmp\page_068\openmp_page_068\auto

# Queues

Can be viewed as an abstraction of a line of customers waiting to pay for their groceries in a supermarket.

• A natural data structure to use in many multithreaded applications.

• For example, suppose we have several “producer” threads and several “consumer” threads.

– Producer threads might “produce” requests for data.

– Consumer threads might “consume” the request by finding or generating the requested data.

---

## Lecture: output\openmp\page_069\openmp_page_069\auto

# Message-Passing

Each thread could have a shared message queue, and when one thread wants to “send a message” to another thread, it could enqueue the message in the destination thread’s queue.

• A thread could receive a message by dequeuing the message at the head of its message queue.

---

## Lecture: output\openmp\page_070\openmp_page_070\auto

# Message-Passing

while (! Done ()) Try_receive () ;

---

## Lecture: output\openmp\page_071\openmp_page_071\auto

# Sending Messages

mes $\begin{array}{c} \begin{array} { l } { { \mathrm { ~  ~ \gamma ~ } } _ { \mathrm { ~ \tiny ~  ~ } } = { \mathrm { ~ \tiny ~ \ r a n d o m ~ } } ( { \bf \gamma } ) : \ { \mathrm { ~  ~ \gamma ~ } } _ { \mathrm { ~ \tiny ~  ~ } } } \\ { { \mathrm { ~  ~  ~ } } _ { \mathrm { ~ \tiny ~  ~ } } = { \mathrm { ~ \tiny ~ \ r a n d o m ~ } } ( { \bf \gamma } ) { \mathrm { ~ \tiny ~ \mathcal { H } _ { \mathrm { ~ \tiny ~ \ t ~ h ~ r e a d } _ { - } c o } ~ } } } \\ { { \bf g m a } { \mathrm { ~ \tiny ~ \ o m p ~ } } { \mathrm { ~ \tiny ~ c ~ r ~ i ~ t ~ i ~ c ~ a ~ l ~ } } } \\ { { \mathrm { ~ \tiny ~  ~ } } _ { \mathrm { ~ \tiny ~  ~ } } { \mathrm { ~  ~  ~ } } _ { \mathrm { ~ \tiny ~  ~ } } { \mathrm { ~  ~  ~ } } _ { \mathrm { ~ \tiny ~  ~ } } { \mathrm { ~  ~  ~ } } _ { \mathrm { ~ \tiny ~  ~ } } { \mathrm { ~  ~  ~  ~ { \bf \gamma } ~ } } _ { \mathrm { ~ \tiny ~  ~ } } { \mathrm { ~  ~  ~  ~ { \bf \gamma } ~ } } _ { \mathrm { ~ \tiny ~  ~ } } { \mathrm { ~  ~  ~  ~ { \bf \gamma } ~ } } _ { \mathrm { ~ \tiny ~  ~ } } { \mathrm { ~  ~  ~  ~ { \bf \gamma } ~ } } _ { \mathrm { ~ \tiny ~ [ ~ \Psi _ { \mathrm { ~ \tiny ~  ~ } ~ } ] ~ } } } \end{array}   \end{array}$   
des   
pra   
En

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\openmp\page_071\openmp_page_071\auto\images\09f67afdb02d9046fd0f3d4f7665b7fca8a60717609259058fb369786a50bbcc.jpg

---

## Lecture: output\openmp\page_072\openmp_page_072\auto

# Receiving Messages

if els ${ \begin{array} { r l } & { { \mathrm { ( ~ q u e ~ u e ~ e ~ s ~ i ~ z ~ e ~ = ~ 0 ~ ) } } { \mathrm { ~ r e t u r n } } } \\ & { \bullet { \mathrm { ~ i f ~ } } { \mathrm { ~ ( ~ q u e ~ u e ~ e ~ s ~ i ~ z ~ e ~ = ~ 1 ~ ) } } } \\ & { { \mathrm { p r a g m a ~ o m p ~ c ~ r ~ i ~ t ~ i ~ c ~ a ~ l ~ } } } \\ & { { \mathrm { D e ~ q u e ~ u e ~ ( ~ q u e ~ u e ~ , ~ } } { \& } { \mathrm { ~ \alpha ~ s ~ r { c } ~ , ~ } } { \& } { \mathrm { ~ \alpha ~ m } } } \\ & { \bullet } \\ & { { \mathrm { D e ~ q u e ~ u e ~ ( ~ q u e ~ u e ~ , ~ } } { \& } { \mathrm { ~ \alpha ~ s ~ r { c } ~ , ~ } } { \& } { \mathrm { ~ \alpha ~ m } } } \\ & { { \mathrm { . n t . } } { \mathrm { ~ n e s ~ s ~ a ~ g e ~ ( ~ s ~ r { c } ~ , ~ } } { \mathrm { ~ \alpha ~ n e ~ s ~ g ~ ) } } ; } \end{array} }$ sg); els

sg); Pri

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\openmp\page_072\openmp_page_072\auto\images\4ffb0bef2036cafd6bcc27c4a98c559bf1d081cdb690c16ae666e2d7c0a41044.jpg

---

## Lecture: output\openmp\page_073\openmp_page_073\auto

# Termination Detection

queue_size = enqueued - dequeued; if (queue_size == 0 && done_sending $= =$ thread_count)

return TRUE; else return FALsE;

![](images/e779f33a18a7bb5de7e327776e9cb18fd2815ffeeea894ba3d365ef809994bc0.jpg)

each thread increments this after completing its for loop

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\openmp\page_073\openmp_page_073\auto\images\e779f33a18a7bb5de7e327776e9cb18fd2815ffeeea894ba3d365ef809994bc0.jpg

---

## Lecture: output\openmp\page_074\openmp_page_074\auto

# Startup (1)

• When the program begins execution, a single thread, the master thread, will get command line arguments and allocate an array of message queues: one for each thread.

• This array needs to be shared among the threads, since any thread can send to any other thread, and hence any thread can enqueue a message in any of the queues.

---

## Lecture: output\openmp\page_075\openmp_page_075\auto

# Startup (2)

• One or more threads may finish allocating their queues before some other threads.

We need an explicit barrier so that when a thread encounters the barrier, it blocks until all the threads in the team have reached the barrier.

• After all the threads have reached the barrier all the threads in the team can proceed.

# pragma omp barrier

---

## Lecture: output\openmp\page_076\openmp_page_076\auto

# The Atomic Directive (1)

• Unlike the critical directive, it can only protect critical sections that consist of a single C assignment statement.

# pragma omp atomic

• Further, the statement must have one of the following forms:

x <op>= <expression >;   
x++;   
++x;   
x—— X;

---

## Lecture: output\openmp\page_077\openmp_page_077\auto

# The Atomic Directive (2)

• Here <op> can be one of the binary operators $* , - , / , \& , \hat { \ } , | , < < , \mathrm { o r }$

• Many processors provide a special load-modifystore instruction.

A critical section that only does a load-modifystore can be protected much more efficiently by using this special instruction rather than the constructs that are used to protect more general critical sections.

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\openmp\page_077\openmp_page_077\auto\images\f29e019d2a893a88ce0e326d283f192ff1db973855c6ab887475cac51d57b566.jpg

---

## Lecture: output\openmp\page_078\openmp_page_078\auto

# Critical Sections

• OpenMP provides the option of adding a name to a critical directive:

# pragma omp critical(name)

When we do this, two blocks protected with critical directives with different names can be executed simultaneously.

• However, the names are set during compilation, and we want a different critical section for each thread’s queue.

---

## Lecture: output\openmp\page_079\openmp_page_079\auto

# Locks

• A lock consists of a data structure and functions that allow the programmer to explicitly enforce mutual exclusion in a critical section.

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\openmp\page_079\openmp_page_079\auto\images\30029a0e7e2378ad5fa46d225b0fa324549dbd7a76c5cc5af9fff5a7c0e3e196.jpg

---

## Lecture: output\openmp\page_080\openmp_page_080\auto

# Locks

/\* Executed by one thread \*/   
Initialize the lock data structure;   
  
/\* Executed by multiple threads \*/   
Attempt to lock or set the lock data structure; Critical section;   
/\* Executed by one thread \*/   
Destroy the lock data structure;

---

## Lecture: output\openmp\page_081\openmp_page_081\auto

# Using Locks in the Message-Passing Program

![](images/315c2f4e3531560a9b989aa022478ee66ad269a6801acba47ba61bf03bbb8f13.jpg)

$$
\begin{array} { r l } & { \mathrm { ~ \ ^ { ' } ~ } \notin q _ { - } p \ = \ m s g _ { - } q u e u e s [ \ d e s t \ ] } \\ & { \mathrm { ~ \ ^ { ) } ~ } \operatorname* { m p } _ { - } s \in \mathsf { t } _ { - } 1 \circ \mathsf { c k } ( \& { q _ { - } \mathtt { p } } \mathrm { - } > 1 \circ \mathsf { c k } ) ; } \\ & { \mathrm { ~ \ } \mathrm { ~ i } \mathtt { n q u e u e } ( \mathtt { q \_ p } \mathrm { , ~ \Pi ~ } \mathfrak { m } \mathrm { y \_ r a n k \ , ~ \Pi ~ } \mathfrak { m e s } } \\ & { \mathrm { ~ \ } \mathrm { ~ ^ { ) } ~ } \operatorname* { m p } _ { - } \mathtt { u n s e t \_ l o c k } ( \& { q _ { - } \mathtt { p } } \mathrm { - } > 1 \circ \mathsf { c k } } \end{array}
$$

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\openmp\page_081\openmp_page_081\auto\images\315c2f4e3531560a9b989aa022478ee66ad269a6801acba47ba61bf03bbb8f13.jpg
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\openmp\page_081\openmp_page_081\auto\images\7c3e1d40189666ed208cedacbd56f2c58eb212e5fdf44b0d074f4e17e1df7997.jpg

---

## Lecture: output\openmp\page_082\openmp_page_082\auto

# Using Locks in the Message-Passing Program

![](images/d6a1201e6552e515067821827cfab15d210299ac834ce0369058b86893937dfd.jpg)

$\begin{array} { l } { { / { * } \quad q \mathrm { - } p \ = \ m s g \mathrm { - } q u e u e s \left[ \ m y \mathrm { - } r \mathrm { - } \right. } } \\ { { \mathrm { o m p \mathrm { - } s e t \mathrm { - } 1 0 c k } ( \& q \mathrm { \mathrm { - } p \mathrm { - } > } \mathrm { 1 } \mathrm { o c k } ) } } \\ { { \mathrm { D e q u e u e } ( \mathrm { q \mathrm { \mathrm { - } p } \ , \& x c \mathrm { ~ } \& m e s g } } } \\ { { \mathrm { o m p \mathrm { \mathrm { - } u n s e t \mathrm { - } l o c k } ( \& q \mathrm { \mathrm { - } p \mathrm { - } p \mathrm { - } > } \mathrm { 1 } \mathrm { o c } ) } } } \end{array}$ ank] \*/ ; ); );

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\openmp\page_082\openmp_page_082\auto\images\d6a1201e6552e515067821827cfab15d210299ac834ce0369058b86893937dfd.jpg
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\openmp\page_082\openmp_page_082\auto\images\e80bdc7b2f26dc9a204e6e19c5f5ac7f373286e984500d930ba169beb85dc520.jpg

---

## Lecture: output\openmp\page_083\openmp_page_083\auto

# Some Caveats

1. We shouldn’t mix the different types of mutual exclusion for a single critical section.

2. There is no guarantee of fairness in mutual exclusion constructs.

3. It can be dangerous to “nest” mutual exclusion constructs.

---

## Lecture: output\openmp\page_084\openmp_page_084\auto

# Matrix-vector multiplication

$$
y _ { i } = a _ { i 0 } x _ { 0 } + a _ { i 1 } x _ { 1 } + \cdot \cdot \cdot + a _ { i , n - 1 } x _ { n - 1 }
$$

<table><tr><td rowspan=3 colspan=1>aoo</td><td rowspan=3 colspan=1>a01</td><td rowspan=3 colspan=1></td><td rowspan=3 colspan=1>a0,n−1</td><td></td><td></td></tr><tr><td rowspan=7 colspan=1>X0x1:Xn-1</td><td></td></tr><tr><td rowspan=1 colspan=1>y0</td></tr><tr><td rowspan=1 colspan=1>a10</td><td rowspan=1 colspan=1>a11</td><td rowspan=1 colspan=1>··</td><td rowspan=1 colspan=1>a1,n−1</td><td rowspan=1 colspan=1>y1</td></tr><tr><td rowspan=1 colspan=1>·</td><td rowspan=1 colspan=1>.</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=2>ai0           ail</td><td rowspan=1 colspan=2>ai,n−1</td><td rowspan=1 colspan=1>yi = ai0x0 + ai1x1 + · · · ai,n−1Xn−1</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>am−1,0</td><td rowspan=1 colspan=1>am−1,1</td><td rowspan=1 colspan=1>··</td><td rowspan=1 colspan=1>am−1,n−1</td><td rowspan=1 colspan=1>ym-1</td></tr></table>

$$
\begin{array} { r } { \begin{array} { r l l } { \mathbf { f o r } } & { ( \mathrm { ~ i ~ \omega ~ = ~ 0 ; ~ \varepsilon ~ i ~ < ~ m ; ~ \varepsilon ~ i + + } ) } & { \{ } } \\ { \mathrm { ~ y ~ [ \varepsilon ~ i ~ ] ~ \varepsilon = ~ 0 . 0 ; ~ } } & { } \\ { \mathbf { f o r } } & { ( \mathrm { ~ j ~ = ~ 0 ; ~ \varepsilon ~ j ~ < ~ n ~ ; ~ \varepsilon ~ j + + } ) } \\ { \mathrm { ~ y ~ [ \varepsilon ~ i ~ ] ~ \varepsilon + = ~ \mathbb { A } [ \varepsilon ~ i ~ ] [ \varepsilon ~ j ] * x [ \varepsilon ~ j ~ ] ; } } \end{array}  \end{array}
$$

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\openmp\page_084\openmp_page_084\auto\images\4279d4d3a40ea80bb505cdfae8a764acb873cc420d84b62ee5c0e01c84c41d7a.jpg
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\openmp\page_084\openmp_page_084\auto\images\7fbec473702a4eaf73015fb439c3379e57b416eb00140decafd0fc91ecd25c49.jpg
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\openmp\page_084\openmp_page_084\auto\images\ce46f436be7775f0fdf979eb113c6e0a9c0752e815569111ecbfb241e77fe7ca.jpg

---

## Lecture: output\openmp\page_085\openmp_page_085\auto

# Matrix-vector multiplication

# pragma omp parallel for num_threads(thread_count) i default(none) private(i, j) shared(A, x, Y, m, n) for( $\mathrm { ~ i ~ } = \mathrm { ~ 0 ~ }$ y[i] = 0.0; Run-times and efficiencies of matrix-vector multiplication y[i] += A[i ][j]\*x[j ]; (times are in seconds)

<table><tr><td rowspan=3 colspan=1>Threads</td><td rowspan=1 colspan=6>Matrix Dimension</td></tr><tr><td rowspan=1 colspan=2>8,000,000×8</td><td rowspan=1 colspan=2>8000×8000</td><td rowspan=1 colspan=2>8×8,000,000</td></tr><tr><td rowspan=1 colspan=1>Time</td><td rowspan=1 colspan=1>Eff.</td><td rowspan=1 colspan=1>Time</td><td rowspan=1 colspan=1>Eff.</td><td rowspan=1 colspan=1>Time</td><td rowspan=1 colspan=1>Eff.</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0.322</td><td rowspan=1 colspan=1>1.000</td><td rowspan=1 colspan=1>0.264</td><td rowspan=1 colspan=1>1.000</td><td rowspan=1 colspan=1>0.333</td><td rowspan=1 colspan=1>1.000</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>0.219</td><td rowspan=1 colspan=1>0.735</td><td rowspan=1 colspan=1>0.189</td><td rowspan=1 colspan=1>0.698</td><td rowspan=1 colspan=1>0.300</td><td rowspan=1 colspan=1>0.555</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>0.141</td><td rowspan=1 colspan=1>0.571</td><td rowspan=1 colspan=1>0.119</td><td rowspan=1 colspan=1>0.555</td><td rowspan=1 colspan=1>0.303</td><td rowspan=1 colspan=1>0.275</td></tr></table>

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\openmp\page_085\openmp_page_085\auto\images\aace2859597f9b4df36424124f0e18f05cd5017c0bf3e75bfead8880528bf5f5.jpg

---

## Lecture: output\openmp\page_086\openmp_page_086\auto

int Thread-Safety int   
char \*my_token ;   
# pragma omp parallel num _threads(thread _count) default(none) private(my_rank , i, j, my_token) shared(lines, line_count) $=$   
# pragma omp for sche dule (static , 1) for $\mathrm { ~  ~ { ~ i ~ } ~ } = \mathrm { ~ \ r ~ { ~ 0 ~ } ~ }$ $>$ $=$ $\begin{array} { r l r } { \dot { ] } } & { { } = } & { 0 } \end{array}$ $=$ while(my_token $\mid =$ $=$ $=$ } /\* omp parallel \*/

---

## Lecture: output\openmp\page_087\openmp_page_087\auto

# Concluding Remarks (1)

• OpenMP is a standard for programming shared-memory systems. OpenMP uses both special functions and preprocessor directives called pragmas. OpenMP programs start multiple threads rather than multiple processes.   
• Many OpenMP directives can be modified by clauses.

---

## Lecture: output\openmp\page_088\openmp_page_088\auto

# Concluding Remarks (2)

• A major problem in the development of shared memory programs is the possibility of race conditions.

OpenMP provides several mechanisms for insuring mutual exclusion in critical sections.

– Critical directives – Named critical directives – Atomic directives – Simple locks

---

## Lecture: output\openmp\page_089\openmp_page_089\auto

# Concluding Remarks (3)

• By default most systems use a blockpartitioning of the iterations in a parallelized for loop.

• OpenMP offers a variety of scheduling options.

• In OpenMP the scope of a variable is the collection of threads to which the variable is accessible.

---

## Lecture: output\openmp\page_090\openmp_page_090\auto

# Concluding Remarks (4)

• A reduction is a computation that applies an operator to a sequence of operands to get a single result.

---

## Lecture: output\parallelComputing\page_001\parallelComputing_page_001\auto

# Introduction to High-Performance and Parallel Computing

Introduction to Parallel Computing

Slides adapted from the lecture notes by Peter Pacheco

---

## Lecture: output\parallelComputing\page_002\parallelComputing_page_002\auto

# Roadmap

• Why we need ever-increasing performance.

• Why we’re building parallel systems.

• Why we need to write parallel programs.

• How do we write parallel programs?

Concurrent, parallel, distributed!

---

## Lecture: output\parallelComputing\page_003\parallelComputing_page_003\auto

# Changing times

• From 1986 – 2002, microprocessors were speeding like a rocket, increasing in performance an average of 50% per year.

• Since then, it’s dropped to about 20% increase per year.

---

## Lecture: output\parallelComputing\page_004\parallelComputing_page_004\auto

# An intelligent solution

• Instead of designing and building faster microprocessors, put multiple processors on a single integrated circuit.

![](images/4c64dc9061f2e44dbfce472f2f17569d72b20b3bb58846d6d3a19ed1dade26a5.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\parallelComputing\page_004\parallelComputing_page_004\auto\images\4c64dc9061f2e44dbfce472f2f17569d72b20b3bb58846d6d3a19ed1dade26a5.jpg

---

## Lecture: output\parallelComputing\page_005\parallelComputing_page_005\auto

Now it’s up to the programmers

• Adding more processors doesn’t help much if programmers aren’t aware of them…

• … or don’t know how to use them.

• Serial programs don’t benefit from this approach (in most cases).

---

## Lecture: output\parallelComputing\page_006\parallelComputing_page_006\auto

# Why we need ever-increasing performance

Computational power is increasing, but so are our computation problems and needs.

• Problems we never dreamed of have been solved, such as decoding the human genome.

• More complex problems are still waiting to be solved.

---

## Lecture: output\parallelComputing\page_007\parallelComputing_page_007\auto

# Climate modeling

![](images/93010df6f68b41d26d4415456457b31da7fa2c093703d7800cb4d9f9ce451363.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\parallelComputing\page_007\parallelComputing_page_007\auto\images\93010df6f68b41d26d4415456457b31da7fa2c093703d7800cb4d9f9ce451363.jpg

---

## Lecture: output\parallelComputing\page_008\parallelComputing_page_008\auto

# Protein folding

![](images/71e218afebb2d648ea35cef1ace954b921753296f3263cc87adc930d1051c4ee.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\parallelComputing\page_008\parallelComputing_page_008\auto\images\71e218afebb2d648ea35cef1ace954b921753296f3263cc87adc930d1051c4ee.jpg

---

## Lecture: output\parallelComputing\page_009\parallelComputing_page_009\auto

# Drug discovery

-

![](images/7f8b94191e5d41b0717a3e8f1939c176a13348aeca09fb358ace79996f58bf86.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\parallelComputing\page_009\parallelComputing_page_009\auto\images\7f8b94191e5d41b0717a3e8f1939c176a13348aeca09fb358ace79996f58bf86.jpg

---

## Lecture: output\parallelComputing\page_010\parallelComputing_page_010\auto

# Energy research

![](images/ce789240eae5701e6051384f8f14282c5c8a6cd52ef69f3567ad62b6c09dc579.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\parallelComputing\page_010\parallelComputing_page_010\auto\images\ce789240eae5701e6051384f8f14282c5c8a6cd52ef69f3567ad62b6c09dc579.jpg

---

## Lecture: output\parallelComputing\page_011\parallelComputing_page_011\auto

# Data analysis

+5.000

![](images/1db03516bee93fbb422fa78ea20399138e85668817634ab5c88fd309cff3c477.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\parallelComputing\page_011\parallelComputing_page_011\auto\images\1db03516bee93fbb422fa78ea20399138e85668817634ab5c88fd309cff3c477.jpg

---

## Lecture: output\parallelComputing\page_012\parallelComputing_page_012\auto

# Why we’re building parallel systems

• Up to now, performance increases have been attributable to increasing density of transistors.

But there are inherent problems.

![](images/0d66a285d139b672162304e2f55986f7d22acd801ef818f6f43e21c6748ca8f9.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\parallelComputing\page_012\parallelComputing_page_012\auto\images\0d66a285d139b672162304e2f55986f7d22acd801ef818f6f43e21c6748ca8f9.jpg

---

## Lecture: output\parallelComputing\page_013\parallelComputing_page_013\auto

# Problem

• Denser transistors -> faster processors.   
• Faster processors -> increased power consumption.   
• Increased power consumption -> increased heat.   
• Increased heat -> unreliable processors.

---

## Lecture: output\parallelComputing\page_014\parallelComputing_page_014\auto

# Solution

• Move away from single-core systems to multicore processors.

• “core”: a processing unit

Introducing parallelism!!!

![](images/80cac2c900c39f618252fed72bde414d46859556e22b144c3759aa3b57a7ef2e.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\parallelComputing\page_014\parallelComputing_page_014\auto\images\80cac2c900c39f618252fed72bde414d46859556e22b144c3759aa3b57a7ef2e.jpg

---

## Lecture: output\parallelComputing\page_015\parallelComputing_page_015\auto

# Why we need to write parallel programs

Running multiple instances of a serial program often isn’t very useful.

• Think of running multiple instances of your favorite game.

• What you really want is for it to run faster.

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\parallelComputing\page_015\parallelComputing_page_015\auto\images\c53d814722e5e73a6eabecde0fea43ccd80c55fa7b360584f8cf984735cff0c6.jpg

---

## Lecture: output\parallelComputing\page_016\parallelComputing_page_016\auto

# Approaches to the serial problem

Rewrite serial programs so that they’re parallel.

Write translation programs that automatically convert serial programs into parallel programs.

– This is very difficult to do.   
– Success has been limited.

---

## Lecture: output\parallelComputing\page_017\parallelComputing_page_017\auto

# More problems about translation

• Some coding constructs can be recognized by an automatic program generator, and converted to a parallel construct.

• However, it’s likely that the result will be a very inefficient program.

• Sometimes the best parallel solution is to step back and devise an entirely new algorithm.

---

## Lecture: output\parallelComputing\page_018\parallelComputing_page_018\auto

# Example

• Compute n values and add them together.

Serial solution:

sum = 0;   
for (i = 0;i < n;i++) { x = Compute_next_value（. sum += x;   
}

---

## Lecture: output\parallelComputing\page_019\parallelComputing_page_019\auto

# Example (cont.)

• We have p cores, p much smaller than n.

• Each core performs a partial sum of approximately n/p values.

![](images/c1df9dc30005a98a4c9740e30690610373ea44ba871c4e1e23e9e4af6f0a2cf7.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\parallelComputing\page_019\parallelComputing_page_019\auto\images\c1df9dc30005a98a4c9740e30690610373ea44ba871c4e1e23e9e4af6f0a2cf7.jpg

---

## Lecture: output\parallelComputing\page_020\parallelComputing_page_020\auto

# Example (cont.)

After each core completes execution of the code, a private variable my_sum contains the sum of the values computed by its calls to Compute_next_value.

• Ex., 8 cores, n = 24, then the calls to Compute_next_value return:

1,4,3, 9,2,8, 5,1,1, 5,2,7, 2,5,0, 4,1,8, 6,5,1, 2,3,9

---

## Lecture: output\parallelComputing\page_021\parallelComputing_page_021\auto

# Example (cont.)

Once all the cores are done computing their private my_sum, they form a global sum by sending results to a designated “master” core which adds the final result.

---

## Lecture: output\parallelComputing\page_022\parallelComputing_page_022\auto

# Example (cont.)

if (I'm the master core) { sum = my_x; for each core other than myself f receive value from core; sum += value;   
} else { send my_x to the master;   
}

---

## Lecture: output\parallelComputing\page_023\parallelComputing_page_023\auto

# Example (cont.)

<table><tr><td rowspan=1 colspan=1>Core</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>7</td></tr><tr><td rowspan=1 colspan=1>my_sum</td><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1>19</td><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>15</td><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>13</td><td rowspan=1 colspan=1>12</td><td rowspan=1 colspan=1>14</td></tr></table>

Global sum $8 + 1 9 + 7 + 1 5 + 7 + 1 3 + 1 2 + 1 4 = 9 5$

<table><tr><td rowspan=1 colspan=1>Core</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>7</td></tr><tr><td rowspan=1 colspan=1>my_sum</td><td rowspan=1 colspan=1>95</td><td rowspan=1 colspan=1>19</td><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>15</td><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>13</td><td rowspan=1 colspan=1>12</td><td rowspan=1 colspan=1>14</td></tr></table>

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\parallelComputing\page_023\parallelComputing_page_023\auto\images\02e5ab22d55add796881781909b5a8ec9e818e5aeaba8b72b16cf672aa08b335.jpg
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\parallelComputing\page_023\parallelComputing_page_023\auto\images\29c860cb2de1f0bb07f63191650291a6543b6f53995f2d7b34da0d1ecf047b65.jpg
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\parallelComputing\page_023\parallelComputing_page_023\auto\images\cd07472c3b6039810d114cbff1158ff35a5c2a554fba11df6f42bac663d3798b.jpg

---

## Lecture: output\parallelComputing\page_024\parallelComputing_page_024\auto

# Better parallel algorithm

• Don’t make the master core do all the work.   
• Share it among the other cores.   
• Pair the cores so that core 0 adds its result with core 1’s result.   
• Core 2 adds its result with core 3’s result, etc.   
• Work with odd and even numbered pairs of cores.

---

## Lecture: output\parallelComputing\page_025\parallelComputing_page_025\auto

# Better parallel algorithm (cont.)

• Repeat the process now with only the evenly ranked cores.

• Core 0 adds result from core 2.

• Core 4 adds the result from core 6, etc.

• Now cores divisible by 4 repeat the process, and so forth, until core 0 has the final result.

---

## Lecture: output\parallelComputing\page_026\parallelComputing_page_026\auto

# Multiple cores forming a global sum

![](images/899ed7ed69e66ba967ecc7e538313f648b16381517c77ef790fc4f57b2e7fc4d.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\parallelComputing\page_026\parallelComputing_page_026\auto\images\899ed7ed69e66ba967ecc7e538313f648b16381517c77ef790fc4f57b2e7fc4d.jpg

---

## Lecture: output\parallelComputing\page_027\parallelComputing_page_027\auto

# Analysis

• In the first example, the master core performs 7 receives and 7 additions.

• In the second example, the master core performs 3 receives and 3 additions.

• The improvement is more than a factor of 2!

---

## Lecture: output\parallelComputing\page_028\parallelComputing_page_028\auto

# Analysis (cont.)

• The difference is more dramatic with a larger number of cores.   
• If we have 1000 cores: – The first example would require the master to perform 999 receives and 999 additions. – The second example would only require 10 receives and 10 additions.

• That’s an improvement of almost a factor of 100!

---

## Lecture: output\parallelComputing\page_029\parallelComputing_page_029\auto

# How do we write parallel programs?

• Task parallelism – Partition various tasks solving the problem among the cores.

Data parallelism

– Partition the data used in solving the problem among the cores.

– Each core carries out similar operations on its part of the data.

---

## Lecture: output\parallelComputing\page_030\parallelComputing_page_030\auto

# Professor P

15 questions   
300 exams

![](images/9ce8d13e1a367ef232c7911f3061d6833e3f7b9ab07c6751f4cb79c699d53bda.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\parallelComputing\page_030\parallelComputing_page_030\auto\images\9ce8d13e1a367ef232c7911f3061d6833e3f7b9ab07c6751f4cb79c699d53bda.jpg
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\parallelComputing\page_030\parallelComputing_page_030\auto\images\c13b2821d36a0a4cb69c5a055671cd80c9932c3ba01fcf59bdb5bb7b1f579451.jpg

---

## Lecture: output\parallelComputing\page_031\parallelComputing_page_031\auto

# Professor P's grading assistants

![](images/ac853b965ab02137e23f1957836a4904e3603c1374d8ce374a8d62333d04d49c.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\parallelComputing\page_031\parallelComputing_page_031\auto\images\ac853b965ab02137e23f1957836a4904e3603c1374d8ce374a8d62333d04d49c.jpg

---

## Lecture: output\parallelComputing\page_032\parallelComputing_page_032\auto

# Division of work – data parallelism

# TA#1

![](images/4487552335481c0ef5488aebe8cfe4524d8cc6ca085528dc83f426e93b28afe8.jpg)

100 exams

![](images/a9010a77a96be51d52946279d9d9d2189e6fc781b4043758bd785ccfe5660cdf.jpg)

100 exams

![](images/aea546e18a083d50ec31d8659bbdc3b98ca1f8bb3ca3ea892099803fa08f9022.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\parallelComputing\page_032\parallelComputing_page_032\auto\images\4487552335481c0ef5488aebe8cfe4524d8cc6ca085528dc83f426e93b28afe8.jpg
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\parallelComputing\page_032\parallelComputing_page_032\auto\images\a9010a77a96be51d52946279d9d9d2189e6fc781b4043758bd785ccfe5660cdf.jpg
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\parallelComputing\page_032\parallelComputing_page_032\auto\images\aea546e18a083d50ec31d8659bbdc3b98ca1f8bb3ca3ea892099803fa08f9022.jpg

---

## Lecture: output\parallelComputing\page_033\parallelComputing_page_033\auto

Division of work – task parallelism

TA#1

![](images/2c4c00d9a0844bcba9a863406300a78db2751355d908b36188459d0b8d1acbf8.jpg)

![](images/4626af3812bb130cce9311dd36bdda79669c7f9ec2611b18d3bb5e5d7cf6aad8.jpg)

TA#3

Questions 1 - 5

Questions 11 - 15

![](images/8bdff31db5209f7b1ecfe2d415b6e34d4ca5889b21343d173514da6743c53a26.jpg)

TA#2

Questions 6 - 10

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\parallelComputing\page_033\parallelComputing_page_033\auto\images\2c4c00d9a0844bcba9a863406300a78db2751355d908b36188459d0b8d1acbf8.jpg
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\parallelComputing\page_033\parallelComputing_page_033\auto\images\4626af3812bb130cce9311dd36bdda79669c7f9ec2611b18d3bb5e5d7cf6aad8.jpg
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\parallelComputing\page_033\parallelComputing_page_033\auto\images\8bdff31db5209f7b1ecfe2d415b6e34d4ca5889b21343d173514da6743c53a26.jpg

---

## Lecture: output\parallelComputing\page_034\parallelComputing_page_034\auto

# Division of work - data parallelism

sum = 0;   
for (i = 0;i < n;i++) { x = Compute_next_value ( . sum += x;   
]

---

## Lecture: output\parallelComputing\page_035\parallelComputing_page_035\auto

# Division of work – task parallelism

if (I'm the master core) { sum = my_x i for each core other than myself f receive value from core; sum $+ =$ value; Tasks send my_x to the master; 1)   
2)

Receiving Addition

---

## Lecture: output\parallelComputing\page_036\parallelComputing_page_036\auto

# Coordination

• Cores usually need to coordinate their work.

Communication – one or more cores send their current partial sums to another core.

Load balancing – share the work evenly among the cores so that one is not heavily loaded.

Synchronization – because each core works at its own pace, make sure cores do not get too far ahead of the rest.

---

## Lecture: output\parallelComputing\page_037\parallelComputing_page_037\auto

# Type of parallel systems

• Shared-memory – The cores can share access to the computer’s memory. – Coordinate the cores by having them examine and update shared memory locations.   
• Distributed-memory – Each core has its own, private memory. – The cores must communicate explicitly by sending messages across a network.

---

## Lecture: output\parallelComputing\page_038\parallelComputing_page_038\auto

# Type of parallel systems

![](images/5add3d2cf316f2adc5fa59883df0aadbe6ac93fc4aa0ea86f39ea1aa796096ce.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\parallelComputing\page_038\parallelComputing_page_038\auto\images\5add3d2cf316f2adc5fa59883df0aadbe6ac93fc4aa0ea86f39ea1aa796096ce.jpg

---

## Lecture: output\parallelComputing\page_039\parallelComputing_page_039\auto

# Terminology

Concurrent computing – In a program multiple tasks can be in progress at any instant.

Parallel computing – In a program multiple tasks cooperate closely to solve a problem.

Distributed computing – A program may need to cooperate with other programs to solve a problem.

---

## Lecture: output\parallelComputing\page_040\parallelComputing_page_040\auto

# Concluding Remarks

• Parallel systems are the trend of computing.   
• Serial programs typically don’t benefit from multiple cores.   
• Learning to write parallel programs involves learning how to coordinate the cores.   
Parallel programs are usually very complex and therefore, require sound program techniques and development.

---

## Lecture: output\parallelHardware\page_001\parallelHardware_page_001\auto

# Introduction to High-Performance and Parallel Computing

Parallel Hardware

Slides adapted from the lecture notes by Peter Pacheco

---

## Lecture: output\parallelHardware\page_002\parallelHardware_page_002\auto

![](images/d73cce4a1d0d6c362e29d76d6e135cb58a2f711d39c802ac8b896c9ee35031a3.jpg)

A programmer can write code to exploit.

PARALLEL HARDWARE

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\parallelHardware\page_002\parallelHardware_page_002\auto\images\d73cce4a1d0d6c362e29d76d6e135cb58a2f711d39c802ac8b896c9ee35031a3.jpg

---

## Lecture: output\parallelHardware\page_003\parallelHardware_page_003\auto

# Flynn’s Taxonomy

<table><tr><td colspan="2">assic Von Neumann</td></tr><tr><td>SISD Single instruction stream Single data stream</td><td>(SIMD) Single instruction stream Multiple data stream</td></tr><tr><td>MISD Multiple instruction stream</td><td>(MIMD) Multiple instruction stream</td></tr><tr><td>Single data stream not coyer</td><td>Multiple data stream</td></tr></table>

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\parallelHardware\page_003\parallelHardware_page_003\auto\images\4e7d4de54eeb3d840e45a5bdccfafaae4bde2a8d321736d2b4019939e537c2ec.jpg

---

## Lecture: output\parallelHardware\page_004\parallelHardware_page_004\auto

# SIMD

• Parallelism achieved by dividing data among the processors.

• Applies the same instruction to multiple data items.

Called data parallelism.

---

## Lecture: output\parallelHardware\page_005\parallelHardware_page_005\auto

# SIMD example

![](images/ab7b0f8c396b4dd2eb93b80250870e90ad8e51057107fcbf93db0494f0e06136.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\parallelHardware\page_005\parallelHardware_page_005\auto\images\ab7b0f8c396b4dd2eb93b80250870e90ad8e51057107fcbf93db0494f0e06136.jpg

---

## Lecture: output\parallelHardware\page_006\parallelHardware_page_006\auto

# SIMD

• What if we don’t have as many ALUs as data items? • Divide the work and process iteratively. • Ex. m = 4 ALUs and n = 15 data items.

<table><tr><td rowspan=1 colspan=1>Round3</td><td rowspan=1 colspan=1>ALU1</td><td rowspan=1 colspan=1>ALU2</td><td rowspan=1 colspan=1>ALU3</td><td rowspan=1 colspan=1>ALU4</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>×[0]</td><td rowspan=1 colspan=1>×[1]</td><td rowspan=1 colspan=1>X[2]</td><td rowspan=1 colspan=1>X[3]</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>×[4]</td><td rowspan=1 colspan=1>×[5]</td><td rowspan=1 colspan=1>×[6]</td><td rowspan=1 colspan=1>×[7]</td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>×[8]</td><td rowspan=1 colspan=1>×[9]</td><td rowspan=1 colspan=1>×[10]</td><td rowspan=1 colspan=1>X[11]</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>×[12]</td><td rowspan=1 colspan=1>X[13]</td><td rowspan=1 colspan=1>×[14]</td><td rowspan=1 colspan=1></td></tr></table>

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\parallelHardware\page_006\parallelHardware_page_006\auto\images\1fef2538b39ff8120b42fc25abca1e99c30932ece1b01b078a2ef3b8559cee26.jpg

---

## Lecture: output\parallelHardware\page_007\parallelHardware_page_007\auto

# SIMD drawbacks

• All ALUs are required to execute the same instruction, or remain idle.   
• In traditional design, they must also operate synchronously.   
• The ALUs have no instruction storage.   
Efficient for large data parallel problems, but not other types of more complex parallel problems.

---

## Lecture: output\parallelHardware\page_008\parallelHardware_page_008\auto

# Vector processors (1)

• Operate on arrays or vectors of data while conventional CPU’s operate on individual data elements or scalars.

• Vector registers – Capable of storing a vector of operands and operating simultaneously on their contents.

---

## Lecture: output\parallelHardware\page_009\parallelHardware_page_009\auto

# Vector processors (2)

• Vectorized and pipelined functional units – The same operation is applied to each element in the vector (or pairs of elements).

• Vector instructions – Operate on vectors rather than scalars.

---

## Lecture: output\parallelHardware\page_010\parallelHardware_page_010\auto

# Vector processors (3)

Interleaved memory

– Multiple “banks” of memory, which can be accessed more or less independently.

– Distribute elements of a vector across multiple banks, so reduce or eliminate delay in loading/storing successive elements.

• Strided memory access and hardware scatter/gather

– The program accesses elements of a vector located at fixed intervals.

---

## Lecture: output\parallelHardware\page_011\parallelHardware_page_011\auto

# Vector processors - Pros

• Fast.   
• Easy to use. Vectorizing compilers are good at identifying code to exploit. Compilers also can provide information about code that cannot be vectorized. – Helps the programmer re-evaluate code.   
• High memory bandwidth.   
• Uses every item in a cache line.

---

## Lecture: output\parallelHardware\page_012\parallelHardware_page_012\auto

# Vector processors - Cons

• They don’t handle irregular data structures as well as other parallel architectures.

• Limited to their ability to handle ever larger problems. (scalability)

---

## Lecture: output\parallelHardware\page_013\parallelHardware_page_013\auto

# Graphics Processing Units (GPU)

Real time graphics application programming interfaces or API’s use points, lines, and triangles to internally represent the surface of an object.

![](images/17dc06e36d2eeda7b17067e1e7030453a8e0b2dded962796aa2de122c814715a.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\parallelHardware\page_013\parallelHardware_page_013\auto\images\17dc06e36d2eeda7b17067e1e7030453a8e0b2dded962796aa2de122c814715a.jpg

---

## Lecture: output\parallelHardware\page_014\parallelHardware_page_014\auto

# GPUs

• A graphics processing pipeline converts the internal representation into an array of pixels that can be sent to a computer screen.

• Several stages of this pipeline (called shader functions) are programmable.

– Typically just a few lines of C code.

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\parallelHardware\page_014\parallelHardware_page_014\auto\images\d5a4f29fd123ed771196157277875dcfee6eced10fbadf2ab3be5eb08c87ffc0.jpg

---

## Lecture: output\parallelHardware\page_015\parallelHardware_page_015\auto

# GPUs

• Shader functions are also implicitly parallel, since they can be applied to multiple elements in the graphics stream.

GPU’s can often optimize performance by using SIMD parallelism.

• The current generation of GPU’s use SIMD parallelism.

– Although they are not pure SIMD systems.

---

## Lecture: output\parallelHardware\page_016\parallelHardware_page_016\auto

# MIMD

Supports multiple simultaneous instruction streams operating on multiple data streams.

• Typically consist of a collection of fully independent processing units or cores, each of which has its own control unit and its own ALU.

---

## Lecture: output\parallelHardware\page_017\parallelHardware_page_017\auto

# Shared Memory System (1)

• A collection of autonomous processors is connected to a memory system via an interconnection network.

• Each processor can access each memory location.

• The processors usually communicate implicitly by accessing shared data structures.

---

## Lecture: output\parallelHardware\page_018\parallelHardware_page_018\auto

# Shared Memory System (2)

• Most widely available shared memory systems use one or more multicore processors.

– (multiple CPU’s or cores on a single chip)

![](images/a9d4d66d4be771c898d91d9aed759b2fef18f550f91e91b675550c4e1aa8ae9f.jpg)

![](images/2db62cdb2c26fdef553857cb8ed49acd7931014544eb9e6b6488b30de9be83f7.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\parallelHardware\page_018\parallelHardware_page_018\auto\images\2db62cdb2c26fdef553857cb8ed49acd7931014544eb9e6b6488b30de9be83f7.jpg
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\parallelHardware\page_018\parallelHardware_page_018\auto\images\a9d4d66d4be771c898d91d9aed759b2fef18f550f91e91b675550c4e1aa8ae9f.jpg

---

## Lecture: output\parallelHardware\page_019\parallelHardware_page_019\auto

# Shared Memory System

![](images/ad946c67c68b233654121de12242974d076ee9b56cfda02eb703ffcf61ad6077.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\parallelHardware\page_019\parallelHardware_page_019\auto\images\ad946c67c68b233654121de12242974d076ee9b56cfda02eb703ffcf61ad6077.jpg

---

## Lecture: output\parallelHardware\page_020\parallelHardware_page_020\auto

# UMA multicore system

![](images/3f2dc82f0ae81d5a48a74e4b0b440c608afad042555f025d69070479b3d8f3f6.jpg)

Time to access all the memory locations is the same for all the cores.

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\parallelHardware\page_020\parallelHardware_page_020\auto\images\3f2dc82f0ae81d5a48a74e4b0b440c608afad042555f025d69070479b3d8f3f6.jpg

---

## Lecture: output\parallelHardware\page_021\parallelHardware_page_021\auto

# NUMA multicore system

![](images/327edd88d8c38b0e20aeff076c6eab82069da82dd4574f2bb19028a2b91a13ad.jpg)

A memory location a core is directly connected to can be accessed faster than a memory location that must be accessed through another chip.

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\parallelHardware\page_021\parallelHardware_page_021\auto\images\327edd88d8c38b0e20aeff076c6eab82069da82dd4574f2bb19028a2b91a13ad.jpg

---

## Lecture: output\parallelHardware\page_022\parallelHardware_page_022\auto

# Distributed Memory System

• Clusters (most popular form in practice)

– A collection of commodity systems.

– Connected by a commodity interconnection network.

Nodes of a cluster are individual computation units joined by a communication network.

---

## Lecture: output\parallelHardware\page_023\parallelHardware_page_023\auto

# Distributed Memory System

![](images/48539377fb7287f5b88eae501827138f95fd2764d6c83d31bf2f1ccab0b012b2.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\parallelHardware\page_023\parallelHardware_page_023\auto\images\48539377fb7287f5b88eae501827138f95fd2764d6c83d31bf2f1ccab0b012b2.jpg

---

## Lecture: output\parallelHardware\page_024\parallelHardware_page_024\auto

# Interconnection networks

• Affects performance of both distributed and shared memory systems.

• Two categories: – Shared memory interconnects – Distributed memory interconnects

---

## Lecture: output\parallelHardware\page_025\parallelHardware_page_025\auto

# Shared memory interconnects

Bus interconnect

– A collection of parallel communication wires together with some hardware that controls access to the bus.   
– Communication wires are shared by the devices that are connected to it.   
– As the number of devices connected to the bus increases, contention for use of the bus increases, and performance decreases.

---

## Lecture: output\parallelHardware\page_026\parallelHardware_page_026\auto

# Shared memory interconnects

Switched interconnect

– Uses switches to control the routing of data among the connected devices.

# – Crossbar –

• Allows simultaneous communication among different devices.

• Faster than buses.

• But the cost of the switches and links is relatively high.

---

## Lecture: output\parallelHardware\page_027\parallelHardware_page_027\auto

# (a) A crossbar switch connecting 4 processors (Pi) and 4 memory modules (Mj)

(b)   
Configuration of internal switches in a   
crossbar

![](images/50afb6065ee4a616ad91a404145dae85409b9f39b9a7bb4a3552363d897fcf60.jpg)

(c) Simultaneous memory accesses by the processors

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\parallelHardware\page_027\parallelHardware_page_027\auto\images\50afb6065ee4a616ad91a404145dae85409b9f39b9a7bb4a3552363d897fcf60.jpg

---

## Lecture: output\parallelHardware\page_028\parallelHardware_page_028\auto

# Distributed memory interconnects

Two groups – Direct interconnect

• Each switch is directly connected to a processor memory pair, and the switches are connected to each other.

– Indirect interconnect

• Switches may not be directly connected to a processor.

---

## Lecture: output\parallelHardware\page_029\parallelHardware_page_029\auto

# Direct interconnect

![](images/1056527cc4d47b2eba2ba1e8a1d28ed1ab51d3742968b149c5b313cdd3d9891b.jpg)  
toroidal mesh

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\parallelHardware\page_029\parallelHardware_page_029\auto\images\1056527cc4d47b2eba2ba1e8a1d28ed1ab51d3742968b149c5b313cdd3d9891b.jpg

---

## Lecture: output\parallelHardware\page_030\parallelHardware_page_030\auto

# Bisection width

• A measure of “number of simultaneous communications” or “connectivity”.

• How many simultaneous communications can take place “across the divide” between the halves?

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\parallelHardware\page_030\parallelHardware_page_030\auto\images\84a05e42d5f1ecc4a7e2b3b05ec0c0271f3306f5ad4c8d40ee5ac31f235b8b79.jpg

---

## Lecture: output\parallelHardware\page_031\parallelHardware_page_031\auto

# Two bisections of a ring

![](images/7e0cb73dd49d8fd34983b78804b958115baddd46d202d5d0a8020a44dc246c81.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\parallelHardware\page_031\parallelHardware_page_031\auto\images\7e0cb73dd49d8fd34983b78804b958115baddd46d202d5d0a8020a44dc246c81.jpg

---

## Lecture: output\parallelHardware\page_032\parallelHardware_page_032\auto

# A bisection of a toroidal mesh

---

## Lecture: output\parallelHardware\page_033\parallelHardware_page_033\auto

# Definitions

• Bandwidth – The rate at which a link can transmit data. – Usually given in megabits or megabytes per second.

• Bisection bandwidth – A measure of network quality. – Instead of counting the number of links joining the halves, it sums the bandwidth of the links.

---

## Lecture: output\parallelHardware\page_034\parallelHardware_page_034\auto

# Fully connected network

• Each switch is directly connected to every other switch.

![](images/5a7fabfdd851cdedf9330685bb6c937b23a60c051cd33cbdafe3e86b1982a811.jpg)

bisection width = p2/4

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\parallelHardware\page_034\parallelHardware_page_034\auto\images\5a7fabfdd851cdedf9330685bb6c937b23a60c051cd33cbdafe3e86b1982a811.jpg
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\parallelHardware\page_034\parallelHardware_page_034\auto\images\d5c1e25fb547aa1036b9b33af24d9c492d75ae62dd95a96335e66ba68dfbf6ce.jpg

---

## Lecture: output\parallelHardware\page_035\parallelHardware_page_035\auto

# Hypercube

• Highly connected direct interconnect.   
• Built inductively: – A one-dimensional hypercube is a fully-connecte system with two processors. – A two-dimensional hypercube is built from two one-dimensional hypercubes by joining “corresponding” switches. – Similarly a three-dimensional hypercube is built from two two-dimensional hypercubes.

---

## Lecture: output\parallelHardware\page_036\parallelHardware_page_036\auto

# Hypercubes

![](images/56e18ae050c438d2ce828ff19cdf5deeef5a3fea2a97c48858d96a76b90a5936.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\parallelHardware\page_036\parallelHardware_page_036\auto\images\56e18ae050c438d2ce828ff19cdf5deeef5a3fea2a97c48858d96a76b90a5936.jpg

---

## Lecture: output\parallelHardware\page_037\parallelHardware_page_037\auto

# Indirect interconnects

Simple examples of indirect networks:

– Crossbar – Omega network

Often shown with unidirectional links and a collection of processors, each of which has an outgoing and an incoming link, and a switching network.

---

## Lecture: output\parallelHardware\page_038\parallelHardware_page_038\auto

# A generic indirect network

![](images/e927661946e89fd0732352d703de8d07f2ec48c21fc702781bd864de054591b6.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\parallelHardware\page_038\parallelHardware_page_038\auto\images\e927661946e89fd0732352d703de8d07f2ec48c21fc702781bd864de054591b6.jpg

---

## Lecture: output\parallelHardware\page_039\parallelHardware_page_039\auto

# Crossbar interconnect for distributed memory

![](images/f22348b71c315baa257403a633f20a898830b9c1c1ee6570d3068fced34b6dd5.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\parallelHardware\page_039\parallelHardware_page_039\auto\images\f22348b71c315baa257403a633f20a898830b9c1c1ee6570d3068fced34b6dd5.jpg

---

## Lecture: output\parallelHardware\page_040\parallelHardware_page_040\auto

# An omega network

![](images/3b01a44e2860410f6444fbe90026fa51484ccad1f229c5d41b63dd7c30b65334.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\parallelHardware\page_040\parallelHardware_page_040\auto\images\3b01a44e2860410f6444fbe90026fa51484ccad1f229c5d41b63dd7c30b65334.jpg

---

## Lecture: output\parallelHardware\page_041\parallelHardware_page_041\auto

# A switch in an omega network

![](images/94393bf47e279dbfcd4bd07e6a3fb66dcc25e0473aaff92b51a81a0cc637ae80.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\parallelHardware\page_041\parallelHardware_page_041\auto\images\94393bf47e279dbfcd4bd07e6a3fb66dcc25e0473aaff92b51a81a0cc637ae80.jpg

---

## Lecture: output\parallelHardware\page_042\parallelHardware_page_042\auto

# More definitions

• About transmitting data from a source to a destination:

# Latency

– The time that elapses between the source’s beginning to transmit the data and the destination’s starting to receive the first byte.

# Bandwidth

– The rate at which the destination receives data after it has started to receive the first byte.

---

## Lecture: output\parallelHardware\page_043\parallelHardware_page_043\auto

Message transmission time = L + N / B

latency (seconds)

length of message (bytes)

bandwidth (bytes per second)

![](images/36bd529a48828d17ecb7caa7040303f7b69b6aa089e6f0fe72147f3808cdfb5d.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\parallelHardware\page_043\parallelHardware_page_043\auto\images\36bd529a48828d17ecb7caa7040303f7b69b6aa089e6f0fe72147f3808cdfb5d.jpg

---

## Lecture: output\parallelHardware\page_044\parallelHardware_page_044\auto

# Cache coherence

Programmers have no control over caches and when they get updated.

A shared memory system with two cores and two caches

![](images/2c3f97df2336fee6e5372e1c40179e1bbb525f31192f2bd07b7a23c414bccc6b.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\parallelHardware\page_044\parallelHardware_page_044\auto\images\2c3f97df2336fee6e5372e1c40179e1bbb525f31192f2bd07b7a23c414bccc6b.jpg

---

## Lecture: output\parallelHardware\page_045\parallelHardware_page_045\auto

# Cache coherence

y0 privately owned by Core 0   
y1 and z1 privately owned by Core 1

$\mathbf { x } = 2$ ; /\* shared variable \*/

<table><tr><td rowspan=1 colspan=1>Time</td><td rowspan=1 colspan=1>Core 0</td><td rowspan=1 colspan=1>Core 1</td></tr><tr><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>y0 = x;</td><td rowspan=1 colspan=1>y1 = 3*x;</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>x = 7;</td><td rowspan=1 colspan=1>Statement(s) not involving x</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>Statement(s) not involving x</td><td rowspan=1 colspan=1>z1=4*x;</td></tr></table>

$\mathbf { y 0 }$ eventually ends up = 2 y1 eventually ends up = 6 z1 = ???

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\parallelHardware\page_045\parallelHardware_page_045\auto\images\40a0204c060a4f453095f09dfa7cdb0a33dab8cb98c6ba1a31f77d9c50b654bd.jpg

---

## Lecture: output\parallelHardware\page_046\parallelHardware_page_046\auto

# Snooping Cache Coherence

• The cores share a bus .

• Any signal transmitted on the bus can be “seen” by all cores connected to the bus.

When core 0 updates the copy of x stored in its cache it also broadcasts this information across the bus.

• If core 1 is “snooping” the bus, it will see that x has been updated and it can mark its copy of x as invalid.

---

## Lecture: output\parallelHardware\page_047\parallelHardware_page_047\auto

# Directory Based Cache Coherence

• Uses a data structure called a directory that stores the status of each cache line.

• When a variable is updated, the directory is consulted, and the cache controllers of the cores that have that variable’s cache line in their caches are invalidated.

---

## Lecture: output\parallelSoftware\page_001\parallelSoftware_page_001\auto

# Introduction to High-Performance and Parallel Computing

Parallel Software

Slides adapted from the lecture notes by Peter Pacheco

---

## Lecture: output\parallelSoftware\page_002\parallelSoftware_page_002\auto

# Roadmap

• Parallel software Input and output   
Performance Parallel program design Writing and running parallel programs Concluding Remarks

---

## Lecture: output\parallelSoftware\page_003\parallelSoftware_page_003\auto

![](images/250602baeaa783e12e4e8bff984245ac05af46286c4c0a3071aa8e496e77c340.jpg)

PARALLEL SOFTWARE

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\parallelSoftware\page_003\parallelSoftware_page_003\auto\images\250602baeaa783e12e4e8bff984245ac05af46286c4c0a3071aa8e496e77c340.jpg

---

## Lecture: output\parallelSoftware\page_004\parallelSoftware_page_004\auto

# The burden is on software

• Hardware and compilers can keep up the pace needed for parallelism.

• How does parallel software work? – In shared memory programs:

• Start a single process and fork threads.

• Threads carry out tasks.

– In distributed memory programs:

• Start multiple processes.   
• Processes carry out tasks.

---

## Lecture: output\parallelSoftware\page_005\parallelSoftware_page_005\auto

SPMD – single program multiple data

A SPMD program consists of a single executable that can behave as if it were multiple different programs through the use of conditional branches.

if (I’m thread/process i) do this;   
else do that;

---

## Lecture: output\parallelSoftware\page_006\parallelSoftware_page_006\auto

# Writing Parallel Programs

1. Divide the work among the processes/threads

(a) so each process/thread gets roughly the same amount of work

(b) and communication is minimized.

double x[n], y[n]; for (i = 0; i < n; i++) x[i] += y[i];

2. Arrange for the processes/threads to synchronize.

3. Arrange for communication among processes/threads.

---

## Lecture: output\parallelSoftware\page_007\parallelSoftware_page_007\auto

# Shared Memory

Dynamic threads

– Master thread waits for work, forks new threads, and when threads are done, they terminate – Efficient use of resources, but thread creation and termination is time consuming.

Static threads   
– Pool of threads created and are allocated work, but do not terminate until cleanup.   
– Better performance, but potential waste of system resources.

---

## Lecture: output\parallelSoftware\page_008\parallelSoftware_page_008\auto

# Nondeterminism

printf ( "Thread %d > my_val = %d\n" , my_rank , my_x ) ;

![](images/fd2002f0c5d78df0f8f0982053020bcb26d7636228381594cc767d46154cb30f.jpg)

![](images/e4c09726cde3db1b9b1c307d6ebc85a39ebc5e5985e3b88cbd8221fa22383c6a.jpg)

Thread 0 > my_val = 7   
Thread 1 > my_val = 19   
Thread 1 > my_val = 19   
Thread 0 > my_val = 7

The same input can result in different output.

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\parallelSoftware\page_008\parallelSoftware_page_008\auto\images\e4c09726cde3db1b9b1c307d6ebc85a39ebc5e5985e3b88cbd8221fa22383c6a.jpg
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\parallelSoftware\page_008\parallelSoftware_page_008\auto\images\fd2002f0c5d78df0f8f0982053020bcb26d7636228381594cc767d46154cb30f.jpg

---

## Lecture: output\parallelSoftware\page_009\parallelSoftware_page_009\auto

# Race Condition

my_val = Compute_val ( my_rank ) ;   
x += my_val ;

<table><tr><td rowspan=1 colspan=1>Time</td><td rowspan=1 colspan=1>Core 0</td><td rowspan=1 colspan=1>Core 1</td></tr><tr><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>Finish assignment to my-val</td><td rowspan=1 colspan=1>In call to Compute_val</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>Load x = 0 into register</td><td rowspan=1 colspan=1>Finish assignment to my_val</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>Load my_val = 7 into register</td><td rowspan=1 colspan=1>Load x = 0 into register</td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>Add my_val = 7 to x</td><td rowspan=1 colspan=1>Load my_val = 19 into register</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>Store x = 7</td><td rowspan=1 colspan=1>Add my-val to x</td></tr><tr><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>Start other work</td><td rowspan=1 colspan=1>Store x = 19</td></tr></table>

The output depends on the timing of concurrent execution.

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\parallelSoftware\page_009\parallelSoftware_page_009\auto\images\e71ca36d969b0ce6ba8605285fc5aebdfed0b98f942e9bdd18769aee192b26b1.jpg

---

## Lecture: output\parallelSoftware\page_010\parallelSoftware_page_010\auto

# Critical Section

• Programmer’s job to ensure mutually exclusive access to the critical section

– Mutual exclusion lock (mutex, or simply lock)

my_val = Compute_val ( my_rank ) ;   
Lock(&add_my_val_lock ) ;   
x += my_val ;   
Unlock(&add_my_val_lock ) ;

A block of code that can only be executed by one thread at a time.

---

## Lecture: output\parallelSoftware\page_011\parallelSoftware_page_011\auto

# busy-waiting

my_val = Compute_val ( my_rank ) ; i f ( my_rank == 1)

whi l e ( ! ok_for_1 ) ; /\* Busy−wait loop \*/   
x += my_val ; /\* Critical section \*/   
i f ( my_rank == 0) ok_for_1 = true ; /\* Let thread 1 update x \*/

---

## Lecture: output\parallelSoftware\page_012\parallelSoftware_page_012\auto

message-passing program example char message [ 1 0 0 ] ;

my_rank = Get_rank ( ) ;

i f ( my_rank == 1) {

sprintf ( message , "Greetings from process 1" ) ;

Send ( message , MSG_CHAR , 100 , 0 ) ;

} e l s e i f ( my_rank == 0) {

Receive ( message , MSG_CHAR , 100 , 1 ) ;

printf ( "Process 0 > Received: %s\n" , message ) ; }

---

## Lecture: output\parallelSoftware\page_013\parallelSoftware_page_013\auto

# Notes on the message-passing program

• It is SPMD. The two processes are using the same executable.

• The variable message refers to memory blocks in different processes.

• Process 0 is able to write to stdout.

• Typically both Send and Receive may block until the message is sent/received.

• There are other MPI API functions.

---

## Lecture: output\parallelSoftware\page_014\parallelSoftware_page_014\auto

# Input and Output

• In distributed memory programs, only process 0 will access stdin. In shared memory programs, only the master thread or thread 0 will access stdin.

• In both distributed memory and shared memory programs all the processes/threads can access stdout and stderr.

---

## Lecture: output\parallelSoftware\page_015\parallelSoftware_page_015\auto

# Input and Output

• However, because of the indeterminacy of the order of output to stdout, in most cases only a single process/thread will be used for all output to stdout other than debugging output.

• Debug output should always include the rank or id of the process/thread that’s generating the output.

---

## Lecture: output\parallelSoftware\page_016\parallelSoftware_page_016\auto

# Input and Output

Only a single process/thread will attempt to access any single file other than stdin, stdout, or stderr. So, for example, each process/thread can open its own, private file for reading or writing, but no two processes/threads will open the same file.

---

## Lecture: output\parallelSoftware\page_017\parallelSoftware_page_017\auto

# PERFORMANCE

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\parallelSoftware\page_017\parallelSoftware_page_017\auto\images\9976c8de25abbc3f753cf818548721ee5981042db3809c71d638c03e51bca0af.jpg

---

## Lecture: output\parallelSoftware\page_018\parallelSoftware_page_018\auto

# Speedup of a parallel program

• Number of cores = p • Serial run-time = Tserial • Parallel run-time = Tparallel

![](images/5f6ad4e7b58508d0e521fd0b8f4f8e8a3db1bb817d9dd4c4acfbaf9cd08ff266.jpg)

S = Tserial T Tparallel = Tserial / p parallel

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\parallelSoftware\page_018\parallelSoftware_page_018\auto\images\5f6ad4e7b58508d0e521fd0b8f4f8e8a3db1bb817d9dd4c4acfbaf9cd08ff266.jpg

---

## Lecture: output\parallelSoftware\page_019\parallelSoftware_page_019\auto

# Efficiency of a parallel program

![](images/5d90a4d3520731b929244310468c0fae801632a190f6c581eaa098fa30f49294.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\parallelSoftware\page_019\parallelSoftware_page_019\auto\images\5d90a4d3520731b929244310468c0fae801632a190f6c581eaa098fa30f49294.jpg

---

## Lecture: output\parallelSoftware\page_020\parallelSoftware_page_020\auto

# Speedup and efficiency example

<table><tr><td rowspan=1 colspan=1>P</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1>16</td></tr><tr><td rowspan=1 colspan=1>S</td><td rowspan=1 colspan=1>1.0</td><td rowspan=1 colspan=1>1.9</td><td rowspan=1 colspan=1>3.6</td><td rowspan=1 colspan=1>6.5</td><td rowspan=1 colspan=1>10.8</td></tr><tr><td rowspan=1 colspan=1>E =S/p</td><td rowspan=1 colspan=1>1.0</td><td rowspan=1 colspan=1>0.95</td><td rowspan=1 colspan=1>0.90</td><td rowspan=1 colspan=1>0.81</td><td rowspan=1 colspan=1>0.68</td></tr></table>

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\parallelSoftware\page_020\parallelSoftware_page_020\auto\images\d2404f76564193277041e275349b6315b303be74e89243f2d74ad8d475936ec7.jpg

---

## Lecture: output\parallelSoftware\page_021\parallelSoftware_page_021\auto

Speedups and efficiencies of parallel program on different problem sizes

<table><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>P</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1>16</td></tr><tr><td rowspan=2 colspan=1>Half</td><td rowspan=1 colspan=1>S</td><td rowspan=1 colspan=1>1.0</td><td rowspan=1 colspan=1>1.9</td><td rowspan=1 colspan=1>3.1</td><td rowspan=1 colspan=1>4.8</td><td rowspan=1 colspan=1>6.2</td></tr><tr><td rowspan=1 colspan=1>E</td><td rowspan=1 colspan=1>1.0</td><td rowspan=1 colspan=1>0.95</td><td rowspan=1 colspan=1>0.78</td><td rowspan=1 colspan=1>0.60</td><td rowspan=1 colspan=1>0.39</td></tr><tr><td rowspan=2 colspan=1>Original</td><td rowspan=1 colspan=1>S</td><td rowspan=1 colspan=1>1.0</td><td rowspan=1 colspan=1>1.9</td><td rowspan=1 colspan=1>3.6</td><td rowspan=1 colspan=1>6.5</td><td rowspan=1 colspan=1>10.8</td></tr><tr><td rowspan=1 colspan=1>E</td><td rowspan=1 colspan=1>1.0</td><td rowspan=1 colspan=1>0.95</td><td rowspan=1 colspan=1>0.90</td><td rowspan=1 colspan=1>0.81</td><td rowspan=1 colspan=1>0.68</td></tr><tr><td rowspan=2 colspan=1>Double</td><td rowspan=1 colspan=1>S</td><td rowspan=1 colspan=1>1.0</td><td rowspan=1 colspan=1>1.9</td><td rowspan=1 colspan=1>3.9</td><td rowspan=1 colspan=1>7.5</td><td rowspan=1 colspan=1>14.2</td></tr><tr><td rowspan=1 colspan=1>E</td><td rowspan=1 colspan=1>1.0</td><td rowspan=1 colspan=1>0.95</td><td rowspan=1 colspan=1>0.98</td><td rowspan=1 colspan=1>0.94</td><td rowspan=1 colspan=1>0.89</td></tr></table>

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\parallelSoftware\page_021\parallelSoftware_page_021\auto\images\8cd6d14048e966c72d79f385a8a18b86159f79a3fceec58f52eee92390bcaa6b.jpg

---

## Lecture: output\parallelSoftware\page_022\parallelSoftware_page_022\auto

# Example Speedup Figure

![](images/eecc6a39083d0c52fc3a03e062e859e3870cfb98e6fd7a92ea6eec29e3a9161e.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\parallelSoftware\page_022\parallelSoftware_page_022\auto\images\eecc6a39083d0c52fc3a03e062e859e3870cfb98e6fd7a92ea6eec29e3a9161e.jpg

---

## Lecture: output\parallelSoftware\page_023\parallelSoftware_page_023\auto

# Example Efficiency Figure

![](images/aadd244cf3402d1a3a161d4694985dc51de8ca874d1e95c8630f7f81fd0853aa.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\parallelSoftware\page_023\parallelSoftware_page_023\auto\images\aadd244cf3402d1a3a161d4694985dc51de8ca874d1e95c8630f7f81fd0853aa.jpg

---

## Lecture: output\parallelSoftware\page_024\parallelSoftware_page_024\auto

Parallel program overhead

Tparallel = Tserial / p + Toverhead

---

## Lecture: output\parallelSoftware\page_025\parallelSoftware_page_025\auto

# Amdahl’s Law

Unless virtually all of a serial program is parallelized, the possible speedup is going to be very limited — regardless of the number of cores available.

p: number of cores; f: fraction of the serial time that the parallelizable part takes

Tserial Speedup = = f x Tserial / p + (1-f) x Tserial 1 - f + f/p

---

## Lecture: output\parallelSoftware\page_026\parallelSoftware_page_026\auto

# Example

• We can parallelize 90% of a serial program.

• Parallelization is “perfect” regardless of the number of cores p we use.

Tserial = 20 seconds

• Parallel runtime of parallelizable part is

---

## Lecture: output\parallelSoftware\page_027\parallelSoftware_page_027\auto

# Example (cont.)

Runtime of “unparallelizable” part is

0.1 x T serial = 2

• Overall parallel run-time is

Tparallel = 0.9 x Tserial / p + 0.1 x Ts erial = 18 / p + 2

---

## Lecture: output\parallelSoftware\page_028\parallelSoftware_page_028\auto

# Example (cont.)

Speedup

Tserial 20 S 0.9 x Tserial / p + 0.1 x Tserial 18 / p + 2

---

## Lecture: output\parallelSoftware\page_029\parallelSoftware_page_029\auto

# Scalability

• In general, a program is scalable if it can handle ever increasing problem sizes.

• If we increase the number of processes/threads and keep the efficiency fixed without increasing problem size, the problem is strongly scalable.

If we keep the efficiency fixed by increasing the problem size at the same rate as we increase the number of processes/threads, the problem is weakly scalable.

---

## Lecture: output\parallelSoftware\page_030\parallelSoftware_page_030\auto

# Time Measurement

• Wall clock time • CPU time (reported by c function clock) ? • Start to finish (Unix shell command time)? • A program segment of interest?

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\parallelSoftware\page_030\parallelSoftware_page_030\auto\images\b5970e0086933a26af4ab9430cb55312bf07f528b0737d440565ba7ca2da73a7.jpg

---

## Lecture: output\parallelSoftware\page_031\parallelSoftware_page_031\auto

# Measure Elapsed Time

![](images/78c5807a2dcd6a7671595149958f4e13d545028b5a70e0640f382d1942ceff1a.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\parallelSoftware\page_031\parallelSoftware_page_031\auto\images\78c5807a2dcd6a7671595149958f4e13d545028b5a70e0640f382d1942ceff1a.jpg

---

## Lecture: output\parallelSoftware\page_032\parallelSoftware_page_032\auto

# Taking Timings in Parallel Programs

# private

Houble start , finish;

start $=$ Get_current_time (); /\* Code that we want to time \*/

finish $=$ Get_current_time ();

rintf("The elapsed time $=$ %e seconds $:$ n" , finish—start );

---

## Lecture: output\parallelSoftware\page_033\parallelSoftware_page_033\auto

# Elapsed Time in Parallel Programs

shared double global_elapsed;   
private double my_start , my_finish , my_elapsed;   
/\* Synchronize all processes/threads \*/ Barrier（);   
my_start $=$ Get_current_time （);

/\* Code that we want to time \*/

my_finish $=$ Get_current_time ();   
my_elapsed $=$ my_finish — my_start ;   
/\* Find the max across all processes/threads \*/   
global_elapsed $=$ Global_max(my_elapsed);   
if (my_rank == 0) printf("The elapsed time $=$ %e seconds $\backprime$ n", global_elapsed);

---

## Lecture: output\parallelSoftware\page_034\parallelSoftware_page_034\auto

# PARALLEL PROGRAM DESIGN

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\parallelSoftware\page_034\parallelSoftware_page_034\auto\images\3d1b1ba6312094d647de005c7cb1014fcaed9301e1a2fc23fe9ca5935382e617.jpg

---

## Lecture: output\parallelSoftware\page_035\parallelSoftware_page_035\auto

# Foster’s methodology

Partitioning: divide the computation to be performed and the data operated on by the computation into small tasks.

The focus here should be on identifying tasks that can be executed in parallel.

---

## Lecture: output\parallelSoftware\page_036\parallelSoftware_page_036\auto

# Foster’s methodology

Communication: determine what communication needs to be carried out among the tasks identified in the previous step.

---

## Lecture: output\parallelSoftware\page_037\parallelSoftware_page_037\auto

# Foster’s methodology

● Agglomeration or aggregation: combine tasks and communications identified in the first step into larger tasks.

For example, if task A must be executed before task B can be executed, it may make sense to aggregate them into a single composite task.

---

## Lecture: output\parallelSoftware\page_038\parallelSoftware_page_038\auto

# Foster’s methodology

4. Mapping: assign the composite tasks identified in the previous step to processes/threads.

This should be done so that communication is minimized, and each process/thread gets roughly the same amount of work.

---

## Lecture: output\parallelSoftware\page_039\parallelSoftware_page_039\auto

# Example – histogram building

1.3, 2.9, 0.4, 0.3, 1.3, 4.4, 1.7, 0.4, 3.2, 0.3,   
4.9, 2.4, 3.1, 4.4, 3.9, 0.4, 4.2, 4.5, 4.9, 0.9

![](images/0f1a64a825fe905b19e6d31c3667689f3e233d7b9e339c5fff7d1902c6ea7a18.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\parallelSoftware\page_039\parallelSoftware_page_039\auto\images\0f1a64a825fe905b19e6d31c3667689f3e233d7b9e339c5fff7d1902c6ea7a18.jpg

---

## Lecture: output\parallelSoftware\page_040\parallelSoftware_page_040\auto

# Serial program - input

1. The number of measurements: data_count

2. An array of data_count floats: data

3. The minimum value for the bin containing the smallest values: min_meas

4. The maximum value for the bin containing the largest values: max_meas

5. The number of bins: bin_count

---

## Lecture: output\parallelSoftware\page_041\parallelSoftware_page_041\auto

# Serial program - output

1. bin_maxes : an array of bin_count floats

2. bin_counts : an array of bin_count ints

---

## Lecture: output\parallelSoftware\page_042\parallelSoftware_page_042\auto

# First two stages of Foster's Methodology

Find_bin .. data [i-1] data[i] data [i + 1] ···   
icrement ● bin_counts[b-1]++ bin_counts[b]++   
in_counts

---

## Lecture: output\parallelSoftware\page_043\parallelSoftware_page_043\auto

# Alternative definition of tasks and communication

![](images/304a839f2730769a32eb1a265350efe9aefa9cd2a1a563b30c9152638224e473.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\parallelSoftware\page_043\parallelSoftware_page_043\auto\images\304a839f2730769a32eb1a265350efe9aefa9cd2a1a563b30c9152638224e473.jpg

---

## Lecture: output\parallelSoftware\page_044\parallelSoftware_page_044\auto

# Adding the local arrays

![](images/d9032fe2e260e3cffdd4275a3fa6a5e1bb993c7ae4b3996a400dd4ede24cdd07.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\parallelSoftware\page_044\parallelSoftware_page_044\auto\images\d9032fe2e260e3cffdd4275a3fa6a5e1bb993c7ae4b3996a400dd4ede24cdd07.jpg

---

## Lecture: output\parallelSoftware\page_045\parallelSoftware_page_045\auto

# Concluding Remarks (1)

• Serial systems – The standard model of computer hardware has been the von Neumann architecture.

Parallel hardware – Flynn’s taxonomy.

Parallel software – We focus on software for homogeneous MIMD systems, consisting of a single program that obtains parallelism by branching (SPMD).

---

## Lecture: output\parallelSoftware\page_046\parallelSoftware_page_046\auto

# Concluding Remarks (2)

Input and Output

– We’ll write programs in which one process or thread can access stdin, and all processes can access stdout and stderr.

– However, because of nondeterminism, except for debug output we’ll usually have a single process or thread accessing stdout.

---

## Lecture: output\parallelSoftware\page_047\parallelSoftware_page_047\auto

# Concluding Remarks (3)

Performance – Speedup – Efficiency – Amdahl’s law – Scalability • Parallel Program Design – Foster’s methodology

---

## Lecture: output\parallel_reduce\page_001\parallel_reduce_page_001\auto

# Parallel Programming

Data-Parallel Primitives: Reduction

---

## Lecture: output\parallel_reduce\page_002\parallel_reduce_page_002\auto

# Overview

• The Reduction Operation • Sequential Implementation • Baseline Reduction Kernel • Improved Reduction Kernel

---

## Lecture: output\parallel_reduce\page_003\parallel_reduce_page_003\auto

# Reduce (Reduction)

• A commonly used strategy for processing large input data sets

• There is no required order of processing elements in a data set (associative and commutative)

– Partition the data set into smaller chunks   
– Have each thread to process a chunk   
– Use a reduction tree to summarize the results from each chunk into the final answer

• Google and Hadoop MapReduce frameworks support this strategy

---

## Lecture: output\parallel_reduce\page_004\parallel_reduce_page_004\auto

# Reduction in Other Parallel Operations

• Reduction is also needed to clean up after some commonly used transformations

Privatization   
– Multiple threads write into an output location   
– Replicate the output location so that each thread has a private output location   
– Use a reduction tree to combine the values of private locations into the original output location

---

## Lecture: output\parallel_reduce\page_005\parallel_reduce_page_005\auto

# Computation used in Reduction

• Summarize a set of input values into one value using a “reduction operation”

– Max   
– Min   
– Sum   
– Product   
– User defined reduction operation function as long as the operation

• Is associative and commutative • Has a well-defined identity value (e.g., 0 for sum)

---

## Lecture: output\parallel_reduce\page_006\parallel_reduce_page_006\auto

# Sequential Reduction

• Initialize the result as an identity value for the reduction operation

– Smallest possible value for max reduction – Largest possible value for min reduction – 0 for sum reduction   
– 1 for product reduction

• Iterate through the input and perform the reduction operation between the result value and the current input value

– N reduction operations performed for N input values

---

## Lecture: output\parallel_reduce\page_007\parallel_reduce_page_007\auto

# A Reduction Tree

![](images/ebdb22b9600535bbb48b2fb52897f25b580992666d9b223ad2359887cbad6aff.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\parallel_reduce\page_007\parallel_reduce_page_007\auto\images\ebdb22b9600535bbb48b2fb52897f25b580992666d9b223ad2359887cbad6aff.jpg

---

## Lecture: output\parallel_reduce\page_008\parallel_reduce_page_008\auto

# Analysis of Reduction Tree

• For N input values, the reduction tree performs

(1/2)N + (1/ $4 ) \mathsf { N } + ( 1 / 8 ) \mathsf { N } + \ldots 1 = ( 1 - ( 1 / \mathsf { N } ) ) \mathsf { N } = \mathsf { N } { - } 1$ operations

• In Log (N) steps – 1,000,000 input values take 20 steps – Assuming that we have enough execution resources

• Average Parallelism (N-1)/Log(N))

– For N = 1,000,000, average parallelism is 50,000 – However, peak resource requirement is 500,000! – This is not resource efficient.

• This is a work-efficient parallel algorithm – The amount of work done is comparable to sequential – Many parallel algorithms are not work efficient

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\parallel_reduce\page_008\parallel_reduce_page_008\auto\images\f28927f42771252dc7e1c0a16652e57fce1642aa387d1dbf237006c822b78fd8.jpg

---

## Lecture: output\parallel_reduce\page_009\parallel_reduce_page_009\auto

# Parallel Implementation

Parallel execution of reduction tree – Add two values per thread in each step – Halve # of threads for next step – Takes log(n) steps for n elements – Requires n/2 threads at most in a step • In-place reduction using shared memory – The original vector is in device global memory The shared memory is used to hold a partial sum vector Each step brings the partial sum vector closer to the sum – The final sum will be in element 0 – Reduces global memory traffic due to partial sum values $\scriptstyle \ n < = 2 0 4 8$ for current GPU due to limit of number of threads per SM

---

## Lecture: output\parallel_reduce\page_010\parallel_reduce_page_010\auto

# Example of Parallel Reduction

![](images/2734e204803102c4a49c0a5c7cb101a52784453c55e5269146156220e6769e36.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\parallel_reduce\page_010\parallel_reduce_page_010\auto\images\2734e204803102c4a49c0a5c7cb101a52784453c55e5269146156220e6769e36.jpg

---

## Lecture: output\parallel_reduce\page_011\parallel_reduce_page_011\auto

# Baseline Thread-to-Data Mapping

• Each thread is responsible for an even-index location of the partial sum vector

– In each step, one of the input is always from the location of responsibility

– The other input comes from an increasing distance away

• After each step, half of the threads are no longer needed

---

## Lecture: output\parallel_reduce\page_012\parallel_reduce_page_012\auto

# Simple Thread Block Design

• Each thread block takes 2\* BlockDim.x input elements

• Each thread loads 2 elements into shared memory

shared__ float partialSum[2\*BLOCK_SIZE];   
unsigned int t = threadIdx.x;   
unsigned int start = 2\*blockIdx.x\*blockDim.x;   
p $\mathsf { a r t i a l S u m [ t ] } = \mathsf { i n p u t [ s t a r t + t ] } ;$   
partialSum[blockDim.x+t] = input[start + blockDim

---

## Lecture: output\parallel_reduce\page_013\parallel_reduce_page_013\auto

# Reduction

for (unsigned int stride = 1; stride <=   
blockDim.x; stride \*= 2)   
{

syncthreads(); if (t % stride == 0)

partialSum[2\*t]+=partialSum[2\*t+stride]; }

---

## Lecture: output\parallel_reduce\page_014\parallel_reduce_page_014\auto

# Synchronization Barrier

_syncthreads() is needed to ensure that all elements of each version of partial sums have been generated before we proceed to the next step

---

## Lecture: output\parallel_reduce\page_015\parallel_reduce_page_015\auto

# Finishing Up Reduction

At the end of the kernel, Thread 0 in each thread block writes the sum of the thread block in partialSum[0] into a vector indexed by the blockIdx.x

There can be a large number of such sums if the original input array for reduction is very large – The host code may iterate and launch another kernel • If there are only a small number of sums, the host can simply transfer the data back and add them together.

---

## Lecture: output\parallel_reduce\page_016\parallel_reduce_page_016\auto

# Problems in the Simple Reduction Kernel

In each iteration, two control flow paths will   
be sequentially traversed for each warp   
– Threads that perform addition and threads that do not – Threads that do not perform addition still consume execution resources

---

## Lecture: output\parallel_reduce\page_017\parallel_reduce_page_017\auto

# Problems in the Simple Reduction Kernel

• Half or fewer of threads will be executing after the first step

– All odd-index threads are disabled after first step – After the 5th step, entire warps in each block will fail the if test, poor resource utilization but no divergence.

– This can go on for a while, up to 6 more steps (stride = 32, 64, 128, 256, 512, 1024), where each active warp only has one productive thread until all warps in a block retire

---

## Lecture: output\parallel_reduce\page_018\parallel_reduce_page_018\auto

# Thread Index Usage Matters

• In some algorithms, one can shift the index usage to improve the divergence behavior – Commutative and associative operators

• Always compact the partial sums into the front locations in the partialSum[] array • Keep the active threads consecutive

---

## Lecture: output\parallel_reduce\page_019\parallel_reduce_page_019\auto

# An Example of Four Threads

Thread 0 Thread 1 Thread 2 Thread 3   

<table><tr><td rowspan=1 colspan=2>3</td><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>3</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=2>7</td><td rowspan=1 colspan=2>2</td><td rowspan=1 colspan=1>13</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=2>20</td><td rowspan=1 colspan=2>5</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=2>25</td><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=2></td><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr></table>

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\parallel_reduce\page_019\parallel_reduce_page_019\auto\images\bdb6683525f5fc5816a24bc4aa1c31cf8253d8e6731f3193788b30849960b504.jpg

---

## Lecture: output\parallel_reduce\page_020\parallel_reduce_page_020\auto

# A Better Reduction Kernel

for (unsigned int stride = blockDim.x; stride > 0; stride /= 2)   
{ __syncthreads(); if (t < stride) partialSum[t] += partialSum[t+stride];   
}

---

## Lecture: output\parallel_reduce\page_021\parallel_reduce_page_021\auto

# Analysis on the Better Kernel

• For a 1024 thread block – No divergence in the first 5 steps

• 1024, 512, 256, 128, 64, 32 consecutive threads are active in each step

• All threads in each warp either all active or all inactive

– The final 5 steps will still have divergence

---

## Lecture: output\parallel_reduce\page_022\parallel_reduce_page_022\auto

# Summary

• Reduction or reduce is also a data-parallel primitive   
Sequential implementation is of O(n) time complexity   
• Parallel reduction tree algorithm is work efficient   
• Thread index mapping improves reduction kernel performance

---

## Lecture: output\TreeSearch\page_001\TreeSearch_page_001\auto

# TREE SEARCH

![](images/6a3be2f41508e1d820bd8daff871c3dc0017f5e011a6f915d0908d25153bb03a.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\TreeSearch\page_001\TreeSearch_page_001\auto\images\6a3be2f41508e1d820bd8daff871c3dc0017f5e011a6f915d0908d25153bb03a.jpg

---

## Lecture: output\TreeSearch\page_002\TreeSearch_page_002\auto

# Traveling Salesman Problem

Finding a minimum cost tour.

An NP-complete problem.

No known solution to TSP that is better in all cases than exhaustive search.

---

## Lecture: output\TreeSearch\page_003\TreeSearch_page_003\auto

# A Four-City TSP

![](images/08bd51a603603134d6ca9d31c80bd0cf101d6aa762e701fb92e92ebd7e7276c8.jpg)

![](images/a45716d10cc55398b319f7813ecbd7a0fbebd8ec0ccebdd7389cdfb818e40310.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\TreeSearch\page_003\TreeSearch_page_003\auto\images\08bd51a603603134d6ca9d31c80bd0cf101d6aa762e701fb92e92ebd7e7276c8.jpg
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\TreeSearch\page_003\TreeSearch_page_003\auto\images\a45716d10cc55398b319f7813ecbd7a0fbebd8ec0ccebdd7389cdfb818e40310.jpg

---

## Lecture: output\TreeSearch\page_004\TreeSearch_page_004\auto

# Search Tree for Four-City TSP

![](images/983d872656d068b2e401b195d1307b4ff21bd3d0cae5c28eb1a9aa6dacbd37c8.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\TreeSearch\page_004\TreeSearch_page_004\auto\images\983d872656d068b2e401b195d1307b4ff21bd3d0cae5c28eb1a9aa6dacbd37c8.jpg

---

## Lecture: output\TreeSearch\page_005\TreeSearch_page_005\auto

# Pseudo-code for a recursive solution to TSP using depth-first search

void Depth_first_search(tour_t tour) { if (Best_tour(tour)) Update_best_tour(tour); $\}$ else{ Depth_first_search(tour); Remove_last_city(tour); }

---

## Lecture: output\TreeSearch\page_006\TreeSearch_page_006\auto

# Pseudo-code for an implementation of a depth-first solution to TSP without recursion

while (!Empty(stack)) { $=$ Pop(stack); if(city $=$ NO_CITY) // End of child list , else { if (Best_tour(curr_tour)) Update_best_tour(curr_tour); $\}$ else{ for (nbr = n−l; nbr $> = 1$ } /\* if Feasible \*/   
} /\* while !Empty \*/

---

## Lecture: output\TreeSearch\page_007\TreeSearch_page_007\auto

# Pseudo-code for a second solution to TSP that

# doesn’t use recursion

while (! Empty(stack )) { $\}$ else{ for (nbr = n−l; nbr $> = 1$ }

---

## Lecture: output\TreeSearch\page_008\TreeSearch_page_008\auto

# Using pre-processor macros

/\* Find the ith city on the partial tour \*/   
int Tour_city(tour_t tour, int i) $\{$ return tour->cities[i];   
$\}$ /\* Tour_city \*/

![](images/b000c14df563cd06a0e60219c69dc8acd880c5aaa9ef3a0b960ea535584b7844.jpg)

/\* Find the ith city on the partial tour \*/

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\TreeSearch\page_008\TreeSearch_page_008\auto\images\b000c14df563cd06a0e60219c69dc8acd880c5aaa9ef3a0b960ea535584b7844.jpg

---

## Lecture: output\TreeSearch\page_009\TreeSearch_page_009\auto

# Run-Times of the Three Serial

# Implementations of Tree Search

<table><tr><td rowspan=1 colspan=1>Recursive</td><td rowspan=1 colspan=1>First Iterative</td><td rowspan=1 colspan=1>Second Iterative</td></tr><tr><td rowspan=1 colspan=1>30.5</td><td rowspan=1 colspan=1>29.2</td><td rowspan=1 colspan=1>32.9</td></tr></table>

(in seconds)

The digraph contains 15 cities.

All three versions visited approximately 95,000,000 tree nodes.

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\TreeSearch\page_009\TreeSearch_page_009\auto\images\cd6a8fd32145373dd6c6babfa19778081f06b769cbafef91d63864f94574a864.jpg
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\TreeSearch\page_009\TreeSearch_page_009\auto\images\fec444ec53793fdbfef7180b0772d0c5c025821e40a8749f719e0ee63fc142bd.jpg

---

## Lecture: output\TreeSearch\page_010\TreeSearch_page_010\auto

# Making sure we have the “best tour” (1)

When a process finishes a tour, it needs to check if it has a better solution than recorded so far.

The global Best_tour function only reads the global best cost, so we don’t need to tie it up by locking it. There’s no contention with other readers.

If the process does not have a better solution, then it does not attempt an update.

---

## Lecture: output\TreeSearch\page_011\TreeSearch_page_011\auto

# Making sure we have the “best tour” (2)

If another thread is updating while we read, we may see the old value or the new value.

The new value is preferable, but to ensure this would be more costly than it is worth.

---

## Lecture: output\TreeSearch\page_012\TreeSearch_page_012\auto

# Making sure we have the “best tour” (3)

In the case where a thread tests and decides it has a better global solution, we need to ensure two things:

1) That the process locks the value with a mutex, preventing a race condition.

2) In the possible event that the first check was against an old value while another process was updating, we do not put a worse value than the new one that was being written.

We handle this by locking, then testing again.

---

## Lecture: output\TreeSearch\page_013\TreeSearch_page_013\auto

# First scenario

![](images/faacdaa79eb061810e990cee1659c062bb12cfe3336c9c278e38c2f86115d3c5.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\TreeSearch\page_013\TreeSearch_page_013\auto\images\faacdaa79eb061810e990cee1659c062bb12cfe3336c9c278e38c2f86115d3c5.jpg

---

## Lecture: output\TreeSearch\page_014\TreeSearch_page_014\auto

# Second scenario

![](images/649b3dabc2c6c29b23cd571943b4f7767ee32379c09f52ad8bbfe823ce34dc28.jpg)

3. test

6. lock

7. test again

8. unlock

1. test   
2. lock   
4. update   
5. unlock

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\TreeSearch\page_014\TreeSearch_page_014\auto\images\649b3dabc2c6c29b23cd571943b4f7767ee32379c09f52ad8bbfe823ce34dc28.jpg

---

## Lecture: output\TreeSearch\page_015\TreeSearch_page_015\auto

# Parallelizing the Tree Search Programs Using OpenMP

Same basic issues implementing the static and dynamic parallel tree search programs as Pthreads.

A few small changes can be noted.

![](images/90c78099edb13e8e8b1ff8653e269c616a45846d1c3466d2d2a5e4472c8695d8.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\TreeSearch\page_015\TreeSearch_page_015\auto\images\90c78099edb13e8e8b1ff8653e269c616a45846d1c3466d2d2a5e4472c8695d8.jpg
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\TreeSearch\page_015\TreeSearch_page_015\auto\images\ed5b8c36c9f22d5006cc4beb7479df9423175d7feb1349be309e267a1bdd6231.jpg

---

## Lecture: output\TreeSearch\page_016\TreeSearch_page_016\auto

# OpenMP emulated condition wait

int a $\begin{array} { r l } & { \begin{array} { r l } & { \vert o b a l \quad \nu a r s \quad * / } \\ & { \vert \mathrm { w a k e n e d } _ { - } \mathrm { t h } \mathrm { r e a d } \quad = \quad - 1 ; } \\ & { \mathrm { . r e m a i n s ~ = ~ 1 } ; \quad \nearrow \quad t r u e \quad * / } \end{array} } \\ & { \begin{array} { r l } & { \vert o \mathrm { b } \quad \mathrm { e } \in \mathrm { L } _ { - } \mathrm { l o c k } ( \& \mathrm { t e r m } _ { - } \mathrm { l o c k } ) ; } \\ & { \quad \mathrm { ~ ( ~ a ~ w a k e n e d } _ { - } \mathrm { t h } \mathrm { r e a d } \quad \mathrm { l } \mathrm { = ~ \mu ~ \mathrm { ~ m y } \mathrm { - } r a n k ~ \& } \mathcal { \& } \end{array} ~ } } \\ & { \begin{array} { r l } & { \mathrm { e } \in \mathrm { L } _ { - } \mathrm { l o c k } ( \& \mathrm { t e r m } _ { - } \mathrm { l o c k } ) ; } \end{array} } \end{array}$   
work_   
omp_u   
while   
omp_s

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\TreeSearch\page_016\TreeSearch_page_016\auto\images\d8b9a137fbf3b04b61519cf15dbde39abf5829a9d83d9df54dfeac603266ce03.jpg

---

## Lecture: output\TreeSearch\page_017\TreeSearch_page_017\auto

# IMPLEMENTATION OF TREE SEARCH USING MPI AND STATIC PARTITIONING

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\TreeSearch\page_017\TreeSearch_page_017\auto\images\b6aaa0247ab808146c8e3884d5da0d119106971199999306b33c4b8d00425216.jpg

---

## Lecture: output\TreeSearch\page_018\TreeSearch_page_018\auto

# Sending a different number of objects to each process in the communicator

int MPI_Scatterv( void\* sendbuf int $^ *$ sendcounts int $^ *$ displacements MPI_Datatype sendtype void\* recvbuf int recvcount int root MPI_Comm comm

$$
\begin{array} { r l } { \quad / * } & { { } i n \quad \mathrm { ~  ~ \psi ~ } ^ { * , \prime } , } \\ { \quad / * } & { { } i n \quad \mathrm { ~  ~ \psi ~ } ^ { * , \prime } , } \\ { \quad / * } & { { } i n \quad \mathrm { ~  ~ \psi ~ } ^ { * , \prime } , } \\ { \quad / * } & { { } i n \quad \mathrm { ~  ~ \psi ~ } ^ { * , \prime } , } \\ { \quad / * } & { { } o u t \quad \mathrm { ~  ~ \psi ~ } ^ { * , \prime } , } \\ { \quad / * } & { { } i n \quad \mathrm { ~  ~ \psi ~ } ^ { * , \prime } , } \\ { \quad / * } & { { } i n \quad \mathrm { ~  ~ \psi ~ } ^ { * , \prime } , } \\ { \quad / * } & { { } i n \quad \mathrm { ~  ~ \psi ~ } ^ { * , \prime } , } \\ { \quad / * } & { { } i n \quad \mathrm { ~  ~ \psi ~ } ^ { * , \prime } , } \end{array}
$$

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\TreeSearch\page_018\TreeSearch_page_018\auto\images\bdb33e2d8a7fe20b4946556f7acde5136c578d2c5cf1ee1f0cd659a60f44e0ce.jpg

---

## Lecture: output\TreeSearch\page_019\TreeSearch_page_019\auto

# Gathering a different number of objects from each process in the communicator

int MPI_Gatherv( void\* sendbuf int sendcount MPI_Datatype sendtype void $^ *$ recvbuf int $^ *$ recvcounts int $^ *$ displacements MPI_Datatype recvtype int root MPI_Comm comm

$$
\begin{array} { r l } { \mathrm { ~ / ~ * ~ } } & { { } i n \quad \mathrm { ~ \ } \ast \mathrm { ~ / ~ , ~ } } \\ { \mathrm { ~ / ~ * ~ } } & { { } i n \quad \mathrm { ~ \ } \ast \mathrm { ~ / ~ , ~ } } \\ { \mathrm { ~ / ~ * ~ } } & { { } i n \quad \mathrm { ~ \ } \ast \mathrm { ~ / ~ , ~ } } \\ { \mathrm { ~ / ~ * ~ } } & { { } o u t \quad \ast \mathrm { ~ / ~ , ~ } } \\ { \mathrm { ~ / ~ * ~ } } & { { } i n \quad \mathrm { ~ \ } \ast \mathrm { ~ / ~ , ~ } } \\ { \mathrm { ~ / ~ * ~ } } & { { } i n \quad \mathrm { ~ \ } \ast \mathrm { ~ / ~ , ~ } } \\ { \mathrm { ~ / ~ * ~ } } & { { } i n \quad \mathrm { ~ \ } \ast \mathrm { ~ / ~ , ~ } } \\ { \mathrm { ~ / ~ * ~ } } & { { } i n \quad \mathrm { ~ \ } \ast \mathrm { ~ / ~ , ~ } } \\ { \mathrm { ~ / ~ * ~ } } & { { } i n \quad \mathrm { ~ \ } \ast \mathrm { ~ / ~ , ~ } } \\ { \mathrm { ~ / ~ * ~ } } & { { } i n \quad \mathrm { ~ \ } \ast \mathrm { ~ / ~ , ~ } } \end{array}
$$

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\TreeSearch\page_019\TreeSearch_page_019\auto\images\3034bb274a0c6754b6a3eb5c8e362278e1bc8d85db137734af1226e54d72578d.jpg

---

## Lecture: output\TreeSearch\page_020\TreeSearch_page_020\auto

# Checking to see if a message is available

int MPI_Iprobe(

int source $\begin{array} { r l } & { \begin{array} { r l l } { f _ { * } } & { i n } & { * < { \it \Psi } , } \\ { f _ { * } } & { i n } & { * < { \it \Psi } , } \\ { f _ { * } } & { i n } & { * < { \it \Psi } , } \\ { f _ { * } } & { o u t } & { * < { \it \Psi } , } \end{array} } \\ & { \begin{array} { r l } { f _ { * } } & { o u t } & { * < { \it \Psi } , } \\ { f _ { * } } & { o u t } & { * < { \it \Psi } ) ; } \end{array} } \end{array}$   
int   
MPI_Comm comm   
int $^ *$ msg_avail_p

![](images/75ef14bd20187461e67adcf93ad755aad871a5d0f9b67a727d43ae41f78450bc.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\TreeSearch\page_020\TreeSearch_page_020\auto\images\31c421ebb1da1e54be674b6d37400f20bfe73d479835211d51b1ac88cd5b977d.jpg
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\TreeSearch\page_020\TreeSearch_page_020\auto\images\75ef14bd20187461e67adcf93ad755aad871a5d0f9b67a727d43ae41f78450bc.jpg

---

## Lecture: output\TreeSearch\page_021\TreeSearch_page_021\auto

return false; /\* Still more work \*/ $\}$ else { /\* At most I available tour \*/ /\* work that I have none $\}$ $\scriptstyle = = \ 1$ ) return true; $=$ while (1) { $\}$ $=$ $\}$ else { return false; 1 a Dynamically that Uses

Terminated Function for Partitioned TSP solver MPI.

---

## Lecture: output\TreeSearch\page_022\TreeSearch_page_022\auto

# Printing the best tour

struct { int cost; int rank;

$=$ $=$

if （global_data.rank $\qquad = = \quad 0$ ) return; /\* 0 already has the best tour \*/ if (my_rank $\scriptstyle = { \begin{array} { l l } { \_ { 0 } } \end{array} }$

else if (my_rank $= =$

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\TreeSearch\page_022\TreeSearch_page_022\auto\images\f123778b7c33f99a258bf04b630382b43d5dca7c10017d2792fe5f7cb2cd5731.jpg

---

## Lecture: output\TreeSearch\page_023\TreeSearch_page_023\auto

# Terminated Function for a Dynamically Partitioned TSP solver with MPI (1)

Fulfill_request (my_stack );   
return false; /\* Still more work \*/   
else { /\* At most I available tour \*/ /\* work that I have none if (!Empty_stack(my_stack)) { return false; /\* Still more work \*/ $\}$ if (comm_sz == 1) return true; while (1) { return true; /\* No work left . Quit \*/

---

## Lecture: output\TreeSearch\page_024\TreeSearch_page_024\auto

# Terminated Function for a Dynamically Partitioned TSP solver with MPI (2)

else if (!work_request_sent) {   
else return false;

---

## Lecture: output\TreeSearch\page_025\TreeSearch_page_025\auto

# Packing data into a buffer of contiguous memory

int MPI_Pack(

void\*   
int   
MPI_Datatype   
void\*   
int   
int\*   
MPI_Comm   
data_to_be_packed   
to_be_packed_count   
datatype   
contig_buf_size   
comm

$$
\begin{array} { l l l } { { \nonumber \ l ^ { \prime } * } } & { { i n } } & { { * \nonumber \ l ^ { \prime } , } } \\ { { \ l ^ { \prime } * } } & { { i n } } & { { * \nonumber \ l ^ { \prime } , } } \\ { { \ l ^ { \prime } * } } & { { i n } } & { { * \nonumber \ l ^ { \prime } , } } \\ { { \ l ^ { \prime } * } } & { { o u t } } & { { * \nonumber \ l ^ { \prime } , } } \\ { { \ l ^ { \prime } * } } & { { i n } } & { { * \ l ^ { \prime } , } } \\ { { \ l ^ { \prime } * } } & { { i n \ l ^ { \prime } o u t } } & { { * \ l ^ { \prime } , } } \\ { { \ l ^ { \prime } * } } & { { i n } } & { { * \ l ^ { \prime } , } } \end{array}
$$

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\TreeSearch\page_025\TreeSearch_page_025\auto\images\5633f85136b559d5845e3ff26b2d5c667221c5ce7371955b08a4aa21083ba2ee.jpg

---

## Lecture: output\TreeSearch\page_026\TreeSearch_page_026\auto

# Unpacking data from a buffer of contiguous memory

int MPI_Unpack(

void\* contig_buf   
int contig_buf_size   
int\*   
void\* unpacked_data   
int unpack_count   
MPI_Datatype datatype   
MPI_Comm comm

$$
\begin{array} { l l l } { { \nonumber \ l _ { * } } } & { { i n } } & { { \ l _ { * } \ l ^ { \prime } , } } \\ { { \ l _ { * } } } & { { i n } } & { { \ l _ { * } \ l ^ { \prime } , } } \\ { { \ l _ { * } } } & { { i n / o u t } } & { { \ l _ { * } \ l ^ { \prime } , } } \\ { { \ l _ { * } } } & { { o u t } } & { { \ l _ { * } \ l ^ { \prime } , } } \\ { { \ l _ { * } } } & { { i n } } & { { \ l _ { * } \ l ^ { \prime } , } } \\ { { \ l _ { * } } } & { { i n } } & { { \ l _ { * } \ l ^ { \prime } , } } \\ { { \ l _ { * } } } & { { i n } } & { { \ l _ { * } \ l ^ { \prime } , } } \end{array}
$$

![](images/e18563854ca5b4e0bb72bb39d5eeba5f9c73cb1fd9bbdb724877f349e543e026.jpg)

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\TreeSearch\page_026\TreeSearch_page_026\auto\images\e18563854ca5b4e0bb72bb39d5eeba5f9c73cb1fd9bbdb724877f349e543e026.jpg
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\TreeSearch\page_026\TreeSearch_page_026\auto\images\e3a80e19a095f33ac3caeafabea98efb2951e4145d0ca29f95cf63e4cc289f30.jpg

---

## Lecture: output\TreeSearch\page_027\TreeSearch_page_027\auto

<table><tr><td rowspan=1 colspan=5>Table 6.10 Termination Events that Result in an Error</td></tr><tr><td rowspan=1 colspan=1>Time</td><td rowspan=1 colspan=1>Process 0</td><td rowspan=1 colspan=2>Process 1</td><td rowspan=1 colspan=1>Process 2</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Out of Work</td><td rowspan=1 colspan=2>Out of Work</td><td rowspan=1 colspan=1>Working</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Notify 1,2</td><td rowspan=1 colspan=2>Notify 0, 2</td><td rowspan=1 colspan=1>0OW = 0</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>00W = 1</td><td rowspan=1 colspan=2>00W = 1</td><td rowspan=3 colspan=1>Recv notify fr 100W = 1</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>Send request to 1</td><td rowspan=1 colspan=2>Send Request to 2</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>00W = 1</td><td rowspan=1 colspan=2>00W  1</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>00W = 1</td><td rowspan=1 colspan=2>Recv notify fr 0</td><td rowspan=1 colspan=1>Recv request fr 1</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=2>00W= 2</td><td rowspan=1 colspan=1>00W = 1</td></tr><tr><td rowspan=2 colspan=1>3</td><td rowspan=2 colspan=1>00W = 1</td><td rowspan=1 colspan=2>00W= 2</td><td rowspan=1 colspan=1>Send work to 1</td></tr><tr><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1>0OW = 0</td></tr><tr><td rowspan=4 colspan=1>45</td><td rowspan=1 colspan=1>00W = 1</td><td rowspan=1 colspan=2>Recv work fr 2</td><td rowspan=1 colspan=1>Recv notify fr 0</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=2>00W = 1</td><td rowspan=1 colspan=1>00W = 1</td></tr><tr><td rowspan=1 colspan=1>00W =1</td><td></td><td rowspan=1 colspan=1>Notify 0</td><td rowspan=1 colspan=1>Working</td></tr><tr><td rowspan=1 colspan=1></td><td></td><td rowspan=1 colspan=1>00W =1</td><td rowspan=1 colspan=1>00W = 1</td></tr><tr><td rowspan=1 colspan=2>6     00W = 1</td><td></td><td rowspan=1 colspan=1>Recv request fr 0</td><td rowspan=1 colspan=1>Out of work</td></tr><tr><td rowspan=3 colspan=2>7      Recv notify fr 2</td><td></td><td rowspan=1 colspan=1>ooW = 1</td><td rowspan=1 colspan=1>Notify 0, 1</td></tr><tr><td></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>00W = 2</td></tr><tr><td></td><td rowspan=1 colspan=1>Send work to 0</td><td rowspan=1 colspan=1>Send request to 1</td></tr><tr><td rowspan=1 colspan=3>00W= 2</td><td rowspan=1 colspan=1>0OW= 0</td><td rowspan=1 colspan=1>00W= 2</td></tr><tr><td rowspan=1 colspan=3>8      Recv 1st notify fr 1</td><td rowspan=1 colspan=2>Recv notify fr 2        00W= 2</td></tr><tr><td rowspan=2 colspan=5>00W = 3                00W = 19      Quit                         Recv request fr 2     00W = 200W = 1</td></tr><tr><td rowspan=1 colspan=3>9      Quit</td><td rowspan=1 colspan=1>Recv request fr 2</td></tr></table>

### Images:
- data\DSAA_3032_Introduction to High-Performance and Parallel Computing\Slides\output\TreeSearch\page_027\TreeSearch_page_027\auto\images\adf8fbe54f82c79bc6b4501a14a293e90a8e74f05258348abe1711c943ecbc76.jpg

---

## Lecture: output\TreeSearch\page_028\TreeSearch_page_028\auto

# Concluding Remarks (1)

When deciding which API to use, we should consider whether to use shared- or distributed-memory.

We should look at the memory requirements of the application and the amount of communication among the processes/threads.

---

## Lecture: output\TreeSearch\page_029\TreeSearch_page_029\auto

# Concluding Remarks (2)

If the memory requirements are great or the distributed memory version can work mainly with cache, then a distributed memory program is likely to be much faster.

On the other hand, if there is considerable communication, a shared memory program will probably be faster.

---

