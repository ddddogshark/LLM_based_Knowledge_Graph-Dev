# Course: Design and Analysis of Algorithms

## Lecture: L01-Intro\page_001\L01-Intro_page_001\auto

# Design and Analysis of Algorithms

Introduction   
Algorithm   
Max in an Array and Insertion sort   
Loop Invariant

### Images:
- data\Design and Analysis of Algorithms\L01-Intro\page_001\L01-Intro_page_001\auto\images\3b847b9d6b9912929b621468144aad7d0cd22cffd5d2d15169d0aef18d1c9c69.jpg

---

## Lecture: L01-Intro\page_002\L01-Intro_page_002\auto

# Design and Analysis of Algorithms, Fall 2025

• Lecture Time: Mon + Wed, 09:00 – 10:20am, E1-101

• Lab Session: Fri, 12:00 – 12:50pm, E1-101  E1-227

• Instructor: Yanlin Zhang – yanlinzhang AT hkust-gz.edu.cn – https://zhyanlin.github.io/

• Office hour: Thursday 10-11 am, E1-5F-511

• TA – Junning Feng, jfeng496@connect.hkust-gz.edu.cn – Houcheng Su, hsu638@connect.hkust-gz.edu.cn

• Course materials – Canvas

---

## Lecture: L01-Intro\page_003\L01-Intro_page_003\auto

# Introduction

---

## Lecture: L01-Intro\page_004\L01-Intro_page_004\auto

# Course Goals

• The design and analysis of algorithms – They usually appear together

• By taking this course, you will – Obtain a good understanding of various data structures and algorithms – Learn to think analytically about algorithms – Learn to design and apply algorithms to solve computational problems effectively – Learn to implement and evaluate algorithms and data structures

---

## Lecture: L01-Intro\page_005\L01-Intro_page_005\auto

# Contents (Tentative)

<table><tr><td rowspan=1 colspan=1>Week</td><td rowspan=1 colspan=1>Topic</td><td rowspan=1 colspan=1>Content(if any)</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>Course introduction &amp; basic algorithms</td><td rowspan=1 colspan=1>RAM model &amp; Array</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>Analysis of algorithms</td><td rowspan=1 colspan=1>Asymptotic Analysis</td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>Sorting algorithms</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>Divide-and-conquer</td><td rowspan=1 colspan=1>Merge sort, Binary search, Integer multiplication,Master&#x27;s theorem</td></tr><tr><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>Basic data structures</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>Advanced data structures</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>Dynamic Programming I</td><td rowspan=1 colspan=1>Knapsack Problem</td></tr><tr><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1>Dynamic Programming Il and Midterm Exam</td><td rowspan=1 colspan=1>Longest Common Subsequence, backtracking</td></tr><tr><td rowspan=1 colspan=1>9</td><td rowspan=1 colspan=1>Greedy</td><td rowspan=1 colspan=1>Scheduling, MsT</td></tr><tr><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>Graph algorithm I</td><td rowspan=1 colspan=1>Graph representation, Graph traversal, Topologicalsorting, Cycle detection</td></tr><tr><td rowspan=1 colspan=1>11</td><td rowspan=1 colspan=1>Graph algorithm II</td><td rowspan=1 colspan=1>Strongly connected component, etc.</td></tr><tr><td rowspan=1 colspan=1>12</td><td rowspan=1 colspan=1>Graph algorithm II</td><td rowspan=1 colspan=1>shortest path algorithms</td></tr><tr><td rowspan=1 colspan=1>13</td><td rowspan=1 colspan=1>NP</td><td rowspan=1 colspan=1>P/NP, NP-complete</td></tr><tr><td rowspan=1 colspan=1>14</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr></table>

### Images:
- data\Design and Analysis of Algorithms\L01-Intro\page_005\L01-Intro_page_005\auto\images\79f150a0c8dbf3ed03e88e3c58ea0384e4979f424e0e66af509bd860cb755640.jpg

---

## Lecture: L01-Intro\page_006\L01-Intro_page_006\auto

# Textbook and Materials

# Textbook:

• Introduction to Algorithms. Cormen, Leiserson, Rivest, and Stein (CLRS)

Reference books:

• Algorithm Design. Kleinberg and Tardos The Algorithm Design Manual. Steven Skiena

Online resources:

• MIT 6.006 - Introduction to Algorithms

• Stanford CS161 - Design and Analysis of Algorithms

---

## Lecture: L01-Intro\page_007\L01-Intro_page_007\auto

# Assessment and Grading (Tentative)

Class Participation $( 5 \% )$

Lab Exercises and OJ (10%+5%):

work on lab exercises and submit by the deadline (each week); Solving 30 OJ problems

Individual Project $( 1 5 \% )$ : a two-phase programming exercise

• Mid-term exam $( 2 5 \% )$ : closed book, on computer, week 8

• Final exam $( 4 0 \% )$ : closed book, written

• We assess student performance using criterion-referencing approach. In addition to the criterion written in course syllabus, you can estimate

your performance from your course work score:

![](images/429d674e47b564ee2cdc39e7b5ab7bd67d1dd270482d05ecd4b1e3d26a339dbc.jpg)

– A level: [85, 100] – C level: [55, 70] – F level: [0, 40) – B level: [70, 85) – D level: [40, 55)

### Images:
- data\Design and Analysis of Algorithms\L01-Intro\page_007\L01-Intro_page_007\auto\images\429d674e47b564ee2cdc39e7b5ab7bd67d1dd270482d05ecd4b1e3d26a339dbc.jpg

---

## Lecture: L01-Intro\page_008\L01-Intro_page_008\auto

# ow to get the most out of this course

Preview, Participate, and Review matters!

# • Before class:

– Prepare for the lecture

# During class:

– Class participation: ask any questions anytime – Engage with in-class questions and exercises

# • After class:

– Review contents timely and ask questions $\circleddot$  Don’t wait until the day before exam  – Do exercises

# Generative AI:

– Using Generative AI to prepare and review course content is allowed.

– Don’t use it (brainlessly) to solve exercise.

• Learning requires generation by you (not AI)

Learning algorithm do require learning abstraction, in-depth thinking, and asking critical questions! 8

---

## Lecture: L01-Intro\page_009\L01-Intro_page_009\auto

# Midterm Exam

• Time: 13:00–14:30, Sat, Nov 1, 2025

• Location: TBA

• Format: On computer (solve algorithmic problems by writing code)

• Preparation:

– Having a good understanding of algorithms covered in class – Learn to write code without LLM (i.e., no copilot, no cursor, etc.) – Know basic python grammar such as use self in a python class.

• Fun data of last course offering: – Mean/median midterm score: \~50  many students failed at writing bug-free code – Mean/median course score: \~80

---

## Lecture: L01-Intro\page_010\L01-Intro_page_010\auto

Algorithm

---

## Lecture: L01-Intro\page_011\L01-Intro_page_011\auto

# Programming Languages

• Natural Languages • Chinese, English, Japanese, …

Programming Languages (PLs)

• High Level PLs • Pascal, C, Java, …

• Low Level PLs

• Assembly Languages

• A Machine Language executed by a CPU

Programming: to tell what CPU to do step-by-step

$$
2 + 3 = ?
$$

• Input/Output,

• Get the answer (computing)

![](images/8b19c727e1526f45573b3c9b7add40f87945ec37d655d314fa48c45bebbd76eb.jpg)

### Images:
- data\Design and Analysis of Algorithms\L01-Intro\page_011\L01-Intro_page_011\auto\images\2f5e75c7368f475c90f82372d69bd974723ff05391e948807f7caf7b550c3aa2.jpg
- data\Design and Analysis of Algorithms\L01-Intro\page_011\L01-Intro_page_011\auto\images\8b19c727e1526f45573b3c9b7add40f87945ec37d655d314fa48c45bebbd76eb.jpg

---

## Lecture: L01-Intro\page_012\L01-Intro_page_012\auto

# Data Structures and Algorithms

• Algorithm: Outline, the essence of a computational procedure, step-by-step instructions

• Program: an implementation of an algorithm in some programming language

• Data structure: Organization of data needed to solve the problem

---

## Lecture: L01-Intro\page_013\L01-Intro_page_013\auto

# What Is an Algorithm

# THE FRIENDSHIP ALGORITHM

![](images/09a9e8e93101b41bb6c91acfab08d2d8eda5215afa242730237f6645adc80630.jpg)

### Images:
- data\Design and Analysis of Algorithms\L01-Intro\page_013\L01-Intro_page_013\auto\images\09a9e8e93101b41bb6c91acfab08d2d8eda5215afa242730237f6645adc80630.jpg

---

## Lecture: L01-Intro\page_014\L01-Intro_page_014\auto

# An Algorithm is Like a Recipe

• The ingredients • The equipment • The list of steps

![](images/6029b83c6b5b148daecccda2bb4073745b41e23cb5c993363a1723c48253a77a.jpg)

![](images/e972a245ea0770c2bca8479d7f263426db7ab4525ee0213940c6a98e97b4e0d9.jpg)

### Images:
- data\Design and Analysis of Algorithms\L01-Intro\page_014\L01-Intro_page_014\auto\images\6029b83c6b5b148daecccda2bb4073745b41e23cb5c993363a1723c48253a77a.jpg
- data\Design and Analysis of Algorithms\L01-Intro\page_014\L01-Intro_page_014\auto\images\e972a245ea0770c2bca8479d7f263426db7ab4525ee0213940c6a98e97b4e0d9.jpg

---

## Lecture: L01-Intro\page_015\L01-Intro_page_015\auto

• An algorithm is a finite set of instructions that, if followed, accomplishes a particular task to solve a problem.

• All algorithms satisfy the following criteria:

• Input: 0 or more quantities are supplied.

• Output: At least one quantity is produced.

• Definiteness: Each instruction is clear and unambiguous.

• Finiteness: For all cases, the algorithm terminates after a finite number of steps.

• Effectiveness: Every instruction must be basic enough (feasible).

---

## Lecture: L01-Intro\page_016\L01-Intro_page_016\auto

# Basic Instructions

• Unlike human, one instruction can only do a very basic thing,

• read/write a single data value

• compare two data values

• Arithmetic operations $( + , - , \times , \div )$ , etc.

Depends on computer, programming language, ...

• Consider sorting cards.

• Human can quickly sort cards in order, because they can see all the cards simultaneously.

• An algorithm cannot.

![](images/e11c449df1dd94c877bd54e7d7b5619017f6a00a1d2e45fa81d52a2ede13012a.jpg)

### Images:
- data\Design and Analysis of Algorithms\L01-Intro\page_016\L01-Intro_page_016\auto\images\e11c449df1dd94c877bd54e7d7b5619017f6a00a1d2e45fa81d52a2ede13012a.jpg

---

## Lecture: L01-Intro\page_017\L01-Intro_page_017\auto

# Models of Computation

# ● Real Computers are complicated

• Memory hierarchy, floating point operations, garbage collector, compiler optimizations, different programming languages, . . .

# Models of Computation:

• Simple abstraction of a Computer

• Defines the “Rules of the Game”:

• Which operations is an algorithm allowed to do?

• What is the cost of each operation?

• Cost of an algorithm $= \ \sum$ cost of all its operations

---

## Lecture: L01-Intro\page_018\L01-Intro_page_018\auto

RAM Model: Random Access Machine Model

• Infinite Random Access Memory (an array), each cell has a unique address

• Each cell stores one word, e.g., an integer, a character, an address, etc.

RAM   

<table><tr><td rowspan="4">1 2 3 4</td><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td rowspan="5">5f 7 8</td><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td rowspan="2">9 10</td><td></td></tr><tr><td></td></tr></table>

• Input: Stored in RAM

• Output: To be written into RAM

• A finite (constant) number of registers (e.g., 4)

# • In a single Step we can:

• Load a word from memory into a register

• Compute $( + , - , * , / )$ , bit operations, comparisons, etc. on registers

• Move a word from register to memory

<table><tr><td rowspan="2">1</td><td>Registers</td></tr><tr><td></td></tr><tr><td rowspan="3">2 3 4</td><td></td></tr><tr><td></td></tr><tr><td></td></tr></table>

### Images:
- data\Design and Analysis of Algorithms\L01-Intro\page_018\L01-Intro_page_018\auto\images\4b3a900cf5420e3de28e7eda70e9b9e76ec6a696b02528dfd15d4f5169a2f772.jpg
- data\Design and Analysis of Algorithms\L01-Intro\page_018\L01-Intro_page_018\auto\images\b685c46faf8412d12017964def286db1a819cdd7596bd2ecd7a1861c2306dfff.jpg

---

## Lecture: L01-Intro\page_019\L01-Intro_page_019\auto

# Algorithm in the RAM Model

Sequence of elementary operations (similar to assembler code)

● Example: Compute the sum of two integers

Assume that M[1] and M[2] contain the integers

Write output to position M[3]

Cost of an Algorithm:

Runtime: Total cost of all elementary operations

Space: Total number of memory cells used

---

## Lecture: L01-Intro\page_020\L01-Intro_page_020\auto

# Take-away Messages

• This is not a programming course; however, you will engage in exercises that focus on problem-solving through programming.

• Programming is the last step in software development, which occurs only after the algorithms are clear.

• Computer science is a branch of mathematics with its art reflected in the beauty of algorithms.

• Programming knowledge is not necessary to study algorithms.

---

## Lecture: L01-Intro\page_021\L01-Intro_page_021\auto

# Max in an Array and Insertion sort

---

## Lecture: L01-Intro\page_022\L01-Intro_page_022\auto

• An array is a linear data structure that stores a fixed-size collection of elements of the same type in contiguous memory locations.

– Fixed Size – Its size is declared at initialization and cannot be changed.

– Contiguous Memory Allocation – Elements are stored sequentially in memory, making access fast (O(1) for direct access by index).

– Homogeneous – All elements in an array must be of the same data type.   
– Index-Based Access – Elements are accessed using an index, starting from 1.

Array:

<table><tr><td>10</td><td>25</td><td>30</td><td>40</td><td>50</td></tr><tr><td>1</td><td colspan="2">2 3</td><td colspan="2">4 5</td></tr></table>

Index:

### Images:
- data\Design and Analysis of Algorithms\L01-Intro\page_022\L01-Intro_page_022\auto\images\450bfd1e4df7b5eb1c6f1d2df618419274dc5e431cf8624742725086d8ef179c.jpg

---

## Lecture: L01-Intro\page_023\L01-Intro_page_023\auto

# Max in an Array

Algorithm findMax(A)

Input: An array A storing n values

Output: The maximum element in A

### Images:
- data\Design and Analysis of Algorithms\L01-Intro\page_023\L01-Intro_page_023\auto\images\010d03ebc67e2ab0b62dbce16d8b3383fdad3438d74fc762a807736cfc6c51e6.jpg
- data\Design and Analysis of Algorithms\L01-Intro\page_023\L01-Intro_page_023\auto\images\faf3b4087333e8d3a9ee97489be6bb9ed375583f90ef53090c8d40623077361f.jpg

---

## Lecture: L01-Intro\page_024\L01-Intro_page_024\auto

# Pseudo-Code

Pseudo-code: A mixture of natural language and high-level programming concepts that describes the main ideas behind a generic implementation of a data structure or algorithm.

• It is more structured than usual prose but less formal than a programming language

• Expressions – use standard mathematical symbols to describe numeric and boolean expressions – use for assignment ${ \bf \chi } ^ { \prime \prime } = { \bf \chi } ^ { \prime \prime }$ in Python) – use $=$ for equality relationship ( $\mathit { \Omega } ^ { \prime \prime } = = \mathit { \Omega } ^ { \prime \prime }$ in Python)

• Method declarations – algorithm name(param1,param2)

---

## Lecture: L01-Intro\page_025\L01-Intro_page_025\auto

# Pseudo-Code

Programming constructs

![](images/77c3f5a0b8f5fec599118685049b16ab63b5eec45e3724e869ef93df40d12a90.jpg)

calls: object method(args) returns: return value

### Images:
- data\Design and Analysis of Algorithms\L01-Intro\page_025\L01-Intro_page_025\auto\images\77c3f5a0b8f5fec599118685049b16ab63b5eec45e3724e869ef93df40d12a90.jpg

---

## Lecture: L01-Intro\page_026\L01-Intro_page_026\auto

# findMax pseudo-code

Algorithm FindMax(A) Input: An array A with n elements Output: The maximum value in A

1. max_so_far A[1] // Initialize max with the first element   
2. for $\dot { \textbf { 1 } }  2$ to length(A) - 1 do   
3. if A[i] > max_so_far then   
4. max_so_far A[i] // Update max if a larger value is found   
5. end if   
6. end for Visualization of Finding Max in an Array

![](images/cde89bdc8bc9f8b195b95f994de9de001afae47ac917abe9592f666e6ab6b4c5.jpg)

### Images:
- data\Design and Analysis of Algorithms\L01-Intro\page_026\L01-Intro_page_026\auto\images\cde89bdc8bc9f8b195b95f994de9de001afae47ac917abe9592f666e6ab6b4c5.jpg

---

## Lecture: L01-Intro\page_027\L01-Intro_page_027\auto

# Sorting an Array

Algorithm sort(A)

Input: An array A storing n values

Output: A permutation of A where elements are ordered in increasing sequence

### Images:
- data\Design and Analysis of Algorithms\L01-Intro\page_027\L01-Intro_page_027\auto\images\8c6dffb6b2aae365e700b907cd3f5a40e961c94273bf30123ba79fea1eb0ef84.jpg

---

## Lecture: L01-Intro\page_028\L01-Intro_page_028\auto

# INPUT

sequence of numbers

# OUTPUT

a permutation of the sequence of numbers

![](images/4ce75524bc837c427a714d1c6e270f0bc7b535c1d917e6f18ccf8aa5416a160b.jpg)

Correctness (requirements for the output)

For any given input the algorithm halts with the output:

$\bullet \mathsf { b } _ { 1 } < \mathsf { b } _ { 2 } < \mathsf { b } _ { 3 } < \ldots < \mathsf { b } _ { \mathsf { n } }$   
$\bullet \mathsf { b } _ { 1 } , \mathsf { b } _ { 2 } , \mathsf { b } _ { 3 } , . . . . , \mathsf { b } _ { \mathsf { n } }$ is a permutation of   
$\_$

# Running time

Depends on

• number of elements (n)

•how (partially) sorted they are

•algorithm

### Images:
- data\Design and Analysis of Algorithms\L01-Intro\page_028\L01-Intro_page_028\auto\images\4ce75524bc837c427a714d1c6e270f0bc7b535c1d917e6f18ccf8aa5416a160b.jpg
- data\Design and Analysis of Algorithms\L01-Intro\page_028\L01-Intro_page_028\auto\images\cc1c639a9c4ce0645dcf390d4ff0b05960a565e5b1850682fb0014186718e469.jpg
- data\Design and Analysis of Algorithms\L01-Intro\page_028\L01-Intro_page_028\auto\images\d26f4c0357168520fb08f9b52b9a1aba1b615026eb520629e25b95684875dc33.jpg

---

## Lecture: L01-Intro\page_029\L01-Intro_page_029\auto

# Picking and Placing Cards at Hand

Poker-Style Insertion Sort (magic power)

Table:□5

Table:□2

Hand: 5

# Strategy

• Start "empty handed"   
• Insert a card in the right   
position of the already   
sorted hand   
• Continue until all cards are   
inserted/sorted

![](images/ffd82ad5f184fbdc0aac75cf9cb15c79dbdbe0da435dfd49c57867017d97d8ab.jpg)

Table: -3   
Hand: 2 - 4 5

Table: Hand:12 3 4 -5

![](images/3df3f5b0fc4c58c8a08f3791e67deb477bffea4ede2d179a50de8810d005ed3c.jpg)

Table: Hand:□I□2 3 4 5

### Images:
- data\Design and Analysis of Algorithms\L01-Intro\page_029\L01-Intro_page_029\auto\images\3df3f5b0fc4c58c8a08f3791e67deb477bffea4ede2d179a50de8810d005ed3c.jpg
- data\Design and Analysis of Algorithms\L01-Intro\page_029\L01-Intro_page_029\auto\images\ffd82ad5f184fbdc0aac75cf9cb15c79dbdbe0da435dfd49c57867017d97d8ab.jpg

---

## Lecture: L01-Intro\page_030\L01-Intro_page_030\auto

# Insertion Sort

Algorithm InsertionSort(A) Input: An array A with n elements Output: A sorted in non-decreasing order

1. for $\dot { 1 }  2$ to length(A) do   
2. key A[i] // Current element to be inserted   
3. j ← i - 1 // Start comparing from the previous element   
4. while j > 0 and A[j] $>$ key do   
5. A[j + 1] ← A[j] // Shift element to the right   
6. j ← j - 1   
7. end while   
8. $\mathsf { A } [ \mathsf { j } \ + \ \mathsf { 1 } ] \  \ \mathsf { k e y }$ // Place key in the correct position   
9. end for

10. return A // Sorted array

# Insertion Sort Step-by-Step

![](images/323d6160c619c3d81ce11593b6d017826172e97d98dc816d1815a497c03cef9e.jpg)

### Images:
- data\Design and Analysis of Algorithms\L01-Intro\page_030\L01-Intro_page_030\auto\images\323d6160c619c3d81ce11593b6d017826172e97d98dc816d1815a497c03cef9e.jpg

---

## Lecture: L01-Intro\page_031\L01-Intro_page_031\auto

# Loop Invariant

---

## Lecture: L01-Intro\page_032\L01-Intro_page_032\auto

# Proving the Correctness of FindMax

Algorithm FindMax(A)

Input: An array A with n elements Output: The maximum value in A

1. max_so_far A[1]   
2. for $\dot { \textbf { 1 } }  2$ to length(A) - 1 do   
3. if A[i] $>$ max_so_far then   
4. max_so_far A[i]   
5. end if   
6. end for   
7. return max_so_far

# Proof of Correctness

Goal: Showing that max_so_far stores the maximum value of A.

1. Before the Loop Starts (Initialization)

•Before entering the loop, max_so_far = A[1].   
Since we’ve only seen one element, this is correct.

2. During Each Iteration (Maintenance)

•If A[i] $>$ max_so_far, we update max_so_far = A[i], ensuring it holds the maximum seen so far.

•Otherwise, max_so_far remains unchanged, which is still correct.

3. After the Loop Ends (Termination)

•At the end, max_so_far contains the maximum of all A[1] to A[n].

---

## Lecture: L01-Intro\page_033\L01-Intro_page_033\auto

# Loop Invariant

• A loop invariant is a property or condition that holds true before and after each iteration of a loop.

• Purpose:

– To show that an algorithm maintains a specific condition throughout its execution.

– To help prove that the algorithm works correctly (via initialization, maintenance, and termination).

• The way that we prove FindMax correct is Loop Invariant. – Loop invariant: max_so_far holds the maximum value among A[1:i].

---

## Lecture: L01-Intro\page_034\L01-Intro_page_034\auto

# Structure of a Loop Invariant Proof

• Initialization: Show that the invariant holds before the first iteration (base case).

• Maintenance: Assuming the invariant holds at the beginning of any iteration, prove that it still holds after executing the loop body.

• Termination: When the loop terminates, the invariant (plus the loop’s exit condition) gives a useful property that helps prove the algorithm’s correctness.

FYI. The three steps is introduced in CLRS. In other books, you may find Establishment (i.e. Initialization), Preservation (i.e. Maintenance), Postcondition and Termination: Postcondition ensures the final goal is achieved if the loop stops; Termination guarantees that the loop will stop.

---

## Lecture: L01-Intro\page_035\L01-Intro_page_035\auto

# Proving Insertion-sort

# Proof of Correctness

Algorithm InsertionSort(A) Input: An array A with n elements Output: A sorted in non-decreasing order

1. for $\dot { \textbf { 1 } }  2$ to length(A) do   
2. key ← A[i]   
3. j ← i - 1   
4. while j > 0 and A[j] > key do   
5. A[j + 1] ← A[j]   
6. j ← j - 1   
7. end while   
8. $\mathsf { A } [ \mathsf { j } \ + \ \mathsf { 1 } ] \  \ \mathsf { k e y }$   
9. end for

10. return A

Loop Invariant: A[1:i-1] is a sorted list of elements in the original A[1:i-1]

1. Initialization (Note: i ← 2 is not part of the loop) • When $\mathsf { i } = 2$ , A[1:1] contains one value  sorted.

# 2. Maintenance

• Within the loop-body, A[1:i-1] is assumed to be sorted. We move A[i-1], A[i-2], … toward the right, until we find a position for A[i]. Once A[i] is inserted, A[1:i] remains sorted.

# 3. Termination

• As i goes from 2 to length(A), and the loop body does not modify i. The loop will terminate. By termination, i=length(A) means A[1:length(A)] is sorted.

### Images:
- data\Design and Analysis of Algorithms\L01-Intro\page_035\L01-Intro_page_035\auto\images\f59a5646e7188a29c29abe7905a10fc588e33c5f8d36d401c97d326874d5e981.jpg

---

## Lecture: L01-Intro\page_036\L01-Intro_page_036\auto

# Discussion: a Loop Invariant for Linear Search

Algorithm LinearSearch(A, x) Input: An array A with n elements, target value x Output: Index of $\mathbf { x }$ in A, or -1 if not found

1. loc = -1   
2. for $\mathrm { ~ \bf ~ i ~ }  \mathrm { ~ 1 ~ }$ to length(A) d   
3. if A[i] == x then   
4. loc $\mathbf { \mu } = \mathbf { \dot { \lambda } } \mathbf { \dot { 1 } }$ // Found x at index i   
5. end if   
6. end for   
7. return loc

# Proof of Correctness

Loop Invariant: What is true and related to this task?

1. Initialization: What is true about A[1:i] before the loop starts?

2. Maintenance: How does each iteration preserve the correctness of the search?

3. Termination: When the loop exits, why can we be sure the correct index or -1 is returned?

---

## Lecture: L01-Intro\page_037\L01-Intro_page_037\auto

# Discussion: a Loop Invariant for Linear Search

Algorithm LinearSearch2(A, x) Input: An array A with n elements, target value x Output: Index of x in A, or -1 if not found

1. for $\mathrm { ~ \bf ~ i ~ }  1$ to length(A) do   
2. if A[i] == x then   
3. return i // Found x at index i   
4. end if   
5. end for   
6. return -1 // x is not in A

# Proof of Correctness

Loop Invariant:

1. Initialization:

2. Maintenance:

3. Termination:

---

## Lecture: L01-Intro\page_038\L01-Intro_page_038\auto

# Finding the Sugared Water

You have 100 cups of water, but only one contains sugar. How can you find it quickly?

Possible Solution: Naïve Approach (Brute Force)

Taste each cup one by one $ 1 0 0$ checks needed

Can We Do Better?

Is there a smarter, faster way?

![](images/46e283a9195a41d94dbfa7c02f1df52670b5c0d24329affdb52ad5ec630b1981.jpg)

### Images:
- data\Design and Analysis of Algorithms\L01-Intro\page_038\L01-Intro_page_038\auto\images\46e283a9195a41d94dbfa7c02f1df52670b5c0d24329affdb52ad5ec630b1981.jpg

---

## Lecture: L01-Intro\page_039\L01-Intro_page_039\auto

# An Example

• Suppose we use a list of integers as the data structure to store a set ???? of ???? integers.

• Consider how to support the search operation:

• A function search(????, search_num) that returns the index i of search_num in the list, or -1 if it is not found.

• Example:

• ???? = 3, 7,9,12, 13,18,20,23,27 • Is 20 in ?????

• We give two algorithms to implement it.

---

## Lecture: L01-Intro\page_040\L01-Intro_page_040\auto

# An Example: Linear Search

• Simply read the integer of index ???? for each $i \in [ 0 , n - 1 ] ,$ .   
• If there exists ???? s.t. $S [ i ] = s e a r c h$ _num, return ????;   
• Otherwise, return -1.

def search(integer_set, search_num): for i in range(len(integer_set)): if integer_set{i] == search_num: return i # Return the index if found return -1 # Return -1 if not found

---

## Lecture: L01-Intro\page_041\L01-Intro_page_041\auto

# An Example: Binary Search

• Assume sets of integers are sorted.

• Let us compare search_num to the element in the middle (the (????/2)- th) of ????)

![](images/d65ef9ca66c37a12e9b92c465d57169ba201e580083aa2c01c805fcb126626e7.jpg)

### Images:
- data\Design and Analysis of Algorithms\L01-Intro\page_041\L01-Intro_page_041\auto\images\d65ef9ca66c37a12e9b92c465d57169ba201e580083aa2c01c805fcb126626e7.jpg

---

## Lecture: L01-Intro\page_042\L01-Intro_page_042\auto

# searchnum $=$ 18 size = 9

<table><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>9</td><td rowspan=1 colspan=1>12</td><td rowspan=1 colspan=1>1213</td><td rowspan=1 colspan=1>18</td><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1>23</td><td rowspan=1 colspan=1>27d:</td></tr></table>

![](images/ca7c8f7adde0a56c9f65ae046ea569d199e4b2896e83f8f91fe291f52a0bc9b2.jpg)

### Images:
- data\Design and Analysis of Algorithms\L01-Intro\page_042\L01-Intro_page_042\auto\images\8df061859e69a539d0e848aff6fc66bc23e4f2ae432f6e3fb24b84ab67a30a3f.jpg
- data\Design and Analysis of Algorithms\L01-Intro\page_042\L01-Intro_page_042\auto\images\ca7c8f7adde0a56c9f65ae046ea569d199e4b2896e83f8f91fe291f52a0bc9b2.jpg

---

## Lecture: L01-Intro\page_043\L01-Intro_page_043\auto

# searchnum $=$ 28 size = 9

<table><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>9</td><td rowspan=1 colspan=1>1213</td><td rowspan=1 colspan=1>1213</td><td rowspan=1 colspan=1>18</td><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1>23id</td><td rowspan=1 colspan=1>27</td></tr></table>

![](images/7c5dfe46259ba779c6c02e05bc6aefcfa0d04c3f3666156cd6f78939cf896ebc.jpg)

### Images:
- data\Design and Analysis of Algorithms\L01-Intro\page_043\L01-Intro_page_043\auto\images\7c5dfe46259ba779c6c02e05bc6aefcfa0d04c3f3666156cd6f78939cf896ebc.jpg
- data\Design and Analysis of Algorithms\L01-Intro\page_043\L01-Intro_page_043\auto\images\86c0775ba3c88571881159ad71f2bc857abba3dd5110173a70460aed026df96b.jpg

---

## Lecture: L01-Intro\page_044\L01-Intro_page_044\auto

# Linear search VS binary search: which one is better?

def search(integer_set, search_num): for i in range(len(integer_set)): if integer_set[i] == search_num: return i # Return the index if found return -1 # Return -1 if not found

def binary_search(sorted_set, search_num): left =0 right = len(sorted_set) - 1 while left <= right: middle = (left + right) // 2 # Find the middle index if sorted_set[middle] < search_num: left = middle + i # Narrow search to the right half elif sorted_set[middle] > search_num: right = middle - 1 # Narrow search to the left half else: return middle # Return the index if found return -1 # Return -1 if not found

---

## Lecture: L02-Asymptotic\page_001\L02-Asymptotic_page_001\auto

# Analysis of Algorithms

Motivations

primitive operations Best/Worst/Average Case

Asymptotic Analysis

#

-The Big O notation Big Omega and Big Theta - Rules

Analyzing insertion sort

---

## Lecture: L02-Asymptotic\page_002\L02-Asymptotic_page_002\auto

# Motivations

---

## Lecture: L02-Asymptotic\page_003\L02-Asymptotic_page_003\auto

# Algorithmic Problem​

![](images/3ef4e882688d81516b6a0af67dd37f911bc0dc583fc178fe03efa817b815c871.jpg)

Infinite number of input instances satisfying the specification.

• E.g., a sorted, non-decreasing sequence of natural numbers of non-zero, finite length:

• 1, 20, 908, 909, 100000, 1000000000   
• 3

### Images:
- data\Design and Analysis of Algorithms\L02-Asymptotic\page_003\L02-Asymptotic_page_003\auto\images\3ef4e882688d81516b6a0af67dd37f911bc0dc583fc178fe03efa817b815c871.jpg

---

## Lecture: L02-Asymptotic\page_004\L02-Asymptotic_page_004\auto

# Algorithmic Solution

![](images/7e6d6f2e0f07265e24388a660571dde49b1fb9c217c5a60e7eb286309b4b4b93.jpg)

Algorithm describes actions on the input instance

• Many correct algorithms for the same algorithmic problem

### Images:
- data\Design and Analysis of Algorithms\L02-Asymptotic\page_004\L02-Asymptotic_page_004\auto\images\7e6d6f2e0f07265e24388a660571dde49b1fb9c217c5a60e7eb286309b4b4b93.jpg

---

## Lecture: L02-Asymptotic\page_005\L02-Asymptotic_page_005\auto

# What is a Good Algorithm?

• Efficient – Running time – Space used

• Efficiency as a function of input size – The number of bits in an input number – Number of data elements (numbers, points)

---

## Lecture: L02-Asymptotic\page_006\L02-Asymptotic_page_006\auto

# What is Analysis of Algorithms

Estimate the running time.

Estimate the memory space required.

Time and space depend on the input size.

---

## Lecture: L02-Asymptotic\page_007\L02-Asymptotic_page_007\auto

# Measuring the Running Time Experimentally

How should we measure the running time of an algorithm?

![](images/47f82bbd4ddae89601f3c6e5e44596821be890774f8f9b7eb95d3b6a61b726d2.jpg)  
Sorting Algorithm Performance on 1000 Elements Over 10 Runs (Mean ± Std

# Experimental Study

Write a program that implements the algorithm   
Run the program with data sets of varying size and composition Use a system call to get an accurate measure of the actual running time

### Images:
- data\Design and Analysis of Algorithms\L02-Asymptotic\page_007\L02-Asymptotic_page_007\auto\images\47f82bbd4ddae89601f3c6e5e44596821be890774f8f9b7eb95d3b6a61b726d2.jpg

---

## Lecture: L02-Asymptotic\page_008\L02-Asymptotic_page_008\auto

# Limitations of Experimental Studies

• Must implement and test the algorithm to determine its running time

• Experiments done only on a limited set of inputs

– May not be indicative of the running time on other inputs not included in the experiment

• To compare two algorithms, the same hardware and software environments needed

---

## Lecture: L02-Asymptotic\page_009\L02-Asymptotic_page_009\auto

# Beyond Experimental Studies

• We will develop a general methodology for analyzing running time of algorithms. This approach

– Uses a high-level description (pseudocode) of the algorithm instead of testing one of its implementations

– Considers all possible inputs

– Evaluates the efficiency of any algorithm being independent of the hardware and software environment

• To achieve that, we need to

– Make simplifying assumptions about the running time of each basic (primitive) operations

– Study how the number of primitive operations depends on the size of the problem solved

---

## Lecture: L02-Asymptotic\page_010\L02-Asymptotic_page_010\auto

# Primitive Operations

Simple computer operation that can be performed in time that is always the same, independent of the size of the bigger problem solved (we say: constant time)

Assigning a value to a variable: $\mathsf { x } \gets 1$ Tassign Calling a method: Expos.addWin() Tcall Note: doesn' t include the time to execute the method Returning from a method: return x; Treturn Arithmetic operations on primitive types Tarith $\mathsf { x } + \mathsf { y } , \mathsf { r } ^ { \ast } 3 . 1 4 1 6 , \mathsf { x } / \mathsf { y } ,$ etc. Comparisons on primitive types: $\tt x = = y$ Tcomp Conditionals: if (.…..) then.. else... Tcond Indexing into an array: A[i] Tindex Following object reference: Expos.losses Tref

Note: Multiplying two Large Integers is not a primitive operation, because the running time depends on the size of the numbers multiplied.

---

## Lecture: L02-Asymptotic\page_011\L02-Asymptotic_page_011\auto

# More assumptions

• Counting each type of primitive operations is tedious

• The running time of each operation is roughly comparable:

Tasign ≈ Tcomp ≈ Tarit≈…≈Tindex= 1 primitive operation

• We are only interested in the number of primitive operations performed

---

## Lecture: L02-Asymptotic\page_012\L02-Asymptotic_page_012\auto

# Estimating Running Time for FindMin

Algorithm findMin(A, start, stop)   
Input: Array A, index start & stop   
output: Index of the smallest element of A[start:stop]   
minvalue ← A[start] Tindex + Tassign   
minindex start Tassinn Running time   
index start + 1 Tarth + Tasssignn   
while( index $< =$ stop ) do { Tcomp+ Tcond if (A[index]<minvalue) Tindex + Tcomp + Tcond then { repeated minvalue $ \texttt { A }$ [index] Tindex +Tasignn stop-start minindex index Tassign times } index $=$ index + 1 Tassin + Tarithth   
} Tcomp+ Tcond (last check of loop)   
return minindex Treturn

---

## Lecture: L02-Asymptotic\page_013\L02-Asymptotic_page_013\auto

# Estimating Running Time for FindMin

• Running time depends on n = stop – start + 1

• $\Gamma ( \mathrm { n } ) = 8 + 1 0$ \* (n-1) primitive operations – 8 primitive operations outside the loop – 10 primitive operations inside the loop

• How will the running time change for the following two input instances?

<table><tr><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td></tr></table>

<table><tr><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>5</td></tr></table>

### Images:
- data\Design and Analysis of Algorithms\L02-Asymptotic\page_013\L02-Asymptotic_page_013\auto\images\872a7b264553abbe9a35761bb9a5f51ac591b72520e84cde449a62d3b0da33ad.jpg
- data\Design and Analysis of Algorithms\L02-Asymptotic\page_013\L02-Asymptotic_page_013\auto\images\e7f0747db9878a51f604b2c81283d8f3e4901e17605bd18bc56dc0c17ffa4117.jpg

---

## Lecture: L02-Asymptotic\page_014\L02-Asymptotic_page_014\auto

# Insertion Sort (Recap.)

Algorithm InsertionSort(A) Input: An array A with n elements Output: A sorted in non-decreasing order

![](images/cd2be151e48b8543e3e3dfc4bd82354aa20a8f78772d3548d262d30fb2dfcf2d.jpg)

2. key A[i] // Current element to be inserted   
3. j ← i - 1 // Start comparing from the previous element   
4. while j > 0 and A[j] $>$ key do   
5. $\mathsf { A } [ \mathsf { j } \ + \ \mathsf { 1 } ] \  \ \mathsf { A } [ \mathsf { j } ]$ // Shift element to the right   
6. j ← j - 1   
7. end while   
8. $\mathsf { A } [ \mathsf { j } \ + \ \mathsf { 1 } ] \  \ \mathsf { k e y }$ // Place key in the correct position   
9. end for

10. return A // Sorted array

# Insertion Sort Step-by-Step

![](images/f11b09b78f476c43091d7e34de6f2b7cdf81b2ce5e8b96ef286ea1abeeb13f6a.jpg)

### Images:
- data\Design and Analysis of Algorithms\L02-Asymptotic\page_014\L02-Asymptotic_page_014\auto\images\cd2be151e48b8543e3e3dfc4bd82354aa20a8f78772d3548d262d30fb2dfcf2d.jpg
- data\Design and Analysis of Algorithms\L02-Asymptotic\page_014\L02-Asymptotic_page_014\auto\images\f11b09b78f476c43091d7e34de6f2b7cdf81b2ce5e8b96ef286ea1abeeb13f6a.jpg

---

## Lecture: L02-Asymptotic\page_015\L02-Asymptotic_page_015\auto

# Insertion Sort

<table><tr><td colspan="2">INSERTION-SORT(A, n)</td></tr><tr><td>for i = 2 to n</td><td>C1 N</td></tr><tr><td>key = A[i]</td><td>C2 n−1</td></tr><tr><td>/ Insert A[i] into the sorted subarray A[1 : i — 1]. 3</td><td>0 n−1</td></tr><tr><td>j = i − 1 4</td><td>C4 n-1</td></tr><tr><td>while j &gt; 0 and A[j] &gt; key 5</td><td>C5</td></tr><tr><td>A[j + 1] = A[j] 6</td><td>C6 ∑i=2(ti − 1) an</td></tr><tr><td>j = j − 1 7</td><td>an C7 ∑i=2(ti − 1)</td></tr><tr><td>A[j + 1] = key 8</td><td>C8 n-1</td></tr></table>

$\cdot$ : the number of while-loops used for inserting A[j]

$$
\begin{array} { r l } & { n ( c _ { 1 } + c _ { 2 } + c _ { 4 } + c _ { 8 } - c _ { 6 } - c _ { 7 } ) + \sum _ { \mathrm { i } = 2 } ^ { n } t _ { \mathrm { i } } ( c _ { 5 } + c _ { 6 } - } \\ & { - ( c _ { 2 } + c _ { 4 } - c _ { 6 } - c _ { 7 } + c _ { 8 } ) } \end{array}
$$

### Images:
- data\Design and Analysis of Algorithms\L02-Asymptotic\page_015\L02-Asymptotic_page_015\auto\images\acf8f047b44e63874aeb7513f0f3dd9a974619232fe08db5882ecf3ab083249b.jpg
- data\Design and Analysis of Algorithms\L02-Asymptotic\page_015\L02-Asymptotic_page_015\auto\images\fcb8a2096e57457987b7455979fddcf770ad1f6d713f57dde8a29311ded2958a.jpg

---

## Lecture: L02-Asymptotic\page_016\L02-Asymptotic_page_016\auto

$$
\begin{array} { r l } & { : n ( c _ { 1 } + c _ { 2 } + c _ { 4 } + c _ { 8 } - c _ { 6 } - c _ { 7 } ) + \sum _ { \mathrm { i } = 2 } ^ { n } t _ { \mathrm { i } } ( c _ { 5 } + c _ { 6 } } \\ & { - ( c _ { 2 } + c _ { 4 } - c _ { 6 } - c _ { 7 } + c _ { 8 } ) } \end{array}
$$

# Best case:

– elements are already sorted; Each element only does one comparison $( \mathfrak { t } _ { \mathrm { i } } \overline { { = } } 1 ) _ { \mathrm { \Omega } }$ , running time $=$ f(n), i.e., linear time

# • Worst case:

– elements are sorted in reverse order; each element shifts i-1 times (ti=i-1), running time $= f ( n ^ { 2 } )$ , i.e., quadratic time

# Average case:

– Each element moves above half of its maximum shifts $( t _ { \mathrm { i } } = ( \mathrm { i } - 1 ) / 2 ) ,$ , running time $= f ( n ^ { 2 } )$ , i.e., quadratic time

### Images:
- data\Design and Analysis of Algorithms\L02-Asymptotic\page_016\L02-Asymptotic_page_016\auto\images\751224cfc761cc8442216eaf84e4c2367d306ad8d6601171a6579f611df64b49.jpg

---

## Lecture: L02-Asymptotic\page_017\L02-Asymptotic_page_017\auto

• For a specific size of input n, investigate running times for different input instances:

![](images/51eb5f9b3ef18b7bf5a88e013bb6bd66bcfca409714df6013087cc1be38a212d.jpg)

### Images:
- data\Design and Analysis of Algorithms\L02-Asymptotic\page_017\L02-Asymptotic_page_017\auto\images\51eb5f9b3ef18b7bf5a88e013bb6bd66bcfca409714df6013087cc1be38a212d.jpg

---

## Lecture: L02-Asymptotic\page_018\L02-Asymptotic_page_018\auto

• For inputs of all sizes:

![](images/a1a6ca8fb6683fd7838452c3c04de2ff3992ddffda98e74a4d5905f0cd820f34.jpg)

### Images:
- data\Design and Analysis of Algorithms\L02-Asymptotic\page_018\L02-Asymptotic_page_018\auto\images\a1a6ca8fb6683fd7838452c3c04de2ff3992ddffda98e74a4d5905f0cd820f34.jpg

---

## Lecture: L02-Asymptotic\page_019\L02-Asymptotic_page_019\auto

# Best/Worst/Average Case

# • Worst case is usually used

– It is an upper-bound and in certain application domains (e.g., air traffic control, surgery) knowing the worst-case time complexity is of crucial importance   
– For some algorithms worst case occurs fairly often   
– Average case is often as bad as worst case

• Finding average case can be very difficult • The best (fastest) case is seldom of interest

---

## Lecture: L02-Asymptotic\page_020\L02-Asymptotic_page_020\auto

# Worst-Case Time of Binary Search

• Let us call the integers whose indices fall within [left, right] as active elements.

• Refer to each while-loop as an iteration. Each iteration performs a constant $c$ number of atomic operations. A loose upper bound is $c \leq 1 0$ .

• How many iterations are there?

def binary_search(sorted_set, search_num): left =o right = len(sorted_set) - 1 while left <= right: middle = (left + right) // 2 # Find the middle index if sorted_set[middle] < search_num: left = middle + i # Narrow search to the right half elif sorted_set[middle] > search_num: right = middle - 1 # Narrow search to the left half else: return middle # Return the index if found return -1 # Return -1 if not found

---

## Lecture: L02-Asymptotic\page_021\L02-Asymptotic_page_021\auto

# Worst-Case Time of Binary Search

• How many iterations are there?

Property: After the i-th iteration, the number of active elements is at most $n / 2 ^ { i }$ .

• Suppose there are $h$ iterations in total. • It holds that $\textstyle { \frac { n } { 2 ^ { h } } } \geq 1$ and thus $h \leq 1 + \log _ { 2 } n$

• The worst-case time of binary search is thus at most • $1 0 \cdot ( 1 + \log _ { 2 } n )$

• The worst-case time of linear search is at most • $4 \cdot ( 1 + n )$ (try verifying this yourself)

• When $n$ is large, binary search is much faster than linear search

### Images:
- data\Design and Analysis of Algorithms\L02-Asymptotic\page_021\L02-Asymptotic_page_021\auto\images\e0ca1cd9d109a2f2f360c76490286ed2789e62edb3dcb54e43c5ae775a8e508d.jpg

---

## Lecture: L02-Asymptotic\page_022\L02-Asymptotic_page_022\auto

# Asymptotic Analysis

---

## Lecture: L02-Asymptotic\page_023\L02-Asymptotic_page_023\auto

# Asymptotic Analysis

• Consider an arbitrary problem. Suppose that Algorithm 1 runs in • $1 0 0 0 n \cdot c _ { m u l t i } + 1 0 n \cdot c _ { m e m }$ time,

• where ???? is the time of one multiplication and $c _ { m e m }$ the time of   
one memory access; Algorithm 2 runs in • $1 0 n \cdot c _ { m u l t i } + 1 0 0 n \cdot c _ { m e m }$ time.

• Which one is better? It depends on the specific values of ???????????????????????? and ???? , which vary from machine to machine.

---

## Lecture: L02-Asymptotic\page_024\L02-Asymptotic_page_024\auto

# Why Not Constants?

• Consider an arbitrary problem. Suppose that Algorithm 1 runs in • $1 0 0 0 n \cdot c _ { m u l t i } + 1 0 n \cdot c _ { m e m }$ time,

• where ???????????????????????? is the time of one multiplication and $c _ { m e m }$ the time of   
one memory access; Algorithm 2 runs in • $1 0 n \cdot c _ { m u l t i } + 1 0 0 n \cdot c _ { m e m }$ time.

• In mathematics, we want to make a universally correct conclusion, which holds on all machines:

• Regardless of the machine, their costs differ by at most a constant factor.

---

## Lecture: L02-Asymptotic\page_025\L02-Asymptotic_page_025\auto

# Asymptotic Analysis

• Goal: to simplify analysis of running time by getting rid of “details”, which may be affected by specific implementation and hardware

– like “rounding”: 1,000,001 ≈ 1,000,000 $- 3 n ^ { 2 } \approx n ^ { 2 }$

• Capturing the essence:

– The growth of the running time with the problem size ???? – We care about the efficiency of the problem when ???? is large (think: why?)

---

## Lecture: L02-Asymptotic\page_026\L02-Asymptotic_page_026\auto

# Asymptotic Notation

• The “big-Oh” O-Notation

– asymptotic upper bound   
– let $f \left( n \right)$ and $g ( n )$ be two functions of $n$ .   
– we say that $f ( n )$ grows asymptotically no faster than $g ( n )$ if there exists positive constants $c$ and $\mathrm { n } _ { 0 }$ , s.t. $f ( n ) \leq c \cdot g ( n )$ for all $n \geq n _ { 0 }$ .   
– we can denote this by $f ( n ) \ = \ O ( g ( n ) ) .$ -

Used for worst-case analysis

Art of Computer Science:

– Minimize the growth of running time in solving a problem

![](images/db076b6001c6449de5cabdf1851b35cef90d920d322dd708d54fefcb6ab555e7.jpg)

### Images:
- data\Design and Analysis of Algorithms\L02-Asymptotic\page_026\L02-Asymptotic_page_026\auto\images\db076b6001c6449de5cabdf1851b35cef90d920d322dd708d54fefcb6ab555e7.jpg

---

## Lecture: L02-Asymptotic\page_027\L02-Asymptotic_page_027\auto

For functions $f ( n )$ and $g ( n )$ there are positive constants $c$ and $n _ { 0 }$ such that: $f ( n ) \leq c \cdot g ( n )$ for all $n \geq n _ { 0 }$ .

conclusion: 2n+6 is O(n)

$f ( n ) = 2 n + 6$

![](images/cbe92c06427d757bb63b4af250cfd61e08d7dfea82281c45270bc201a646df4b.jpg)

### Images:
- data\Design and Analysis of Algorithms\L02-Asymptotic\page_027\L02-Asymptotic_page_027\auto\images\cbe92c06427d757bb63b4af250cfd61e08d7dfea82281c45270bc201a646df4b.jpg

---

## Lecture: L02-Asymptotic\page_028\L02-Asymptotic_page_028\auto

# Another Example

On the other hand…

$n ^ { 2 }$ is not $O ( n )$ because there is no $c$ and $\pmb { n _ { 0 } }$ such that:

$$
n ^ { 2 } \ \leq \ c n \ \mathsf { f o r } n \ \geq \ n _ { 0 }
$$

The graph to the right illustrates that no matter how large a $c$ is chosen there is an $n$ big enough that $n ^ { 2 } > c n$ .

![](images/b7a8f67fa4aa3935ff4065947a89b5fb02f691f4ab646cbd2253e89ee8795bd4.jpg)

### Images:
- data\Design and Analysis of Algorithms\L02-Asymptotic\page_028\L02-Asymptotic_page_028\auto\images\b7a8f67fa4aa3935ff4065947a89b5fb02f691f4ab646cbd2253e89ee8795bd4.jpg
- data\Design and Analysis of Algorithms\L02-Asymptotic\page_028\L02-Asymptotic_page_028\auto\images\f42cdb784351e56afc7f62a6080415c5823c767433043e336f2b65893745d42e.jpg

---

## Lecture: L02-Asymptotic\page_029\L02-Asymptotic_page_029\auto

# Asymptotic Notation

• Simple Rule: drop lower order terms and constant factors.

• 50?????????? ???? is $O ( n \log n )$   
• $7 n - 3$ is $O ( n )$   
• $8 n ^ { 2 } \log n + 5 n ^ { 2 } + n \mathrm { i } s O ( n ^ { 2 } \log n )$

# • An interesting fact:

$\log _ { b _ { 1 } } n = O ( \log _ { b _ { 2 } } n )$ for any constants $b _ { 1 } > 1$ and $b _ { 2 } > 1$

• Because of the above, in computer science, we omit all the constant logarithm bases in big-O. For example, instead of $O ( \log _ { 2 } n )$ , we will simply write $O ( \log n )$ .

### Images:
- data\Design and Analysis of Algorithms\L02-Asymptotic\page_029\L02-Asymptotic_page_029\auto\images\d31c90db27ee6fea87bfa90c1b1e9d5cffdf5c32b2d3452b624cdd4538545733.jpg

---

## Lecture: L02-Asymptotic\page_030\L02-Asymptotic_page_030\auto

# Asymptotic Analysis of Running Time

• Use O-notation to express number of primitive operations executed as function of input size.

• Comparing asymptotic running times

• an algorithm that runs in $O ( n )$ time is better than one that runs in $O ( n ^ { 2 } )$ time   
• similarly, $O ( \log n )$ is better than $O ( n )$   
• hierarchy of functions: $\log n \ < \ n < \ n ^ { 2 } \ < \ n ^ { 3 } \ < \ 2 ^ { n }$

• Caution! Beware of very large constant factors. An algorithm running in time 1,000,000 $n$ is still $O ( n )$ but might be less efficient than one running in time $2 n ^ { 2 }$ , which is ${ \dot { O ( n ^ { 2 } ) } }$

---

## Lecture: L02-Asymptotic\page_031\L02-Asymptotic_page_031\auto

# Example of Asymptotic Analysis

Algorithm prefixAverages1(X)

![](images/9ca9b36ec29f3edb84ebe70611e6add0b694a26b8ae6bfd42c02d3b83dc9e582.jpg)

Analysis: running time is O(n2)

### Images:
- data\Design and Analysis of Algorithms\L02-Asymptotic\page_031\L02-Asymptotic_page_031\auto\images\9ca9b36ec29f3edb84ebe70611e6add0b694a26b8ae6bfd42c02d3b83dc9e582.jpg

---

## Lecture: L02-Asymptotic\page_032\L02-Asymptotic_page_032\auto

# Better Algorithm

Algorithm prefixAverages2(X)

Input: An n-element array X of numbers

Output: An n-element array A of numbers such that A[i] is the average of elements X[1], ... , X[i]

![](images/d5fde8d0dc829080a7019ac0ff33cee2435ac0e2349a0588f9e30e87bad93aeb.jpg)

Analysis: Running time is …

### Images:
- data\Design and Analysis of Algorithms\L02-Asymptotic\page_032\L02-Asymptotic_page_032\auto\images\d5fde8d0dc829080a7019ac0ff33cee2435ac0e2349a0588f9e30e87bad93aeb.jpg

---

## Lecture: L02-Asymptotic\page_033\L02-Asymptotic_page_033\auto

# Asymptotic Notation (Terminology)

• Special classes of algorithms:

• Logarithmic: $O ( \log n )$

• Linear: $O ( n )$

• Quadratic: $O ( n ^ { 2 } )$

• Polynomial: $O ( n ^ { k } ) , k \ge 1$

• Exponential: $O ( a ^ { n } ) , a \ > \ 1$

• “Relatives” of the Big-Oh

• $\Omega \left( f ( n ) \right)$ : Big Omega -asymptotic lower bound

• Θ $( f ( n ) )$ : Big Theta -asymptotic tight bound

---

## Lecture: L02-Asymptotic\page_034\L02-Asymptotic_page_034\auto

# What does O(1) mean?

We say $t ( n )$ is $O ( 1 )$ , if there exist two positive constants ????0 and $c$ such that, for all $n \geq n _ { 0 }$ .

$$
t ( n ) \leq c
$$

So, it means that $t ( n )$ is bounded.

### Images:
- data\Design and Analysis of Algorithms\L02-Asymptotic\page_034\L02-Asymptotic_page_034\auto\images\6c100abbe53bfa5cfc4dcd8be9bc66967f3cf014d033489d1e83bed6e5443354.jpg

---

## Lecture: L02-Asymptotic\page_035\L02-Asymptotic_page_035\auto

# Asymptotic Notation

• The “big-Omega” Ω−Notation

• Asymptotic lower bound

• Let $f \left( n \right)$ and $g ( n )$ be two functions of $n$ .

• We say that $f ( n )$ grows asymptotically no slower than $g ( n )$ if there exists positive constants $c$ and $\mathrm { n } _ { 0 }$ , s.t.

• We can denote this by $f ( n ) = \Omega ( g ( n ) )$ .

• Used to describe best-case running times or lower bounds for algorithmic problems

• E.g., lower-bound for searching in an unsorted array is $\Omega ( n )$ .

![](images/a3843e8b9714293cc3164744ef13957119dfd2a6293993f83930f93a91cb0402.jpg)

### Images:
- data\Design and Analysis of Algorithms\L02-Asymptotic\page_035\L02-Asymptotic_page_035\auto\images\a3843e8b9714293cc3164744ef13957119dfd2a6293993f83930f93a91cb0402.jpg

---

## Lecture: L02-Asymptotic\page_036\L02-Asymptotic_page_036\auto

# Asymptotic Notation

• The “big-Theta” Θ −Notation

• asymptotically tight bound

• let $f \ ( n )$ and $g ( n )$ be two functions of $n$ .

• If $f ( n ) = 0 ( g ( n ) )$ and $f ( n ) = \Omega ( g ( n ) )$ , then we define $\_$ to indicate that $f ( n )$ grows asymptotically as fast as $\mathsf { g } ( \mathsf { n } )$ .

• $f ( n ) = \Theta ( g ( n ) )$ if and only if there exists positive constants $c _ { 1 } , c _ { 2 }$ and $\mathrm { n } _ { 0 }$ , s.t.

$c _ { 1 } \cdot g ( n ) \leq f ( n ) \leq c _ { 2 } \cdot g ( n )$ for all $n \geq n _ { 0 }$

![](images/428663fdc4afc599908b07f6dff4a5331ae8039b0bb25f8552544e8a36cf0398.jpg)

### Images:
- data\Design and Analysis of Algorithms\L02-Asymptotic\page_036\L02-Asymptotic_page_036\auto\images\428663fdc4afc599908b07f6dff4a5331ae8039b0bb25f8552544e8a36cf0398.jpg

---

## Lecture: L02-Asymptotic\page_037\L02-Asymptotic_page_037\auto

# Asymptotic Notation

Two more asymptotic notations

• “Little-Oh” notation $f ( n )$ is $o ( g ( n ) )$ non-tight analogue of Big-Oh • For every $c > 0$ , there should exist $n _ { 0 }$ , s.t. $f ( n ) \leq c \cdot g ( n )$ for $n \geq n _ { 0 }$ • Used for comparisons of running times. If $f ( n )$ is $\mathsf { o } ( \mathsf { g } ( \mathsf { n } ) )$ , it is said that $g ( n )$ dominates $f ( n )$ .

• “Little-omega” notation $f ( n ) \mid _ { \mathsf { S } } \omega ( g ( n ) )$ non-tight analogue of BigOmega

---

## Lecture: L02-Asymptotic\page_038\L02-Asymptotic_page_038\auto

# Asymptotic Notation

Analogy with real numbers f(n) is O(g(n)) ≅ f ≤ g f(n) is Ω(g(n)) ≅ f ≥ g f(n) is Θ(g(n)) ≅ f = g f(n) is o(g(n)) ≅ f < g f(n) is ω(g(n)) ≅ f > g

![](images/f12d86fc9b3d393f10b5074ca034faba952b01ed4b945b29b3763e19e30eeb4b.jpg)

• Abuse of notation: $f ( n ) = O ( g ( n ) )$ actually means f(n) ∈O(g(n))

The big O (resp. big Ω) denotes a tight upper (resp. lower) bounds, while the little o (resp. little $\omega$ ) denotes a loose upper (resp. lower) bounds.

### Images:
- data\Design and Analysis of Algorithms\L02-Asymptotic\page_038\L02-Asymptotic_page_038\auto\images\f12d86fc9b3d393f10b5074ca034faba952b01ed4b945b29b3763e19e30eeb4b.jpg

---

## Lecture: L02-Asymptotic\page_039\L02-Asymptotic_page_039\auto

# Practical meaning of big O…

<table><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>constant</td><td rowspan=1 colspan=1>logarithmic</td><td rowspan=1 colspan=1>linear</td><td rowspan=1 colspan=1>N-log-N</td><td rowspan=1 colspan=1>quadratic</td><td rowspan=1 colspan=1>(cicd</td><td rowspan=1 colspan=1>exponential</td></tr><tr><td rowspan=1 colspan=1>n</td><td rowspan=1 colspan=1>0(1)</td><td rowspan=1 colspan=1>O(log n)</td><td rowspan=1 colspan=1>O(n)</td><td rowspan=1 colspan=1>O(n logn)</td><td rowspan=1 colspan=1>0(n2)</td><td rowspan=1 colspan=1>0(n³)</td><td rowspan=1 colspan=1>0(2n)</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1>4</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1>16d</td><td rowspan=1 colspan=1>64</td><td rowspan=1 colspan=1>16</td></tr><tr><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1>24</td><td rowspan=1 colspan=1>64</td><td rowspan=1 colspan=1>512</td><td rowspan=1 colspan=1>256</td></tr><tr><td rowspan=1 colspan=1>16</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>16</td><td rowspan=1 colspan=1>64</td><td rowspan=1 colspan=1>256</td><td rowspan=1 colspan=1>4,096</td><td rowspan=1 colspan=1>65536</td></tr><tr><td rowspan=1 colspan=1>32</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>32</td><td rowspan=1 colspan=1>160</td><td rowspan=1 colspan=1>1,024</td><td rowspan=1 colspan=1>32,768</td><td rowspan=1 colspan=1>4,294,967,296</td></tr><tr><td rowspan=1 colspan=1>64</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>64</td><td rowspan=1 colspan=1>384</td><td rowspan=1 colspan=1>4,069</td><td rowspan=1 colspan=1>262,144</td><td rowspan=1 colspan=1>1.84 x 1019</td></tr></table>

If the unit is in seconds, this would make ${ \sim } 1 0 ^ { 1 1 }$ years…

![](images/e9a01c52c73e7b25fe7549f46ac48fddcae98a5ba74f4286b207b6d9a1bec853.jpg)

### Images:
- data\Design and Analysis of Algorithms\L02-Asymptotic\page_039\L02-Asymptotic_page_039\auto\images\758323b7d4cb99b15140bd815a84813be4e16c76fa04ec1103684e675268fb1f.jpg
- data\Design and Analysis of Algorithms\L02-Asymptotic\page_039\L02-Asymptotic_page_039\auto\images\e9a01c52c73e7b25fe7549f46ac48fddcae98a5ba74f4286b207b6d9a1bec853.jpg

---

## Lecture: L02-Asymptotic\page_040\L02-Asymptotic_page_040\auto

# Constant Factor Factor Rule

Suppose $\operatorname { f } ( \mathrm { n } )$ is ${ \mathrm { 0 } } ( { \mathrm { g } } ( { \mathrm { n } } ) )$ and a is a positive constant. Then, $a \cdot f ( n )$ is also $O ( g ( n ) )$

Proof: By definition, if $\operatorname { f } ( \mathrm { n } )$ is ${ \mathrm { 0 } } ( { \mathrm { g } } ( { \mathrm { n } } ) )$ then there exists two positive constants $n _ { 0 }$ and $c$ such that for all $n \geq n _ { 0 } .$ ,

$$
f ( n ) \leq c \cdot g ( n )
$$

Thus,

$$
\begin{array} { r l } { \cdot f ( n ) \leq } & { { } \cdot c \cdot g ( n ) } \end{array}
$$

We use the constant $a \cdot c$ to show that $a \cdot f ( n )$ is $O ( g ( n ) )$

Multiplying a function by a constant does not change its Big O upper bound since these upper bounds ignore constants

### Images:
- data\Design and Analysis of Algorithms\L02-Asymptotic\page_040\L02-Asymptotic_page_040\auto\images\3be7a43e418f42b2d1707a32490bc8a1ba44fb61e2dfa061d8e45a906c0ff37c.jpg
- data\Design and Analysis of Algorithms\L02-Asymptotic\page_040\L02-Asymptotic_page_040\auto\images\6ac027aaa1ad7d9f93a124cd9effcb8d62be498840551b3504bf4d7198a5368a.jpg

---

## Lecture: L02-Asymptotic\page_041\L02-Asymptotic_page_041\auto

Suppose $f _ { 1 } ( n ) i s O ( g ( n ) )$ and $f _ { 2 } ( n )$ is 0(g (n)). Then, $f _ { 1 } ( n ) + f _ { 2 } ( n ) i s O ( g ( n ) ) .$ (cid:)

Proof: Let $n _ { 1 } , c _ { 1 }$ and $n _ { 2 } , c _ { 2 }$ be constants such that

So, $f _ { 1 } ( n ) + f _ { 2 } ( n ) \leq ( c _ { 1 } + c _ { 2 } ) g ( n )$ , for all $n \geq \operatorname* { m a x } ( n _ { 1 } , n _ { 2 } )$

We can use the constants $c _ { 1 } + c _ { 2 }$ and max $( n _ { 1 } , n _ { 2 } )$ to satisfy the definition.

A sum of two functions is inferior to a sum of two greater functions

---

## Lecture: L02-Asymptotic\page_042\L02-Asymptotic_page_042\auto

Suppose $f _ { 1 } ( n )$ is 0(g(n)) and $f _ { 2 } ( n )$ is 0(g (n)). Then, $f _ { 1 } ( n ) \cdot f _ { 2 } ( n ) i s O ( g _ { 1 } ( n ) \cdot g _ { 2 } ( n ) ) .$

Proof: Let $n _ { 1 } , c _ { 1 }$ and $n _ { 2 } , c _ { 2 }$ be constants such that

So, $f _ { 1 } ( n ) \cdot f _ { 2 } ( n ) \leq ( c _ { 1 } \cdot c _ { 2 } ) \cdot ( g _ { 1 } ( n ) \cdot g _ { 2 } ( n ) )$ ,for all $n \geq$ (cid:) $\operatorname* { m a x } ( n _ { 1 } , n _ { 2 } )$ .

We can use the constants $c _ { 1 } \cdot c _ { 2 }$ and max $( n _ { 1 } , n _ { 2 } )$ to satisfy the definition.

A product of two functions is less than a product of two greater functions

### Images:
- data\Design and Analysis of Algorithms\L02-Asymptotic\page_042\L02-Asymptotic_page_042\auto\images\2680cea58652445292d5d34750f1c3636045af72017bb7d5dd13be90f38600e9.jpg
- data\Design and Analysis of Algorithms\L02-Asymptotic\page_042\L02-Asymptotic_page_042\auto\images\e1b83986a1eff5076f26ba6330e82db75d635e914f63c155ce86cfa52d75b734.jpg

---

## Lecture: L02-Asymptotic\page_043\L02-Asymptotic_page_043\auto

# Transitivity Rule

Suppose $f ( n )$ is $O ( g ( n ) )$ and $g ( n )$ is 0(h(n)). Then, $f ( n ) i s O ( h ( n ) )$

Proof: Let $n _ { 1 } , c _ { 1 }$ and $n _ { 2 } , c _ { 2 }$ be constants such that

So, $f ( n ) \leq ( c _ { 1 } \cdot c _ { 2 } ) h ( n )$ ,for all $n \geq \operatorname* { m a x } ( n _ { 1 } , n _ { 2 } )$ .

We can use the constants $c _ { 1 } \cdot c _ { 2 }$ and $\boldsymbol { \mathrm { m a x } } ( n _ { 1 } , n _ { 2 } )$ to satisfy the definition.

If a function A is greater than function B, and function B is greater than function C, then function A is greater than function C

---

## Lecture: L02-Asymptotic\page_044\L02-Asymptotic_page_044\auto

# Analyzing insertion sort

---

## Lecture: L02-Asymptotic\page_045\L02-Asymptotic_page_045\auto

# O(n²) sorting algorithm: Insertion Sort

<table><tr><td>INSERTION-SORT(A, n)</td><td>Cost times</td></tr><tr><td>for i = 2 to n</td><td>N</td></tr><tr><td>key = A[i]</td><td>n−1</td></tr><tr><td>// Insert A[i] into the sorted subarray A[1 : i — 1].</td><td>n-1</td></tr><tr><td>j = i − 1</td><td>C4 n −1</td></tr><tr><td>while j &gt; 0 and A[j] &gt; key</td><td>C5</td></tr><tr><td>A[j + 1] = A[j] 6</td><td>C6</td></tr><tr><td>j = j − 1</td><td>n C7 ∑i=2(ti − 1)</td></tr><tr><td>A[j + 1] = key 8</td><td>C8 n −1</td></tr></table>

Best case: A is sorted, while loop does not execute.

$$
\operatorname { T } ( n ) = n ( c _ { 1 } + c _ { 2 } + c _ { 4 } + c _ { 5 } + c _ { 8 } ) - ( c _ { 2 } + c _ { 4 } + c _ { 5 }
$$

### Images:
- data\Design and Analysis of Algorithms\L02-Asymptotic\page_045\L02-Asymptotic_page_045\auto\images\2bae3f1d066e10fb4d94ccde534a17ff6a68377393df94923e61f31137565d2d.jpg
- data\Design and Analysis of Algorithms\L02-Asymptotic\page_045\L02-Asymptotic_page_045\auto\images\defcf367b526cf0177ff1080a969a295e659f6981b72240a3490f3a3de7dcd19.jpg

---

## Lecture: L02-Asymptotic\page_046\L02-Asymptotic_page_046\auto

# O(n²) sorting algorithm: Insertion Sort

<table><tr><td>INSERTION-SORT(A, n) Cost</td></tr><tr><td>times for i = 2 to n C1 N</td></tr><tr><td>key = A[i] C2 n− 1</td></tr><tr><td>/ Insert A[i] into the sorted subarray A[1 : i — 1]. 0 n−1</td></tr><tr><td>j = i − 1 C4 n−1 4</td></tr><tr><td>while j &gt; 0 and A[j] &gt; key C5 5 ∠i=2 ti</td></tr><tr><td>A[j + 1] = A[j] (n 6 C6 ∑i=2(ti − 1)</td></tr><tr><td>j = j − 1 (cid:) C7 7 ∑i=2(ti − 1)</td></tr><tr><td>A[j + 1] = key 8 C8 n −1</td></tr></table>

Worse case: A is reverse-ordered. The while loop execute i-1 times for each i

$$
\begin{array} { c } { { = n ( c _ { 1 } + c _ { 2 } + c _ { 4 } + c _ { 8 } - c _ { 6 } - c _ { 7 } ) + \displaystyle { \sum _ { \bf i = 2 } ^ { n } ( i - 1 ) ( c _ { 5 } + c _ { 6 } + } } } \\ { { ( c _ { 1 } + c _ { 2 } + c _ { 4 } + c _ { 8 } - c _ { 6 } - c _ { 7 } ) n + \displaystyle { \frac { n ( n - 1 ) ( c _ { 5 } + c _ { 6 } + c _ { 7 } ) } { 2 } } - } } \end{array}
$$

### Images:
- data\Design and Analysis of Algorithms\L02-Asymptotic\page_046\L02-Asymptotic_page_046\auto\images\1b8b45e2f75dbef3cb7c9340fbe71edde772581a0712fb42b025422fda499928.jpg
- data\Design and Analysis of Algorithms\L02-Asymptotic\page_046\L02-Asymptotic_page_046\auto\images\3555a4897457e8d47f2a16cb3ac9e57ecb550b6447d56a0454de68d95265c8ef.jpg

---

## Lecture: L02-Asymptotic\page_047\L02-Asymptotic_page_047\auto

# O(n²) sorting algorithm: Insertion Sort

<table><tr><td>INSERTION-SORT(A, n) cost</td></tr><tr><td>times for i = 2 to n C1 N</td></tr><tr><td>key = A[i] C2 n−1</td></tr><tr><td>// Insert A[i] into the sorted subarray A[1 : i — 1]. 0 n−1</td></tr><tr><td>j = i -1 C4 n-1</td></tr><tr><td>while j &gt; 0 and A[j] &gt; key C5 ∑n ∠i=2 ti</td></tr><tr><td>A[j + 1] = A[j] C6 ∑i=2(ti − 1) an</td></tr><tr><td>j = j − 1 C7 ∑i=2(ti − 1)</td></tr><tr><td>A[j + 1] = key 8 C8 n−1</td></tr></table>

Average case: The while loop is expected to execute (i-1)/2 times for each i

$$
\begin{array} { l } { { \displaystyle { \mathrm { } _ { ! } ( c _ { 1 } + c _ { 2 } + c _ { 4 } + c _ { 8 } - c _ { 6 } - c _ { 7 } ) + \sum _ { \mathrm { { i } = 2 } } ^ { n } \frac { i - 1 } { 2 } ( c _ { 5 } + c _ { 6 } + c _ { 7 } ) } } } \\ { { \displaystyle { \mathrm { } _ { : 1 } + c _ { 2 } + c _ { 4 } + c _ { 8 } - c _ { 6 } - c _ { 7 } ) n + \frac { n ( n - 1 ) ( c _ { 5 } + c _ { 6 } + c _ { 7 } ) } { 4 } - ( \frac { } { 6 6 } - c _ { 7 } ) } } } \end{array}
$$

### Images:
- data\Design and Analysis of Algorithms\L02-Asymptotic\page_047\L02-Asymptotic_page_047\auto\images\479eefbfacb5c2a698ca828dc6f061d1e0b395081bb6831eeb9cc2fdc934ffd4.jpg
- data\Design and Analysis of Algorithms\L02-Asymptotic\page_047\L02-Asymptotic_page_047\auto\images\aae08956b64dbeb02866f51539e5fd4230784adbba9aef223916b2df0fd03b62.jpg

---

## Lecture: L03-Sorting\page_001\L03-Sorting_page_001\auto

# Sorting algorithms

Sorting Overview

Elementary Sorting Algorithms

-Insertion sort (recap.) Bubble sort — Selection sort

Merge Sort

Quick Sort

---

## Lecture: L03-Sorting\page_002\L03-Sorting_page_002\auto

# The Problem of Sorting

• Input – A sequence of n numbers $<$ a1, a2, …, an> • Output – Permutation $<$ a'1, a'2, …, a'n> such that a'1 ≤ a'2 ≤ … ≤ a'n

• Example – Input: 8 2 4 9 3 6 – Output: 2 3 4 6 8 9 • Sorting is a fundamental operation: – Searching (Binary Search requires sorted arrays) – Data Processing (Efficient indexing in databases) – Graph Algorithms (Kruskal’s algorithm for MST) – Bioinformatics (Sorting datasets before analysis)

---

## Lecture: L03-Sorting\page_003\L03-Sorting_page_003\auto

# Elementary Sorting Algorithms

---

## Lecture: L03-Sorting\page_004\L03-Sorting_page_004\auto

# Insertion Sort (Recap.)

Poker-Style Insertion Sort (magic power)

Table:□5

![](images/d9eda5c7c53beb43c040a871ec16e0369c3d516ab357537a4d2765ab6b44aa71.jpg)

Table:□2

Hand: 5

Poker-Style Insertion Sort (no magic power)

Table: [ -5

![](images/1f5d103628db845961214528929736a54e31a72cc21508ba9627ee3873497aa1.jpg)

![](images/fd1767a9966566e4273a1aea7894143ad0433d216fbb392f0126be3e7fe9697d.jpg)

![](images/0d79bbd7987e54142901814ff4ae4f53b49fb4e4607cdc67af2898510d284cf4.jpg)

![](images/ea7430577a6e037c0eb08d2451eb81da7d859c740fcc1ca28140965bc734da93.jpg)

Table: Hand:1□23 4 5

# Strategy

• Start "empty handed"

•Insert a card in the right position of the already sorted hand

![](images/dfd560d9783d6489afc379415fce056101320b3a40cb06bb158a4c52c08b4072.jpg)

![](images/face0ac2d5fca2063b7c2c1195bf627779edca2b09c95d83376bbb90aa9e9482.jpg)

Table: Hand:I□2 34 5

### Images:
- data\Design and Analysis of Algorithms\L03-Sorting\page_004\L03-Sorting_page_004\auto\images\0d79bbd7987e54142901814ff4ae4f53b49fb4e4607cdc67af2898510d284cf4.jpg
- data\Design and Analysis of Algorithms\L03-Sorting\page_004\L03-Sorting_page_004\auto\images\1f5d103628db845961214528929736a54e31a72cc21508ba9627ee3873497aa1.jpg
- data\Design and Analysis of Algorithms\L03-Sorting\page_004\L03-Sorting_page_004\auto\images\d9eda5c7c53beb43c040a871ec16e0369c3d516ab357537a4d2765ab6b44aa71.jpg
- data\Design and Analysis of Algorithms\L03-Sorting\page_004\L03-Sorting_page_004\auto\images\dfd560d9783d6489afc379415fce056101320b3a40cb06bb158a4c52c08b4072.jpg
- data\Design and Analysis of Algorithms\L03-Sorting\page_004\L03-Sorting_page_004\auto\images\ea7430577a6e037c0eb08d2451eb81da7d859c740fcc1ca28140965bc734da93.jpg
- data\Design and Analysis of Algorithms\L03-Sorting\page_004\L03-Sorting_page_004\auto\images\face0ac2d5fca2063b7c2c1195bf627779edca2b09c95d83376bbb90aa9e9482.jpg
- data\Design and Analysis of Algorithms\L03-Sorting\page_004\L03-Sorting_page_004\auto\images\fd1767a9966566e4273a1aea7894143ad0433d216fbb392f0126be3e7fe9697d.jpg

---

## Lecture: L03-Sorting\page_005\L03-Sorting_page_005\auto

# Insertion Sort (Recap.)

Algorithm InsertionSort(A) Input: An array A with n elements Output: A sorted in non-decreasing order

1. for $\dot { 1 }  2$ to length(A) do   
2. key A[i] // Current element to be inserted   
3. j ← i - 1 // Start comparing from the previous element   
4. while j > 0 and A[j] $>$ key do   
5. A[j + 1] ← A[j] // Shift element to the right   
6. j ← j - 1   
7. end while   
8. $\mathsf { A } [ \mathsf { j } \ + \ \mathsf { 1 } ] \  \ \mathsf { k e y }$ // Place key in the correct position   
9. end for

10. return A // Sorted array

# Insertion Sort Step-by-Step

![](images/896bac6c1f2ed5518cefe2219e972704e124dc3743f0250e1f5459b1c1e10185.jpg)

### Images:
- data\Design and Analysis of Algorithms\L03-Sorting\page_005\L03-Sorting_page_005\auto\images\896bac6c1f2ed5518cefe2219e972704e124dc3743f0250e1f5459b1c1e10185.jpg

---

## Lecture: L03-Sorting\page_006\L03-Sorting_page_006\auto

# One Main Idea for Sorting

• Always consider the array has two portions: the sorted portion followed by the unsorted portion.

– Initially, the sorted portion is empty, and the entire array is unsorted. – Enlarge the sorted portion by adding one more number in every iteration, and shrink the unsorted portion accordingly.

• Insertion sort is an instance of this idea. This lecture will introduce two more algorithms using this idea.

---

## Lecture: L03-Sorting\page_007\L03-Sorting_page_007\auto

# One Main Idea for Sorting

• Always consider the array has two portions: a sorted portion and a unsorted portion.

• Initially, the sorted portion is empty, and the entire array is unsorted.

• Enlarge the sorted portion by adding one more number in every iteration, and shrink the unsorted portion accordingly.

• Insertion sort is an instance of this idea. This lecture will introduce two more algorithms using this idea.

---

## Lecture: L03-Sorting\page_008\L03-Sorting_page_008\auto

# Bubble Sort: "Bubbling Up" the Largest Element

• Traverse a collection of elements

• Move from the front to the end

• “Bubble” the largest value to the end using pair-wise comparisons and swapping

<table><tr><td rowspan=1 colspan=1>77</td><td rowspan=1 colspan=1>42</td><td rowspan=1 colspan=1>35</td><td rowspan=1 colspan=1>12</td><td rowspan=1 colspan=1>101</td><td rowspan=1 colspan=1>5</td></tr></table>

### Images:
- data\Design and Analysis of Algorithms\L03-Sorting\page_008\L03-Sorting_page_008\auto\images\7639bf231a7a8f260d4541e2b715c27c376b861eafe8e5c94356f06a25333c27.jpg

---

## Lecture: L03-Sorting\page_009\L03-Sorting_page_009\auto

# Bubble Sort: "Bubbling Up" the Largest Element

• Traverse a collection of elements

• Move from the front to the end

• “Bubble” the largest value to the end using pair-wise comparisons and swapping

![](images/f1619ea40ea1add31e47e157d8ead0a19fd020596c3fcea92fa39b028e22c279.jpg)

### Images:
- data\Design and Analysis of Algorithms\L03-Sorting\page_009\L03-Sorting_page_009\auto\images\f1619ea40ea1add31e47e157d8ead0a19fd020596c3fcea92fa39b028e22c279.jpg

---

## Lecture: L03-Sorting\page_010\L03-Sorting_page_010\auto

# Bubble Sort: "Bubbling Up" the Largest Element

• Traverse a collection of elements

• Move from the front to the end

• “Bubble” the largest value to the end using pair-wise comparisons and swapping

![](images/a1bdea7849b16091fd01a809a4a62667cebfe14eae76ba3ba35623b629549a19.jpg)

### Images:
- data\Design and Analysis of Algorithms\L03-Sorting\page_010\L03-Sorting_page_010\auto\images\a1bdea7849b16091fd01a809a4a62667cebfe14eae76ba3ba35623b629549a19.jpg

---

## Lecture: L03-Sorting\page_011\L03-Sorting_page_011\auto

# Bubble Sort: "Bubbling Up" the Largest Element

• Traverse a collection of elements

• Move from the front to the end

• “Bubble” the largest value to the end using pair-wise comparisons and swapping

![](images/212c899bf2ac2e07a60096b73c855c2b7b2762748b2d2fa0b027a169c49706db.jpg)

### Images:
- data\Design and Analysis of Algorithms\L03-Sorting\page_011\L03-Sorting_page_011\auto\images\212c899bf2ac2e07a60096b73c855c2b7b2762748b2d2fa0b027a169c49706db.jpg

---

## Lecture: L03-Sorting\page_012\L03-Sorting_page_012\auto

# Bubble Sort: "Bubbling Up" the Largest Element

• Traverse a collection of elements

• Move from the front to the end

• “Bubble” the largest value to the end using pair-wise comparisons and swapping

![](images/01c5de315713b3e5dae55cbe1ff9257c17dcf1ee648ef5758ccefe6a95fb6dbc.jpg)

No need to swap

### Images:
- data\Design and Analysis of Algorithms\L03-Sorting\page_012\L03-Sorting_page_012\auto\images\01c5de315713b3e5dae55cbe1ff9257c17dcf1ee648ef5758ccefe6a95fb6dbc.jpg

---

## Lecture: L03-Sorting\page_013\L03-Sorting_page_013\auto

# Bubble Sort: "Bubbling Up" the Largest Element

• Traverse a collection of elements

• Move from the front to the end

• “Bubble” the largest value to the end using pair-wise comparisons and swapping

<table><tr><td colspan="5"></td></tr><tr><td>42</td><td>35</td><td>12</td><td>77</td><td>101</td></tr></table>

### Images:
- data\Design and Analysis of Algorithms\L03-Sorting\page_013\L03-Sorting_page_013\auto\images\6a764863ed2474b82452d540d6ef76cf4d52bd6573c1bf2d319230c84553a1df.jpg

---

## Lecture: L03-Sorting\page_014\L03-Sorting_page_014\auto

# Bubble Sort: "Bubbling Up" the Largest Element

• Traverse a collection of elements

• Move from the front to the end

• “Bubble” the largest value to the end using pair-wise comparisons and swapping

<table><tr><td rowspan=1 colspan=1>42</td><td rowspan=1 colspan=1>35</td><td rowspan=1 colspan=1>12</td><td rowspan=1 colspan=1>77</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>101</td></tr></table>

# Largest value correctly placed

### Images:
- data\Design and Analysis of Algorithms\L03-Sorting\page_014\L03-Sorting_page_014\auto\images\75c69185d0258e5aa3aef94c4429045b155b9b688c87fffc7655aef70a60e4d7.jpg

---

## Lecture: L03-Sorting\page_015\L03-Sorting_page_015\auto

# The “Bubble Up” Algorithm

index ← 1

last_compare_at ← n – 1

while index < last_compare_at+1 if(A[index] > A[index + 1]) then

Swap(A[index], A[index + 1])

end if

index ← index + 1 end while

---

## Lecture: L03-Sorting\page_016\L03-Sorting_page_016\auto

# Items of Interest

● Notice that only the largest value is correctly placed

All other values are still out of order

So we need to repeat this process

<table><tr><td rowspan=1 colspan=1>42</td><td rowspan=1 colspan=1>35</td><td rowspan=1 colspan=1>12</td><td rowspan=1 colspan=1>77</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>101</td></tr></table>

# Largest value correctly placed

### Images:
- data\Design and Analysis of Algorithms\L03-Sorting\page_016\L03-Sorting_page_016\auto\images\5d6db1d23c4f2714cf09efe569c3815fc05091252039c8342921084c8149464f.jpg

---

## Lecture: L03-Sorting\page_017\L03-Sorting_page_017\auto

# Repeat “Bubble Up” How Many Times?

If we have N elements …   
And if each time we bubble an element, we place it in its correct location …   
Then we repeat the “bubble up” process N – 1 times   
• This guarantees we’ll correctly place all N elements

---

## Lecture: L03-Sorting\page_018\L03-Sorting_page_018\auto

# “Bubbling” All the Elements

![](images/9604e7d28663ae9afabc992a37d454fbef2fd748444f0c2140c0f547e6aa60d4.jpg)

### Images:
- data\Design and Analysis of Algorithms\L03-Sorting\page_018\L03-Sorting_page_018\auto\images\9604e7d28663ae9afabc992a37d454fbef2fd748444f0c2140c0f547e6aa60d4.jpg

---

## Lecture: L03-Sorting\page_019\L03-Sorting_page_019\auto

# Reducing the Number of Comparisons

<table><tr><td rowspan=1 colspan=1>77</td><td rowspan=1 colspan=1>42</td><td rowspan=1 colspan=1>35</td><td rowspan=1 colspan=1>12</td><td rowspan=1 colspan=1>101</td><td rowspan=1 colspan=1>5</td></tr></table>

<table><tr><td rowspan=1 colspan=1>42</td><td rowspan=1 colspan=1>35</td><td rowspan=1 colspan=1>12</td><td rowspan=1 colspan=1>77</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>101</td></tr></table>

<table><tr><td rowspan=2 colspan=2>35</td><td rowspan=1 colspan=1>35</td><td rowspan=1 colspan=1>12</td><td rowspan=1 colspan=1>42</td><td rowspan=1 colspan=1></td><td rowspan=2 colspan=1>77</td></tr><tr><td rowspan=1 colspan=1></td><td></td><td></td><td></td></tr></table>

<table><tr><td rowspan=1 colspan=1>12</td><td rowspan=1 colspan=1>35</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>42</td><td rowspan=2 colspan=1>77</td><td rowspan=2 colspan=1>101</td></tr><tr><td></td><td></td><td></td><td></td></tr></table>

<table><tr><td rowspan=1 colspan=1>12</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>35</td><td rowspan=1 colspan=1>42</td><td rowspan=1 colspan=1>77</td><td rowspan=1 colspan=1>101</td></tr></table>

### Images:
- data\Design and Analysis of Algorithms\L03-Sorting\page_019\L03-Sorting_page_019\auto\images\0b410bc640cdbc2b50db236ebceea02f9fc1ae2361a0cbd25438d342c80a76a0.jpg
- data\Design and Analysis of Algorithms\L03-Sorting\page_019\L03-Sorting_page_019\auto\images\5f192ed0d880ba622381981658342f6db6c0fa07df2abf7e5f1128024bf55af1.jpg
- data\Design and Analysis of Algorithms\L03-Sorting\page_019\L03-Sorting_page_019\auto\images\7eabce593dac212522e6ffcdf3b995c64b826b0b1b2ffcdc959f041f86a85a6b.jpg
- data\Design and Analysis of Algorithms\L03-Sorting\page_019\L03-Sorting_page_019\auto\images\9efc83eecc03a4fb5bba9291fbbe9863b139d2b73dc8d03872c4935f84015b24.jpg
- data\Design and Analysis of Algorithms\L03-Sorting\page_019\L03-Sorting_page_019\auto\images\f0e0113c15017dea236acac43ab4f284c232508ba8e27dd8444d7e2777744ae0.jpg

---

## Lecture: L03-Sorting\page_020\L03-Sorting_page_020\auto

# Reducing the Number of Comparisons

• On the Nth “bubble up”, we only need to do MAX – N comparisons

For example:

• This is the 4th “bubble up” • MAX is 6 • Thus we have 2 comparisons to do

<table><tr><td rowspan=1 colspan=1>12</td><td rowspan=1 colspan=1>35</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>42</td><td rowspan=1 colspan=1>77</td><td rowspan=1 colspan=1>101</td></tr></table>

![](images/5a9459efb0be2689cad0688745d92b39fcfa3da1cca13113538179840627126a.jpg)

### Images:
- data\Design and Analysis of Algorithms\L03-Sorting\page_020\L03-Sorting_page_020\auto\images\17d1d8fae653ca68756042b7aed9c333435e31cef51a5249a81cf48b5f70ee77.jpg
- data\Design and Analysis of Algorithms\L03-Sorting\page_020\L03-Sorting_page_020\auto\images\5a9459efb0be2689cad0688745d92b39fcfa3da1cca13113538179840627126a.jpg

---

## Lecture: L03-Sorting\page_021\L03-Sorting_page_021\auto

# Putting It All Together

![](images/631a70d79925c2defae08b4d25e70d5dc7063b8d35493d74b0051f05991fe7e5.jpg)

### Images:
- data\Design and Analysis of Algorithms\L03-Sorting\page_021\L03-Sorting_page_021\auto\images\631a70d79925c2defae08b4d25e70d5dc7063b8d35493d74b0051f05991fe7e5.jpg

---

## Lecture: L03-Sorting\page_022\L03-Sorting_page_022\auto

# Already Sorted Collections?

What if the collection was already sorted?

What if only a few elements were out of place and after a couple of “bubble ups,” the collection was sorted?

• We want to be able to detect this and “stop early”!

<table><tr><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>12</td><td rowspan=1 colspan=1>35</td><td rowspan=1 colspan=1>42</td><td rowspan=1 colspan=1>77</td><td rowspan=1 colspan=1>101</td></tr></table>

### Images:
- data\Design and Analysis of Algorithms\L03-Sorting\page_022\L03-Sorting_page_022\auto\images\e404866a24e4ec1efa5e4d27a4cedceff2350a82267bd48e723b129e424e73fd.jpg

---

## Lecture: L03-Sorting\page_023\L03-Sorting_page_023\auto

# Using a Boolean “Flag”

We can use a boolean variable to determine if any swapping occurred during the “bubble up”

If no swapping occurred, then we know that the collection is already sorted!

This boolean “flag” needs to be reset after each “bubble up”

---

## Lecture: L03-Sorting\page_024\L03-Sorting_page_024\auto

# Pseudo-Code

algorithm Bubblesort(A) to_do: index isoftype Num did_swap: Boolean t $) \_ \mathrm { ~ d }  \textsf { N } - \texttt { 1 }$ did_swap true

while (to_do>0) or (not did_swap): index $ 1$ did_swap false while index<to_ ${ \mathsf { d o } } { + } 1$ if(A[index] > A[index + 1]) then Swap(A[index], A[index + 1]) did_swap true endif index index + 1 end while to_do to_do – 1 end while

---

## Lecture: L03-Sorting\page_025\L03-Sorting_page_025\auto

# Selection sort

• Continuously finds the smallest element from the unsorted part and swaps it with the first unsorted position.

Input: An array A of size n (1-based index)   
Output: A sorted array A in non-decreasing order   
Algorithm SelectionSort(A, n): for $\dot { \mathrm { ~ \bf ~ i ~ } }  1$ to n do min_index i for $\textbf { j }  \textbf { i } + 1$ to n do if A[j] < A[min_index] then min_index j swap A[i] and A[min_index] return A

<table><tr><td rowspan=1 colspan=1>Pass</td><td rowspan=1 colspan=1>Unsorted Part</td><td rowspan=1 colspan=1>Min Element</td><td rowspan=1 colspan=1>Swap</td><td rowspan=1 colspan=1>Updated Array</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>[6, 3, 8, 5, 2]</td><td rowspan=1 colspan=1>2 (at index 5)</td><td rowspan=1 colspan=1>Swap A[1] ↔ A[5]</td><td rowspan=1 colspan=1>[2.3, 8, 5, 6]</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>[3, 8, 5, 6]</td><td rowspan=1 colspan=1>3(at index 2)</td><td rowspan=1 colspan=1>No swap needed</td><td rowspan=1 colspan=1>2.38, 5, 6]</td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>[8, 5, 6]</td><td rowspan=1 colspan=1>5(at index 4)</td><td rowspan=1 colspan=1>Swap A[3] ↔A[4]</td><td rowspan=1 colspan=1>2.3.58,6]</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>[8, 6]</td><td rowspan=1 colspan=1>6 (at index 5)</td><td rowspan=1 colspan=1>Swap A[4] ↔ A[5]</td><td rowspan=1 colspan=1>2.3,5,618]</td></tr><tr><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>[8]</td><td rowspan=1 colspan=1>No need to swap</td><td rowspan=1 colspan=1>Done</td><td rowspan=1 colspan=1>[2,3,5,6,8]</td></tr></table>

### Images:
- data\Design and Analysis of Algorithms\L03-Sorting\page_025\L03-Sorting_page_025\auto\images\e8e32bf6adce2d55948e59eae96b598f96e94ada2c9c2e24758e0d8e1e00f1ce.jpg

---

## Lecture: L03-Sorting\page_026\L03-Sorting_page_026\auto

# Comparison of elementary sorting algorithms

# • Number of Comparisons

Bubble Sort: ${ \mathsf { O } } ( { \mathsf { n } } ^ { 2 } )$ comparisons (compares adjacent elements in every pass). Selection Sort: ${ \mathsf { O } } ( { \mathsf { n } } ^ { 2 } )$ comparisons (finds the minimum element in each pass). Insertion Sort: ${ \mathsf { O } } ( { \mathsf { n } } ^ { 2 } )$ comparisons (worst case), but O(n) for nearly sorted array

# • Number of Swaps

Bubble Sort: ${ \mathsf { O } } ( { \mathsf { n } } ^ { 2 } )$ swaps (every adjacent swap is performed).   
– Selection Sort: O(n) swaps (only one swap per pass). Insertion Sort: O(n) swaps (only shifts elements when needed); fewer swaps in nearly sorted cases.

• Best Case vs. Worst Case

Bubble Sort: Best case O(n) (if already sorted, it can stop early).   
Selection Sort: Always ${ \mathsf { O } } ( { \mathsf { n } } ^ { 2 } )$ (even if sorted, it always scans the full array).   
Insertion Sort: Best case O(n) (if sorted, only checks each element once).

# • Stability and Adaptability

– Bubble Sort and Insertion Sort are stable (maintain the order of equal elements); and adaptive (take advantage of partially sorted data).   
– Selection sort always scans the full array, and may reorder equal elements.

---

## Lecture: L03-Sorting\page_027\L03-Sorting_page_027\auto

# Comparison of elementary sorting algorithms

![](images/7016ff2e84a4f59a370607ab2d82fd6e50054522372173038fd5249f32bfbe46.jpg)  
Sorting 1000 Random Numbers Over 10 Runs (Mean ± Std)

### Images:
- data\Design and Analysis of Algorithms\L03-Sorting\page_027\L03-Sorting_page_027\auto\images\7016ff2e84a4f59a370607ab2d82fd6e50054522372173038fd5249f32bfbe46.jpg

---

## Lecture: L03-Sorting\page_028\L03-Sorting_page_028\auto

# A Simple Algorithm for Sorting?

Consider an array $\cdot$ of ???? integers. Every integer is in the range of $[ 1 , U ]$ , where $U \geq n$ . Example: [2,3,8,7,1,2,2,2,7,3,9,8,2,1,4,2,4,6,9,2].

A simple and direct approach to make these numbers in order:

1. Create a Count Array $B$ of length $U$ . Initialize $B$ by setting all its cells to 0.

2. Count the Occurrences: For every $i \in [ 0 , n - 1 ]$ , increase $B \left[ A [ i ] \right] \mathsf { b y } 1 $ .

3. Generate the sorted order as follows (set $A$ to empty):

$- \mathsf { F o r } x \ = \ 1 \mathsf { t o } \ U$ • while $B [ x ] > 0$ do – append integer $x$ to $A$ . $- \ B [ x ] \ = \ B [ x ] \ - \ 1$

### Images:
- data\Design and Analysis of Algorithms\L03-Sorting\page_028\L03-Sorting_page_028\auto\images\c24685aae430261813836e6a73efc9558d2666920f7d673577670c36d0461621.jpg

---

## Lecture: L03-Sorting\page_029\L03-Sorting_page_029\auto

Consider a collection of integers: [2,3,8,7,1,2,2,2,7,3,9,8,2,1,4,2,4,6,9,2].

A simple and direct approach to make these numbers in order:

1. Create a Count Array   
2. Count the Occurrences   
3. Traverse and output

![](images/cc7917756205ba29fa3aa6d2e2a5c4cb979c1709d4e3936615ab94bbbaea3e34.jpg)

### Images:
- data\Design and Analysis of Algorithms\L03-Sorting\page_029\L03-Sorting_page_029\auto\images\cc7917756205ba29fa3aa6d2e2a5c4cb979c1709d4e3936615ab94bbbaea3e34.jpg

---

## Lecture: L03-Sorting\page_030\L03-Sorting_page_030\auto

# A Simple Algorithm for Sorting?

The algorithm is called counting sort. It can handles a special case of the sorting problem where the integers come from a small domain.

Two main properties:

• Non-Comparison-Based: Relies on counting the frequency of elements and using array indices rather than comparisons.

• Limited Applicability: Only works for integers or discrete data that can be mapped to integers.

---

## Lecture: L03-Sorting\page_031\L03-Sorting_page_031\auto

# Analysis of Counting Sort

• Steps 1 and 3 take $O ( U )$ time.

• Step 2 takes $O ( n )$ time.

• Therefore, the overall running time of counting sort is $O ( n + U ) =$ $O ( U )$ .

• For small $U = O ( n )$ (e.g., 1000????), the counting sort runs in ????(????) time.

---

## Lecture: L03-Sorting\page_032\L03-Sorting_page_032\auto

# Comparison Among Sorting Algorithms

<table><tr><td rowspan=1 colspan=1>SortingAlgorithm</td><td rowspan=1 colspan=1>Time Complexity</td><td rowspan=1 colspan=1>SpaceComplexity</td><td rowspan=1 colspan=1>Stability</td></tr><tr><td rowspan=1 colspan=1>Insertion Sort</td><td rowspan=1 colspan=1>- Best: O(n) (sorted)- Worst: O(n²)</td><td rowspan=1 colspan=1>0(1)</td><td rowspan=1 colspan=1>Stable</td></tr><tr><td rowspan=1 colspan=1>Bubble Sort</td><td rowspan=1 colspan=1>- Best: O(n) (sorted)- Worst: O(n²)</td><td rowspan=1 colspan=1>0(1)</td><td rowspan=1 colspan=1>Stable</td></tr><tr><td rowspan=1 colspan=1>Selection Sort</td><td rowspan=1 colspan=1>- 0(n²)</td><td rowspan=1 colspan=1>0(1)</td><td rowspan=1 colspan=1>Not Stable</td></tr><tr><td rowspan=1 colspan=1>Counting Sort</td><td rowspan=1 colspan=1>-O(n+U)</td><td rowspan=1 colspan=1>o(u)</td><td rowspan=1 colspan=1>Stable</td></tr></table>

An algorithm is stable if numbers with the same value appear in the output array in the same order as they do in the input array.

### Images:
- data\Design and Analysis of Algorithms\L03-Sorting\page_032\L03-Sorting_page_032\auto\images\0f750b32e7fdb4eeb72de7a0fbc7ce639e5c87468f7feef85363a8a9339d6227.jpg

---

## Lecture: L03-Sorting\page_033\L03-Sorting_page_033\auto

# Merge Sort

---

## Lecture: L03-Sorting\page_034\L03-Sorting_page_034\auto

# The Problem with O(n²) Sorting Algorithms

<table><tr><td rowspan=1 colspan=1>Algorithm</td><td rowspan=1 colspan=1>Comparisons (Worst Case)</td><td rowspan=1 colspan=1>Swaps (Worst Case)</td></tr><tr><td rowspan=1 colspan=1>Bubble Sort</td><td rowspan=1 colspan=1>O(n²)</td><td rowspan=1 colspan=1>O(n²)</td></tr><tr><td rowspan=1 colspan=1>Selection Sort</td><td rowspan=1 colspan=1>O(n²)</td><td rowspan=1 colspan=1>o(n)</td></tr><tr><td rowspan=1 colspan=1>Insertion Sort</td><td rowspan=1 colspan=1>O(n²)</td><td rowspan=1 colspan=1>o(n)</td></tr></table>

# • We need a sorting method that reduces swaps and comparisons.

![](images/29aebdf56818921ec619369f523ebba956695e9816e1e3948728c76c763573c0.jpg)  
Bubble Sort Performance: Sorting 100 Values (10 Times) vs. 1000 Values (Once)

### Images:
- data\Design and Analysis of Algorithms\L03-Sorting\page_034\L03-Sorting_page_034\auto\images\29aebdf56818921ec619369f523ebba956695e9816e1e3948728c76c763573c0.jpg
- data\Design and Analysis of Algorithms\L03-Sorting\page_034\L03-Sorting_page_034\auto\images\b6ea15466d7177a842a438ba566882dd37b96349a24ca28dd073e09c7a26be52.jpg

---

## Lecture: L03-Sorting\page_035\L03-Sorting_page_035\auto

# How Would You Sort 1000 Pieces of Paper?

• Method A: Uses Insertion Sort strategy (picking one paper at a time and inserting it in order).

• Method B: Uses Merge-like strategy (first sorts small sections, then merges them together).

– How many comparisons are needed for merging two sorted sections?

• Result: Method B finishes much faster!

• Lesson: Sorting small sections first, then merging, is faster than moving elements one by one.

– Fewer swaps and comparisons $=$ faster sorting!

– Merging sorted sections is easier than sorting everything from scratch.

---

## Lecture: L03-Sorting\page_036\L03-Sorting_page_036\auto

Algorithm Merge-Sort A[1 . . n]

1. If n = 1, done

2. Recursively sort A[ 1 . . n/2 ] and $A [ \lceil n / 2 \rceil { + } 1$ . . n ]

3. “ $M e r g e ^ { 9 9 }$ the 2 sorted lists

Key subroutine: MERGE

---

## Lecture: L03-Sorting\page_037\L03-Sorting_page_037\auto

# Merging Two Sorted Arrays (Algo. Merge)

![](images/48044a13cf4e536837226bbeef4497b8c04f5fc00fd7ce55208e2b9698cf3927.jpg)

${ \mathrm { T i m e } } = \Theta ( n )$ to merge a total of n elements (linear time)

### Images:
- data\Design and Analysis of Algorithms\L03-Sorting\page_037\L03-Sorting_page_037\auto\images\48044a13cf4e536837226bbeef4497b8c04f5fc00fd7ce55208e2b9698cf3927.jpg

---

## Lecture: L03-Sorting\page_038\L03-Sorting_page_038\auto

# Merge-Sort Example

![](images/b8326ec67ecf8d5876346e1e089b82e1042c233ce34400e25e683f2e4db87266.jpg)

![](images/658917938ddc9f7027ac151fd0e98c2856538bb0ae2c6b5b9f99b17fa9b01bc6.jpg)

### Images:
- data\Design and Analysis of Algorithms\L03-Sorting\page_038\L03-Sorting_page_038\auto\images\658917938ddc9f7027ac151fd0e98c2856538bb0ae2c6b5b9f99b17fa9b01bc6.jpg
- data\Design and Analysis of Algorithms\L03-Sorting\page_038\L03-Sorting_page_038\auto\images\b8326ec67ecf8d5876346e1e089b82e1042c233ce34400e25e683f2e4db87266.jpg

---

## Lecture: L03-Sorting\page_039\L03-Sorting_page_039\auto

# Analyzing Merge Sort

MERGE-SORT $A [ 1 \ldots n ]$

1. If $n = 1$ , done

![](images/237b49bc4421f71e87a943aef33f2e2119eb281cfb2cfa05baa659b646d950a1.jpg)

2. Recursively sort A[ 1 . . n/2 ] and A[ n/2+1 . . n ]

3. “Merge” the $2$ sorted lists

Sloppiness: Should be $T ( \lceil n / 2 \rceil ) + T ( \lfloor n / 2 \rfloor ) .$ but it turns out not to matter asymptotically.

### Images:
- data\Design and Analysis of Algorithms\L03-Sorting\page_039\L03-Sorting_page_039\auto\images\237b49bc4421f71e87a943aef33f2e2119eb281cfb2cfa05baa659b646d950a1.jpg

---

## Lecture: L03-Sorting\page_040\L03-Sorting_page_040\auto

# Recurrence for Merge Sort

$$
T ( n ) = { \left\{ \begin{array} { l l } { \Theta ( 1 ) { \mathrm { i f } } n = 1 ; } \\ { 2 T ( n / 2 ) + \Theta ( n ) { \mathrm { i f } } n > 1 . } \end{array} \right. }
$$

• We shall usually omit stating the base case when $T ( n ) = \Theta ( 1 )$ for sufficiently small n, but only when it has no effect on the asymptotic solution to the recurrence.

• CLRS provides several ways to find a good upper bound on T(n).

### Images:
- data\Design and Analysis of Algorithms\L03-Sorting\page_040\L03-Sorting_page_040\auto\images\1ba1e7c67ec0c5b19639bd85d161f9243b3d720454fc98564c969119b2ee9b5f.jpg

---

## Lecture: L03-Sorting\page_041\L03-Sorting_page_041\auto

Solve $T ( n ) = 2 T ( n / 2 ) + c n$ , where $c > 0$ is constant.

---

## Lecture: L03-Sorting\page_042\L03-Sorting_page_042\auto

Solve $T ( n ) = 2 T ( n / 2 ) + c n$ , where $c > 0$ is constant. T(n)

---

## Lecture: L03-Sorting\page_043\L03-Sorting_page_043\auto

Solve $T ( n ) = 2 T ( n / 2 ) + c n$ , where $c > 0$ is constant.

![](images/1ded25f3ac1ada0fddd5b6fd18fd0080c563c2ff7214290ddd0c6972c512e181.jpg)

### Images:
- data\Design and Analysis of Algorithms\L03-Sorting\page_043\L03-Sorting_page_043\auto\images\1ded25f3ac1ada0fddd5b6fd18fd0080c563c2ff7214290ddd0c6972c512e181.jpg

---

## Lecture: L03-Sorting\page_044\L03-Sorting_page_044\auto

Solve $T ( n ) = 2 T ( n / 2 ) + c n$ , where $c > 0$ is constant.

![](images/5cca21b0fc9a78bb8706c84d707d52805978e8cc09dcda1a85d77a82f28e4980.jpg)

### Images:
- data\Design and Analysis of Algorithms\L03-Sorting\page_044\L03-Sorting_page_044\auto\images\5cca21b0fc9a78bb8706c84d707d52805978e8cc09dcda1a85d77a82f28e4980.jpg

---

## Lecture: L03-Sorting\page_045\L03-Sorting_page_045\auto

Solve $T ( n ) = 2 T ( n / 2 ) + c n$ , where $c > 0$ is constant.

![](images/6d0bd5bb48cdcda4fe201d8e7eada3a1076cafa3470db8ca33104f736b780f9d.jpg)

Θ(1)

### Images:
- data\Design and Analysis of Algorithms\L03-Sorting\page_045\L03-Sorting_page_045\auto\images\6d0bd5bb48cdcda4fe201d8e7eada3a1076cafa3470db8ca33104f736b780f9d.jpg

---

## Lecture: L03-Sorting\page_046\L03-Sorting_page_046\auto

Solve $T ( n ) = 2 T ( n / 2 ) + c n$ , where $c > 0$ is constant.

![](images/c990d1df9ff4ca33edc974ccdaa86c842f468f7cddf9ccb98d6ff281145463a2.jpg)

### Images:
- data\Design and Analysis of Algorithms\L03-Sorting\page_046\L03-Sorting_page_046\auto\images\c990d1df9ff4ca33edc974ccdaa86c842f468f7cddf9ccb98d6ff281145463a2.jpg

---

## Lecture: L03-Sorting\page_047\L03-Sorting_page_047\auto

Solve $T ( n ) = 2 T ( n / 2 ) + c n$ , where $c > 0$ is constant.

![](images/dd95d2ef6c07906115e847a5c48bc635b2a857476d76ba6ce586bb42bda2de9a.jpg)

### Images:
- data\Design and Analysis of Algorithms\L03-Sorting\page_047\L03-Sorting_page_047\auto\images\dd95d2ef6c07906115e847a5c48bc635b2a857476d76ba6ce586bb42bda2de9a.jpg

---

## Lecture: L03-Sorting\page_048\L03-Sorting_page_048\auto

Solve $T ( n ) = 2 T ( n / 2 ) + c n$ , where $c > 0$ is constant.

![](images/bb09c97ed6bdd4ed2b12c0e6ac0afd3da6b299461434de1abfd231a529b3ad21.jpg)

### Images:
- data\Design and Analysis of Algorithms\L03-Sorting\page_048\L03-Sorting_page_048\auto\images\bb09c97ed6bdd4ed2b12c0e6ac0afd3da6b299461434de1abfd231a529b3ad21.jpg

---

## Lecture: L03-Sorting\page_049\L03-Sorting_page_049\auto

Solve $T ( n ) = 2 T ( n / 2 ) + c n .$ , where $c > 0$ is constant.

![](images/66d140adbd2fc77cffd804074a3bb21d602339c62eda70d9cafdde0ff3a6945b.jpg)

### Images:
- data\Design and Analysis of Algorithms\L03-Sorting\page_049\L03-Sorting_page_049\auto\images\66d140adbd2fc77cffd804074a3bb21d602339c62eda70d9cafdde0ff3a6945b.jpg

---

## Lecture: L03-Sorting\page_050\L03-Sorting_page_050\auto

# Recursion Tree

Solve $T ( n ) = 2 T ( n / 2 ) + c n .$ , where $c > 0$ is constant.

![](images/ea9404b4e9b67010ddfd1740bfa6ebd5cae390f659c7895b96f217f6330e71c7.jpg)

### Images:
- data\Design and Analysis of Algorithms\L03-Sorting\page_050\L03-Sorting_page_050\auto\images\ea9404b4e9b67010ddfd1740bfa6ebd5cae390f659c7895b96f217f6330e71c7.jpg

---

## Lecture: L03-Sorting\page_051\L03-Sorting_page_051\auto

# Recursion Tree

Solve $T ( n ) = 2 T ( n / 2 ) + c n$ , where $c > 0$ is constant.

![](images/ce71f4137db71593a05d74d31b3ec968c31830eef7361ce5fe784485465a3814.jpg)

### Images:
- data\Design and Analysis of Algorithms\L03-Sorting\page_051\L03-Sorting_page_051\auto\images\ce71f4137db71593a05d74d31b3ec968c31830eef7361ce5fe784485465a3814.jpg

---

## Lecture: L03-Sorting\page_052\L03-Sorting_page_052\auto

# Sort Algorithms Performance

![](images/f775277b2ac281635a316993641aad275a063f93e3e69edf6a1c0013f95d1a0d.jpg)  
Sorting Algorithm Performance on 1000 Elements Over 5 Runs (Mean ± Std)

### Images:
- data\Design and Analysis of Algorithms\L03-Sorting\page_052\L03-Sorting_page_052\auto\images\f775277b2ac281635a316993641aad275a063f93e3e69edf6a1c0013f95d1a0d.jpg

---

## Lecture: L03-Sorting\page_053\L03-Sorting_page_053\auto

# Conclusions

$\Theta ( n \lg n )$ grows more slowly than $\Theta ( n ^ { 2 } )$ .

• Therefore, merge sort asymptotically beats insertion sort in the worst case.

• In practice, merge sort beats insertion sort for $n > 3 0$ or so.

• Go test it out for yourself!

---

## Lecture: L03-Sorting\page_054\L03-Sorting_page_054\auto

# Quick Sort

---

## Lecture: L03-Sorting\page_055\L03-Sorting_page_055\auto

# Merge Sort Weaknesses

• Requires extra space. • Slower in practice due to copying.  We need in-place sorting

Algorithm Merge(A, left, mid, right): Create two temporary arrays: Left[] and Right[] Copy elements from A[left:mid] into Left[] Copy elements from A[mid+1:right] into Right[] $\mathrm { ~ \underline { ~ } { ~ } ~ } \gets \mathrm { ~ \underline { ~ } { ~ } ~ } ,$ j ← 1, k ← left while i ≤ length(Left) and j ≤ length(Right) do if Left[i] ≤ Right[j] then A[k] Left[i] i ← i + 1 else A[k] ← Right[j] j ← j + 1 $k \gets \mathrm { ~ k ~ } + \mathrm { ~ 1 ~ }$ while i ≤ length(Left) do A[k] Left[i] i ← i + 1 $k \gets \mathrm { ~ k ~ } + \mathrm { ~ 1 ~ }$ while j ≤ length(Right) do A[k] Right[j] j ← j + 1 k ← k + 1

---

## Lecture: L03-Sorting\page_056\L03-Sorting_page_056\auto

# Sorting Papers on a Table Revisits

• Imagine sorting 1000 papers on a tiny table.

Merge Sort Approach:

Split into smaller piles, sort them separately, then merge.

• Problem: Needs extra space for temporary piles.

• Quick Sort Approach:

• Pick a pivot (e.g., middle paper).

• Move smaller papers to the left, larger papers to the right.

の Repeat sorting within the same space.

---

## Lecture: L03-Sorting\page_057\L03-Sorting_page_057\auto

# Quick Sort

• A popular sorting algorithm discovered by C.A.R. Hoare in 1962 – In many situations, it’s the fastest, in $O ( n \log n )$ time (for in-memory sorting)

• Basic scheme

– Partition: partition an array into two subarrays around a pivot ???? such that elements in left subarray $\leq x \leq$ the elements

<table><tr><td>≤x</td><td>X</td><td>Mx</td></tr></table>

Recursion: recursively apply quicksort to each of the two subarrays

### Images:
- data\Design and Analysis of Algorithms\L03-Sorting\page_057\L03-Sorting_page_057\auto\images\a9cabc9133c3e1df469fe61dbec422d32d9bc097a4bad26b7452b0e429262bd2.jpg

---

## Lecture: L03-Sorting\page_058\L03-Sorting_page_058\auto

# Quick Sort (Pseudo-Code)

QUICKSORT(A, p, r) if p < r $q \gets \mathrm { P A R T I T I O N } ( A , p , r )$ QUICKSORT(A, p, q–1) //recursively sort the low side QUICKSORT(A, q+1, r) //recursively sort the high side   
Initial call: QUICKSORT(A, 1, n)

# Partition

Divide data into two groups, such that:

All items with a value higher than a specified amount (the   
pivot) are in one group   
All items with a lower value are in another

### Images:
- data\Design and Analysis of Algorithms\L03-Sorting\page_058\L03-Sorting_page_058\auto\images\8886d0de89e0613f5044f06dac85819de151aad8590bf380cc5a8c24530eb415.jpg
- data\Design and Analysis of Algorithms\L03-Sorting\page_058\L03-Sorting_page_058\auto\images\f66aa174cd3949aaf841a8c84748c4dacfe9c3cabab94febac2129aa80cb1570.jpg

---

## Lecture: L03-Sorting\page_059\L03-Sorting_page_059\auto

• Say I have 12 values: – 175 192 95 45 115 105 20 60 185 5 90 180 • I pick a pivot=104, and partition (NOT sorting yet): – 95 45 20 60 5 90 | 175 192 115 105 185 180 – Note: In the future the pivot will be an actual element – Also: Partitioning need not maintain order of elements an won’t, although I did in this example

• The partition is the leftmost item in the right array:

– 95 45 20 60 5 90 | 175 192 115 105 185 180 • Which we return to designate where the division is located

---

## Lecture: L03-Sorting\page_060\L03-Sorting_page_060\auto

# Partitioning

• The partition process (two indexs)

– Start with two pointers: leftIndex initialized to one position to the left of the first cell; rightIndex to one position to the right of the last cell   
– leftIndex moves to the right; rightIndex moves to the left

• Stopping and Swapping

– When leftIndex encounters an item smaller than the pivot, it keeps going; when it finds a larger item, it stops

– When rightIndex encounters an item larger than the pivot, it keeps going; when it finds a smaller item, it stops

– When the two indexs eventually meet, the process is complete

– When the two indexs stop, swap the two elements

---

## Lecture: L03-Sorting\page_061\L03-Sorting_page_061\auto

# Efficiency: Partitioning

• O(n) time

– left starts at 1 and moves one-by-one to the right – right starts at n and moves one-by-one to the left – When left and right cross, we stop.

• So we’ll hit each element just once • Number of comparisons is n+1 • Number of swaps is worst case n/2 – Worst case, we swap every single time – Each swap involves two elements – Usually, it will be less than this

• Since in the random case, some elements will be on the correct side of the pivot

---

## Lecture: L03-Sorting\page_062\L03-Sorting_page_062\auto

# Modified Partitioning

• In preparation for Quicksort:

– Choose our pivot value to be the rightmost element – Partition the array around the pivot – Ensure the pivot is at the location of the partition • Meaning, the pivot should be the leftmost element of the right subarray • Example: Unpartitioned 42 89 63 12 94 27 78 3 50 36 • Partitioned around Pivot: 3 27 12 36 63 94 89 78 42 50 • What does this imply about the pivot element after the partition?

---

## Lecture: L03-Sorting\page_063\L03-Sorting_page_063\auto

# Placing the PIVOT

• Goal: Pivot must be in the leftmost position in the right subarray – 3 27 12 36 63 94 89 78 42 50

• Our algorithm does not do this currently • It currently will not touch the pivot – left increments till it finds an element $>$ pivot – right decrements till it finds an element $<$ pivot – So the pivot itself won’t be touched, and will stay on the right: – 3 27 12 63 94 89 78 42 50 36

---

## Lecture: L03-Sorting\page_064\L03-Sorting_page_064\auto

# Shifting the PIVOT

• We have this: – 3 27 12 63 94 89 78 42 50 36

• Our goal is the position of 36

• Shift every element in the right subarray up (inefficient)

– 3 27 12 36 63 94 89 78 42 50

![](images/0d186ac7e64ffe5912011dcefe2ad2804601853d79ab31ef7261a3dd73875e16.jpg)

Recursive calls sort subarrays.

### Images:
- data\Design and Analysis of Algorithms\L03-Sorting\page_064\L03-Sorting_page_064\auto\images\0d186ac7e64ffe5912011dcefe2ad2804601853d79ab31ef7261a3dd73875e16.jpg

---

## Lecture: L03-Sorting\page_065\L03-Sorting_page_065\auto

# Swapping the PIVOT

![](images/ef8bd4b2d7fdee3b9a55b92b1a805278d98c6e6da2b191947df70e14d3728546.jpg)

![](images/e9a70b1d79b62465744164812a73a3af8da56274f4296fc9a1ad0de1632cba67.jpg)

Swapping the pivot.

• Just swap the leftmost with the pivot! Better

– 3 27 12 36 94 89 78 42 50 63

– We can do this because the right subarray is not in any particular order

• Just takes one more line to our Python method

– Basically, a single call to swap() – Swaps A[end-1] (the pivot) with A[left] (the partition index)

### Images:
- data\Design and Analysis of Algorithms\L03-Sorting\page_065\L03-Sorting_page_065\auto\images\e9a70b1d79b62465744164812a73a3af8da56274f4296fc9a1ad0de1632cba67.jpg
- data\Design and Analysis of Algorithms\L03-Sorting\page_065\L03-Sorting_page_065\auto\images\ef8bd4b2d7fdee3b9a55b92b1a805278d98c6e6da2b191947df70e14d3728546.jpg

---

## Lecture: L03-Sorting\page_066\L03-Sorting_page_066\auto

Algorithm Partition(A, left, right):

Input: Array A, starting index left, ending index right

Output: Index of the pivot after rearrangement

pivot A[left] // Choose first element as pivot   
leftIndex left + 1   
rightIndex right

// Move leftIndex to the right until finding an element $> =$ pivot while leftIndex ≤ right and A[leftIndex] < pivot do:

// Move rightIndex to the left until finding an element $< =$ pivot while rightIndex ≥ left and A[rightIndex] > pivot do:

rightIndex rightIndex - 1 if leftIndex ≥ rightIndex then:

break // Indices have crossed, partitioning is complete swap A[leftIndex] and A[rightIndex] // Swap elements swap A[left] and A[rightIndex] // Move pivot to correct position return rightIndex // Return final position of pivot

---

## Lecture: L03-Sorting\page_067\L03-Sorting_page_067\auto

# Shall We Try It On An ARRAY?

![](images/cbe2259eec3ca1a48dcfa4455b4ec874af082391f2e906bf1d50a92413ad55cd.jpg)

1, 7, 5, 3, 6, 9, 0, 4, 8, 2

![](images/22c02922b54965db667211dd4d4a2b7d749baeac42fcd36ea047e1e7a0078e7b.jpg)

Let’s go step-by-step via Quick Sort

### Images:
- data\Design and Analysis of Algorithms\L03-Sorting\page_067\L03-Sorting_page_067\auto\images\22c02922b54965db667211dd4d4a2b7d749baeac42fcd36ea047e1e7a0078e7b.jpg
- data\Design and Analysis of Algorithms\L03-Sorting\page_067\L03-Sorting_page_067\auto\images\cbe2259eec3ca1a48dcfa4455b4ec874af082391f2e906bf1d50a92413ad55cd.jpg

---

## Lecture: L03-Sorting\page_068\L03-Sorting_page_068\auto

# BEST Case…

• We partition the array each time into two equal subarrays   
• Say we start with array of size $n = 2 ^ { i }$   
• We recurse until the base case, 1 element

• Draw the tree

– First call $- >$ Partition n elements, n operations   
– Second calls $- >$ Each partition n/2 elements, $2 ( n / 2 ) = n$ operations   
– Third calls $- >$ Each partition $\mathsf { n } / 4 , 4 ( \mathsf { n } / 4 ) = \mathsf { n }$ operations …   
– (i+1)th calls $- >$ Each partition $\mathsf { n } / 2 ^ { i } = 1 , 2 ^ { i } ( 1 ) = \mathsf { n } ( 1 ) = \mathsf { n }$ ops

• Total: $( \mathsf { i } { + } 1 ) ^ { \ast } \mathsf { n } = ( \mathsf { l o g } \mathsf { n } + 1 ) ^ { \ast } \mathsf { n } \to \mathsf { O } ( \mathsf { n } \mathsf { l o g } \mathsf { n } )$

---

## Lecture: L03-Sorting\page_069\L03-Sorting_page_069\auto

# The Very BAD Case….

• If the array is sorted

• Let’s see the problem: – 0 10 20 30 40 50 60 70 80 90

• What happens after the partition? This: – 0 10 20 30 40 50 60 70 80 90

• This is sorted, but the algorithm doesn’t know it.

• It will then call itself on an array of zero size (the left subarray) and an array of n-1 size (the right subarray).

• Producing: – 0 10 20 30 40 50 60 70 80 90

---

## Lecture: L03-Sorting\page_070\L03-Sorting_page_070\auto

# The Very BAD Case….

• In the worst case, we partition every time into an array of n-1 elements and an array of 0 elements

• This yields ${ \mathsf { O } } ( n ^ { 2 } )$ time:

– First call: Partition n elements, n operations – Second calls: Partition n-1 and 0 elements, n-1 operations – Third calls: Partition n-2 and 0 elements, n-2 operations – Draw the tree

• Yielding: Operati $\mathsf { o n s } = \mathsf { n } + \mathsf { n } - 1 + \mathsf { n } - 2 + \ldots + 1 = \mathsf { n } ( \mathsf { n } + 1 ) / 2 \to \mathsf { O } ( \mathsf { n }$ n2)

### Images:
- data\Design and Analysis of Algorithms\L03-Sorting\page_070\L03-Sorting_page_070\auto\images\8c66fa33d63af437a0b283e1d78b93d2786513bbaee304d5520ec67cb08b2ec6.jpg

---

## Lecture: L03-Sorting\page_071\L03-Sorting_page_071\auto

# Choosing Pivot

• What caused the problem was “blindly” choosing the pivot from the right end.

• In the case of a reverse sorted array, this is not a good choice at all

• Can we improve our choice of the pivot? Let’s choose the middle of three values

---

## Lecture: L03-Sorting\page_072\L03-Sorting_page_072\auto

# Median-Of-Three Partitioning

• Every time you partition, choose the median value of the left, center and right element as the pivot

• Example: – 44 11 55 33 77 22 00 99 101 66 88

• Pivot: Take the median of the leftmost, middle and rightmost – 44 11 55 33 77 22 00 99 101 66 88 - Median: 44

• Then partition around this pivot: – 11 00 33 22 44 77 55 99 101 66 88

• Increases the likelihood of an equal partition – Also, it cannot possibly be the worst case

---

## Lecture: L03-Sorting\page_073\L03-Sorting_page_073\auto

# How This Fixes The WORST Case?

• Here’s our array:

– 0 10 20 30 40 50 60 70 80 90

• Let’s see on the board how this fixes things

• In fact in a perfectly sorted array, we choose the middle element as the pivot!

– Which is optimal – We get ????(????log????)

• Vast majority of the time, if you use QuickSort with a Median-OfThree partition, you get ${ \cal O } ( N | \mathrm { o g } N )$ behavior

---

## Lecture: L03-Sorting\page_074\L03-Sorting_page_074\auto

# One Final Optimization…

• After a certain point, just doing insertion sort is faster than partitioning small arrays and making recursive calls

• Once you get to a very small subarray, you can just sort with insertion sort

• You can experiment a bit with ‘cutoff’ values – Knuth: ${ \mathsf n } { = } 9$

---

## Lecture: L03-Sorting\page_075\L03-Sorting_page_075\auto

# Operation Count Estimates

• For QuickSort • $\mathsf { n } { = } 8$ : 30 comparisons, 12 swaps • n=12: 50 comparisons, 21 swaps • n=16: 72 comparisons, 32 swaps • n=64: 396 comparisons, 192 swaps • n=100: 678 comparisons, 332 swaps • n=128: 910 comparisons, 448 swaps • The only competitive algorithm is MergeSort – But, takes much more memory like we said

---

## Lecture: L03-Sorting\page_076\L03-Sorting_page_076\auto

# Summary of Quicksort

![](images/15b24e7f5dbeacf93a14753db5dcea7692cfb73774ab2431abf9704146a5416a.jpg)

• Quick sort operates in ${ \cal O } ( N { * } | \mathrm { o g } N )$ time (except when the simpler version is applied to already-sorted data).

• Subarrays smaller than a certain size (the cutoff) can be sorted by a method other than quicksort.

• The insertion sort is commonly used to sort subarrays smaller than the cutoff.

• The insertion sort can also be applied to the entire array, after it has been sorted down to a cutoff point by quicksort.

Swaps and Comparisons in Quicksort   

<table><tr><td>N</td><td>8</td><td>12</td><td>16</td><td>64</td><td>100</td><td>128</td></tr><tr><td>loggN</td><td>3</td><td>3.59</td><td>4</td><td>6</td><td>6.65</td><td>7</td></tr><tr><td>N&#x27;log,N</td><td>24</td><td>43</td><td>64</td><td>384</td><td>665</td><td>896</td></tr><tr><td>Comparisons: (N+2)logN</td><td>30</td><td>50</td><td>72</td><td>396</td><td>678</td><td>910</td></tr><tr><td>Swaps: fewer than N/2*log,N</td><td>12</td><td>21</td><td>32</td><td>192</td><td>332</td><td>448</td></tr></table>

\*The $\ln \frac { \pi } { \rho } =$ N quantity used in the table is true only in the best-case scenario, where each subarray is partitioned exactly in half. For random data, it is slightly greater.

### Images:
- data\Design and Analysis of Algorithms\L03-Sorting\page_076\L03-Sorting_page_076\auto\images\15b24e7f5dbeacf93a14753db5dcea7692cfb73774ab2431abf9704146a5416a.jpg
- data\Design and Analysis of Algorithms\L03-Sorting\page_076\L03-Sorting_page_076\auto\images\d2b2431119b0fd8025eb45b8b3dfecb98bcbdc01e97344caede2ee8c271c484d.jpg
- data\Design and Analysis of Algorithms\L03-Sorting\page_076\L03-Sorting_page_076\auto\images\e503523ac78bd1a1b478ee064398cc15c9088a93afa38c836b01267cd06e5f19.jpg

---

## Lecture: L03-Sorting\page_077\L03-Sorting_page_077\auto

# Sort algorithm performance

![](images/d87e9f9efe96ff2b68d6e48c0e7c5114d9f97ca9fba2869c76420dfb97ddf39b.jpg)  
Sorting Algorithm Performance on 1000 Elements Over 10 Runs (Mean ± Std:

### Images:
- data\Design and Analysis of Algorithms\L03-Sorting\page_077\L03-Sorting_page_077\auto\images\d87e9f9efe96ff2b68d6e48c0e7c5114d9f97ca9fba2869c76420dfb97ddf39b.jpg

---

## Lecture: L03-Sorting-extra\page_001\L03-Sorting-extra_page_001\auto

• There are ????! different ways to permute the ???? elements in the input array ????.

• Example: For $n = 3$ , 6 permutations:

$$
\begin{array} { r l } & { A [ 1 ] , A [ 2 ] , A [ 3 ] } \\ & { A [ 1 ] , A [ 3 ] , A [ 2 ] } \\ & { A [ 2 ] , A [ 1 ] , A [ 3 ] } \\ & { A [ 2 ] , A [ 3 ] , A [ 1 ] } \\ & { A [ 3 ] , A [ 1 ] , A [ 2 ] } \\ & { A [ 3 ] , A [ 2 ] , A [ 1 ] } \end{array}
$$

• The goal of sorting is essentially to decide which of ????! Permutations is the final sorted order.

### Images:
- data\Design and Analysis of Algorithms\L03-Sorting-extra\page_001\L03-Sorting-extra_page_001\auto\images\e325c61c94f502797b8e4d238e8bc355e4d736e3571e0ed9154db13cd0c6dd94.jpg

---

## Lecture: L03-Sorting-extra\page_002\L03-Sorting-extra_page_002\auto

# Sorting Lower Bound: Comparison-Based Algorithm

Formally, such an algorithm works by continuously shrinking a pool $P$ of possible permutations.

• At the beginning, $P$ contains all the ????! permutations.   
• Every comparison allows the algorithm to discard all those permutations in $P$ that are inconsistent with the comparison’s result.   
• Eventually, $P$ has only 1 permutation left, which is thus the final sorted order.

In other words, at any moment, all the permutations that remain in $P$ are possible results. The algorithm cannot terminate as long as $| P | \ge 2$ .

---

## Lecture: L03-Sorting-extra\page_003\L03-Sorting-extra_page_003\auto

• Shrinking the Pool: An Example

![](images/c92b57cc5edd396bad22d83d8581ba5669f7d80dcc0ba866744b0496ab5e15a3.jpg)

• In general, each comparison allows us to shrink $P$ to either $P _ { 1 }$ or $P _ { 2 }$ .

### Images:
- data\Design and Analysis of Algorithms\L03-Sorting-extra\page_003\L03-Sorting-extra_page_003\auto\images\c92b57cc5edd396bad22d83d8581ba5669f7d80dcc0ba866744b0496ab5e15a3.jpg

---

## Lecture: L03-Sorting-extra\page_004\L03-Sorting-extra_page_004\auto

# Sorting Lower Bound: The Framework of Comparison-Based Algorithm

# Framework

1. $P $ all the $\pmb { \eta } \smash { ! }$ ! permutations of A   
2. while $| P | > 1$   
3. make a comparison between elements $e _ { 1 }$ and $e _ { 2 }$   
4. if $e _ { 1 } < e _ { 2 }$ then   
5. $P  P _ { 1 }$ , where $P _ { 1 }$ is the set of permutations in $P$ consistent with $e _ { 1 } < e _ { 2 }$   
6. else   
7. $P  P _ { 2 }$ ,where $P _ { 2 }$ is the set of permutations in $P$ consistent with $e _ { 1 } > e _ { 2 }$

8. return the permutation in $P$

---

## Lecture: L03-Sorting-extra\page_005\L03-Sorting-extra_page_005\auto

# Sorting Lower Bound: A Worst-Case Lower Bound

Formally, such an algorithm works by continuously shrinking a pool $\cdot$ of possible permutations.

• Note that one of $P _ { 1 }$ and $P _ { 2 }$ contains at least half of the permutations in $P$ (i.e., either $| P _ { 1 } | \ge | P | / 2$ or $| P _ { 2 } | \ge | P | / 2 \ \}$ .

• The worst case happens when $P$ always shrinks to the larger set between $P _ { 1 }$ and $P _ { 2 }$ .

• In this case, the size of $P$ shrinks by at most half after each comparison.

Hence, the number of comparisons required before $| P |$ decreases to 1 is $\log _ { 2 } ( n ! )$ .

The next slide shows $\log _ { 2 } ( n ! ) = \Omega ( n \log n )$ .

---

## Lecture: L03-Sorting-extra\page_006\L03-Sorting-extra_page_006\auto

$$
\begin{array} { l } { \displaystyle \log _ { 2 } ( n ! ) = \sum _ { i = 1 } ^ { n } \log _ { 2 } i } \\ { \displaystyle \ge \sum _ { i = n / 2 } ^ { n } \log _ { 2 } i } \\ { \displaystyle \ge ( n / 2 ) \log _ { 2 } ( n / 2 ) } \\ { \displaystyle = \Omega ( n \log n ) } \end{array}
$$

We now conclude that any comparison-based algorithm must incur $\Omega ( n \log n )$ time sorting ???? elements in the worst case.

### Images:
- data\Design and Analysis of Algorithms\L03-Sorting-extra\page_006\L03-Sorting-extra_page_006\auto\images\d67f3d3bcee1655134b5cbb1ffb2bc113069f2067653090638fb0e83dbf2a68b.jpg

---

## Lecture: L04-D&C\page_001\L04-D&C_page_001\auto

# Divide-and-Conquer

Merge-sort (Recap.)   
Master Theorem   
More Divide-and-Conquer algorithms

---

## Lecture: L04-D&C\page_002\L04-D&C_page_002\auto

# Analyzing Merge Sort (Recap.)

MERGE-SORT $A [ 1 \ldots n ]$

1. If $n = 1$ , done

![](images/8928427febc9a7b6bcf364130e70a0b28b5b4c959aaf4e82f093c05e75461905.jpg)

2. Recursively sort A[ 1 . . n/2 ] and A[ n/2+1 . . n ]

3. “Merge” the $2$ sorted lists

Sloppiness: Should be $T ( \lceil n / 2 \rceil ) + T ( \lfloor n / 2 \rfloor ) .$ but it turns out not to matter asymptotically.

### Images:
- data\Design and Analysis of Algorithms\L04-D&C\page_002\L04-D&C_page_002\auto\images\8928427febc9a7b6bcf364130e70a0b28b5b4c959aaf4e82f093c05e75461905.jpg

---

## Lecture: L04-D&C\page_003\L04-D&C_page_003\auto

# Recurrence for Merge Sort

$$
T ( n ) = { \left\{ \begin{array} { l l } { \Theta ( 1 ) { \mathrm { i f } } n = 1 ; } \\ { 2 T ( n / 2 ) + \Theta ( n ) { \mathrm { i f } } n > 1 . } \end{array} \right. }
$$

• We shall usually omit stating the base case when $T ( n ) =$

Θ(1) for sufficiently small n, but only when it has no effect on the asymptotic solution to the recurrence.

CLRS provides several ways to find a good upper bound on T(n).

### Images:
- data\Design and Analysis of Algorithms\L04-D&C\page_003\L04-D&C_page_003\auto\images\06e69daead59c726f1570bdb865862a8385981a27f39f02a61b2239711cfc1d1.jpg

---

## Lecture: L04-D&C\page_004\L04-D&C_page_004\auto

# Recursion Tree

Solve $T ( n ) = 2 T ( n / 2 ) + c n$ , where $c > 0$ is constant.

![](images/c1ab3c9f77231ac43b37f23098d75ed1057ca54fe59305b55a9dc25eef4ee5d7.jpg)

### Images:
- data\Design and Analysis of Algorithms\L04-D&C\page_004\L04-D&C_page_004\auto\images\c1ab3c9f77231ac43b37f23098d75ed1057ca54fe59305b55a9dc25eef4ee5d7.jpg

---

## Lecture: L04-D&C\page_005\L04-D&C_page_005\auto

# The Divide-and-Conquer Design Paradigm

1. Divide the problem (instance) into subproblems.

2. Conquer the subproblems by solving them recursively.

3. Combine subproblem solutions.

---

## Lecture: L04-D&C\page_006\L04-D&C_page_006\auto

# Merge Sort

1. Divide: Trivial.

2. Conquer: Recursively sort 2 subarrays.

3. Combine: Linear-time merge.

---

## Lecture: L04-D&C\page_007\L04-D&C_page_007\auto

# Merge Sort

1. Divide: Trivial.

2. Conquer: Recursively sort 2 subarrays.

3. Combine: Linear-time merge.

![](images/4b1c45f04242742c14c58b9a05342aaf90a15db564db42fc1bc3a0e3dbbd205d.jpg)

### Images:
- data\Design and Analysis of Algorithms\L04-D&C\page_007\L04-D&C_page_007\auto\images\4b1c45f04242742c14c58b9a05342aaf90a15db564db42fc1bc3a0e3dbbd205d.jpg

---

## Lecture: L04-D&C\page_008\L04-D&C_page_008\auto

# Master Theorem (Reprise)

$$
T ( n ) = a T ( n / b ) + f ( n )
$$

CASE 1: $f ( n ) = O ( n ^ { \log b a - \varepsilon } )$ , constant $\varepsilon > 0$ ⇒ $T ( n ) = \Theta ( n ^ { \mathrm { l o g } _ { b } a } )$

$\mathbb { C } _ { \mathrm { A S E } } \mathbb { Z } : f ( n ) = \Theta ( n ^ { \log b a } \log ^ { l } n )$ , constant $l \geq 0$ $\Rightarrow T ( n ) = \Theta ( n ^ { \mathrm { l o g } b a } \log ^ { l + 1 } n )$

CAS $\varepsilon 3 \colon f ( n ) = \Omega ( n ^ { \mathrm { l o g } b a + \varepsilon } ) .$ , constant $\varepsilon > 0$ , and regularity condition $a f ( n / b ) \leq c f ( n )$ , constant $c < 1$ for all sufficiently large n ⇒ $T ( n ) = \Theta ( f ( n ) )$

### Images:
- data\Design and Analysis of Algorithms\L04-D&C\page_008\L04-D&C_page_008\auto\images\0a50629056156979d97fa01940808b32838a37b5a102ecaed0864d413513f62f.jpg

---

## Lecture: L04-D&C\page_009\L04-D&C_page_009\auto

# Master Theorem (Reprise)

$$
T ( n ) = a T ( n / b ) + f ( n )
$$

(cd $\mathbb { C } _ { \mathrm { { A S E } } } 1 { : } f ( n ) = O ( n ^ { \log b a - \varepsilon } )$ , constant $\varepsilon > 0$ ⇒ $T ( n ) = \Theta ( n ^ { \mathrm { l o g } _ { b } a } )$

CASE $\therefore f ( n ) = \Theta ( n ^ { \mathrm { l o g } b a } \log ^ { l } n )$ , constant $l \geq 0$ ⇒ $> T ( n ) = \Theta ( n ^ { \mathrm { l o g } b a } \log ^ { l + 1 } n )$

$\mathbb { C } _ { \mathrm { A S E } } \mathcal { B } : f ( n ) = \Omega ( n ^ { \mathrm { l o g } _ { b } a + \varepsilon } )$ , constant $\varepsilon > 0$ , and regularity condition $a f ( n / b ) \leq c f ( n )$ , constant $c < 1$ for all sufficiently large  n $\Rightarrow T ( n ) = \Theta ( f ( n ) )$

Merge sort: $a = 2 , b = 2 \Rightarrow n ^ { \mathrm { l o g } b a } = n ^ { \mathrm { l o g } 2 2 } = n$ ⇒ CASE ${ \mathrm { ~  ~ \psi ~ } } _ { \mathrm { ~ \tiny ~ 2 ~ } } ( l = 0 ) \ \Rightarrow \ T ( n ) = \Theta ( n \log n )$

### Images:
- data\Design and Analysis of Algorithms\L04-D&C\page_009\L04-D&C_page_009\auto\images\536756d634c12622af5ca059e4306c7e79f07ad233858f134d9f7d47a692da3d.jpg
- data\Design and Analysis of Algorithms\L04-D&C\page_009\L04-D&C_page_009\auto\images\b53dcb9a0def0e8569cf466ca0bca3af8e3c76f2a3926e0d94745bba80177188.jpg
- data\Design and Analysis of Algorithms\L04-D&C\page_009\L04-D&C_page_009\auto\images\e90cdf613d54ce183a52802b1e008f6124cc462616808eaeae20ada09c719b90.jpg

---

## Lecture: L04-D&C\page_010\L04-D&C_page_010\auto

# Master Theorem (Proof)

$$
T ( n ) = a T ( n / b ) + f ( n )
$$

$\begin{array} { r } { T ( n ) = \Theta \big ( n ^ { \log _ { b } a } \big ) + \sum _ { i = 0 } ^ { k - 1 } a ^ { i } f ( \frac { n } { b ^ { i } } ) , \qquad \cdot \operatorname { \nabla } g ( \boldsymbol { n } _ { \mathrm { a } } ) } \end{array}$ $n = b ^ { k } , k = \log _ { b } n , a ^ { k } = a ^ { \log _ { b } n } = n ^ { \log _ { b } a }$

Try to solve case 2 in lab!

t) = k− if ( )

For case1： $f ( n ) = { \bf 0 } ( n ^ { ( \log _ { b } a ) - \varepsilon } ) , \ \varepsilon > 0$

We have:

$$
\begin{array} { r l } & { g ( n ) = \mathbf { 0 } ( \sum _ { i = 0 } ^ { k - 1 } a ^ { i } \left( \frac { n } { b ^ { i } } \right) ^ { ( \log b ~ a ) - \varepsilon } ) } \\ & { \qquad = \mathbf { 0 } ( n ^ { ( \log b ~ a ) - \varepsilon } \sum _ { i = 0 } ^ { k - 1 } \left( \frac { a b ^ { \varepsilon } } { b ^ { | | \mathbf { g } _ { \mathcal { Y } _ { i } } } a | } \right) ^ { i } ) } \\ & { \qquad = \mathbf { 0 } ( n ^ { ( \log b ~ a ) - \varepsilon } \sum _ { i = 0 } ^ { k - 1 } ( b ^ { \varepsilon } ) ^ { i } ) } \\ & { \qquad = \mathbf { 0 } ( n ^ { ( \log b ~ a ) - \varepsilon } \sum _ { i = 0 } ^ { k - 1 } ( b ^ { \varepsilon } ) ^ { i } ) } \\ & { \qquad = \mathbf { 0 } ( n ^ { ( \log b ~ a ) - \varepsilon } \frac { n ^ { \varepsilon } - 1 } { b ^ { \varepsilon } - 1 } ) } \\ & { \qquad = \mathbf { 0 } ( n ^ { ( \log b ~ a ) - \varepsilon } \frac { n ^ { \varepsilon } - 1 } { b ^ { \varepsilon } - 1 } ) } \\ & { \qquad = \mathbf { 0 } \big ( n ^ { \log b ~ a } \big ) } \end{array}
$$

For case3： $f ( n ) = \Omega ( n ^ { ( \log _ { b } a ) + \varepsilon } ) , \ \varepsilon > 0$

$$
\begin{array} { r } { \mathbf { \Delta } a f ( \frac { n } { b } ) \leq c f ( n ) , c < 1 } \end{array}
$$

We have: $\begin{array} { c } { { { \pmb a } { \pmb f } \left( \frac { n } { b ^ { 2 } } \right) \leq c { \pmb f } \left( \frac { n } { b } \right) } } \\ { { \vdots } } \end{array}$

$$
\begin{array} { r } { \pmb { a } \pmb { f } \left( \frac { \pmb { n } } { b ^ { i } } \right) \le c \pmb { f } \left( \frac { \pmb { n } } { b ^ { i - 1 } } \right) } \end{array}
$$

Multiply both sides: $\begin{array} { r } { a ^ { i } f ( \frac { n } { b ^ { i } } ) \leq c ^ { i } f ( n ) } \end{array}$

$$
\begin{array} { c } { g ( { \pmb n } ) = \sum _ { i = 0 } ^ { k - 1 } a ^ { i } f ( \frac n { b ^ { i } } ) \leq \sum _ { i = 0 } ^ { k - 1 } c ^ { i } f ( { \pmb n } ) = f ( { \pmb n } ) \sum _ { i = 0 } ^ { k - 1 } c ^ { i } } \\ { \leq f ( { \pmb n } ) \frac 1 { 1 - c } = \Theta ( f ( { \pmb n } ) ) } \end{array}
$$

### Images:
- data\Design and Analysis of Algorithms\L04-D&C\page_010\L04-D&C_page_010\auto\images\40fdf1888131c7ae443753caaff5b9ead9699f156036feae49e40cf8cd6351a1.jpg
- data\Design and Analysis of Algorithms\L04-D&C\page_010\L04-D&C_page_010\auto\images\57bd641d8ad4fa9606b587f6ba2ea33b2e47d15438c39ae4245d09008873a77c.jpg
- data\Design and Analysis of Algorithms\L04-D&C\page_010\L04-D&C_page_010\auto\images\7bc2d101b718c798a10447ac1a652865de5774240c1fde517b727aaaeebcc88c.jpg
- data\Design and Analysis of Algorithms\L04-D&C\page_010\L04-D&C_page_010\auto\images\965036f9122288d81082332238c2d2dfa5d86dbde15c25a3c655aac44678902c.jpg
- data\Design and Analysis of Algorithms\L04-D&C\page_010\L04-D&C_page_010\auto\images\a88858fcd6a3fbe7151f3e9b81b452ccabe6cbfdfca3322fb198c231ade932f5.jpg
- data\Design and Analysis of Algorithms\L04-D&C\page_010\L04-D&C_page_010\auto\images\b987c2bfd3c2c70250177f1fc8199a34fe9c4896a67cadfa9ec38d09fa09ac11.jpg
- data\Design and Analysis of Algorithms\L04-D&C\page_010\L04-D&C_page_010\auto\images\f1428080381a5ec7d48b9274ff09ddca8484aa0e7e024cd7242657d1b80027a7.jpg
- data\Design and Analysis of Algorithms\L04-D&C\page_010\L04-D&C_page_010\auto\images\f51483d8bf3caf3af4848449d55e163caf1e05695b53ff031dd7f315c8432aa4.jpg
- data\Design and Analysis of Algorithms\L04-D&C\page_010\L04-D&C_page_010\auto\images\f69a4f49692310ee508643b2c2f2414a6a6c02b56f85b168f1275d8f89be6d84.jpg

---

## Lecture: L04-D&C\page_011\L04-D&C_page_011\auto

Find an element in a sorted array:

1. Divide: Check middle element.

2. Conquer: Recursively search 1 subarray.

3. Combine: Trivial.

---

## Lecture: L04-D&C\page_012\L04-D&C_page_012\auto

Find an element in a sorted array:

1. Divide: Check middle element.

2. Conquer: Recursively search 1 subarray.

3. Combine: Trivial.

Example: Find 9

3 5 7 8 9 12 15

---

## Lecture: L04-D&C\page_013\L04-D&C_page_013\auto

Find an element in a sorted array:

1. Divide: Check middle element.

2. Conquer: Recursively search 1 subarray.

3. Combine: Trivial.

Example: Find 9

![](images/de4eeee9b44cdabb7eb57d9a2abe23df108b5c0334365f359bc94d4c7ed70128.jpg)

### Images:
- data\Design and Analysis of Algorithms\L04-D&C\page_013\L04-D&C_page_013\auto\images\de4eeee9b44cdabb7eb57d9a2abe23df108b5c0334365f359bc94d4c7ed70128.jpg

---

## Lecture: L04-D&C\page_014\L04-D&C_page_014\auto

Find an element in a sorted array:

1. Divide: Check middle element.

2. Conquer: Recursively search 1 subarray.

3. Combine: Trivial.

Example: Find 9

![](images/42b3ac3784133405484ad3983256abfe39c861b4b0ca3919a3dc9f0d3c869449.jpg)

### Images:
- data\Design and Analysis of Algorithms\L04-D&C\page_014\L04-D&C_page_014\auto\images\42b3ac3784133405484ad3983256abfe39c861b4b0ca3919a3dc9f0d3c869449.jpg

---

## Lecture: L04-D&C\page_015\L04-D&C_page_015\auto

Find an element in a sorted array:

1. Divide: Check middle element.

2. Conquer: Recursively search 1 subarray.

3. Combine: Trivial.

Example: Find 9

![](images/09a5797f43b529ffe822be908d826b919f904a0fefe62562b08555ec6a5ca9b0.jpg)

### Images:
- data\Design and Analysis of Algorithms\L04-D&C\page_015\L04-D&C_page_015\auto\images\09a5797f43b529ffe822be908d826b919f904a0fefe62562b08555ec6a5ca9b0.jpg

---

## Lecture: L04-D&C\page_016\L04-D&C_page_016\auto

Find an element in a sorted array:

1. Divide: Check middle element.

2. Conquer: Recursively search 1 subarray.

3. Combine: Trivial.

Example: Find 9

![](images/a3b88f22fb4439525e94fa581d87e76bde26cd12fdeb614ae17f0ccae17e04c8.jpg)

### Images:
- data\Design and Analysis of Algorithms\L04-D&C\page_016\L04-D&C_page_016\auto\images\a3b88f22fb4439525e94fa581d87e76bde26cd12fdeb614ae17f0ccae17e04c8.jpg

---

## Lecture: L04-D&C\page_017\L04-D&C_page_017\auto

Find an element in a sorted array:

1. Divide: Check middle element.

2. Conquer: Recursively search 1 subarray.

3. Combine: Trivial.

Example: Find 9

![](images/a68c5f05c1d2146814fa640eefe97cb7440f4803bd16e6f912e4b93594445743.jpg)

### Images:
- data\Design and Analysis of Algorithms\L04-D&C\page_017\L04-D&C_page_017\auto\images\a68c5f05c1d2146814fa640eefe97cb7440f4803bd16e6f912e4b93594445743.jpg

---

## Lecture: L04-D&C\page_018\L04-D&C_page_018\auto

# Recurrence for Binary Search

![](images/b19abaf62ceb2aacafb4ffb80de6a7641495b2815b38e77b108c14ce2fc0e8bc.jpg)

### Images:
- data\Design and Analysis of Algorithms\L04-D&C\page_018\L04-D&C_page_018\auto\images\b19abaf62ceb2aacafb4ffb80de6a7641495b2815b38e77b108c14ce2fc0e8bc.jpg

---

## Lecture: L04-D&C\page_019\L04-D&C_page_019\auto

# Recurrence for Binary Search

![](images/67c4c336d2ae29b7be9a6e2538d48e3ef8ddabdfb97f849e7f7508a50f3d30a0.jpg)

$n ^ { \log b a } = n ^ { \log 2 1 } = n ^ { 0 } = 1 \Rightarrow { \mathrm { ~ C ~ } }$ ASE 2 (l = 0) $\Rightarrow T ( n ) = \Theta ( \lg n ) .$ .

### Images:
- data\Design and Analysis of Algorithms\L04-D&C\page_019\L04-D&C_page_019\auto\images\164f947d6d5b29ecbe044fb339489f8869b0ebfb71049e9cceb8475842ab2fae.jpg
- data\Design and Analysis of Algorithms\L04-D&C\page_019\L04-D&C_page_019\auto\images\67c4c336d2ae29b7be9a6e2538d48e3ef8ddabdfb97f849e7f7508a50f3d30a0.jpg
- data\Design and Analysis of Algorithms\L04-D&C\page_019\L04-D&C_page_019\auto\images\f0cd7d13faf94694edeeb34a72ad3da563068059264f1b220260484a4b10f941.jpg

---

## Lecture: L04-D&C\page_020\L04-D&C_page_020\auto

Problem: Compute $a ^ { n }$ , where n ∈N.

Naive algorithm: $\Theta ( n )$ .

---

## Lecture: L04-D&C\page_021\L04-D&C_page_021\auto

Problem: Compute $a ^ { n }$ , where n ∈N.

Naive algorithm: $\Theta ( n )$ .

Divide-and-conquer algorithm:

$$
a ^ { n } = { \left\{ \begin{array} { l l } { a ^ { n / 2 } \cdot a ^ { n / 2 } } & { { \mathrm { ~ i f ~ } } n { \mathrm { ~ i s ~ e v e n ; } } } \\ { a ^ { ( n - 1 ) / 2 } \cdot a ^ { ( n - 1 ) / 2 } \cdot a } & { { \mathrm { ~ i f ~ } } n { \mathrm { ~ i s ~ o d d . } } } \end{array} \right. }
$$

### Images:
- data\Design and Analysis of Algorithms\L04-D&C\page_021\L04-D&C_page_021\auto\images\0e11de634b73daf0d586babe2a208ae2098e62dd8eb8ece540af3f7a4ebe534e.jpg

---

## Lecture: L04-D&C\page_022\L04-D&C_page_022\auto

Problem: Compute $a ^ { n }$ , where n ∈N.

Naive algorithm: $\Theta ( n )$ .

Divide-and-conquer algorithm:

$$
a ^ { n } = { \left\{ \begin{array} { l l } { a ^ { n / 2 } \cdot a ^ { n / 2 } } & { { \mathrm { ~ i f ~ } } n { \mathrm { ~ i s ~ e v e n ; } } } \\ { a ^ { ( n - 1 ) / 2 } \cdot a ^ { ( n - 1 ) / 2 } \cdot a } & { { \mathrm { ~ i f ~ } } n { \mathrm { ~ i s ~ o d d . } } } \end{array} \right. }
$$

$$
T ( n ) = T ( n / 2 ) + \Theta ( 1 ) \implies T ( n ) = \Theta ( \lg n / \lg
$$

### Images:
- data\Design and Analysis of Algorithms\L04-D&C\page_022\L04-D&C_page_022\auto\images\4a2a1ee657371c0dbfbaffecaa733dd0adadb12762e3f990e864f16486e9959b.jpg
- data\Design and Analysis of Algorithms\L04-D&C\page_022\L04-D&C_page_022\auto\images\8b5da5041080b444293d5f60a9dff45baa7d9ab23bfa5d673586dd07fd9fef0a.jpg

---

## Lecture: L04-D&C\page_023\L04-D&C_page_023\auto

# Fibonacci Numbers

# Recursive definition:

$$
F _ { n } = { \left\{ \begin{array} { l l } { 1 } & { { \mathrm { i f ~ } } n = 0 ; } \\ { 2 } & { { \mathrm { i f ~ } } n = 1 ; } \\ { F _ { n - 1 } + F _ { n - 2 } } & { { \mathrm { i f ~ } } n \geq 2 . } \end{array} \right. }
$$

0 1 1 2 3 5 8 13 21 34

### Images:
- data\Design and Analysis of Algorithms\L04-D&C\page_023\L04-D&C_page_023\auto\images\8ca5e129b5d2e2ea1969b8dc84efa61246f768869305933058eec4d89f737195.jpg

---

## Lecture: L04-D&C\page_024\L04-D&C_page_024\auto

# Fibonacci Numbers

Recursive definition:

$$
F _ { n } = { \left\{ \begin{array} { l l } { 0 } & { { \mathrm { i f } } n = 0 ; } \\ { 1 } & { { \mathrm { i f } } n = 1 ; } \\ { F _ { n - 1 } + F _ { n - 2 } } & { { \mathrm { i f } } n \geq 2 . } \end{array} \right. }
$$

0 1 1 2 3 5 8 13 21 34

Naive recursive algorithm: $\Omega ( \phi ^ { n } )$ (exponential time), where $\phi = ( 1 + \sqrt { 5 } ) / 2$ is the golden ratio.

### Images:
- data\Design and Analysis of Algorithms\L04-D&C\page_024\L04-D&C_page_024\auto\images\15112291e511402fb34156a50c59713f7d406b4e428d3cc75337992fdd19ae55.jpg

---

## Lecture: L04-D&C\page_025\L04-D&C_page_025\auto

# Computing Fibonacci Numbers

# Bottom-up:

● Compute $F _ { 0 } , F _ { 1 } , F _ { 2 } , . . . , F _ { n }$ in order, forming each number by summing the two previous.

Running time: $\Theta ( n )$ .

---

## Lecture: L04-D&C\page_026\L04-D&C_page_026\auto

# Computing Fibonacci Numbers

# Bottom-up:

• Compute $F _ { 0 } , F _ { 1 } , F _ { 2 } , . . . , F _ { n }$ in order, forming each number by summing the two previous.

Running time: $\Theta ( n )$ .

Naive recursive squaring:

$F _ { n } = \phi ^ { n } / 5$ rounded to the nearest integer.

• Recursive squaring: $\Theta ( \lg n )$ time.

• This method is unreliable, since floating-point arithmetic is prone to round-off errors.

---

## Lecture: L04-D&C\page_027\L04-D&C_page_027\auto

# Recursive Squaring

${ \left[ \begin{array} { l l } { F _ { n + 1 } } & { F _ { n } } \\ { F _ { n } } & { F _ { n - 1 } } \end{array} \right] } = { \left[ \begin{array} { l l } { 1 } & { 1 } \\ { 1 } & { 0 } \end{array} \right] } ^ { n }$ Theorem:

### Images:
- data\Design and Analysis of Algorithms\L04-D&C\page_027\L04-D&C_page_027\auto\images\0debcb71c7bd67e1b7ec8d5d9fa384098b3917797a88a4eb824d5c0ada8c1b1e.jpg

---

## Lecture: L04-D&C\page_028\L04-D&C_page_028\auto

# Recursive Squaring

Theorem: ${ \left[ \begin{array} { l l } { F _ { n + 1 } } & { F _ { n } } \\ { F _ { n } } & { F _ { n - 1 } } \end{array} \right] } = { \left[ \begin{array} { l l } { 1 } & { 1 } \\ { 1 } & { 0 } \end{array} \right] } ^ { n }$

Algorithm: Recursive squaring. ${ \mathrm { T i m e } } = \Theta ( \lg n )$ .

### Images:
- data\Design and Analysis of Algorithms\L04-D&C\page_028\L04-D&C_page_028\auto\images\007589e05cc007a9fa578346304918b898be5c6cebae651ab4143fef981ad800.jpg
- data\Design and Analysis of Algorithms\L04-D&C\page_028\L04-D&C_page_028\auto\images\cbefd6f7b908bf10f48cab3f83a94884d5bff5e143c33a3ec92fe827e3413284.jpg

---

## Lecture: L04-D&C\page_029\L04-D&C_page_029\auto

# Recursive Squaring

Theorem: ${ \left[ \begin{array} { l l } { F _ { n + 1 } } & { F _ { n } } \\ { F _ { n } } & { F _ { n - 1 } } \end{array} \right] } = { \left[ \begin{array} { l l } { 1 } & { 1 } \\ { 1 } & { 0 } \end{array} \right] } ^ { n }$

Algorithm: Recursive squaring.

${ \mathrm { T i m e } } = \Theta ( \lg n )$ .

Proof of theorem. (Induction on n.)

$$
{ \mathrm { : ~ } } ( n = 1 ) \colon { \left[ \begin{array} { l l } { F _ { 2 } } & { F _ { 1 } } \\ { F _ { 1 } } & { F _ { 0 } } \end{array} \right] } = { \left[ \begin{array} { l l } { 1 } & { 1 } \\ { 1 } & { 0 } \end{array} \right] } ^ { 1 }
$$

### Images:
- data\Design and Analysis of Algorithms\L04-D&C\page_029\L04-D&C_page_029\auto\images\74fd549825f8cd9ef145fc973212654b0c80ecd38270fb1a601843e0bbf44c7d.jpg
- data\Design and Analysis of Algorithms\L04-D&C\page_029\L04-D&C_page_029\auto\images\e338e6c9c7041affdd8cae6b627b9480863b0dcb1044ddb3c701d27ad4a70e7f.jpg

---

## Lecture: L04-D&C\page_030\L04-D&C_page_030\auto

Inductive step (n ≥ 2):

$$
\begin{array} { r l } { \mathsf { F } _ { n + 1 } ^ { \mathsf { } } } & { F _ { n } ^ { \mathsf { } } } \\ { F _ { n } ^ { \prime } } & { F _ { n - 1 } ^ { \prime } } \end{array} ] = [ \begin{array} { l l } { F _ { n } ^ { \prime } } & { F _ { n - 1 } ^ { \prime } } \\ { F _ { n - 1 } } & { F _ { n - 2 } ^ { \prime } } \end{array} ] \cdot \begin{array} { l } { \mathsf { I } } & { } \\ { \mathsf { I } } & { = [ \begin{array} { l l } { 1 } & { 1 } \\ { 1 } & { 0 } \end{array} ] ^ { n - 1 } \cdot [ \begin{array} { l l } { 1 } & { } \\ { 1 } & { } \end{array}  } \\ { \mathsf { = } [ \begin{array} { l l } { 1 } & { 1 } \\ { 1 } & { 0 } \end{array} ] ^ { n } } \end{array}
$$

### Images:
- data\Design and Analysis of Algorithms\L04-D&C\page_030\L04-D&C_page_030\auto\images\b3b73cde5f96b38c102ac7584640e50be7a6475e890b5a9092ce995e1bfeadaf.jpg

---

## Lecture: L04-D&C\page_031\L04-D&C_page_031\auto

$$
\begin{array} { r l } { \mathbf { \Phi } _ { n + 1 } } & { { } F _ { n } \mathbf { ] } = \left[ F _ { n } \quad F _ { n - 1 } \right] \cdot \left[ \begin{array} { l } { 1 } \\ { 1 } \end{array} \right. } \end{array}
$$

### Images:
- data\Design and Analysis of Algorithms\L04-D&C\page_031\L04-D&C_page_031\auto\images\c5d12edc90155ff110a4b11ec574517d5b6becc4db399921615c992a8f74324f.jpg

---

## Lecture: L04-D&C\page_032\L04-D&C_page_032\auto

# Matrix Multiplication

Input: Output: $\begin{array} { l } { { A = [ a _ { i j } ] , B = [ b _ { i j } ] . \nonumber \ \} \ i , j = 1 , 2 , \ldots , n . } } \\ { { C = [ c _ { i j } ] = A { \cdot } B . \qquad \ } } \end{array}$

$$
{ \left[ \begin{array} { l } { \vdots } \\ { \vdots } \\ { a _ { n n } } \end{array} \right] } = { \left[ \begin{array} { l l l l } { a _ { 1 1 } } & { a _ { 1 2 } } & { \cdots } & { a _ { 1 n } } \\ { a _ { 2 1 } } & { a _ { 2 2 } } & { \cdots } & { a _ { 2 n } } \\ { \vdots } & { \vdots } & { \ddots } & { \vdots } \\ { a _ { n 1 } } & { a _ { n 2 } } & { \cdots } & { a _ { n n } } \end{array} \right] } . { \left[ \begin{array} { l l l l } { b _ { 1 1 } } & { b _ { 1 2 } } & { \cdots } & { b _ { 1 n } } \\ { b _ { 2 1 } } & { b _ { 2 2 } } & { \cdots } & { b _ { 2 n } } \\ { \vdots } & { \vdots } & { \ddots } & { \vdots } \\ { b _ { n 1 } } & { b _ { n 2 } } & { \cdots } & { b _ { n n } } \end{array} \right] }
$$

$$
c _ { i j } = \sum _ { k = 1 } ^ { n } a _ { i k } \cdot b _ { k j }
$$

### Images:
- data\Design and Analysis of Algorithms\L04-D&C\page_032\L04-D&C_page_032\auto\images\202917155e07406823e7db3c367c2ad9eae13b7ad317fb6743f1bc3faeeea4bf.jpg
- data\Design and Analysis of Algorithms\L04-D&C\page_032\L04-D&C_page_032\auto\images\3ef4a99b66c697bee5cf8fdb33d67a938b2ab6e10fb2b1c876d2c65040e12180.jpg
- data\Design and Analysis of Algorithms\L04-D&C\page_032\L04-D&C_page_032\auto\images\7786d3ca1426ba2607ad38e2170c5d5504e7deb45a2b70cbb73815deac206584.jpg

---

## Lecture: L04-D&C\page_033\L04-D&C_page_033\auto

# Standard Algorithm

for $i \gets 1$ to n do $\mathbf { f o r } j \gets 1$ to n do $c _ { i j } \gets 0$ $\mathbf { f o r } k \gets 1$ to n ${ \bf d o } \ c _ { i j }  c _ { i j } + a _ { i k } \cdot b _ { k j }$

### Images:
- data\Design and Analysis of Algorithms\L04-D&C\page_033\L04-D&C_page_033\auto\images\622f8f7e855911dd4627e7226482388bd389fd26fbef6ad2e3aa34ed9a335e82.jpg

---

## Lecture: L04-D&C\page_034\L04-D&C_page_034\auto

# Standard Algorithm

for $i \gets 1$ to n do $\mathbf { f o r } j \gets 1$ to n do $c _ { i j } \gets 0$ $\mathbf { f o r } k \gets 1$ to n ${ \bf d o } \ c _ { i j }  c _ { i j } + a _ { i k } \cdot b _ { k j }$

Running time = Θ(n3)

### Images:
- data\Design and Analysis of Algorithms\L04-D&C\page_034\L04-D&C_page_034\auto\images\1e139837ed7ba9ec4c0df0a4ea5c356f038b246468db6ad271f6f2ed2971f110.jpg

---

## Lecture: L04-D&C\page_035\L04-D&C_page_035\auto

# Divide-and-Conquer Algorithm

# IDEA:

$n { \times } n$ matrix = 2×2 matrix of $( n / 2 ) { \times } ( n / 2 )$ submatrices:

$$
\begin{array} { r } { \Big [ r \quad s \Big ] = \Big [ a \quad b \Big ] \cdot \Big [ e \quad f \Big ] } \\ { \Big [ t \quad u \Big ] = \Big [ c \quad d \Big ] \cdot \Big [ g \quad h \Big ] } \\ { \qquad C = \quad A \qquad B } \end{array}
$$

![](images/0ac2f4948adbb1d4c5094a455a6cd043adedd6a15af0662b008871cbc22cf9a3.jpg)

### Images:
- data\Design and Analysis of Algorithms\L04-D&C\page_035\L04-D&C_page_035\auto\images\0ac2f4948adbb1d4c5094a455a6cd043adedd6a15af0662b008871cbc22cf9a3.jpg
- data\Design and Analysis of Algorithms\L04-D&C\page_035\L04-D&C_page_035\auto\images\15fe4128ef9837352e7d7a474f5f96f3b572449d1d9cdcf8e0825382ef4bd116.jpg

---

## Lecture: L04-D&C\page_036\L04-D&C_page_036\auto

# Divide-and-Conquer Algorithm

# IDEA:

$n { \times } n$ matrix = 2×2 matrix of $( n / 2 ) { \times } ( n / 2 )$ submatrices:

![](images/803b4be0b0e0301ad6b44e38923e02845253c82e51e0e9146dfd410b36ed99c5.jpg)

### Images:
- data\Design and Analysis of Algorithms\L04-D&C\page_036\L04-D&C_page_036\auto\images\803b4be0b0e0301ad6b44e38923e02845253c82e51e0e9146dfd410b36ed99c5.jpg

---

## Lecture: L04-D&C\page_037\L04-D&C_page_037\auto

# Analysis of D&C Algorithm

![](images/c1b97afcf7696aa99cf7c7970a4689435c49dd193831c52dafa35efe9f3cadd1.jpg)

### Images:
- data\Design and Analysis of Algorithms\L04-D&C\page_037\L04-D&C_page_037\auto\images\c1b97afcf7696aa99cf7c7970a4689435c49dd193831c52dafa35efe9f3cadd1.jpg

---

## Lecture: L04-D&C\page_038\L04-D&C_page_038\auto

# Analysis of D&C Algorithm

![](images/9daa2072efaaacf0fb283cc3ea99c638fa3cdf433e467656cbc46a2243263477.jpg)

nlogba = nlog28 = n3 ⇒ CASE 1 ⇒ T(n) = Θ(n3).

### Images:
- data\Design and Analysis of Algorithms\L04-D&C\page_038\L04-D&C_page_038\auto\images\9daa2072efaaacf0fb283cc3ea99c638fa3cdf433e467656cbc46a2243263477.jpg

---

## Lecture: L04-D&C\page_039\L04-D&C_page_039\auto

# Analysis of D&C Algorithm

![](images/5e4386fb22bd4bc0f94398337e33a6423cb39a88c5c4bff60fd3850a2feda5f3.jpg)

nlogba = nlog28 = n3 ⇒ CASE 1 ⇒ T(n) = Θ(n3).

No better than the ordinary algorithm.

### Images:
- data\Design and Analysis of Algorithms\L04-D&C\page_039\L04-D&C_page_039\auto\images\5e4386fb22bd4bc0f94398337e33a6423cb39a88c5c4bff60fd3850a2feda5f3.jpg

---

## Lecture: L04-D&C\page_040\L04-D&C_page_040\auto

# • Multiply $2 \times 2$ matrices with only 7 recursive mults.

---

## Lecture: L04-D&C\page_041\L04-D&C_page_041\auto

• Multiply $2 \times 2$ matrices with only 7 recursive mults.

$$
\begin{array} { r l } & { P _ { 1 } = a \cdot ( f - h ) } \\ & { P _ { 2 } = ( a + b ) \cdot h } \\ & { P _ { 3 } = ( c + d ) \cdot e } \\ & { P _ { 4 } = d \cdot ( g - e ) } \\ & { P _ { 5 } = ( a + d ) \cdot ( e + h ) } \\ & { P _ { 6 } = ( b - d ) \cdot ( g + h ) } \\ & { P _ { 7 } = ( a - c ) \cdot ( e + f ) } \end{array}
$$

### Images:
- data\Design and Analysis of Algorithms\L04-D&C\page_041\L04-D&C_page_041\auto\images\363d53f63025c58d49dc0fd69a318794f574274dd262bfa7280bfd84d32575bb.jpg

---

## Lecture: L04-D&C\page_042\L04-D&C_page_042\auto

# Strassen’s Idea

• Multiply $2 \times 2$ matrices with only 7 recursive mults.

$$
\begin{array} { r l } & { P _ { 1 } = a \cdot ( f - h ) } \\ & { P _ { 2 } = ( a + b ) \cdot h } \\ & { P _ { 3 } = ( c + d ) \cdot e } \\ & { P _ { 4 } = d \cdot ( g - e ) } \\ & { P _ { 5 } = ( a + d ) \cdot ( e + h ) } \\ & { P _ { 6 } = ( b - d ) \cdot ( g + h ) } \\ & { P _ { 7 } = ( a - c ) \cdot ( e + f ) } \end{array}
$$

$$
\begin{array} { l } { r = P _ { 5 } + P _ { 4 } - P _ { 2 } + P _ { 6 } } \\ { s = P _ { 1 } + P _ { 2 } } \\ { t = P _ { 3 } + P _ { 4 } } \\ { u = P _ { 5 } + P _ { 1 } - P _ { 3 } - P _ { 7 } } \end{array}
$$

### Images:
- data\Design and Analysis of Algorithms\L04-D&C\page_042\L04-D&C_page_042\auto\images\27d7e3720f80b19fe20a68a6f5d5291eef7f6e50d65d123b04df883cd14d466b.jpg
- data\Design and Analysis of Algorithms\L04-D&C\page_042\L04-D&C_page_042\auto\images\c47e76a34ee6e7c863eb24982fc79c34a5653bd67aa5a77a272f2b35d65753d6.jpg

---

## Lecture: L04-D&C\page_043\L04-D&C_page_043\auto

# Strassen’s Idea

Multiply $2 \times 2$ matrices with only 7 recursive mults.

$$
\begin{array} { r l } & { P _ { 1 } = a \cdot ( f - h ) } \\ & { P _ { 2 } = ( a + b ) \cdot h } \\ & { P _ { 3 } = ( c + d ) \cdot e } \\ & { P _ { 4 } = d \cdot ( g - e ) } \\ & { P _ { 5 } = ( a + d ) \cdot ( e + h ) } \\ & { P _ { 6 } = ( b - d ) \cdot ( g + h ) } \\ & { P _ { 7 } = ( a - c ) \cdot ( e + f ) } \end{array}
$$

$$
\begin{array} { l } { r = P _ { 5 } + P _ { 4 } - P _ { 2 } + P _ { 6 } } \\ { s = P _ { 1 } + P _ { 2 } } \\ { t = P _ { 3 } + P _ { 4 } } \\ { u = P _ { 5 } + P _ { 1 } - P _ { 3 } - P _ { 7 } } \end{array}
$$

7 mults, 18 adds/subs.

Note: No reliance on commutativity of mult!

### Images:
- data\Design and Analysis of Algorithms\L04-D&C\page_043\L04-D&C_page_043\auto\images\479dc350970ed8ba3f182bf53917a0c296e9a881d6314134a7ec8e81a7cf423d.jpg
- data\Design and Analysis of Algorithms\L04-D&C\page_043\L04-D&C_page_043\auto\images\57e622c62368c2bc312e5004ca1e5ce14941bd624c8d33b76016896e5daf1e6a.jpg

---

## Lecture: L04-D&C\page_044\L04-D&C_page_044\auto

# Strassen’s Idea

- Multiply $2 \times 2$ matrices with only 7 recursive mults.

$$
\begin{array} { r l } & { P _ { 1 } = a \cdot ( f - h ) } \\ & { P _ { 2 } = ( a + b ) \cdot h } \\ & { P _ { 3 } = ( c + d ) \cdot e } \\ & { P _ { 4 } = d \cdot ( g - e ) } \\ & { P _ { 5 } = ( a + d ) \cdot ( e + h ) } \\ & { P _ { 6 } = ( b - d ) \cdot ( g + h ) } \\ & { P _ { 7 } = ( a - c ) \cdot ( e + f ) } \end{array}
$$

![](images/343870d6c24ee2e87c8b2dc7774aeab5220c477feffdf34eba7fcf94b8d12fcf.jpg)

### Images:
- data\Design and Analysis of Algorithms\L04-D&C\page_044\L04-D&C_page_044\auto\images\343870d6c24ee2e87c8b2dc7774aeab5220c477feffdf34eba7fcf94b8d12fcf.jpg
- data\Design and Analysis of Algorithms\L04-D&C\page_044\L04-D&C_page_044\auto\images\57aeba387267b45c9fa8e22e5a059ba04a744ff2852e3f117ec7da3b824677f7.jpg

---

## Lecture: L04-D&C\page_045\L04-D&C_page_045\auto

# Strassen’s Algorithm

1. Divide: Partition $A$ and $B$ into $( n / 2 ) { \times } ( n / 2 )$ submatrices. Form terms to be multiplied using + and – .

2. Conquer: Perform 7 multiplications of $( n / 2 ) { \times } ( n / 2 )$ submatrices recursively.

3. Combine: Form $C$ using + and – on $( n / 2 ) { \times } ( n / 2 )$ submatrices.

---

## Lecture: L04-D&C\page_046\L04-D&C_page_046\auto

# Strassen’s Algorithm

1. Divide: Partition $A$ and $B$ into $( n / 2 ) { \times } ( n / 2 )$ submatrices. Form terms to be multiplied using + and – .

2. Conquer: Perform 7 multiplications of $( n / 2 ) { \times } ( n / 2 )$ submatrices recursively.

3. Combine: Form $C$ using + and – on $( n / 2 ) { \times } ( n / 2 )$ submatrices.

$$
T ( n ) = 7 \ T ( n / 2 ) + \Theta ( n ^ { 2 } )
$$

### Images:
- data\Design and Analysis of Algorithms\L04-D&C\page_046\L04-D&C_page_046\auto\images\f33162d0a15329358dc1e88ada58c491a07e70ccd785e6eb8369e5a7b1f68e48.jpg

---

## Lecture: L04-D&C\page_047\L04-D&C_page_047\auto

# Analysis of Strassen

$$
T ( n ) = 7 \ T ( n / 2 ) + \Theta ( n ^ { 2 } )
$$

### Images:
- data\Design and Analysis of Algorithms\L04-D&C\page_047\L04-D&C_page_047\auto\images\66a6368025c9d91c8f886fb33e38776bb4e5b91f24b62a622543031d2a6c84bd.jpg

---

## Lecture: L04-D&C\page_048\L04-D&C_page_048\auto

# Analysis of Strassen

$$
T ( n ) = 7 \ T ( n / 2 ) + \Theta ( n ^ { 2 } )
$$

nlogba = nlog27 ≈ n2.81 ⇒ CASE 1 ⇒ T(n) = Θ(nlg 7).

### Images:
- data\Design and Analysis of Algorithms\L04-D&C\page_048\L04-D&C_page_048\auto\images\c25267b2a9b724b4deb4a0613823c218f6a4817f8711c2c721da00429322471b.jpg

---

## Lecture: L04-D&C\page_049\L04-D&C_page_049\auto

# Analysis of Strassen

$$
T ( n ) = 7 \ T ( n / 2 ) + \Theta ( n ^ { 2 } )
$$

# nlogba = nlog27 ≈ n2.81 ⇒ CASE 1 ⇒ T(n) = Θ(nlg 7).

The number $2 . 8 1$ may not seem much smaller than 3, but because the difference is in the exponent, the impact on running time is significant. In fact, Strassen’s algorithm beats the ordinary algorithm on today’s machines for $n \geq 3 2$ or so.

### Images:
- data\Design and Analysis of Algorithms\L04-D&C\page_049\L04-D&C_page_049\auto\images\b726c0fd9acc7b24cdb758d13778340b689d70aa2b258c2278c143022134c74f.jpg

---

## Lecture: L04-D&C\page_050\L04-D&C_page_050\auto

# Analysis of Strassen

$$
T ( n ) = 7 \ T ( n / 2 ) + \Theta ( n ^ { 2 } )
$$

# nlogba = nlog27 ≈ n2.81 ⇒ CASE 1 ⇒ T(n) = Θ(nlg 7).

The number 2.81 may not seem much smaller than 3, but because the difference is in the exponent, the impact on running time is significant. In fact, Strassen’s algorithm beats the ordinary algorithm on today’s machines for $n \geq 3 2$ or so.

Best to date (of theoretical interest only): $\Theta ( n ^ { 2 . 3 7 6 \dots } )$ .

### Images:
- data\Design and Analysis of Algorithms\L04-D&C\page_050\L04-D&C_page_050\auto\images\e3dca51920644d1874d91837766f3d95d01b3f8e3b826da838dd420a0bda8d45.jpg

---

## Lecture: L04-D&C\page_051\L04-D&C_page_051\auto

# Conclusion

• Divide and conquer is just one of several powerful techniques for algorithm design.

Divide-and-conquer algorithms can be analyzed using recurrences and the master method (so practice this math).

The divide-and-conquer strategy often leads to efficient algorithms.

---

## Lecture: L05-basic-structures\page_001\L05-basic-structures_page_001\auto

# Design and Analysis of Algorithms

# Basic Data Structures

-Arrays Linked Lists Stacks - Queues

---

## Lecture: L05-basic-structures\page_002\L05-basic-structures_page_002\auto

# What Is a Data Structure

“A data structure is a way to store and organize data in order to facilitate access and modifications. Using the appropriate data structure or structures is an important part of algorithm design. No single data structure works well for all purposes, and so you should know the strengths and limitations of several of them.”

---

## Lecture: L05-basic-structures\page_003\L05-basic-structures_page_003\auto

# Basic Data Structures

Arrays Lists Stacks Queues Trees

![](images/97bfc5570609b587ac074d3c0fe9c66f4e0c9f5380c394c5f81396d71c60e414.jpg)

### Images:
- data\Design and Analysis of Algorithms\L05-basic-structures\page_003\L05-basic-structures_page_003\auto\images\97bfc5570609b587ac074d3c0fe9c66f4e0c9f5380c394c5f81396d71c60e414.jpg

---

## Lecture: L05-basic-structures\page_004\L05-basic-structures_page_004\auto

• An array is a linear data structure that stores a fixed-size collection of elements of the same type in contiguous memory locations.

– Fixed Size – Its size is declared at initialization and cannot be changed.

– Contiguous Memory Allocation – Elements are stored sequentially in memory, making access fast (O(1) for direct access by index).

– Homogeneous – All elements in an array must be of the same data type.   
– Index-Based Access – Elements are accessed using an index, starting from 1.

Array:

<table><tr><td>10</td><td>25</td><td>30</td><td>40</td><td>50</td></tr><tr><td>1</td><td colspan="2">2 3</td><td colspan="2">4 5</td></tr></table>

Index:

### Images:
- data\Design and Analysis of Algorithms\L05-basic-structures\page_004\L05-basic-structures_page_004\auto\images\097f4f85e77f880072f6dd6dfd7f4f53f4b82562d71f63d5b732ad2d3837cecc.jpg

---

## Lecture: L05-basic-structures\page_005\L05-basic-structures_page_005\auto

# Array-based Matrix

• We can use an array or arrays to store a matrix.

$$
M = { \left( \begin{array} { l l l } { 1 } & { 2 } & { 3 } \\ { 4 } & { 5 } & { 6 } \end{array} \right) }
$$

<table><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>6</td></tr></table>

![](images/c814bc120828754d25ac9123e3b075bdbf6427c116d2f7689b2661d503dbbf7b.jpg)

![](images/ed7a4e971eff5d8640a7aa190155c0e8d02233a5373939578a46fe12e297c015.jpg)

<table><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>42</td><td rowspan=1 colspan=1>42</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>6</td></tr></table>

Row-major ordering

Column-major ordering

Row-major ordering

Column-major ordering

Blue: Array of pointers to arrays

![](images/b2f5399fbbd80729f6469ddf68ab3b18b91550eff745247752e1b4f1e678b078.jpg)

### Images:
- data\Design and Analysis of Algorithms\L05-basic-structures\page_005\L05-basic-structures_page_005\auto\images\16ada1d4c6eaa8384555ad8f3d488ff39aaaf282e0d0ceb84d8ce9ca4e8e6470.jpg
- data\Design and Analysis of Algorithms\L05-basic-structures\page_005\L05-basic-structures_page_005\auto\images\217e376744e68d5458000d0128efc32a754a99e10bf066a5b9309b379e1a3e88.jpg
- data\Design and Analysis of Algorithms\L05-basic-structures\page_005\L05-basic-structures_page_005\auto\images\3f37d7854c50f478ed73d0557cf60ae6eae9807a4b2d54b495203267e97b3d35.jpg
- data\Design and Analysis of Algorithms\L05-basic-structures\page_005\L05-basic-structures_page_005\auto\images\b2f5399fbbd80729f6469ddf68ab3b18b91550eff745247752e1b4f1e678b078.jpg
- data\Design and Analysis of Algorithms\L05-basic-structures\page_005\L05-basic-structures_page_005\auto\images\c814bc120828754d25ac9123e3b075bdbf6427c116d2f7689b2661d503dbbf7b.jpg
- data\Design and Analysis of Algorithms\L05-basic-structures\page_005\L05-basic-structures_page_005\auto\images\ed7a4e971eff5d8640a7aa190155c0e8d02233a5373939578a46fe12e297c015.jpg

---

## Lecture: L05-basic-structures\page_006\L05-basic-structures_page_006\auto

# Implementing a Dynamic Array

• What if the array is full when appending a new element?

• We perform the following steps:

• Allocate a new array B with larger capacity.   
• Set $\mathsf { B } [ \mathsf { i } ] = \mathsf { A } [ \mathsf { i } ]$ , for $\dot { \mathsf { I } } = 0 ,$ , …, n - 1 where n denotes the current number of items.   
• Set $\mathsf { A } = \mathsf { B } .$ , i.e., we use B as the array supporting the list.   
• Insert the new element in the new array.

![](images/bf610dc142e0f2fcb9fe1ce645d0dc9bf2dcdd681f57f66461c1422aa6f3a8ab.jpg)

• How large of a new array to create?

• Common rule - the new array to have twice the capacity of the existing array.

### Images:
- data\Design and Analysis of Algorithms\L05-basic-structures\page_006\L05-basic-structures_page_006\auto\images\bf610dc142e0f2fcb9fe1ce645d0dc9bf2dcdd681f57f66461c1422aa6f3a8ab.jpg

---

## Lecture: L05-basic-structures\page_007\L05-basic-structures_page_007\auto

# Implementing a Dynamic Array

![](images/a72cf1b159e5016a6cf2004ab2d6c69042ef6f718bd86cd3c4362f1a6f44e43e.jpg)  
Run-time of a series of append operations on a dynamic array

3 class DynamicArray: self._capacity = 1 self._A[self._n] = obj B = self._make_array(c) B[k] $=$ self._A[k] self._capacity = c

The amortized cost for inserting each element is O(1).

### Images:
- data\Design and Analysis of Algorithms\L05-basic-structures\page_007\L05-basic-structures_page_007\auto\images\a72cf1b159e5016a6cf2004ab2d6c69042ef6f718bd86cd3c4362f1a6f44e43e.jpg

---

## Lecture: L05-basic-structures\page_008\L05-basic-structures_page_008\auto

# Singly Linked List

• A singly linked list is a dynamic data structure consisting of a sequence of nodes

• Each node contains two parts:

– Data – Stores the actual value.   
– Next Pointer – Points to the next node in the list.   
– The last node’s next pointer is NULL, indicating the end of the list.

![](images/787f540c402b742eb6d6cb49dcb8e10605a81dd5abb577557609f1acb9909355.jpg)

![](images/d8b5bcade798e388e2b3d7667084105653380f43831a02a9c35d5d52d2c0370b.jpg)

### Images:
- data\Design and Analysis of Algorithms\L05-basic-structures\page_008\L05-basic-structures_page_008\auto\images\787f540c402b742eb6d6cb49dcb8e10605a81dd5abb577557609f1acb9909355.jpg
- data\Design and Analysis of Algorithms\L05-basic-structures\page_008\L05-basic-structures_page_008\auto\images\d8b5bcade798e388e2b3d7667084105653380f43831a02a9c35d5d52d2c0370b.jpg

---

## Lecture: L05-basic-structures\page_009\L05-basic-structures_page_009\auto

# Singly Linked List

• Minimally, the linked list instance should keep:

– Head Reference: Needed to locate the first node and access the entire list.   
– Tail Reference: Optional but useful to quickly access the last node without traversing the list.   
– Size Count: Optional but helpful to track the number of nodes without having to traverse the list each time.

---

## Lecture: L05-basic-structures\page_010\L05-basic-structures_page_010\auto

# Inserting an Element at the Head

• An important property:

• the space is proportional to the current number of elements. we can easily insert an element at the head of the list.

• Steps for inserting an element: • Create a new node. • Set its element to the new element. • Set its next link to refer to the current head. • Set the list’s head to point to the new node.

![](images/c77ab32a726b33e572d677dc99fe06d7a01cd1ec63c55625a913e8eb5531ce83.jpg)

Algorithm add_first $( \mathsf { L } , \mathsf { e } )$

newest $=$ Node(e){create new node instance storing reference to element e} newest.next $=$ L.head   
L.head $\stackrel { \triangledown } { = }$ newest   
L.size $=$ L.size + 1 fincrement the node count}

### Images:
- data\Design and Analysis of Algorithms\L05-basic-structures\page_010\L05-basic-structures_page_010\auto\images\c77ab32a726b33e572d677dc99fe06d7a01cd1ec63c55625a913e8eb5531ce83.jpg

---

## Lecture: L05-basic-structures\page_011\L05-basic-structures_page_011\auto

# Removing an Element

C Removing from Head: Easy, just reverse the insert-at-head process.

Removing Last Node: Difficult because you need access to the node before the last one.

Accessing Preceding Node: Requires starting at the head and searching through the list.

![](images/1cd8bd0d8b3ab557b1881dfb61ecfbb4f87822d8a1b0e6e08bfa1b920b36237a.jpg)

Algorithm remove_first(L): if L.head is None then Indicate an error: the list is empty. L.head $\stackrel { } { = }$ L.head.next L.size $\circeq$ L.size −1

### Images:
- data\Design and Analysis of Algorithms\L05-basic-structures\page_011\L05-basic-structures_page_011\auto\images\1cd8bd0d8b3ab557b1881dfb61ecfbb4f87822d8a1b0e6e08bfa1b920b36237a.jpg

---

## Lecture: L05-basic-structures\page_012\L05-basic-structures_page_012\auto

# Doubly Linked List - Motivation

• Singly Linked List Limitation: Each node only points to the next one.

• Challenges:

• Hard to efficiently remove the last node.

• More generally, difficult to remove any node if you only have a reference to it, because you can't easily find the previous node to update its link.

![](images/5f1864f0246e2b72aa37fdc0d729a9314de83a5064807350026024b83509cbf4.jpg)

### Images:
- data\Design and Analysis of Algorithms\L05-basic-structures\page_012\L05-basic-structures_page_012\auto\images\5f1864f0246e2b72aa37fdc0d729a9314de83a5064807350026024b83509cbf4.jpg

---

## Lecture: L05-basic-structures\page_013\L05-basic-structures_page_013\auto

# Doubly Linked List

• Structure: Each node has links to both the next and previous nodes.

Advantages:

• Quick insertions and deletions anywhere in the list (O(1) time).

# Sentinel Nodes:

• Use special "header" and "trailer" nodes at the start and end.   
• These dummy nodes make handling edge cases easier.   
In an empty list, the header points to the trailer, and the trailer points back to the header.

![](images/addc451fa5eee629da2ebe776848d7e5fb26fbd97e99748d8f30626626667e14.jpg)

### Images:
- data\Design and Analysis of Algorithms\L05-basic-structures\page_013\L05-basic-structures_page_013\auto\images\addc451fa5eee629da2ebe776848d7e5fb26fbd97e99748d8f30626626667e14.jpg

---

## Lecture: L05-basic-structures\page_014\L05-basic-structures_page_014\auto

# Inserting with a Doubly Linked List

![](images/af5231d4759e6393b6603fe1401674a364a542d8b13d08bc11a1d1913237acb7.jpg)

### Images:
- data\Design and Analysis of Algorithms\L05-basic-structures\page_014\L05-basic-structures_page_014\auto\images\af5231d4759e6393b6603fe1401674a364a542d8b13d08bc11a1d1913237acb7.jpg

---

## Lecture: L05-basic-structures\page_015\L05-basic-structures_page_015\auto

# Deleting a Node in a Doubly Linked List

![](images/3a7399db5b937529d3a3796e896c88d95cc41c2a05ec30026421644a8fc19180.jpg)

Due to the use of sentinels, the same implementation can be used for deleting the first or the last node.

Removing a node at an arbitrary location

### Images:
- data\Design and Analysis of Algorithms\L05-basic-structures\page_015\L05-basic-structures_page_015\auto\images\3a7399db5b937529d3a3796e896c88d95cc41c2a05ec30026421644a8fc19180.jpg

---

## Lecture: L05-basic-structures\page_016\L05-basic-structures_page_016\auto

# Basic Implementation of a Doubly Linked List (1)

1 class _DoublyLinkedBase: Base Class declaratic   
2 A base class providing a doubly linked list representation.   
3   
4 #   
5 class_Node:   
6 Lightweight, nonpublic class for storing a doubly linked node..   
7 slots_ $=$ '_element','_prev','_next' # streamline memory   
8   
9 def_init_(self,element, prev,next):#initialize node's field   
10 self._element $=$ element #element to be stored   
11 self._prev $=$ prev #Previous node reference   
12 self._next $=$ next #next node reference   
13 #-   
14 def_init_(self):   
15 create an empty list.   
17 self. trader $=$ We maintain two   
18 self._header._next $=$ $=$ self._trailer #trailer is after header references: _prev   
29 self._trai self._trailer._prev prev $=$ self. _header # heaer if before trailer &_next   
$\mathit { \Theta } = \mathit { \Theta } \Theta$   
21   
22 def_len_(self):   
23 'Return the number of elements in the list..   
24 return self._size   
25   
26 def is_empty(self):   
27 'Return True if list is empty.   
28 return self._size $\scriptstyle = = \ 0$

---

## Lecture: L05-basic-structures\page_017\L05-basic-structures_page_017\auto

# Basic Implementation of a Doubly Linked List (2)

30 def_insert between(self, e, predecessor, successor):   
31 'Add element e between two existing nodes and return new node.   
32 newest $=$ self._Node(e, predecessor, successor) # linked to neighbors   
33 predecessor._next $=$ newest   
34 successor._prev $=$ newest   
35 self._size $+ = \textrm { 1 }$   
36 return newest   
37   
38 defdelete_node(self, node):   
39 'Delete nonsentinel node from the list and return its element.   
40 predecessor $=$ node._prev   
41 successor $=$ node._next   
42 predecessor._next $=$ successor   
43 successor. prev $=$ predecessor   
44 self._size $\mathbf { \Phi } - \mathbf { \Phi } _ { 1 }$ #record deleted element   
45 element $=$ node._element   
46 node._prev $=$ node._next $=$ node._element $=$ None # deprecate node   
47 return element #return deleted element

---

## Lecture: L05-basic-structures\page_018\L05-basic-structures_page_018\auto

# Link-Based Vs Array-Based Sequences

<table><tr><td rowspan=1 colspan=1>Feature</td><td rowspan=1 colspan=1>Array</td><td rowspan=1 colspan=1>Linked Lists</td></tr><tr><td rowspan=1 colspan=1>Access Time</td><td rowspan=1 colspan=1>O(1) for accessingelements via index</td><td rowspan=1 colspan=1>O(1) if knowing thereference to the node</td></tr><tr><td rowspan=1 colspan=1>Insertion/Deletion</td><td rowspan=1 colspan=1>O(n), requires shiftingelements</td><td rowspan=1 colspan=1>O(1) at any position</td></tr><tr><td rowspan=1 colspan=1>Storage</td><td rowspan=1 colspan=1>Continuous</td><td rowspan=1 colspan=1>Consist of small blocks, notnecessarily continuous</td></tr><tr><td rowspan=1 colspan=1>Memory Usage</td><td rowspan=1 colspan=1>O(n) space; more memory-efficient, stores onlyelements</td><td rowspan=1 colspan=1>O(n) space; less memory-efficient, stores elementand pointers</td></tr><tr><td rowspan=1 colspan=1>Performance Consistency</td><td rowspan=1 colspan=1> May have variableperformance due toresizing</td><td rowspan=1 colspan=1>Consistent performance,predictable time bounds</td></tr><tr><td rowspan=1 colspan=1>Use Case Efficiency</td><td rowspan=1 colspan=1>Better for scenariosrequiring frequent access</td><td rowspan=1 colspan=1>Better for scenarios withfrequentinsertions/deletions</td></tr></table>

### Images:
- data\Design and Analysis of Algorithms\L05-basic-structures\page_018\L05-basic-structures_page_018\auto\images\2cc6dfe556eae89d374972ba251f68f3f1c9cbdae2ca3bd9f5261a7fa8577764.jpg

---

## Lecture: L05-basic-structures\page_019\L05-basic-structures_page_019\auto

# Stack

def. A list for which Insert (push) and Delete (pop) are allowed only at one end of the list (the top)  LIFO – Last in, First out

![](images/92e8c8f249352771272c69a9bf9f739a4c25dd734d22f0ec79eb6f2434148d8e.jpg)

• Objects: A finite sequence of nodes

# Operations:

– Push: Insert element at top – Pop: Remove and return top element

• Applications: undo operations

![](images/77b88081b8c46cce04596933a3614f5b31b191ad768f3db29d59bf301b519e63.jpg)

### Images:
- data\Design and Analysis of Algorithms\L05-basic-structures\page_019\L05-basic-structures_page_019\auto\images\77b88081b8c46cce04596933a3614f5b31b191ad768f3db29d59bf301b519e63.jpg
- data\Design and Analysis of Algorithms\L05-basic-structures\page_019\L05-basic-structures_page_019\auto\images\92e8c8f249352771272c69a9bf9f739a4c25dd734d22f0ec79eb6f2434148d8e.jpg

---

## Lecture: L05-basic-structures\page_020\L05-basic-structures_page_020\auto

# Exercise: Stack

• Describe the output of the following series of stack operations

– Push(8) – Push(3) – Pop() – Push(2) – Push(5) – Pop() – Pop() – Push(9) – Push(1)

---

## Lecture: L05-basic-structures\page_021\L05-basic-structures_page_021\auto

# Array-based Stack

![](images/e13b5ff29b3d17ccbb95acdf1a402f3e7276f539f8b0d7308c23c62185faafd0.jpg)

### Images:
- data\Design and Analysis of Algorithms\L05-basic-structures\page_021\L05-basic-structures_page_021\auto\images\e13b5ff29b3d17ccbb95acdf1a402f3e7276f539f8b0d7308c23c62185faafd0.jpg

---

## Lecture: L05-basic-structures\page_022\L05-basic-structures_page_022\auto

# Growable Array-Based Stack

INITIALIZE(S, size)   
1 S.size $=$ size   
2 S.array $=$ new array of size S.size   
3 S.top = 0 # Stack starts empty

# STACK-EMPTY(S)

1 if S.top == 0   
2 return TRUE   
3 else return FALSE

# GROW(S)

1 new_size = 2 \* S.size # Double the size   
2 new_array $=$ new array of size new_size   
3 for $\dot { \textbf { 1 } } = \textbf { 1 }$ to S.size:   
4 new_array[i] = S.array[i] # Copy elements   
5 S.array $=$ new_array   
6 S.size $=$ new_size   
PUSH(S, x)   
1 if S.top == S.size:   
2 GROW(S) # Expand the array   
3 S.top = S.top + 1   
4 S.array[S.top] = x   
POP(S)   
1 if STACK-EMPTY(S)   
2 error "underflow"   
3 else S.top $=$ S.top - 1   
5 return S[S.top+1]

---

## Lecture: L05-basic-structures\page_023\L05-basic-structures_page_023\auto

# Stack with a Singly Linked List

• We can implement a stack with a singly linked list • The top element is stored at the first node of the list The space used is $O ( n )$ and each operation of the Stack takes O(1) time

![](images/c603f89120855554c09b15e1a18f02729e60263e523363b44a66c648b79ce5ba.jpg)

### Images:
- data\Design and Analysis of Algorithms\L05-basic-structures\page_023\L05-basic-structures_page_023\auto\images\c603f89120855554c09b15e1a18f02729e60263e523363b44a66c648b79ce5ba.jpg

---

## Lecture: L05-basic-structures\page_024\L05-basic-structures_page_024\auto

# Stack Summary

<table><tr><td rowspan=1 colspan=1>Implementation</td><td rowspan=1 colspan=1>Push</td><td rowspan=1 colspan=1>Pop</td><td rowspan=1 colspan=1>isEmpty</td><td rowspan=1 colspan=1>Top</td><td rowspan=1 colspan=1>Space</td></tr><tr><td rowspan=1 colspan=1>Fixed-size Array</td><td rowspan=1 colspan=1>0(1)</td><td rowspan=1 colspan=1>0(1)</td><td rowspan=1 colspan=1>0(1)</td><td rowspan=1 colspan=1>0(1)</td><td rowspan=1 colspan=1>O(n) (Extra capacity overhead)</td></tr><tr><td rowspan=1 colspan=1>Growable Array</td><td rowspan=1 colspan=1>O(1) amortized/O(n) worst</td><td rowspan=1 colspan=1>0(1)</td><td rowspan=1 colspan=1>0(1)</td><td rowspan=1 colspan=1>0(1)</td><td rowspan=1 colspan=1>O(n) (Extra capacity overhead)</td></tr><tr><td rowspan=1 colspan=1>Linked List</td><td rowspan=1 colspan=1>0(1)</td><td rowspan=1 colspan=1>0(1)</td><td rowspan=1 colspan=1>0(1)</td><td rowspan=1 colspan=1>0(1)</td><td rowspan=1 colspan=1>O(n) (Extra pointer overhead)</td></tr></table>

• Fixed-Size Array: Best for known, small-sized stacks but has wasted memory when underutilized.

• Growable Array: Balances flexibility and speed, but resizing incurs occasional O(n) cost.

• Linked List: No need to predefine size, but higher space overhead (extra pointers for each node).

### Images:
- data\Design and Analysis of Algorithms\L05-basic-structures\page_024\L05-basic-structures_page_024\auto\images\3ce804da25c930fa8ad54dee44d062de9f6a19560181ef93a8e04899777a0256.jpg

---

## Lecture: L05-basic-structures\page_025\L05-basic-structures_page_025\auto

• def.: A Queue is a linear data structure that follows the FIFO (First In, First Out) principle. This means that elements are added at the rear (enqueue) and removed from the front (dequeue).

# • Operations:

– Enqueue(x) → Adds x to the rear.   
– Dequeue() Removes and returns the front element.

Applications: printer’s jobs

![](images/f4d6d566424038afc8f6a49cfcad4d72e5da4b60e6d6210e6be0775c02c05d49.jpg)

### Images:
- data\Design and Analysis of Algorithms\L05-basic-structures\page_025\L05-basic-structures_page_025\auto\images\f4d6d566424038afc8f6a49cfcad4d72e5da4b60e6d6210e6be0775c02c05d49.jpg

---

## Lecture: L05-basic-structures\page_026\L05-basic-structures_page_026\auto

# Exercise: Queues

• Describe the output of the following series of queue operations

– enqueue(8) – enqueue(3) – dequeue() – enqueue(2) – enqueue(5) – dequeue() – dequeue() – enqueue(9) – enqueue(1)

---

## Lecture: L05-basic-structures\page_027\L05-basic-structures_page_027\auto

# Circular Array based Queue

![](images/35b99d5dde66aa2d36ac0deb69887291d2e47a873503316ba956d73c77a375b0.jpg)

INITIALIZE(Q, size)   
1 Q.size $=$ size   
2 Q.array $=$ new array of size Q.size   
3 Q.head $=$ -1 # Indicates an empty queue   
4 Q.tail = -1   
IS-EMPTY(Q)   
1 return Q.head == -1   
IS-FULL(Q)   
1 return (Q.tail + 1) % Q.size $= = ~ 0$ .head   
ENQUEUE(Q, x)   
1 if IS-FULL(Q):   
2 error "Queue is full"   
3 else if IS-EMPTY(Q):   
4 Q.head $=$ Q.tail = 0 # First element in queue   
5 else:   
6 Q.tail = (Q.tail + 1) $\%$ Q.size # wrap around   
7 Q.array[Q.tail] = x

### Images:
- data\Design and Analysis of Algorithms\L05-basic-structures\page_027\L05-basic-structures_page_027\auto\images\35b99d5dde66aa2d36ac0deb69887291d2e47a873503316ba956d73c77a375b0.jpg

---

## Lecture: L05-basic-structures\page_028\L05-basic-structures_page_028\auto

# Circular Array based Queue (cont.)

![](images/ecf8fca880149743dfa634e4594dfa8b9720042051d2e12debaf1cfab7745a7a.jpg)

DEQUEUE(Q)   
1 if IS-EMPTY(Q):   
2 error "Queue is empty"   
3 else:   
4 temp $= 0$ .array[Q.head] #Store the head element   
5 if Q.head $= = ~ 0$ .tail: #Only 1 element was present   
6 Q.head $=$ Q.tail $=$ -1 # Reset queue   
7 else:   
8 Q.head $=$ (Q.head + 1) % Q.size #wrap around   
9 return temp

FRONT(Q) 1 if IS-EMPTY(Q): 2 error "Queue is empty" 3 return Q.array[Q.head]

### Images:
- data\Design and Analysis of Algorithms\L05-basic-structures\page_028\L05-basic-structures_page_028\auto\images\ecf8fca880149743dfa634e4594dfa8b9720042051d2e12debaf1cfab7745a7a.jpg

---

## Lecture: L05-basic-structures\page_029\L05-basic-structures_page_029\auto

# Growable Array-based Queue

• In an enqueue operation, when the array is full, instead of throw an exception, we can replace the array with doubled sized • Similar to what we did for an array-based stack • The enqueue operation has amortized running time O(1)

---

## Lecture: L05-basic-structures\page_030\L05-basic-structures_page_030\auto

# Queue with a Singly Linked List

We can implement a queue with a singly linked list – The front element is stored at the head of the list – The rear element is stored at the tail of the list

• The space used is $O ( n )$ and each operation of the Queue takes O(1) time   
• the queue is NEVER full

![](images/6b5c3d13f47bf6e66ff8fd5dd40aaa9323c1cd16ddebd70e935451429b52b239.jpg)

### Images:
- data\Design and Analysis of Algorithms\L05-basic-structures\page_030\L05-basic-structures_page_030\auto\images\6b5c3d13f47bf6e66ff8fd5dd40aaa9323c1cd16ddebd70e935451429b52b239.jpg

---

## Lecture: L05-basic-structures\page_031\L05-basic-structures_page_031\auto

# Queues Summary

<table><tr><td rowspan=1 colspan=1>Implementation</td><td rowspan=1 colspan=1>Enqueue</td><td rowspan=1 colspan=1>Dequeue</td><td rowspan=1 colspan=1>isEmpty</td><td rowspan=1 colspan=1>Head</td><td rowspan=1 colspan=1>Space</td></tr><tr><td rowspan=1 colspan=1>Circular Array</td><td rowspan=1 colspan=1>0(1)</td><td rowspan=1 colspan=1>0(1)</td><td rowspan=1 colspan=1>0(1)</td><td rowspan=1 colspan=1>0(1)</td><td rowspan=1 colspan=1>O(n) (Fixed size, extra capacity overhead)</td></tr><tr><td rowspan=1 colspan=1>Growable Array</td><td rowspan=1 colspan=1>0(1) amortized/o(n) worst</td><td rowspan=1 colspan=1>0(1)</td><td rowspan=1 colspan=1>0(1)</td><td rowspan=1 colspan=1>0(1)</td><td rowspan=1 colspan=1>O(n) (Extra capacity overhead)</td></tr><tr><td rowspan=1 colspan=1>Linked List</td><td rowspan=1 colspan=1>0(1)</td><td rowspan=1 colspan=1>0(1)</td><td rowspan=1 colspan=1>0(1)</td><td rowspan=1 colspan=1>0(1)</td><td rowspan=1 colspan=1>O(n) (Extra pointer overhead)</td></tr></table>

• Circular Array: Best for known, small-sized queues but has wasted memory when underutilized.

• Growable Array: Balances flexibility and speed, but resizing incurs occasional O(n) cost.

• Linked List: No need to predefine size, but higher space overhead (extra pointers for each node).

### Images:
- data\Design and Analysis of Algorithms\L05-basic-structures\page_031\L05-basic-structures_page_031\auto\images\2a9a613467a40ba6c4c969aa200de044b998fc5aa254bb2162a95849e6a207d1.jpg
- data\Design and Analysis of Algorithms\L05-basic-structures\page_031\L05-basic-structures_page_031\auto\images\7367653a16d9799f8555ae953784b13f379cd3a75f8909f229147f97363458eb.jpg

---

## Lecture: L05-basic-structures\page_032\L05-basic-structures_page_032\auto

# Deque: double-ended queue

• Def. A Deque (Pronounced ‘deck’) is a linear data structure that allows insertion and deletion from both ends (front and rear).

• Supports both FIFO and LIFO operations. – Insert and delete from both front and rear.

• More flexible than a normal queue. – Efficient O(1) insertion $\&$ deletion at both ends

![](images/fd471cc0db5116360093ae7e682611d386fb9462593ec5d12e20b3e8faf48a9e.jpg)

### Images:
- data\Design and Analysis of Algorithms\L05-basic-structures\page_032\L05-basic-structures_page_032\auto\images\fd471cc0db5116360093ae7e682611d386fb9462593ec5d12e20b3e8faf48a9e.jpg

---

## Lecture: L05-basic-structures\page_033\L05-basic-structures_page_033\auto

# Deque with a Doubly Linked List

• We can implement a deque with a doubly linked list

– The front element is stored at the first node – The rear element is stored at the last node

• The space used is $O ( n )$ and each operation of the Deque ADT takes O(1) time

![](images/89eafdc584f26a8206832c1a8690a84062c5dfaafa989f6cd9441c2ec2c95d46.jpg)

### Images:
- data\Design and Analysis of Algorithms\L05-basic-structures\page_033\L05-basic-structures_page_033\auto\images\89eafdc584f26a8206832c1a8690a84062c5dfaafa989f6cd9441c2ec2c95d46.jpg

---

## Lecture: L05-basic-structures\page_034\L05-basic-structures_page_034\auto

# Implementing Deques with Doubly Linked Lists

Here’s a visualization of the code for   
removeLast().

![](images/028b83d8584dba7c1efeff5c0371b7782b3ea988fd7c9c66e9d5553d5e72d45a.jpg)

![](images/6a4bd267a979b28cc52159a2c533050d006d5509cd6fbf3e112dd99c7071cb71.jpg)

![](images/9c406cfda13a930a26a56f7ffdc84c15bca03c1624783cb0a0791acad34d15aa.jpg)

### Images:
- data\Design and Analysis of Algorithms\L05-basic-structures\page_034\L05-basic-structures_page_034\auto\images\028b83d8584dba7c1efeff5c0371b7782b3ea988fd7c9c66e9d5553d5e72d45a.jpg
- data\Design and Analysis of Algorithms\L05-basic-structures\page_034\L05-basic-structures_page_034\auto\images\6a4bd267a979b28cc52159a2c533050d006d5509cd6fbf3e112dd99c7071cb71.jpg
- data\Design and Analysis of Algorithms\L05-basic-structures\page_034\L05-basic-structures_page_034\auto\images\9c406cfda13a930a26a56f7ffdc84c15bca03c1624783cb0a0791acad34d15aa.jpg

---

## Lecture: L05-basic-structures\page_035\L05-basic-structures_page_035\auto

# Abstract Data Type (ADT)

• ADT: A mathematical definition of objects, with operations defined on them  an ADT specifies what a data structure should do, but not how it does it.

• Key Characteristics of ADTs:

– Encapsulation: ADTs hide internal representations, exposing necessary operations. – Implementation Independent: ADTs can be implemented using different underlying structures. – Operations-Oriented: ADTs define operations, not implementations.

ADT Example - List:   
– collection of elements.   
– Common operations: insert(index, value), delete(index), get(index), size(). – Implementation: Arrays, Linked Lists.

---

## Lecture: L05-basic-structures\page_036\L05-basic-structures_page_036\auto

# Implementing Stacks and Queues with Deque

Stacks ADT with Deques:

<table><tr><td>Stack] Method</td><td>Deque Imp lementation</td></tr><tr><td>sizeO isEmptyO topO push(e) popO</td><td>sizeO isEmptyO 1astO insertLast(e) removeLastO</td></tr></table>

Queues ADT with Deques:

<table><tr><td>Queue Method</td><td>Deque Imp lementation</td></tr><tr><td>sizeO isEmptyO</td><td>sizeO isEmptyO</td></tr><tr><td>frontO</td><td>firstO</td></tr><tr><td>enqueueO dequeueO</td><td>insertLast(e) removeFirstO</td></tr></table>

### Images:
- data\Design and Analysis of Algorithms\L05-basic-structures\page_036\L05-basic-structures_page_036\auto\images\7f21e1147288f41bc9602d803f6fa2fe0ab5b8d56268f6e9d8c5e606e3a5649d.jpg
- data\Design and Analysis of Algorithms\L05-basic-structures\page_036\L05-basic-structures_page_036\auto\images\b6c50906a1ac73be8da945d6388d2efd72b52feb0d810fda90e52de54b7e3f5d.jpg

---

## Lecture: L06-AdvDataStructures\page_001\L06-AdvDataStructures_page_001\auto

# Advanced Data Structures

Binary Search Trees

AVL Trees

Heaps

---

## Lecture: L06-AdvDataStructures\page_002\L06-AdvDataStructures_page_002\auto

Find an element in a sorted array:

1. Divide: Check middle element.

2. Conquer: Recursively search 1 subarray.

3. Combine: Trivial.

---

## Lecture: L06-AdvDataStructures\page_003\L06-AdvDataStructures_page_003\auto

Find an element in a sorted array:

1. Divide: Check middle element.

2. Conquer: Recursively search 1 subarray.

3. Combine: Trivial.

Example: Find 9

3 5 7 8 9 12 15

---

## Lecture: L06-AdvDataStructures\page_004\L06-AdvDataStructures_page_004\auto

Find an element in a sorted array:

1. Divide: Check middle element.

2. Conquer: Recursively search 1 subarray.

3. Combine: Trivial.

Example: Find 9

![](images/8b008d11210b4e5d381dd43f419355293bde08d3da5341ad1cd88c5468883287.jpg)

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures\page_004\L06-AdvDataStructures_page_004\auto\images\8b008d11210b4e5d381dd43f419355293bde08d3da5341ad1cd88c5468883287.jpg

---

## Lecture: L06-AdvDataStructures\page_005\L06-AdvDataStructures_page_005\auto

Find an element in a sorted array:

1. Divide: Check middle element.

2. Conquer: Recursively search 1 subarray.

3. Combine: Trivial.

Example: Find 9

![](images/83dc56e0abbcd5ee6948605c78dcd2ad0b5275558b281a1f795f8518a3ba1cd6.jpg)

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures\page_005\L06-AdvDataStructures_page_005\auto\images\83dc56e0abbcd5ee6948605c78dcd2ad0b5275558b281a1f795f8518a3ba1cd6.jpg

---

## Lecture: L06-AdvDataStructures\page_006\L06-AdvDataStructures_page_006\auto

Find an element in a sorted array:

1. Divide: Check middle element.

2. Conquer: Recursively search 1 subarray.

3. Combine: Trivial.

Example: Find 9

![](images/0d7367cda561e8fc1c7942f046489fffd741981d6f97da4e490ddd3c96936f7c.jpg)

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures\page_006\L06-AdvDataStructures_page_006\auto\images\0d7367cda561e8fc1c7942f046489fffd741981d6f97da4e490ddd3c96936f7c.jpg

---

## Lecture: L06-AdvDataStructures\page_007\L06-AdvDataStructures_page_007\auto

Find an element in a sorted array:

1. Divide: Check middle element.

2. Conquer: Recursively search 1 subarray.

3. Combine: Trivial.

Example: Find 9

![](images/f37d824c35a9ca5b542edfb6dc03f048dd43f0305b4244e89b0107d8607fd2b5.jpg)

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures\page_007\L06-AdvDataStructures_page_007\auto\images\f37d824c35a9ca5b542edfb6dc03f048dd43f0305b4244e89b0107d8607fd2b5.jpg

---

## Lecture: L06-AdvDataStructures\page_008\L06-AdvDataStructures_page_008\auto

Find an element in a sorted array:

1. Divide: Check middle element.

2. Conquer: Recursively search 1 subarray.

3. Combine: Trivial.

Example: Find 9

![](images/111308e47286bb50e2c30c58744755b4cb745dfcc7c3d3d0b2c3898adbf5c35e.jpg)

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures\page_008\L06-AdvDataStructures_page_008\auto\images\111308e47286bb50e2c30c58744755b4cb745dfcc7c3d3d0b2c3898adbf5c35e.jpg

---

## Lecture: L06-AdvDataStructures\page_009\L06-AdvDataStructures_page_009\auto

Sorted Array:

![](images/7b4d03ade77d8d75264a5a0963aad4887d5be49de7d02eb9dd573989c4210876.jpg)

Linked list (not necessarily sorted):

![](images/c3242cf152437c8da67d512c6e75f3643509e6854c294a4a9e799d1a29781f43.jpg)

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures\page_009\L06-AdvDataStructures_page_009\auto\images\7b4d03ade77d8d75264a5a0963aad4887d5be49de7d02eb9dd573989c4210876.jpg
- data\Design and Analysis of Algorithms\L06-AdvDataStructures\page_009\L06-AdvDataStructures_page_009\auto\images\c3242cf152437c8da67d512c6e75f3643509e6854c294a4a9e799d1a29781f43.jpg

---

## Lecture: L06-AdvDataStructures\page_010\L06-AdvDataStructures_page_010\auto

• ????(????) INSERT/DELETE:

– First, find the relevant element (we’ll see how below), and then move a bunch elements in the array:

![](images/bfd9aaa79fd62dcbff8cf42c5641d186ef11067614c66f1f2ffc75ddac93c3e9.jpg)

• ????(log(????)) SEARCH (if sorted):

![](images/5e64be1e210c1fda7be11b61893b3eed5bc4878c0179e45e17b0397eaf5a5396.jpg)

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures\page_010\L06-AdvDataStructures_page_010\auto\images\5e64be1e210c1fda7be11b61893b3eed5bc4878c0179e45e17b0397eaf5a5396.jpg
- data\Design and Analysis of Algorithms\L06-AdvDataStructures\page_010\L06-AdvDataStructures_page_010\auto\images\bfd9aaa79fd62dcbff8cf42c5641d186ef11067614c66f1f2ffc75ddac93c3e9.jpg

---

## Lecture: L06-AdvDataStructures\page_011\L06-AdvDataStructures_page_011\auto

# Linked Lists

• ????(1) INSERT (manipulating pointers)

![](images/017820a1feea2e2a49518c97714c2b21a173531966867246775a79578c76a91c.jpg)

• ????(????) SEARCH/DELETE:

![](images/ed1d284435129fa969651cec68f905a03ee02b8a61866bed4b91798479f981c4.jpg)

eg, search for 3 (and then you could delete it by manipulating pointers).

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures\page_011\L06-AdvDataStructures_page_011\auto\images\017820a1feea2e2a49518c97714c2b21a173531966867246775a79578c76a91c.jpg
- data\Design and Analysis of Algorithms\L06-AdvDataStructures\page_011\L06-AdvDataStructures_page_011\auto\images\ed1d284435129fa969651cec68f905a03ee02b8a61866bed4b91798479f981c4.jpg

---

## Lecture: L06-AdvDataStructures\page_012\L06-AdvDataStructures_page_012\auto

# Binary Search Tree

<table><tr><td rowspan=1 colspan=1>Arrays</td><td rowspan=1 colspan=1>Linked Lists</td><td rowspan=1 colspan=1>(Balanced)Binary SearchTrees</td></tr><tr><td rowspan=1 colspan=1>Search</td><td rowspan=1 colspan=1>0(n)(0(log n) if sorted)</td><td rowspan=1 colspan=1>0(n)</td><td rowspan=1 colspan=1>0 (log n)</td></tr><tr><td rowspan=1 colspan=1>Delete</td><td rowspan=1 colspan=1>0(n)</td><td rowspan=1 colspan=1>0(n)</td><td rowspan=1 colspan=1>0 (log n)</td></tr><tr><td rowspan=1 colspan=1>Insert</td><td rowspan=1 colspan=1>0(n)</td><td rowspan=1 colspan=1>0(1)</td><td rowspan=1 colspan=1>0 (logn)</td></tr></table>

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures\page_012\L06-AdvDataStructures_page_012\auto\images\90ea12f75692f0c093a10264bd1abd0739f5df7cfd757a5b6f83e76d62113c7b.jpg

---

## Lecture: L06-AdvDataStructures\page_013\L06-AdvDataStructures_page_013\auto

# Binary Tree Terminology

Every node stores a distinct element as its key and has at most two children.

![](images/da1ff8e67b41d589b4470932ba69c09a902ef52f7a8259fc3f20ddb2873cbde9.jpg)

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures\page_013\L06-AdvDataStructures_page_013\auto\images\da1ff8e67b41d589b4470932ba69c09a902ef52f7a8259fc3f20ddb2873cbde9.jpg

---

## Lecture: L06-AdvDataStructures\page_014\L06-AdvDataStructures_page_014\auto

# Example 1: HKUST(GZ)

![](images/bf1520ad67ae89b84bfbb8f1db69846839a69ef7e5af027ad181b29e97c66939.jpg)

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures\page_014\L06-AdvDataStructures_page_014\auto\images\bf1520ad67ae89b84bfbb8f1db69846839a69ef7e5af027ad181b29e97c66939.jpg

---

## Lecture: L06-AdvDataStructures\page_015\L06-AdvDataStructures_page_015\auto

# Example 2: File System

• In each directory, we can create new directories or files.

![](images/c27fda141949346398f066e343e2d1d847e660d5b4fb0526917de32447317a26.jpg)

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures\page_015\L06-AdvDataStructures_page_015\auto\images\c27fda141949346398f066e343e2d1d847e660d5b4fb0526917de32447317a26.jpg

---

## Lecture: L06-AdvDataStructures\page_016\L06-AdvDataStructures_page_016\auto

# Binary Search Tree

• A binary search tree (BST) on a set ???? of $n$ integers is a binary tree ???? satisfying all the following requirements:

– Each node ???? in $T$ stores a distinct integer in ????, which is called the key of ????.

– (Order Property) For every internal $u$ , it holds that:

• The key of $u$ is larger than all the keys in the left subtree of $u$ .

• sThe key of $u$ is smaller than all the keys in the right subtree of $u$

3

4

5

8

1

7

2

---

## Lecture: L06-AdvDataStructures\page_017\L06-AdvDataStructures_page_017\auto

# Binary Search Tree

• A BST is a binary tree so that:

– Every LEFT descendant of a node has key less than that node.   
– Every RIGHT descendant of a node has key larger than that node.

3

4

5

8

7

1

2

---

## Lecture: L06-AdvDataStructures\page_018\L06-AdvDataStructures_page_018\auto

# Binary Search Tree

• A BST is a binary tree so that:

– Every LEFT descendant of a node has key less than that node.   
– Every RIGHT descendant of a node has key larger than that node.

3

5

1

2

4

7

8

---

## Lecture: L06-AdvDataStructures\page_019\L06-AdvDataStructures_page_019\auto

# Binary Search Tree

• A BST is a binary tree so that:

– Every LEFT descendant of a node has key less than that node.   
– Every RIGHT descendant of a node has key larger than that node.

![](images/899044682b9cf602ad50f4495156a2fd55c74d9c89bc384a25aaf02edd45893a.jpg)

8

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures\page_019\L06-AdvDataStructures_page_019\auto\images\899044682b9cf602ad50f4495156a2fd55c74d9c89bc384a25aaf02edd45893a.jpg

---

## Lecture: L06-AdvDataStructures\page_020\L06-AdvDataStructures_page_020\auto

# Binary Search Tree

• A BST is a binary tree so that:

– Every LEFT descendant of a node has key less than that node.   
– Every RIGHT descendant of a node has key larger than that node.

![](images/8976a312a2eff590766767ff27d68c55cb3ce44131317d15798c0c79538471b2.jpg)

Q: Is this the only binary search tree I could possibly build with these values?

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures\page_020\L06-AdvDataStructures_page_020\auto\images\8976a312a2eff590766767ff27d68c55cb3ce44131317d15798c0c79538471b2.jpg

---

## Lecture: L06-AdvDataStructures\page_021\L06-AdvDataStructures_page_021\auto

# Traversal

• Output all the elements in sorted order!

• inOrderTraversal(x): – if $x ! = N ! L$ : • inOrderTraversal( x.left ) • print( x.key ) • inOrderTraversal( x.right )

Pre-order / post-order traversal?

![](images/5a89bee321751a4fd9364f00bbe934954f82346d8716b776a5b0034ea75cf794.jpg)

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures\page_021\L06-AdvDataStructures_page_021\auto\images\5a89bee321751a4fd9364f00bbe934954f82346d8716b776a5b0034ea75cf794.jpg

---

## Lecture: L06-AdvDataStructures\page_022\L06-AdvDataStructures_page_022\auto

# Search

![](images/1cde370b81d958a09b808f4acb35a35039eefeb3f898529aca485fe2f1ccb4d6.jpg)

1

EXAMPLE: Search for 4.

# EXAMPLE: Search for 4.5

• It turns out it will be convenient to return 4 in this case (that is, return the last node before we went off the tree)

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures\page_022\L06-AdvDataStructures_page_022\auto\images\1cde370b81d958a09b808f4acb35a35039eefeb3f898529aca485fe2f1ccb4d6.jpg

---

## Lecture: L06-AdvDataStructures\page_023\L06-AdvDataStructures_page_023\auto

![](images/bf037d7e242a8e211456f3714b37fcf4418621c112c3ab5f4208a821f15e12dd.jpg)

# EXAMPLE: Insert 4.5

• INSERT(key):

$\mathsf { X } = \mathsf { S E A R C H } ( \mathsf { k e y } )$ Insert a new node with desired key at x…

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures\page_023\L06-AdvDataStructures_page_023\auto\images\bf037d7e242a8e211456f3714b37fcf4418621c112c3ab5f4208a821f15e12dd.jpg

---

## Lecture: L06-AdvDataStructures\page_024\L06-AdvDataStructures_page_024\auto

# Insert

![](images/5fd6976b7ce6044f609a3ea1cf4c89a7d85329323674379ec237f5a238c31120.jpg)

# EXAMPLE: Insert 4.5

INSERT(key):

$\mathsf { X } = \mathsf { S E A R C H } ( \mathsf { k e y } )$

if key $>$ x.key:

Make a new node with the correct key, and put it as the right child of x

if key < x.key:

Make a new node with the correct key, and put it as the left child of $\pmb { \mathsf { X } }$

• if x.key $= =$ key: return

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures\page_024\L06-AdvDataStructures_page_024\auto\images\5fd6976b7ce6044f609a3ea1cf4c89a7d85329323674379ec237f5a238c31120.jpg

---

## Lecture: L06-AdvDataStructures\page_025\L06-AdvDataStructures_page_025\auto

![](images/15c21e37aeb067157e0cc99b39c54281bfd61085ca22b66a9701876e2277fb36.jpg)

1

# EXAMPLE: Delete 2

# DELETE(key):

${ \sf x } = \sf { S E A R C H } ( { \sf k e y } )$ if $\mathsf { x } . \mathsf { k e y } = \mathsf { = k e y }$ : ….delete x….

![](images/2208a7a3a82f194779dc1efe2c7475b0b646e63e2db3facaaf37d8199853d41e.jpg)

This is a bit more complicated…

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures\page_025\L06-AdvDataStructures_page_025\auto\images\15c21e37aeb067157e0cc99b39c54281bfd61085ca22b66a9701876e2277fb36.jpg
- data\Design and Analysis of Algorithms\L06-AdvDataStructures\page_025\L06-AdvDataStructures_page_025\auto\images\2208a7a3a82f194779dc1efe2c7475b0b646e63e2db3facaaf37d8199853d41e.jpg

---

## Lecture: L06-AdvDataStructures\page_026\L06-AdvDataStructures_page_026\auto

![](images/0a1a0e5b9172d86aa9e0f0a93a4cc8edca4c752c971681a3a6415388de5fd14f.jpg)

Case 1: if 3 is a leaf, just delete it.

![](images/feeca750106d95ecebf85487e84d8924ad39e172a5d33a426a9ae3b73c59d8e1.jpg)

Case 2: if 3 has just one child, move that up.

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures\page_026\L06-AdvDataStructures_page_026\auto\images\0a1a0e5b9172d86aa9e0f0a93a4cc8edca4c752c971681a3a6415388de5fd14f.jpg
- data\Design and Analysis of Algorithms\L06-AdvDataStructures\page_026\L06-AdvDataStructures_page_026\auto\images\feeca750106d95ecebf85487e84d8924ad39e172a5d33a426a9ae3b73c59d8e1.jpg

---

## Lecture: L06-AdvDataStructures\page_027\L06-AdvDataStructures_page_027\auto

Case 3: if 3 has two children, replace 3 with it’s immediate successor. (aka, next biggest thing after 3)

![](images/54fc62e00cadb7473e33962b48a0a44be4fc692b52a8bb22f38d79dc4cc35703.jpg)

• Does this maintain the BST property? ● Yes

• How do we find the immediate successor? • SEARCH for 3 in the subtree under 3.right

• How do we remove it when we find it? • If [3.1] has 0 or 1 children, do one of the previous cases • What if [3.1] has two children? • It doesn’t

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures\page_027\L06-AdvDataStructures_page_027\auto\images\54fc62e00cadb7473e33962b48a0a44be4fc692b52a8bb22f38d79dc4cc35703.jpg

---

## Lecture: L06-AdvDataStructures\page_028\L06-AdvDataStructures_page_028\auto

# More Operations

• findmin(x): finds the minimum of the tree rooted at x

• findmax(x): finds the max of the tree rooted at x

• deletemin(): finds the minimum of the tree and delete it

Time complexities of them?

---

## Lecture: L06-AdvDataStructures\page_029\L06-AdvDataStructures_page_029\auto

# The Importance of Being Balanced

• This is a valid binary search tree

• The version with n nodes has depth ????, not Θ(log(????))

![](images/a0e92003ab844008abde7a93b77a80e5ce7caa92284af84530d46953ac778a98.jpg)

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures\page_029\L06-AdvDataStructures_page_029\auto\images\a0e92003ab844008abde7a93b77a80e5ce7caa92284af84530d46953ac778a98.jpg

---

## Lecture: L06-AdvDataStructures\page_030\L06-AdvDataStructures_page_030\auto

# Balanced BST Strategy

• Augment every node with some property   
• Define a local invariant on property   
• Show (prove) that invariant guarantees Θ log ???? height • Design algorithms to maintain property and the invariant

---

## Lecture: L06-AdvDataStructures\page_031\L06-AdvDataStructures_page_031\auto

# AVL Trees

---

## Lecture: L06-AdvDataStructures\page_032\L06-AdvDataStructures_page_032\auto

An AVL (Adelson-Velskii and Landis) tree is a binary search tree that also meets the following rule

AVL condition: For every node, the height of its left subtree and right subtree differ by at most 1.

Height of a tree: Maximum number of edges on a path from the root to a leaf.

A tree with one node has height 0.   
A null tree (no nodes) has height -1.

---

## Lecture: L06-AdvDataStructures\page_033\L06-AdvDataStructures_page_033\auto

# Which one(s) is balanced according to AVL’s definition?

![](images/a3fbaff4018b5f1ef1f4a4ba540328aa8eb3158bd1eab2b8def71430d5380341.jpg)

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures\page_033\L06-AdvDataStructures_page_033\auto\images\a3fbaff4018b5f1ef1f4a4ba540328aa8eb3158bd1eab2b8def71430d5380341.jpg

---

## Lecture: L06-AdvDataStructures\page_034\L06-AdvDataStructures_page_034\auto

An AVL tree is a binary search tree that also meets the following rule

AVL condition: For every node, the height of its left subtree and right subtree differ by at most 1.

This will avoid the Θ ???? behavior! We have to check:

1. We must be able to maintain this property when inserting/deleting.   
2. Such a tree must have height Θ(log ????) .

---

## Lecture: L06-AdvDataStructures\page_035\L06-AdvDataStructures_page_035\auto

# Bounding the Height

• Let $n ( h )$ be the minimum number of nodes in an AVL tree of height ℎ.

• If we can say $n ( h )$ is big, we’ll be able to say that a tree with ???? nodes has a small height.

• So…what’s $n ( h ) !$

$$
n ( h ) = \left\{ { 2 \atop { n ( h - 1 ) + n ( h - 2 ) + 1 , \mathrm { ~ o t h e } } } \right. \nonumber
$$

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures\page_035\L06-AdvDataStructures_page_035\auto\images\0c1bfd5770772c216664fe874968aa670631fcd31a31ae9d4111c746675cba3b.jpg

---

## Lecture: L06-AdvDataStructures\page_036\L06-AdvDataStructures_page_036\auto

# Bounding the Height

• Hey! That’s a recurrence!

• Recurrences can describe any kind of function, not just running time of code!

$$
n ( h ) = { \left\{ \begin{array} { l l } { 1 , } & { { \mathrm { i f ~ } } h = 0 } \\ { 2 , } & { { \mathrm { i f ~ } } h = 1 } \\ { n ( h - 1 ) + n ( h - 2 ) + 1 , } & { { \mathrm { o t h e r w i s e } } } \end{array} \right. }
$$

• We could use tree method, but it’s a little…weird.

• It’ll be easier if we change things just a bit:

$$
n ( h ) \geq { \left\{ \begin{array} { l l } { 1 , } & { { \mathrm { i f ~ } } h = 0 } \\ { 2 , } & { { \mathrm { i f ~ } } h = 1 } \\ { n ( h - 2 ) + n ( h - 2 ) + 1 , } & { { \mathrm { o t h e r w i s e } } } \end{array} \right. }
$$

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures\page_036\L06-AdvDataStructures_page_036\auto\images\0d7c830fa5504b31223f27cf17f30b95dd61c535a454e409693fa56a6a0b69c6.jpg
- data\Design and Analysis of Algorithms\L06-AdvDataStructures\page_036\L06-AdvDataStructures_page_036\auto\images\22385313a56fbd2b6a18ee2b6bbb93b2ac76e6286029c2bb591770823778c964.jpg

---

## Lecture: L06-AdvDataStructures\page_037\L06-AdvDataStructures_page_037\auto

# Bounding the Height

$$
\begin{array} { c } { { n ( h ) = n ( h - 1 ) + n ( h - 2 ) + 1 } } \\ { { > 2 n ( h - 2 ) } } \\ { { > 2 \times 2 n ( h - 4 ) } } \\ { { > 2 \frac { h } { 2 } } } \end{array}
$$

$$
h < 2 \log n ( h )
$$

Hence, $h = \Theta ( \log n )$ .

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures\page_037\L06-AdvDataStructures_page_037\auto\images\14b61292b60db337b31d0cce1d5eda3ad67e22eb2ec90b7f18a3af177f68f8b1.jpg
- data\Design and Analysis of Algorithms\L06-AdvDataStructures\page_037\L06-AdvDataStructures_page_037\auto\images\a7c437cd3a166f315622ebbbb196435375a78a6c242b0ac63f4fc78250004f8b.jpg

---

## Lecture: L06-AdvDataStructures\page_038\L06-AdvDataStructures_page_038\auto

# What happens if when we the AVL condition is violated after insertion?

![](images/fd00e2d8212bf45ccc356d5f435b28072341cf61f8ef12fd50930f1a2194d007.jpg)

Balanced

Imbalanced

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures\page_038\L06-AdvDataStructures_page_038\auto\images\fd00e2d8212bf45ccc356d5f435b28072341cf61f8ef12fd50930f1a2194d007.jpg

---

## Lecture: L06-AdvDataStructures\page_039\L06-AdvDataStructures_page_039\auto

# Insertion

Rotations!

![](images/965cc7ad52e0e3ba5cc8c7bb86c0fcca959cdeac38eecaa3b2cd5583e496a3b7.jpg)

Rotations can reduce the height!

![](images/1eb74b75fe97631bf24a275c52307a88e5cdffa19fbfe8b2e5d642248fe3e0fb.jpg)

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures\page_039\L06-AdvDataStructures_page_039\auto\images\1eb74b75fe97631bf24a275c52307a88e5cdffa19fbfe8b2e5d642248fe3e0fb.jpg
- data\Design and Analysis of Algorithms\L06-AdvDataStructures\page_039\L06-AdvDataStructures_page_039\auto\images\965cc7ad52e0e3ba5cc8c7bb86c0fcca959cdeac38eecaa3b2cd5583e496a3b7.jpg

---

## Lecture: L06-AdvDataStructures\page_040\L06-AdvDataStructures_page_040\auto

# Insertion / Deletion

• Insert new node u as in the simple BST • Can create imbalance   
• Work your way up the tree, restoring the balance   
• Similar issue/solution when deleting a node

![](images/4ac4a7ffb9aa7011e54a6be9ebc899e83af9899383c2c9fad9a364efc9fc59fe.jpg)

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures\page_040\L06-AdvDataStructures_page_040\auto\images\4ac4a7ffb9aa7011e54a6be9ebc899e83af9899383c2c9fad9a364efc9fc59fe.jpg

---

## Lecture: L06-AdvDataStructures\page_041\L06-AdvDataStructures_page_041\auto

# Balancing

• Let x be the lowest “violating” node we will try to correct that and move up the tree

• Assume that x is “right-heavy” • we analyze more the right subtree of x • y is the right child of x

• Scenarios

• Case 1: y is right-heavy / balanced • Case 2: y is left-heavy

The right child of x has $+ 2$ height than the left child of x

![](images/ed2f7442eab18b87420d4cf7dfb907715cd38481a1873ab66b5b05266449b652.jpg)

![](images/9e19d079a7128ad6b774f6d8a45f325d6b7c4506b79b49d494b3b4f77f0cab18.jpg)

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures\page_041\L06-AdvDataStructures_page_041\auto\images\9e19d079a7128ad6b774f6d8a45f325d6b7c4506b79b49d494b3b4f77f0cab18.jpg
- data\Design and Analysis of Algorithms\L06-AdvDataStructures\page_041\L06-AdvDataStructures_page_041\auto\images\ed2f7442eab18b87420d4cf7dfb907715cd38481a1873ab66b5b05266449b652.jpg

---

## Lecture: L06-AdvDataStructures\page_042\L06-AdvDataStructures_page_042\auto

# Case 1.1: y is right-heavy

![](images/a9741be8d974639b49a1c9582afafd7adc6190ea25177441573e382e03a0b2a1.jpg)

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures\page_042\L06-AdvDataStructures_page_042\auto\images\a9741be8d974639b49a1c9582afafd7adc6190ea25177441573e382e03a0b2a1.jpg

---

## Lecture: L06-AdvDataStructures\page_043\L06-AdvDataStructures_page_043\auto

Case 1.2: y is balanced

![](images/bb610e94cfc854b6507ea0cc917337e6dc8462a0bc4bef61ef079d037bafc716.jpg)

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures\page_043\L06-AdvDataStructures_page_043\auto\images\bb610e94cfc854b6507ea0cc917337e6dc8462a0bc4bef61ef079d037bafc716.jpg

---

## Lecture: L06-AdvDataStructures\page_044\L06-AdvDataStructures_page_044\auto

# Case 2: y is left-heavy

![](images/f7805debb2b64f332bc18008f42d027daeed8cf15441da79b9b9509e8aa8ae66.jpg)

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures\page_044\L06-AdvDataStructures_page_044\auto\images\f7805debb2b64f332bc18008f42d027daeed8cf15441da79b9b9509e8aa8ae66.jpg

---

## Lecture: L06-AdvDataStructures\page_045\L06-AdvDataStructures_page_045\auto

![](images/0b63b0b7738febcada91c8eca2de494824f434830e069238d21e738e25a5feb5.jpg)  
Case 2: y is left-heavy

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures\page_045\L06-AdvDataStructures_page_045\auto\images\0b63b0b7738febcada91c8eca2de494824f434830e069238d21e738e25a5feb5.jpg

---

## Lecture: L06-AdvDataStructures\page_046\L06-AdvDataStructures_page_046\auto

# Case 2: y is left-heavy

![](images/6c1d15416f7384beb2d310edc189547fc40e47feb9fe7139ddda1c373d028dfa.jpg)

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures\page_046\L06-AdvDataStructures_page_046\auto\images\6c1d15416f7384beb2d310edc189547fc40e47feb9fe7139ddda1c373d028dfa.jpg

---

## Lecture: L06-AdvDataStructures\page_047\L06-AdvDataStructures_page_047\auto

Case 2: y is left-heavy

![](images/1d9a88a378e36650fbaf33af327570e726f93b6bc1706bdb8875b9f345468911.jpg)

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures\page_047\L06-AdvDataStructures_page_047\auto\images\1d9a88a378e36650fbaf33af327570e726f93b6bc1706bdb8875b9f345468911.jpg

---

## Lecture: L06-AdvDataStructures\page_048\L06-AdvDataStructures_page_048\auto

# Four Types of Rotations

To summarize

![](images/a1760e6940e10550952d5e3f7554334d23e07b369732ed2aef58fc07132c534e.jpg)

<table><tr><td rowspan=1 colspan=1>Insert location</td><td rowspan=1 colspan=1>Solution</td></tr><tr><td rowspan=1 colspan=1>Left subtree of leftchild (A)</td><td rowspan=1 colspan=1> Single right rotation</td></tr><tr><td rowspan=1 colspan=1>Right subtree ofleft child (B)</td><td rowspan=1 colspan=1>Double (left-right) rotation</td></tr><tr><td rowspan=1 colspan=1>Left subtree ofright child (C)</td><td rowspan=2 colspan=1>Double (right-left) rotationSingle left rotation</td></tr><tr><td rowspan=1 colspan=1>Right subtree ofright child(D)</td></tr></table>

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures\page_048\L06-AdvDataStructures_page_048\auto\images\a1760e6940e10550952d5e3f7554334d23e07b369732ed2aef58fc07132c534e.jpg
- data\Design and Analysis of Algorithms\L06-AdvDataStructures\page_048\L06-AdvDataStructures_page_048\auto\images\e2d6c52b51fbe285879925f89448d84fb7b378253f6e7eccf7d2bfe18f6007ec.jpg

---

## Lecture: L06-AdvDataStructures\page_049\L06-AdvDataStructures_page_049\auto

# Other Self-Balancing Trees

• “Red-black trees” work on a similar principle to AVL trees.

• “Splay trees”: Get ????(log ????) amortized bounds for all operations.

• “Scapegoat trees”: worst case O(Log n) search complexity. Others are same as splay trees.

• “Treaps” – a BST and heap in one (!)

Similar tradeoffs to AVL trees.

---

## Lecture: L06-AdvDataStructures\page_050\L06-AdvDataStructures_page_050\auto

• An important observation: The root can be switched from red to black without violating any rule.

• Add 0 as a red node.

• Flip the colors of its parent and uncle.

• Pass the red to the top.

![](images/19a3822cbe7615e648a314c3a23b9d860ad0130071f9cde9dd57a4c98872e688.jpg)

• Flip the color of the root from red to black.

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures\page_050\L06-AdvDataStructures_page_050\auto\images\19a3822cbe7615e648a314c3a23b9d860ad0130071f9cde9dd57a4c98872e688.jpg

---

## Lecture: L06-AdvDataStructures\page_051\L06-AdvDataStructures_page_051\auto

(Binary) Heaps

---

## Lecture: L06-AdvDataStructures\page_052\L06-AdvDataStructures_page_052\auto

# Revisiting FindMin

• Application: Find the smallest (or highest priority) item quickly

Operating system needs to schedule jobs according to priority instead of FIFO

Event simulation (bank customers arriving and departing, ordered according to when the event happened)

– Find student with highest grade, employee with highest salary etc.

---

## Lecture: L06-AdvDataStructures\page_053\L06-AdvDataStructures_page_053\auto

# Priority Queue ADT

• Priority Queue can efficiently do:

– FindMin (and DeleteMin) – Insert

What if we use…

– Lists: If sorted, what is the run time for Insert and FindMin? Unsorted? Binary Search Trees: What is the run time for Insert and FindMin? Hash Tables (Maybe next lecture): What is the run time for Insert and FindMin?

---

## Lecture: L06-AdvDataStructures\page_054\L06-AdvDataStructures_page_054\auto

# Less Flexibility More Speed

# Lists

– If sorted: FindMin is O(1) but Insert is O(N) – If not sorted: Insert is O(1) but FindMin is O(N)

Balanced Binary Search Trees (BSTs) – Insert is O(log N) and FindMin is O(log N)

• BSTs look good but… BSTs are efficient for all Finds, not just FindMin We only need FindMin

---

## Lecture: L06-AdvDataStructures\page_055\L06-AdvDataStructures_page_055\auto

# Better than a speeding BST

• Can we do better than Balanced Binary Search Trees? – Very limited requirements: Insert, FindMin, DeleteMin – The goals are:

FindMin is $O ( 1 )$

• Insert is ${ \cal O } ( \log N )$

• DeleteMin is ${ \cal O } ( \log N )$

---

## Lecture: L06-AdvDataStructures\page_056\L06-AdvDataStructures_page_056\auto

# Binary Heaps

• A binary heap is a binary tree (NOT a BST) that is:

Complete: the tree is completely filled except possibly the bottom level, which is filled from left to right

Satisfies the heap order property

every node is less than or equal to its children (MinHeap, the default)

or every node is greater than or equal to its children (for MaxHeap)

• The root node is always the smallest node

or the largest, depending on the heap order (for MaxHeap)

---

## Lecture: L06-AdvDataStructures\page_057\L06-AdvDataStructures_page_057\auto

# Heap order property

• A heap provides limited ordering information   
• Each path is sorted, but the subtrees are not sorted relative to each other – A binary heap is NOT a binary search tree

![](images/1dd742166e4159606b2dc5a3b77d1fe4c9286e82bf87ef43e9abeb2aabdee36c.jpg)

![](images/f36221696dea11c3ef70c55a8ca11932ce2e7b60611a0857c5fe350bcf71e782.jpg)

![](images/0ac609f7d0346dadf126854fd05e71f93290fa893e95b472da12d8c0d7c2c5f6.jpg)

These are all valid binary min heaps

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures\page_057\L06-AdvDataStructures_page_057\auto\images\0ac609f7d0346dadf126854fd05e71f93290fa893e95b472da12d8c0d7c2c5f6.jpg
- data\Design and Analysis of Algorithms\L06-AdvDataStructures\page_057\L06-AdvDataStructures_page_057\auto\images\1dd742166e4159606b2dc5a3b77d1fe4c9286e82bf87ef43e9abeb2aabdee36c.jpg
- data\Design and Analysis of Algorithms\L06-AdvDataStructures\page_057\L06-AdvDataStructures_page_057\auto\images\f36221696dea11c3ef70c55a8ca11932ce2e7b60611a0857c5fe350bcf71e782.jpg

---

## Lecture: L06-AdvDataStructures\page_058\L06-AdvDataStructures_page_058\auto

# Binary Heap vs Binary Search Tree

Binary Heap

Binary Search Tree

![](images/b00525cabf705a6479f1dcec26a6464ad16ccdea7d7a50a9a3afcbc7ff6c7b10.jpg)

![](images/059659cadd56d56988352c8e1a10ae67b745a40a06cdfac0515509e77e4eff61.jpg)

Parent is less than both left and right children

Parent is greater than left child, less than right child

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures\page_058\L06-AdvDataStructures_page_058\auto\images\059659cadd56d56988352c8e1a10ae67b745a40a06cdfac0515509e77e4eff61.jpg
- data\Design and Analysis of Algorithms\L06-AdvDataStructures\page_058\L06-AdvDataStructures_page_058\auto\images\b00525cabf705a6479f1dcec26a6464ad16ccdea7d7a50a9a3afcbc7ff6c7b10.jpg

---

## Lecture: L06-AdvDataStructures\page_059\L06-AdvDataStructures_page_059\auto

# Structure Property

• A binary heap is a complete tree – All nodes are in use except for possibly the right end of the bottom row

![](images/e9c19337544a3880c286549e82d543001b03f9f530a6a2a1f4b629366e3d3ca6.jpg)

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures\page_059\L06-AdvDataStructures_page_059\auto\images\e9c19337544a3880c286549e82d543001b03f9f530a6a2a1f4b629366e3d3ca6.jpg

---

## Lecture: L06-AdvDataStructures\page_060\L06-AdvDataStructures_page_060\auto

![](images/b53f188e105c5375bf77c2be9370b1a4c77f91d07f21a86d0ecbc95859e2c4eb.jpg)

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures\page_060\L06-AdvDataStructures_page_060\auto\images\b53f188e105c5375bf77c2be9370b1a4c77f91d07f21a86d0ecbc95859e2c4eb.jpg

---

## Lecture: L06-AdvDataStructures\page_061\L06-AdvDataStructures_page_061\auto

# Array Implementation (Implicit Pointers)

• Root node $=$ A[1]   
• Children of $\mathsf { A } [ \mathsf { i } ] = \mathsf { A } [ 2 \mathsf { i } ] , \mathsf { A } [ 2 \mathsf { i } + 1 ]$   
• Parent of $\mathsf { A } [ \mathrm { j } ] = \mathsf { A } [ \mathrm { j } / 2 ]$   
• Keep track of current size $N$ (number of nodes)

![](images/65833db2059e2c8715881b178867cc8154f298687058427d72e9c0eee4cb38e3.jpg)

![](images/39d080ee0594e33f71417f5facfffed852b932fc139ecde9d62c1b93ea378bd1.jpg)

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures\page_061\L06-AdvDataStructures_page_061\auto\images\39d080ee0594e33f71417f5facfffed852b932fc139ecde9d62c1b93ea378bd1.jpg
- data\Design and Analysis of Algorithms\L06-AdvDataStructures\page_061\L06-AdvDataStructures_page_061\auto\images\65833db2059e2c8715881b178867cc8154f298687058427d72e9c0eee4cb38e3.jpg

---

## Lecture: L06-AdvDataStructures\page_062\L06-AdvDataStructures_page_062\auto

# FindMin and DeleteMin

• FindMin: Easy! – Return root value A[1] – Run time = ?

• DeleteMin: – Delete (and return) value at root node?

![](images/56c3f3a9103c8afa8d2454980787762080c48d175894da20a569da85762b14a7.jpg)

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures\page_062\L06-AdvDataStructures_page_062\auto\images\56c3f3a9103c8afa8d2454980787762080c48d175894da20a569da85762b14a7.jpg

---

## Lecture: L06-AdvDataStructures\page_063\L06-AdvDataStructures_page_063\auto

# Maintain the Structure Property

• Delete (and return) value at root node

![](images/bd8713cd6f64e77c818bbe7261a904fa6175c779f5e587bf42e9b3fa4d878227.jpg)

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures\page_063\L06-AdvDataStructures_page_063\auto\images\bd8713cd6f64e77c818bbe7261a904fa6175c779f5e587bf42e9b3fa4d878227.jpg

---

## Lecture: L06-AdvDataStructures\page_064\L06-AdvDataStructures_page_064\auto

# Maintain the Structure Property

• We now have a “Hole” at the root

• Need to fill the hole with another value

• When we get done, the tree will have one less node and must still be complete

![](images/644a98660875a5528cd94c36650c4cbf18062a34774d6651e5c4b4a751af2136.jpg)

![](images/64e072a423c737b21091bf53b6817fa295c2463758f5573632eb8f443bfb8ced.jpg)

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures\page_064\L06-AdvDataStructures_page_064\auto\images\644a98660875a5528cd94c36650c4cbf18062a34774d6651e5c4b4a751af2136.jpg
- data\Design and Analysis of Algorithms\L06-AdvDataStructures\page_064\L06-AdvDataStructures_page_064\auto\images\64e072a423c737b21091bf53b6817fa295c2463758f5573632eb8f443bfb8ced.jpg

---

## Lecture: L06-AdvDataStructures\page_065\L06-AdvDataStructures_page_065\auto

# Maintain the Heap Property

• The last value has lost its node

• we need to find a new place for it

![](images/8529b4e3c7d69a888cfc0bf25629f6d75c8c9e93f4e62fc3e4d7f4ce46820a94.jpg)

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures\page_065\L06-AdvDataStructures_page_065\auto\images\8529b4e3c7d69a888cfc0bf25629f6d75c8c9e93f4e62fc3e4d7f4ce46820a94.jpg

---

## Lecture: L06-AdvDataStructures\page_066\L06-AdvDataStructures_page_066\auto

# DeleteMin: Percolate Down

![](images/48cfe252f1da6ff9505be5606794a2c3add78421cee7af11ed93c4b517bccd8d.jpg)

• Keep comparing with children A[2i] and A[2i + 1]

• Copy smaller child up and go down one level

• Done if both children are $\geq$ item or reached a leaf node

• What is the run time?

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures\page_066\L06-AdvDataStructures_page_066\auto\images\48cfe252f1da6ff9505be5606794a2c3add78421cee7af11ed93c4b517bccd8d.jpg

---

## Lecture: L06-AdvDataStructures\page_067\L06-AdvDataStructures_page_067\auto

# Percolate Down

PercDown(i: integer, x: integer): { // N is the number elements, i is the hole, x is the value to insert Case { No child $\begin{array} { r l } & { \tt N : ~ \mathbb { A } [ i ] \gamma : = \gamma _ \alpha : } \\ & { \tt N : ~ i f \mathbb { A } [ 2 i ] < x \epsilon ~ t h e n ~ \mathbb { A } [ i ] : = \mathbb { A } [ 2 i ] : \mathbb { A } [ 2 i ] } \\ & { \tt e l s e ~ \mathbb { A } [ i ] \gamma : = \mathbb { x } } \\ & { \tt N : ~ i f \mathbb { A } [ 2 i ] < \mathbb { A } [ 2 i + 1 ] ~ t h e n ~ j ~ : = 2 i } \\ & { \tt e l s e ~ j ~ : = 2 i + 1 } \\ & { \tt ~ i f \mathbb { A } [ j ] < x \epsilon ~ t h e n ~ } \end{array}$ One child at the end := x Two Children $\mathbb { A } \left[ \dot { \mathrm {  ~ i ~ } } \right] : = \mathrm {  ~ \mathbb { A } \left[ \dot { \mathrm {  ~ j ~ } } \right] ~ } \mathfrak { p e r c o w n } \left( \dot { \mathrm {  ~ j ~ } } , \mathrm {  ~ \ x ~ } \right) ;$ $\begin{array} { r } { \mathsf { e l s e ~ A } [ \dot { \mathrm {  ~ i ~ } } ] : = \mathrm { ~  ~ x ~ } } \end{array}$

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures\page_067\L06-AdvDataStructures_page_067\auto\images\22bedd5c11f7c9ca6d7073991d2eefce72d0110b1abbb4e22f819d8d159ca4fc.jpg
- data\Design and Analysis of Algorithms\L06-AdvDataStructures\page_067\L06-AdvDataStructures_page_067\auto\images\334c3c69e8b437e9c59cd3e4311a9d5a250ad2f8563c5db5b83267f74544dc97.jpg
- data\Design and Analysis of Algorithms\L06-AdvDataStructures\page_067\L06-AdvDataStructures_page_067\auto\images\407b3d6c513a1342c621faa58b1559530d5c25854caa437b4a819b5bbe9297e6.jpg

---

## Lecture: L06-AdvDataStructures\page_068\L06-AdvDataStructures_page_068\auto

# DeleteMin: Run Time Analysis

• Run time is ????(?????????????????? ???????? ℎ????????????)

• A heap is a complete binary tree

• Depth of a complete binary tree of N nodes? – depth = log(????)

• Run time of DeleteMin is ????(log ????)

---

## Lecture: L06-AdvDataStructures\page_069\L06-AdvDataStructures_page_069\auto

# Insert

• Add a value to the tree • Structure and heap order properties must still be correct when we are done

![](images/6dafd1ddc54425918e3120ffb5b968d6bdf93337496adc1d3214fd631207fe9f.jpg)

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures\page_069\L06-AdvDataStructures_page_069\auto\images\6dafd1ddc54425918e3120ffb5b968d6bdf93337496adc1d3214fd631207fe9f.jpg

---

## Lecture: L06-AdvDataStructures\page_070\L06-AdvDataStructures_page_070\auto

# Maintain the Structure Property

• The only valid place for a new node in a complete tree is at the end of the array

• We need to decide on the correct value for the new node, and adjust the heap accordingly

![](images/7aea10b5a24ce881abfef1bd89152bd6c5bc0eee8d9cb80e77304207857a2eee.jpg)

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures\page_070\L06-AdvDataStructures_page_070\auto\images\7aea10b5a24ce881abfef1bd89152bd6c5bc0eee8d9cb80e77304207857a2eee.jpg

---

## Lecture: L06-AdvDataStructures\page_071\L06-AdvDataStructures_page_071\auto

# Maintain the Heap Property

• The new value goes where?

![](images/5708d00549b8c5df81270e036f8dc9b6db9b23600194c29862ec9b412e0041c3.jpg)

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures\page_071\L06-AdvDataStructures_page_071\auto\images\5708d00549b8c5df81270e036f8dc9b6db9b23600194c29862ec9b412e0041c3.jpg

---

## Lecture: L06-AdvDataStructures\page_072\L06-AdvDataStructures_page_072\auto

# Insert: Percolate Up

![](images/3b2f4a57dfd5ff8afd29271a8878257f2106cc2fabe3c3be6ad3f1bbd4dbdeb2.jpg)

• Start at last node and keep comparing with parent A[i/2]

• If parent larger, copy parent down and go up one level

• Done if parent ≤ item or reached top node A[1]

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures\page_072\L06-AdvDataStructures_page_072\auto\images\3b2f4a57dfd5ff8afd29271a8878257f2106cc2fabe3c3be6ad3f1bbd4dbdeb2.jpg

---

## Lecture: L06-AdvDataStructures\page_073\L06-AdvDataStructures_page_073\auto

![](images/b732f4feb51d1b7f10b6bbd3d69d0640f1497be93db851a76f07d4a786459e1d.jpg)

• Run time?

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures\page_073\L06-AdvDataStructures_page_073\auto\images\b732f4feb51d1b7f10b6bbd3d69d0640f1497be93db851a76f07d4a786459e1d.jpg

---

## Lecture: L06-AdvDataStructures\page_074\L06-AdvDataStructures_page_074\auto

# Binary Heap Analysis

• Space needed for heap of N nodes: O(MaxN) – An array of size MaxN, plus a variable to store the size N

• Time

– FindMin: O(1) – DeleteMin and Insert: O(log N) – BuildHeap from N inputs ???

---

## Lecture: L06-AdvDataStructures\page_075\L06-AdvDataStructures_page_075\auto

BuildHeap { for i = N/2 to 1 PercDown(i, A[i])   
}

![](images/d925aa5c446b148962d01613f6b95616c330a9e21f976a122c4b98182a647608.jpg)

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures\page_075\L06-AdvDataStructures_page_075\auto\images\d925aa5c446b148962d01613f6b95616c330a9e21f976a122c4b98182a647608.jpg

---

## Lecture: L06-AdvDataStructures\page_076\L06-AdvDataStructures_page_076\auto

![](images/80aeb5c5a927cfc13be48d0462c3d3fa0cacdb58b6ab7303868969c8c90845f4.jpg)

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures\page_076\L06-AdvDataStructures_page_076\auto\images\80aeb5c5a927cfc13be48d0462c3d3fa0cacdb58b6ab7303868969c8c90845f4.jpg

---

## Lecture: L06-AdvDataStructures\page_077\L06-AdvDataStructures_page_077\auto

![](images/07b8bc0958c962acbaabe8a9a30097f288f86ce6bc58186b7a819efbb6706be4.jpg)

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures\page_077\L06-AdvDataStructures_page_077\auto\images\07b8bc0958c962acbaabe8a9a30097f288f86ce6bc58186b7a819efbb6706be4.jpg

---

## Lecture: L06-AdvDataStructures\page_078\L06-AdvDataStructures_page_078\auto

# Time Complexity

Naïve considerations:

– ????/2 calls to PercDown, each takes ???? ⋅ log(????) – Total: ???? ⋅ ???? ⋅ log(????)

• More careful considerations: – Only $O ( n )$

---

## Lecture: L06-AdvDataStructures\page_079\L06-AdvDataStructures_page_079\auto

# Analysis of Build Heap

Assume $n ~ = ~ 2 ^ { h + 1 } - 1$ where h is height of the tree

– Thus, level $h$ has $2 ^ { h }$ nodes but there is nothing to PercDown – At level $h - 1$ there are $2 ^ { h - 1 }$ nodes, each might percolate down 1 level – At level $h - j ,$ there are $2 ^ { h - j }$ nodes, each might percolate down ???? levels

$$
T ( n ) = \sum _ { j = 0 } ^ { h } j 2 ^ { h - j } = \sum _ { j = 0 } ^ { h } j { \frac { 2 ^ { h } } { 2 ^ { j } } }
$$

Total Time $\mathbf { \Omega } = O ( n )$

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures\page_079\L06-AdvDataStructures_page_079\auto\images\02bc9d00fc375555ff96f94674dff5bedf4e4ef174918f8e2c98b69c7fb334b6.jpg

---

## Lecture: L06-AdvDataStructures\page_080\L06-AdvDataStructures_page_080\auto

# Other Heap Operations

Find(X, H): Find the element X in heap H of $N$ elements – What is the running time? $O ( N )$

• FindMax(H): Find the maximum element in H

• Where FindMin is ????(1) – What is the running time? $O ( N )$

• We sacrificed performance of these operations in order to get $\cdot$ performance for FindMin

---

## Lecture: L06-AdvDataStructures\page_081\L06-AdvDataStructures_page_081\auto

# Other Heap Operations

• DecreaseKey(P,Δ,H): Decrease the key value of node at position P by a positive amount $\Delta$ , e.g., to increase priority

– First, subtract $\Delta$ from current value at P – Heap order property may be violated – so percolate up to fix   
– Running Time: ${ \cal O } ( \log N )$

---

## Lecture: L06-AdvDataStructures\page_082\L06-AdvDataStructures_page_082\auto

# Other Heap Operations

• Delete(P,H): E.g. Delete a job waiting in queue that has been preemptively terminated by user

– Use DecreaseKey(P, Δ,H) followed by DeleteMin – Running Time: ${ \cal O } ( \log N )$

Merge(H1,H2): Merge two heaps H1 and H2 of size $O ( N )$ . H1 and H2 are stored in two arrays.

– Can do $O ( N )$ Insert operations: ${ \cal O } ( N \log N )$ time Better: Copy H2 at the end of H1 and use BuildHeap. Running Time: $O ( N )$

---

## Lecture: L06-AdvDataStructures\page_083\L06-AdvDataStructures_page_083\auto

# Other Heap Operations

• Merge(H1,H2): Merge two heaps H1 and H2 of size ????(????). H1 and H2 are stored in two arrays.

– Can do $O ( N )$ Insert operations: ${ \cal O } ( N \log N )$ time Better: Copy H2 at the end of H1 and use BuildHeap. Running Time: $O ( N )$

---

## Lecture: L06-AdvDataStructures\page_084\L06-AdvDataStructures_page_084\auto

# Heap Sort

• Idea: buildHeap then call deleteMin n times

input $=$ buildHeap(...);   
output $=$ new E[n];   
for (int $\mathsf { i } = 0 ; \mathsf { i } < \mathsf { n } ; \mathsf { i } + + \mathsf { f } \left\{ \begin{array} { r l } \end{array} \right.$ output[i] $=$ deleteMin(input);   
}

• Runtime?

• Best-case • Worst-case • Average-case • Stable?

• In-place?

---

## Lecture: L06-AdvDataStructures\page_085\L06-AdvDataStructures_page_085\auto

# Heap Sort

• Idea: buildHeap then call deleteMin ???? times

input $=$ buildHeap(...);   
output $=$ new E[n];   
for (int $\mathsf { i } = 0 ; \mathsf { i } < \mathsf { n } ; \mathsf { i } + + \mathsf { f } \left\{ \begin{array} { r l } \end{array} \right.$ output[i] $=$ deleteMin(input);   
}

• Runtime?

• Best-case, Worst-case, and Average-case: $O ( n \log ( n ) )$

• Stable? No.

• In-place? No. But it could be, with a slight trick...

---

## Lecture: L06-AdvDataStructures\page_086\L06-AdvDataStructures_page_086\auto

# In-place Heap Sort

• Treat the initial array as a heap (via buildHeap)

But this reverse sorts – how would you fix that?

• When you delete the ith element, put it at arr[n-i] • That array location isn’t needed for the heap anymore!

![](images/827d8f57e5dcee344b261d32192965a21abde5679b520571bd0cfcbbcfd6302c.jpg)

put the min at the end of the heap data

![](images/9294ebeec28cc5832ef4be0012bab968f214a21bcb12240156127773a418c4c1.jpg)

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures\page_086\L06-AdvDataStructures_page_086\auto\images\827d8f57e5dcee344b261d32192965a21abde5679b520571bd0cfcbbcfd6302c.jpg
- data\Design and Analysis of Algorithms\L06-AdvDataStructures\page_086\L06-AdvDataStructures_page_086\auto\images\9294ebeec28cc5832ef4be0012bab968f214a21bcb12240156127773a418c4c1.jpg

---

## Lecture: L06-AdvDataStructures\page_087\L06-AdvDataStructures_page_087\auto

Sure, we can also use an AVL tree to:

• Insert each element: total time $O ( n \mathrm { l o g } n )$

• Repeatedly deleteMin: total time $O ( n \log n )$ – Better: in-order traversal $O ( n )$ , but still $O ( n \log n )$ overall

• But this cannot be done in-place and has worse constant factors than heap sort

---

## Lecture: L06-AdvDataStructures_revised\page_001\L06-AdvDataStructures_revised_page_001\auto

# Advanced Data Structures

Binary Search Trees

AVL Trees

Heaps

---

## Lecture: L06-AdvDataStructures_revised\page_002\L06-AdvDataStructures_revised_page_002\auto

Find an element in a sorted array:

1. Divide: Check middle element.

2. Conquer: Recursively search 1 subarray.

3. Combine: Trivial.

---

## Lecture: L06-AdvDataStructures_revised\page_003\L06-AdvDataStructures_revised_page_003\auto

Find an element in a sorted array:

1. Divide: Check middle element.

2. Conquer: Recursively search $1$ subarray.

3. Combine: Trivial.

Example: Find 9

3 5 7 8 9 12 15

---

## Lecture: L06-AdvDataStructures_revised\page_004\L06-AdvDataStructures_revised_page_004\auto

Find an element in a sorted array:

1. Divide: Check middle element.

2. Conquer: Recursively search 1 subarray.

3. Combine: Trivial.

Example: Find 9

![](images/49f25867c9da611254dcbdf7c5b289aea7b06bfbdbd1982019ec13578c2dd3d7.jpg)

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures_revised\page_004\L06-AdvDataStructures_revised_page_004\auto\images\49f25867c9da611254dcbdf7c5b289aea7b06bfbdbd1982019ec13578c2dd3d7.jpg

---

## Lecture: L06-AdvDataStructures_revised\page_005\L06-AdvDataStructures_revised_page_005\auto

Find an element in a sorted array:

1. Divide: Check middle element.

2. Conquer: Recursively search $1$ subarray.

3. Combine: Trivial.

Example: Find 9

![](images/d6f29bb7e3b4937cb67115924ddc142d902b57e3912f7ed0289d8c3a99424061.jpg)

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures_revised\page_005\L06-AdvDataStructures_revised_page_005\auto\images\d6f29bb7e3b4937cb67115924ddc142d902b57e3912f7ed0289d8c3a99424061.jpg

---

## Lecture: L06-AdvDataStructures_revised\page_006\L06-AdvDataStructures_revised_page_006\auto

Find an element in a sorted array:

1. Divide: Check middle element.

2. Conquer: Recursively search $^ 1$ subarray.

3. Combine: Trivial.

Example: Find 9

![](images/09e2a7d87a721af1f619bd757caf75d4dcdbe55ee83bd1c3a110a3ff97f910a8.jpg)

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures_revised\page_006\L06-AdvDataStructures_revised_page_006\auto\images\09e2a7d87a721af1f619bd757caf75d4dcdbe55ee83bd1c3a110a3ff97f910a8.jpg

---

## Lecture: L06-AdvDataStructures_revised\page_007\L06-AdvDataStructures_revised_page_007\auto

Find an element in a sorted array:

1. Divide: Check middle element.

2. Conquer: Recursively search $1$ subarray.

3. Combine: Trivial.

Example: Find 9

![](images/c98f3fc31cf546762b969525789bf6c2b5cf1579f4e35ac7690eba67b794f7e8.jpg)

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures_revised\page_007\L06-AdvDataStructures_revised_page_007\auto\images\c98f3fc31cf546762b969525789bf6c2b5cf1579f4e35ac7690eba67b794f7e8.jpg

---

## Lecture: L06-AdvDataStructures_revised\page_008\L06-AdvDataStructures_revised_page_008\auto

Find an element in a sorted array:

1. Divide: Check middle element.

2. Conquer: Recursively search $^ 1$ subarray.

3. Combine: Trivial.

Example: Find 9

![](images/12af515e6d5b571718c73502b800ca0c34c36e251b0885103592376191a972c3.jpg)

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures_revised\page_008\L06-AdvDataStructures_revised_page_008\auto\images\12af515e6d5b571718c73502b800ca0c34c36e251b0885103592376191a972c3.jpg

---

## Lecture: L06-AdvDataStructures_revised\page_009\L06-AdvDataStructures_revised_page_009\auto

Sorted Array:

![](images/7b4d03ade77d8d75264a5a0963aad4887d5be49de7d02eb9dd573989c4210876.jpg)

Linked list (not necessarily sorted):

![](images/c3242cf152437c8da67d512c6e75f3643509e6854c294a4a9e799d1a29781f43.jpg)

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures_revised\page_009\L06-AdvDataStructures_revised_page_009\auto\images\7b4d03ade77d8d75264a5a0963aad4887d5be49de7d02eb9dd573989c4210876.jpg
- data\Design and Analysis of Algorithms\L06-AdvDataStructures_revised\page_009\L06-AdvDataStructures_revised_page_009\auto\images\c3242cf152437c8da67d512c6e75f3643509e6854c294a4a9e799d1a29781f43.jpg

---

## Lecture: L06-AdvDataStructures_revised\page_010\L06-AdvDataStructures_revised_page_010\auto

• ????(????) INSERT/DELETE:

– First, find the relevant element (we’ll see how below), and then move a bunch elements in the array:

![](images/45db4690bb70003440d6245826b55c697cc258efc3d434bf51c1069a8db0d862.jpg)

• ????(log(????)) SEARCH (if sorted):

![](images/cc56476e18be9876b6c39b9845f1838c303a6dddbdf59f0e89ae5cca7cdb6b53.jpg)

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures_revised\page_010\L06-AdvDataStructures_revised_page_010\auto\images\45db4690bb70003440d6245826b55c697cc258efc3d434bf51c1069a8db0d862.jpg
- data\Design and Analysis of Algorithms\L06-AdvDataStructures_revised\page_010\L06-AdvDataStructures_revised_page_010\auto\images\cc56476e18be9876b6c39b9845f1838c303a6dddbdf59f0e89ae5cca7cdb6b53.jpg

---

## Lecture: L06-AdvDataStructures_revised\page_011\L06-AdvDataStructures_revised_page_011\auto

# Linked Lists

• ????(1) INSERT (manipulating pointers)

![](images/017820a1feea2e2a49518c97714c2b21a173531966867246775a79578c76a91c.jpg)

• ????(????) SEARCH/DELETE:

![](images/ed1d284435129fa969651cec68f905a03ee02b8a61866bed4b91798479f981c4.jpg)

eg, search for 3 (and then you could delete it by manipulating pointers).

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures_revised\page_011\L06-AdvDataStructures_revised_page_011\auto\images\017820a1feea2e2a49518c97714c2b21a173531966867246775a79578c76a91c.jpg
- data\Design and Analysis of Algorithms\L06-AdvDataStructures_revised\page_011\L06-AdvDataStructures_revised_page_011\auto\images\ed1d284435129fa969651cec68f905a03ee02b8a61866bed4b91798479f981c4.jpg

---

## Lecture: L06-AdvDataStructures_revised\page_012\L06-AdvDataStructures_revised_page_012\auto

# Binary Search Tree

<table><tr><td rowspan=1 colspan=1>Arrays</td><td rowspan=1 colspan=1>Linked Lists</td><td rowspan=1 colspan=1>(Balanced)Binary SearchTrees</td></tr><tr><td rowspan=1 colspan=1>Search</td><td rowspan=1 colspan=1>0(n)(0(log n) if sorted)</td><td rowspan=1 colspan=1>0(n)</td><td rowspan=1 colspan=1>0 (log n)</td></tr><tr><td rowspan=1 colspan=1>Delete</td><td rowspan=1 colspan=1>0(n)</td><td rowspan=1 colspan=1>0(n)</td><td rowspan=1 colspan=1>0 (log n)</td></tr><tr><td rowspan=1 colspan=1>Insert</td><td rowspan=1 colspan=1>0(n)</td><td rowspan=1 colspan=1>0(1)</td><td rowspan=1 colspan=1>0 (logn)</td></tr></table>

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures_revised\page_012\L06-AdvDataStructures_revised_page_012\auto\images\90ea12f75692f0c093a10264bd1abd0739f5df7cfd757a5b6f83e76d62113c7b.jpg

---

## Lecture: L06-AdvDataStructures_revised\page_013\L06-AdvDataStructures_revised_page_013\auto

# Binary Tree Terminology

Every node stores a distinct element as its key and has at most two children.

![](images/eeb686e4eeb5bc22b090bd8dab3e706e1187d5e3a40edbd356da0f5b40177ca3.jpg)

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures_revised\page_013\L06-AdvDataStructures_revised_page_013\auto\images\eeb686e4eeb5bc22b090bd8dab3e706e1187d5e3a40edbd356da0f5b40177ca3.jpg

---

## Lecture: L06-AdvDataStructures_revised\page_014\L06-AdvDataStructures_revised_page_014\auto

# Example 1: HKUST(GZ)

![](images/a241ce14bfcbb9b6c01c1d1be19b8f4a65b743dd74f918432b4a457fbf1114bf.jpg)

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures_revised\page_014\L06-AdvDataStructures_revised_page_014\auto\images\a241ce14bfcbb9b6c01c1d1be19b8f4a65b743dd74f918432b4a457fbf1114bf.jpg

---

## Lecture: L06-AdvDataStructures_revised\page_015\L06-AdvDataStructures_revised_page_015\auto

# Example 2: File System

• In each directory, we can create new directories or files.

![](images/c27fda141949346398f066e343e2d1d847e660d5b4fb0526917de32447317a26.jpg)

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures_revised\page_015\L06-AdvDataStructures_revised_page_015\auto\images\c27fda141949346398f066e343e2d1d847e660d5b4fb0526917de32447317a26.jpg

---

## Lecture: L06-AdvDataStructures_revised\page_016\L06-AdvDataStructures_revised_page_016\auto

# Binary Search Tree

• A binary search tree (BST) on a set ???? of $n$ integers is a binary tree ???? satisfying all the following requirements:

– Each node ???? in $T$ stores a distinct integer in ????, which is called the key of ????.

– (Order Property) For every internal $u$ , it holds that:

• The key of $u$ is larger than all the keys in the left subtree of $u$ .

• The key of $u$ is smaller than all the keys in the right subtree of $u$

3

4

5

8

1

7

2

---

## Lecture: L06-AdvDataStructures_revised\page_017\L06-AdvDataStructures_revised_page_017\auto

# Binary Search Tree

• A BST is a binary tree so that:

– Every LEFT descendant of a node has key less than that node.   
– Every RIGHT descendant of a node has key larger than that node.

3

4

5

8

7

1

2

---

## Lecture: L06-AdvDataStructures_revised\page_018\L06-AdvDataStructures_revised_page_018\auto

# Binary Search Tree

• A BST is a binary tree so that:

– Every LEFT descendant of a node has key less than that node.   
– Every RIGHT descendant of a node has key larger than that node.

3

5

1

2

4

7

8

---

## Lecture: L06-AdvDataStructures_revised\page_019\L06-AdvDataStructures_revised_page_019\auto

# Binary Search Tree

• A BST is a binary tree so that:

– Every LEFT descendant of a node has key less than that node.   
– Every RIGHT descendant of a node has key larger than that node.

![](images/e7ae6c758882d65bdfd30c98acbec21f279273f108e5bb337382daa828b4c404.jpg)

8

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures_revised\page_019\L06-AdvDataStructures_revised_page_019\auto\images\e7ae6c758882d65bdfd30c98acbec21f279273f108e5bb337382daa828b4c404.jpg

---

## Lecture: L06-AdvDataStructures_revised\page_020\L06-AdvDataStructures_revised_page_020\auto

# Binary Search Tree

• A BST is a binary tree so that:

– Every LEFT descendant of a node has key less than that node.   
– Every RIGHT descendant of a node has key larger than that node.

![](images/8976a312a2eff590766767ff27d68c55cb3ce44131317d15798c0c79538471b2.jpg)

Q: Is this the only binary search tree I could possibly build with these values?

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures_revised\page_020\L06-AdvDataStructures_revised_page_020\auto\images\8976a312a2eff590766767ff27d68c55cb3ce44131317d15798c0c79538471b2.jpg

---

## Lecture: L06-AdvDataStructures_revised\page_021\L06-AdvDataStructures_revised_page_021\auto

# Traversal

• Output all the elements in sorted order!

• inOrderTraversal(x): – if $x ! = N ! L$ : • inOrderTraversal( x.left ) • print( x.key ) • inOrderTraversal( x.right )

Pre-order / post-order traversal?

![](images/5a89bee321751a4fd9364f00bbe934954f82346d8716b776a5b0034ea75cf794.jpg)

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures_revised\page_021\L06-AdvDataStructures_revised_page_021\auto\images\5a89bee321751a4fd9364f00bbe934954f82346d8716b776a5b0034ea75cf794.jpg

---

## Lecture: L06-AdvDataStructures_revised\page_022\L06-AdvDataStructures_revised_page_022\auto

# Search

![](images/1cde370b81d958a09b808f4acb35a35039eefeb3f898529aca485fe2f1ccb4d6.jpg)

1

EXAMPLE: Search for 4.

# EXAMPLE: Search for 4.5

• It turns out it will be convenient to return 4 in this case (that is, return the last node before we went off the tree)

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures_revised\page_022\L06-AdvDataStructures_revised_page_022\auto\images\1cde370b81d958a09b808f4acb35a35039eefeb3f898529aca485fe2f1ccb4d6.jpg

---

## Lecture: L06-AdvDataStructures_revised\page_023\L06-AdvDataStructures_revised_page_023\auto

![](images/bf037d7e242a8e211456f3714b37fcf4418621c112c3ab5f4208a821f15e12dd.jpg)

# EXAMPLE: Insert 4.5

• INSERT(key):

$\mathsf { X } = \mathsf { S E A R C H } ( \mathsf { k e y } )$ Insert a new node with desired key at x…

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures_revised\page_023\L06-AdvDataStructures_revised_page_023\auto\images\bf037d7e242a8e211456f3714b37fcf4418621c112c3ab5f4208a821f15e12dd.jpg

---

## Lecture: L06-AdvDataStructures_revised\page_024\L06-AdvDataStructures_revised_page_024\auto

# Insert

![](images/5fd6976b7ce6044f609a3ea1cf4c89a7d85329323674379ec237f5a238c31120.jpg)

# EXAMPLE: Insert 4.5

INSERT(key):

$\mathsf { X } = \mathsf { S E A R C H } ( \mathsf { k e y } )$

if key $>$ x.key:

Make a new node with the correct key, and put it as the right child of x

if key < x.key:

Make a new node with the correct key, and put it as the left child of $\pmb { \mathsf { X } }$

• if x.key $= =$ key: return

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures_revised\page_024\L06-AdvDataStructures_revised_page_024\auto\images\5fd6976b7ce6044f609a3ea1cf4c89a7d85329323674379ec237f5a238c31120.jpg

---

## Lecture: L06-AdvDataStructures_revised\page_025\L06-AdvDataStructures_revised_page_025\auto

![](images/b17bc1bab19e15566cb4ebf3cb9556ff09a261475ed0a00437ce6f4a08db55d4.jpg)

# EXAMPLE: Delete 2

# DELETE(key):

${ \sf x } = \sf { S E A R C H } ( { \sf k e y } )$ if x.key $= =$ key: ….delete x….

1

![](images/cfb275fba3bbf0800f587fa3b91d2f3ec1e25ced5745b0ebf0549260d46238dc.jpg)

This is a bit more complicated…

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures_revised\page_025\L06-AdvDataStructures_revised_page_025\auto\images\b17bc1bab19e15566cb4ebf3cb9556ff09a261475ed0a00437ce6f4a08db55d4.jpg
- data\Design and Analysis of Algorithms\L06-AdvDataStructures_revised\page_025\L06-AdvDataStructures_revised_page_025\auto\images\cfb275fba3bbf0800f587fa3b91d2f3ec1e25ced5745b0ebf0549260d46238dc.jpg

---

## Lecture: L06-AdvDataStructures_revised\page_026\L06-AdvDataStructures_revised_page_026\auto

![](images/0a1a0e5b9172d86aa9e0f0a93a4cc8edca4c752c971681a3a6415388de5fd14f.jpg)

Case 1: if 3 is a leaf, just delete it.

![](images/feeca750106d95ecebf85487e84d8924ad39e172a5d33a426a9ae3b73c59d8e1.jpg)

Case 2: if 3 has just one child, move that up.

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures_revised\page_026\L06-AdvDataStructures_revised_page_026\auto\images\0a1a0e5b9172d86aa9e0f0a93a4cc8edca4c752c971681a3a6415388de5fd14f.jpg
- data\Design and Analysis of Algorithms\L06-AdvDataStructures_revised\page_026\L06-AdvDataStructures_revised_page_026\auto\images\feeca750106d95ecebf85487e84d8924ad39e172a5d33a426a9ae3b73c59d8e1.jpg

---

## Lecture: L06-AdvDataStructures_revised\page_027\L06-AdvDataStructures_revised_page_027\auto

Case 3: if 3 has two children, replace 3 with it’s immediate successor. (aka, next biggest thing after 3)

![](images/54fc62e00cadb7473e33962b48a0a44be4fc692b52a8bb22f38d79dc4cc35703.jpg)

• Does this maintain the BST property? ● Yes

• How do we find the immediate successor? • SEARCH for 3 in the subtree under 3.right

• How do we remove it when we find it? • If [3.1] has 0 or 1 children, do one of the previous cases • What if [3.1] has two children? • It doesn’t

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures_revised\page_027\L06-AdvDataStructures_revised_page_027\auto\images\54fc62e00cadb7473e33962b48a0a44be4fc692b52a8bb22f38d79dc4cc35703.jpg

---

## Lecture: L06-AdvDataStructures_revised\page_028\L06-AdvDataStructures_revised_page_028\auto

# More Operations

• findmin(x): finds the minimum of the tree rooted at x

• findmax(x): finds the max of the tree rooted at x

• deletemin(): finds the minimum of the tree and delete it

Time complexities of them?

---

## Lecture: L06-AdvDataStructures_revised\page_029\L06-AdvDataStructures_revised_page_029\auto

# The Importance of Being Balanced

• This is a valid binary search tree

• The version with n nodes has depth ????, not Θ(log(????))

![](images/a0e92003ab844008abde7a93b77a80e5ce7caa92284af84530d46953ac778a98.jpg)

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures_revised\page_029\L06-AdvDataStructures_revised_page_029\auto\images\a0e92003ab844008abde7a93b77a80e5ce7caa92284af84530d46953ac778a98.jpg

---

## Lecture: L06-AdvDataStructures_revised\page_030\L06-AdvDataStructures_revised_page_030\auto

# Balanced BST Strategy

• Augment every node with some property   
• Define a local invariant on property   
• Show (prove) that invariant guarantees Θ log ???? height • Design algorithms to maintain property and the invariant

---

## Lecture: L06-AdvDataStructures_revised\page_031\L06-AdvDataStructures_revised_page_031\auto

# AVL Trees

---

## Lecture: L06-AdvDataStructures_revised\page_032\L06-AdvDataStructures_revised_page_032\auto

An AVL (Adelson-Velskii and Landis) tree is a binary search tree that also meets the following rule

AVL condition: For every node, the height of its left subtree and right subtree differ by at most 1.

Height of a tree:

Maximum number of edges on a path from the root to a leaf.

A tree with one node has height 0.   
A null tree (no nodes) has height -1.

---

## Lecture: L06-AdvDataStructures_revised\page_033\L06-AdvDataStructures_revised_page_033\auto

# Which one(s) is balanced according to AVL’s definition?

![](images/a3fbaff4018b5f1ef1f4a4ba540328aa8eb3158bd1eab2b8def71430d5380341.jpg)

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures_revised\page_033\L06-AdvDataStructures_revised_page_033\auto\images\a3fbaff4018b5f1ef1f4a4ba540328aa8eb3158bd1eab2b8def71430d5380341.jpg

---

## Lecture: L06-AdvDataStructures_revised\page_034\L06-AdvDataStructures_revised_page_034\auto

An AVL tree is a binary search tree that also meets the following rule

AVL condition: For every node, the height of its left subtree and right subtree differ by at most 1.

This will avoid the Θ ???? behavior! We have to check:

1. We must be able to maintain this property when inserting/deleting.   
2. Such a tree must have height Θ(log ????) .

---

## Lecture: L06-AdvDataStructures_revised\page_035\L06-AdvDataStructures_revised_page_035\auto

# Bounding the Height

• Let $n ( h )$ be the minimum number of nodes in an AVL tree of height ℎ.

• If we can say $n ( h )$ is big, we’ll be able to say that a tree with ???? nodes has a small height.

• So…what’s $n ( h ) !$

$$
n ( h ) = \left\{ { 2 \atop { n ( h - 1 ) + n ( h - 2 ) + 1 , \mathrm { ~ o t h e } } } \right. \nonumber
$$

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures_revised\page_035\L06-AdvDataStructures_revised_page_035\auto\images\0c1bfd5770772c216664fe874968aa670631fcd31a31ae9d4111c746675cba3b.jpg

---

## Lecture: L06-AdvDataStructures_revised\page_036\L06-AdvDataStructures_revised_page_036\auto

# Bounding the Height

• Hey! That’s a recurrence!

• Recurrences can describe any kind of function, not just running time of code!

$$
n ( h ) = { \left\{ \begin{array} { l l } { 1 , } & { { \mathrm { i f ~ } } h = 0 } \\ { 2 , } & { { \mathrm { i f ~ } } h = 1 } \\ { n ( h - 1 ) + n ( h - 2 ) + 1 , } & { { \mathrm { o t h e r w i s e } } } \end{array} \right. }
$$

• We could use tree method, but it’s a little…weird.

• It’ll be easier if we change things just a bit:

$$
n ( h ) \geq { \left\{ \begin{array} { l l } { 1 , } & { { \mathrm { i f ~ } } h = 0 } \\ { 2 , } & { { \mathrm { i f ~ } } h = 1 } \\ { n } & { { \mathrm { ~ + ~ } } n ( h - 2 ) + 1 , } \end{array} \right. }
$$

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures_revised\page_036\L06-AdvDataStructures_revised_page_036\auto\images\80889a7d0c72110698e7dbffca2439201e1859e88e2d235cf4c8ed3ec0982e82.jpg
- data\Design and Analysis of Algorithms\L06-AdvDataStructures_revised\page_036\L06-AdvDataStructures_revised_page_036\auto\images\f8a5fc12361567cd237d90360f2a854bc77b1e3f8f48f02b41e22f1c0b0faa8e.jpg

---

## Lecture: L06-AdvDataStructures_revised\page_037\L06-AdvDataStructures_revised_page_037\auto

# Bounding the Height

$$
\begin{array} { c } { { n ( h ) = n ( h - 1 ) + n ( h - 2 ) + 1 } } \\ { { > 2 n ( h - 2 ) } } \\ { { > 2 \times 2 n ( h - 4 ) } } \\ { { > 2 \frac { h } { 2 } } } \end{array}
$$

$$
h < 2 \log n ( h )
$$

Hence, $h = \Theta ( \log n )$ .

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures_revised\page_037\L06-AdvDataStructures_revised_page_037\auto\images\14b61292b60db337b31d0cce1d5eda3ad67e22eb2ec90b7f18a3af177f68f8b1.jpg
- data\Design and Analysis of Algorithms\L06-AdvDataStructures_revised\page_037\L06-AdvDataStructures_revised_page_037\auto\images\a7c437cd3a166f315622ebbbb196435375a78a6c242b0ac63f4fc78250004f8b.jpg

---

## Lecture: L06-AdvDataStructures_revised\page_038\L06-AdvDataStructures_revised_page_038\auto

# AVL Tree Insertion

• Consider inserting a new integer ???? into an AVL tree ????. First create a new leaf node ???? storing the key ????. Then the insertion can be done via a root-to-leaf path as follows:

• Initialization: Set ????  the root of ????

• If $e <$ the key of ????:

• If $u$ has a left child, set ????  ????. ????????????????_?????????????????? • Otherwise, set ????. ????????????????_??????????????????  ????, and finish

• Otherwise:

• If ???? has a right child, set ????  ????. ??????????????????_?????????????????? • Otherwise, set ????. ??????????????????_??????????????????  ????, and finish

• Repeat the steps above.

• Finally, update the subtree heights on the node of the root-to-leaf path in the bottom-up order. The total cost is proportional to the height of $T$ , i.e., $O ( \log n )$ .

---

## Lecture: L06-AdvDataStructures_revised\page_039\L06-AdvDataStructures_revised_page_039\auto

# What happens if when we the AVL condition is violated after insertion?

![](images/d073e367ff6a6cde411a9ecca99d5aa213f9d7278e7612456e448e84453f4275.jpg)

Balanced

Imbalanced

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures_revised\page_039\L06-AdvDataStructures_revised_page_039\auto\images\d073e367ff6a6cde411a9ecca99d5aa213f9d7278e7612456e448e84453f4275.jpg

---

## Lecture: L06-AdvDataStructures_revised\page_040\L06-AdvDataStructures_revised_page_040\auto

# Insertion

Rotations!

![](images/2c89dd07ecf5f8f8682377177a8b7b5850db0825daa21c3a21ef3ec51c81e8b2.jpg)

Rotations can reduce the height!

![](images/55e4cb06335e760421e19ceea1a73f3caa2ad6598124cc6aaafb85804c070c5a.jpg)

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures_revised\page_040\L06-AdvDataStructures_revised_page_040\auto\images\2c89dd07ecf5f8f8682377177a8b7b5850db0825daa21c3a21ef3ec51c81e8b2.jpg
- data\Design and Analysis of Algorithms\L06-AdvDataStructures_revised\page_040\L06-AdvDataStructures_revised_page_040\auto\images\55e4cb06335e760421e19ceea1a73f3caa2ad6598124cc6aaafb85804c070c5a.jpg

---

## Lecture: L06-AdvDataStructures_revised\page_041\L06-AdvDataStructures_revised_page_041\auto

# Balancing

• We first consider a specific scenario called 2-level imbalance:

• There is a difference of 2 in the heights of the left and right subtrees of $u$ , namely, the balance factor of ???? is 2.

• All the proper descendants of $u$ are balanced.

![](images/7dd095bf48ce4a42e6e45adb1073a51c357adbb64bad8fbd6878a1700c4bf51a.jpg)

• Due to symmetry, it suffices to explain only the right case.

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures_revised\page_041\L06-AdvDataStructures_revised_page_041\auto\images\7dd095bf48ce4a42e6e45adb1073a51c357adbb64bad8fbd6878a1700c4bf51a.jpg

---

## Lecture: L06-AdvDataStructures_revised\page_042\L06-AdvDataStructures_revised_page_042\auto

# Balancing

• Let x be the lowest “violating” node we will try to correct that and move up the tree

• Assume that x is “right-heavy” • we analyze more the right subtree of x • y is the right child of x

• Scenarios

• Case 1: y is right-heavy / balanced • Case 2: y is left-heavy

The right child of x has $+ 2$ height than the left child of x

![](images/86717dd4cbfaa7f97db213d4b740849fc6c4d8f38207f9c16e8c43ecb452e9d9.jpg)

![](images/0c1f3efa22eba79fbede4843b94000119cdad6cabc5c758b4d89b02d2247872d.jpg)

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures_revised\page_042\L06-AdvDataStructures_revised_page_042\auto\images\0c1f3efa22eba79fbede4843b94000119cdad6cabc5c758b4d89b02d2247872d.jpg
- data\Design and Analysis of Algorithms\L06-AdvDataStructures_revised\page_042\L06-AdvDataStructures_revised_page_042\auto\images\86717dd4cbfaa7f97db213d4b740849fc6c4d8f38207f9c16e8c43ecb452e9d9.jpg

---

## Lecture: L06-AdvDataStructures_revised\page_043\L06-AdvDataStructures_revised_page_043\auto

# Case 1.1: y is right-heavy

![](images/0f3f3e3bf4cda18beda641c8decbc0254f21314ea3f42b4d9e5bf70ea0c9b970.jpg)

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures_revised\page_043\L06-AdvDataStructures_revised_page_043\auto\images\0f3f3e3bf4cda18beda641c8decbc0254f21314ea3f42b4d9e5bf70ea0c9b970.jpg

---

## Lecture: L06-AdvDataStructures_revised\page_044\L06-AdvDataStructures_revised_page_044\auto

Case 1.2: y is balanced

![](images/5d6a1f52df2371aa6cfad2d417704fda34410fc8860acd6ea738dc5f5b98bdf3.jpg)

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures_revised\page_044\L06-AdvDataStructures_revised_page_044\auto\images\5d6a1f52df2371aa6cfad2d417704fda34410fc8860acd6ea738dc5f5b98bdf3.jpg

---

## Lecture: L06-AdvDataStructures_revised\page_045\L06-AdvDataStructures_revised_page_045\auto

# Case 2: y is left-heavy

![](images/99a0ed7051b5c90989717e5bd893a6552b47482640e4980a89aba5f3c2482040.jpg)

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures_revised\page_045\L06-AdvDataStructures_revised_page_045\auto\images\99a0ed7051b5c90989717e5bd893a6552b47482640e4980a89aba5f3c2482040.jpg

---

## Lecture: L06-AdvDataStructures_revised\page_046\L06-AdvDataStructures_revised_page_046\auto

![](images/743bfbc63fbe3a2817548ec1c18da2d08c46109b27aaa5826ee0fdc3d95e64f6.jpg)  
Case 2: y is left-heavy

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures_revised\page_046\L06-AdvDataStructures_revised_page_046\auto\images\743bfbc63fbe3a2817548ec1c18da2d08c46109b27aaa5826ee0fdc3d95e64f6.jpg

---

## Lecture: L06-AdvDataStructures_revised\page_047\L06-AdvDataStructures_revised_page_047\auto

# Case 2: y is left-heavy

![](images/8f530b840aefb36982fbb0156c1d5c1065705a76eef54385e4923bc756c19c4a.jpg)

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures_revised\page_047\L06-AdvDataStructures_revised_page_047\auto\images\8f530b840aefb36982fbb0156c1d5c1065705a76eef54385e4923bc756c19c4a.jpg

---

## Lecture: L06-AdvDataStructures_revised\page_048\L06-AdvDataStructures_revised_page_048\auto

Case 2: y is left-heavy

![](images/9c5233462df43c081d0fa6f2a567c3275309b2624d100568aa3f9e99b04abd7d.jpg)

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures_revised\page_048\L06-AdvDataStructures_revised_page_048\auto\images\9c5233462df43c081d0fa6f2a567c3275309b2624d100568aa3f9e99b04abd7d.jpg

---

## Lecture: L06-AdvDataStructures_revised\page_049\L06-AdvDataStructures_revised_page_049\auto

# Four Types of Rotations

To summarize

![](images/0460d4754bcc6797505fd879255c1241921365e0b4ac7252a6e09298effb1a16.jpg)

<table><tr><td rowspan=1 colspan=1>Insert location</td><td rowspan=1 colspan=1>Solution</td></tr><tr><td rowspan=1 colspan=1>Left subtree of leftchild (A)</td><td rowspan=1 colspan=1> Single right rotation</td></tr><tr><td rowspan=1 colspan=1>Right subtree ofleft child (B)</td><td rowspan=1 colspan=1>Double (left-right) rotation</td></tr><tr><td rowspan=1 colspan=1>Left subtree ofright child (C)</td><td rowspan=2 colspan=1>Double (right-left) rotationSingle left rotation</td></tr><tr><td rowspan=1 colspan=1>Right subtree ofright child(D)</td></tr></table>

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures_revised\page_049\L06-AdvDataStructures_revised_page_049\auto\images\0460d4754bcc6797505fd879255c1241921365e0b4ac7252a6e09298effb1a16.jpg
- data\Design and Analysis of Algorithms\L06-AdvDataStructures_revised\page_049\L06-AdvDataStructures_revised_page_049\auto\images\35e06b7a3b65e1f09ac51b1c5375c1fc65b63e224339d0455bdb55b12f712082.jpg

---

## Lecture: L06-AdvDataStructures_revised\page_050\L06-AdvDataStructures_revised_page_050\auto

# Rebalance for AVL Tree Insertion

Insights (left as exercise for you to prove):

• Only the nodes along the path from the insertion path (from the root to the newly added leaf) can become imbalanced.

• Only 2-level imbalance can occur in an insertion.

• It suffices remedy only the lowest imbalanced node. Once it is remedied, all the nodes in the tree will become balance again.

• The total insertion time is therefore $O ( \log n )$ .

![](images/28052249b5500515d25f574bc3d92361fcdcbe8f39851117461477f1f02810de.jpg)

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures_revised\page_050\L06-AdvDataStructures_revised_page_050\auto\images\28052249b5500515d25f574bc3d92361fcdcbe8f39851117461477f1f02810de.jpg

---

## Lecture: L06-AdvDataStructures_revised\page_051\L06-AdvDataStructures_revised_page_051\auto

• Suppose we would like to delete an integer ???? in an AVL tree ????. First, find the node ???? whose key equals ???? in $O ( \log n )$ time (via predecessor search). Then, we would need to consider three possible cases during the deletion process.

• Case 1: Node ???? is a leaf node.   
• Case 2: Node ???? is not a leaf node and has a right subtree.   
• Case 3: Node ???? is not a leaf node and has no right subtree.

---

## Lecture: L06-AdvDataStructures_revised\page_052\L06-AdvDataStructures_revised_page_052\auto

• Case 1: Node ???? is a leaf node.

• Simply remove ???? from the AVL tree ????.

![](images/43c8b09d57946df8deab581fdfeb34c2c781e5dedff0495e9cf9e639d9f46531.jpg)

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures_revised\page_052\L06-AdvDataStructures_revised_page_052\auto\images\43c8b09d57946df8deab581fdfeb34c2c781e5dedff0495e9cf9e639d9f46531.jpg

---

## Lecture: L06-AdvDataStructures_revised\page_053\L06-AdvDataStructures_revised_page_053\auto

• Case 2: Node ???? is not a leaf node, and ???? has a right subtree:

• Find the node ???? storing the successor $s$ of $e$ (Recall the successor definition) Set the key of ???? to ????   
(Case 2.1) If ???? is a leaf node, then remove it from ????.

![](images/516da78504a084c1fda8db5524664afacc2ed8aeb17331d89ff56562b47564af.jpg)

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures_revised\page_053\L06-AdvDataStructures_revised_page_053\auto\images\516da78504a084c1fda8db5524664afacc2ed8aeb17331d89ff56562b47564af.jpg

---

## Lecture: L06-AdvDataStructures_revised\page_054\L06-AdvDataStructures_revised_page_054\auto

• Case 2: Node ???? is not a leaf node, and ???? has a right subtree:

• Find the node ???? storing the successor $s$ of $e$ (Recall the successor definition) • Set the key of ???? to ????

(Case 2.2) If ???? is not a leaf node, it must hold that ???? has a right child ????,

which is a leaf, but not left child ((why? ).

• Set the key of ???? to that of ????;   
• Set the key of ???? to that of $w$ , and remove ???? from ????.

![](images/a0c15a6aae4c1a1c2ed9b34c0ffe1fde63e6d34de08e50a414d4344991502062.jpg)

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures_revised\page_054\L06-AdvDataStructures_revised_page_054\auto\images\a0c15a6aae4c1a1c2ed9b34c0ffe1fde63e6d34de08e50a414d4344991502062.jpg

---

## Lecture: L06-AdvDataStructures_revised\page_055\L06-AdvDataStructures_revised_page_055\auto

# AVL Tree Deletion

• Case 3: Node ???? is not a leaf node, and ???? has no right subtree: ● It must hold that ???? has a left child $v ,$ which is a leaf. (why? • Set the key of ???? to that of $v$ , and remove ???? from ????.

![](images/718e3112a9efc577815918d45d59b287b46f5d00f3f46292fc9ecb889108859d.jpg)

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures_revised\page_055\L06-AdvDataStructures_revised_page_055\auto\images\718e3112a9efc577815918d45d59b287b46f5d00f3f46292fc9ecb889108859d.jpg

---

## Lecture: L06-AdvDataStructures_revised\page_056\L06-AdvDataStructures_revised_page_056\auto

# AVL Tree Deletion

• In all above cases, we have essentially descended a root-to-leaf path (the deletion path), and removed a leaf node.

• We can now update the subtree height values for the nodes on this path in the bottom-up order (similar to which in the insertion process).

• The cost so far is $O ( \log n )$ . Recall that the successor of an integer can be found in $O ( \log n )$ time.

![](images/1b2c0f097ce6f491f4885b62f74f37eb305abae01e2de0925095b7f2b7d2b6dd.jpg)

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures_revised\page_056\L06-AdvDataStructures_revised_page_056\auto\images\1b2c0f097ce6f491f4885b62f74f37eb305abae01e2de0925095b7f2b7d2b6dd.jpg

---

## Lecture: L06-AdvDataStructures_revised\page_057\L06-AdvDataStructures_revised_page_057\auto

# Rebalance for AVL Tree Deletion

• However, after the deletion process, the AVL Tree can be imbalanced as well.

Imbalance!

![](images/1b393432e1824e3a107ee37f77dcd62ab364a6451c49df3b2fd9a3043c44a033.jpg)

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures_revised\page_057\L06-AdvDataStructures_revised_page_057\auto\images\1b393432e1824e3a107ee37f77dcd62ab364a6451c49df3b2fd9a3043c44a033.jpg

---

## Lecture: L06-AdvDataStructures_revised\page_058\L06-AdvDataStructures_revised_page_058\auto

# Rebalance for AVL Tree Deletion

Insight to rebalance for AVL Tree Deletion:

• Only the nodes along the deletion path may become imbalanced.

• Only 2-level imbalance can occur after deletion.

• However, it may require to remedy more than one imbalanced node

---

## Lecture: L06-AdvDataStructures_revised\page_059\L06-AdvDataStructures_revised_page_059\auto

# Rebalance for AVL Tree Deletion: Example

• Delete node 40

![](images/2cefd4b2ab4c5ce80268918fbb189ed40fcfa2ccc207e38e29ebdffbc20c749e.jpg)

• Node 73 becomes imbalanced.

• A left-right case that can be handled by a double rotation.

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures_revised\page_059\L06-AdvDataStructures_revised_page_059\auto\images\2cefd4b2ab4c5ce80268918fbb189ed40fcfa2ccc207e38e29ebdffbc20c749e.jpg

---

## Lecture: L06-AdvDataStructures_revised\page_060\L06-AdvDataStructures_revised_page_060\auto

# Rebalance for AVL Tree Deletion: Example

![](images/64166e6b1c972d08a76825a015e81b6083accf5a156daeb1912afb019a7b1078.jpg)

• After rebalancing node 73, we can notice that node 30 is still imbalanced.

• A left-right case that can be handled by a double rotation.

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures_revised\page_060\L06-AdvDataStructures_revised_page_060\auto\images\64166e6b1c972d08a76825a015e81b6083accf5a156daeb1912afb019a7b1078.jpg

---

## Lecture: L06-AdvDataStructures_revised\page_061\L06-AdvDataStructures_revised_page_061\auto

# Rebalance for AVL Tree Deletion: Example

![](images/71fc6e5a64aa5573a88c2514dd0c72836063b96aa17fccbb8f6ceff59e7b6533.jpg)

• Final tree after the deletion. • Note that this deletion required fixing 2 imbalanced nodes.   
• Since we spend $O ( 1 )$ time fixing each imbalanced nodes, the total deletion time is $O ( \log n )$ .

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures_revised\page_061\L06-AdvDataStructures_revised_page_061\auto\images\71fc6e5a64aa5573a88c2514dd0c72836063b96aa17fccbb8f6ceff59e7b6533.jpg

---

## Lecture: L06-AdvDataStructures_revised\page_062\L06-AdvDataStructures_revised_page_062\auto

# AVL Tree: Complexity

• AVL Tree with n keys provide the following worst-case guarantees:

• Space consumption: • $O ( n )$

• Time complexity:

Search for a key: $O ( \log n )$

• Insertion: $O ( \log n )$

# Animations about AVL trees:

https://www.w3schools.com/dsa/dsa_data_avltrees.php

---

## Lecture: L06-AdvDataStructures_revised\page_063\L06-AdvDataStructures_revised_page_063\auto

# Other Self-Balancing Trees

• “Red-black trees” work on a similar principle to AVL trees.

• “Splay trees”: Get ????(log ????) amortized bounds for all operations.

• “Scapegoat trees”: worst case O(Log n) search complexity. Others are same as splay trees.

• “Treaps” – a BST and heap in one (!)

Similar tradeoffs to AVL trees.

---

## Lecture: L06-AdvDataStructures_revised\page_064\L06-AdvDataStructures_revised_page_064\auto

(Binary) Heaps

---

## Lecture: L06-AdvDataStructures_revised\page_065\L06-AdvDataStructures_revised_page_065\auto

# Revisiting FindMin

• Application: Find the smallest (or highest priority) item quickly

Operating system needs to schedule jobs according to priority instead of FIFO

Event simulation (bank customers arriving and departing, ordered according to when the event happened)

– Find student with highest grade, employee with highest salary etc.

---

## Lecture: L06-AdvDataStructures_revised\page_066\L06-AdvDataStructures_revised_page_066\auto

# Priority Queue ADT

• Priority Queue can efficiently do:

– FindMin (and DeleteMin) – Insert

What if we use…

– Lists: If sorted, what is the run time for Insert and FindMin? Unsorted? Binary Search Trees: What is the run time for Insert and FindMin? Hash Tables (Maybe next lecture): What is the run time for Insert and FindMin?

---

## Lecture: L06-AdvDataStructures_revised\page_067\L06-AdvDataStructures_revised_page_067\auto

# Less Flexibility More Speed

# Lists

– If sorted: FindMin is O(1) but Insert is O(N) – If not sorted: Insert is O(1) but FindMin is O(N)

Balanced Binary Search Trees (BSTs) – Insert is O(log N) and FindMin is O(log N)

• BSTs look good but… BSTs are efficient for all Finds, not just FindMin We only need FindMin

---

## Lecture: L06-AdvDataStructures_revised\page_068\L06-AdvDataStructures_revised_page_068\auto

# Better than a speeding BST

• Can we do better than Balanced Binary Search Trees? – Very limited requirements: Insert, FindMin, DeleteMin – The goals are:

FindMin is $O ( 1 )$

• Insert is ${ \cal O } ( \log N )$

• DeleteMin is ${ \cal O } ( \log N )$

---

## Lecture: L06-AdvDataStructures_revised\page_069\L06-AdvDataStructures_revised_page_069\auto

# Binary Heaps

• A binary heap is a binary tree (NOT a BST) that is:

Complete: the tree is completely filled except possibly the bottom level, which is filled from left to right

Satisfies the heap order property

every node is less than or equal to its children (MinHeap, the default)

or every node is greater than or equal to its children (for MaxHeap)

• The root node is always the smallest node

or the largest, depending on the heap order (for MaxHeap)

---

## Lecture: L06-AdvDataStructures_revised\page_070\L06-AdvDataStructures_revised_page_070\auto

# Heap order property

• A heap provides limited ordering information   
• Each path is sorted, but the subtrees are not sorted relative to each other – A binary heap is NOT a binary search tree

![](images/3058e56d2bcc78365a8084ba911869c3f33bf0f618fcda86348317e6bb7b3e25.jpg)

![](images/b70deaeb0d33a000d8bcfc5f7862d363091d5012bd320b30da9916ddee382d0f.jpg)

![](images/838cb6fee1ba375516cca73ca80baafd7a34cf6daafec739091943a417c5ca4e.jpg)

These are all valid binary min heaps

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures_revised\page_070\L06-AdvDataStructures_revised_page_070\auto\images\3058e56d2bcc78365a8084ba911869c3f33bf0f618fcda86348317e6bb7b3e25.jpg
- data\Design and Analysis of Algorithms\L06-AdvDataStructures_revised\page_070\L06-AdvDataStructures_revised_page_070\auto\images\838cb6fee1ba375516cca73ca80baafd7a34cf6daafec739091943a417c5ca4e.jpg
- data\Design and Analysis of Algorithms\L06-AdvDataStructures_revised\page_070\L06-AdvDataStructures_revised_page_070\auto\images\b70deaeb0d33a000d8bcfc5f7862d363091d5012bd320b30da9916ddee382d0f.jpg

---

## Lecture: L06-AdvDataStructures_revised\page_071\L06-AdvDataStructures_revised_page_071\auto

# Binary Heap vs Binary Search Tree

Binary Heap

Binary Search Tree

![](images/b45eab8dbcbce3e4ecb6e24fecb6cabd0300752f9c1e747951b850ec0aa14587.jpg)

![](images/8c36d4b29285897059227598bc71ead24840d30e28070bf1eb1c291589215c24.jpg)

Parent is less than both left and right children

Parent is greater than left child, less than right child

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures_revised\page_071\L06-AdvDataStructures_revised_page_071\auto\images\8c36d4b29285897059227598bc71ead24840d30e28070bf1eb1c291589215c24.jpg
- data\Design and Analysis of Algorithms\L06-AdvDataStructures_revised\page_071\L06-AdvDataStructures_revised_page_071\auto\images\b45eab8dbcbce3e4ecb6e24fecb6cabd0300752f9c1e747951b850ec0aa14587.jpg

---

## Lecture: L06-AdvDataStructures_revised\page_072\L06-AdvDataStructures_revised_page_072\auto

# Structure Property

• A binary heap is a complete tree – All nodes are in use except for possibly the right end of the bottom row

![](images/acb642e852bea787836498d2d392a8b1aad6cecf87522caa9bff8458a69654be.jpg)

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures_revised\page_072\L06-AdvDataStructures_revised_page_072\auto\images\acb642e852bea787836498d2d392a8b1aad6cecf87522caa9bff8458a69654be.jpg

---

## Lecture: L06-AdvDataStructures_revised\page_073\L06-AdvDataStructures_revised_page_073\auto

![](images/8bc7dad87ba0d7bc335b6746deb1eda0f7a87c211ff6386dad9a0de253ddcafd.jpg)

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures_revised\page_073\L06-AdvDataStructures_revised_page_073\auto\images\8bc7dad87ba0d7bc335b6746deb1eda0f7a87c211ff6386dad9a0de253ddcafd.jpg

---

## Lecture: L06-AdvDataStructures_revised\page_074\L06-AdvDataStructures_revised_page_074\auto

# Array Implementation (Implicit Pointers)

• Root node $=$ A[1]   
• Children of $\mathsf { A } [ \mathsf { i } ] = \mathsf { A } [ 2 \mathsf { i } ] , \mathsf { A } [ 2 \mathsf { i } + 1 ]$   
• Parent of $\mathsf { A } [ \mathrm { j } ] = \mathsf { A } [ \mathrm { j } / 2 ]$   
• Keep track of current size $N$ (number of nodes)

![](images/e6d97987128901f41999431e3f7490fc59ce18cf7a288a18ee54bbb38dff2b06.jpg)

![](images/95522da4fb82b65620ca3f33128b870605316d47c38645e3b20391a1a1549ece.jpg)

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures_revised\page_074\L06-AdvDataStructures_revised_page_074\auto\images\95522da4fb82b65620ca3f33128b870605316d47c38645e3b20391a1a1549ece.jpg
- data\Design and Analysis of Algorithms\L06-AdvDataStructures_revised\page_074\L06-AdvDataStructures_revised_page_074\auto\images\e6d97987128901f41999431e3f7490fc59ce18cf7a288a18ee54bbb38dff2b06.jpg

---

## Lecture: L06-AdvDataStructures_revised\page_075\L06-AdvDataStructures_revised_page_075\auto

# FindMin and DeleteMin

• FindMin: Easy! – Return root value A[1] – Run time = ?

• DeleteMin: – Delete (and return) value at root node?

![](images/05315a4c3445a57b18684071823762bd6d9b98c0a662659096cc917f432830f5.jpg)

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures_revised\page_075\L06-AdvDataStructures_revised_page_075\auto\images\05315a4c3445a57b18684071823762bd6d9b98c0a662659096cc917f432830f5.jpg

---

## Lecture: L06-AdvDataStructures_revised\page_076\L06-AdvDataStructures_revised_page_076\auto

# Maintain the Structure Property

• Delete (and return) value at root node

![](images/37b9488bffe339f4692a8d6df91193859b158cf5b38b8e882cac6428fd63bddd.jpg)

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures_revised\page_076\L06-AdvDataStructures_revised_page_076\auto\images\37b9488bffe339f4692a8d6df91193859b158cf5b38b8e882cac6428fd63bddd.jpg

---

## Lecture: L06-AdvDataStructures_revised\page_077\L06-AdvDataStructures_revised_page_077\auto

# Maintain the Structure Property

• We now have a “Hole” at the root

• Need to fill the hole with another value

• When we get done, the tree will have one less node and must still be complete

![](images/812f6185b1f3d6a756c42f82df38ecd7f45f8fb36b9c7617d4e9b529ec82e9c0.jpg)

![](images/c7441b546873d6df799127d64546cbb8d01bd7e78733ae1a1f895ab887b9ce3e.jpg)

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures_revised\page_077\L06-AdvDataStructures_revised_page_077\auto\images\812f6185b1f3d6a756c42f82df38ecd7f45f8fb36b9c7617d4e9b529ec82e9c0.jpg
- data\Design and Analysis of Algorithms\L06-AdvDataStructures_revised\page_077\L06-AdvDataStructures_revised_page_077\auto\images\c7441b546873d6df799127d64546cbb8d01bd7e78733ae1a1f895ab887b9ce3e.jpg

---

## Lecture: L06-AdvDataStructures_revised\page_078\L06-AdvDataStructures_revised_page_078\auto

# Maintain the Heap Property

• The last value has lost its node

• we need to find a new place for it

![](images/775b6adcffb284fabb6ab6c6317bb859871b50d9b7669a3ce880ad8ceb57b783.jpg)

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures_revised\page_078\L06-AdvDataStructures_revised_page_078\auto\images\775b6adcffb284fabb6ab6c6317bb859871b50d9b7669a3ce880ad8ceb57b783.jpg

---

## Lecture: L06-AdvDataStructures_revised\page_079\L06-AdvDataStructures_revised_page_079\auto

# DeleteMin: Percolate Down

![](images/d5280315ee154fe1a89e1bea0308e1219a96eeddefec8a85fb9e1c5698cde90e.jpg)

• Keep comparing with children A[2i] and A[2i + 1]

• Copy smaller child up and go down one level

• Done if both children are $\geq$ item or reached a leaf node

• What is the run time?

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures_revised\page_079\L06-AdvDataStructures_revised_page_079\auto\images\d5280315ee154fe1a89e1bea0308e1219a96eeddefec8a85fb9e1c5698cde90e.jpg

---

## Lecture: L06-AdvDataStructures_revised\page_080\L06-AdvDataStructures_revised_page_080\auto

# Percolate Down

PercDown(i: integer, x: integer): { // N is the number elements, i is the hole, x is the value to insert Case { No child $\begin{array} { r l } & { \tt N : ~ \mathbb { A } [ i ] \gamma : = \gamma _ \alpha : } \\ & { \tt N : ~ i f \mathbb { A } [ 2 i ] < x \epsilon ~ t h e n ~ \mathbb { A } [ i ] : = \mathbb { A } [ 2 i ] : \mathbb { A } [ 2 i ] } \\ & { \tt e l s e ~ \mathbb { A } [ i ] \gamma : = \mathbb { x } } \\ & { \tt N : ~ i f \mathbb { A } [ 2 i ] < \mathbb { A } [ 2 i + 1 ] ~ t h e n ~ j ~ : = 2 i } \\ & { \tt e l s e ~ j ~ : = 2 i + 1 } \\ & { \tt ~ i f \mathbb { A } [ j ] < x \epsilon ~ t h e n ~ } \end{array}$ One child at the end := x Two Children $\mathbb { A } \left[ \dot { \mathrm {  ~ i ~ } } \right] : = \mathrm {  ~ \mathbb { A } \left[ \dot { \mathrm {  ~ j ~ } } \right] ~ } \mathfrak { p e r c o w n } \left( \dot { \mathrm {  ~ j ~ } } , \mathrm {  ~ \ x ~ } \right) ;$ $\begin{array} { r } { \mathsf { e l s e ~ A } [ \dot { \mathrm {  ~ i ~ } } ] : = \mathrm { ~  ~ x ~ } } \end{array}$

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures_revised\page_080\L06-AdvDataStructures_revised_page_080\auto\images\21df785e49feab093209f0f3966f9eb39411331d58571cfb7ddfef06cca5c266.jpg
- data\Design and Analysis of Algorithms\L06-AdvDataStructures_revised\page_080\L06-AdvDataStructures_revised_page_080\auto\images\e569d6b7eab68489a7580a08f386d1e21000db1ce57f18ff20a9f908f4a8b9fe.jpg
- data\Design and Analysis of Algorithms\L06-AdvDataStructures_revised\page_080\L06-AdvDataStructures_revised_page_080\auto\images\fb78ab90ded00acc1632a723d762f9477cd50eedfa04736314e03b137e525d4b.jpg

---

## Lecture: L06-AdvDataStructures_revised\page_081\L06-AdvDataStructures_revised_page_081\auto

# DeleteMin: Run Time Analysis

• Run time is ????(?????????????????? ???????? ℎ????????????)

• A heap is a complete binary tree

• Depth of a complete binary tree of N nodes? – depth = log(????)

• Run time of DeleteMin is ????(log ????)

---

## Lecture: L06-AdvDataStructures_revised\page_082\L06-AdvDataStructures_revised_page_082\auto

# Insert

• Add a value to the tree • Structure and heap order properties must still be correct when we are done

![](images/49439512a9cf653bb021f46bd938af6ec90a47f486f333f5bb32424f0ddc766d.jpg)

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures_revised\page_082\L06-AdvDataStructures_revised_page_082\auto\images\49439512a9cf653bb021f46bd938af6ec90a47f486f333f5bb32424f0ddc766d.jpg

---

## Lecture: L06-AdvDataStructures_revised\page_083\L06-AdvDataStructures_revised_page_083\auto

# Maintain the Structure Property

• The only valid place for a new node in a complete tree is at the end of the array

• We need to decide on the correct value for the new node, and adjust the heap accordingly

![](images/e688752a067c7bb910758bb187181d1e115c91d413ec62786bd1b951919123b3.jpg)

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures_revised\page_083\L06-AdvDataStructures_revised_page_083\auto\images\e688752a067c7bb910758bb187181d1e115c91d413ec62786bd1b951919123b3.jpg

---

## Lecture: L06-AdvDataStructures_revised\page_084\L06-AdvDataStructures_revised_page_084\auto

# Maintain the Heap Property

• The new value goes where?

![](images/c9a4da05bc3c6e520a82024ee8700d1c35f1412306ea3ac856e21ce252324b54.jpg)

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures_revised\page_084\L06-AdvDataStructures_revised_page_084\auto\images\c9a4da05bc3c6e520a82024ee8700d1c35f1412306ea3ac856e21ce252324b54.jpg

---

## Lecture: L06-AdvDataStructures_revised\page_085\L06-AdvDataStructures_revised_page_085\auto

# Insert: Percolate Up

![](images/37295862ba3a0a1b70cd87373b3c4837b9f84d2610af734b2583e538ccafbf73.jpg)

• Start at last node and keep comparing with parent A[i/2]

• If parent larger, copy parent down and go up one level

• Done if parent ≤ item or reached top node A[1]

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures_revised\page_085\L06-AdvDataStructures_revised_page_085\auto\images\37295862ba3a0a1b70cd87373b3c4837b9f84d2610af734b2583e538ccafbf73.jpg

---

## Lecture: L06-AdvDataStructures_revised\page_086\L06-AdvDataStructures_revised_page_086\auto

![](images/54c4612a9c6e59471a01e5cef3ba93df77dcb48d1b66201cb15f107691108387.jpg)

• Run time?

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures_revised\page_086\L06-AdvDataStructures_revised_page_086\auto\images\54c4612a9c6e59471a01e5cef3ba93df77dcb48d1b66201cb15f107691108387.jpg

---

## Lecture: L06-AdvDataStructures_revised\page_087\L06-AdvDataStructures_revised_page_087\auto

# Binary Heap Analysis

• Space needed for heap of N nodes: O(MaxN) – An array of size MaxN, plus a variable to store the size N

• Time

– FindMin: O(1) – DeleteMin and Insert: O(log N) – BuildHeap from N inputs ???

---

## Lecture: L06-AdvDataStructures_revised\page_088\L06-AdvDataStructures_revised_page_088\auto

BuildHeap { for i = N/2 to 1 PercDown(i, A[i])   
}

![](images/573101af8207f1330ce791dfd6e328e6edc520a845be9681cf7a7e2c1ab302f9.jpg)

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures_revised\page_088\L06-AdvDataStructures_revised_page_088\auto\images\573101af8207f1330ce791dfd6e328e6edc520a845be9681cf7a7e2c1ab302f9.jpg

---

## Lecture: L06-AdvDataStructures_revised\page_089\L06-AdvDataStructures_revised_page_089\auto

![](images/4add06fa9963f0e2cb1ac21c994c9f8c2e44b3298e2dea90462faf74cc068eae.jpg)

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures_revised\page_089\L06-AdvDataStructures_revised_page_089\auto\images\4add06fa9963f0e2cb1ac21c994c9f8c2e44b3298e2dea90462faf74cc068eae.jpg

---

## Lecture: L06-AdvDataStructures_revised\page_090\L06-AdvDataStructures_revised_page_090\auto

![](images/8ebe19b5f2694049ac412e3a9090fee0f1a77e1cddf484d058f673c31b3a3f85.jpg)

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures_revised\page_090\L06-AdvDataStructures_revised_page_090\auto\images\8ebe19b5f2694049ac412e3a9090fee0f1a77e1cddf484d058f673c31b3a3f85.jpg

---

## Lecture: L06-AdvDataStructures_revised\page_091\L06-AdvDataStructures_revised_page_091\auto

# Time Complexity

Naïve considerations:

– ????/2 calls to PercDown, each takes ???? ⋅ log(????) – Total: $c \cdot n \cdot \log ( n )$

• More careful considerations: – Only $O ( n )$

---

## Lecture: L06-AdvDataStructures_revised\page_092\L06-AdvDataStructures_revised_page_092\auto

# Analysis of Build Heap

Assume $n ~ = ~ 2 ^ { h + 1 } - 1$ where h is height of the tree

– Thus, level $h$ has $2 ^ { h }$ nodes but there is nothing to PercDown – At level $h - 1$ there are $2 ^ { h - 1 }$ nodes, each might percolate down 1 level – At level $h - j ,$ there are $2 ^ { h - j }$ nodes, each might percolate down ???? levels

$$
T ( n ) = \sum _ { j = 0 } ^ { h } j 2 ^ { h - j } = \sum _ { j = 0 } ^ { h } j { \frac { 2 ^ { h } } { 2 ^ { j } } }
$$

Total Time $\mathbf { \Omega } = O ( n )$

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures_revised\page_092\L06-AdvDataStructures_revised_page_092\auto\images\02bc9d00fc375555ff96f94674dff5bedf4e4ef174918f8e2c98b69c7fb334b6.jpg

---

## Lecture: L06-AdvDataStructures_revised\page_093\L06-AdvDataStructures_revised_page_093\auto

# Other Heap Operations

Find(X, H): Find the element X in heap H of $N$ elements – What is the running time? $O ( N )$

• FindMax(H): Find the maximum element in H

• Where FindMin is ????(1) – What is the running time? $O ( N )$

• We sacrificed performance of these operations in order to get $\cdot$ performance for FindMin

---

## Lecture: L06-AdvDataStructures_revised\page_094\L06-AdvDataStructures_revised_page_094\auto

# Other Heap Operations

• DecreaseKey(P,Δ,H): Decrease the key value of node at position P by a positive amount $\Delta$ , e.g., to increase priority

– First, subtract $\Delta$ from current value at P – Heap order property may be violated – so percolate up to fix   
– Running Time: ${ \cal O } ( \log N )$

---

## Lecture: L06-AdvDataStructures_revised\page_095\L06-AdvDataStructures_revised_page_095\auto

# Other Heap Operations

• Delete(P,H): E.g. Delete a job waiting in queue that has been preemptively terminated by user

– Use DecreaseKey(P, Δ,H) followed by DeleteMin – Running Time: ${ \cal O } ( \log N )$

Merge(H1,H2): Merge two heaps H1 and H2 of size $O ( N )$ . H1 and H2 are stored in two arrays.

– Can do $O ( N )$ Insert operations: ${ \cal O } ( N \log N )$ time Better: Copy H2 at the end of H1 and use BuildHeap. Running Time: $O ( N )$

---

## Lecture: L06-AdvDataStructures_revised\page_096\L06-AdvDataStructures_revised_page_096\auto

# Other Heap Operations

• Merge(H1,H2): Merge two heaps H1 and H2 of size ????(????). H1 and H2 are stored in two arrays.

– Can do $O ( N )$ Insert operations: ${ \cal O } ( N \log N )$ time Better: Copy H2 at the end of H1 and use BuildHeap. Running Time: $O ( N )$

---

## Lecture: L06-AdvDataStructures_revised\page_097\L06-AdvDataStructures_revised_page_097\auto

# Heap Sort

• Idea: buildHeap then call deleteMin n times

input $=$ buildHeap(...);   
output $=$ new E[n];   
for (int $\mathsf { i } = 0 ; \mathsf { i } < \mathsf { n } ; \mathsf { i } + + \mathsf { f } \left\{ \begin{array} { r l } \end{array} \right.$ output[i] $=$ deleteMin(input);   
}

• Runtime?

• Best-case • Worst-case • Average-case • Stable?

• In-place?

---

## Lecture: L06-AdvDataStructures_revised\page_098\L06-AdvDataStructures_revised_page_098\auto

# Heap Sort

• Idea: buildHeap then call deleteMin ???? times

input $=$ buildHeap(...);   
output $=$ new E[n];   
for (int $\mathsf { i } = 0 ; \mathsf { i } < \mathsf { n } ; \mathsf { i } + + \mathsf { f } \left\{ \begin{array} { r l } \end{array} \right.$ output[i] $=$ deleteMin(input);   
}

• Runtime?

• Best-case, Worst-case, and Average-case: $O ( n \log ( n ) )$

• Stable? No.

• In-place? No. But it could be, with a slight trick...

---

## Lecture: L06-AdvDataStructures_revised\page_099\L06-AdvDataStructures_revised_page_099\auto

# In-place Heap Sort

• Treat the initial array as a heap (via buildHeap)

But this reverse sorts – how would you fix that?

• When you delete the ith element, put it at arr[n-i] • That array location isn’t needed for the heap anymore!

![](images/81ed35a02838451df30bd7e99047e9d8be253962541469bbdbeff828712d8bb1.jpg)

put the min at the end of the heap data

![](images/8e079f2153c3799f7d3045b628c0cfeab5c6a1360280db94b2041dcc70a70d41.jpg)

### Images:
- data\Design and Analysis of Algorithms\L06-AdvDataStructures_revised\page_099\L06-AdvDataStructures_revised_page_099\auto\images\81ed35a02838451df30bd7e99047e9d8be253962541469bbdbeff828712d8bb1.jpg
- data\Design and Analysis of Algorithms\L06-AdvDataStructures_revised\page_099\L06-AdvDataStructures_revised_page_099\auto\images\8e079f2153c3799f7d3045b628c0cfeab5c6a1360280db94b2041dcc70a70d41.jpg

---

## Lecture: L06-AdvDataStructures_revised\page_100\L06-AdvDataStructures_revised_page_100\auto

Sure, we can also use an AVL tree to:

• Insert each element: total time $O ( n \mathrm { l o g } n )$

• Repeatedly deleteMin: total time $O ( n \log n )$ – Better: in-order traversal $O ( n )$ , but still $O ( n \log n )$ overall

• But this cannot be done in-place and has worse constant factors than heap sort

---

## Lecture: L07-DP\page_001\L07-DP_page_001\auto

# Dynamic Programming (1)

Fibonacci Numbers Matrix chain multiplication Knapsack Problem

---

## Lecture: L07-DP\page_002\L07-DP_page_002\auto

# Fibonacci Numbers

• Definition

$$
f ( n ) = \left\{ \begin{array} { c } { { 0 } } { { i f ~ n = 0 } } \\ { { 1 } } \\ { { { } } } \\ { { { \cal F } ( n - 1 ) + { \cal F } ( n - 2 ) ~ i f ~ n > 1 } } \end{array} \right.
$$

![](images/cf0b4fa8045c29425601124a6140979fbae124362015c8f1ef72601c5f67d6da.jpg)

• The first several numbers are: – 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89 , 144 …

• Question: Given n, how to compute F(n)? Recursion

Leonardo Fibonacci

### Images:
- data\Design and Analysis of Algorithms\L07-DP\page_002\L07-DP_page_002\auto\images\49a838c8aa184b76aa64bc94db1d0f2578bc3c99da30850f95bb1a9d5e314d40.jpg
- data\Design and Analysis of Algorithms\L07-DP\page_002\L07-DP_page_002\auto\images\cf0b4fa8045c29425601124a6140979fbae124362015c8f1ef72601c5f67d6da.jpg

---

## Lecture: L07-DP\page_003\L07-DP_page_003\auto

# Fibonacci Numbers – Naïve Algorithm

• Computing the ${ \mathsf n } ^ { \mathsf { t h } }$ Fibonacci number recursively:

$$
f ( n ) = \left\{ \begin{array} { c } { { 0 } } \\ { { 1 } } \\ { { } } \\ { { F ( n - 1 ) + F ( n - 2 ) i f n > 1 } } \end{array} \right.
$$

def Fib(n): if $( \mathsf { n } < = 1 )$ return n; else return $\mathsf { F i b } ( \mathsf { n } - 1 ) + \mathsf { F i b } ( \mathsf { n } - 2 ) ;$ ;

![](images/869d6e6b544cccbecef23a7036c3750109f69bdb8d98b7447964a9cca9d9dde2.jpg)

### Images:
- data\Design and Analysis of Algorithms\L07-DP\page_003\L07-DP_page_003\auto\images\869d6e6b544cccbecef23a7036c3750109f69bdb8d98b7447964a9cca9d9dde2.jpg
- data\Design and Analysis of Algorithms\L07-DP\page_003\L07-DP_page_003\auto\images\b47f75c3b5b6e07d21d714945c33c321eb75790fd99bc1236dc99ef2f69dc96d.jpg

---

## Lecture: L07-DP\page_004\L07-DP_page_004\auto

# Fibonacci Numbers – Naïve Algorithm

• Running time

$$
T ( n ) = T ( n - 1 ) + T ( n - 2 ) + O ( 1 )
$$

$$
\Rightarrow T ( n ) \geq T ( n - 1 ) + T ( n - 2 ) { \mathrm { ~ f o r ~ } } n \geq 2
$$

• What is the solution to this?

– Clearly it is O(2n), but this is not tight.   
– A lower bound is $\Omega ( 2 ^ { { \mathsf { n } } / 2 } )$ .   
– You should notice that T(n) grows as fast as the Fibonacci numbers F(n), so in fact ${ \sf T } ( { \sf n } ) = \Theta ( { \sf F } ( { \sf n } ) )$ .

### Images:
- data\Design and Analysis of Algorithms\L07-DP\page_004\L07-DP_page_004\auto\images\6c5d0208f38e6318126188bb976249165312cfa73a4ef1630dda9485899f177a.jpg
- data\Design and Analysis of Algorithms\L07-DP\page_004\L07-DP_page_004\auto\images\78c14672a0626f90ca68092dde2f0f7669b991a2625fac3f3be802c3a20793c0.jpg

---

## Lecture: L07-DP\page_005\L07-DP_page_005\auto

# Fibonacci Numbers – Naïve Algorithm

• What’s going on with this naïve approach?

![](images/f89b48365c247793de151a32dc80523d18844cb8f8d8a39b0be75842e973624f.jpg)

That’s a lot of repeated computation!

### Images:
- data\Design and Analysis of Algorithms\L07-DP\page_005\L07-DP_page_005\auto\images\f89b48365c247793de151a32dc80523d18844cb8f8d8a39b0be75842e973624f.jpg

---

## Lecture: L07-DP\page_006\L07-DP_page_006\auto

• Memoization frees us from redundant calculations  – Remember solutions of all the sub-problems – Trade space for time

![](images/dbfd0efa95332799b0a7cf8dd5370442886ceaca74c252a5825b72061a61ccbe.jpg)

<table><tr><td rowspan=1 colspan=1>Sub-problem</td><td rowspan=1 colspan=1>Opt Solution</td></tr><tr><td rowspan=1 colspan=1>fib(0)</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>fib(1)</td><td rowspan=1 colspan=1>1</td></tr><tr><td rowspan=1 colspan=1>fib(2)</td><td rowspan=1 colspan=1>1</td></tr><tr><td rowspan=1 colspan=1>fib(3)</td><td rowspan=1 colspan=1>2</td></tr><tr><td rowspan=1 colspan=1>fib(4)</td><td rowspan=1 colspan=1>3</td></tr></table>

### Images:
- data\Design and Analysis of Algorithms\L07-DP\page_006\L07-DP_page_006\auto\images\78ac37430b0be4db3453c0495f26e59e57aab2c7a7d3f9439ca2591393779bb0.jpg
- data\Design and Analysis of Algorithms\L07-DP\page_006\L07-DP_page_006\auto\images\dbfd0efa95332799b0a7cf8dd5370442886ceaca74c252a5825b72061a61ccbe.jpg

---

## Lecture: L07-DP\page_007\L07-DP_page_007\auto

# Fibonacci Numbers

– Computing the $\mathsf { n } ^ { \mathrm { t h } }$ Fibonacci number using as follow:

![](images/bfe0227a403a5d8e76eac3f2dc3ac25648a0fa4412c964da329bedf7b6249ae6.jpg)

def fasterFibonacci(n): F = [0, 1, None, None, …, None ] \\ F has length n + 1 for i = 2, …, n: $\mathrm { ~ F ~ [ \dot { ~ } ] ~ } ~ = ~ \mathrm { ~ F ~ [ \dot { ~ } - 1 ~ ] ~ } ~ + ~ \mathrm { ~ F ~ [ \dot { ~ } { \bf ~ i } - 2 ~ ] ~ }$ return F[n]

<table><tr><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>F(n-2)</td><td rowspan=1 colspan=1>F(n-1)</td><td rowspan=1 colspan=1>F(n)</td></tr></table>

• Efficiency: – Time – O(n) – Space – O(n)  can be improved to O(1)

This is an example of dynamic programming 

### Images:
- data\Design and Analysis of Algorithms\L07-DP\page_007\L07-DP_page_007\auto\images\bfe0227a403a5d8e76eac3f2dc3ac25648a0fa4412c964da329bedf7b6249ae6.jpg
- data\Design and Analysis of Algorithms\L07-DP\page_007\L07-DP_page_007\auto\images\cd5ffc2714b3b164deee00ff5042b8eebd8c8ab3f6575315cfe748b793085e3c.jpg

---

## Lecture: L07-DP\page_008\L07-DP_page_008\auto

# Dynamic Programming

Ideas

Ensure all needed recursive calls are already computed and memorized

a good schedule of computation

(Optional) Reused space to store previous recursive call results

 Arrive at the same efficient (special) solution for Fib()

![](images/85e1d84d09f31630a9bfdcb73cf7892ce423618e08e06973112c4072e8598696.jpg)

### Images:
- data\Design and Analysis of Algorithms\L07-DP\page_008\L07-DP_page_008\auto\images\85e1d84d09f31630a9bfdcb73cf7892ce423618e08e06973112c4072e8598696.jpg

---

## Lecture: L07-DP\page_009\L07-DP_page_009\auto

“ Those who cannot remember the past are condemned to repeat it.

Dynamic Programming

---

## Lecture: L07-DP\page_010\L07-DP_page_010\auto

# Dynamic Programming

• Dynamic Programming is an algorithm design technique for optimization problems: often minimizing or maximizing.

• Like divide and conquer, DP solves problems by combining solutions to sub-problems.

• Unlike divide and conquer, sub-problems are not independent. – DP breaks up a problem into a series of overlapping sub-problems. • i.e, Both F[i+1] and F[i+2] directly use F[i]. And lots of different $\mathsf { F } [ \mathsf { i } + \mathsf { x } ]$ indirectly use F[i]

---

## Lecture: L07-DP\page_011\L07-DP_page_011\auto

# Main Ideas

1. Recursion: Divide the problem into sub-problems, so that their solutions can be combined into a solution to the problem.

2. Tabulation of sub-problems: Solve each sub-problem just once and save its solution in a “look-up” table.

---

## Lecture: L07-DP\page_012\L07-DP_page_012\auto

# Dynamic Programming

• The term Dynamic Programming comes from Control Theory, not computer science. Programming refers to the use of tables (arrays) to construct a solution.

• In Dynamic Programming, we usually reduce time by increasing the amount of space.

• We solve the problem by solving sub-problems of increasing size and saving each optimal solution in a table (usually).

• The table is then used for finding the optimal solution to larger problems.

• Time is saved since each sub-problem is solved only once.

---

## Lecture: L07-DP\page_013\L07-DP_page_013\auto

# Two Ways to Think and Implement DP

• Top down:

• Think of it like a recursive algorithm.   
To solve the big problem: Recurse to solve smaller problems Those recurse to solve smaller problems etc..

• The difference from divide and conquer:

Keep track of what small problems you’ve already solved to prevent resolving the same problem twice. • Aka, “memoization”

• Bottom up:

• For Fibonacci:

• Solve the small problems first • fill in F[0],F[1]

• Then bigger problems

• Then bigger problems fill in F[n-1]

• Then finally solve the real problem. fill in F[n]

---

## Lecture: L07-DP\page_014\L07-DP_page_014\auto

# Example of Top-Down Fibonacci

define a global list F = [0,1,None, None, …, None] def Fibonacci(n):

if $\begin{array} { r } { \mathrm { ~ \mathbb { E } ~ } [ { \mathrm { ~ n ~ } } ] \quad ! = { \mathrm { ~ \mathbb { N } o n e : ~ } } } \end{array}$ return F[n]   
else: $\begin{array} { r l } { \operatorname { F } \left[ \mathrm { n } \right] } & { { } = } \end{array}$ Fibonacci(n-1) $+$ Fibonacci(n-2)   
return F[n]

Memoization: Keeps track (in F) of the stuff you've already done.

![](images/be3fbbf6df913e4351e934c58dbe5fbcb280e5b6e42a26396b941921d4baf8ad.jpg)

### Images:
- data\Design and Analysis of Algorithms\L07-DP\page_014\L07-DP_page_014\auto\images\be3fbbf6df913e4351e934c58dbe5fbcb280e5b6e42a26396b941921d4baf8ad.jpg

---

## Lecture: L07-DP\page_015\L07-DP_page_015\auto

# Memoization Visualization

![](images/09f654a27fa597bc713af3817cfec46de72ba9438b294979231073c502762098.jpg)

### Images:
- data\Design and Analysis of Algorithms\L07-DP\page_015\L07-DP_page_015\auto\images\09f654a27fa597bc713af3817cfec46de72ba9438b294979231073c502762098.jpg

---

## Lecture: L07-DP\page_016\L07-DP_page_016\auto

# Dynamic Programming

• Underpins many optimization problems, e.g., – Matrix Chaining optimization – Longest Common Subsequence – 0-1 Knapsack Problem – Shortest path

• Next we will give many example problems to help understand the basic idea of Dynamic Programming.

---

## Lecture: L07-DP\page_017\L07-DP_page_017\auto

# Recipe for Applying Dynamic Programming

• Step 1: Identify optimal substructure.

• Step 2: Find a recursive formulation for the value of the optimal solution.

• Step 3: Use dynamic programming to find the value of the optimal solution.

Step 4: If needed, keep track of some additional info so that the algorithm from Step 3 can find the actual solution.

• Step 5: If needed, code this up.

---

## Lecture: L07-DP\page_018\L07-DP_page_018\auto

# Matrix Chain Multiplication

• Review: Matrix Multiplication.

$- C = A ^ { * } B$ $\begin{array} { l } { - A \mathrm { ~ i s ~ } d \times e \mathrm { ~ a n d ~ } B \mathrm { ~ i s ~ } e \times f } \\ { - O ( d \cdot e \cdot f ) \mathrm { t i m e } } \end{array}$

$$
C [ i , j ] = \sum _ { k = 0 } ^ { e - 1 } A [ i , k ] * B [ k , j ]
$$

![](images/05f92dedb3a9401e305eff3b5714b54aef9ce2619ce1f414154f6525107c2ca5.jpg)

### Images:
- data\Design and Analysis of Algorithms\L07-DP\page_018\L07-DP_page_018\auto\images\05f92dedb3a9401e305eff3b5714b54aef9ce2619ce1f414154f6525107c2ca5.jpg
- data\Design and Analysis of Algorithms\L07-DP\page_018\L07-DP_page_018\auto\images\27c763c00f927ceeb217892e91774a3825f0f855f3a6f7ee782fdcddc34e3aaa.jpg
- data\Design and Analysis of Algorithms\L07-DP\page_018\L07-DP_page_018\auto\images\c50b4fc03b4ac0774a6ae9a4553c0019a06e7156f0d92714fea3ab26945af989.jpg
- data\Design and Analysis of Algorithms\L07-DP\page_018\L07-DP_page_018\auto\images\d27da5d312624f37adb941ce2ed68c53b0ab4f089cd023225b8a3b1c6187991f.jpg

---

## Lecture: L07-DP\page_019\L07-DP_page_019\auto

# Matrix Chain Multiplication

# • Matrix Chain Multiplication:

– Compute $\mathsf { A } { = } \mathsf { A } _ { 0 } { } ^ { * } \mathsf { A } _ { 1 } { } ^ { * } { \ldots } { } ^ { * } \mathsf { A } _ { \mathsf { n } { - } 1 }$ (id – Ai is di × di+1 – Problem: How to parenthesize?

• Example

– B is 3 × 100   
– C is 100 × 5   
– D is 5 × 5   
$- ( \mathsf { B } ^ { \ast } \mathsf { C } ) ^ { \ast } \mathsf { D }$ takes $1 5 0 0 + 7 5 = 1 5 7 5$ ops • $( 3 \times 1 0 0 \times 5 ) + ( 3 \times 5 \times 5 )$   
$- \textsf { B } ^ { * } ( \mathsf { C } ^ { * } \mathsf { D } )$ takes $1 5 0 0 + 2 5 0 0 = 4 0 0 0$ ops

### Images:
- data\Design and Analysis of Algorithms\L07-DP\page_019\L07-DP_page_019\auto\images\de1ebd9b60c3078744dc00571cf7a24880d6a16954b208885325b370b1dd897c.jpg

---

## Lecture: L07-DP\page_020\L07-DP_page_020\auto

# Enumeration Approach for MCM

# • Matrix Chain Multiplication Alg.:

– Try all possible ways to parenthesize $\mathsf { A } { = } \mathsf { A } _ { 0 } { } ^ { * } \mathsf { A } _ { 1 } { } ^ { * } { \ldots } { } ^ { * } \mathsf { A } _ { \mathsf { n } { - } 1 }$   
– Calculate number of ops for each one   
– Pick the one that is best

• Running time:

– The number of parenthesizations is equal to the number of binary trees with $n - 1$ nodes   
– This is exponential!   
– It is called the Catalan number, and it is almost $4 ^ { n }$ .   
– This is a terrible algorithm!

---

## Lecture: L07-DP\page_021\L07-DP_page_021\auto

# Greedy Approach for MCM

• Idea #1: repeatedly select the product that uses the fewest operations.

• Counter-example:

– A is $1 0 1 \times 1 1$   
– B is 11 × 9   
– C is 9 × 100   
– D is 100 × 99   
– Greedy idea #1 gives $\mathsf { A } ^ { * } ( ( \mathsf { B } ^ { * } \mathsf { C } ) ^ { * } \mathsf { D } ) )$ , which takes 109989+9900+108900=228789 ops   
$- \ ( \mathsf { A } ^ { * } \mathsf { B } ) ^ { * } ( \mathsf { C } ^ { * } \mathsf { D } )$ takes 9999+89991+89100 $=$ 189090 ops

• The greedy approach is not giving us the optimal value.

---

## Lecture: L07-DP\page_022\L07-DP_page_022\auto

# Dynamic Programming Approach for MCM

• The optimal solution can be defined in terms of optimal sub-problems

– There has to be a final multiplication (root of the expression tree) for the optimal solution.   
– Say, the final multiplication is at index k: $( { \mathsf { A } _ { 0 } } ^ { * } . . . . ^ { * } { \mathsf { A } _ { \mathrm { k } } } ) ^ { * } ( { \mathsf { A } _ { { \mathrm { k } } + 1 } } ^ { * } . . . ^ { * } { \mathsf { A } _ { { \mathrm { n } } - 1 } } ) .$

• Let us consider all possible places for that final multiplication: – There are $n { - } 1$ possible splits. Assume we know the minimum cost of computing the matrix product of each combination $\mathsf { A } _ { 0 } . . . \mathsf { A } _ { \mathrm { i } }$ and $\mathsf { A } _ { \mathsf { i } + 1 } . . . \mathsf { A } _ { \mathsf { n } - 1 }$ . Let’s call these $\mathsf { N } _ { 0 , \mathsf { I } }$ i and $\mathsf { N } _ { \mathsf { i } + 1 , \mathsf { n } - 1 }$ .

• Recall that A $\mathsf { \Omega } _ { \mathrm { i } } \mathsf { i } s \mathsf { a } \mathsf { d } _ { \mathrm { i } } \times \mathsf { d } _ { \mathsf { i } + 1 }$ dimensional matrix, and the final result will be a ${ \sf d } _ { 0 } \times { \sf d } _ { \sf n }$ .

### Images:
- data\Design and Analysis of Algorithms\L07-DP\page_022\L07-DP_page_022\auto\images\c4dcf1acf8783b87d49367984c00c365ad2cbc2d49f56f8e21f045e21874b19f.jpg

---

## Lecture: L07-DP\page_023\L07-DP_page_023\auto

# Dynamic Programming Approach for MCM

Define the following:

– Then the optimal solution $\mathsf { N } _ { 0 , \mathsf { n } - 1 }$ is the sum of two optimal sub-problems, $\mathsf { N } _ { 0 , \mathsf { k } }$ and $\mathsf { N } _ { \mathsf { k } + 1 , \mathsf { n } - 1 }$ plus the time for the last multiplication.

---

## Lecture: L07-DP\page_024\L07-DP_page_024\auto

# Dynamic Programming Approach for MCM

• Define sub-problems:

– Find the best parenthesization of an arbitrary set of consecutive products: $\mathsf { A } _ { \mathrm { i } } ^ { * } \mathsf { A } _ { \mathrm { i } + 1 } ^ { * } \cdots ^ { * } \mathsf { A } _ { \mathrm { j } } .$   
– Let Ni,j denote the minimum number of operations done by this sub-problem. • Define $\mathsf { N } _ { \mathsf { k , k } } = 0$ for all $\boldsymbol { \mathsf { k } }$ .   
– The optimal solution for the whole problem is then $\mathsf { N } _ { 0 , \mathsf { n } - 1 }$ .

---

## Lecture: L07-DP\page_025\L07-DP_page_025\auto

# Dynamic Programming Approach for MCM

• The characterizing equation for Ni,j is:

$$
\ d s _ { i , j } = \operatorname * { m i n } _ { i \leq k < j } \{ N _ { i , k } + N _ { k + 1 , j } + d _ { i } d _ { k + 1 } d _ { j }
$$

• Note that, for example $\mathsf { N } _ { 2 , 6 }$ and $\mathsf { N } _ { 3 , 7 } ,$ , both need solutions to $\mathsf { N } _ { 3 , 6 } , \mathsf { N } _ { 4 , 6 } , \mathsf { N } _ { 5 , 6 } ,$ and $\mathsf { N } _ { 6 , 6 }$ . Solutions from the set of no matrix multiplies to four matrix multiplies.

– This is an example of high sub-problem overlap, and clearly pre-computing these will significantly speed up the algorithm.

### Images:
- data\Design and Analysis of Algorithms\L07-DP\page_025\L07-DP_page_025\auto\images\8a9e7326aa949616e5f49a9ddc79d3a9c415b34fff3a00588f2425eed161b567.jpg

---

## Lecture: L07-DP\page_026\L07-DP_page_026\auto

# Recursive Approach

• We could implement the calculation of these Ni,j’s using a straightforward recursive implementation of the equation (aka not pre-compute them).

Algorithm RecursiveMatrixChain(S, i, j):

Input: sequence $\mathcal { S }$ of n matrices to be multiplied   
Output: number of operations in an optimal parenthesization of $\mathcal { S }$   
if i=j then return 0   
for $k \gets \mathrm { i }$ to $j$ do Ni, j ← min{Ni,j, RecursiveMatrixChain(S, i ,k) + RecursiveMatrixChain(S, k+1,j) + di dk+1 dj+1}   
return $N _ { i , j }$

---

## Lecture: L07-DP\page_027\L07-DP_page_027\auto

# Subproblem Overlap

$$
\bar { \mathrm { V } } _ { i , j } = \operatorname * { m i n } _ { i \leq k < j } \{ N _ { i , k } + N _ { k + 1 , j } + . .
$$

![](images/54be142336b3d265e35b107c688b57e017d0fa6c9f79b80f0527f2b1cac4fc2f.jpg)

### Images:
- data\Design and Analysis of Algorithms\L07-DP\page_027\L07-DP_page_027\auto\images\54be142336b3d265e35b107c688b57e017d0fa6c9f79b80f0527f2b1cac4fc2f.jpg
- data\Design and Analysis of Algorithms\L07-DP\page_027\L07-DP_page_027\auto\images\f05884d3075ce013d71eb34306cceba00cac26cca6a03b4b9ac35fbb409260a1.jpg

---

## Lecture: L07-DP\page_028\L07-DP_page_028\auto

# Dynamic Programming Algorithm

• High sub-problem overlap, with independent sub-problems indicate that a dynamic programming approach may work.

• Construct optimal sub-problems “bottom-up.” and remember them.

• Ni,i’s are easy, so start with them

• Then do problems of length 2,3,… sub-problems, and so on.

• Running time: O(n3)

---

## Lecture: L07-DP\page_029\L07-DP_page_029\auto

# Dynamic Programming Algorithm

Algorithm matrixChain $( S )$ :

Input: sequence $\boldsymbol { \cdot }$ of n matrices to be multiplied   
Output: number of operations in an optimal parenthesization of $S$   
for $i \gets 1$ to $m - 1$ do $N _ { i , i } \gets 0$   
for $b \gets 1$ to $n - 1$ do { $b = j - \tau$ is the length of the problem } for $i \gets 0$ to $n - 6 = 7$ do $j \gets i + b$ $N _ { i , j } \gets + \infty$ for $k \gets i$ to $j - 1$ do $N _ { i , j } \gets \operatorname* { m i n } \{ N _ { i , j } , N _ { i , k } + N _ { k + 1 , j } + d _ { i } d _ { k + 1 } d _ { j + 1 } \}$   
return ${ \cal N } _ { 0 , n - 1 }$

### Images:
- data\Design and Analysis of Algorithms\L07-DP\page_029\L07-DP_page_029\auto\images\3d81939e612d009f96968e42ff3d17b6f9dc16149e2a135f360ff4908514905d.jpg
- data\Design and Analysis of Algorithms\L07-DP\page_029\L07-DP_page_029\auto\images\68146b92e8fcdf89676254054763514a0809e5b973905d508a336ed4e016a002.jpg
- data\Design and Analysis of Algorithms\L07-DP\page_029\L07-DP_page_029\auto\images\ae4230fc4d7b9c2c0d2459c71521174d109c41c91d77c7051a0f5bfd3447429c.jpg
- data\Design and Analysis of Algorithms\L07-DP\page_029\L07-DP_page_029\auto\images\bff6d9eba8dcfd45afcc1a75be3f62e557d668decd57ae6f1d459811da09c447.jpg

---

## Lecture: L07-DP\page_030\L07-DP_page_030\auto

# Algorithm Visualization

• The bottom-up construction fills in the N array by diagonals

• Ni,j gets values from previous entries in i-th row and j-th column

• Filling in each entry in the N table takes O(n) time.

• Total run time: O(n3)

• Getting actual parenthesization can be done by remembering $" \mathrm { k } '$ for each N entry

$$
N _ { i , j } = \operatorname* { m i n } _ { i \leq k < j } \{ N _ { i , k } + N _ { k + 1 , j } + d _ { i } d _ { k + 1 } d _ { j + 1 } \}
$$

![](images/65e11b9f18a300dd664892e3cc0493ce5cb0e02fc8154444591414ef1d5bbedf.jpg)

### Images:
- data\Design and Analysis of Algorithms\L07-DP\page_030\L07-DP_page_030\auto\images\65e11b9f18a300dd664892e3cc0493ce5cb0e02fc8154444591414ef1d5bbedf.jpg
- data\Design and Analysis of Algorithms\L07-DP\page_030\L07-DP_page_030\auto\images\9d45649f440ac894cf67b59650d8739e882db31bf1ef2086a5eb2ceb97eba365.jpg

---

## Lecture: L07-DP\page_031\L07-DP_page_031\auto

# Algorithm Visualization

• A0: 30 X 35; A1: 35 X15; A2: 15X5; A3: 5X10; A4: 10X20; $\mathsf { A } _ { 5 }$ : 20 X 25

![](images/39c501dc84196ec3e7f12f528e3ce83e16a32c32caeba0bcc9633500899e0698.jpg)

$$
N _ { i , j } = \operatorname* { m i n } _ { i \leq k < j } \{ N _ { i , k } + N _ { k + 1 , j } + d _ { i } d _ { k + 1 } d _ { j + 1 } \}
$$

$$
\begin{array} { r l } & { N _ { 1 , 4 } = \operatorname* { m i n } \{ } \\ & { N _ { 1 , 1 } + N _ { 2 , 4 } + d _ { 1 } d _ { 2 } d _ { 5 } = 0 + 2 5 0 0 + 3 5 * 1 5 * 2 0 = 1 3 0 0 0 , } \\ & { N _ { 1 , 2 } + N _ { 3 , 4 } + d _ { 1 } d _ { 3 } d _ { 5 } = 2 6 2 5 + 1 0 0 0 + 3 5 * 5 * 2 0 = 7 1 2 5 } \\ & { N _ { 1 , 3 } + N _ { 4 , 4 } + d _ { 1 } d _ { 4 } d _ { 5 } = 4 3 7 5 + 0 + 3 5 * 1 0 * 2 0 = 1 1 3 7 5 } \\ & { \vdots } \\ & { = 7 1 2 5 } \end{array}
$$

### Images:
- data\Design and Analysis of Algorithms\L07-DP\page_031\L07-DP_page_031\auto\images\0565d2b563ac4697349f8fde87117ac120bbe6dc2bc56167f747127a4923d78d.jpg
- data\Design and Analysis of Algorithms\L07-DP\page_031\L07-DP_page_031\auto\images\0f8a31faffd68f157ff91b71b570f3909a662e533ec9c5822279c8f55cf1ab76.jpg
- data\Design and Analysis of Algorithms\L07-DP\page_031\L07-DP_page_031\auto\images\39c501dc84196ec3e7f12f528e3ce83e16a32c32caeba0bcc9633500899e0698.jpg

---

## Lecture: L07-DP\page_032\L07-DP_page_032\auto

$$
( \mathsf { A } _ { 0 } ^ { \ast } ( \mathsf { A } _ { 1 } ^ { \ast } \mathsf { A } _ { 2 } ) ) ^ { \ast } ( ( \mathsf { A } _ { 3 } ^ { \ast } \mathsf { A } _ { 4 } ) ^ { \ast } \mathsf { A } _ { 5 } )
$$

![](images/8a350f1bb5fd91decfeeaa3c871a09d97b08f5b8ce0857dc72e3b64189b87215.jpg)

![](images/f2c7a6fd381e78d661febfb189c6e0c732a52140f436b903cb76c8cb9b413d8b.jpg)

### Images:
- data\Design and Analysis of Algorithms\L07-DP\page_032\L07-DP_page_032\auto\images\6d818113b8477a546e96775ea0745e49af13bd310f76a5168ee5f9ad97538c33.jpg
- data\Design and Analysis of Algorithms\L07-DP\page_032\L07-DP_page_032\auto\images\8a350f1bb5fd91decfeeaa3c871a09d97b08f5b8ce0857dc72e3b64189b87215.jpg
- data\Design and Analysis of Algorithms\L07-DP\page_032\L07-DP_page_032\auto\images\f2c7a6fd381e78d661febfb189c6e0c732a52140f436b903cb76c8cb9b413d8b.jpg

---

## Lecture: L07-DP\page_033\L07-DP_page_033\auto

# Matrix Chain Multiplication

• Some final thoughts

–We reduced replaced a O(2n) algorithm with a Θ(n3) algorithm.

–While the generic top-down recursive algorithm would have solved $O ( 2 ^ { \mathfrak { n } } )$ sub-problems, there are Θ(n2) subproblems.

• Implies a high overlap of sub-problems.

–The sub-problems are independent:

• Solution to $\mathsf { A } _ { 0 } \mathsf { A } _ { 1 } . . . \mathsf { A } _ { \mathsf { k } }$ is independent of the solution to $\mathsf { A } _ { \mathsf { k } + 1 } . . . \mathsf { A } _ { \mathsf { n } }$

---

## Lecture: L07-DP\page_034\L07-DP_page_034\auto

# Matrix Chain Multiplication Summary

• Determine the cost of each pair-wise multiplication, then the minimum cost of multiplying three consecutive matrices (2 possible choices), using the pre-computed costs for two matrices.

• Repeat until we compute the minimum cost of all n matrices using the costs of the minimum n-1 matrix product costs. – n-1 possible choices.

---

## Lecture: L07-DP\page_035\L07-DP_page_035\auto

# The 0/1 Knapsack Problem

• Given: A set S of $n$ items (one piece each), with each item i having – wi - a positive weight – bi - a positive benefit

• Goal: Choose items with maximum total benefit but with weight at most W.

• If we are not allowed to take fractional amounts, then this is the 0/1 knapsack problem.

– In this case, we let T denote the set of items we take   
– Objective: maximize $\sum _ { i \in T } b _ { i }$   
– Constraint: $\sum _ { i \in T } w _ { i } \leq W$

Linear Programming formulation

### Images:
- data\Design and Analysis of Algorithms\L07-DP\page_035\L07-DP_page_035\auto\images\0bfa0a5efea6ffdb8a16c4b73a56f097a0dbc525c37fb6070919cfc1aa62bc68.jpg
- data\Design and Analysis of Algorithms\L07-DP\page_035\L07-DP_page_035\auto\images\6371d171e5ab1ed26cdc0b9be88468e8edd442cd10486d4cab83fca1e52cc239.jpg

---

## Lecture: L07-DP\page_036\L07-DP_page_036\auto

• Given: A set S of n items, with each item i having – b - a positive “benefit” – w - a positive “weight”

• Goal: Choose items with maximum total benefit but with weight at most W.

Items:

“knapsack”

![](images/13894db7b58fcac68417b5b94e0f3e446f4e867803dd31bfbbeb58f4cdb629d8.jpg)

![](images/d27b8206c9b1924088f62ebe879f8d7da2ceb212794e663a26ebc9d63bc3b849.jpg)

box of width 9 in

Weight: 4 in 2 in 2 in 6 in 2 in Benefit: \$20 \$3 \$6 \$25 \$80

Solution:

• item 5 (\$80, 2 in) • item 3 (\$6, 2 in) • item 1 (\$20, 4 in)

### Images:
- data\Design and Analysis of Algorithms\L07-DP\page_036\L07-DP_page_036\auto\images\13894db7b58fcac68417b5b94e0f3e446f4e867803dd31bfbbeb58f4cdb629d8.jpg
- data\Design and Analysis of Algorithms\L07-DP\page_036\L07-DP_page_036\auto\images\d27b8206c9b1924088f62ebe879f8d7da2ceb212794e663a26ebc9d63bc3b849.jpg

---

## Lecture: L07-DP\page_037\L07-DP_page_037\auto

# First Attempt

• S : Set of items numbered 1 to k.

• Define B[k] $=$ best selection from $\mathsf { S } _ { \mathsf { k } }$ .

• Problem: does not have sub-problem optimality: – Consider set $S = 1$ {(3,2),(5,4),(8,5),(4,3),(10,9)} of (benefit, weight) pairs and total weight $W = 2 0$

Best for $\mathsf { S } _ { 4 }$ :

<table><tr><td rowspan=1 colspan=1>(3,2)</td><td rowspan=1 colspan=1>(5,4)</td><td rowspan=1 colspan=1>(8,5)</td><td rowspan=1 colspan=1>(4,3)</td></tr></table>

Best for $\mathsf { S } _ { 5 }$

![](images/be048b429e461bc1a15dbb1e25103bd9622598028d1dc30d90dc4c7a2990e7b6.jpg)

### Images:
- data\Design and Analysis of Algorithms\L07-DP\page_037\L07-DP_page_037\auto\images\be048b429e461bc1a15dbb1e25103bd9622598028d1dc30d90dc4c7a2990e7b6.jpg
- data\Design and Analysis of Algorithms\L07-DP\page_037\L07-DP_page_037\auto\images\f69745193e082b661c6e6472aafba940c5914c2a1f207dcfd9c98c0e5b18df26.jpg

---

## Lecture: L07-DP\page_038\L07-DP_page_038\auto

# Second Attempt

• S : Set of items numbered 1 to k.   
• Define $\mathsf { B } [ \mathsf { k } , \mathsf { w } ]$ to be the best selection from $\mathsf { S } _ { \mathsf { k } }$ with weight at most w • This does have sub-problem optimality.

$$
\begin{array} { r } { c , w \Big ] = \left\{ \begin{array} { c } { B [ k - 1 , w ] } \\ { \mathrm { m a x } \{ B [ k - 1 , w ] , ~ B [ k - 1 , w - w _ { k } ] + b } \end{array} \right. } \end{array}
$$

• I.e., the best subset of $\mathsf { S } _ { \mathsf { k } }$ with weight at most w is either: – the best subset of $S _ { \mathrm { k } - 1 }$ with weight at most w or – the best subset of $\mathsf { S } _ { \mathsf { k } - 1 }$ with weight at most $w { - } w _ { k }$ plus item $k$

### Images:
- data\Design and Analysis of Algorithms\L07-DP\page_038\L07-DP_page_038\auto\images\4046b11dddaec1d480d5e1dcfbc6f6697170c08e6f4136309fe390720e61143e.jpg

---

## Lecture: L07-DP\page_039\L07-DP_page_039\auto

# Knapsack Example

Knapsack of capacity $W = 5$ $\begin{array} { l l } { { w _ { \scriptscriptstyle 1 } = 2 , v _ { \scriptscriptstyle 1 } = 1 2 \quad w _ { \scriptscriptstyle 2 } = 1 , v _ { \scriptscriptstyle 2 } = 1 0 } } \\ { { } } & { { } } \\ { { w _ { \scriptscriptstyle 3 } = 3 , v _ { \scriptscriptstyle 3 } = 2 0 \quad w _ { \scriptscriptstyle 4 } = 2 , v _ { \scriptscriptstyle 4 } = 1 5 } } \end{array}$

<table><tr><td>item</td><td>weight</td><td>value</td></tr><tr><td>1</td><td>2</td><td>$12</td></tr><tr><td>2</td><td>1</td><td>$10</td></tr><tr><td>3</td><td>3</td><td>$20</td></tr><tr><td>4</td><td>2</td><td>$15</td></tr></table>

<table><tr><td rowspan=2 colspan=1>Max itemallowed</td><td rowspan=1 colspan=6>Max Weight</td></tr><tr><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>5</td></tr><tr><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>12</td><td rowspan=1 colspan=1>12</td><td rowspan=1 colspan=1>12</td><td rowspan=1 colspan=1>12</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>12</td><td rowspan=1 colspan=1>22</td><td rowspan=1 colspan=1>22</td><td rowspan=1 colspan=1>22</td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>12</td><td rowspan=1 colspan=1>22</td><td rowspan=1 colspan=1>30</td><td rowspan=1 colspan=1>32</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>15</td><td rowspan=1 colspan=1>25</td><td rowspan=1 colspan=1>30</td><td rowspan=1 colspan=1>37</td></tr></table>

????[???? $, w ] = \left\{ { \atop \operatorname* { m a x } \{ B [ k - 1 , w ] , ~ B [ k - 1 , w - w _ { k } ] + b _ { l } }  \right.$ if $w _ { k } > w$ ????} else

### Images:
- data\Design and Analysis of Algorithms\L07-DP\page_039\L07-DP_page_039\auto\images\051bd8bcbecef961ecfaf11c93385be50b496194fb39134815b13911a6eb95d7.jpg
- data\Design and Analysis of Algorithms\L07-DP\page_039\L07-DP_page_039\auto\images\0648c0a58847a60341b21be163359dc8cbe11b55c18616685944b9a1eff6f56a.jpg
- data\Design and Analysis of Algorithms\L07-DP\page_039\L07-DP_page_039\auto\images\dabdff15bd996e6e8e971702a8fc6d60e21d7d5e56f09b3bb1e0695c60acee42.jpg
- data\Design and Analysis of Algorithms\L07-DP\page_039\L07-DP_page_039\auto\images\e4ae247735e9e1ac05d4c3b265930941f4cfd6a74d91918b3c42ad08f3416a42.jpg

---

## Lecture: L07-DP\page_040\L07-DP_page_040\auto

• Since B $[ \mathsf { k } , \mathsf { w } ]$ is defined in terms of B[k−1,\*], we can use two arrays of instead of a matrix.

• Running time is O(nW).

# Algorithm

Input: set $s$ of $n$ items with benefit $b _ { i }$   
and weight $w _ { i } { \dot { , } }$ maximum weight $W$   
Output: benefit of best subset of $s$ with weight at most $W$   
let $A$ and $\ b { B }$ be arrays of length $W + 1$   
for $w  0$ to $W$ do $B [ w ]  0$   
for $k \gets 1$ to n do copy array $B$ into array $A$ for $w  w _ { k }$ to $W$ do if $A [ \mathbb { W } - \mathbb { W } _ { k } ] + b _ { k } > A [ \mathbb { W } ]$   
then $B [ w ]  A [ w - w _ { k } ] + b _ { k }$   
return B[W]

• Not a polynomial-time algorithm since W may be large.

• Called a pseudo-polynomial time algorithm.

### Images:
- data\Design and Analysis of Algorithms\L07-DP\page_040\L07-DP_page_040\auto\images\6b3d37b4ab4a1d96f945c9191f9edba1fbce414183a211e939bf0077fe540523.jpg

---

## Lecture: L08-DP\page_001\L08-DP_page_001\auto

# Dynamic Programming (1)

Longest common subsequence Independent sets in trees Balanced partition problem

---

## Lecture: L08-DP\page_002\L08-DP_page_002\auto

# 5min Warm-up: Minimum Coins

• Problem Statement:

– You are given: A list of coins: coins $=$ [1, 2, 5]   
– A total amount: amount $= \textsf { X }$   
– Find the minimum number of coins needed to make up that amount. If it's not possible to form the amount, return -1.

---

## Lecture: L08-DP\page_003\L08-DP_page_003\auto

# Last time

• Dynamic programming is an algorithm design paradigm.

• Basic idea: – Identify optimal sub-structure Optimum to the big problem is built out of optima of small sub-problems – Take advantage of overlapping sub-problems • Only solve each sub-problem once, then use it again and again – Keep track of the solutions to sub-problems in a table as you build solution.

---

## Lecture: L08-DP\page_004\L08-DP_page_004\auto

# The goal of this lecture

• For you to get really bored of dynamic programming

![](images/4f0afb12b6972c78e705bbace2bcfa0f055435295454901764219c98054a222d.jpg)

### Images:
- data\Design and Analysis of Algorithms\L08-DP\page_004\L08-DP_page_004\auto\images\4f0afb12b6972c78e705bbace2bcfa0f055435295454901764219c98054a222d.jpg

---

## Lecture: L08-DP\page_005\L08-DP_page_005\auto

# Longest Common Subsequence (LCS)

• A subsequence of a sequence/string S is obtained by deleting zero or more symbols from S.

• For example, the following are some subsequences of “president”: pred, sdn, predent. In other words, the letters of a subsequence of S appear in order in S, but they are not required to be consecutive.

• The longest common subsequence problem is to find a maximum length common subsequence between two sequences.

---

## Lecture: L08-DP\page_006\L08-DP_page_006\auto

# Longest Common Subsequence

• How similar are these two species?

![](images/5c01931be8d92dc1191e99794569b79b2ba546194ecd09389dcd9e214a284780.jpg)

![](images/f8a4263891407b21f5bbff581996cfad94a09043bd618125022edad4bcbc1eec.jpg)

DNA: AGCCCTAAGGGCTACCTAGCTT GACAGCCTACAAGCGTTAGCTTG

Pretty similar, their DNA has a long common subsequence: AGCCTAAGCTTAGCTT

### Images:
- data\Design and Analysis of Algorithms\L08-DP\page_006\L08-DP_page_006\auto\images\5c01931be8d92dc1191e99794569b79b2ba546194ecd09389dcd9e214a284780.jpg
- data\Design and Analysis of Algorithms\L08-DP\page_006\L08-DP_page_006\auto\images\f8a4263891407b21f5bbff581996cfad94a09043bd618125022edad4bcbc1eec.jpg

---

## Lecture: L08-DP\page_007\L08-DP_page_007\auto

# Longest Common Subsequence

• Subsequence: BDFH is a subsequence of ABCDEFGH

• If X and Y are sequences, a common subsequence is a sequence which is a subsequence of both.

– BDFH is a common subsequence of ABCDEFGH and of ABDFGHI

• A longest common subsequence…

– …is a common subsequence that is longest.   
– The longest common subsequence of ABCDEFGH and ABDFGHI is ABDFGH.

---

## Lecture: L08-DP\page_008\L08-DP_page_008\auto

# We sometimes want to find these

• Applications in bioinformatics

![](images/ec70d5022c47ea6cb04794741c771a592ef9e76a479c6459278c4800addb98c7.jpg)

![](images/700442dbf3a1af81e76a0d986d4720f5c4e4e120d2ad958754d064364ab990c9.jpg)

• The unix command diff

• Merging in version control – svn, git, etc…

![](images/465577e4f1d0bea4ac6e0aaac8487c4ec17bc1eeadc1de75c910dbe1dce185f1.jpg)

### Images:
- data\Design and Analysis of Algorithms\L08-DP\page_008\L08-DP_page_008\auto\images\465577e4f1d0bea4ac6e0aaac8487c4ec17bc1eeadc1de75c910dbe1dce185f1.jpg
- data\Design and Analysis of Algorithms\L08-DP\page_008\L08-DP_page_008\auto\images\700442dbf3a1af81e76a0d986d4720f5c4e4e120d2ad958754d064364ab990c9.jpg
- data\Design and Analysis of Algorithms\L08-DP\page_008\L08-DP_page_008\auto\images\ec70d5022c47ea6cb04794741c771a592ef9e76a479c6459278c4800addb98c7.jpg

---

## Lecture: L08-DP\page_009\L08-DP_page_009\auto

# Recipe for applying Dynamic Programming

• Step 1: Identify optimal substructure.

![](images/3fb2bc1c4760c552316b3dd0b879781c3c1f529db23c9eceeb1a7aa35deee226.jpg)

• Step 2: Find a recursive formulation for the length of the longest common subsequence.

Step 3: Use dynamic programming to find the length of the longest common subsequence.

• Step 4: If needed, keep track of some additional info so that the algorithm from Step 3 can find the actual LCS.

• Step 5: If needed, code this up like a reasonable person.

### Images:
- data\Design and Analysis of Algorithms\L08-DP\page_009\L08-DP_page_009\auto\images\3fb2bc1c4760c552316b3dd0b879781c3c1f529db23c9eceeb1a7aa35deee226.jpg

---

## Lecture: L08-DP\page_010\L08-DP_page_010\auto

# Step 1: Optimal substructure

Prefixes:

![](images/8b0324ee383636de2a5d0cbbf4c60dd9aad4f77bb58ca443d5dfef9389ca7929.jpg)

Notation: denote this prefix ACGC by $\Upsilon _ { 4 }$

• Our sub-problems will be finding LCS’s of prefixes to X and Y. • Let C[i,j] $=$ length_of_LCS( Xi, Yj )

Examples: C[2,3] = 2 $\cdot 1 4 . 4 . 5 .$

### Images:
- data\Design and Analysis of Algorithms\L08-DP\page_010\L08-DP_page_010\auto\images\8b0324ee383636de2a5d0cbbf4c60dd9aad4f77bb58ca443d5dfef9389ca7929.jpg

---

## Lecture: L08-DP\page_011\L08-DP_page_011\auto

# Recipe for applying Dynamic Programming

• Step 1: Identify optimal substructure.

• Step 2: Find a recursive formulation for the length of the longest common subsequence.

Step 3: Use dynamic programming to find the length of the longest common subsequence.

• Step 4: If needed, keep track of some additional info so that the algorithm from Step 3 can find the actual LCS.

• Step 5: If needed, code this up like a reasonable person.

---

## Lecture: L08-DP\page_012\L08-DP_page_012\auto

• Write C[i,j] in terms of the solutions to smaller sub-problems

![](images/471d1142bc9c5ddc4d009c1cfa6ca17d07086f0c6cd041506a30e3a14d0c21ef.jpg)

C[i,j] = length_of_LCS( Xi, Yj )

### Images:
- data\Design and Analysis of Algorithms\L08-DP\page_012\L08-DP_page_012\auto\images\471d1142bc9c5ddc4d009c1cfa6ca17d07086f0c6cd041506a30e3a14d0c21ef.jpg

---

## Lecture: L08-DP\page_013\L08-DP_page_013\auto

Case 1: X[i] = Y[j]

![](images/0f06cd82faba3dda04d06ef28f008a7155ace12f5baaf2c27f38b5d1973111a4.jpg)

• Our sub-problems will be finding LCS’s of prefixes to X and Y. • Let C[i,j] $=$ length_of_LCS( Xi, Yj )

Then $\mathsf { C } [ \mathsf { i } , \mathsf { j } ] = 1 + \mathsf { C } [ \mathsf { i } - 1 , \mathsf { j } - 1 ] .$ • because $\begin{array} { r l r } { \mathrm { ~  ~ \omega ~ } } & { { } = } & { \delta ( \omega _ { 1 } , \omega _ { 1 } ) = \frac { \Gamma _ { 1 } } { \Gamma _ { 1 } } } \end{array}$ followed by

A

### Images:
- data\Design and Analysis of Algorithms\L08-DP\page_013\L08-DP_page_013\auto\images\0f06cd82faba3dda04d06ef28f008a7155ace12f5baaf2c27f38b5d1973111a4.jpg

---

## Lecture: L08-DP\page_014\L08-DP_page_014\auto

Case 2: X[i] != Y[j]

![](images/8523bf6a58f9880dda6a2a31863308fefff9c692e64decafd1eb7be4035f4631.jpg)

Our sub-problems will be finding LCS’s of prefixes to X and Y. • Let C[i,j] $=$ length_of_LCS( Xi, Yj )

Then $\mathsf { C } [ \mathsf { i } , \mathsf { j } ] = \mathsf { m a x } \{ \mathsf { C } [ \mathsf { i } - 1 , \mathsf { j } ] , \mathsf { C } [ \mathsf { i } , \mathsf { j } - 1 ] \} .$

• either $\mathsf { L C S } ( \mathsf X _ { \mathrm { i } } , \mathsf Y _ { \mathrm { j } } ) = \mathsf { L C S } ( \mathsf X _ { \mathrm { i - 1 } } , \mathsf Y _ { \mathrm { j } } )$ and T is not involved, or $\lfloor \mathbf { C S } ( \mathsf { X } _ { \mathrm { i } } , \mathsf { Y } _ { \mathrm { j } } ) = \lfloor \mathbf { C S } ( \mathsf { X } _ { \mathrm { i } } , \mathsf { Y } _ { \mathrm { j - 1 } } )$ and is not involved,A (maybe both are not involved, that’s covered by the “or”).

### Images:
- data\Design and Analysis of Algorithms\L08-DP\page_014\L08-DP_page_014\auto\images\8523bf6a58f9880dda6a2a31863308fefff9c692e64decafd1eb7be4035f4631.jpg

---

## Lecture: L08-DP\page_015\L08-DP_page_015\auto

# Recursive formulation of the optimal solution

![](images/20bf70190e549a15fb011a87c9a8964e96231d6071fe8bf9727d1d74c896d375.jpg)

### Images:
- data\Design and Analysis of Algorithms\L08-DP\page_015\L08-DP_page_015\auto\images\20bf70190e549a15fb011a87c9a8964e96231d6071fe8bf9727d1d74c896d375.jpg

---

## Lecture: L08-DP\page_016\L08-DP_page_016\auto

# Recipe for applying Dynamic Programming

• Step 1: Identify optimal substructure.

• Step 2: Find a recursive formulation for the length of the longest common subsequence.

![](images/0381e28155d43b4748d01a8aa01625e08989eef05edea1904fd4f02bfac11f7d.jpg)

Step 3: Use dynamic programming to find the length of the longest common subsequence.

• Step 4: If needed, keep track of some additional info so that the algorithm from Step 3 can find the actual LCS.

• Step 5: If needed, code this up like a reasonable person.

### Images:
- data\Design and Analysis of Algorithms\L08-DP\page_016\L08-DP_page_016\auto\images\0381e28155d43b4748d01a8aa01625e08989eef05edea1904fd4f02bfac11f7d.jpg

---

## Lecture: L08-DP\page_017\L08-DP_page_017\auto

# LCS DP

• LCS(X, Y): $- \mathbb { C } [ \mathsf { i } , 0 ] = \mathbb { C } [ 0 , \mathsf { j } ] = 0$ for all i = 0,…,m, j=0,…n. $- \mathsf { F o r i } = 1 , . . . , \mathsf { m a n d j } = 1 , . . . , \mathsf { n } \colon$ If X[i] = Y[j]: $- \mathsf { C } [ \mathsf { i } , \mathsf { j } ] = \mathsf { C } [ \mathsf { i } - 1 , \mathsf { j } - 1 ] \ + \ 1$ Else: $- \mathbb { C } [ \bar { \mathsf { i } } , \bar { \mathsf { j } } ] = \mathsf { m a x } \{ \mathbb { C } [ \bar { \mathsf { i } } , \bar { \mathsf { j } } - \underline { { 1 } } ] , \mathbb { C } [ \bar { \mathsf { i } } - \underline { { 1 } } , \bar { \mathsf { j } } ] \}$ – Return C[m,n]

$$
C [ i , j ] = \left\{ C [ i - 1 , j - 1 ] + 1 \quad \begin{array} { c l } { { \mathrm { i f ~ } i = 0 \mathrm { ~ o r ~ } j = 0 } } & { { } } \\ { { { \cal C } [ i - 1 , j - 1 ] + 1 } } & { { \mathrm { i f ~ } X [ i ] = Y [ j ] \mathrm { ~ a n d } } } \\ { { \operatorname* { m a x } \{ C [ i , j - 1 ] , C [ i - 1 , j ] \} } } & { { \mathrm { i f ~ } X [ i ] \neq Y [ j ] \mathrm { ~ a n d } } } \end{array} \right.
$$

### Images:
- data\Design and Analysis of Algorithms\L08-DP\page_017\L08-DP_page_017\auto\images\1192b34983262395e61e80f3c58da0506cdbacda0657e45562ee86a0cead4e18.jpg
- data\Design and Analysis of Algorithms\L08-DP\page_017\L08-DP_page_017\auto\images\673d493c17d2ba49812321d2407f131b94b526f04dc1fe6048a6225f199dbac5.jpg
- data\Design and Analysis of Algorithms\L08-DP\page_017\L08-DP_page_017\auto\images\695beb92780e00f6618902a1e9bfb4584fc6117b065bb59972c4d2239e0f720c.jpg
- data\Design and Analysis of Algorithms\L08-DP\page_017\L08-DP_page_017\auto\images\ef9f1a18ad9dd32d6db878721d98dc7999197f9ecd374c796e3bef845140ff3a.jpg

---

## Lecture: L08-DP\page_018\L08-DP_page_018\auto

![](images/50b17f104c949a7ea05241fdf43c2128d63fb806a8d803254c2903d91717e6c3.jpg)

![](images/4a5188e4a6f7301a0b4db45e9a6ce832f8c0107ea04236c433174f40aa8590fd.jpg)

if $i = 0 \mathrm { o r } j = 0$ if $X [ i ] = Y [ j ]$ and $i , j > 0$ $4 \times 1 1 1 = 4 8 1 1$ and $\cdot$

![](images/a5a77a09b92c0d17eb2552534385a7b1d6e022017c6046c3c07c9d6de7a5db4b.jpg)

![](images/1b88b3da546e45575abc9f098d43eabb222b876801397382bfdc2595bd8c4ea9.jpg)

### Images:
- data\Design and Analysis of Algorithms\L08-DP\page_018\L08-DP_page_018\auto\images\1b88b3da546e45575abc9f098d43eabb222b876801397382bfdc2595bd8c4ea9.jpg
- data\Design and Analysis of Algorithms\L08-DP\page_018\L08-DP_page_018\auto\images\4a5188e4a6f7301a0b4db45e9a6ce832f8c0107ea04236c433174f40aa8590fd.jpg
- data\Design and Analysis of Algorithms\L08-DP\page_018\L08-DP_page_018\auto\images\50b17f104c949a7ea05241fdf43c2128d63fb806a8d803254c2903d91717e6c3.jpg
- data\Design and Analysis of Algorithms\L08-DP\page_018\L08-DP_page_018\auto\images\a5a77a09b92c0d17eb2552534385a7b1d6e022017c6046c3c07c9d6de7a5db4b.jpg

---

## Lecture: L08-DP\page_019\L08-DP_page_019\auto

![](images/7a0bcd032db4d0451a4d61623258178553657a593b7a8752c3c78ef22f49bbc5.jpg)

![](images/5b57f554ef5b6aa9965a8d7da660ac4fd3433cadd950569e895205edd8f17e42.jpg)

???? ????, ???? = � ???? ???? − 1, ???? − 1 + 1 max ???? ????, ???? − 1 , ???? ???? − 1, ????

if $i = 0 \mathrm { o r } j = 0$ if $X [ i ] = Y [ j ]$ and $i , j > 0$ ${ \mathrm { i f } } X [ i ] \neq Y [ j ]$ and $\cdot$

![](images/2db7610aeef52e8a387bf30fa99c7a289e22ebf4edd424b7211c044d8cbd88fb.jpg)

So the LCS of X and Y has length 3.

### Images:
- data\Design and Analysis of Algorithms\L08-DP\page_019\L08-DP_page_019\auto\images\2db7610aeef52e8a387bf30fa99c7a289e22ebf4edd424b7211c044d8cbd88fb.jpg
- data\Design and Analysis of Algorithms\L08-DP\page_019\L08-DP_page_019\auto\images\5b57f554ef5b6aa9965a8d7da660ac4fd3433cadd950569e895205edd8f17e42.jpg
- data\Design and Analysis of Algorithms\L08-DP\page_019\L08-DP_page_019\auto\images\7a0bcd032db4d0451a4d61623258178553657a593b7a8752c3c78ef22f49bbc5.jpg

---

## Lecture: L08-DP\page_020\L08-DP_page_020\auto

# Recipe for applying Dynamic Programming

• Step 1: Identify optimal substructure.

• Step 2: Find a recursive formulation for the length of the longest common subsequence.

• Step 3: Use dynamic programming to find the length of the longest common subsequence.

![](images/e03419c8dcbb560755f70e4180596f5d3d1e39d5e37ef9866ea7fae349a4c1f9.jpg)

• Step 4: If needed, keep track of some additional info so that the algorithm from Step 3 can find the actual LCS.

• Step 5: If needed, code this up like a reasonable person.

### Images:
- data\Design and Analysis of Algorithms\L08-DP\page_020\L08-DP_page_020\auto\images\e03419c8dcbb560755f70e4180596f5d3d1e39d5e37ef9866ea7fae349a4c1f9.jpg

---

## Lecture: L08-DP\page_021\L08-DP_page_021\auto

# Example

???? ????, ???? = � ???? ???? − 1, ???? − 1 + 1 max ???? ????, ???? − 1 , ???? ???? − 1, ????

if $i = 0 \mathrm { o r } j = 0$ if $X [ i ] = Y [ j ]$ and $i , j > 0$ ${ \mathrm { i f } } X [ i ] \neq Y [ j ]$ and $\cdot$

![](images/f71b109697f4dec89e94969f0ac701b2b5f2ea401aafed47cd77d0ae80c279cf.jpg)

![](images/9695f1e77391984a17e017a780be22bc48216e092e021725a69f6658d364705e.jpg)

![](images/acb741616f540dec1f0182bbed36548e28ef07014a2b2a37e3c44c0692ec3cfc.jpg)

### Images:
- data\Design and Analysis of Algorithms\L08-DP\page_021\L08-DP_page_021\auto\images\9695f1e77391984a17e017a780be22bc48216e092e021725a69f6658d364705e.jpg
- data\Design and Analysis of Algorithms\L08-DP\page_021\L08-DP_page_021\auto\images\acb741616f540dec1f0182bbed36548e28ef07014a2b2a37e3c44c0692ec3cfc.jpg
- data\Design and Analysis of Algorithms\L08-DP\page_021\L08-DP_page_021\auto\images\f71b109697f4dec89e94969f0ac701b2b5f2ea401aafed47cd77d0ae80c279cf.jpg

---

## Lecture: L08-DP\page_022\L08-DP_page_022\auto

# Example

???? ????, ???? = � ???? ???? − 1, ???? − 1 + 1 max ???? ????, ???? − 1 , ???? ???? − 1, ????

if $i = 0 \mathrm { o r } j = 0$ if $X [ i ] = Y [ j ]$ and $i , j > 0$ $4 \times 1 1 1 = 4 8 1 1$ and $i , j > 0$

![](images/f8bed1db46d9a11a507954e954351368b65a00f44b0a0123142cbbafe414b148.jpg)

![](images/64291325b49bc690133a6bd4cd11144cd593850a3708ba1573e345c162c0daad.jpg)

![](images/5d67f335782e705754529581fb1aab115278750f644475b3ecb32967399a11de.jpg)

Once we’ve filled this in, we can work backwards.

### Images:
- data\Design and Analysis of Algorithms\L08-DP\page_022\L08-DP_page_022\auto\images\5d67f335782e705754529581fb1aab115278750f644475b3ecb32967399a11de.jpg
- data\Design and Analysis of Algorithms\L08-DP\page_022\L08-DP_page_022\auto\images\64291325b49bc690133a6bd4cd11144cd593850a3708ba1573e345c162c0daad.jpg
- data\Design and Analysis of Algorithms\L08-DP\page_022\L08-DP_page_022\auto\images\f8bed1db46d9a11a507954e954351368b65a00f44b0a0123142cbbafe414b148.jpg

---

## Lecture: L08-DP\page_023\L08-DP_page_023\auto

# Example

???? ????, ???? = � ???? ???? − 1, ???? − 1 + 1 max ???? ????, ???? − 1 , ???? ???? − 1, ????

if $i = 0 \mathrm { o r } j = 0$ if $X [ i ] = Y [ j ]$ and $i , j > 0$ ${ \mathrm { i f } } X [ i ] \neq Y [ j ]$ and $i , j > 0$

![](images/947baa1b2f7700d842dc9517cca09330fa03fc192512c8f5edd6101ecb3215cb.jpg)

![](images/fb72526293c5378048d37e9b99dd5c9b9d5062b49369585b24f66a1e5548a1e9.jpg)

![](images/efa253119b6468d589fd7feb5943f33b71e8eef72b7ad05de6cde241dad77c8e.jpg)

Once we’ve filled this in, we can work backwards.

That 3 must have come from the 3 above it.

### Images:
- data\Design and Analysis of Algorithms\L08-DP\page_023\L08-DP_page_023\auto\images\947baa1b2f7700d842dc9517cca09330fa03fc192512c8f5edd6101ecb3215cb.jpg
- data\Design and Analysis of Algorithms\L08-DP\page_023\L08-DP_page_023\auto\images\efa253119b6468d589fd7feb5943f33b71e8eef72b7ad05de6cde241dad77c8e.jpg
- data\Design and Analysis of Algorithms\L08-DP\page_023\L08-DP_page_023\auto\images\fb72526293c5378048d37e9b99dd5c9b9d5062b49369585b24f66a1e5548a1e9.jpg

---

## Lecture: L08-DP\page_024\L08-DP_page_024\auto

# Example

???? ????, ???? = � ???? ???? − 1, ???? − 1 + 1 max ???? ????, ???? − 1 , ???? ???? − 1, ????

if $i = 0 \mathrm { o r } j = 0$ if $X [ i ] = Y [ j ]$ and $i , j > 0$ ${ \mathrm { i f } } X [ i ] \neq Y [ j ]$ and $i , j > 0$

![](images/3174c3931314887f31b659e492f8c28eb075225f81e683aa51b4b9e1a1834281.jpg)

![](images/4530827db0a7b2206d7dfa5f739c847c4c205e1ebb748141898aff04dc417465.jpg)

![](images/32a510f47bfd9aa80443ece4ac5fe8f841a02e82a4aef7a39c950fda25481e15.jpg)

![](images/9a538da880d155f505ecc8ede44ef6ad5299220d648e801c001b4b1fb395e9a6.jpg)

Once we’ve filled this in, we can work backwards.

• A diagonal jump means that we found an element of the LCS!

This 3 came from that 2 – we found a match!

![](images/96a3ecc396e2ce6550226ad3b77e470d9a6e36e490c123b7cac9f755375baef7.jpg)

### Images:
- data\Design and Analysis of Algorithms\L08-DP\page_024\L08-DP_page_024\auto\images\3174c3931314887f31b659e492f8c28eb075225f81e683aa51b4b9e1a1834281.jpg
- data\Design and Analysis of Algorithms\L08-DP\page_024\L08-DP_page_024\auto\images\32a510f47bfd9aa80443ece4ac5fe8f841a02e82a4aef7a39c950fda25481e15.jpg
- data\Design and Analysis of Algorithms\L08-DP\page_024\L08-DP_page_024\auto\images\4530827db0a7b2206d7dfa5f739c847c4c205e1ebb748141898aff04dc417465.jpg
- data\Design and Analysis of Algorithms\L08-DP\page_024\L08-DP_page_024\auto\images\96a3ecc396e2ce6550226ad3b77e470d9a6e36e490c123b7cac9f755375baef7.jpg
- data\Design and Analysis of Algorithms\L08-DP\page_024\L08-DP_page_024\auto\images\9a538da880d155f505ecc8ede44ef6ad5299220d648e801c001b4b1fb395e9a6.jpg

---

## Lecture: L08-DP\page_025\L08-DP_page_025\auto

# Example

???? ????, ???? = � ???? ???? − 1, ???? − 1 + 1 max ???? ????, ???? − 1 , ???? ???? − 1, ????

if $i = 0 \mathrm { o r } j = 0$ if $X [ i ] = Y [ j ]$ and $i , j > 0$ ${ \mathrm { i f } } X [ i ] \neq Y [ j ]$ and $\cdot$

![](images/cdffbe05c9fff353dd6159680316c0b33e61028b9036cc6a4b5474e496ab1ea8.jpg)

![](images/650df3fe0af9bcf534def75fa74d7c449475b63c309a01d5bd9bbb219cfc676f.jpg)

![](images/e3be174397c5b989ac002bd1dc41c663f6c7793dbaaab74145cbee54f3978b3c.jpg)

![](images/b79a592eb28143bb706e60f787122fadbba15fa47ab90a67a569cd5357fa5dca.jpg)

Once we’ve filled this in, we can work backwards.

A diagonal jump means that we found an element of the LCS!

That 2 may as well have come from this other 2.

G

### Images:
- data\Design and Analysis of Algorithms\L08-DP\page_025\L08-DP_page_025\auto\images\650df3fe0af9bcf534def75fa74d7c449475b63c309a01d5bd9bbb219cfc676f.jpg
- data\Design and Analysis of Algorithms\L08-DP\page_025\L08-DP_page_025\auto\images\b79a592eb28143bb706e60f787122fadbba15fa47ab90a67a569cd5357fa5dca.jpg
- data\Design and Analysis of Algorithms\L08-DP\page_025\L08-DP_page_025\auto\images\cdffbe05c9fff353dd6159680316c0b33e61028b9036cc6a4b5474e496ab1ea8.jpg
- data\Design and Analysis of Algorithms\L08-DP\page_025\L08-DP_page_025\auto\images\e3be174397c5b989ac002bd1dc41c663f6c7793dbaaab74145cbee54f3978b3c.jpg

---

## Lecture: L08-DP\page_026\L08-DP_page_026\auto

# Example

???? ????, ???? = � ???? ???? − 1, ???? − 1 + 1 max ???? ????, ???? − 1 , ???? ???? − 1, ????

if $i = 0 \mathrm { o r } j = 0$ if $X [ i ] = Y [ j ]$ and $i , j > 0$ $4 \times 1 1 1 = 4 8 1 1$ and $\cdot$

![](images/261f55010d1bb024c4fd3154aa35a7cd605438dc592371b33309d4b9e04ef220.jpg)

![](images/a5ab94d40c790e2f3169cf1a5860f80f2da536c21a8e91de68e403f871744e75.jpg)

![](images/ac12b822d6a7b0d1292f512fb05376c0ccf11c1f98c1a27c3b92d015f023a6bb.jpg)

![](images/8e1603b8b3f192a4c1a77fbd4587e801457523e9265ab3ed909e2070acc802a3.jpg)

Once we’ve filled this in, we can work backwards.

A diagonal jump means that we found an element of the LCS!

![](images/ac0db7be6fa26eba59ed1c14b4f3eb3c1b6b0260fe6f9e5d0c2dd1cfaf9d8616.jpg)

### Images:
- data\Design and Analysis of Algorithms\L08-DP\page_026\L08-DP_page_026\auto\images\261f55010d1bb024c4fd3154aa35a7cd605438dc592371b33309d4b9e04ef220.jpg
- data\Design and Analysis of Algorithms\L08-DP\page_026\L08-DP_page_026\auto\images\8e1603b8b3f192a4c1a77fbd4587e801457523e9265ab3ed909e2070acc802a3.jpg
- data\Design and Analysis of Algorithms\L08-DP\page_026\L08-DP_page_026\auto\images\a5ab94d40c790e2f3169cf1a5860f80f2da536c21a8e91de68e403f871744e75.jpg
- data\Design and Analysis of Algorithms\L08-DP\page_026\L08-DP_page_026\auto\images\ac0db7be6fa26eba59ed1c14b4f3eb3c1b6b0260fe6f9e5d0c2dd1cfaf9d8616.jpg
- data\Design and Analysis of Algorithms\L08-DP\page_026\L08-DP_page_026\auto\images\ac12b822d6a7b0d1292f512fb05376c0ccf11c1f98c1a27c3b92d015f023a6bb.jpg

---

## Lecture: L08-DP\page_027\L08-DP_page_027\auto

# Example

???? ????, ???? = � ???? ???? − 1, ???? − 1 + 1 max ???? ????, ???? − 1 , ???? ???? − 1, ????

if $i = 0 \mathrm { o r } j = 0$ if $X [ i ] = Y [ j ]$ and $i , j > 0$ $4 \times 1 1 1 = 4 8 1 1$ and $\cdot$

![](images/046f4da56efab0879ef89b92db0f33593f5842de701c7112839727346a8ad6bc.jpg)

![](images/a465314c16e884a8ecff8856d8f38708d29011ddf013a130698051a6c83f0e25.jpg)

![](images/563ceb26c97aa9f4659d68cfa54f1444aee42ee73f077aa57deed74632c211f6.jpg)

![](images/bc239f1eff6870d569cacb46cbaea3b62127b4ddb382c78dcdc2e09bb9837204.jpg)

Once we’ve filled this in, we can work backwards.

A diagonal jump means that we found an element of the LCS!

![](images/c12e102a19059b8effa14e40f57ebd24751cf695f15b8841be6a46cbecd182af.jpg)

### Images:
- data\Design and Analysis of Algorithms\L08-DP\page_027\L08-DP_page_027\auto\images\046f4da56efab0879ef89b92db0f33593f5842de701c7112839727346a8ad6bc.jpg
- data\Design and Analysis of Algorithms\L08-DP\page_027\L08-DP_page_027\auto\images\563ceb26c97aa9f4659d68cfa54f1444aee42ee73f077aa57deed74632c211f6.jpg
- data\Design and Analysis of Algorithms\L08-DP\page_027\L08-DP_page_027\auto\images\a465314c16e884a8ecff8856d8f38708d29011ddf013a130698051a6c83f0e25.jpg
- data\Design and Analysis of Algorithms\L08-DP\page_027\L08-DP_page_027\auto\images\bc239f1eff6870d569cacb46cbaea3b62127b4ddb382c78dcdc2e09bb9837204.jpg
- data\Design and Analysis of Algorithms\L08-DP\page_027\L08-DP_page_027\auto\images\c12e102a19059b8effa14e40f57ebd24751cf695f15b8841be6a46cbecd182af.jpg

---

## Lecture: L08-DP\page_028\L08-DP_page_028\auto

# Example

???? ????, ???? = � ???? ???? − 1, ???? − 1 + 1 max ???? ????, ???? − 1 , ???? ???? − 1, ????

if $i = 0 \ : \mathrm { o r } \ : j = 0 \ :$ if $X [ i ] = Y [ j ]$ and $i , j > 0$ $4 \times 1 1 1 = 4 8 ( c m ^ { 2 } )$ and $i , j > 0$

![](images/ddc00e4ffa8ed55ef68c902c84219bd9243aace5fc83f186c138984ae49f836a.jpg)

![](images/8316c9d22fdabeaf10277cff8b3feaf9284e9a3bf685272050d44f770a96edf5.jpg)

![](images/82fac2bab72a93fe866ddc1f7ecfdf0362696acc302aa180197a723712ef802d.jpg)

![](images/d8c80f96ed1e2c2370b774789a1d058e8b353ead6601e4124dd77adf8643a6f9.jpg)

Once we’ve filled this in, we can work backwards.

A diagonal jump means that we found an element of the LCS!

![](images/63ac24d98d1ac990016c19da0c2bd0356bfb6c728a309f311745076bef66b43e.jpg)

This is the LCS!

### Images:
- data\Design and Analysis of Algorithms\L08-DP\page_028\L08-DP_page_028\auto\images\63ac24d98d1ac990016c19da0c2bd0356bfb6c728a309f311745076bef66b43e.jpg
- data\Design and Analysis of Algorithms\L08-DP\page_028\L08-DP_page_028\auto\images\82fac2bab72a93fe866ddc1f7ecfdf0362696acc302aa180197a723712ef802d.jpg
- data\Design and Analysis of Algorithms\L08-DP\page_028\L08-DP_page_028\auto\images\8316c9d22fdabeaf10277cff8b3feaf9284e9a3bf685272050d44f770a96edf5.jpg
- data\Design and Analysis of Algorithms\L08-DP\page_028\L08-DP_page_028\auto\images\d8c80f96ed1e2c2370b774789a1d058e8b353ead6601e4124dd77adf8643a6f9.jpg
- data\Design and Analysis of Algorithms\L08-DP\page_028\L08-DP_page_028\auto\images\ddc00e4ffa8ed55ef68c902c84219bd9243aace5fc83f186c138984ae49f836a.jpg

---

## Lecture: L08-DP\page_029\L08-DP_page_029\auto

# Finding an LCS

• Good exercise to write out pseudocode for what we just saw! Or you can find it in lecture notes.

• Takes time O(mn) to fill the table

• Takes time O(n + m) on top of that to recover the LCS We walk up and left in an n-by-m array – We can only do that for n + m steps.

• Altogether, we can find LCS(X,Y) in time O(mn).

---

## Lecture: L08-DP\page_030\L08-DP_page_030\auto

# Recipe for applying Dynamic Programming

• Step 1: Identify optimal substructure.

• Step 2: Find a recursive formulation for the length of the longest common subsequence.

• Step 3: Use dynamic programming to find the length of the longest common subsequence.

• Step 4: If needed, keep track of some additional info so that the algorithm from Step 3 can find the actual LCS.

![](images/f05a96989a9934ac806c372b25d450b4ec1917d783598b780bc7a4aea79b6875.jpg)

• Step 5: If needed, code this up like a reasonable person.

### Images:
- data\Design and Analysis of Algorithms\L08-DP\page_030\L08-DP_page_030\auto\images\f05a96989a9934ac806c372b25d450b4ec1917d783598b780bc7a4aea79b6875.jpg

---

## Lecture: L08-DP\page_031\L08-DP_page_031\auto

<table><tr><td>Input X</td><td>springtime</td></tr><tr><td>Input Y</td><td>printing</td></tr></table>

printi

LCS-LENGTH(X, Y) Execute LCS Length Sstep: ie nt no i- ${ } = 0$ =19,, $8 ] = 6$ $\mathrm { ~ i ~ } = \mathrm { ~ 1 ~ }$ See line number 13 and 14 4 do c[i，0] = 0 j 0 1 2 3 4 5 6 7 8 5 for j = i to n 6 do c[0，j] = 0 y p r nl t i n g 7 for $\mathrm { ~ \\\dot { ~ } ~ } = \mathrm { ~ \bf ~ 1 ~ }$ tom   
0 0 0 0 0 0 0 0 00 do for $\dot { \mathrm { ~ \scriptsize ~ j ~ } } = \mathrm { ~ \scriptsize ~ 1 ~ }$ $\mathbf { x } \mathbf { i _ { \lambda } } = = \mathbf { \lambda } \mathbf { y } \mathbf { j _ { \lambda } }$ 1 0^0^0↑0^0↑0↑0↑0↑0 then c[i,j] $=$ c[i-1, j-1] + 1   
2 p 01←1←1←1←1 ←1←1←1 elsebif,1 $=$ AR $> =$ CO, j−   
3 r 0^12←2←2←2←2←2←2 then c[i, $\scriptstyle { \dot { \mathsf { J } } } ] = \mathbf { c } [ { \dot { \mathsf { 1 } } } - { \mathsf { 1 } }$ ,j b[i，j] $=$ ARROW_UP   
4 0^1↑2<3←3←33←3←3 else c[i, j] ${ \mathsf { I } } = \mathbf { { c } } \left[ \mathbf { \Lambda } \right]$ i，j-1]   
5 n 0↑1↑2↑3 4←4←44←4 17return c and b b[i，j] $=$ ARROW_LEFT   
6 g 0↑1↑2↑3↑4↑4↑4↑4\~5 PRINT-LCS(b, x, i, j) Execute PRINT LCS t 0↑1↑2↑3↑4\~5←5←5↑5 1 if i=0 or $\dot { \mathsf { J } } = 0$ 7 2 then return   
8 0↑1↑23↑4↑56←6←6 3 if b[i, j] $= =$ ARROW_CORNER   
9 m 0↑1↑2↑3↑4↑5↑6↑6↑6 then pint -Ics(b, x, i-1, j−1)   
10 e 0↑1↑2↑3↑4↑5↑6↑6↑6 6 elseif b{i, j] $= =$ ARROW_UP 7 then PRINT-LcS(b, x, i-1, j)

### Images:
- data\Design and Analysis of Algorithms\L08-DP\page_031\L08-DP_page_031\auto\images\1be76ac9284936b287bd12651de32ffa2636d35fdfdae9d3a09edb9cd131b269.jpg
- data\Design and Analysis of Algorithms\L08-DP\page_031\L08-DP_page_031\auto\images\ac52659470f242436107adc7eb4d8dd939b52a26b1f6761b5a45c9b2dbef74c6.jpg

---

## Lecture: L08-DP\page_032\L08-DP_page_032\auto

# Our approach actually isn’t so bad

• If we are only interested in the length of the LCS we can do a bit better on space:

– Since we go across the table one-row-at-a-time, we can only keep two rows if we want.

• If we want to recover the LCS, we need to keep the whole table.

の Can we do better than O(mn) time? – A bit better. By a log factor or so. – Try to design it (as your lab work)!

---

## Lecture: L08-DP\page_033\L08-DP_page_033\auto

# What have we learned?

• We can find LCS(X,Y) in time O(nm) – if |Y|=n, |X|=m

• We went through the steps of coming up with a dynamic programming algorithm.

– We kept a 2-dimensional table, breaking down the problem by decrementing the length of X and Y.

---

## Lecture: L08-DP\page_034\L08-DP_page_034\auto

# Independent Set

![](images/976d02c1b95839599b984f08c49da715f6cb5b79b0f7af6f42c1cbf07f891a78.jpg)

### Images:
- data\Design and Analysis of Algorithms\L08-DP\page_034\L08-DP_page_034\auto\images\976d02c1b95839599b984f08c49da715f6cb5b79b0f7af6f42c1cbf07f891a78.jpg

---

## Lecture: L08-DP\page_035\L08-DP_page_035\auto

# Independent Set

• Actually, this problem is NP-complete. So, we are unlikely to find an efficient algorithm.

• But if we also assume that the graph is a tree…

![](images/f7d0bc50b9b024d32b84cef82d1718e27f10077cb55648e59dc1a92dbcce83b2.jpg)

find a maximal independent set in a tree (with vertex weights).

### Images:
- data\Design and Analysis of Algorithms\L08-DP\page_035\L08-DP_page_035\auto\images\f7d0bc50b9b024d32b84cef82d1718e27f10077cb55648e59dc1a92dbcce83b2.jpg

---

## Lecture: L08-DP\page_036\L08-DP_page_036\auto

# Recipe for applying Dynamic Programming

• Step 1: Identify optimal substructure.

![](images/5bcb08cdef2c0e8cf40a702052ca5b2f5ae55dbda2af435122ac648c98be06a4.jpg)

• Step 2: Find a recursive formulation for the value of the optimal solution

• Step 3: Use dynamic programming to find the value of the optimal solution

Step 4: If needed, keep track of some additional info so that the algorithm from Step 3 can find the actual solution.

• Step 5: If needed, code this up like a reasonable person.

### Images:
- data\Design and Analysis of Algorithms\L08-DP\page_036\L08-DP_page_036\auto\images\5bcb08cdef2c0e8cf40a702052ca5b2f5ae55dbda2af435122ac648c98be06a4.jpg

---

## Lecture: L08-DP\page_037\L08-DP_page_037\auto

# Optimal substructure

• Subtrees are a natural candidate.

• There are two cases:

1. The root of this tree is not in a maximal independent set.

2. Or it is.

![](images/b91849b19c1736632c2ea8a0dd4cca0f3060806e42b66cb44739d9eb7e1c1acb.jpg)

### Images:
- data\Design and Analysis of Algorithms\L08-DP\page_037\L08-DP_page_037\auto\images\b91849b19c1736632c2ea8a0dd4cca0f3060806e42b66cb44739d9eb7e1c1acb.jpg

---

## Lecture: L08-DP\page_038\L08-DP_page_038\auto

# Case 1: the root is not in a maximal independent set

• Use the optimal solution from these smaller problems.

![](images/2d20cdce31ad9673fda6a91b4fe1d9fb1c7044438e18e5272e6a668401d07d9c.jpg)

### Images:
- data\Design and Analysis of Algorithms\L08-DP\page_038\L08-DP_page_038\auto\images\2d20cdce31ad9673fda6a91b4fe1d9fb1c7044438e18e5272e6a668401d07d9c.jpg

---

## Lecture: L08-DP\page_039\L08-DP_page_039\auto

# Case 2 : the root is in an maximal independent set

• Then its children can’t be.

• Below that, use the optimal solution from

these smaller subproblems.

![](images/46a214d20186859c0e24ddcf587804e4356d541a6b270cffaf6f87ef70c09bf4.jpg)

### Images:
- data\Design and Analysis of Algorithms\L08-DP\page_039\L08-DP_page_039\auto\images\46a214d20186859c0e24ddcf587804e4356d541a6b270cffaf6f87ef70c09bf4.jpg

---

## Lecture: L08-DP\page_040\L08-DP_page_040\auto

# Recipe for applying Dynamic Programming

• Step 1: Identify optimal substructure.

• Step 2: Find a recursive formulation for the value of the optimal solution.

• Step 3: Use dynamic programming to find the value of the optimal solution

• Step 4: If needed, keep track of some additional info so that the algorithm from Step 3 can find the actual solution.

• Step 5: If needed, code this up like a reasonable person.

---

## Lecture: L08-DP\page_041\L08-DP_page_041\auto

# Recursive formulation: try 1

• Let A[u] be the weight of a maximal independent set in the tree rooted at u.

![](images/dd1f8d3a685dcf04a0671fff1cb7e92f47bbfe35a0a440d845bb5d18ab74d29a.jpg)

![](images/abc309a308f966da44ce41067751ea1c2ce7886a7327cf9a19bf17f1daf1dc3a.jpg)

When we implement this, how do we keep track of this term?

![](images/80a57abd8f4b82221effb3589d87b4a9f305ac004ca0eca86a7b8585ece2922f.jpg)

### Images:
- data\Design and Analysis of Algorithms\L08-DP\page_041\L08-DP_page_041\auto\images\80a57abd8f4b82221effb3589d87b4a9f305ac004ca0eca86a7b8585ece2922f.jpg
- data\Design and Analysis of Algorithms\L08-DP\page_041\L08-DP_page_041\auto\images\abc309a308f966da44ce41067751ea1c2ce7886a7327cf9a19bf17f1daf1dc3a.jpg
- data\Design and Analysis of Algorithms\L08-DP\page_041\L08-DP_page_041\auto\images\dd1f8d3a685dcf04a0671fff1cb7e92f47bbfe35a0a440d845bb5d18ab74d29a.jpg

---

## Lecture: L08-DP\page_042\L08-DP_page_042\auto

# Recursive formulation: try 2

# Keep two arrays!

• Let A[u] be the weight of a maximal independent set in the tree rooted at u.

• Let B[u ] = ∑????∈????.children ????[????]

$$
A [ u ] = \mathrm { m a x } \left\{ \begin{array} { r } { \sum _ { v \in u . \mathrm { c h i l d r e n } } A [ v ] } \\ { \qquad \ } \\ { \mathrm { w e i g h t } ( u ) + \sum _ { v \in u . \mathrm { c h i l d r e n } } \ } \end{array} \right.
$$

### Images:
- data\Design and Analysis of Algorithms\L08-DP\page_042\L08-DP_page_042\auto\images\0bb7a7c2c09bb6bfb71d5947d808fc1093c867601f230172fa6141f6173884f9.jpg
- data\Design and Analysis of Algorithms\L08-DP\page_042\L08-DP_page_042\auto\images\2f5e2a5a1e7e28a694c81df1f3b0bdfa9e3dab68827ffc8d70361ee2a29b442b.jpg
- data\Design and Analysis of Algorithms\L08-DP\page_042\L08-DP_page_042\auto\images\c7c22728b3b25ee279bd147aa6ee520cb3d351f9df041a49a62ffb49e180602d.jpg

---

## Lecture: L08-DP\page_043\L08-DP_page_043\auto

# Recipe for applying Dynamic Programming

• Step 1: Identify optimal substructure.

• Step 2: Find a recursive formulation for the value of the optimal solution.

• Step 3: Use dynamic programming to find the value of the optimal solution.

• Step 4: If needed, keep track of some additional info so that the algorithm from Step 3 can find the actual solution.

• Step 5: If needed, code this up like a reasonable person.

### Images:
- data\Design and Analysis of Algorithms\L08-DP\page_043\L08-DP_page_043\auto\images\4a1f8b2b84d08d6f8bfac35524bf354f7c8389b61aae12df714144d4380f1831.jpg

---

## Lecture: L08-DP\page_044\L08-DP_page_044\auto

# Dynamic Programming

• MIS_subtree(u):

– if u is a leaf:

$$
\mathsf { A } [ \mathsf { u } ] = \mathsf { w e i g h t } ( \mathsf { u } )
$$

• $\mathsf { B } [ \mathsf { u } ] = 0$ – else:

• for v in u.children: – MIS_subtree(v)   
• $A [ u ] = \operatorname* { m a x } \{$ { ∑????∈????.children ????[????] , weight ???? + ∑????∈????.children ????[????] } $\mathrm { B } [ u ] = \Sigma _ { 1 }$ ????∈????.children ????[????]

Initialize global arrays A, B that we will use in all of the recursive calls.

• MIS(T): – MIS_subtree(T.root) – return A[T.root]

# Running time?

We visit each vertex once, and for every vertex we do O(1) work:

Make a recursive call Participate in summations of parent node

Running time is O(|V|)

### Images:
- data\Design and Analysis of Algorithms\L08-DP\page_044\L08-DP_page_044\auto\images\ea9e5051a1b58cedb23ff6bbf4e3cc916a0e249969e21a8bfaa6e9a8083d05c9.jpg

---

## Lecture: L08-DP\page_045\L08-DP_page_045\auto

# Recipe for applying Dynamic Programming

• Step 1: Identify optimal substructure.

• Step 2: Find a recursive formulation for the value of the optimal solution.

• Step 3: Use dynamic programming to find the value of the optimal solution.

Step 4: If needed, keep track of some additional info so that the algorithm from Step 3 can find the actual solution.

You do this one!

• Step 5: If needed, code this up like a reasonable person.

### Images:
- data\Design and Analysis of Algorithms\L08-DP\page_045\L08-DP_page_045\auto\images\0d613f65a7949af04cbab05a17162785e0d10c7eb0fcd2a2e67d995ca5c73e8e.jpg

---

## Lecture: L08-DP\page_046\L08-DP_page_046\auto

# What have we learned?

• We can find maximal independent sets in trees in time O(|V|) using dynamic programming!

• For this example, it was natural to implement our DP algorithm in a top-down way.

---

## Lecture: L08-DP\page_047\L08-DP_page_047\auto

# Balanced Partition (BP) Problem

• We are given ???? integers $I = \{ k _ { 1 } , k _ { 2 } , . . . , k _ { n } \} , s . \mathsf { t } . 0 \leq k _ { i } \leq K .$

• We like to partition them into two sets $S _ { 1 }$ and $S _ { 2 }$ s.t. the difference ???? of the total sizes of the two sets is as small as possible

$$
\operatorname* { m i n } _ { S _ { 1 } , S _ { 2 } } d \ s . { \sf t } . d = \ \vert \ \sum _ { i \in S _ { 1 } } k _ { i } - \sum _ { \bf j \in S _ { 2 } } k _ { \bf j } \ \vert .
$$

$$
k _ { 1 } = 1 , k _ { 2 } = 3 , k _ { 3 } = 4 , k _ { 4 } = 6 , k _ { 5 } = 7
$$

![](images/cf6e05d6d6907718e6dc6e634e83bfe06ac65ccef2652de6599e6e79d8ebafe5.jpg)

$\left| ~ S _ { 1 } \right| ~ = ~ 1 0 ~ \left| ~ S _ { 2 } \right| ~ = ~ 1 1$ $d = \left| \ 1 0 - \ 1 1 \right| = 1$

### Images:
- data\Design and Analysis of Algorithms\L08-DP\page_047\L08-DP_page_047\auto\images\37800138f230c6b9b9d666224282478cc58841575a1eac81424baffd33442f9c.jpg
- data\Design and Analysis of Algorithms\L08-DP\page_047\L08-DP_page_047\auto\images\7ce0d6f6bc222f060eff8b7d4541041db24fbaf0a06556f8bc846bfe36bd69f0.jpg
- data\Design and Analysis of Algorithms\L08-DP\page_047\L08-DP_page_047\auto\images\912cc425b2578c6a854c3913ea76c564cd69192d4522f5aba44194bf845889df.jpg
- data\Design and Analysis of Algorithms\L08-DP\page_047\L08-DP_page_047\auto\images\9292e882efd81b6f3a8592f561333b942ec0467583568b45a249652200c52daa.jpg
- data\Design and Analysis of Algorithms\L08-DP\page_047\L08-DP_page_047\auto\images\cf6e05d6d6907718e6dc6e634e83bfe06ac65ccef2652de6599e6e79d8ebafe5.jpg
- data\Design and Analysis of Algorithms\L08-DP\page_047\L08-DP_page_047\auto\images\f19b1e38dfc28da8334979c48a7fc2ceceae0e9c4e4893d8a58eee87ad0960c5.jpg

---

## Lecture: L08-DP\page_048\L08-DP_page_048\auto

max item size

• Let ???? = ∑ ???? ≤ ????????.

• $m = 0$ : The best we can hope for is $| S _ { 1 } | = \left\lfloor { \frac { M } { 2 } } \right\rfloor - 0$ and ????2 = ???? − ????1.

---

## Lecture: L08-DP\page_049\L08-DP_page_049\auto

max item size

• Let $\begin{array} { r } { M = \sum _ { i } k _ { i } \le n K } \end{array}$ .

• $m = 0$ : The best we can hope for is $\begin{array} { r } { | S _ { 1 } | = ~ \overline { { \left\lfloor \frac { M } { 2 } \right\rfloor - 0 ~ \mathsf { a n d } ~ S _ { 2 } } } = ~ M - { S _ { 1 } } . } \end{array}$

• ???? = 1: If this is not possible, the next best is $\left| S _ { 1 } \right| = \left\lfloor { \frac { M } { 2 } } \right\rfloor - 1$ and $S _ { 2 } = M - S _ { 1 }$ .

---

## Lecture: L08-DP\page_050\L08-DP_page_050\auto

max item size

• Let $\begin{array} { r } { M = \sum _ { i } k _ { i } \le n K } \end{array}$ .

• $m = 0$ : The best we can hope for is $| S _ { 1 } | = \left\lfloor { \frac { M } { 2 } } \right\rfloor - 0$ and $S _ { 2 } = M - S _ { 1 }$ .

• ???? = 1: If this is not possible, the next best is $\left| S _ { 1 } \right| = \left\lfloor { \frac { M } { 2 } } \right\rfloor - 1$ and $S _ { 2 } = M - S _ { 1 }$ .

• ???? = 2: If this is not possible, the next best is ????1 = ????2 − 2 and $S _ { 2 } = M - S _ { 1 }$

• ???? = 3: If this is not possible, the next best is ????1 = ???? − 3 and $S _ { 2 } = M - S _ { 1 }$

• … try up to $m = \left\lfloor { \frac { M } { 2 } } \right\rfloor$ . This is always possible since we have $S _ { 1 } = \emptyset , S _ { 2 } = I .$ .

So, lets check the best we can achieve starting from $m = 0$ .

---

## Lecture: L08-DP\page_051\L08-DP_page_051\auto

# Example

![](images/c47d7ea896f9204c8d00c58d7cb0b535240c9ac4f5b4591d8e9318f9dbb4ba13.jpg)

????2

Given:

$$
M = 2 1 , ~ \left\lfloor { \frac { M } { 2 } } \right\rfloor = ~ 1 0
$$

### Images:
- data\Design and Analysis of Algorithms\L08-DP\page_051\L08-DP_page_051\auto\images\22821c556af8c88829d3a2fe0342eafbde5174b6685e68e0a4b715e27ac9460b.jpg
- data\Design and Analysis of Algorithms\L08-DP\page_051\L08-DP_page_051\auto\images\c47d7ea896f9204c8d00c58d7cb0b535240c9ac4f5b4591d8e9318f9dbb4ba13.jpg
- data\Design and Analysis of Algorithms\L08-DP\page_051\L08-DP_page_051\auto\images\f8eebe9359349749e73620849f64714970e432da9b3704ffdc991efb5e2deff2.jpg

---

## Lecture: L08-DP\page_052\L08-DP_page_052\auto

# eduction to the Subset sum Problem (SSP)

• We reduced BP to the problem SP:

• $S P [ n , D ]$ : We are given ???? integers $I = \{ k _ { 1 } , . . . , k _ { n } \} , s . t . 0 \leq k _ { i } \leq K _ { i }$ , and an integer $D \leq n K$ . Is there a subset $S$ of them such that $\textstyle \sum _ { i \in S } k _ { i } = D ?$ (True/False).

---

## Lecture: L08-DP\page_053\L08-DP_page_053\auto

# Reduction to the Subset Sum Problem (SSP)

• Solution of BP:

• Solve $B P$ by finding the smallest value of $= 0 , 1 , . . . , \frac { 1 } { 2 } \left\lfloor \frac { 1 } { 2 } \right\rfloor \mathsf { f o r w h i c h }$ $S P [ n , { \frac { \mid M \mid } { 2 } } ] - m ] = T r u e .$

• Do we need to solve $S P$ repeatedly (again and again form scratch) to solve BP?

Can we reuse the solution of subproblems?

### Images:
- data\Design and Analysis of Algorithms\L08-DP\page_053\L08-DP_page_053\auto\images\b80351ed158cb0e00b07b7b2c696c1f98c6f940f8479a61b5595d9dd3a6bcc64.jpg

---

## Lecture: L08-DP\page_054\L08-DP_page_054\auto

# Solving SSP

• Write the DP equations for SSP.

• Very similar to knapsack problem.

• Can you guess them?

---

## Lecture: L08-DP\page_055\L08-DP_page_055\auto

• Recursion for????????????[????, ????]:

![](images/456f8a54bcfe568c74fb16758d7547c3ae9711c695c3e10e606c7e37e8913b43.jpg)

S $\langle S P [ j , X ] = \mathsf { m a x } \{ S S P [ j - 1 , X ] , S S P [ j - 1 , \boldsymbol { \bot }$ $- \ 1 , X ] \ , S S P [ j \ - \ 1 , X - \ k j ] \ \} \ , \ 0 \leq j \ \leq n , X$ ≤ ????, S $\dot { S } P [ j , 0 ] = 1 , j = 0 , . . . , n , S S P [ 0 , X > 0 ] = 0 ,$ $0 , . . . , n , \ S S P [ 0 , X > 0 ] = 0 , \ S S P [ k , X < 0 ] :$ = 0.

• Solution: $S S P [ n , D ]$ .

• Complexity: ?? -> same as Knapsack = ????(????????).

### Images:
- data\Design and Analysis of Algorithms\L08-DP\page_055\L08-DP_page_055\auto\images\0f581e6454a7c5cbb32f2e9f3644ce68a449f4fb5b8bdc185ae79f79e5373dfa.jpg
- data\Design and Analysis of Algorithms\L08-DP\page_055\L08-DP_page_055\auto\images\3112889460744663d5fc1bae7782ae144c9d1b0ea364234b6f9dfbbc9f5f842a.jpg
- data\Design and Analysis of Algorithms\L08-DP\page_055\L08-DP_page_055\auto\images\456f8a54bcfe568c74fb16758d7547c3ae9711c695c3e10e606c7e37e8913b43.jpg
- data\Design and Analysis of Algorithms\L08-DP\page_055\L08-DP_page_055\auto\images\51206e7db6922c652c51b1ea910113d9024fcf1c220c1e8ff4f444e87ef4a084.jpg
- data\Design and Analysis of Algorithms\L08-DP\page_055\L08-DP_page_055\auto\images\9f369b620e995557147d4118ef33bdd18467823122dd67fb0df85286caae2e03.jpg

---

## Lecture: L08-DP\page_056\L08-DP_page_056\auto

• Recursion for $S S P [ n , D ]$ :

![](images/48a90dbccac7c874e622d8830b6bb76c082ad7bd7a9876cf2a96436a5dec3893.jpg)

S $\langle S P [ j , X ] = \mathsf { m a x } \{ S S P [ j - 1 , X ] , S S P [ j - 1 , \boldsymbol { \bot }$ $- \ 1 , X ] \ , S S P [ j \ - \ 1 , X - \ k j ] \ \} \ , \ 0 \leq j \ \leq n , X$ ≤ ????, S $\mathrm { \large { : } } S P [ j , 0 ] = 1 , j = 0 , . . . , n , S S P [ 0 , X > 0 ] = 0 ,$ $0 , . . . , n , \ S S P [ 0 , X > 0 ] = 0 , \ S S P [ k , X < 0 ] :$ = 0.

# Solution for BP:

????: sum of item sizes

• Solve ????????[????, ????/2 ], fill in table of sub-problems.

• Find largest ???? = ????/2 , ????/2 − 1, …, s. t. ????????[1. .????, ????] = 1.

### Images:
- data\Design and Analysis of Algorithms\L08-DP\page_056\L08-DP_page_056\auto\images\017ef542a28811038028b87f387873c894d4552a8ae302a86e013a599c01c66f.jpg
- data\Design and Analysis of Algorithms\L08-DP\page_056\L08-DP_page_056\auto\images\01db246bc795d641498ee35f81930e4b5a67a2de63aa70b7162f10bb85bbd657.jpg
- data\Design and Analysis of Algorithms\L08-DP\page_056\L08-DP_page_056\auto\images\48a90dbccac7c874e622d8830b6bb76c082ad7bd7a9876cf2a96436a5dec3893.jpg
- data\Design and Analysis of Algorithms\L08-DP\page_056\L08-DP_page_056\auto\images\e9efc252f0e1e162a070a64666924ecb80e661afcc17bc9a1d377325b078f92f.jpg
- data\Design and Analysis of Algorithms\L08-DP\page_056\L08-DP_page_056\auto\images\f89289c720c77d083ce4ca0d37bb0508ace97bc7a8f97b407133bf0b3d19e239.jpg

---

## Lecture: L08-DP\page_057\L08-DP_page_057\auto

• Solve BP for item sizes 1,2,3,4. ???? = 10, ????/2 = 5

????????????[????, ????] = $\begin{array} { r } { \begin{array} { r } { \mathsf { m a x } \{ S S P [ j - 1 , X ] , S S P [ j - 1 , X - k _ { j } ] \} , 0 \leq j \leq n } \\ { 1 , j = 0 , . . . , n , S S P [ 0 , X > 0 ] = 0 , S S P [ k , X < 0 ] = 0 } \end{array} } \end{array}$ ,???? ≤ ????, ????????????[????, 0] = .

<table><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>X=0</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>5</td></tr><tr><td rowspan=1 colspan=1>j=0</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr></table>

### Images:
- data\Design and Analysis of Algorithms\L08-DP\page_057\L08-DP_page_057\auto\images\6ea2f49ec925c08efb49fd7ad8ecce02a351bd1773f1d73ba7054c732d1dedbf.jpg
- data\Design and Analysis of Algorithms\L08-DP\page_057\L08-DP_page_057\auto\images\9129441861fcc4d24e529cab923d9b4f86a2eea8df6e90636c38f8987db5ae3a.jpg

---

## Lecture: L08-DP\page_058\L08-DP_page_058\auto

• Solve BP for item sizes 1,2,3,4. ???? = 10, ????/2 = 5

????????????[????, ????] = $\begin{array} { r } { \begin{array} { r } { \mathsf { m a x } \{ S S P [ j - 1 , X ] , S S P [ j - 1 , X - k _ { j } ] \} , 0 \leq j \leq n } \\ { 1 , j = 0 , . . . , n , S S P [ 0 , X > 0 ] = 0 , S S P [ k , X < 0 ] = 0 } \end{array} } \end{array}$ ,???? ≤ ????, ????????????[????, 0] = .

<table><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>X=0</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>5</td></tr><tr><td rowspan=1 colspan=1>j=0</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1</td></tr></table>

### Images:
- data\Design and Analysis of Algorithms\L08-DP\page_058\L08-DP_page_058\auto\images\151de55f5937c77da2efcf7aa7e694f7050a60d0e0d122dd33f41dcb321049ca.jpg
- data\Design and Analysis of Algorithms\L08-DP\page_058\L08-DP_page_058\auto\images\5930451a5cc002d223738adf26d8c700a19704f1f80d51d538b3d977f4469ee5.jpg

---

## Lecture: L08-DP\page_059\L08-DP_page_059\auto

# Conclusions

• DP is a technique for solving complex optimization problems computationally.

• Key idea is to decompose a problem into a calculation involving the independent solution of similar type problems defined on reduced size systems (recurrence).

• The reduction of the complexity is due to memoization: solving each subproblem only once and remembering the results.

---

## Lecture: L09-Greedy\page_001\L09-Greedy_page_001\auto

# Greedy Algorithms

Activity selection Activity selection version 2 Minimum Spanning Trees

---

## Lecture: L09-Greedy\page_002\L09-Greedy_page_002\auto

# Greedy Algorithms

• Make choices one-at-a-time.

• Never look back.

• Hope for the best.

![](images/421031704396f80f0a37f5a6032052cfbebdd462e631be353b5f23fab2d6ea17.jpg)

### Images:
- data\Design and Analysis of Algorithms\L09-Greedy\page_002\L09-Greedy_page_002\auto\images\421031704396f80f0a37f5a6032052cfbebdd462e631be353b5f23fab2d6ea17.jpg

---

## Lecture: L09-Greedy\page_003\L09-Greedy_page_003\auto

One example of a greedy algorithm that does not work: Knapsack again

Three examples of greedy algorithms that do work:

Activity Selection Job Scheduling Minimum Spanning Tree

---

## Lecture: L09-Greedy\page_004\L09-Greedy_page_004\auto

# Non-example: Unbounded Knapsack

Capacity: 10

Item: Weight: Value:

![](images/db0f9d8e23e948c9d4906d91bbd174f6b3b805e86f05a842f154165d9eb37c1e.jpg)

• Unbounded Knapsack:

• Suppose I have infinite copies of all items. • What’s the most valuable way to fill the knapsack?

Total weight: 10   
Total value: 42

• “Greedy” algorithm for unbounded knapsack:

• Tacos have the best Value/Weight ratio!

Total weight: 9   
Total value: 39

• Keep grabbing tacos!

### Images:
- data\Design and Analysis of Algorithms\L09-Greedy\page_004\L09-Greedy_page_004\auto\images\23a3a51e12b70e6e4b47d6946b74a61a5a0d304ee3085dc366324dfd29be179b.jpg
- data\Design and Analysis of Algorithms\L09-Greedy\page_004\L09-Greedy_page_004\auto\images\3e87f30e324c21a657fcc0ba0866d7bfe038853c3cd334379acb43a7854792f9.jpg
- data\Design and Analysis of Algorithms\L09-Greedy\page_004\L09-Greedy_page_004\auto\images\45f2c8dd30935de9b5b30bbfefc631ebbedabf10d2494458a51bf7a1ec6defe0.jpg
- data\Design and Analysis of Algorithms\L09-Greedy\page_004\L09-Greedy_page_004\auto\images\db0f9d8e23e948c9d4906d91bbd174f6b3b805e86f05a842f154165d9eb37c1e.jpg

---

## Lecture: L09-Greedy\page_005\L09-Greedy_page_005\auto

# Example where greedy works

![](images/267ee0d286687529ad86413fc57a37fcc693024ed09657f949c10d0328223cf9.jpg)

### Images:
- data\Design and Analysis of Algorithms\L09-Greedy\page_005\L09-Greedy_page_005\auto\images\267ee0d286687529ad86413fc57a37fcc693024ed09657f949c10d0328223cf9.jpg

---

## Lecture: L09-Greedy\page_006\L09-Greedy_page_006\auto

# Activity selection

• Input:

– Activities a1, a2, …, an – Start times s1, s2, …, sn – Finish times $\mathsf { f } _ { 1 } , \mathsf { f } _ { 2 } , . . . , \mathsf { f } _ { \mathrm { n } }$

![](images/fd4efd647a6c9dc8d37d597b1474e5b5c47531a6a05eb40642472e5f5c2149bd.jpg)

• Output:

– A way to maximize the number of activities you can do today.

In what order should you greedily add activities?

### Images:
- data\Design and Analysis of Algorithms\L09-Greedy\page_006\L09-Greedy_page_006\auto\images\fd4efd647a6c9dc8d37d597b1474e5b5c47531a6a05eb40642472e5f5c2149bd.jpg

---

## Lecture: L09-Greedy\page_007\L09-Greedy_page_007\auto

# In what order?

• Shortest job first?

![](images/589348c9dd3274c0d079a750b9ae791e0dcb924f2d5c92a43562ab68f1e65d9a.jpg)

• Earliest start time?

• Earliest finish time?

### Images:
- data\Design and Analysis of Algorithms\L09-Greedy\page_007\L09-Greedy_page_007\auto\images\589348c9dd3274c0d079a750b9ae791e0dcb924f2d5c92a43562ab68f1e65d9a.jpg
- data\Design and Analysis of Algorithms\L09-Greedy\page_007\L09-Greedy_page_007\auto\images\6dd2487f891c47ddd6ce8a619e2b876e5f18b562e6a0afdb75954fd61a3619de.jpg

---

## Lecture: L09-Greedy\page_008\L09-Greedy_page_008\auto

# Greedy Algorithm

• Pick activity you can add with the smallest finish time.

• Repeat.

![](images/5cb7fdee08e3e48715c49c4ecf784267b9cd5b5211e70688fb24371af817e061.jpg)

### Images:
- data\Design and Analysis of Algorithms\L09-Greedy\page_008\L09-Greedy_page_008\auto\images\5cb7fdee08e3e48715c49c4ecf784267b9cd5b5211e70688fb24371af817e061.jpg

---

## Lecture: L09-Greedy\page_009\L09-Greedy_page_009\auto

# Greedy Algorithm

• Pick activity you can add with the smallest finish time.

• Repeat.

![](images/703bba04eff368a1a8ba2cc2a861aa44632543b174e26683e6903d24a1543180.jpg)

### Images:
- data\Design and Analysis of Algorithms\L09-Greedy\page_009\L09-Greedy_page_009\auto\images\703bba04eff368a1a8ba2cc2a861aa44632543b174e26683e6903d24a1543180.jpg

---

## Lecture: L09-Greedy\page_010\L09-Greedy_page_010\auto

# Greedy Algorithm

• Pick activity you can add with the smallest finish time.

• Repeat.

![](images/2aca4b402328bcd935cdc781462c1747a2d284e7c83926404c197a0944d80552.jpg)

### Images:
- data\Design and Analysis of Algorithms\L09-Greedy\page_010\L09-Greedy_page_010\auto\images\2aca4b402328bcd935cdc781462c1747a2d284e7c83926404c197a0944d80552.jpg

---

## Lecture: L09-Greedy\page_011\L09-Greedy_page_011\auto

# Greedy Algorithm

• Pick activity you can add with the smallest finish time.

• Repeat.

![](images/7be17d2229aa03a76820bec933a6c1af2149018423049a759bcb316b88bbbc35.jpg)

### Images:
- data\Design and Analysis of Algorithms\L09-Greedy\page_011\L09-Greedy_page_011\auto\images\7be17d2229aa03a76820bec933a6c1af2149018423049a759bcb316b88bbbc35.jpg

---

## Lecture: L09-Greedy\page_012\L09-Greedy_page_012\auto

# Greedy Algorithm

• Pick activity you can add with the smallest finish time.

• Repeat.

![](images/d95de4a1bafb03288fc361e83a5ab7e527fda8f93b68d1155f7dbac2525fcbbc.jpg)

### Images:
- data\Design and Analysis of Algorithms\L09-Greedy\page_012\L09-Greedy_page_012\auto\images\d95de4a1bafb03288fc361e83a5ab7e527fda8f93b68d1155f7dbac2525fcbbc.jpg

---

## Lecture: L09-Greedy\page_013\L09-Greedy_page_013\auto

# Greedy Algorithm

• Pick activity you can add with the smallest finish time.

• Repeat.

![](images/9f90e8aae4bf6cb04dc2c2ff99ffeeb3585f6487aa1156501b03f735c3941690.jpg)

### Images:
- data\Design and Analysis of Algorithms\L09-Greedy\page_013\L09-Greedy_page_013\auto\images\9f90e8aae4bf6cb04dc2c2ff99ffeeb3585f6487aa1156501b03f735c3941690.jpg

---

## Lecture: L09-Greedy\page_014\L09-Greedy_page_014\auto

# Greedy Algorithm

• Pick activity you can add with the smallest finish time.

• Repeat.

![](images/4c35224a3f20b8a79ec120dafaeaaab9d2e89ed4d761de4b5af763e6407f8d8f.jpg)

### Images:
- data\Design and Analysis of Algorithms\L09-Greedy\page_014\L09-Greedy_page_014\auto\images\4c35224a3f20b8a79ec120dafaeaaab9d2e89ed4d761de4b5af763e6407f8d8f.jpg

---

## Lecture: L09-Greedy\page_015\L09-Greedy_page_015\auto

# Greedy Algorithm

• Pick activity you can add with the smallest finish time.

• Repeat.

![](images/577c60615108cde8ee70b92dcf58039a0e4823de3134e46b475b29db99d52c2b.jpg)

### Images:
- data\Design and Analysis of Algorithms\L09-Greedy\page_015\L09-Greedy_page_015\auto\images\577c60615108cde8ee70b92dcf58039a0e4823de3134e46b475b29db99d52c2b.jpg

---

## Lecture: L09-Greedy\page_016\L09-Greedy_page_016\auto

• Running time:

–O(n) if the activities are already sorted by finish time.   
–Otherwise, O(n log(n)) if you have to sort them first.

---

## Lecture: L09-Greedy\page_017\L09-Greedy_page_017\auto

1. Does this greedy algorithm for activity selection work? – Yes

2. Greedy is simple. But why are we getting to it in week 9 (not earlier)?

– Proving that greedy algorithms work is often not so easy…

3. In general, when are greedy algorithms a good idea?

– When the problem exhibits especially nice optimal substructure.

---

## Lecture: L09-Greedy\page_018\L09-Greedy_page_018\auto

# Back to Activity Selection

Why does it work?

• We never rule out an optimal solution

• At the end of the algorithm, we’ve got some solution.

• So it must be optimal.

---

## Lecture: L09-Greedy\page_019\L09-Greedy_page_019\auto

# The Correctness of Activity Selection

• Suppose we’ve already chosen ai, and there is still an optimal solution T\* that extends our choices.

![](images/ab2b1ed2dfc1410bca73bad11f2b3f6098ae56da5a7c101691de32782fc6d975.jpg)

### Images:
- data\Design and Analysis of Algorithms\L09-Greedy\page_019\L09-Greedy_page_019\auto\images\ab2b1ed2dfc1410bca73bad11f2b3f6098ae56da5a7c101691de32782fc6d975.jpg

---

## Lecture: L09-Greedy\page_020\L09-Greedy_page_020\auto

# The Correctness of Activity Selection

• Suppose we’ve already chosen ai, and there is still an optimal solution T\* that extends our choices.

• Now consider the next choice we make, say it’s $\mathsf { a } _ { \mathsf { k } }$

If $\mathsf { a } _ { \mathsf { k } }$ is in T\*, we’re still on track.

![](images/c6103d44ab5ac8da5b8a368e6b94a546dda88bdbb20e2d7d851685d11f0baf53.jpg)

### Images:
- data\Design and Analysis of Algorithms\L09-Greedy\page_020\L09-Greedy_page_020\auto\images\c6103d44ab5ac8da5b8a368e6b94a546dda88bdbb20e2d7d851685d11f0baf53.jpg

---

## Lecture: L09-Greedy\page_021\L09-Greedy_page_021\auto

# The Correctness of Activity Selection

• Suppose we’ve already chosen ai, and there is still an optimal solution T\* that extends our choices.

• Now consider the next choice we make, say it’s $\mathsf { a } _ { \mathsf { k } }$

• If $\mathsf { a } _ { \mathsf { k } }$ is not in T\*

![](images/81839041ddf1cb49a70e53afdefa6eef228f17bd6957afe85c576865e0990398.jpg)

### Images:
- data\Design and Analysis of Algorithms\L09-Greedy\page_021\L09-Greedy_page_021\auto\images\81839041ddf1cb49a70e53afdefa6eef228f17bd6957afe85c576865e0990398.jpg

---

## Lecture: L09-Greedy\page_022\L09-Greedy_page_022\auto

# The Correctness of Activity Selection

• If ak is not in T\*

• Let aj be the activity in T\* with the smallest end time.

• Now consider schedule T you get by swapping aj for $\mathsf { a } _ { \mathsf { k } }$

![](images/317eab765a8865f9120f2cc4fc49c5426f24682137f834e680255ec6f364fe80.jpg)

### Images:
- data\Design and Analysis of Algorithms\L09-Greedy\page_022\L09-Greedy_page_022\auto\images\317eab765a8865f9120f2cc4fc49c5426f24682137f834e680255ec6f364fe80.jpg

---

## Lecture: L09-Greedy\page_023\L09-Greedy_page_023\auto

# The Correctness of Activity Selection

• If ak is not in T\*

• Let aj be the activity in T\* with the smallest end time.

• Now consider schedule T you get by swapping aj for $\mathsf { a } _ { \mathsf { k } }$

![](images/5f8424bc8f58a4d273124e28ec10b9c65fe0083f3f98ba5cc71c5a2a13adeaad.jpg)

### Images:
- data\Design and Analysis of Algorithms\L09-Greedy\page_023\L09-Greedy_page_023\auto\images\5f8424bc8f58a4d273124e28ec10b9c65fe0083f3f98ba5cc71c5a2a13adeaad.jpg

---

## Lecture: L09-Greedy\page_024\L09-Greedy_page_024\auto

# The Correctness of Activity Selection

• This schedule T is still allowed.

– Since $\mathsf { a } _ { \mathsf { k } }$ has the smallest ending time, it ends before aj.   
– Thus, $\mathsf { a } _ { \mathsf { k } }$ doesn’t conflict with anything chosen after aj.

• And T is still optimal.

– It has the same number of activities as T\*.

![](images/0cf54cc753d00a611208c81935e06d1bf636f497de07515b45696860fa739734.jpg)

### Images:
- data\Design and Analysis of Algorithms\L09-Greedy\page_024\L09-Greedy_page_024\auto\images\0cf54cc753d00a611208c81935e06d1bf636f497de07515b45696860fa739734.jpg

---

## Lecture: L09-Greedy\page_025\L09-Greedy_page_025\auto

# The Correctness of Activity Selection

• We’ve just shown:

– If there was an optimal solution that extends the choices we made so far… …then there is an optimal schedule that also contains our next greedy choice ak

![](images/47d4b9b7c6c631c6f09bd8e753d95dd8f77cbd7c19d1366ae50d69060b4a1a99.jpg)

### Images:
- data\Design and Analysis of Algorithms\L09-Greedy\page_025\L09-Greedy_page_025\auto\images\47d4b9b7c6c631c6f09bd8e753d95dd8f77cbd7c19d1366ae50d69060b4a1a99.jpg

---

## Lecture: L09-Greedy\page_026\L09-Greedy_page_026\auto

# The Correctness of Activity Selection

So it’s correct!

• We never rule out an optimal solution

• At the end of the algorithm, we’ve got some solution.

• So it must be optimal.

---

## Lecture: L09-Greedy\page_027\L09-Greedy_page_027\auto

# A Common Strategy

A common strategy for proving the correctness of greedy algorithms:

• Make a series of choices.   
• Show that, at each step, our choice won’t rule out an optimal solution at the end of the day.   
• After we’ve made all our choices, we haven’t ruled out an optimal solution, so we must have found one.

---

## Lecture: L09-Greedy\page_028\L09-Greedy_page_028\auto

# A Common Strategy

• Inductive Hypothesis: – After greedy choice t, you haven’t ruled out success.

• Base case: – Success is possible before you make any choices.

– If you haven’t ruled out success after choice t, then you won’t rule out success after choice t+1.

• Conclusion:

– If you reach the end of the algorithm and haven’t ruled out success then you must have succeeded.

---

## Lecture: L09-Greedy\page_029\L09-Greedy_page_029\auto

# A Common Strategy

A common strategy for showing we don’t rule out the optimal solution:

• Suppose that you’re on track to make an optimal solution T\*. – E.g., after you’ve picked activity i, you’re still on track.

• Suppose that T\* disagrees with your next greedy choice. E.g., it doesn’t involve activity k.

• Manipulate T\* in order to make a solution T that’s not worse but that agrees with your greedy choice.

– E.g., swap whatever activity T\* did pick next with activity k.

---

## Lecture: L09-Greedy\page_030\L09-Greedy_page_030\auto

# Three Questions

1. Does this greedy algorithm for activity selection work?

– Yes

2. Greedy is simple. But why are we getting to it in week 9?

![](images/bee058973bff344c8d977cda24de6bddd75b6a2c1940a218bc021fec5f696b86.jpg)

– Proving that greedy algorithms work is often not so easy…

![](images/e6075a7930a6db6ac7311c50b4fe0d9cc866f23f9d7290b46d5457f68387e58f.jpg)

3. In general, when are greedy algorithms a good idea?

– When the problem exhibits especially nice optimal substructure.

### Images:
- data\Design and Analysis of Algorithms\L09-Greedy\page_030\L09-Greedy_page_030\auto\images\bee058973bff344c8d977cda24de6bddd75b6a2c1940a218bc021fec5f696b86.jpg
- data\Design and Analysis of Algorithms\L09-Greedy\page_030\L09-Greedy_page_030\auto\images\e6075a7930a6db6ac7311c50b4fe0d9cc866f23f9d7290b46d5457f68387e58f.jpg

---

## Lecture: L09-Greedy\page_031\L09-Greedy_page_031\auto

# Sub-problem graph view

• Divide-and-conquer:

![](images/68ecb449cd55304e93fd02879ebe769b2de23095f65e2c563cbafbd81ad97e1c.jpg)

### Images:
- data\Design and Analysis of Algorithms\L09-Greedy\page_031\L09-Greedy_page_031\auto\images\68ecb449cd55304e93fd02879ebe769b2de23095f65e2c563cbafbd81ad97e1c.jpg

---

## Lecture: L09-Greedy\page_032\L09-Greedy_page_032\auto

# Sub-problem graph view

• Dynamic Programming:

![](images/380c5bae5270c542bff74c9235b49594203923babca3216f4afbd83bf6dbbcac.jpg)

### Images:
- data\Design and Analysis of Algorithms\L09-Greedy\page_032\L09-Greedy_page_032\auto\images\380c5bae5270c542bff74c9235b49594203923babca3216f4afbd83bf6dbbcac.jpg

---

## Lecture: L09-Greedy\page_033\L09-Greedy_page_033\auto

# Sub-problem graph view

• Greedy algorithms:

![](images/74ace65e492d7b96d95100c992f341e17f0bea0260dc98cec9c3cd0ed67eda24.jpg)

### Images:
- data\Design and Analysis of Algorithms\L09-Greedy\page_033\L09-Greedy_page_033\auto\images\74ace65e492d7b96d95100c992f341e17f0bea0260dc98cec9c3cd0ed67eda24.jpg

---

## Lecture: L09-Greedy\page_034\L09-Greedy_page_034\auto

# Sub-problem graph view

• Greedy algorithms:

![](images/729c68afe42c166485ce758f5b1a452a189af168c75e4076583c3b4f3c206557.jpg)

• Not only is there optimal sub-structure:

● optimal solutions to a problem are made up from optimal solutions of sub-problems

• but each problem depends on only one sub-problem.

### Images:
- data\Design and Analysis of Algorithms\L09-Greedy\page_034\L09-Greedy_page_034\auto\images\729c68afe42c166485ce758f5b1a452a189af168c75e4076583c3b4f3c206557.jpg

---

## Lecture: L09-Greedy\page_035\L09-Greedy_page_035\auto

# Three Questions

1. Does this greedy algorithm for activity selection work?

– Yes

2. Greedy is simple. But why are we getting to it in week 9?

![](images/850ffdd4b1b5e59775a0aa8fff386c7a019408fa342c91dcbb08b9d534c977cf.jpg)

– Proving that greedy algorithms work is often not so easy…

3. In general, when are greedy algorithms a good idea?

![](images/686e0ad9086715af7f06b4c8c1278de4214adc7902ed93de2363c7ee8aa072ad.jpg)

– When the problem exhibits especially nice optimal substructure.

### Images:
- data\Design and Analysis of Algorithms\L09-Greedy\page_035\L09-Greedy_page_035\auto\images\686e0ad9086715af7f06b4c8c1278de4214adc7902ed93de2363c7ee8aa072ad.jpg
- data\Design and Analysis of Algorithms\L09-Greedy\page_035\L09-Greedy_page_035\auto\images\850ffdd4b1b5e59775a0aa8fff386c7a019408fa342c91dcbb08b9d534c977cf.jpg

---

## Lecture: L09-Greedy\page_036\L09-Greedy_page_036\auto

# Another Example: Scheduling

![](images/77d547f44d9db1df884babb304f9ddd009998d3ef097d8f22715d3b632dd8514.jpg)

### Images:
- data\Design and Analysis of Algorithms\L09-Greedy\page_036\L09-Greedy_page_036\auto\images\65676afa2495db742cc0b92f8ed6557c90b61890d7cf0e3f9338675648773844.jpg
- data\Design and Analysis of Algorithms\L09-Greedy\page_036\L09-Greedy_page_036\auto\images\77d547f44d9db1df884babb304f9ddd009998d3ef097d8f22715d3b632dd8514.jpg

---

## Lecture: L09-Greedy\page_037\L09-Greedy_page_037\auto

• n tasks   
• Task i takes ti hours   
• For every hour that passes until task i is done, pay ci

![](images/6f826d0b33897c298e73971c501d77b4ed550da2870cd4df31522cc19b04098a.jpg)

![](images/9d59fe6408ef4eed67ac6958da8bd4f508c05338d8e7a8c8ee07ee261e92887e.jpg)

Cost: 2 units per hour until it’s done.

Cost: 3 units per hour until it’s done.

• DSAA2043 HW, then Sleep: costs $1 0 \cdot 2 + { \bigl ( } 1 0 + 8 { \bigr ) } \cdot 3 = 7 4$ units • Sleep, then DSAA2043 HW: costs $8 \cdot 3 + ( 1 0 + 8 ) \cdot 2 = 6 0$ units

### Images:
- data\Design and Analysis of Algorithms\L09-Greedy\page_037\L09-Greedy_page_037\auto\images\6f826d0b33897c298e73971c501d77b4ed550da2870cd4df31522cc19b04098a.jpg
- data\Design and Analysis of Algorithms\L09-Greedy\page_037\L09-Greedy_page_037\auto\images\9d59fe6408ef4eed67ac6958da8bd4f508c05338d8e7a8c8ee07ee261e92887e.jpg

---

## Lecture: L09-Greedy\page_038\L09-Greedy_page_038\auto

• This problem breaks up nicely into sub-problems:

Suppose this is the optimal schedule:

![](images/6157b72a03442884534f1ca5ae4c5130b274f710fa85e71d9090c7b840cf7fdd.jpg)

Then this must be the optimal schedule on just jobs $\mathsf { B } , \mathsf { C } , \mathsf { D }$ .

If not, then rearranging B,C,D could make a better schedule than (A,B,C,D)!

### Images:
- data\Design and Analysis of Algorithms\L09-Greedy\page_038\L09-Greedy_page_038\auto\images\6157b72a03442884534f1ca5ae4c5130b274f710fa85e71d9090c7b840cf7fdd.jpg

---

## Lecture: L09-Greedy\page_039\L09-Greedy_page_039\auto

# • Seems amenable to a greedy algorithm:

# Take the best job first

![](images/bb34d3e1fd9775171279e5f7be5e8956a22a9d2ab3ed763323b1f1821be54e0e.jpg)

### Images:
- data\Design and Analysis of Algorithms\L09-Greedy\page_039\L09-Greedy_page_039\auto\images\bb34d3e1fd9775171279e5f7be5e8956a22a9d2ab3ed763323b1f1821be54e0e.jpg

---

## Lecture: L09-Greedy\page_040\L09-Greedy_page_040\auto

# What does “best” mean?

• Of these two jobs, which should we do first?

Cost: z units per hour until it’s done.

![](images/b5baba39b8de944af72b8222ee4e59c4b9845754fc61a8abfc801466befbf347.jpg)

Cost: w units per hour until it’s done.

• Cost( A then B ) = x ⋅ z + (x + y) ⋅ w

• Cost( B then A ) = y ⋅ w + (x + y) ⋅ z

AB is better than BA when:

$$
\begin{array} { c } { { x z + ( x + y ) w \leq y w + ( x + y ) z } } \\ { { x z + x w + y w \leq y w + x z + y z } } \\ { { w x \leq y z } } \\ { { \displaystyle \frac { w } { y } \leq \frac { z } { x } } } \end{array}
$$

### Images:
- data\Design and Analysis of Algorithms\L09-Greedy\page_040\L09-Greedy_page_040\auto\images\70bfe25e7f754660ebd52931e5d2e38599e10d1e83d51e25937bd4f7cde9755f.jpg
- data\Design and Analysis of Algorithms\L09-Greedy\page_040\L09-Greedy_page_040\auto\images\b5baba39b8de944af72b8222ee4e59c4b9845754fc61a8abfc801466befbf347.jpg

---

## Lecture: L09-Greedy\page_041\L09-Greedy_page_041\auto

# Idea for Greedy

cost of delay • Choose the job with the biggest ratio. time it takes

---

## Lecture: L09-Greedy\page_042\L09-Greedy_page_042\auto

# Correctness

• Suppose you have already chosen some jobs, and haven’t yet ruled out success:

![](images/a70a15a773a2a56a8286e6b11caab3b9ec6e8efc163859008963ac5c0fc88ce4.jpg)

• Then if you choose the next job to be the one left that maximizes the ratio cost/time, you still won’t rule out success.

# Proof sketch:

Say Job B maximizes this ratio, but it’s not the next job in the opt. soln.

• Switch A and B! Nothing else will change, and we just showed that the cost of the solution won’t increase.

Job E

Job C

Job B

Job A

Repeat until B is first.

# Job E

Job B

Job C

Job A

の Now this is an optimal schedule where B is first.

### Images:
- data\Design and Analysis of Algorithms\L09-Greedy\page_042\L09-Greedy_page_042\auto\images\a70a15a773a2a56a8286e6b11caab3b9ec6e8efc163859008963ac5c0fc88ce4.jpg

---

## Lecture: L09-Greedy\page_043\L09-Greedy_page_043\auto

• Inductive Hypothesis:

• After greedy choice t, you haven’t ruled out success.

• Base case: ● Success is possible before you make any choices.

• If you haven’t ruled out success after choice t, then you won’t rule out success after choice t+1.

• Conclusion:

• If you reach the end of the algorithm and haven’t ruled out success then you must have succeeded.

---

## Lecture: L09-Greedy\page_044\L09-Greedy_page_044\auto

# Greedy Scheduling Solution

• scheduleJobs( JOBS ): – Sort JOBS in decreasing order by the ratio: ???? = ???????? cost of delaying job i – Return JOBS

Running time: O(n log(n))

---

## Lecture: L09-Greedy\page_045\L09-Greedy_page_045\auto

# Minimum Spanning Trees

---

## Lecture: L09-Greedy\page_046\L09-Greedy_page_046\auto

# Minimum Spanning Trees

• Greedy algorithms for Minimum Spanning Tree.

• Agenda:

1. What is a Minimum Spanning Tree?

2. Short break to introduce some graph theory tools

3. Prim’s algorithm

Kruskal’s algorithm

---

## Lecture: L09-Greedy\page_047\L09-Greedy_page_047\auto

# Minimum Spanning Trees

• Say we have an undirected weighted graph

![](images/7acfcc59f1dfb0477c6360d554300b2beb65611e7a4018757bb0ac85630ed407.jpg)

A tree is a connected graph with no cycles!

A spanning tree is a tree that connects all of the vertices.

### Images:
- data\Design and Analysis of Algorithms\L09-Greedy\page_047\L09-Greedy_page_047\auto\images\7acfcc59f1dfb0477c6360d554300b2beb65611e7a4018757bb0ac85630ed407.jpg

---

## Lecture: L09-Greedy\page_048\L09-Greedy_page_048\auto

# Minimum Spanning Trees

• Say we have an undirected weighted graph

The cost of a spanning tree is the sum of the weights on the edges.

This is a spanning tree with cost 67.

![](images/df775284b643435374379d2e116af0fa257f4b0f49ca89e6b02c5227f50b5125.jpg)

A spanning tree is a tree that connects all of the vertices.

### Images:
- data\Design and Analysis of Algorithms\L09-Greedy\page_048\L09-Greedy_page_048\auto\images\df775284b643435374379d2e116af0fa257f4b0f49ca89e6b02c5227f50b5125.jpg

---

## Lecture: L09-Greedy\page_049\L09-Greedy_page_049\auto

# Minimum Spanning Trees

• Say we have an undirected weighted graph

This is also a spanning tree, with cost 37.

![](images/7339633a3255c638e7a9ef0bc2677effb86c8e3f4de9c758f173f9fd4882c042.jpg)

A spanning tree is a tree that connects all of the vertices.

### Images:
- data\Design and Analysis of Algorithms\L09-Greedy\page_049\L09-Greedy_page_049\auto\images\7339633a3255c638e7a9ef0bc2677effb86c8e3f4de9c758f173f9fd4882c042.jpg

---

## Lecture: L09-Greedy\page_050\L09-Greedy_page_050\auto

# Minimum Spanning Trees

• Say we have an undirected weighted graph

![](images/79affd43b7418e6df885e8659f92eaea024c6cbe3040963ce3d5d8816ec755c6.jpg)

minimum

of minimum cost

A spanning tree is a tree that connects all of the vertices.

### Images:
- data\Design and Analysis of Algorithms\L09-Greedy\page_050\L09-Greedy_page_050\auto\images\79affd43b7418e6df885e8659f92eaea024c6cbe3040963ce3d5d8816ec755c6.jpg

---

## Lecture: L09-Greedy\page_051\L09-Greedy_page_051\auto

# Why MSTs?

• Network design – Connecting cities with roads/electricity/telephone/…

• Cluster analysis – E.g., genetic distance

• Image processing – E.g., image segmentation

![](images/b92a7ebb7547a87d880fb5d2b64f430ba1c9a2876a44078378019f5d3885e0ab.jpg)

• Useful primitive – For other graph algs

![](images/3c5a60db61d2fde018e8b961437ff791192e9a068bb8593e227c10d54ae7651c.jpg)

### Images:
- data\Design and Analysis of Algorithms\L09-Greedy\page_051\L09-Greedy_page_051\auto\images\3c5a60db61d2fde018e8b961437ff791192e9a068bb8593e227c10d54ae7651c.jpg
- data\Design and Analysis of Algorithms\L09-Greedy\page_051\L09-Greedy_page_051\auto\images\b92a7ebb7547a87d880fb5d2b64f430ba1c9a2876a44078378019f5d3885e0ab.jpg

---

## Lecture: L09-Greedy\page_052\L09-Greedy_page_052\auto

# How to find an MST

• Today we’ll see two greedy algorithms.

• In order to prove that these greedy algorithms work, we’ll show something like:

Suppose that our choices so far are consistent with an MST.

Then the next greedy choice that we make is still consistent with an MST.

• This is not the only way to prove that these algorithms work!

---

## Lecture: L09-Greedy\page_053\L09-Greedy_page_053\auto

# Brief Aside – Cuts in Graphs

• A cut is a partition of the vertices into two parts:

![](images/09f426839e38f3e76dc1dc73eb46dafe5d03c6394c288709910d82d060a6048c.jpg)

This is the cut “{A,B,D,E} and $\{ { \mathsf { C } } , { \mathsf { I } } , { \mathsf { H } } , { \mathsf { G } } , { \mathsf { F } } \} ^ { n }$

### Images:
- data\Design and Analysis of Algorithms\L09-Greedy\page_053\L09-Greedy_page_053\auto\images\09f426839e38f3e76dc1dc73eb46dafe5d03c6394c288709910d82d060a6048c.jpg

---

## Lecture: L09-Greedy\page_054\L09-Greedy_page_054\auto

# Brief Aside – Cuts in Graphs

• One or both of the two parts might be disconnected.

![](images/c602cfaac9f50ae95cc6693a57e0e50b1e04f684f559f664e1ab9bb483e6d9c9.jpg)

This is the cut “{B,C,E,G,H} and $\{ A , D , 1 , F \} ^ { \prime }$

### Images:
- data\Design and Analysis of Algorithms\L09-Greedy\page_054\L09-Greedy_page_054\auto\images\c602cfaac9f50ae95cc6693a57e0e50b1e04f684f559f664e1ab9bb483e6d9c9.jpg

---

## Lecture: L09-Greedy\page_055\L09-Greedy_page_055\auto

# Brief Aside – Cuts in Graphs

Let S be a set of edges in G

• We say a cut respects S if no edges in S cross the cut.

• An edge crossing a cut is called light if it has the smallest weight of

![](images/cc41c75cb199e4702dd29c775ea2acb3acf4a3da92109f4696350f6ae1856ebf.jpg)

### Images:
- data\Design and Analysis of Algorithms\L09-Greedy\page_055\L09-Greedy_page_055\auto\images\cc41c75cb199e4702dd29c775ea2acb3acf4a3da92109f4696350f6ae1856ebf.jpg

---

## Lecture: L09-Greedy\page_056\L09-Greedy_page_056\auto

# Brief Aside – Cuts in Graphs

Let S be a set of edges in G

• We say a cut respects S if no edges in S cross the cut.

• An edge crossing a cut is called light if it has the smallest weight of This edge is light

![](images/637c360dfb9c243c1a8ba2f562722aaf7676d2b80ab57b4516ff60dad02bc8e9.jpg)

### Images:
- data\Design and Analysis of Algorithms\L09-Greedy\page_056\L09-Greedy_page_056\auto\images\637c360dfb9c243c1a8ba2f562722aaf7676d2b80ab57b4516ff60dad02bc8e9.jpg

---

## Lecture: L09-Greedy\page_057\L09-Greedy_page_057\auto

# Brief Aside – Cuts in Graphs

Lemma

• Let S be a set of edges, and consider a cut that respects S.

• Suppose there is an MST containing S.

• Let $\{ \mathfrak { u } , \mathfrak { v } \}$ be a light edge.

This edge is light

• Then there is an MST containing S ∪ {{u,v}} Aka:

If we haven’t ruled out the possibility of success so far, then adding a light edge still won’t rule it out.

![](images/4641560e953f9b501ced329167fff1c19dd4e9d47dcc1c9b5acea3e88a8e88f2.jpg)

### Images:
- data\Design and Analysis of Algorithms\L09-Greedy\page_057\L09-Greedy_page_057\auto\images\4641560e953f9b501ced329167fff1c19dd4e9d47dcc1c9b5acea3e88a8e88f2.jpg

---

## Lecture: L09-Greedy\page_058\L09-Greedy_page_058\auto

# Brief Aside – Cuts in Graphs

Proof of Lemma

• Assume that we have: – a cut that respects S

![](images/6b2f04ead302c302a186f35aab806fe39190be767c570316f99a50efd9be7125.jpg)

### Images:
- data\Design and Analysis of Algorithms\L09-Greedy\page_058\L09-Greedy_page_058\auto\images\6b2f04ead302c302a186f35aab806fe39190be767c570316f99a50efd9be7125.jpg

---

## Lecture: L09-Greedy\page_059\L09-Greedy_page_059\auto

# Brief Aside – Cuts in Graphs

Proof of Lemma

• Assume that we have:

– a cut that respects S – S is part of some MST T.

![](images/61274637e5f21b32571cbf5928270933e9945a2ded77200bdc10d38ce9d1afa9.jpg)

### Images:
- data\Design and Analysis of Algorithms\L09-Greedy\page_059\L09-Greedy_page_059\auto\images\61274637e5f21b32571cbf5928270933e9945a2ded77200bdc10d38ce9d1afa9.jpg

---

## Lecture: L09-Greedy\page_060\L09-Greedy_page_060\auto

# Brief Aside – Cuts in Graphs

Proof of Lemma

• Assume that we have: – a cut that respects S – S is part of some MST T.

• Say that $\{ \boldsymbol { \mathbf { u } } , \boldsymbol { \mathbf { \check { v } } } \}$ is light. – lowest cost crossing the cut

• If $\{ \boldsymbol { \mathbf { u } } , \boldsymbol { \mathbf { v } } \}$ is in T, we are done. – T is an MST containing both {u,v} and S.

![](images/5f4f4139975ee0e8077a84d9fc9152662ac64a1f42be652254a8c72bc732e3d5.jpg)

### Images:
- data\Design and Analysis of Algorithms\L09-Greedy\page_060\L09-Greedy_page_060\auto\images\5f4f4139975ee0e8077a84d9fc9152662ac64a1f42be652254a8c72bc732e3d5.jpg

---

## Lecture: L09-Greedy\page_061\L09-Greedy_page_061\auto

# Brief Aside – Cuts in Graphs

Proof of Lemma

• Assume that we have: – a cut that respects S – S is part of some MST T.

• Say that $\{ \boldsymbol { \mathbf { u } } , \boldsymbol { \mathbf { \check { v } } } \}$ is light. – lowest cost crossing the cut

• Say $\{ \mathfrak { u } , \mathfrak { v } \}$ is not in T. – Note that adding $\{ \boldsymbol { \mathbf { u } } , \boldsymbol { \mathbf { v } } \}$ to T will make a cycle.

![](images/b5d7b559af01a73c47cb4074d5ef4379baa9daa027b67f4816c63338192b3736.jpg)

### Images:
- data\Design and Analysis of Algorithms\L09-Greedy\page_061\L09-Greedy_page_061\auto\images\b5d7b559af01a73c47cb4074d5ef4379baa9daa027b67f4816c63338192b3736.jpg

---

## Lecture: L09-Greedy\page_062\L09-Greedy_page_062\auto

# Brief Aside – Cuts in Graphs

Proof of Lemma

• Assume that we have: – a cut that respects S – S is part of some MST T.

• Say that $\{ \boldsymbol { \mathbf { u } } , \boldsymbol { \mathbf { \check { v } } } \}$ is light. – lowest cost crossing the cut

• Say $\{ \mathfrak { u } , \mathfrak { v } \}$ is not in T. – Note that adding $\{ \boldsymbol { \mathbf { u } } , \boldsymbol { \mathbf { v } } \}$ to T will make a cycle.

![](images/ff866c6f17598c92df40f8bca43c212e173fb1de5fc9bcd1720f307bd40091bc.jpg)

• There is at least one other edge, $\{ x , y \}$

### Images:
- data\Design and Analysis of Algorithms\L09-Greedy\page_062\L09-Greedy_page_062\auto\images\ff866c6f17598c92df40f8bca43c212e173fb1de5fc9bcd1720f307bd40091bc.jpg

---

## Lecture: L09-Greedy\page_063\L09-Greedy_page_063\auto

# Brief Aside – Cuts in Graphs

Proof of Lemma ctd.

• Consider swapping $\{ \mathfrak { u } , \mathfrak { v } \}$ for {x,y} in T. – Call the resulting tree T’.

![](images/7c26f4df92a623a2377e90f91476408684c4e73d60d1d33e5eea48d16911c5b8.jpg)

### Images:
- data\Design and Analysis of Algorithms\L09-Greedy\page_063\L09-Greedy_page_063\auto\images\7c26f4df92a623a2377e90f91476408684c4e73d60d1d33e5eea48d16911c5b8.jpg

---

## Lecture: L09-Greedy\page_064\L09-Greedy_page_064\auto

# Brief Aside – Cuts in Graphs

Proof of Lemma ctd.

• Consider swapping $\{ \mathfrak { u } , \mathfrak { v } \}$ for {x,y} in T. – Call the resulting tree T’.

• Claim: T’ is still an MST.

– It is still a spanning tree (why?) – It has cost at most that of $\boldsymbol { \mathsf { T } }$ – $\boldsymbol { \mathsf { T } }$ had minimal cost. – So ${ \boldsymbol { \mathsf { T } } } ^ { \prime }$ does too.

• So ${ \bar { \mathbb { T } } } ^ { \prime }$ is an MST containing S and {u,v}.

![](images/3390e922620dc64dda8670697f76a8c2d532d3b4696c4ba1af795aae235319ad.jpg)

### Images:
- data\Design and Analysis of Algorithms\L09-Greedy\page_064\L09-Greedy_page_064\auto\images\3390e922620dc64dda8670697f76a8c2d532d3b4696c4ba1af795aae235319ad.jpg

---

## Lecture: L09-Greedy\page_065\L09-Greedy_page_065\auto

# How to find an MST

• How do we find one?

• Today we’ll see two greedy algorithms.

• The strategy:

– Make a series of choices, adding edges to the tree.

– Show that each edge we add is safe to add:

● we do not rule out the possibility of success

we will choose light edges crossing cuts and use the Lemma.

– Keep going until we have an MST.

---

## Lecture: L09-Greedy\page_066\L09-Greedy_page_066\auto

# How to find an MST

# Idea:

Start growing a tree, greedily add the shortest edge we can to grow the tree.

![](images/d152ee4c9473e2f247ab0846a28ef1f45a0b75bc45349b73b92b6f3bdb9138a6.jpg)

### Images:
- data\Design and Analysis of Algorithms\L09-Greedy\page_066\L09-Greedy_page_066\auto\images\d152ee4c9473e2f247ab0846a28ef1f45a0b75bc45349b73b92b6f3bdb9138a6.jpg

---

## Lecture: L09-Greedy\page_067\L09-Greedy_page_067\auto

# How to find an MST

# Idea:

Start growing a tree, greedily add the shortest edge we can to grow the tree.

![](images/6b1646ef9f33193ec059145a4615a6145245261b94078fde1bec9e2c21151a9f.jpg)

### Images:
- data\Design and Analysis of Algorithms\L09-Greedy\page_067\L09-Greedy_page_067\auto\images\6b1646ef9f33193ec059145a4615a6145245261b94078fde1bec9e2c21151a9f.jpg

---

## Lecture: L09-Greedy\page_068\L09-Greedy_page_068\auto

# How to find an MST

# Idea:

Start growing a tree, greedily add the shortest edge we can to grow the tree.

![](images/ed1529635f7172f8aa7781040327cf9b9436ac88a9eaa9e20fdbc02c921544ed.jpg)

### Images:
- data\Design and Analysis of Algorithms\L09-Greedy\page_068\L09-Greedy_page_068\auto\images\ed1529635f7172f8aa7781040327cf9b9436ac88a9eaa9e20fdbc02c921544ed.jpg

---

## Lecture: L09-Greedy\page_069\L09-Greedy_page_069\auto

# How to find an MST

# Idea:

Start growing a tree, greedily add the shortest edge we can to grow the tree.

![](images/6379ca2c1f0e6268af5ea324941e767965fe2d9d7f779fb19cb5c9314ec4c040.jpg)

### Images:
- data\Design and Analysis of Algorithms\L09-Greedy\page_069\L09-Greedy_page_069\auto\images\6379ca2c1f0e6268af5ea324941e767965fe2d9d7f779fb19cb5c9314ec4c040.jpg

---

## Lecture: L09-Greedy\page_070\L09-Greedy_page_070\auto

# How to find an MST

# Idea:

Start growing a tree, greedily add the shortest edge we can to grow the tree.

![](images/d26b06efbea689f75d90e6cff98e99fc28adabb4e760ba101929566b5ab48356.jpg)

### Images:
- data\Design and Analysis of Algorithms\L09-Greedy\page_070\L09-Greedy_page_070\auto\images\d26b06efbea689f75d90e6cff98e99fc28adabb4e760ba101929566b5ab48356.jpg

---

## Lecture: L09-Greedy\page_071\L09-Greedy_page_071\auto

# How to find an MST

# Idea:

Start growing a tree, greedily add the shortest edge we can to grow the tree.

![](images/e1e75abf7fa0481e5ccc6fcb1a4f664665dbce334cc6221366e70ce36b46b6af.jpg)

### Images:
- data\Design and Analysis of Algorithms\L09-Greedy\page_071\L09-Greedy_page_071\auto\images\e1e75abf7fa0481e5ccc6fcb1a4f664665dbce334cc6221366e70ce36b46b6af.jpg

---

## Lecture: L09-Greedy\page_072\L09-Greedy_page_072\auto

# How to find an MST

# Idea:

Start growing a tree, greedily add the shortest edge we can to grow the tree.

![](images/99aae1c0396e9e4609f4646e317ed4fa4e0837d54e5ae6ed7c0c02e19238d8a6.jpg)

### Images:
- data\Design and Analysis of Algorithms\L09-Greedy\page_072\L09-Greedy_page_072\auto\images\99aae1c0396e9e4609f4646e317ed4fa4e0837d54e5ae6ed7c0c02e19238d8a6.jpg

---

## Lecture: L09-Greedy\page_073\L09-Greedy_page_073\auto

# How to find an MST

# Idea:

Start growing a tree, greedily add the shortest edge we can to grow the tree.

![](images/0e37998d73613013c6f94268f48ece111f9d4fc0192bf27d09a9073cb00f1c48.jpg)

### Images:
- data\Design and Analysis of Algorithms\L09-Greedy\page_073\L09-Greedy_page_073\auto\images\0e37998d73613013c6f94268f48ece111f9d4fc0192bf27d09a9073cb00f1c48.jpg

---

## Lecture: L09-Greedy\page_074\L09-Greedy_page_074\auto

# How to find an MST

# Idea:

Start growing a tree, greedily add the shortest edge we can to grow the tree.

![](images/e82008a93db32e47914318b477f6dfde802cacd22050f0705df05c41c8a29b41.jpg)

### Images:
- data\Design and Analysis of Algorithms\L09-Greedy\page_074\L09-Greedy_page_074\auto\images\e82008a93db32e47914318b477f6dfde802cacd22050f0705df05c41c8a29b41.jpg

---

## Lecture: L09-Greedy\page_075\L09-Greedy_page_075\auto

# Prim’s Algorithm

# We’ve discovered Prim’s algorithm!

• slowPrim( $\mathsf { G } = ( \mathsf { V } , \mathsf { E } )$ , starting vertex s ):

• $M S T = \{ \}$

• verticesVisite $ \mathsf { d } = \{ \mathsf { s } \}$

• while |verticesVisited $| < | \mathsf { V } |$ :

• find the lightest edge $\{ { \sf x } , { \sf v } \}$ in E so that:

• v is not in verticesVisited

• add $\{ { \sf x } , { \sf v } \}$ to MST

• add $\boldsymbol { \mathsf { V } }$ to verticesVisited

• return MST

# Naively, the running time is O(nm):

• For each of ≤n-1 iterations of the while loop:

Go through all the edges.

---

## Lecture: L09-Greedy\page_076\L09-Greedy_page_076\auto

Two questions

1. Does it work?

– That is, does it actually return a MST?

2. How do we actually implement this?

– the pseudocode above says “slowPrim”

---

## Lecture: L09-Greedy\page_077\L09-Greedy_page_077\auto

# Does it work?

• We need to show that our greedy choices don’t rule out success.

• That is, at every step:

– If there exists an MST that contains all of the edges S we have added so far… – …then when we make our next choice {u,v}, there is still an MST containing S and {u,v}.

• Now it is time to use our lemma!

---

## Lecture: L09-Greedy\page_078\L09-Greedy_page_078\auto

# Prim’s Algorithm

Lemma

• Let S be a set of edges, and consider a cut that respects S.

• Suppose there is an MST containing S.

• Let $\{ \mathfrak { u } , \mathfrak { v } \}$ be a light edge.

This edge is light

• Then there is an MST containing S ∪ {{u,v}}

![](images/719dd966faf01b93508e30fcfd17af35857678a9fe36717603b0cf9902cad2b5.jpg)

### Images:
- data\Design and Analysis of Algorithms\L09-Greedy\page_078\L09-Greedy_page_078\auto\images\719dd966faf01b93508e30fcfd17af35857678a9fe36717603b0cf9902cad2b5.jpg

---

## Lecture: L09-Greedy\page_079\L09-Greedy_page_079\auto

# • Assume that our choices S so far don’t rule out success

– There is an MST consistent with those choices How can we use our lemma to show that our next choice also does not rule out success?

S is the set of edges selected so far

![](images/b4e7f6169caf303466cbac274b90c5fa562aa34800fdb44fddf6058471e62b2c.jpg)

### Images:
- data\Design and Analysis of Algorithms\L09-Greedy\page_079\L09-Greedy_page_079\auto\images\b4e7f6169caf303466cbac274b90c5fa562aa34800fdb44fddf6058471e62b2c.jpg

---

## Lecture: L09-Greedy\page_080\L09-Greedy_page_080\auto

# Prim’s Algorithm

• Assume that our choices S so far don’t rule out success – There is an MST consistent with those choices

• Consider the cut {visited, unvisited} – This cut respects S.

S is the set of edges selected so far

![](images/1e91337b5d46765d3e043e2c1908e73c586f7831f3333325785993c04c3d39c2.jpg)

### Images:
- data\Design and Analysis of Algorithms\L09-Greedy\page_080\L09-Greedy_page_080\auto\images\1e91337b5d46765d3e043e2c1908e73c586f7831f3333325785993c04c3d39c2.jpg

---

## Lecture: L09-Greedy\page_081\L09-Greedy_page_081\auto

# Prim’s Algorithm

• Assume that our choices S so far don’t rule out success There is an MST consistent with those choices

• Consider the cut {visited, unvisited} – This cut respects S.

S is the set of edges selected so far

• The edge we add next is a light edge. – Least weight of any edge crossing the cut.

• By the Lemma, that edge is safe to add

– There is still an MST consistent with the new set of edges.

![](images/502340f59ff62e9769edb4a0cb16fc5999995d96ee1b9fdf26ae91b2b0cf1495.jpg)

add this one next

### Images:
- data\Design and Analysis of Algorithms\L09-Greedy\page_081\L09-Greedy_page_081\auto\images\502340f59ff62e9769edb4a0cb16fc5999995d96ee1b9fdf26ae91b2b0cf1495.jpg

---

## Lecture: L09-Greedy\page_082\L09-Greedy_page_082\auto

# Prim’s Algorithm

Formally,

• Inductive hypothesis:

– After adding the t’th edge, there exists an MST with the edges added so far.

• Base case:

– In the beginning, with no edges added, there exists an MST containing all the (zero) edges added so far. YEP.

• Inductive step:

– If the inductive hypothesis holds for t (aka, the choices so far are safe), then it holds for t+1 (aka, the next edge we add is safe).

– That’s what we just showed.

• Conclusion:

– After adding the n-1’st edge, there exists an MST with the edges added so far.

– At this point, we have a spanning tree, so it better be a minimum spanning tree.

---

## Lecture: L09-Greedy\page_083\L09-Greedy_page_083\auto

Two questions

1. Does it work?

– That is, does it actually return a MST? • YES!

2. How do we actually implement this? – the pseudocode above says “slowPrim”

---

## Lecture: L09-Greedy\page_084\L09-Greedy_page_084\auto

# Efficient Implementation

• Each vertex keeps:

– how to get there.

![](images/61435391660570332699d1f1ff8057c725fde52bb7cb24f8f1069272d634ac14.jpg)

### Images:
- data\Design and Analysis of Algorithms\L09-Greedy\page_084\L09-Greedy_page_084\auto\images\61435391660570332699d1f1ff8057c725fde52bb7cb24f8f1069272d634ac14.jpg

---

## Lecture: L09-Greedy\page_085\L09-Greedy_page_085\auto

# Efficient Implementation

• Each vertex keeps:

![](images/e3a4399f2aadbc7776a7ebae3a3d39783851b55ddf732b43ea9aff1e769fa4a8.jpg)

### Images:
- data\Design and Analysis of Algorithms\L09-Greedy\page_085\L09-Greedy_page_085\auto\images\e3a4399f2aadbc7776a7ebae3a3d39783851b55ddf732b43ea9aff1e769fa4a8.jpg

---

## Lecture: L09-Greedy\page_086\L09-Greedy_page_086\auto

# Prim’s Algorithm

# Efficient Implementation

• Each vertex keeps:

– the (single-edge) distance from itself to the growing spanning tree – how to get there.

• Choose the closest vertex, add it.

• Update stored info.

![](images/6d7f308c92a0fa9b40eb83fbdcc7b729f03f0f136167fbaf9942842f7262139d.jpg)

### Images:
- data\Design and Analysis of Algorithms\L09-Greedy\page_086\L09-Greedy_page_086\auto\images\6d7f308c92a0fa9b40eb83fbdcc7b729f03f0f136167fbaf9942842f7262139d.jpg

---

## Lecture: L09-Greedy\page_087\L09-Greedy_page_087\auto

# Prim’s Algorithm

# Efficient Implementation

Every vertex has a key and a parent

![](images/e328c7d95e8997bf7f9a0d3c9107f1b96e3c8363856f74f890b42d52c702aa54.jpg)

Can’t reach x yet x is “active” Can reach x

????[x]

k[x] is the distance of x from the growing tree

![](images/147179c3423199c3309cbb68832f1531d7a73e500d88230db31b3ec6ba90384a.jpg)

${ \mathsf { p } } [ { \mathsf { b } } ] = \mathsf { a } .$ , meaning that a was the vertex that k[b] comes from.

![](images/ec23c807c1f51de9fd3f87749abdb544f4ed3ae9c63aa09e786876a71279342a.jpg)

Until all the vertices are reached:

Activate the unreached vertex u with the smallest key.

• for each of u’s unreached neighbors v:

● $\mathsf { k } [ \mathsf { v } ] = \mathsf { m i n } ( \mathsf { k } [ \mathsf { v } ] ,$ , weight(u,v) )

if k[v] updated, $\mathsf { p } [ \mathsf { v } ] = \mathsf { u }$

### Images:
- data\Design and Analysis of Algorithms\L09-Greedy\page_087\L09-Greedy_page_087\auto\images\147179c3423199c3309cbb68832f1531d7a73e500d88230db31b3ec6ba90384a.jpg
- data\Design and Analysis of Algorithms\L09-Greedy\page_087\L09-Greedy_page_087\auto\images\e328c7d95e8997bf7f9a0d3c9107f1b96e3c8363856f74f890b42d52c702aa54.jpg
- data\Design and Analysis of Algorithms\L09-Greedy\page_087\L09-Greedy_page_087\auto\images\ec23c807c1f51de9fd3f87749abdb544f4ed3ae9c63aa09e786876a71279342a.jpg

---

## Lecture: L09-Greedy\page_088\L09-Greedy_page_088\auto

# Prim’s Algorithm

# Efficient Implementation

Every vertex has a key and a parent

![](images/1168f7dbdf4ac72cd6f4ebcde7ef824deb7c1873b45f3d243918b93c547245d3.jpg)

Can’t reach x yet x is “active” Can reach x

????[x]

k[x] is the distance of x from the growing tree

![](images/0d43a1163c9f7a21d4be4707e22ac6cb4ede0e5a10b9445774d64b6858697937.jpg)

${ \mathsf { p } } [ { \mathsf { b } } ] = \mathsf { a } .$ , meaning that a was the vertex that k[b] comes from.

![](images/f7b7b77a283d1377416daa58dbb842840052e6e1b1a47357b9106366ba3cc708.jpg)

Until all the vertices are reached:

Activate the unreached vertex u with the smallest key.

• for each of u’s unreached neighbors v:

● $\mathsf { k } [ \mathsf { v } ] = \mathsf { m i n } ( \mathsf { k } [ \mathsf { v } ] ,$ , weight(u,v) )

if k[v] updated, $\mathsf { p } [ \mathsf { v } ] = \mathsf { u }$

### Images:
- data\Design and Analysis of Algorithms\L09-Greedy\page_088\L09-Greedy_page_088\auto\images\0d43a1163c9f7a21d4be4707e22ac6cb4ede0e5a10b9445774d64b6858697937.jpg
- data\Design and Analysis of Algorithms\L09-Greedy\page_088\L09-Greedy_page_088\auto\images\1168f7dbdf4ac72cd6f4ebcde7ef824deb7c1873b45f3d243918b93c547245d3.jpg
- data\Design and Analysis of Algorithms\L09-Greedy\page_088\L09-Greedy_page_088\auto\images\f7b7b77a283d1377416daa58dbb842840052e6e1b1a47357b9106366ba3cc708.jpg

---

## Lecture: L09-Greedy\page_089\L09-Greedy_page_089\auto

# Prim’s Algorithm

# Efficient Implementation

Every vertex has a key and a parent

![](images/41f4209804e8aba0a35d1b8815e4a3395f9ac92803ed912b3cb0b314414db813.jpg)

Can’t reach x yet x is “active” Can reach x

????[x]

k[x] is the distance of x from the growing tree

![](images/cba21911378dfa808e2def5bc228bd379ed1e7c04fdf4f700965e02dfac05f03.jpg)

${ \mathsf { p } } [ { \mathsf { b } } ] = \mathsf { a } .$ , meaning that a was the vertex that k[b] comes from.

![](images/8f2d60ac5fe09b9f79c30898dc14bb56eacffd12aa59bf7071221929e5fdc07d.jpg)

Until all the vertices are reached:

Activate the unreached vertex u with the smallest key.

• for each of u’s unreached neighbors v:

● $\mathsf { k } [ \mathsf { v } ] = \mathsf { m i n } ( \mathsf { k } [ \mathsf { v } ] ,$ , weight(u,v) )

if k[v] updated, $\mathsf { p } [ \mathsf { v } ] = \mathsf { u }$

### Images:
- data\Design and Analysis of Algorithms\L09-Greedy\page_089\L09-Greedy_page_089\auto\images\41f4209804e8aba0a35d1b8815e4a3395f9ac92803ed912b3cb0b314414db813.jpg
- data\Design and Analysis of Algorithms\L09-Greedy\page_089\L09-Greedy_page_089\auto\images\8f2d60ac5fe09b9f79c30898dc14bb56eacffd12aa59bf7071221929e5fdc07d.jpg
- data\Design and Analysis of Algorithms\L09-Greedy\page_089\L09-Greedy_page_089\auto\images\cba21911378dfa808e2def5bc228bd379ed1e7c04fdf4f700965e02dfac05f03.jpg

---

## Lecture: L09-Greedy\page_090\L09-Greedy_page_090\auto

# Prim’s Algorithm

# Efficient Implementation

Every vertex has a key and a parent

![](images/332ceaea55b17bfe1e1c5314f01fb65337b0b68feb71229fcdfead6b79fb3aa5.jpg)

Can’t reach x yet x is “active” Can reach x

????[x]

k[x] is the distance of x from the growing tree

![](images/1caca02fc2f43d3985b84363cf6f1986009ba1f302f6cd4f3f51719c2ef8e23f.jpg)

${ \mathsf { p } } [ { \mathsf { b } } ] = \mathsf { a } .$ , meaning that a was the vertex that k[b] comes from.

![](images/10cb2f527b9a53ceb1f0670f68306cc49149ba1467a908b0bdce2e5d031040e4.jpg)

Until all the vertices are reached:

Activate the unreached vertex u with the smallest key.

• for each of u’s unreached neighbors v:

● $\mathsf { k } [ \mathsf { v } ] = \mathsf { m i n } ( \mathsf { k } [ \mathsf { v } ] ,$ , weight(u,v) )

if k[v] updated, $\mathsf { p } [ \mathsf { v } ] = \mathsf { u }$

### Images:
- data\Design and Analysis of Algorithms\L09-Greedy\page_090\L09-Greedy_page_090\auto\images\10cb2f527b9a53ceb1f0670f68306cc49149ba1467a908b0bdce2e5d031040e4.jpg
- data\Design and Analysis of Algorithms\L09-Greedy\page_090\L09-Greedy_page_090\auto\images\1caca02fc2f43d3985b84363cf6f1986009ba1f302f6cd4f3f51719c2ef8e23f.jpg
- data\Design and Analysis of Algorithms\L09-Greedy\page_090\L09-Greedy_page_090\auto\images\332ceaea55b17bfe1e1c5314f01fb65337b0b68feb71229fcdfead6b79fb3aa5.jpg

---

## Lecture: L09-Greedy\page_091\L09-Greedy_page_091\auto

# Prim’s Algorithm

# Efficient Implementation

Every vertex has a key and a parent

![](images/707883011d63613943d157ee9069796dacbfde02f789af05fca023b2821657d1.jpg)

Can’t reach x yet x is “active” Can reach x

????[x]

k[x] is the distance of x from the growing tree

![](images/974ec88bf5dd804b26f8796e466c1afb25fed155bb4e596d85616f47f735f6ea.jpg)

${ \mathsf { p } } [ { \mathsf { b } } ] = \mathsf { a } .$ , meaning that a was the vertex that k[b] comes from.

![](images/5751c0015809e7731b719d883f5d64b704d01737e030bb7ac8eaaa5d9b83da92.jpg)

Until all the vertices are reached:

Activate the unreached vertex u with the smallest key.

• for each of u’s unreached neighbors v:

● $\mathsf { k } [ \mathsf { v } ] = \mathsf { m i n } ( \mathsf { k } [ \mathsf { v } ] ,$ , weight(u,v) )

if k[v] updated, $\mathsf { p } [ \mathsf { v } ] = \mathsf { u }$

### Images:
- data\Design and Analysis of Algorithms\L09-Greedy\page_091\L09-Greedy_page_091\auto\images\5751c0015809e7731b719d883f5d64b704d01737e030bb7ac8eaaa5d9b83da92.jpg
- data\Design and Analysis of Algorithms\L09-Greedy\page_091\L09-Greedy_page_091\auto\images\707883011d63613943d157ee9069796dacbfde02f789af05fca023b2821657d1.jpg
- data\Design and Analysis of Algorithms\L09-Greedy\page_091\L09-Greedy_page_091\auto\images\974ec88bf5dd804b26f8796e466c1afb25fed155bb4e596d85616f47f735f6ea.jpg

---

## Lecture: L09-Greedy\page_092\L09-Greedy_page_092\auto

# Prim’s Algorithm

# Efficient Implementation

Every vertex has a key and a parent

![](images/3ba776c8901d066296d601a3c91fac02facc0cd7e9c27f8e45ba9fd4c0cc25ac.jpg)

Can’t reach x yet x is “active” Can reach x

????[x]

k[x] is the distance of x from the growing tree

![](images/97e6eda93c901d7f61959bc11565b6b87e2eeba59feed71e15c77ca3f9fe7765.jpg)

${ \mathsf { p } } [ { \mathsf { b } } ] = \mathsf { a } .$ , meaning that a was the vertex that k[b] comes from.

![](images/da67483bcb41633c5b34ba36fd8d56cce29aa16bf6c893dbc3169f83ced4b071.jpg)

Until all the vertices are reached:

Activate the unreached vertex u with the smallest key.

• for each of u’s unreached neighbors v:

● $\mathsf { k } [ \mathsf { v } ] = \mathsf { m i n } ( \mathsf { k } [ \mathsf { v } ] ,$ , weight(u,v) )

if k[v] updated, $\mathsf { p } [ \mathsf { v } ] = \mathsf { u }$

### Images:
- data\Design and Analysis of Algorithms\L09-Greedy\page_092\L09-Greedy_page_092\auto\images\3ba776c8901d066296d601a3c91fac02facc0cd7e9c27f8e45ba9fd4c0cc25ac.jpg
- data\Design and Analysis of Algorithms\L09-Greedy\page_092\L09-Greedy_page_092\auto\images\97e6eda93c901d7f61959bc11565b6b87e2eeba59feed71e15c77ca3f9fe7765.jpg
- data\Design and Analysis of Algorithms\L09-Greedy\page_092\L09-Greedy_page_092\auto\images\da67483bcb41633c5b34ba36fd8d56cce29aa16bf6c893dbc3169f83ced4b071.jpg

---

## Lecture: L09-Greedy\page_093\L09-Greedy_page_093\auto

# Prim’s Algorithm

# Efficient Implementation

Every vertex has a key and a parent

![](images/e90a47ff20feb144caf4116b0a2dea317faf77e5f22d4fd8e663ba2b6bcd65ce.jpg)

Can’t reach x yet x is “active” Can reach x

????[x]

k[x] is the distance of x from the growing tree

![](images/c6d631a47c7e73a80937c06c4b04947b3e00e7b9705870b284f09343469d43fa.jpg)

${ \mathsf { p } } [ { \mathsf { b } } ] = \mathsf { a } .$ , meaning that a was the vertex that k[b] comes from.

![](images/755bdfaae8b0bc3d4d55fdb95295515c8d6eef13fc7327893c57fbafbd70f56e.jpg)

Until all the vertices are reached:

Activate the unreached vertex u with the smallest key.

• for each of u’s unreached neighbors v:

● $\mathsf { k } [ \mathsf { v } ] = \mathsf { m i n } ( \mathsf { k } [ \mathsf { v } ] ,$ , weight(u,v) )

if k[v] updated, $\mathsf { p } [ \mathsf { v } ] = \mathsf { u }$

### Images:
- data\Design and Analysis of Algorithms\L09-Greedy\page_093\L09-Greedy_page_093\auto\images\755bdfaae8b0bc3d4d55fdb95295515c8d6eef13fc7327893c57fbafbd70f56e.jpg
- data\Design and Analysis of Algorithms\L09-Greedy\page_093\L09-Greedy_page_093\auto\images\c6d631a47c7e73a80937c06c4b04947b3e00e7b9705870b284f09343469d43fa.jpg
- data\Design and Analysis of Algorithms\L09-Greedy\page_093\L09-Greedy_page_093\auto\images\e90a47ff20feb144caf4116b0a2dea317faf77e5f22d4fd8e663ba2b6bcd65ce.jpg

---

## Lecture: L09-Greedy\page_094\L09-Greedy_page_094\auto

# Prim’s Algorithm

# Efficient Implementation

Every vertex has a key and a parent

![](images/250c977dee6dcb96a44d63a7e76159269324d577a8c8814b02a55302b3abe498.jpg)

Can’t reach x yet x is “active” Can reach x

????[x]

k[x] is the distance of x from the growing tree

![](images/7c219ce3b597b6104707c7157a5ec171d366b72d5c02fb2647189623ca00bed6.jpg)

${ \mathsf { p } } [ { \mathsf { b } } ] = \mathsf { a } .$ , meaning that a was the vertex that k[b] comes from.

![](images/5113d832ab5b722fe840dfc04c18089b7729c27c706a5d9f9a508927ed895d6f.jpg)

Until all the vertices are reached:

Activate the unreached vertex u with the smallest key.

• for each of u’s unreached neighbors v:

● $\mathsf { k } [ \mathsf { v } ] = \mathsf { m i n } ( \mathsf { k } [ \mathsf { v } ] ,$ , weight(u,v) )

if k[v] updated, $\mathsf { p } [ \mathsf { v } ] = \mathsf { u }$

### Images:
- data\Design and Analysis of Algorithms\L09-Greedy\page_094\L09-Greedy_page_094\auto\images\250c977dee6dcb96a44d63a7e76159269324d577a8c8814b02a55302b3abe498.jpg
- data\Design and Analysis of Algorithms\L09-Greedy\page_094\L09-Greedy_page_094\auto\images\5113d832ab5b722fe840dfc04c18089b7729c27c706a5d9f9a508927ed895d6f.jpg
- data\Design and Analysis of Algorithms\L09-Greedy\page_094\L09-Greedy_page_094\auto\images\7c219ce3b597b6104707c7157a5ec171d366b72d5c02fb2647189623ca00bed6.jpg

---

## Lecture: L09-Greedy\page_095\L09-Greedy_page_095\auto

# Prim’s Algorithm

# Efficient Implementation

Every vertex has a key and a parent

![](images/bfd93d74d3001a1c510ea104d56d93b2b9e4331f1900d031e6de1031509de832.jpg)

Can’t reach x yet x is “active” Can reach x

????[x]

k[x] is the distance of x from the growing tree

![](images/bb6e43300d99c4617a42667050e5210361f74f486aec53a21ff96167ceeaf441.jpg)

${ \mathsf { p } } [ { \mathsf { b } } ] = \mathsf { a } .$ , meaning that a was the vertex that k[b] comes from.

![](images/5c19f6b3da0714d7659e79f4d26fb3a866e7d59bb9b991a78d4497fb2b47203b.jpg)

Until all the vertices are reached:

Activate the unreached vertex u with the smallest key.

• for each of u’s unreached neighbors v:

● $\mathsf { k } [ \mathsf { v } ] = \mathsf { m i n } ( \mathsf { k } [ \mathsf { v } ] ,$ , weight(u,v) )

if k[v] updated, $\mathsf { p } [ \mathsf { v } ] = \mathsf { u }$

### Images:
- data\Design and Analysis of Algorithms\L09-Greedy\page_095\L09-Greedy_page_095\auto\images\5c19f6b3da0714d7659e79f4d26fb3a866e7d59bb9b991a78d4497fb2b47203b.jpg
- data\Design and Analysis of Algorithms\L09-Greedy\page_095\L09-Greedy_page_095\auto\images\bb6e43300d99c4617a42667050e5210361f74f486aec53a21ff96167ceeaf441.jpg
- data\Design and Analysis of Algorithms\L09-Greedy\page_095\L09-Greedy_page_095\auto\images\bfd93d74d3001a1c510ea104d56d93b2b9e4331f1900d031e6de1031509de832.jpg

---

## Lecture: L09-Greedy\page_096\L09-Greedy_page_096\auto

# Prim’s Algorithm

# Efficient Implementation

Every vertex has a key and a parent

![](images/29a9add12e85d2e69ae293fa070708c74eb4ad50bf0f54b79867022451f4122e.jpg)

Can’t reach x yet x is “active” Can reach x

????[x]

k[x] is the distance of x from the growing tree

![](images/0c8d00ad6c4b570bba4cb353ce726d92b623e92177876ad5f0ef7b5fc1b1f0b4.jpg)

${ \mathsf { p } } [ { \mathsf { b } } ] = \mathsf { a } .$ , meaning that a was the vertex that k[b] comes from.

![](images/c54eb3c70b86def07d70bdb0fedfd52830ea5dbb0884e51cce430c6af0eb39f9.jpg)

Until all the vertices are reached:

Activate the unreached vertex u with the smallest key.

• for each of u’s unreached neighbors v:

● $\mathsf { k } [ \mathsf { v } ] = \mathsf { m i n } ( \mathsf { k } [ \mathsf { v } ] ,$ , weight(u,v) )

if k[v] updated, $\mathsf { p } [ \mathsf { v } ] = \mathsf { u }$

### Images:
- data\Design and Analysis of Algorithms\L09-Greedy\page_096\L09-Greedy_page_096\auto\images\0c8d00ad6c4b570bba4cb353ce726d92b623e92177876ad5f0ef7b5fc1b1f0b4.jpg
- data\Design and Analysis of Algorithms\L09-Greedy\page_096\L09-Greedy_page_096\auto\images\29a9add12e85d2e69ae293fa070708c74eb4ad50bf0f54b79867022451f4122e.jpg
- data\Design and Analysis of Algorithms\L09-Greedy\page_096\L09-Greedy_page_096\auto\images\c54eb3c70b86def07d70bdb0fedfd52830ea5dbb0884e51cce430c6af0eb39f9.jpg

---

## Lecture: L09-Greedy\page_097\L09-Greedy_page_097\auto

# Prim’s Algorithm

• Very similar to Dijkstra’s algorithm!

# • Differences:

1. Keep track of p[v] in order to return a tree at the end But Dijkstra’s can do that too, that’s not a big difference.

2. Instead of ${ \mathsf { d } } [ { \mathsf { v } } ]$ which we update by の $\mathsf { d } [ \mathsf { v } ] = \mathsf { m i n } ( \mathsf { d } [ \mathsf { v } ] , \mathsf { d } [ \mathsf { u } ] + \mathsf { w } ( \mathsf { u } , \mathsf { v } ) \ )$ we keep $\mathsf { k } [ \mathsf { v } ]$ which we update by $\mathsf { k } [ \mathsf { v } ] = \mathsf { m i n } ( \mathsf { k } [ \mathsf { v } ] , \mathsf { w } ( \mathsf { u } , \mathsf { v } )$ )

Thing 2 is the main difference.

### Images:
- data\Design and Analysis of Algorithms\L09-Greedy\page_097\L09-Greedy_page_097\auto\images\18d720e8676509bb3dc0d839016feeff46a765ceb4dcde71710db0315b7ec002.jpg

---

## Lecture: L09-Greedy\page_098\L09-Greedy_page_098\auto

Two questions

1. Does it work?

– That is, does it actually return a MST? • YES!

2. How do we actually implement this?

– the pseudocode above says “slowPrim”

• Implement it basically the same way we’d implement Dijkstra!

---

## Lecture: L09-Greedy\page_099\L09-Greedy_page_099\auto

# That’s not the only greedy algorithm for MST!

---

## Lecture: L09-Greedy\page_100\L09-Greedy_page_100\auto

what if we just always take the cheapest edge? whether or not it’s connected to what we have so far?

![](images/78b70172f78550076df169f96491641df64d8c1a7259a781462d97d97774281b.jpg)

### Images:
- data\Design and Analysis of Algorithms\L09-Greedy\page_100\L09-Greedy_page_100\auto\images\78b70172f78550076df169f96491641df64d8c1a7259a781462d97d97774281b.jpg

---

## Lecture: L09-Greedy\page_101\L09-Greedy_page_101\auto

what if we just always take the cheapest edge? whether or not it’s connected to what we have so far?

![](images/957c4c23c8793f89f8137c4e29be614dcd68df19237cb53f91044d3eabd00ad5.jpg)

### Images:
- data\Design and Analysis of Algorithms\L09-Greedy\page_101\L09-Greedy_page_101\auto\images\957c4c23c8793f89f8137c4e29be614dcd68df19237cb53f91044d3eabd00ad5.jpg

---

## Lecture: L09-Greedy\page_102\L09-Greedy_page_102\auto

what if we just always take the cheapest edge? whether or not it’s connected to what we have so far?

![](images/a872874a207267aa322bd817fee0b7d87339a93e8d05f9a65bd14459c2cd9888.jpg)

### Images:
- data\Design and Analysis of Algorithms\L09-Greedy\page_102\L09-Greedy_page_102\auto\images\a872874a207267aa322bd817fee0b7d87339a93e8d05f9a65bd14459c2cd9888.jpg

---

## Lecture: L09-Greedy\page_103\L09-Greedy_page_103\auto

what if we just always take the cheapest edge? whether or not it’s connected to what we have so far?

![](images/51854faaad151afeecd7bc6008114e7944fbad85e481aa602b08c67d0b998f9f.jpg)

### Images:
- data\Design and Analysis of Algorithms\L09-Greedy\page_103\L09-Greedy_page_103\auto\images\51854faaad151afeecd7bc6008114e7944fbad85e481aa602b08c67d0b998f9f.jpg

---

## Lecture: L09-Greedy\page_104\L09-Greedy_page_104\auto

what if we just always take the cheapest edge? whether or not it’s connected to what we have so far?

![](images/dfb70b48e62087494f6b283ff9e51e5dd394222ab4836d0c08c4314520f0a844.jpg)

### Images:
- data\Design and Analysis of Algorithms\L09-Greedy\page_104\L09-Greedy_page_104\auto\images\dfb70b48e62087494f6b283ff9e51e5dd394222ab4836d0c08c4314520f0a844.jpg

---

## Lecture: L09-Greedy\page_105\L09-Greedy_page_105\auto

what if we just always take the cheapest edge? whether or not it’s connected to what we have so far?

![](images/d6ca6aedc750d93b8b616ede28a2649e6fa3eab519fd2218763dca51801da1a6.jpg)

### Images:
- data\Design and Analysis of Algorithms\L09-Greedy\page_105\L09-Greedy_page_105\auto\images\d6ca6aedc750d93b8b616ede28a2649e6fa3eab519fd2218763dca51801da1a6.jpg

---

## Lecture: L09-Greedy\page_106\L09-Greedy_page_106\auto

what if we just always take the cheapest edge? whether or not it’s connected to what we have so far?

![](images/586aa1b9db188462c93dcc270755fe1fd12a4f481536d44dcf2002fa7911bdf6.jpg)

### Images:
- data\Design and Analysis of Algorithms\L09-Greedy\page_106\L09-Greedy_page_106\auto\images\586aa1b9db188462c93dcc270755fe1fd12a4f481536d44dcf2002fa7911bdf6.jpg

---

## Lecture: L09-Greedy\page_107\L09-Greedy_page_107\auto

what if we just always take the cheapest edge? whether or not it’s connected to what we have so far?

![](images/56c9b5b77ae9c6b9ab8204515a60704f20195c2e06a25df99878f8a6268fc49c.jpg)

### Images:
- data\Design and Analysis of Algorithms\L09-Greedy\page_107\L09-Greedy_page_107\auto\images\56c9b5b77ae9c6b9ab8204515a60704f20195c2e06a25df99878f8a6268fc49c.jpg

---

## Lecture: L09-Greedy\page_108\L09-Greedy_page_108\auto

what if we just always take the cheapest edge? whether or not it’s connected to what we have so far?

![](images/08f782e4261d268ef2368cbd17bfab8a0a10875151e22ef9f7c57f938470ec33.jpg)

### Images:
- data\Design and Analysis of Algorithms\L09-Greedy\page_108\L09-Greedy_page_108\auto\images\08f782e4261d268ef2368cbd17bfab8a0a10875151e22ef9f7c57f938470ec33.jpg

---

## Lecture: L09-Greedy\page_109\L09-Greedy_page_109\auto

what if we just always take the cheapest edge? whether or not it’s connected to what we have so far?

![](images/20404f303630a29e5c012c15f137c674284cd5eab4c5395047ba91d61152dfb1.jpg)

### Images:
- data\Design and Analysis of Algorithms\L09-Greedy\page_109\L09-Greedy_page_109\auto\images\20404f303630a29e5c012c15f137c674284cd5eab4c5395047ba91d61152dfb1.jpg

---

## Lecture: L09-Greedy\page_110\L09-Greedy_page_110\auto

what if we just always take the cheapest edge? whether or not it’s connected to what we have so far?

![](images/013712e0d0d07b3c9d17cee5e78fb36c1f7489bbed68300351766efc4864d497.jpg)

### Images:
- data\Design and Analysis of Algorithms\L09-Greedy\page_110\L09-Greedy_page_110\auto\images\013712e0d0d07b3c9d17cee5e78fb36c1f7489bbed68300351766efc4864d497.jpg

---

## Lecture: L09-Greedy\page_111\L09-Greedy_page_111\auto

what if we just always take the cheapest edge? whether or not it’s connected to what we have so far?

![](images/5aa56ed759b70aa18bf48d533576e1816db5e51f6dd1fa3078c73b330ba4c198.jpg)

### Images:
- data\Design and Analysis of Algorithms\L09-Greedy\page_111\L09-Greedy_page_111\auto\images\5aa56ed759b70aa18bf48d533576e1816db5e51f6dd1fa3078c73b330ba4c198.jpg

---

## Lecture: L09-Greedy\page_112\L09-Greedy_page_112\auto

# Kruskal’s Algorithm

• slowKruskal $\mathbf { \check { G } } = \left( \mathsf { V } , \mathsf { E } \right) )$ :

– Sort the edges in E by non-decreasing weight.   
$- M S T = \{ \}$   
– for e in E (in sorted order): m iterations through this loop • if adding e to MST won’t cause a cycle: – add e to MST. How do we check this?   
– return MST

---

## Lecture: L09-Greedy\page_113\L09-Greedy_page_113\auto

# At each step of Kruskal’s, we are maintaining a forest.

![](images/ce582009e4676b4a3b9d76a3b0f5047eef91dc2defd6086ddfaf0956f84043a5.jpg)

### Images:
- data\Design and Analysis of Algorithms\L09-Greedy\page_113\L09-Greedy_page_113\auto\images\ce582009e4676b4a3b9d76a3b0f5047eef91dc2defd6086ddfaf0956f84043a5.jpg

---

## Lecture: L09-Greedy\page_114\L09-Greedy_page_114\auto

# Kruskal’s Algorithm

At each step of Kruskal’s, we are maintaining a forest.

When we add an edge, we merge two trees:

![](images/8e2e8532d50c0befe2003be6b1ce6577c672b3fdf9f63e55467dcacc393bbd3b.jpg)

### Images:
- data\Design and Analysis of Algorithms\L09-Greedy\page_114\L09-Greedy_page_114\auto\images\8e2e8532d50c0befe2003be6b1ce6577c672b3fdf9f63e55467dcacc393bbd3b.jpg

---

## Lecture: L09-Greedy\page_115\L09-Greedy_page_115\auto

# Kruskal’s Algorithm

Union-find data structure

• Used for storing collections of sets

• Supports:

– makeSet(u): create a set {u}   
find(u): return the set that u is in   
union(u,v): merge the set that u is in with the set that v is in.

x

y

makeSet(x) makeSet(y) makeSet(z)

union(x,y)

---

## Lecture: L09-Greedy\page_116\L09-Greedy_page_116\auto

# Kruskal’s Algorithm

Union-find data structure

• Used for storing collections of sets

• Supports:

– makeSet(u): create a set {u}   
find(u): return the set that u is in   
union(u,v): merge the set that u is in with the set that v is in.

x

y

makeSet(x) makeSet(y) makeSet(z)

union(x,y)

z

---

## Lecture: L09-Greedy\page_117\L09-Greedy_page_117\auto

# Kruskal’s Algorithm

Union-find data structure

• Used for storing collections of sets

• Supports:

– makeSet(u): create a set {u}   
– find(u): return the set that u is in   
union(u,v): merge the set that u is in with the set that v is in.

x

y

makeSet(x) makeSet(y) makeSet(z)

union(x,y) find(x)

z

---

## Lecture: L09-Greedy\page_118\L09-Greedy_page_118\auto

# Kruskal’s Algorithm

• kruskal $\mathbf { \check { G } } = \left( \mathsf { V } , \mathsf { E } \right) )$

– Sort E by weight in non-decreasing order

// initialize an empty tree

$- M S T = \{ \}$   
– for v in V: • makeSet(v)   
– for $( \mathsf { u } , \mathsf { v } )$ in E: • if find(u) ! ${ } = { }$ find(v): – add (u,v) to MST $- \mathrm { \ u n i o n ( u , v ) }$   
– return MST

// put each vertex in its own tree in the forest // go through the edges in sorted order // if u and v are not in the same tree

// merge u’s tree with v’s tree

### Images:
- data\Design and Analysis of Algorithms\L09-Greedy\page_118\L09-Greedy_page_118\auto\images\1da65035849273e1157bcda58ac259d58fbdc5b06b6e999b2f009c27ae779a61.jpg

---

## Lecture: L09-Greedy\page_119\L09-Greedy_page_119\auto

# Kruskal’s Algorithm

Running time

• Sorting the edges takes O(m log(n))

– In practice, if the weights are small integers we can use radixSort and take time O(m)

• For the rest:

– n calls to makeSet

put each vertex in its own set

– 2m calls to find

for each edge, find its endpoints

– n-1 calls to union

we will never add more than n-1 edges to the tree,

● so we will never call union more than n-1 times.

• Total running time: O(mlog(n))

---

## Lecture: L09-Greedy\page_120\L09-Greedy_page_120\auto

Does it work?

Leave for your assignment.

---

## Lecture: L09-Greedy\page_121\L09-Greedy_page_121\auto

# Comparison

• Prim:

– Grows a tree. – Time O(mlog(n)) with a red-black tree – Time O(m + nlog(n)) with a Fibonacci heap

• Kruskal:

– Grows a forest. – Time O(mlog(n)) with a union-find data structure – If you can do radixSort on the weights, morally $" 0 ( \mathsf { m } ) ^ { \prime \prime }$

Prim might be a better idea on dense graphs if you can’t radixSort edge weights

Kruskal might be a better idea on sparse graphs if you can radixSort edge weights

---

## Lecture: L09-Greedy\page_122\L09-Greedy_page_122\auto

# Can we do better?

• Karger-Klein-Tarjan 1995: $- 0 ( { \mathsf { m } } )$ time randomized algorithm

• Chazelle 2000: $- \mathsf { O } ( \mathsf { m } \cdot \alpha ( n ) )$ time deterministic algorithm

• Pettie-Ramachandran 2002:

The optimal number of comparisons you need to solve the problem, time deterministic algorithm whatever that is…

---

## Lecture: L10-Graph\page_001\L10-Graph_page_001\auto

# 香港科技大学(广州）DSAA 2043 | Design and Analysis of Algorithms THE HONG KONSCIENCE ANDTECHNOLOGY (GUANGZHOU)

# Graph Algorithms (1)

Basic Definitions and Applications Graph Connectivity and Graph Traversal Connectivity in Directed Graphs DAGs & Topological Ordering

### Images:
- data\Design and Analysis of Algorithms\L10-Graph\page_001\L10-Graph_page_001\auto\images\828c4350eb5d17f1946fd32b569c19722d33da59abef915d150360c27823bf8b.jpg

---

## Lecture: L10-Graph\page_002\L10-Graph_page_002\auto

# Basic Definitions and Applications

---

## Lecture: L10-Graph\page_003\L10-Graph_page_003\auto

• A graph: a group of vertices and edges that are used to connect these vertices

• Definition: A graph G can be defined as an ordered set $G ( V , E )$

• ???? represents the set of vertices/nodes

• $E$ represents the set of edges which are used to connect ????

---

## Lecture: L10-Graph\page_004\L10-Graph_page_004\auto

# Applications: Social Network

![](images/5c31491446526abf6cfb7695d4ccc2f9ab734313b43a8f877a52c287206ca622.jpg)  
Figure 1.Largest Connected Subcomponent of the Social Network in the Framingham Heart Study in the Year 2000.   
Each circle (node) represents one person in the data set. There are 2200 persons in this subcomponent of the social network. Circles with red borders denote women, and circles with blue borders denote men. The size of each circle is proportional to the person’s body-mass index. The interior color of the circles indicates the person’s obesity status: yellow denotes an obese person (body-mass index, $\geq 3 0$ ) and green denotes a nonobese person. The colors of the ties between the nodes indicate the relationship between them: purple denotes a friendship or marital tie and orange denotes a familial tie.

### Images:
- data\Design and Analysis of Algorithms\L10-Graph\page_004\L10-Graph_page_004\auto\images\5c31491446526abf6cfb7695d4ccc2f9ab734313b43a8f877a52c287206ca622.jpg

---

## Lecture: L10-Graph\page_005\L10-Graph_page_005\auto

# Road Network

Node $=$ intersection; edge $=$ street.

![](images/653c951b12eb9fb68c62ad835cdcf6abf130b284366e88883723f668d3cc8787.jpg)

### Images:
- data\Design and Analysis of Algorithms\L10-Graph\page_005\L10-Graph_page_005\auto\images\653c951b12eb9fb68c62ad835cdcf6abf130b284366e88883723f668d3cc8787.jpg

---

## Lecture: L10-Graph\page_006\L10-Graph_page_006\auto

# More Applications

<table><tr><td rowspan=1 colspan=1>graph</td><td rowspan=1 colspan=1>node</td><td rowspan=1 colspan=1>edge</td></tr><tr><td rowspan=1 colspan=1>communication</td><td rowspan=1 colspan=1>telephone, computer</td><td rowspan=1 colspan=1>fiber optic cable</td></tr><tr><td rowspan=1 colspan=1>circuit</td><td rowspan=1 colspan=1>gate, register, processor</td><td rowspan=1 colspan=1>wire</td></tr><tr><td rowspan=1 colspan=1>mechanical</td><td rowspan=1 colspan=1>joint</td><td rowspan=1 colspan=1>rod, beam, spring</td></tr><tr><td rowspan=1 colspan=1>financial</td><td rowspan=1 colspan=1>stock, currency</td><td rowspan=1 colspan=1>transactions</td></tr><tr><td rowspan=1 colspan=1>transportation</td><td rowspan=1 colspan=1>street intersection, airport</td><td rowspan=1 colspan=1>highway, airway route</td></tr><tr><td rowspan=1 colspan=1>internet</td><td rowspan=1 colspan=1>class C network</td><td rowspan=1 colspan=1>connection</td></tr><tr><td rowspan=1 colspan=1>game</td><td rowspan=1 colspan=1>board position</td><td rowspan=1 colspan=1>legal move</td></tr><tr><td rowspan=1 colspan=1>social relationship</td><td rowspan=1 colspan=1>person, actor</td><td rowspan=1 colspan=1>friendship, movie cast</td></tr><tr><td rowspan=1 colspan=1>neural network</td><td rowspan=1 colspan=1>neuron</td><td rowspan=1 colspan=1>synapse</td></tr><tr><td rowspan=1 colspan=1>protein network</td><td rowspan=1 colspan=1>protein</td><td rowspan=1 colspan=1>protein-protein interaction</td></tr><tr><td rowspan=1 colspan=1>molecule</td><td rowspan=1 colspan=1>atom</td><td rowspan=1 colspan=1>bond</td></tr></table>

### Images:
- data\Design and Analysis of Algorithms\L10-Graph\page_006\L10-Graph_page_006\auto\images\2f5f705a91ad0db081ebf3ed9aa12b34b1e28663f0d627a0fc711371c88fd3b9.jpg

---

## Lecture: L10-Graph\page_007\L10-Graph_page_007\auto

# Sequential Representation

• Use adjacency matrix to store the mapping represented by vertices and edges

• In adjacency matrix, the rows and columns are represented by the graph vertices

• For a graph having ???? vertices, the adjacency matrix will have a dimension ???? × ????

---

## Lecture: L10-Graph\page_008\L10-Graph_page_008\auto

# Sequential Representation

• Undirected: an entry $A _ { i j }$ in the adjacency matrix will be 1 if there exists an edge between $v _ { i }$ and $v _ { j }$ .

![](images/da5930553da5171c579f12b5f30f472003c407596e728a6c2d0e7e941ff3d359.jpg)  
Undirected Graph

![](images/b44a8373ab5fd370c624bd4f4361727229916a55c125b40e937228e6682dc51d.jpg)  
Adjacency Matrix

### Images:
- data\Design and Analysis of Algorithms\L10-Graph\page_008\L10-Graph_page_008\auto\images\b44a8373ab5fd370c624bd4f4361727229916a55c125b40e937228e6682dc51d.jpg
- data\Design and Analysis of Algorithms\L10-Graph\page_008\L10-Graph_page_008\auto\images\da5930553da5171c579f12b5f30f472003c407596e728a6c2d0e7e941ff3d359.jpg

---

## Lecture: L10-Graph\page_009\L10-Graph_page_009\auto

# Linked Representation

• An adjacency list is used to store the Graph into the computer's memory

• An adjacency list is maintained for each node present in the graph which stores the node value and a pointer to the next adjacent node to the respective node

• If all the adjacent nodes are traversed, then store the NULL in the pointer field of last node of the list

---

## Lecture: L10-Graph\page_010\L10-Graph_page_010\auto

# Linked Representation

• Undirected: The sum of the lengths of adjacency lists is equal to the twice of the number of edges

![](images/24e1dacd790a3184aafbb17d69e2309dce823915ad1b1d5c42ccee9728b663d5.jpg)  
Undirected Graph

![](images/def9c1902c83da2430afb407d898cd78e04fd54bd597e71c54058ed229714286.jpg)

Adjacency List

### Images:
- data\Design and Analysis of Algorithms\L10-Graph\page_010\L10-Graph_page_010\auto\images\24e1dacd790a3184aafbb17d69e2309dce823915ad1b1d5c42ccee9728b663d5.jpg
- data\Design and Analysis of Algorithms\L10-Graph\page_010\L10-Graph_page_010\auto\images\def9c1902c83da2430afb407d898cd78e04fd54bd597e71c54058ed229714286.jpg

---

## Lecture: L10-Graph\page_011\L10-Graph_page_011\auto

# Terminology

Path: a sequence of edges connecting initial node $v _ { 0 }$ to terminal node $v _ { n }$

• Closed Path: A path where the initial node is same as terminal node, i.e., $v _ { 0 } = v _ { n }$

• Simple Path: all the nodes of the path are distinct, with the exception $v _ { 0 } = v _ { n }$

• Closed Simple Path: a simple path with $v _ { 0 } = v _ { n }$

• Cycle: a path which has no repeated edges or vertices except the first and last vertices

• Adjacent Nodes: two nodes ???? and ???? are connected via an edge ???? – the nodes ???? and ???? are also called as neighbors

• Degree of a Node: the number of edges that are connected with the node – A node with degree 0 is called as isolated node

---

## Lecture: L10-Graph\page_012\L10-Graph_page_012\auto

# Terminology

Connected Graph: a graph in which a path exists between every two vertices ????   
and ???? in ???? – There are no isolated nodes in connected graph

• Complete Graph: a graph in which there is an edge between each pair of vertices – A complete graph contain $n ( n - 1 ) / 2$ edges where $n$ is the number of nodes in the graph

• Weighted Graph: each edge is assigned with some data such as length or weight – The weight of an edge $e$ , $w ( e )$

Digraph: each edge of the graph is associated with some direction – The traversing can be done only in the specified direction

---

## Lecture: L10-Graph\page_013\L10-Graph_page_013\auto

# Graph Traversal

---

## Lecture: L10-Graph\page_014\L10-Graph_page_014\auto

# Connectivity

• ????−???? connectivity problem: Given two nodes ???? and ????, is there a path between ???? and ?????

• ????−???? shortest path problem: Given two nodes ???? and $t$ , what is the length of a shortest path between ???? and ?????

• Applications

– Friendster   
– Maze traversal   
– Kevin Bacon number   
– Fewest hops in a communication network

---

## Lecture: L10-Graph\page_015\L10-Graph_page_015\auto

# Graph Traversal

• Traversing the graph means examining all the nodes and vertices of the graph

• Two standard methods to traverse graphs

– Breadth First Search – Depth First Search

![](images/d339a6694b375a655d9b371d1797211a9e5bb34ea8ffb1e291b65045433982a0.jpg)

### Images:
- data\Design and Analysis of Algorithms\L10-Graph\page_015\L10-Graph_page_015\auto\images\d339a6694b375a655d9b371d1797211a9e5bb34ea8ffb1e291b65045433982a0.jpg

---

## Lecture: L10-Graph\page_016\L10-Graph_page_016\auto

# Depth First Search (Stack-Based)

• DFS: starts with the initial node, and then goes to deeper and deeper until we find the goal node or the node which has no children. The algorithm, then backtracks from the dead end towards the most recent node that is yet to be completely unexplored.

– Step 1: SET STATUS as UNVISITED (ready state) for each node in G   
• Step 2: Push the starting node A on the stack   
– Step 3: Repeat Steps 4 and 5 until STACK is empty   
– Step 4: Pop the top node N. If node N is VISITED, repeat Step 4; Otherwise, process it and set its STATUS as VISITED (processed state)   
– Step 5: Push on the stack all the neighbours of N with STATUS UNVISITED   
– Step 6: EXIT

---

## Lecture: L10-Graph\page_017\L10-Graph_page_017\auto

# Depth First Search (Stack-Based)

![](images/c9a976d7f9469bcd7820ceb83461bf9fba66b510847141eddd4151f0ce150ab9.jpg)

の Rule 1: Push every unvisited neighbour (if there is one) of the current vertex on the stack

<table><tr><td colspan="2"></td></tr><tr><td>Event</td><td>Stack</td></tr><tr><td>Visit &amp; Pop A</td><td>A</td></tr><tr><td>Push A&#x27;s unvisited neighbours</td><td>EDCB</td></tr><tr><td>Visit &amp; Pop B</td><td>EDC</td></tr><tr><td>Push B&#x27;s unvisited neighbours</td><td>EDCF</td></tr><tr><td>Visit &amp; Pop F</td><td>EDC</td></tr><tr><td>Push F&#x27;s unvisited neighbours</td><td>EDCH</td></tr><tr><td>Visit &amp; Pop H</td><td>EDC</td></tr><tr><td>Push H&#x27;s unvisited neighbours</td><td>EDC</td></tr><tr><td>Visit &amp; Pop C</td><td></td></tr><tr><td>Push C&#x27;s unvisited neighbours</td><td>ED</td></tr><tr><td></td><td>ED</td></tr><tr><td>Visit &amp; Pop D</td><td>E</td></tr><tr><td>Push D&#x27;s unvisited neighbours</td><td>EG</td></tr><tr><td>Visit &amp; Pop G</td><td>E</td></tr><tr><td>Push G&#x27;s unvisited neighbours</td><td>EI</td></tr><tr><td>Visit &amp; Pop I</td><td>E</td></tr><tr><td>Push &#x27;s unvisited neighbours</td><td>E</td></tr><tr><td>Visit &amp; Pop E</td><td></td></tr><tr><td></td><td></td></tr><tr><td>Done</td><td></td></tr></table>

Rule 2: If you can’t carry out Rule 1 because there are no more unvisited vertices, pop vertices from the stack (if possible) until a vertex is unvisited, mark it visited, and make it the current vertex

• Rule 3: If you can’t carry out Rule 1&2 because the stack is empty, you’re done

Time complexity ????(???? + ????), with an adjacency list

### Images:
- data\Design and Analysis of Algorithms\L10-Graph\page_017\L10-Graph_page_017\auto\images\c9a976d7f9469bcd7820ceb83461bf9fba66b510847141eddd4151f0ce150ab9.jpg
- data\Design and Analysis of Algorithms\L10-Graph\page_017\L10-Graph_page_017\auto\images\d9d0daa5b3861374df3022f5cbb9ebc0fbef3a6f3b009a31e4a0270c8956a532.jpg

---

## Lecture: L10-Graph\page_018\L10-Graph_page_018\auto

# Depth First Search (Recursion-Based)

DFS-recursive(????, ????):

mark ???? as visited   
for all neighbours ???? of ???? in Graph ????: if ???? is not visited: DFS-recursive(G, w)

Assume that we follow neighbours with smaller ID first

![](images/bb754ddfc5cc260c3110d2eb6611a041ed2fe7504f69a2bcc4a52d96efc3420c.jpg)

DFS-recursive $\left[ G , 1 \right] = \left[ 1 , 2 , 4 , 5 , 6 , 3 , 7 , 8 \right]$

Time complexity $O ( n + m )$ , when implemented using an adjacency list.

### Images:
- data\Design and Analysis of Algorithms\L10-Graph\page_018\L10-Graph_page_018\auto\images\bb754ddfc5cc260c3110d2eb6611a041ed2fe7504f69a2bcc4a52d96efc3420c.jpg

---

## Lecture: L10-Graph\page_019\L10-Graph_page_019\auto

# Try to implement the two DFS traversal algorithms (lab)

![](images/fb09c6f0ac00b211d854bf913bed0baeec9cbc6a28eb1b49840c4de9da6adcbf.jpg)

### Images:
- data\Design and Analysis of Algorithms\L10-Graph\page_019\L10-Graph_page_019\auto\images\fb09c6f0ac00b211d854bf913bed0baeec9cbc6a28eb1b49840c4de9da6adcbf.jpg

---

## Lecture: L10-Graph\page_020\L10-Graph_page_020\auto

# Breadth First Search

• BFS: starts traversing the graph from root node and explores all the neighbours. Then, it selects the nearest node and explore all the unexplored nodes. It follows the same process for each of the nearest node until it finds the goal.

– Step 1: SET STATUS $= 1$ (ready state) for each node in G   
– Step 2: Enqueue the starting node A and set its STATUS $= 2$ (waiting state) – Step 3: Repeat Steps 4 and 5 until QUEUE is empty   
– Step 4: Dequeue a node N. Process it and set its STATUS $= 3$ (processed state). – Step 5: Enqueue all neighbours of N in the ready state $( { \mathsf { S T A T U S } } = 1 )$ and set their STATUS $= 2$   
– Step 6: EXIT

---

## Lecture: L10-Graph\page_021\L10-Graph_page_021\auto

# Breadth First Search

<table><tr><td rowspan="14">6 F</td><td colspan="3"></td></tr><tr><td>Event</td><td></td><td>Queue (Front to Rear)</td></tr><tr><td>Visit B</td><td>Visit A</td><td></td></tr><tr><td></td><td>Visit C</td><td>B</td></tr><tr><td></td><td></td><td>BC</td></tr><tr><td>8 H Visit E</td><td>Visit D</td><td>BCD</td></tr><tr><td>Remove B</td><td></td><td>BCDE</td></tr><tr><td>Visit F</td><td></td><td>CDE</td></tr><tr><td></td><td></td><td>CDEF</td></tr><tr><td></td><td>Remove C</td><td>DEF</td></tr><tr><td></td><td>Remove D</td><td>EF</td></tr><tr><td>9 G</td><td>Visit G</td><td>EFG</td></tr><tr><td></td><td>Remove E</td><td>FG</td></tr><tr><td>5</td><td>Remove F</td><td>G</td></tr><tr><td>E</td><td>Visit H</td><td>GH</td></tr><tr><td></td><td>Remove G</td><td>H</td></tr><tr><td></td><td>Visit I</td><td>HI</td></tr><tr><td></td><td>Remove H</td><td>1</td></tr><tr><td></td><td>Remove I</td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td>Done</td><td></td></tr></table>

• Rule 1: Visit the next unvisited vertex (if there is one) that’s adjacent to the current vertex, and insert it into the queue

の Rule 2: If you can’t carry out Rule 1 because there are no more unvisited vertices, remove a vertex from the queue (if possible) and make it the current vertex

● Rule 3: If you can’t carry out Rule 1&2 because the queue is empty, you’re done

Time complexity $O ( m + n )$ , when implemented using an adjacency list

### Images:
- data\Design and Analysis of Algorithms\L10-Graph\page_021\L10-Graph_page_021\auto\images\0439bf4ad77044b426f85056ebdaa32fb79b7f117477a4993cb2855b1954f454.jpg

---

## Lecture: L10-Graph\page_022\L10-Graph_page_022\auto

# Graph Connectivity

---

## Lecture: L10-Graph\page_023\L10-Graph_page_023\auto

# Connected Component

• Connected component: find all nodes reachable from ????

![](images/b0d233471d484ccbaae90bb9bc3b4dcf02ef73a6b254ed67f68360d66859a3c7.jpg)

Connected component containing node 1 is [1, 2, 3, 4, 5, 6, 7, 8 ]

### Images:
- data\Design and Analysis of Algorithms\L10-Graph\page_023\L10-Graph_page_023\auto\images\b0d233471d484ccbaae90bb9bc3b4dcf02ef73a6b254ed67f68360d66859a3c7.jpg

---

## Lecture: L10-Graph\page_024\L10-Graph_page_024\auto

# Connected Component

• Connected component: find all nodes reachable from ????

R will consist of nodes to which $s$ has a path   
Initially $R = \{ s \}$   
While there is an edge $( u , v )$ where $u \in R$ and $\upsilon \notin R$ Add v to R   
Endwhile   
Theorem. Upon termination, $R$ is the connected component containing ????   
・BFS $=$ explore in order of distance from ????   
・DFS $=$ explore in a different way

![](images/a2eda04b5e1f833bfc9e2d1d5cf6d2f8a0608b2444939338ec4d2dd220bad40f.jpg)  
it’s safe to add ????

### Images:
- data\Design and Analysis of Algorithms\L10-Graph\page_024\L10-Graph_page_024\auto\images\a2eda04b5e1f833bfc9e2d1d5cf6d2f8a0608b2444939338ec4d2dd220bad40f.jpg

---

## Lecture: L10-Graph\page_025\L10-Graph_page_025\auto

# Connectivity in Directed Graphs

---

## Lecture: L10-Graph\page_026\L10-Graph_page_026\auto

# Directed Graph

Notation: $G = ( V , E )$

・Edge $( u , v )$ leaves node ???? and enters node ????

![](images/0da560375df45664aeafbc281da07ef9302e985924df43593fa56ac8dfa18b36.jpg)

x. Web graph: hyperlink points from one web page to another

・Orientation of edges is crucial

・Modern web search engines exploit hyperlink structure to rank web pages by importance

### Images:
- data\Design and Analysis of Algorithms\L10-Graph\page_026\L10-Graph_page_026\auto\images\0da560375df45664aeafbc281da07ef9302e985924df43593fa56ac8dfa18b36.jpg

---

## Lecture: L10-Graph\page_027\L10-Graph_page_027\auto

# Application: Ecological Food Web

# Food web graph

Node $=$ species

・Edge $=$ from prey to predator

![](images/de9933d97015561d521d5a6868df42106abc24ae0b94266114b4004a3aaca1d6.jpg)

### Images:
- data\Design and Analysis of Algorithms\L10-Graph\page_027\L10-Graph_page_027\auto\images\de9933d97015561d521d5a6868df42106abc24ae0b94266114b4004a3aaca1d6.jpg

---

## Lecture: L10-Graph\page_028\L10-Graph_page_028\auto

# More Applications

<table><tr><td rowspan=1 colspan=1>directed graph</td><td rowspan=1 colspan=1>node</td><td rowspan=1 colspan=1>directed edge</td></tr><tr><td rowspan=1 colspan=1>transportation</td><td rowspan=1 colspan=1>street intersection</td><td rowspan=1 colspan=1>one-way street</td></tr><tr><td rowspan=1 colspan=1>web</td><td rowspan=1 colspan=1>web page</td><td rowspan=1 colspan=1>hyperlink</td></tr><tr><td rowspan=1 colspan=1>food web</td><td rowspan=1 colspan=1>species</td><td rowspan=1 colspan=1>predator-prey relationship</td></tr><tr><td rowspan=1 colspan=1>WordNet</td><td rowspan=1 colspan=1>synset</td><td rowspan=1 colspan=1>hypernym</td></tr><tr><td rowspan=1 colspan=1>scheduling</td><td rowspan=1 colspan=1>task</td><td rowspan=1 colspan=1>precedence constraint</td></tr><tr><td rowspan=1 colspan=1>financial</td><td rowspan=1 colspan=1>bank</td><td rowspan=1 colspan=1>transaction</td></tr><tr><td rowspan=1 colspan=1>cell phone</td><td rowspan=1 colspan=1>person</td><td rowspan=1 colspan=1>placed call</td></tr><tr><td rowspan=1 colspan=1>infectious disease</td><td rowspan=1 colspan=1>person</td><td rowspan=1 colspan=1>infection</td></tr><tr><td rowspan=1 colspan=1>game</td><td rowspan=1 colspan=1>board position</td><td rowspan=1 colspan=1>legal move</td></tr><tr><td rowspan=1 colspan=1>citation</td><td rowspan=1 colspan=1>journal article</td><td rowspan=1 colspan=1>citation</td></tr><tr><td rowspan=1 colspan=1>object graph</td><td rowspan=1 colspan=1>object</td><td rowspan=1 colspan=1>pointer</td></tr><tr><td rowspan=1 colspan=1> inheritance hierarchy</td><td rowspan=1 colspan=1>class</td><td rowspan=1 colspan=1>inherits from</td></tr><tr><td rowspan=1 colspan=1>control flow</td><td rowspan=1 colspan=1>code block</td><td rowspan=1 colspan=1>jump</td></tr></table>

### Images:
- data\Design and Analysis of Algorithms\L10-Graph\page_028\L10-Graph_page_028\auto\images\37ddf010d792981980861f66163b7643d854640fa7be91d1f1800d0f6de3169e.jpg

---

## Lecture: L10-Graph\page_029\L10-Graph_page_029\auto

# Undirected V.S. Directed

In an undirected graph, edges are not associated with the directions with them

• If an edge exists between vertex A and B then the vertices can be traversed from B to A as well as A to B

• In a directed graph, edges form an ordered pair

Edges represent a specific path from some vertex A to another vertex B   
Node A is called initial node while node B is called terminal node

![](images/752d7e5f8fc1de79a4835bad5b4633007e66b9818e9bb6baf709c42e3e40fbeb.jpg)

### Images:
- data\Design and Analysis of Algorithms\L10-Graph\page_029\L10-Graph_page_029\auto\images\752d7e5f8fc1de79a4835bad5b4633007e66b9818e9bb6baf709c42e3e40fbeb.jpg

---

## Lecture: L10-Graph\page_030\L10-Graph_page_030\auto

# Sequential Representation

• Directed: an entry $A _ { i j }$ in the adjacency matrix will be 1 if there exists an edge directly from $v _ { i }$ to ????????

![](images/b027217e7f805f13eead53243a4e211751845585a200a473cf2fd2d123cfa915.jpg)  
Directed Graph

![](images/048a8cc9063dac33c73babbcaa6c9d29e2c20b6929afad23bfdaaa4a43bcb9a8.jpg)  
Adjacency Matrix

### Images:
- data\Design and Analysis of Algorithms\L10-Graph\page_030\L10-Graph_page_030\auto\images\048a8cc9063dac33c73babbcaa6c9d29e2c20b6929afad23bfdaaa4a43bcb9a8.jpg
- data\Design and Analysis of Algorithms\L10-Graph\page_030\L10-Graph_page_030\auto\images\b027217e7f805f13eead53243a4e211751845585a200a473cf2fd2d123cfa915.jpg

---

## Lecture: L10-Graph\page_031\L10-Graph_page_031\auto

# Linked Representation

# • Directed: The sum of the lengths of adjacency lists is equal to the number of edges

![](images/de9ece1f96da23b77dc1ae4d567624efd2e34eba171f9cab478d15b211bcaf3f.jpg)  
Directed Graph

![](images/ebbb78ead768e81b1828bc9a6f039afcc5108913d45cb90d35cc24e22321ffd7.jpg)

Adjacency List

### Images:
- data\Design and Analysis of Algorithms\L10-Graph\page_031\L10-Graph_page_031\auto\images\de9ece1f96da23b77dc1ae4d567624efd2e34eba171f9cab478d15b211bcaf3f.jpg
- data\Design and Analysis of Algorithms\L10-Graph\page_031\L10-Graph_page_031\auto\images\ebbb78ead768e81b1828bc9a6f039afcc5108913d45cb90d35cc24e22321ffd7.jpg

---

## Lecture: L10-Graph\page_032\L10-Graph_page_032\auto

# Graph Search

• Directed reachability: Given a node ????, find all nodes reachable from ????

• Directed ???? ↝ ???? shortest path problem: Given two nodes ???? and $t$ , what is the length of a shortest path from ???? to ?????

coming soon!

• Graph Traversal: BFS and DFS extend naturally to directed graphs

---

## Lecture: L10-Graph\page_033\L10-Graph_page_033\auto

# Strong Connectivity

• Def. Nodes ???? and ???? are mutually reachable if there is both a path from ???? to ???? and also a path from ???? to ????

• Def. A graph is strongly connected if every pair of nodes is mutually reachable

• Lemma. Let $s$ be any node. $G$ is strongly connected iff every node is reachable

fromPf. $\Rightarrow$ , and ???? is reachable from Follows from definition

Pf. $\Leftarrow$ Path from $u$ to $\nu$ : concatenate $u { \sim } s$ path with $s \sim \nu$ path

Path from $\nu$ to $u$ : concatenate $\nu \sim s$ path with $s \sim u$ path

ok if paths overlap

![](images/3b4ce5b712fcb431a366f91763456c612ebd30faef5e72ec457741fb1d3fad4e.jpg)

### Images:
- data\Design and Analysis of Algorithms\L10-Graph\page_033\L10-Graph_page_033\auto\images\3b4ce5b712fcb431a366f91763456c612ebd30faef5e72ec457741fb1d3fad4e.jpg

---

## Lecture: L10-Graph\page_034\L10-Graph_page_034\auto

# Strong Connectivity: Algorithm

• Theorem. Can determine if ???? is strongly connected in $O ( m + n )$ time

Pf. – Pick any node ???? reverse orientation of every edge in G – Run BFS from ???? in ???? – Run BFS from ???? in $G$ reverse – Return true iff all nodes reached in both BFS executions – Correctness follows immediately from previous lemma

---

## Lecture: L10-Graph\page_035\L10-Graph_page_035\auto

# Strong Components

• Def. A strong component is a maximal subset of mutually reachable

nodes

![](images/01a8296b9d7e020ed7d0f982c4df9b7d5af927edc9353065416a84705c956d88.jpg)

# Theorem. [Tarjan 1972] Can find all strong components in $O ( m + n )$ time

SIAM J. CoMPUT. Vol. 1, No. 2, June 1972

DEPTH-FIRST SEARCH AND LINEAR GRAPH ALGORITHMS\*

ROBERT TARJANt

Abstract. The value of depth-frst search or "backtracking'" as a technique for solving problems is illustrated by two examples. An improved version of an algorithm for finding the strongly connected components of a directed graph and an algorithm for finding the biconnected components of an undirect graph are presented. The space and time requirements of both algorithms are bounded by $k _ { 1 } V + k _ { 2 } E + k _ { 3 }$ for some constants $k _ { 1 } , k _ { 2 }$ , and $k _ { 3 }$ , where $V$ is the number of vertices and $\boldsymbol { E }$ is the number of edges of the graph being examined.

### Images:
- data\Design and Analysis of Algorithms\L10-Graph\page_035\L10-Graph_page_035\auto\images\01a8296b9d7e020ed7d0f982c4df9b7d5af927edc9353065416a84705c956d88.jpg

---

## Lecture: L10-Graph\page_036\L10-Graph_page_036\auto

# Tarjan’s Algorithm: Overview

# 1. Initialization:

1. Assign a unique index to each node, initialize as undefined

2. Assign a lowlink value to each node, initialize as undefined

3. Create an empty stack to keep track of nodes in the current search path

4. Create an empty list to store the strongly connected components (SCCs)

# 2. Depth-First Search (DFS) Loop:

1. For each node $v$ in the graph:

1. If $v$ has not been visited:

1. Call the strongConnect function on $v$

# 3. strongConnect Function:

1. Set the index of $v$ to the current global index

2. Set the lowlink of $v$ to the current global index

3. Push $v$ onto the stack

4. Mark ???? as being on the stack

5. Increment the global index

# 4. Explore Adjacent Nodes:

1. For each adjacent node $u$ of ????:

1. If $u$ has not been visited:

1. Recursively call strongConnect(????)

2. Update the lowlink of $v$ to the minimum of ????.lowlink and $u$ .lowlink

2. If $u$ is on the stack:

1. Update the lowlink of $v$ to the minimum of ????.lowlink and $u$ .index

# 5. Identify SCC:

1. If the lowlink of $v$ is equal to its index:

1. Pop nodes from the stack until $v$ is popped   
2. Each popped node is part of a new SCC   
3. Add the popped nodes to the list of SCCs

# 6. Output:

1. After all nodes have been processed, the list of SCCs contains all the strongly connected components of the graph

---

## Lecture: L10-Graph\page_037\L10-Graph_page_037\auto

# Tarjan's Algorithm: Pseudocode

// GLOBAL VARIABLES

num $< -$ global array of size V initialized to -1 lowest $< -$ global array of size V initialized to -1 /1 visited $< -$ global array of size V initialized to false /1 processed $< -$ global array of size V initialized to false 11 s <- global empty stack 11 (i) $\div \mathrm { ~ < - ~ } \nobreakspace \Theta$ (id

algorithm TarjanAlgorithm(G):

// INPUT   
11 (id ${ \textsf { G } } =$ the graph   
// OUTPUT   
11 SCCs of G are found   
visted $< -$ an empty global visited map   
for v in G.V: if visited[v] $\underline { { \underline { { \mathbf { \delta \pi } } } } }$ false: // global variables are accessible from within DFs DFS(G,V)

algorithm DFS(G, V):

11 INPUT   
11 ${ \textsf { G } } =$ the graph   
11 (id:) $\begin{array} { r l } { \mathsf { v } } & { { } = } \end{array}$ the current vertex   
//OUTPUT   
11 Vertices reachable from v are processed, their sccs are reported

num[v]<-i   
lowest[v] $< -$ num[v]   
$\dot { \textbf { \ i } } < - \dot { \textbf { \ i } } + \textbf { \ i }$ (id:)   
visited[v] $< -$ true   
s.push(v)   
for u in G.neighbours[v]: if visited[u] $=$ false: DFS(G，u) lowest[v] $< -$ min(lowest[v]，lowest[u]) else if processed[u] $=$ false: lowest[v] $< -$ min(lowest[v]，num[u])   
processed[v] $< -$ true   
if lowest[v] $=$ num[v]: scc $< -$ an empty set sccVertex $< -$ s.pop() while sccVertex $\downarrow = ~ \lor$ : scc.add(sccVertex) sccVertex $< -$ s.pop() scc.add(sccVertex) Process the found scc in the desired way

### Images:
- data\Design and Analysis of Algorithms\L10-Graph\page_037\L10-Graph_page_037\auto\images\0768dfceb243ee9d8439ea4bce5aa297d41fb7bcb9d5fde700f6c3cb614dd5a3.jpg

---

## Lecture: L10-Graph\page_038\L10-Graph_page_038\auto

# Tarjan's Algorithm: An Example

![](images/e4bafc808e3c2bed335603c5caec69d460d1ddd3d14abb353df8d280f79c9882.jpg)

C ←— stack   
B   
A

### Images:
- data\Design and Analysis of Algorithms\L10-Graph\page_038\L10-Graph_page_038\auto\images\e4bafc808e3c2bed335603c5caec69d460d1ddd3d14abb353df8d280f79c9882.jpg

---

## Lecture: L10-Graph\page_039\L10-Graph_page_039\auto

# Tarjan's Algorithm: An Example

![](images/78eab31e364fb64cb942426d16f8df6c7f884ddc2a56f5194faf07b51ad88bb9.jpg)

### Images:
- data\Design and Analysis of Algorithms\L10-Graph\page_039\L10-Graph_page_039\auto\images\78eab31e364fb64cb942426d16f8df6c7f884ddc2a56f5194faf07b51ad88bb9.jpg

---

## Lecture: L10-Graph\page_040\L10-Graph_page_040\auto

# Tarjan's Algorithm: An Example

![](images/e2b89e8ae9f3db5013cc85afd9cf2f04e6dce5fc755b87ba60a1499f49508ea0.jpg)

### Images:
- data\Design and Analysis of Algorithms\L10-Graph\page_040\L10-Graph_page_040\auto\images\e2b89e8ae9f3db5013cc85afd9cf2f04e6dce5fc755b87ba60a1499f49508ea0.jpg

---

## Lecture: L10-Graph\page_041\L10-Graph_page_041\auto

# Tarjan's Algorithm: An Example

![](images/aa84e4d8feb67609f39a7e577a2be71a21650930b7acfbe641b43f4520697fd8.jpg)

### Images:
- data\Design and Analysis of Algorithms\L10-Graph\page_041\L10-Graph_page_041\auto\images\aa84e4d8feb67609f39a7e577a2be71a21650930b7acfbe641b43f4520697fd8.jpg

---

## Lecture: L10-Graph\page_042\L10-Graph_page_042\auto

# Tarjan's Algorithm: An Example

![](images/b41d527b0d92cd90633ab59ca87443b2cd482103dbc75744ca4fe302ef79decb.jpg)

### Images:
- data\Design and Analysis of Algorithms\L10-Graph\page_042\L10-Graph_page_042\auto\images\b41d527b0d92cd90633ab59ca87443b2cd482103dbc75744ca4fe302ef79decb.jpg

---

## Lecture: L10-Graph\page_043\L10-Graph_page_043\auto

# Tarjan's Algorithm: An Example

![](images/deb6d1ef238c8c37cfd0886c56cb910936c10501b523f0118a4c678fec7e6f7f.jpg)

### Images:
- data\Design and Analysis of Algorithms\L10-Graph\page_043\L10-Graph_page_043\auto\images\deb6d1ef238c8c37cfd0886c56cb910936c10501b523f0118a4c678fec7e6f7f.jpg

---

## Lecture: L10-Graph\page_044\L10-Graph_page_044\auto

# Tarjan's Algorithm: An Example

![](images/d6925e1c6f503f8454c9450e32e92afa984daa204fedc37ad5e6a1d2519ea9b4.jpg)

### Images:
- data\Design and Analysis of Algorithms\L10-Graph\page_044\L10-Graph_page_044\auto\images\d6925e1c6f503f8454c9450e32e92afa984daa204fedc37ad5e6a1d2519ea9b4.jpg

---

## Lecture: L10-Graph\page_045\L10-Graph_page_045\auto

# Tarjan's Algorithm: An Example

![](images/81aa6c792ebcbd55066886bd8651d5b31c2c901933b24ff317ffcbd614c9a265.jpg)

### Images:
- data\Design and Analysis of Algorithms\L10-Graph\page_045\L10-Graph_page_045\auto\images\81aa6c792ebcbd55066886bd8651d5b31c2c901933b24ff317ffcbd614c9a265.jpg

---

## Lecture: L10-Graph\page_046\L10-Graph_page_046\auto

# Tarjan’s Algorithm

• Tarjan’s algorithm is a modification of the DFS traversal. Hence, the complexity of the algorithm is linear: $O ( n + m )$

– To achieve the mentioned complexity, we must use the adjacency list representation of the graph

• Tarjan’s algorithm for finding strongly connected components in directed graphs. It’s an optimal linear time algorithm

• More Tarjan’s algorithms, have a try if you are interested!

---

## Lecture: L10-Graph\page_047\L10-Graph_page_047\auto

# DAG & Topological Ordering

---

## Lecture: L10-Graph\page_048\L10-Graph_page_048\auto

# Directed Acyclic Graphs

• Def. A DAG is a directed graph that contains no directed cycles

• Def. A topological order of a directed graph $G = ( V , E )$ is an ordering of its nodes as $v _ { 1 } , v _ { 2 } , \ldots , v _ { n }$ so that for every edge $( v _ { i } , v _ { j } )$ we have $i < j$

![](images/b2428378395564e98af57c0db3d7f5ac964bcbdae56b31d88be76413c184c956.jpg)

![](images/3f101337ab2af404ca5fbab7b990ddbff74354c5cf818c28c1229abc7bc0505b.jpg)  
a topological ordering

### Images:
- data\Design and Analysis of Algorithms\L10-Graph\page_048\L10-Graph_page_048\auto\images\3f101337ab2af404ca5fbab7b990ddbff74354c5cf818c28c1229abc7bc0505b.jpg
- data\Design and Analysis of Algorithms\L10-Graph\page_048\L10-Graph_page_048\auto\images\b2428378395564e98af57c0db3d7f5ac964bcbdae56b31d88be76413c184c956.jpg

---

## Lecture: L10-Graph\page_049\L10-Graph_page_049\auto

# Precedence Constraints

• Precedence constraints. Edge $( v _ { i } , v _ { j } )$ means task $v _ { i }$ must occur before ????????

• Applications – Course prerequisite graph: course $v _ { i }$ must be taken before $v _ { j }$ – Compilation: module $v _ { i }$ must be compiled before $v _ { j }$ – Pipeline of computing jobs: output of job $v _ { i }$ needed to determine input of job

????????

![](images/d01de36c8dffcacd77df81b729aeb088aa6ccd2c905722684d8150f081de9f80.jpg)

### Images:
- data\Design and Analysis of Algorithms\L10-Graph\page_049\L10-Graph_page_049\auto\images\d01de36c8dffcacd77df81b729aeb088aa6ccd2c905722684d8150f081de9f80.jpg

---

## Lecture: L10-Graph\page_050\L10-Graph_page_050\auto

# irected Acyclic Graphs

Lemma. If ???? has a topological order, then $G$ is a DAG

Pf. [by contradiction]

• Suppose that $G$ has a topological order $v _ { 1 } , v _ { 2 } , \ldots , v _ { n }$ and that $G$ also has a directed cycle $C$

• Let $v _ { i }$ be the lowest-indexed node in $C$ , and let $v _ { j }$ be the node just before $v _ { i } ;$ thus $( v _ { j } , v _ { i } )$ is an edge

• By our choice of $i$ , we have $i < j$

• On the other hand, since $( v _ { j } , v _ { i } )$ is an edge and $v _ { 1 } , v _ { 2 } , \ldots , v _ { n }$ is a topological order, we must have $j < i$ , a contradiction

the directed cycle C

![](images/6c410bcd4581e9545bdc56bef8ad563074370620510ca708f52fe290d2dde4fe.jpg)

### Images:
- data\Design and Analysis of Algorithms\L10-Graph\page_050\L10-Graph_page_050\auto\images\6c410bcd4581e9545bdc56bef8ad563074370620510ca708f52fe290d2dde4fe.jpg

---

## Lecture: L10-Graph\page_051\L10-Graph_page_051\auto

# Directed Acyclic Graphs

Lemma. If ???? has a topological order, then ???? is a DAG

Q. Does every DAG have a topological ordering?

Q. If so, how do we compute one?

---

## Lecture: L10-Graph\page_052\L10-Graph_page_052\auto

# Directed Acyclic Graphs

Lemma. If $G$ is a DAG, then $G$ has a node with no entering edges

# Pf. [by contradiction]

• Suppose that $G$ is a DAG and every node has at least one entering edge   
• Pick any node $v$ , and begin following edges backward from ????. Since ???? has at least one entering edge $( u , v )$ we can walk backward to $u$ Then, since $u$ has at least one entering edge $( x , u )$ , we can walk backward to ???? Repeat until we visit a node, say ????, twice Let $C$ denote the sequence of nodes encountered between successive visits to ????. $C$ is cycle

![](images/b4e6fa01bab92515d32d4890eb02720e127947daa34d1b5b6abbed45236e064c.jpg)

### Images:
- data\Design and Analysis of Algorithms\L10-Graph\page_052\L10-Graph_page_052\auto\images\b4e6fa01bab92515d32d4890eb02720e127947daa34d1b5b6abbed45236e064c.jpg

---

## Lecture: L10-Graph\page_053\L10-Graph_page_053\auto

# Directed Acyclic Graphs

Lemma. If $G$ is a DAG, then $G$ has a topological ordering

Pf. [by induction on ????]

Base case: true if $n = 1$   
Given DAG on $n > 1$ nodes, find a node $v$ with no entering edges   
$G - \{ v \}$ is a DAG, since deleting $v$ cannot create cycles   
By inductive hypothesis, $G - \{ v \}$ has a topological ordering   
Place $v$ first in topological ordering; then append nodes of $G - \{ v \}$ in topological order. This is   
valid since $v$ has no entering edges   
To compute a topological ordering of $G$   
Find a node $\boldsymbol { v }$ with no incoming edges and order it first   
Delete v from G   
Recursively compute a topological ordering of $G - \{ v \}$ and append this order after v

![](images/61849d62956bdc0af71b56df98de55469d6b3702ff57a8ae888e37a0198d032a.jpg)

### Images:
- data\Design and Analysis of Algorithms\L10-Graph\page_053\L10-Graph_page_053\auto\images\61849d62956bdc0af71b56df98de55469d6b3702ff57a8ae888e37a0198d032a.jpg

---

## Lecture: L10-Graph\page_054\L10-Graph_page_054\auto

# Topological Sorting Algorithm

Theorem. Algorithm finds a topological order in $O ( m + n )$ time • Pf. – Maintain the following information: • count(????) $=$ remaining number of incoming edges • $S = s e t$ of remaining nodes with no incoming edges – Initialization: $O ( m + n )$ via single scan through graph – Update: to delete $v$ • remove ???? from ???? • decrease count(????) for all edges from ???? to ????; and add ???? to ???? if co • this is O(1) per edge

Topological-sort cannot handle graphs with cycles!

---

## Lecture: L10-Graph\page_055\L10-Graph_page_055\auto

# Summary

• Graphs definition

• Graphs representation

• Graph search algorithms

• Connected components in directed/undirected graphs

• Tarjan’s Algorithm

• DAGs and Topological orders

---

## Lecture: L10-MoreOnGraphTraversal\page_001\L10-MoreOnGraphTraversal_page_001\auto

# Graph Traversal

---

## Lecture: L10-MoreOnGraphTraversal\page_002\L10-MoreOnGraphTraversal_page_002\auto

# Graph Traversal

• Traversing the graph means examining all the nodes and vertices of the graph

• Two standard methods to traverse graphs

– Breadth First Search – Depth First Search

![](images/69e44aad3f3122dcbe9d3028d00d65181c35f4ea93dacd2d5e58277ff66652fb.jpg)

### Images:
- data\Design and Analysis of Algorithms\L10-MoreOnGraphTraversal\page_002\L10-MoreOnGraphTraversal_page_002\auto\images\69e44aad3f3122dcbe9d3028d00d65181c35f4ea93dacd2d5e58277ff66652fb.jpg

---

## Lecture: L10-MoreOnGraphTraversal\page_003\L10-MoreOnGraphTraversal_page_003\auto

# Depth First Search (Recursion-Based)

DFS-recursive(????, ????):

mark ???? as visited   
for all neighbours ???? of ???? in Graph ????: if ???? is not visited: DFS-recursive(G, w)

Assume that we follow neighbours with smaller ID first

![](images/c16b1dcca39a2adabebb528acf29dc2c0b7bb1e82923b9ce6303bc5456e396b8.jpg)

DFS-recursive $( G , 1 ) = [ 1 , 2 , 4 , 5 , 6 , 3 , 7 , 8 ]$ Is this correct?

Time complexity $O ( n + m )$ , when implemented using an adjacency list.

### Images:
- data\Design and Analysis of Algorithms\L10-MoreOnGraphTraversal\page_003\L10-MoreOnGraphTraversal_page_003\auto\images\c16b1dcca39a2adabebb528acf29dc2c0b7bb1e82923b9ce6303bc5456e396b8.jpg

---

## Lecture: L10-MoreOnGraphTraversal\page_004\L10-MoreOnGraphTraversal_page_004\auto

# Depth First Search (Stack-Based)

• Use a stack $\cdot$ to manage the vertices we visited

• At the beginning, color all vertices in the graph white and create an empty DFS tree $\cdot$ .

• Initially, $S$ contains an arbitrary node ???? as the start node, and color it gray (which means “in the stack”). Make ???? the root of T.

• Repeat the following until ???? is empty:

– Let ???? be the vertex at the top of the Stack ????

– Does ???? still have white out-neighbor?

• If so: let it be $\cdot$ ; Push $u$ into ????, color it gray, and set ???? as a child of v in T • Otherwise, pop $v$ from $S$ and color it black (meaning $v$ is done).

• If there are still white vertices, repeat the above by restarting from an arbitrary white vertex $v ^ { \prime }$ , creating a new DFS-tree rooted at $v ^ { \prime }$ .

---

## Lecture: L10-MoreOnGraphTraversal\page_005\L10-MoreOnGraphTraversal_page_005\auto

# Depth First Search (Stack-Based)

DFS tree a

![](images/a7c1cea12cf483b24efa2f736850ae71c8ce591e5e0c3e5038f01c67985c6f5e.jpg)

![](images/f36c6f6e18a50296d72cafe827ba1674917f9689f9ab790d03ce75a4f9b1b17d.jpg)

We will create a DFS-forest, which consists of 2 DFS-trees in this example:

Time complexity $O ( m + n )$ , with an adjacency list For every vertex $\boldsymbol { \mathsf { V } }$ , remember which is the next out-neighbor to explore. Use an array to remember the colors of all vertices $O ( m + n )$ stack operations

### Images:
- data\Design and Analysis of Algorithms\L10-MoreOnGraphTraversal\page_005\L10-MoreOnGraphTraversal_page_005\auto\images\a7c1cea12cf483b24efa2f736850ae71c8ce591e5e0c3e5038f01c67985c6f5e.jpg
- data\Design and Analysis of Algorithms\L10-MoreOnGraphTraversal\page_005\L10-MoreOnGraphTraversal_page_005\auto\images\f36c6f6e18a50296d72cafe827ba1674917f9689f9ab790d03ce75a4f9b1b17d.jpg

---

## Lecture: L10-MoreOnGraphTraversal\page_006\L10-MoreOnGraphTraversal_page_006\auto

# Depth First Search (Stack-Based)

# The Ancestor-Descendant Property:

• u is an ancestor of v in the DFS-forest if and only if the following holds: u is already in the stack when v enters the stack.

Each edge (u, v) of G can be classified into:

• Forward edge: if u is a proper ancestor of v in a DFS-tree Back edge: if u is a descendant of v in a DFS-tree • Cross edge: if neither the above applies

![](images/8f7d8fe75817b24066b2679ee6b0f5a48551370c270f206199f1716062b2cf1f.jpg)

### Images:
- data\Design and Analysis of Algorithms\L10-MoreOnGraphTraversal\page_006\L10-MoreOnGraphTraversal_page_006\auto\images\8f7d8fe75817b24066b2679ee6b0f5a48551370c270f206199f1716062b2cf1f.jpg

---

## Lecture: L10-MoreOnGraphTraversal\page_007\L10-MoreOnGraphTraversal_page_007\auto

# Breadth First Search

• BFS: starts traversing the graph from root node and explores all the neighbours. Then, it selects the nearest node and explore all the unexplored nodes. It follows the same process for each of the nearest node until it finds the goal.

– Step 1: SET color $=$ white (STATUS = 1) for each node in G   
– Step 2: Enqueue the starting node A and set its color to gray (STATUS = 2, “in queue”)   
– Step 3: Repeat Steps 4 and 5 until QUEUE is empty   
– Step 4: Dequeue a node N. Process it and set its color to black (STATUS = 3 processed).   
– Step 5: Enqueue all white neighbors of N and color them gray (STATUS = 2) • Make all these neighbors as the child nodes of N in the BFS tree T   
– Step 6: EXIT

---

## Lecture: L10-MoreOnGraphTraversal\page_008\L10-MoreOnGraphTraversal_page_008\auto

# Breadth First Search

<table><tr><td rowspan="14">6 日 K G</td><td colspan="3"></td></tr><tr><td>Event Visit A</td><td></td><td>Queue (Front to Rear)</td></tr><tr><td></td><td>Visit B</td><td></td></tr><tr><td></td><td>Visit C</td><td>B</td></tr><tr><td></td><td></td><td>BC</td></tr><tr><td>8 H Visit E</td><td>Visit D</td><td>BCD</td></tr><tr><td>Remove B</td><td></td><td>BCDE</td></tr><tr><td>Visit F</td><td></td><td>CDE</td></tr><tr><td></td><td></td><td>CDEF</td></tr><tr><td></td><td>Remove C</td><td>DEF</td></tr><tr><td></td><td>Remove D</td><td>EF</td></tr><tr><td>9 Remove E</td><td>Visit G</td><td>EFG</td></tr><tr><td>Remove F</td><td></td><td>FG</td></tr><tr><td>5</td><td></td><td>G</td></tr><tr><td>目</td><td>Visit H</td><td>GH</td></tr><tr><td></td><td>Remove G</td><td>H</td></tr><tr><td></td><td>Visit I</td><td>HI</td></tr><tr><td></td><td>Remove H</td><td>I</td></tr><tr><td></td><td>Remove I</td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td>Done</td><td></td></tr></table>

• When a vertex v is dequeued, we spend $O ( 1 + d ^ { + } ( v ) )$ time processing it, where $d ^ { + } ( v )$ is the out-degree of v

• Time complexity $O ( m + n )$ , when implemented using an adjacency list

• The shortest path from the start vertex A to any vertex, say, x is simply the path from A to node x in the BFS tree!

### Images:
- data\Design and Analysis of Algorithms\L10-MoreOnGraphTraversal\page_008\L10-MoreOnGraphTraversal_page_008\auto\images\4a79b4a1572de144f31be23880d3dbca74eef12beb464667cb612a0a10f28c28.jpg

---

## Lecture: L10-MoreOnGraphTraversal\page_009\L10-MoreOnGraphTraversal_page_009\auto

# Breadth First Search

BFS tree

BFS tree

a

![](images/ebe28183b4ae0cba52c4b97566d98e9a0771f00f9648b448aff00329778a8342.jpg)

![](images/ef438c9082c166d36501721e9271b21f0440e7055ee04f282af26223498a4e28.jpg)

• Given two vertices u, $\mathsf { v } \in \mathsf { V }$ , a shortest path from u to v is a path of the minimum length from u to v .

• Assume that each edge has a length of 1 unit.

• The shortest path from the start vertex A to any vertex, say, x is simply the path from A to node x in the BFS tree!

### Images:
- data\Design and Analysis of Algorithms\L10-MoreOnGraphTraversal\page_009\L10-MoreOnGraphTraversal_page_009\auto\images\ebe28183b4ae0cba52c4b97566d98e9a0771f00f9648b448aff00329778a8342.jpg
- data\Design and Analysis of Algorithms\L10-MoreOnGraphTraversal\page_009\L10-MoreOnGraphTraversal_page_009\auto\images\ef438c9082c166d36501721e9271b21f0440e7055ee04f282af26223498a4e28.jpg

---

## Lecture: L11-Graph\page_001\L11-Graph_page_001\auto

# Graph Algorithms (Il)

Single Source Shortest Path

Dijkstra's algorithm - Bellman-Ford algorithm

All-pairs shortest paths - Floyd-Warshall algorithm

---

## Lecture: L11-Graph\page_002\L11-Graph_page_002\auto

# Single source shortest paths

---

## Lecture: L11-Graph\page_003\L11-Graph_page_003\auto

Consider a digraph $G = \left( V , E \right)$ with edge-weight function w : $E \to { \mathsf { R } }$ .

The weight of path $p = \nu _ { 1 } \to \nu _ { 2 } \to \dots \to \nu _ { k }$ is defined tobe

$$
w ( p ) = \sum _ { i = 1 } ^ { k - 1 } w ( \nu _ { i } , \nu _ { i + 1 } ) .
$$

# Example:

![](images/c355da68eb183a530f51e0485aad8107320351b36a44c7bebfbf589e78d3466d.jpg)

### Images:
- data\Design and Analysis of Algorithms\L11-Graph\page_003\L11-Graph_page_003\auto\images\1bcfbfd9693f272cfbb24b91bc179bfa4d91c41591ed24c40c3ea4d52332379c.jpg
- data\Design and Analysis of Algorithms\L11-Graph\page_003\L11-Graph_page_003\auto\images\c355da68eb183a530f51e0485aad8107320351b36a44c7bebfbf589e78d3466d.jpg

---

## Lecture: L11-Graph\page_004\L11-Graph_page_004\auto

A shortest path from $u$ to v is a path of minimum weight from $u$ to $V$ .

The shortest-path weight from $u$ to $V$ is defined as:

$8 ( u , \nu ) = \operatorname* { m i n } \{ w ( p ) : p$ is a path from u to $\nu \}$ .

Note: $8 ( u , \nu ) = \infty$ if no path from $u$ to v exists.

---

## Lecture: L11-Graph\page_005\L11-Graph_page_005\auto

If a graph $G$ contains a negative-weight cycle, then some shortest paths do not exist.

Example:

![](images/51e1c7b215c39a7bf7e9791a8153cb1345ecd14f93131f15ed98da2f2d421f1d.jpg)

### Images:
- data\Design and Analysis of Algorithms\L11-Graph\page_005\L11-Graph_page_005\auto\images\51e1c7b215c39a7bf7e9791a8153cb1345ecd14f93131f15ed98da2f2d421f1d.jpg

---

## Lecture: L11-Graph\page_006\L11-Graph_page_006\auto

Theorem. A subpath of a shortest path is a shortest path.

Proof. Cut and paste:

![](images/ec0d7be658e224f2510dbca7cfbaee7b6f36085464b2c5cac6cacd4252905776.jpg)

If $v _ { j }$ on optimal path from $v _ { 0 }$ $\mathfrak { t o } v _ { n } \colon \delta ( v _ { 0 } , v _ { n } ) = \delta \big ( v _ { 0 } , v _ { j } \big ) + \delta \big ( v _ { j } , v _ { n } \big ) .$

If the sub-path $v _ { i }$ to $v _ { j }$ is not optimal, then by finding a shorter path from $v _ { i }$ to $v _ { j }$ we can strictly improve the original path.

### Images:
- data\Design and Analysis of Algorithms\L11-Graph\page_006\L11-Graph_page_006\auto\images\ec0d7be658e224f2510dbca7cfbaee7b6f36085464b2c5cac6cacd4252905776.jpg

---

## Lecture: L11-Graph\page_007\L11-Graph_page_007\auto

Theorem. For all $u , \nu , x \in V ,$ we have

$$
\delta ( u , \nu ) \leq \delta ( u , x ) + \delta ( x , \nu ) .
$$

Proof.

![](images/00d38d585192dc3fad02b2c0a92ba44a949e5dffac4aadfb6bd148543c2858b2.jpg)

If u not on shortest path from s to $t \colon \delta ( s , t ) < \delta ( s , u ) + \delta ( u , t ) .$ u is on shortest path from $s$ to $t$ iff $\delta ( s , t ) = \delta ( s , u ) + \delta ( u , t ) .$

### Images:
- data\Design and Analysis of Algorithms\L11-Graph\page_007\L11-Graph_page_007\auto\images\00d38d585192dc3fad02b2c0a92ba44a949e5dffac4aadfb6bd148543c2858b2.jpg
- data\Design and Analysis of Algorithms\L11-Graph\page_007\L11-Graph_page_007\auto\images\e34cae42df10ca0ee0e4fd432e0961c917e9a82d4c7bde24b299b95bb7e7f4ba.jpg

---

## Lecture: L11-Graph\page_008\L11-Graph_page_008\auto

Problem. Assume that $w ( u , \nu ) \geq 0$ for all $( u , \nu ) \in E$ . (Hence, all shortest-path weights must exist.) From a given source vertex $S$ $\in V ,$ find the shortest-path weights $\delta ( s , \nu )$ for all $\nu \in V .$ .

# IDEA: Greedy.

1. Maintain a set $S$ of vertices whose shortest-path distances from $S$ are known.   
2. At each step, add to $S$ the vertex $\nu \in V - S$ . whose distance estimate from $\boldsymbol { S }$ is minimum.   
3. Update the distance estimates of vertices adjacent to $\nu$ .

---

## Lecture: L11-Graph\page_009\L11-Graph_page_009\auto

$d [ s ] \gets 0$ for each $\nu \in V - \{ s \}$ do $d [ \nu ]  \infty$

![](images/7c68d378807c31dc6b96e3014e17fe2d2c021ce7fbe70c5aa349f8f967e5f9fa.jpg)

### Images:
- data\Design and Analysis of Algorithms\L11-Graph\page_009\L11-Graph_page_009\auto\images\734c60845a2e27734650bb2453f8f41427dfe4722d4f97200644534eba3606e6.jpg
- data\Design and Analysis of Algorithms\L11-Graph\page_009\L11-Graph_page_009\auto\images\7c68d378807c31dc6b96e3014e17fe2d2c021ce7fbe70c5aa349f8f967e5f9fa.jpg

---

## Lecture: L11-Graph\page_010\L11-Graph_page_010\auto

![](images/747a228c07118528b0f067c469a727b786507b187e3ca7bcc1dd55ed29cf04f3.jpg)

### Images:
- data\Design and Analysis of Algorithms\L11-Graph\page_010\L11-Graph_page_010\auto\images\747a228c07118528b0f067c469a727b786507b187e3ca7bcc1dd55ed29cf04f3.jpg

---

## Lecture: L11-Graph\page_011\L11-Graph_page_011\auto

![](images/efea0f41e0c8ee8b3cb0b54f41d732877e701666d8812a7ad2c0806cdaa18f22.jpg)

### Images:
- data\Design and Analysis of Algorithms\L11-Graph\page_011\L11-Graph_page_011\auto\images\efea0f41e0c8ee8b3cb0b54f41d732877e701666d8812a7ad2c0806cdaa18f22.jpg

---

## Lecture: L11-Graph\page_012\L11-Graph_page_012\auto

# Example of Dijkstra’s algorithm

Dijkstra can only handle graphs with nonnegative edge weights:

![](images/f0d546e1b75be49603419f29efee1865b2d6054c9ac07510709fbec7a85b404a.jpg)

Try to think why?

### Images:
- data\Design and Analysis of Algorithms\L11-Graph\page_012\L11-Graph_page_012\auto\images\f0d546e1b75be49603419f29efee1865b2d6054c9ac07510709fbec7a85b404a.jpg

---

## Lecture: L11-Graph\page_013\L11-Graph_page_013\auto

![](images/be7fa6f58fb8a00998d2b1acb9e55fdcde503be37e34c1f396d174a5120b8215.jpg)

S: {}

### Images:
- data\Design and Analysis of Algorithms\L11-Graph\page_013\L11-Graph_page_013\auto\images\be7fa6f58fb8a00998d2b1acb9e55fdcde503be37e34c1f396d174a5120b8215.jpg

---

## Lecture: L11-Graph\page_014\L11-Graph_page_014\auto

![](images/2d31b9d864223c28e542c1889cfc85a9733049aeadfa20b26ec178ee35a22770.jpg)

S: { A }

### Images:
- data\Design and Analysis of Algorithms\L11-Graph\page_014\L11-Graph_page_014\auto\images\2d31b9d864223c28e542c1889cfc85a9733049aeadfa20b26ec178ee35a22770.jpg

---

## Lecture: L11-Graph\page_015\L11-Graph_page_015\auto

![](images/6bd2250b41240a1d90f2f20c4e01b96d3fadf2b4a048246742e57bd5eb1faed7.jpg)

S: { A }

### Images:
- data\Design and Analysis of Algorithms\L11-Graph\page_015\L11-Graph_page_015\auto\images\6bd2250b41240a1d90f2f20c4e01b96d3fadf2b4a048246742e57bd5eb1faed7.jpg

---

## Lecture: L11-Graph\page_016\L11-Graph_page_016\auto

![](images/cad3a05c351cca8d51901df831d8dbbd5c1a19cda19a565e4468f13565009a1f.jpg)

$$
S \colon \{ A , C \}
$$

### Images:
- data\Design and Analysis of Algorithms\L11-Graph\page_016\L11-Graph_page_016\auto\images\cad3a05c351cca8d51901df831d8dbbd5c1a19cda19a565e4468f13565009a1f.jpg
- data\Design and Analysis of Algorithms\L11-Graph\page_016\L11-Graph_page_016\auto\images\f594f6f53a727289d91fbfe3e597e07e95c77763966b7df293313e7f32c7aa05.jpg

---

## Lecture: L11-Graph\page_017\L11-Graph_page_017\auto

![](images/6859b9b35200b79929a38966a5e04daa6910a98f54b1cfb1efc5da313f4c6d3a.jpg)

### Images:
- data\Design and Analysis of Algorithms\L11-Graph\page_017\L11-Graph_page_017\auto\images\6859b9b35200b79929a38966a5e04daa6910a98f54b1cfb1efc5da313f4c6d3a.jpg

---

## Lecture: L11-Graph\page_018\L11-Graph_page_018\auto

![](images/7b2ab2134c21e5350419557fb968db402e80e9831137178001f4d9f4352c8217.jpg)

### Images:
- data\Design and Analysis of Algorithms\L11-Graph\page_018\L11-Graph_page_018\auto\images\7b2ab2134c21e5350419557fb968db402e80e9831137178001f4d9f4352c8217.jpg

---

## Lecture: L11-Graph\page_019\L11-Graph_page_019\auto

![](images/2b28e408c3b4eecbebfe1f8d33292ac91fa74befdc6b56f50f589b72e7e28d17.jpg)

### Images:
- data\Design and Analysis of Algorithms\L11-Graph\page_019\L11-Graph_page_019\auto\images\2b28e408c3b4eecbebfe1f8d33292ac91fa74befdc6b56f50f589b72e7e28d17.jpg

---

## Lecture: L11-Graph\page_020\L11-Graph_page_020\auto

![](images/3880e7fcfffb48f6140d3a5786fc346eb017330e63029831b6cd773e10d64383.jpg)

### Images:
- data\Design and Analysis of Algorithms\L11-Graph\page_020\L11-Graph_page_020\auto\images\3880e7fcfffb48f6140d3a5786fc346eb017330e63029831b6cd773e10d64383.jpg

---

## Lecture: L11-Graph\page_021\L11-Graph_page_021\auto

![](images/5a62fcb37373d85a666cbcffe281746bc487cebc076297214411942b4952ee6f.jpg)

### Images:
- data\Design and Analysis of Algorithms\L11-Graph\page_021\L11-Graph_page_021\auto\images\5a62fcb37373d85a666cbcffe281746bc487cebc076297214411942b4952ee6f.jpg

---

## Lecture: L11-Graph\page_022\L11-Graph_page_022\auto

![](images/1a82cb91cbae29b16348b828861e2e0808b65f252c6754b81ef53be945ab3b23.jpg)

### Images:
- data\Design and Analysis of Algorithms\L11-Graph\page_022\L11-Graph_page_022\auto\images\1a82cb91cbae29b16348b828861e2e0808b65f252c6754b81ef53be945ab3b23.jpg

---

## Lecture: L11-Graph\page_023\L11-Graph_page_023\auto

Lemma. Initializing $d [ s ] \gets 0$ and $d [ \nu ]  \infty$ for all $\nu \in V { - \{ s \} }$ establishes $d [ \nu ] \geq \delta ( s , \nu )$ for all $\nu \in V ,$ and this invariant is maintained over any sequence of relaxation steps.

Proof. Suppose not. Let $\nu$ be the first vertex for which $d [ \nu ]$ $< \delta ( s , \nu )$ , and let $u$ be the vertex that caused $d [ \nu ]$ to change: $d [ \nu ] = d [ u ] + w ( u , \nu )$ . Then,

$$
\begin{array} { r l } & { d [ \nu ] < \delta ( s , \nu ) } \\ & { \qquad \leq \delta ( s , u ) + \delta ( u , \nu ) } \\ & { \qquad \leq \delta ( s , u ) + w ( u , \nu ) } \\ & { \qquad \leq d [ u ] + w ( u , \nu ) } \end{array}
$$

Contradiction.

### Images:
- data\Design and Analysis of Algorithms\L11-Graph\page_023\L11-Graph_page_023\auto\images\385c0ec1cb60d9721b483eb2b6d3e7346dadfe5b5f61830fc58b54f396f7121f.jpg

---

## Lecture: L11-Graph\page_024\L11-Graph_page_024\auto

Lemma. Let $u$ be $\nu _ { S } ^ { \prime }$ predecessor on a shortest path from $\boldsymbol { S }$ to $\nu$ . Then, if $d [ u ] = \delta ( s , u )$ and edge $( u , \nu )$ is relaxed, we have $d [ \nu ] = \delta ( s , \nu )$ after the relaxation.

# Proof.

Observe that ${ \delta } ( s , \nu ) = { \delta } ( s , u ) + w ( u , \nu )$ . Suppose that $d [ \nu ] > \delta ( s , \nu )$ before the relaxation. (Otherwise, we’re done.) Then, the test $d [ \nu ] >$ $\boldsymbol { d } [ u ] + { \boldsymbol { w } } ( u , \nu )$ succeeds, because $d [ \nu ] > \delta ( s , \nu ) = \delta ( s , u ) + w ( u , \nu ) =$ $\boldsymbol { d } [ u ] + \boldsymbol { w } ( \boldsymbol { u } , \nu )$ , and the algorithm sets $d [ \nu ] = d [ u ] + w ( u , \nu ) = \delta ( s , \nu )$ .

---

## Lecture: L11-Graph\page_025\L11-Graph_page_025\auto

Theorem. Dijkstra’s algorithm terminates with $d [ \nu ] = \delta ( s , \nu )$ for all $\nu \in V .$ .

Proof. It suffices to show that $d [ \nu ] = \delta ( s , \nu )$ for every $\nu \in V$ when $\nu$ is added to $S$ . Suppose $u$ is the first vertex added to $S$ for which $d [ u ] > \delta ( s , u )$ . Let $y$ be the first vertex in $V - S$ along a shortest path from $S$ to $u$ , and let $x$ be its predecessor:

![](images/2d2117aa7d9457cc6ebc8afb3266cd608124b2339eca7228dc114891326149f5.jpg)

### Images:
- data\Design and Analysis of Algorithms\L11-Graph\page_025\L11-Graph_page_025\auto\images\2d2117aa7d9457cc6ebc8afb3266cd608124b2339eca7228dc114891326149f5.jpg

---

## Lecture: L11-Graph\page_026\L11-Graph_page_026\auto

![](images/578613a0da221879300f2ebbba63c5816d4caf96673f8615dd2e4829b1703691.jpg)

Since $u$ is the first vertex violating the claimed invariant, we have $d [ x ] = \delta ( s , x )$ .

When $x$ was added to $S _ { i }$ , the edge $( x , y )$ was relaxed, which implies that $d [ y ] = \delta ( s , y ) \leq \delta ( s , u ) < d [ u ]$ . But, $d [ u ] \leq d [ y ]$ by our choice of $u$ .

Contradiction.

### Images:
- data\Design and Analysis of Algorithms\L11-Graph\page_026\L11-Graph_page_026\auto\images\578613a0da221879300f2ebbba63c5816d4caf96673f8615dd2e4829b1703691.jpg

---

## Lecture: L11-Graph\page_027\L11-Graph_page_027\auto

![](images/f4878bc525b7e66dd7339f18a214edc0ecf043f22ae3ed44cfa6ede0132b9392.jpg)

### Images:
- data\Design and Analysis of Algorithms\L11-Graph\page_027\L11-Graph_page_027\auto\images\f4878bc525b7e66dd7339f18a214edc0ecf043f22ae3ed44cfa6ede0132b9392.jpg

---

## Lecture: L11-Graph\page_028\L11-Graph_page_028\auto

![](images/b25f3446d21f9e2a2c6e1fa60d47ab429ffc2b8ac09c369d9bbe5e4a300d9f10.jpg)

### Images:
- data\Design and Analysis of Algorithms\L11-Graph\page_028\L11-Graph_page_028\auto\images\b25f3446d21f9e2a2c6e1fa60d47ab429ffc2b8ac09c369d9bbe5e4a300d9f10.jpg

---

## Lecture: L11-Graph\page_029\L11-Graph_page_029\auto

![](images/4093e19da6de4ee06cbc73505676e1e5d9b65b64ec9fbe9ba78c8ae7fe9f1b09.jpg)

### Images:
- data\Design and Analysis of Algorithms\L11-Graph\page_029\L11-Graph_page_029\auto\images\4093e19da6de4ee06cbc73505676e1e5d9b65b64ec9fbe9ba78c8ae7fe9f1b09.jpg

---

## Lecture: L11-Graph\page_030\L11-Graph_page_030\auto

![](images/ce9d71a04821eb209312152e52f65a1f1b4f1c41b6951f6602d0c3cb26d4702c.jpg)

Handshaking Lemma ⇒ Θ(|E|) implicit DECREASE-KEY’s. $\Theta ( | V | \cdot T _ { \mathrm { E X T R A C T - M I N } } + | E | \cdot T _ { \mathrm { D E C R E A S E - K E Y } } )$

Note: Same formula as in the analysis of Prim’s minimum spanning tree algorithm.

### Images:
- data\Design and Analysis of Algorithms\L11-Graph\page_030\L11-Graph_page_030\auto\images\ce9d71a04821eb209312152e52f65a1f1b4f1c41b6951f6602d0c3cb26d4702c.jpg

---

## Lecture: L11-Graph\page_031\L11-Graph_page_031\auto

Time = Θ(|V|)·TEXTRACT-MIN + Θ(|E|)·TDECREASE-KEY

TEXTRACT-MIN TDECREASE-KEY

Total

array

O(|V|)

O(1)

---

## Lecture: L11-Graph\page_032\L11-Graph_page_032\auto

Time = Θ(|V|)·TEXTRACT-MIN + Θ(|E|)·TDECREASE-KEY

TEXTRACT-MIN TDECREASE-KEY

Total

array O(|V|) O(1) O(|V|2)

binaryheap O(lg|V|) O(lg|V|) O(|E|lg|V|)

---

## Lecture: L11-Graph\page_033\L11-Graph_page_033\auto

Time = Θ(|V|)·TEXTRACT-MIN + Θ(|E|)·TDECREASE-KEY

Q TEXTRACT-MIN TDECREASE-KEY

Total

array O(|V|) O(1) O(|V|2 )

binaryheap O(lg|V|) O(lg|V|) O(|E|lg| V|)

Fibonacci O(lg|V|) O(1) O(|E| + |V| lg |V|) heap amortized amortized worst case

---

## Lecture: L11-Graph\page_034\L11-Graph_page_034\auto

Suppose that $w ( u , \nu ) = 1$ for all $( u , \nu ) \in E$ . Can Dijkstra’s algorithm be improved?

• Use a simple FIFO queue instead of a priority queue.

---

## Lecture: L11-Graph\page_035\L11-Graph_page_035\auto

Suppose that $w ( u , \nu ) = 1$ for all $( u , \nu ) \in E$ . Can Dijkstra’s algorithm be improved?

• Use a simple FIFO queue instead of a priority queue.

# Breadth-first search

while $\boldsymbol { Q } \neq \boldsymbol { \mathcal { O } }$ do u ← DEQUEUE(Q) for each $\nu \in A d j [ u ]$ do if $d [ \nu ] = \infty$ then $d [ \nu ] \gets d [ u ] + 1$ ENQUEUE(Q, v)

Analysis: Time $= O ( | V | + | E | )$ .

---

## Lecture: L11-Graph\page_036\L11-Graph_page_036\auto

# Example of breadth-first search

![](images/4850b5f64e7017c29ea7abe4044c2fba49436bfb671fe57cbf9a5bb14e5ad26a.jpg)

Q:

### Images:
- data\Design and Analysis of Algorithms\L11-Graph\page_036\L11-Graph_page_036\auto\images\4850b5f64e7017c29ea7abe4044c2fba49436bfb671fe57cbf9a5bb14e5ad26a.jpg

---

## Lecture: L11-Graph\page_037\L11-Graph_page_037\auto

# Example of breadth-first search

![](images/cca3fabcf831215e30252cbe44640e2354d1393d074253b24cb2c76052c70520.jpg)

### Images:
- data\Design and Analysis of Algorithms\L11-Graph\page_037\L11-Graph_page_037\auto\images\cca3fabcf831215e30252cbe44640e2354d1393d074253b24cb2c76052c70520.jpg

---

## Lecture: L11-Graph\page_038\L11-Graph_page_038\auto

# Example of breadth-first search

![](images/90bb15997c1f679301882a8ddc12668c5f12551a4d1a6e39701c3cf97c5031b1.jpg)

### Images:
- data\Design and Analysis of Algorithms\L11-Graph\page_038\L11-Graph_page_038\auto\images\90bb15997c1f679301882a8ddc12668c5f12551a4d1a6e39701c3cf97c5031b1.jpg

---

## Lecture: L11-Graph\page_039\L11-Graph_page_039\auto

# Example of breadth-first search

![](images/08ea65c3bf038da7636185c5b94a0ca05201a8a4bc3a100b1eb45d8cae78e09a.jpg)

### Images:
- data\Design and Analysis of Algorithms\L11-Graph\page_039\L11-Graph_page_039\auto\images\08ea65c3bf038da7636185c5b94a0ca05201a8a4bc3a100b1eb45d8cae78e09a.jpg

---

## Lecture: L11-Graph\page_040\L11-Graph_page_040\auto

# Example of breadth-first search

![](images/53e300b979cb2974eed95e1982449ecc27454e12ec630bd8eb457b7e632c708c.jpg)

### Images:
- data\Design and Analysis of Algorithms\L11-Graph\page_040\L11-Graph_page_040\auto\images\53e300b979cb2974eed95e1982449ecc27454e12ec630bd8eb457b7e632c708c.jpg

---

## Lecture: L11-Graph\page_041\L11-Graph_page_041\auto

# Example of breadth-first search

![](images/fbe5db3a8f6b10216fec9af763839bf7ba988dcc0b2ca1e6870d2e05af4a83fa.jpg)

### Images:
- data\Design and Analysis of Algorithms\L11-Graph\page_041\L11-Graph_page_041\auto\images\fbe5db3a8f6b10216fec9af763839bf7ba988dcc0b2ca1e6870d2e05af4a83fa.jpg

---

## Lecture: L11-Graph\page_042\L11-Graph_page_042\auto

# Example of breadth-first search

![](images/ff7106af8f79e866061c3459a6e0022aded0075fd7551fd2840b239ba58f61ad.jpg)

### Images:
- data\Design and Analysis of Algorithms\L11-Graph\page_042\L11-Graph_page_042\auto\images\ff7106af8f79e866061c3459a6e0022aded0075fd7551fd2840b239ba58f61ad.jpg

---

## Lecture: L11-Graph\page_043\L11-Graph_page_043\auto

# Example of breadth-first search

![](images/31430134619841a7221fb9d6785b835e3f27660a9a4dde0df741e9a9395ae7e9.jpg)

![](images/1963ec91e0cbd8c380a582fad3b4dec9eba0de73fb82e933d17d4fd842fe7b7c.jpg)

### Images:
- data\Design and Analysis of Algorithms\L11-Graph\page_043\L11-Graph_page_043\auto\images\1963ec91e0cbd8c380a582fad3b4dec9eba0de73fb82e933d17d4fd842fe7b7c.jpg
- data\Design and Analysis of Algorithms\L11-Graph\page_043\L11-Graph_page_043\auto\images\31430134619841a7221fb9d6785b835e3f27660a9a4dde0df741e9a9395ae7e9.jpg

---

## Lecture: L11-Graph\page_044\L11-Graph_page_044\auto

# Example of breadth-first search

![](images/1ab74315e6aa3c6c4a38a607b4366bccfe1030b8c916d94ce56d8081cacaffa2.jpg)

![](images/c79a84b3dee983f682c60412770e06f8b39607aa7533cbc1702b7b3d3b05c969.jpg)

### Images:
- data\Design and Analysis of Algorithms\L11-Graph\page_044\L11-Graph_page_044\auto\images\1ab74315e6aa3c6c4a38a607b4366bccfe1030b8c916d94ce56d8081cacaffa2.jpg
- data\Design and Analysis of Algorithms\L11-Graph\page_044\L11-Graph_page_044\auto\images\c79a84b3dee983f682c60412770e06f8b39607aa7533cbc1702b7b3d3b05c969.jpg

---

## Lecture: L11-Graph\page_045\L11-Graph_page_045\auto

# Example of breadth-first search

![](images/270806b46c5ae8de0789fe3e389f94d7164d97204bd56576d465892c1d568c48.jpg)

### Images:
- data\Design and Analysis of Algorithms\L11-Graph\page_045\L11-Graph_page_045\auto\images\270806b46c5ae8de0789fe3e389f94d7164d97204bd56576d465892c1d568c48.jpg

---

## Lecture: L11-Graph\page_046\L11-Graph_page_046\auto

# Example of breadth-first search

![](images/c9f86f3688d841cafd92084e025071a8af772ddd1283b7aa1243b3685520909c.jpg)

### Images:
- data\Design and Analysis of Algorithms\L11-Graph\page_046\L11-Graph_page_046\auto\images\c9f86f3688d841cafd92084e025071a8af772ddd1283b7aa1243b3685520909c.jpg

---

## Lecture: L11-Graph\page_047\L11-Graph_page_047\auto

# Example of breadth-first search

![](images/5ee3ba649e7391d6648041d604ae377a97f1de3ce64638abc4bef5d111750b92.jpg)

### Images:
- data\Design and Analysis of Algorithms\L11-Graph\page_047\L11-Graph_page_047\auto\images\5ee3ba649e7391d6648041d604ae377a97f1de3ce64638abc4bef5d111750b92.jpg

---

## Lecture: L11-Graph\page_048\L11-Graph_page_048\auto

# while $\boldsymbol { Q } \neq \boldsymbol { \mathcal { O } }$ do u ← DEQUEUE(Q) for each $\nu \in A d j [ u ]$ do if $d [ \nu ] = \infty$ then $d [ \nu ] \gets d [ u ] + 1$ ENQUEUE(Q, v)

# Key idea:

The FIFO $\boldsymbol { \mathcal { Q } }$ in breadth-first search mimics the priority queue $\boldsymbol { \mathcal { Q } }$ in Dijkstra.

Invariant: $\nu$ comes after $u$ in $\mathcal { Q }$ implies that $d [ \nu ] = d [ u ]$ or $\begin{array} { r } { d [ \nu ] = d [ u ] + 1 . } \end{array}$

### Images:
- data\Design and Analysis of Algorithms\L11-Graph\page_048\L11-Graph_page_048\auto\images\77701635ba7780d079fefaa740983a6a169f443c7a7d8b13305ddc7763d60f5c.jpg

---

## Lecture: L11-Graph\page_049\L11-Graph_page_049\auto

# Bellman-Ford algorithm

---

## Lecture: L11-Graph\page_050\L11-Graph_page_050\auto

# Bellman-Ford algorithm

• (-) Slower than Dijkstra’s algorithm

• (+) Can handle negative edge weights.

Can be useful if you want to say that some edges are actively good to take, rather than costly.

Can be useful as a building block in other algorithms.

# Basic idea:

Instead of picking the u with the smallest d[u] to update, just update all of the u’s simultaneously.

---

## Lecture: L11-Graph\page_051\L11-Graph_page_051\auto

# Bellman-Ford(G,s):

• ${ \mathsf { d } } [ { \mathsf { v } } ] = \infty$ for all $\boldsymbol { \mathsf { V } }$ in V   
• ${ \mathsf { d } } [ { \mathsf { s } } ] = 0$   
• For $\mathsf { i } \mathop { = } 0$ ,…,|V|-1: • For u in V: • For v in u.neighbors: • d[v] ← min(d[v], d[u] +

Instead of picking u cleverly, just update for all of the u’s.

edgeWeight(u,v))

Compare to Dijkstra:

• While there are not-sure nodes:

• Pick the not-sure node u with the smallest estimate d[u].

• For v in u.neighbors: • d[v] ← min(d[v], d[u] + edgeWeight(u,v))

Mark u as sure.

---

## Lecture: L11-Graph\page_052\L11-Graph_page_052\auto

# Bellman-Ford algorithm

• We are actually going to change this to be less smart.

• Keep n arrays: d(0), d(1) , …, d(n-1)

# Bellman-Ford\*(G,s):

• $\mathsf { d } ^ { ( \mathrm { i } ) } [ \mathsf { v } ] = \infty$ for all v in V, for all i=0,…,|V|-1   
• d(0)[s] = 0 Slightly different than the original   
• For i=0,…,|V|-2: Bellman-Ford algorithm, but the • For u in V: analysis is basically the same. • For v in u.neighbors: d(i+1)[v] ← min(d(i) [v] , d(i+1)[v], d(i) [u] + edgeWeight(u,v))

• Then dist $\mathbf { \partial } \cdot ( \mathsf { s } , \mathsf { v } ) = \mathsf { d } ^ { ( \mathsf { n } - 1 ) } [ \mathsf { v } ]$

---

## Lecture: L11-Graph\page_053\L11-Graph_page_053\auto

Start with the same graph, no

# How far is a node from Gates?

![](images/3f855d5d87627081fe99197f541675b4af321466e506802eae91068a959f248b.jpg)

![](images/f2662cc0d594ca9de7872725cbf96762fe734b153df16e03356b193b251c519a.jpg)

• For $\mathsf { i } { = } 0 , { \ldots } , | \mathsf { V } | { - } 2 $ : • For u in V: • For $\boldsymbol { \mathsf { v } }$ in u.neighbors: $\mathrm { o l } ^ { \mathrm { ( i + 1 ) } } [ \vee ]  \mathrm { m i n } ( \mathrm { d } ^ { \mathrm { ( i ) } } [ \vee ] ~ , ~ \mathrm { d } ^ { \mathrm { ( i + 1 ) } } [ \vee ] , ~ \mathrm { d } ^ { \mathrm { ( i ) } } [ \mathrm { u } ] + \mathrm { e d } \underline { { \mathrm { g e } } } \mathsf { W } \mathrm { e i g h t } ( \mathrm { u } , \vee ) )$

### Images:
- data\Design and Analysis of Algorithms\L11-Graph\page_053\L11-Graph_page_053\auto\images\3f855d5d87627081fe99197f541675b4af321466e506802eae91068a959f248b.jpg
- data\Design and Analysis of Algorithms\L11-Graph\page_053\L11-Graph_page_053\auto\images\f2662cc0d594ca9de7872725cbf96762fe734b153df16e03356b193b251c519a.jpg

---

## Lecture: L11-Graph\page_054\L11-Graph_page_054\auto

# How far is a node from Gates?

![](images/b509d0bef783f266260e5ba30a2fcb7ae1bc31d0e7dcf084ac3def178fac2b6b.jpg)

Start with the same graph, no

![](images/40aaf09e6afa305e13d2ee7c01a4c8a60083b67e802397def218fd121b89afc2.jpg)

• For $\mathsf { i } { = } 0 , { \ldots } , | \mathsf { V } | { - } 2 $ : • For u in V: • For $\boldsymbol { \mathsf { v } }$ in u.neighbors: $\begin{array} { r l } { \mathbf { \Phi } [ ( \mathsf { i } + \lambda ) } &  { } ] \longleftarrow \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } + \lambda ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [  \end{array}$

### Images:
- data\Design and Analysis of Algorithms\L11-Graph\page_054\L11-Graph_page_054\auto\images\40aaf09e6afa305e13d2ee7c01a4c8a60083b67e802397def218fd121b89afc2.jpg
- data\Design and Analysis of Algorithms\L11-Graph\page_054\L11-Graph_page_054\auto\images\b509d0bef783f266260e5ba30a2fcb7ae1bc31d0e7dcf084ac3def178fac2b6b.jpg

---

## Lecture: L11-Graph\page_055\L11-Graph_page_055\auto

# How far is a node from Gates?

![](images/d8542a861ad35ef24b27dbdc709c9d3ccd0bd0cf69a9b6bfc65b2d412755baf5.jpg)

Start with the same graph, no

![](images/2074c7ec9921d930e0fd5373c477131931104d2927d85f23aed8506a02663c05.jpg)

• For $\mathsf { i } { = } 0 , { \ldots } , | \mathsf { V } | { - } 2 $ : • For u in V: • For $\boldsymbol { \mathsf { v } }$ in u.neighbors: $\begin{array} { r l } { \mathbf { \Phi } [ ( \mathsf { i } + \lambda ) } &  { } ] \longleftarrow \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } + \lambda ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [  \end{array}$

### Images:
- data\Design and Analysis of Algorithms\L11-Graph\page_055\L11-Graph_page_055\auto\images\2074c7ec9921d930e0fd5373c477131931104d2927d85f23aed8506a02663c05.jpg
- data\Design and Analysis of Algorithms\L11-Graph\page_055\L11-Graph_page_055\auto\images\d8542a861ad35ef24b27dbdc709c9d3ccd0bd0cf69a9b6bfc65b2d412755baf5.jpg

---

## Lecture: L11-Graph\page_056\L11-Graph_page_056\auto

Start with the same graph, no

# How far is a node from Gates?

![](images/0dabcb6e7b5ea1c8ef58763817a5dd05d5c451920f523edd97f9bfcc4db6eaec.jpg)

![](images/e8a920d2a4e935ccb34ef5719a6458171a2f418420ebe289305ecc64acfe60a0.jpg)

• For $\mathsf { i } { = } 0 , { \ldots } , | \mathsf { V } | { - } 2 $ : • For u in V: • For v in u.neighbors: $\mathrm { o l } ^ { \mathrm { ( i + 1 ) } } [ \vee ]  \mathrm { m i n } ( \mathrm { d } ^ { \mathrm { ( i ) } } [ \vee ] ~ , ~ \mathrm { d } ^ { \mathrm { ( i + 1 ) } } [ \vee ] , ~ \mathrm { d } ^ { \mathrm { ( i ) } } [ \mathrm { u } ] + \mathrm { e d } \underline { { \mathrm { g e } } } \mathsf { W } \mathrm { e i g h t } ( \mathrm { u } , \vee ) )$

### Images:
- data\Design and Analysis of Algorithms\L11-Graph\page_056\L11-Graph_page_056\auto\images\0dabcb6e7b5ea1c8ef58763817a5dd05d5c451920f523edd97f9bfcc4db6eaec.jpg
- data\Design and Analysis of Algorithms\L11-Graph\page_056\L11-Graph_page_056\auto\images\e8a920d2a4e935ccb34ef5719a6458171a2f418420ebe289305ecc64acfe60a0.jpg

---

## Lecture: L11-Graph\page_057\L11-Graph_page_057\auto

Start with the same graph, no

# How far is a node from Gates?

![](images/a7bf178d8382cf229917f2cf29e99a942d825e892e0e758896a4e509cfe7a436.jpg)

![](images/f6c395303e9363ca5b676d37be59ebbc3562c99f99bb5ed3c9c9072ec50096d9.jpg)

These are the final distances!

• For $\mathsf { i } { = } 0 , { \ldots } , | \mathsf { V } | { - } 2 ;$ : • For u in V: • For v in u.neighbors: $\begin{array} { r l } { \mathbf { \Phi } [ ( \mathsf { i } + \lambda ) } &  { } ] \longleftarrow \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } + \lambda ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [ \mathsf { i } ] \cdot \mathbf { \Phi } [  \end{array}$

### Images:
- data\Design and Analysis of Algorithms\L11-Graph\page_057\L11-Graph_page_057\auto\images\a7bf178d8382cf229917f2cf29e99a942d825e892e0e758896a4e509cfe7a436.jpg
- data\Design and Analysis of Algorithms\L11-Graph\page_057\L11-Graph_page_057\auto\images\f6c395303e9363ca5b676d37be59ebbc3562c99f99bb5ed3c9c9072ec50096d9.jpg

---

## Lecture: L11-Graph\page_058\L11-Graph_page_058\auto

• Does it work?

– Yes – Idea to the right.

![](images/349acc48ebf75e49617639f749693b5550bed5a1b2346c27f92d07462d661954.jpg)

• Is it fast? – Not really…

A simple path is a path with no cycles.

# Inductive Hypothesis:

${ \mathsf { d } } ^ { ( \mathrm { i } ) } [ \mathsf { v } ]$ is equal to the cost of the shortest path between s and v with at most i edges.

# Conclusion:

${ \mathsf { d } } ^ { ( | \vee | - 1 ) } [ \vee ]$ is equal to the cost of the shortest simple path between s and $\mathsf { v } .$ (Since all simple paths have at most |V|-1 edges).

### Images:
- data\Design and Analysis of Algorithms\L11-Graph\page_058\L11-Graph_page_058\auto\images\349acc48ebf75e49617639f749693b5550bed5a1b2346c27f92d07462d661954.jpg

---

## Lecture: L11-Graph\page_059\L11-Graph_page_059\auto

# Proof by induction

# Inductive Hypothesis:

• After iteration i, for each v, $\mathsf { d } ^ { ( \mathrm { i } ) } [ \mathsf { v } ]$ is equal to the cost of the shortest path between s and $\boldsymbol { \mathsf { V } }$ with at most i edges.

• Base case:

• After iteration 0…

![](images/7a7389aad1b8c7c632fb849dbae226251b6179d2b9ab580f04a70d8e1bd66ddf.jpg)

• Inductive step:

### Images:
- data\Design and Analysis of Algorithms\L11-Graph\page_059\L11-Graph_page_059\auto\images\7a7389aad1b8c7c632fb849dbae226251b6179d2b9ab580f04a70d8e1bd66ddf.jpg

---

## Lecture: L11-Graph\page_060\L11-Graph_page_060\auto

# Inductive step

• Suppose the inductive hypothesis holds for i.

• We want to establish it for i+1.

Say this is the shortest path between s and v of with at most $\mathrm { i } + 1$ edges:

Let u be the vertex right before v in this path.

Hypothesis: After iteration i, for each v, ${ \mathsf { d } } ^ { ( \mathrm { i } ) } \left[ \mathsf { v } \right]$ is equal to the cost of the shortest path between s and $\boldsymbol { \mathsf { v } }$ with at most i edges.

![](images/8f96e22d08ec8738356d4605695fcd76f6cdd800f85954e52382df7b228e79c5.jpg)

• By induction, $\mathsf { d } ^ { ( \mathrm { i } ) } [ \mathsf { u } ]$ is the cost of a shortest path between s and u of i edges. By setup, $\mathrm { \Delta }$ is the cost of a shortest path between s and v of $\mathrm { i } + 1$ edges. In the $\cdot$ ’st iteration, we ensure ${ \mathbb { C } } ^ { [ ( 1 + 1 ) } [ { \mathbb { V } } ] < = { \mathbb { d } } ^ { [ \bar { 1 } ) } [ { \mathbb { U } } ] + { \mathbb { W } } ( { \mathbb { U } } , { \mathbb { V } } ) .$ So $\frac { 1 } { 2 } ( 1 + 2 ) \times 1 1 < 2$ cost of shortest path between s and $\cdot$ with $\mathrm { i } + 1$ edges. But ${ \mathsf { d } } ^ { ( \mathrm { i } + \underline { { 1 } } ) } [ \mathsf { v } ] = \mathsf { d }$ cost of a particular path of at most $\mathrm { i } + 1$ edges $> =$ cost of shortest path. So $\cdot$ cost of shortest path with at most $\mathrm { i } + 1$ edges.

### Images:
- data\Design and Analysis of Algorithms\L11-Graph\page_060\L11-Graph_page_060\auto\images\8f96e22d08ec8738356d4605695fcd76f6cdd800f85954e52382df7b228e79c5.jpg

---

## Lecture: L11-Graph\page_061\L11-Graph_page_061\auto

# Pros and cons of Bellman-Ford

• Running time: $O / / V | | E | )$ running time

– For each of $\cdot$ steps we update m edges – Slower than Dijkstra

• However, it’s also more flexible in a few ways.

– Can handle negative edges   
If we constantly do these iterations, any changes in the network will eventually propagate through.

---

## Lecture: L11-Graph\page_062\L11-Graph_page_062\auto

# Negative edge weights?

• What is the shortest path from Gates to the Union?

• Shortest paths aren’t defined if there are negative cycles!

![](images/5f2abdf074b5a50b4f8a03c4b365f25992a4ca39b33822fcf0d061bf141f731a.jpg)

• B-F works with negative edge weights…as long as there a notPack egative cycles. – A negative cycle is a path with the same start and d whose cost is 4 negative.

• However, B-F can detect negative cycles.

![](images/505144b1f17ac07aeb1cf4abcdad35ea327c5177564d1344e1b9d53c5af6c29c.jpg)

### Images:
- data\Design and Analysis of Algorithms\L11-Graph\page_062\L11-Graph_page_062\auto\images\505144b1f17ac07aeb1cf4abcdad35ea327c5177564d1344e1b9d53c5af6c29c.jpg
- data\Design and Analysis of Algorithms\L11-Graph\page_062\L11-Graph_page_062\auto\images\5f2abdf074b5a50b4f8a03c4b365f25992a4ca39b33822fcf0d061bf141f731a.jpg

---

## Lecture: L11-Graph\page_063\L11-Graph_page_063\auto

# How Bellman-Ford deals with negative cycles

• If there are no negative cycles:

Everything works as it should. The algorithm stabilizes after $| \mathsf { V } | - 1$ rounds. Note: Negative edges are okay!!

• If there are negative cycles: – Not everything works as it should… • it couldn’t possibly work, since shortest paths aren’t well-defined if there are negative cycles. – The d[v] values will keep changing.

• Solution: Go one round more and see if things change. If so, return NEGATIVE CYCLE $\cdot$

---

## Lecture: L11-Graph\page_064\L11-Graph_page_064\auto

• The Bellman-Ford algorithm:

– Finds shortest paths in weighted graphs with negative edge weights – runs in time O(|V||E|) on a graph $\textcircled{4}$ with n vertices and m edges.

• If there are no negative cycles in G: – the BF algorithm terminates with $( 1 1 4 - 1 ) \times 1 = 9 6 ( s , V )$

• If there are negative cycles in G: – the BF algorithm returns negative cycle.

---

## Lecture: L11-Graph\page_065\L11-Graph_page_065\auto

# Bellman-Ford is also used in practice.

• eg, Routing Information Protocol (RIP) uses something like BellmanFord.

– Older protocol, not used as much anymore.

• Each router keeps a table of distances to every other router.

• Periodically we do a Bellman-Ford update.

• This means that if there are changes in the network, this will propagate. (maybe slowly…)

<table><tr><td rowspan=1 colspan=1>Destination</td><td rowspan=1 colspan=1>Cost to get there</td><td rowspan=1 colspan=1>Send to whom?</td></tr><tr><td rowspan=1 colspan=1>172.16.1.0</td><td rowspan=1 colspan=1>34</td><td rowspan=1 colspan=1>172.16.1.1</td></tr><tr><td rowspan=1 colspan=1>10.20.40.1</td><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>192.168.1.2</td></tr><tr><td rowspan=1 colspan=1>10.155.120.1</td><td rowspan=1 colspan=1>9</td><td rowspan=1 colspan=1>10.13.50.0</td></tr></table>

![](images/69f0e3268e0c700159f63ad7edd8d25cc1436ac2c7fc31885a846daf3a0c9931.jpg)

### Images:
- data\Design and Analysis of Algorithms\L11-Graph\page_065\L11-Graph_page_065\auto\images\69f0e3268e0c700159f63ad7edd8d25cc1436ac2c7fc31885a846daf3a0c9931.jpg
- data\Design and Analysis of Algorithms\L11-Graph\page_065\L11-Graph_page_065\auto\images\e5917eca13b2b1eeb6ef49ff5a250cc314e904317a5458c121ca528cd56d5d8f.jpg

---

## Lecture: L11-Graph\page_066\L11-Graph_page_066\auto

# All-pairs shortest paths

---

## Lecture: L11-Graph\page_067\L11-Graph_page_067\auto

# All-pairs shortest paths

Input: Digraph $G = ( V , E )$ , where $V = \{ 1 , 2 , . . . , n \}$ , with edge-weight function $w : E \to \mathsf { R }$ .

Output: $n \times n$ matrix of shortest-path lengths $\delta ( i , j )$ for all $i , j \in V .$ .

# IDEA:

• Run Bellman-Ford once from each vertex.

---

## Lecture: L11-Graph\page_068\L11-Graph_page_068\auto

# Bellman-Ford algorithm

# Bellman-Ford\*(G,s):

• ${ \mathsf { d } } ^ { ( 0 ) } [ \mathsf { v } ] = \infty$ for all v in V   
• ${ \mathsf { d } } ^ { ( 0 ) } [ { \mathsf { s } } ] = 0$   
• For i=0,…,n-1: • For v in V: d(i+1)[v] ← min( d(i) [v] , minu in v.inNeighbors {d(i) [u] + w(u,v)} )

If d(n-1) != d(n) : の Return NEGATIVE CYCLE $\textcircled{8}$

$$
\bullet \mathrm { o t h e r w i s e } , \mathsf { d i s t } ( \mathsf { s } , \mathsf { v } ) = \mathsf { d } ^ { ( \mathsf { n } - 1 ) } [ \mathsf { v } ]
$$

Bellman-Ford is also an example of… Dynamic Programming!

### Images:
- data\Design and Analysis of Algorithms\L11-Graph\page_068\L11-Graph_page_068\auto\images\9c2f2577e9aa7113dae8bd20d2359d7e91109e3a6b1d6666cd7720ba53cdffcc.jpg
- data\Design and Analysis of Algorithms\L11-Graph\page_068\L11-Graph_page_068\auto\images\c53aaccdedb50caf93c41dedb2e0662f9f642c72db49640b8a49ebf6617934b1.jpg

---

## Lecture: L11-Graph\page_069\L11-Graph_page_069\auto

# All-pairs shortest paths

Input: Digraph $G = ( V , E )$ , where $V = \{ 1 , 2 , . . . , n \}$ , with edge-weight function $w : E \to \mathsf { R }$ .

Output: $n \times n$ matrix of shortest-path lengths $\delta ( i , j )$ for all $i , j \in V .$ .

# IDEA:

$\textcircled { \scriptsize { 1 } }$ Run Bellman-Ford once from each vertex.

$\bullet$ $\mathsf { T i m e }$ .

• Dense graph $( \Theta ( n ^ { 2 } ) \mathsf { e d g e s } ) \Rightarrow \Theta ( n ^ { 4 } )$ time in the worst case.

Good first try! Can we use DP to solve it？

---

## Lecture: L11-Graph\page_070\L11-Graph_page_070\auto

# Optimal substructure

Sub-problem(k-1):   
For all pairs, $\cdot$ find the cost of the shortest path from u to $\mathsf { V } ,$ so that all the internal vertices on that path are in $\angle B A C = \angle C A E = 1 8 0 ^ { \circ }$

Let $\mathsf { D } ^ { ( \mathsf { k } - 1 ) } [ \mathsf { u } , \mathsf { v } ]$ be the solution to Sub-problem(k-1).

![](images/583c1fcccc66bbeeca199cb1b32f612485a954b64d46ad3178fd2c021fdcaa4f.jpg)

Our DP algorithm will   
fill in the   
n-by-n arrays   
D(0), D(1), ,…, D(n)   
iteratively and then   
we'll be done.

# Label the vertices 1,2,…,n

(We omit some edges in the picture below – meant to be a cartoon, not an example).

![](images/0506f8f2f63761a0b9b46a05ed66e36df77c24c136825ca7a64d3dc044abdd87.jpg)

Question: How can we find D(k)[u,v] using D(k-1)?

![](images/ad4bafe5ae92db0f222957efa8bd6e80a6cd2442b941210c628f0cc25e9682bd.jpg)

### Images:
- data\Design and Analysis of Algorithms\L11-Graph\page_070\L11-Graph_page_070\auto\images\0506f8f2f63761a0b9b46a05ed66e36df77c24c136825ca7a64d3dc044abdd87.jpg
- data\Design and Analysis of Algorithms\L11-Graph\page_070\L11-Graph_page_070\auto\images\583c1fcccc66bbeeca199cb1b32f612485a954b64d46ad3178fd2c021fdcaa4f.jpg
- data\Design and Analysis of Algorithms\L11-Graph\page_070\L11-Graph_page_070\auto\images\ad4bafe5ae92db0f222957efa8bd6e80a6cd2442b941210c628f0cc25e9682bd.jpg

---

## Lecture: L11-Graph\page_071\L11-Graph_page_071\auto

# How can we find D(k)[u,v] using D(k-1)?

$\mathsf { D } ^ { ( \mathsf { k } ) } [ \mathsf { u } , \mathsf { v } ]$ is the cost of the shortest path from u to v so that all internal vertices on that path are in $\{ 1 , . . . , \mathsf { k } \}$ .

![](images/7618af9d91b2b9d67435d8c8084d1c45284f959ba47983c41aa1b192ed163f78.jpg)

### Images:
- data\Design and Analysis of Algorithms\L11-Graph\page_071\L11-Graph_page_071\auto\images\7618af9d91b2b9d67435d8c8084d1c45284f959ba47983c41aa1b192ed163f78.jpg

---

## Lecture: L11-Graph\page_072\L11-Graph_page_072\auto

# How can we find D(k)[u,v] using D(k-1)?

$\mathsf { D } ^ { ( \mathsf { k } ) } [ \mathsf { u } , \mathsf { v } ]$ is the cost of the shortest path from u to v so that all internal vertices on that path are in $\{ 1 , . . . , \mathsf { k } \}$ .

![](images/89ad85d37a0d028401e532410703023817249930d48efce2dfa037534dda81bc.jpg)

### Images:
- data\Design and Analysis of Algorithms\L11-Graph\page_072\L11-Graph_page_072\auto\images\89ad85d37a0d028401e532410703023817249930d48efce2dfa037534dda81bc.jpg

---

## Lecture: L11-Graph\page_073\L11-Graph_page_073\auto

# How can we find D(k)[u,v] using D(k-1)?

$\mathsf { D } ^ { ( \mathsf { k } ) } [ \mathsf { u } , \mathsf { v } ]$ is the cost of the shortest path from u to v so that all internal vertices on that path are in $\{ 1 , . . . , \mathsf { k } \}$ .

![](images/de8569bc3b5a2a6e45fb6c0418fd510b6810d4f59e857373b5afd8ffd060d3e5.jpg)

### Images:
- data\Design and Analysis of Algorithms\L11-Graph\page_073\L11-Graph_page_073\auto\images\de8569bc3b5a2a6e45fb6c0418fd510b6810d4f59e857373b5afd8ffd060d3e5.jpg

---

## Lecture: L11-Graph\page_074\L11-Graph_page_074\auto

# Case 2 continued

Suppose there are no negative cycles.

# Case 2: we need vertex k.

Then WLOG the shortest path from u to v through {1,…,k} is simple.

If that path passes through k, it must look like this: ● This path is the shortest path from u to k through $\{ 1 , . . . , \mathsf { k } \mathrm { - } 1 \}$ . sub-paths of shortest paths are shortest paths

![](images/ddea2f04e6419d66ae581e8225d2d6265773960b07555b5356748bed28d334e5.jpg)

Similarly for this path.

D(k)[u,v] = D(k-1)[u,k] + D(k-1)[k,v]

### Images:
- data\Design and Analysis of Algorithms\L11-Graph\page_074\L11-Graph_page_074\auto\images\ddea2f04e6419d66ae581e8225d2d6265773960b07555b5356748bed28d334e5.jpg

---

## Lecture: L11-Graph\page_075\L11-Graph_page_075\auto

# How can we find D(k)[u,v] using D(k-1)?

![](images/4e3f94325dd42d9f0d96151c465c42f119f88c1ad4fb57e87c25f586711d6483.jpg)  
Case 1: we don’t need vertex k.

![](images/140b7d5e93fe6f9f31fc330bc91cb7e9071aa1e24e1f1a3cb72ca45492d28796.jpg)  
Case 2: we need vertex k.

$$
\mathsf { D } ^ { ( \mathsf { k } ) } [ \mathsf { u } , \mathsf { v } ] = \mathsf { D } ^ { ( \mathsf { k } - 1 ) } [ \mathsf { u } , \mathsf { v } ]
$$

$$
\mathsf { D } ^ { ( \mathsf { k } ) } [ \mathsf { u } , \mathsf { v } ] = \mathsf { D } ^ { ( \mathsf { k } - 1 ) } [ \mathsf { u } , \mathsf { k } ] + \mathsf { D } ^ { ( \mathsf { k } - 1 ) } [ \mathsf { k } , \mathsf { v } ]
$$

### Images:
- data\Design and Analysis of Algorithms\L11-Graph\page_075\L11-Graph_page_075\auto\images\140b7d5e93fe6f9f31fc330bc91cb7e9071aa1e24e1f1a3cb72ca45492d28796.jpg
- data\Design and Analysis of Algorithms\L11-Graph\page_075\L11-Graph_page_075\auto\images\4e3f94325dd42d9f0d96151c465c42f119f88c1ad4fb57e87c25f586711d6483.jpg
- data\Design and Analysis of Algorithms\L11-Graph\page_075\L11-Graph_page_075\auto\images\6061656ee7758b4c9929a8c3284847d2537c1e6687832921f63b20067bc4be12.jpg
- data\Design and Analysis of Algorithms\L11-Graph\page_075\L11-Graph_page_075\auto\images\f7727c6f02982f7bb8a744a79c3a211214ce35fa560ab26b6bb4b11b53f00f66.jpg

---

## Lecture: L11-Graph\page_076\L11-Graph_page_076\auto

# How can we find D(k)[u,v] using D(k-1)?

$\bullet \mathsf { D } ^ { ( \mathsf { k } ) } [ \mathsf { u } , \mathsf { v } ] = \mathsf { m i n } \{ \qquad , \mathsf { D } ^ { ( \mathsf { k } - 1 ) } [ \mathsf { u } , \mathsf { k } ] +$ )[k,v] }

Case 1: Cost of shortest path through {1,…,k-1}

Case 2: Cost of shortest path from u to k and then from k to v through {1,…,k-1}

• Optimal substructure: – We can solve the big problem using solutions to smaller problems.

• Overlapping sub-problems: $- \mathsf { D } ^ { ( \mathsf { k } - \perp ) } [ \mathsf { k } , \mathsf { v } ]$ can be used to help compute D(k)[u,v] for lots of different u’s.

### Images:
- data\Design and Analysis of Algorithms\L11-Graph\page_076\L11-Graph_page_076\auto\images\ab532d7a73c81e625fdc77a53d634ec06c6095f358ed8ed9f9b345ed673aa277.jpg

---

## Lecture: L11-Graph\page_077\L11-Graph_page_077\auto

# How can we find D(k)[u,v] using D(k-1)?

$$
\begin{array} { r } { \mathfrak { d } [ \mathsf { u } , \mathsf { v } ] = \mathsf { m i n } \{ \mathsf { D } ^ { ( \mathsf { k } - 1 ) } [ \mathsf { u } , \mathsf { v } ] , \mathsf { D } ^ { ( \mathsf { k } - 1 ) } [ \mathsf { u } , \mathsf { k } ] + \mathsf { D } ^ { ( \mathsf { k } - 1 ) } [ \mathsf { k } , \mathsf { v } ] } \end{array}
$$

Case 1: Cost of shortest path through {1,…,k-1}

Case 2: Cost of shortest path from u to k and then from k to v through {1,…,k-1}

• Using our $\textcircled{1}$ paradigm, this immediately gives us an algorithm!

![](images/a08d152e8e15dd484b5f89de986ce4e66aceb1f1fac304cf378e6ed0a3b4c4a6.jpg)

### Images:
- data\Design and Analysis of Algorithms\L11-Graph\page_077\L11-Graph_page_077\auto\images\008c338b7ea1ff98c1e74b417b77893d55cce4de7f1eb3a7db9ac845f6d5f241.jpg
- data\Design and Analysis of Algorithms\L11-Graph\page_077\L11-Graph_page_077\auto\images\a08d152e8e15dd484b5f89de986ce4e66aceb1f1fac304cf378e6ed0a3b4c4a6.jpg

---

## Lecture: L11-Graph\page_078\L11-Graph_page_078\auto

# Floyd-Warshall algorithm

• Initialize n-by-n arrays D(k) for k = 0,…,n – D(k)[u,u] = 0 for all u, for all k – D(k)[u,v] = ∞ for all u ≠ v, for all k – D(0)[u,v] = weight(u,v) for all (u,v) in E.

![](images/c09f54f0ddec7536618ea31de122e10932653e427903cc6380583979c0a8172b.jpg)

The base case checks out: the only path through zero other vertices are edges directly from u to v.

$\mathbf { \sigma } \cdot \mathsf { F o r } \ k = 1 , \ . . . , \ \mathsf { n } ;$ – For pairs u,v in $\mathsf { V } ^ { 2 }$ : • $ { \sf D } ^ { ( \mathrm { k } ) } [ { \sf u } , { \sf v } ] = \sf { m i n } \{ \mathrm { ~ \qquad ~ } , { \sf D } ^ { ( \mathrm { k } - 1 ) } [ { \sf u } , { \sf k } ] + \mathrm { ~ \qquad ~ }  \}$

• Return D(n)

This is a bottom-up algorithm.

### Images:
- data\Design and Analysis of Algorithms\L11-Graph\page_078\L11-Graph_page_078\auto\images\c09f54f0ddec7536618ea31de122e10932653e427903cc6380583979c0a8172b.jpg

---

## Lecture: L11-Graph\page_079\L11-Graph_page_079\auto

# We’ve basically just shown

• Theorem:

If there are no negative cycles in a weighted directed graph G, then the FloydWarshall algorithm, running on $\mathsf { G }$ , returns a matrix D(n) so that:

D(n)[u,v] = distance between u and v in G.

• Running time: ${ \mathsf { O } } ( { \mathsf { n } } ^ { 3 } )$ – Better than running Bellman-Ford n times!

Work out the details of a proof!

• Storage:

– Need to store two n-by-n arrays, and the original graph.

As with Bellman-Ford, we don’t really need to store all n of the D(k).

### Images:
- data\Design and Analysis of Algorithms\L11-Graph\page_079\L11-Graph_page_079\auto\images\5d9f4626f73668ac70d266906b65cb408f16fc770b92b450595078ae16734050.jpg

---

## Lecture: L11-Graph\page_080\L11-Graph_page_080\auto

# What if there are negative cycles?

• Just like Bellman-Ford, Floyd-Warshall can detect negative cycles: “Negative cycle” means that there’s some v so that there is a path from v to v that has cost $< 0$ . – Aka, D(n)[v,v] < 0.

• Algorithm:

– Run Floyd-Warshall as before. – If there is some v so that $0 . 0 2 \times 0 . 0 1 < 0 . 0 2$ return negative cycle.

---

## Lecture: L11-Graph\page_081\L11-Graph_page_081\auto

# Shortest Path

# Single-source shortest paths

Nonnegative edge weights

Dijkstra’s algorithm: $O ( | E | + | V | \lg | V | )$

General

Bellman-Ford algorithm: $O / / V | | E | )$

# All-pairs shortest paths

Nonnegative edge weights

Dijkstra’s algorithm $| V |$ times: $O ( | V | | E | + | V | ^ { 2 } \lg | V | )$

General

Floyd-Warshall algorithms: $\Theta ( | V | ^ { 3 } )$ .

### Images:
- data\Design and Analysis of Algorithms\L11-Graph\page_081\L11-Graph_page_081\auto\images\e74532b58fe42e8f9d9e30903fac0f0715cbd797291da4800335c2832b1dd694.jpg

---

## Lecture: Lab-01\page_001\Lab-01_page_001\auto

# Lab Exercises 1: Python Development Setup

# 1. Introduction

This guide introduces how to configure a basic Python development environment on your own computer, and also cover advanced topics such as:

(1) Using virtual environments for projects (2) Installing third-party packages (3) Managing multiple Python versions.

# 2. Objectives

(1) Install Python   
(2) Install an editor   
(3) Create and use virtual environments   
(4) Manage Python Packages   
(5) Use Vscode   
(6) Use OJ platform

# 3. Installation

The following is a basic installation tutorial for Python. On macOS and Windows systems, the operations are similar.

NOTE: You can use any of the following configurations for Python development:

(1) Official Python (2) Vscode $^ +$ Anaconda (recommended)

---

## Lecture: Lab-01\page_002\Lab-01_page_002\auto

# 3.1 Install Official Python

1. Visit the official website (https://www.python.org/downloads/) to download the latest stable release(e.g., Python3.13 (https://www.python.org/ftp/python/3.13.0/ python-3.13.0-amd64.exe)).

![](images/08a09f4e24c705245b35483e70a246415e51cce8b83f128bc518ab123547da16.jpg)

2. Double-click the installer to run it. On the first screen, Check the box labeled Add python.exe to PATH at the bottom. Click on Customize installation if you want to choose specific features or installation locations. Otherwise, click Install Now for default settings.

![](images/45e39c89c3f47871a50479013a087d988918400a5d83fdaadcd8166b11a10f27.jpg)

3. Wait for the installation process to complete. Once done, click Close to exit the installer.

![](images/8b900b4a368709ca436718c4be42ada37c98189799b2e372fa04c9acdb7875df.jpg)

### Images:
- data\Design and Analysis of Algorithms\Lab-01\page_002\Lab-01_page_002\auto\images\08a09f4e24c705245b35483e70a246415e51cce8b83f128bc518ab123547da16.jpg
- data\Design and Analysis of Algorithms\Lab-01\page_002\Lab-01_page_002\auto\images\45e39c89c3f47871a50479013a087d988918400a5d83fdaadcd8166b11a10f27.jpg
- data\Design and Analysis of Algorithms\Lab-01\page_002\Lab-01_page_002\auto\images\8b900b4a368709ca436718c4be42ada37c98189799b2e372fa04c9acdb7875df.jpg

---

## Lecture: Lab-01\page_003\Lab-01_page_003\auto

4. Click on the Start button or press the Windows key on your keyboard. Type PowerShell in the search bar. Click on Windows PowerShell from the search results to open it.

![](images/a9a4a60f11150d3879e7782defba5d74dc2ce2a64003fc51744d02efc21786b0.jpg)

5. Type python --version and press Enter. You should see the installed Python version number.

PS C:\Users\tjj> python --version Python 3.13.0

If it fails, you need to manually check your environment variable settings and add the folloing 2 lines into System variables.

C:\YourPath\Python\Python313\ C:\YourPath\Python\Python313\Scripts\

![](images/7a30b456aaf653382850cb5a5bacf9b56e533788cc607800c0fa589e10c9b171.jpg)

### Images:
- data\Design and Analysis of Algorithms\Lab-01\page_003\Lab-01_page_003\auto\images\7a30b456aaf653382850cb5a5bacf9b56e533788cc607800c0fa589e10c9b171.jpg
- data\Design and Analysis of Algorithms\Lab-01\page_003\Lab-01_page_003\auto\images\a9a4a60f11150d3879e7782defba5d74dc2ce2a64003fc51744d02efc21786b0.jpg

---

## Lecture: Lab-01\page_004\Lab-01_page_004\auto

# 环境变量

![](images/c611474aec9cc8fa2e6359805253e3658aab15c8437d199572ec61372c6e8fd1.jpg)

# 3.2 Install Vscode and Anaconda

# 3.2.1 Visual Studio Code (recommended)

Visual Studio Code (VS Code) is a free, open-source code editor developed by Microsoft. It is widely used by developers for its versatility and extensive customization options.

1. Install VS Code Go to the VS Code website (https://code.visualstudio.com/Download) and click Download for your operating system (Windows, macOS, or Linux). Once downloaded, open the installer and follow the on-screen instructions.

![](images/b7400bfb65e0d0f88bbbac2186cda76ae259cfda578d4547de69dac53a1ce97b.jpg)

### Images:
- data\Design and Analysis of Algorithms\Lab-01\page_004\Lab-01_page_004\auto\images\b7400bfb65e0d0f88bbbac2186cda76ae259cfda578d4547de69dac53a1ce97b.jpg
- data\Design and Analysis of Algorithms\Lab-01\page_004\Lab-01_page_004\auto\images\c611474aec9cc8fa2e6359805253e3658aab15c8437d199572ec61372c6e8fd1.jpg

---

## Lecture: Lab-01\page_005\Lab-01_page_005\auto

![](images/8b50b340f4656c3f4fe0b966d2b9953c74c529fdda7c44da35cb7157f7fc72e7.jpg)

After installation, open VS Code.

![](images/6a48a0204b651bc0e7970b10c42105c6e1a2379553355854e40ebfb023b7939f.jpg)

# 2. Install Python Extension

(1) In VS Code, select View $>$ Extensions to open the Extensions view.

![](images/57883c53d9443f03831c9cbbed610b03cf62f79cb267604acda2142c54dec4db.jpg)

### Images:
- data\Design and Analysis of Algorithms\Lab-01\page_005\Lab-01_page_005\auto\images\57883c53d9443f03831c9cbbed610b03cf62f79cb267604acda2142c54dec4db.jpg
- data\Design and Analysis of Algorithms\Lab-01\page_005\Lab-01_page_005\auto\images\6a48a0204b651bc0e7970b10c42105c6e1a2379553355854e40ebfb023b7939f.jpg
- data\Design and Analysis of Algorithms\Lab-01\page_005\Lab-01_page_005\auto\images\8b50b340f4656c3f4fe0b966d2b9953c74c529fdda7c44da35cb7157f7fc72e7.jpg

---

## Lecture: Lab-01\page_006\Lab-01_page_006\auto

(2) Filter the list of available extensions by entering python in the search box at the top of the Extensions view.   
(3) Select the Python extension published by Microsoft. The details about that extension appear in a tabbed panel on the right. In either the Extensions panel, or in the main panel, select Install.

![](images/b8f53efc7f6492b85e9945dbb74ef6c690d7db044dac2434d455c064b7817ca7.jpg)

When the installation is complete, the Install button changes to a Settings icon in the Extensions view or two buttons, Disable and Uninstall in the main panel. This message lets you know that you've successfully installed the Python extension for Windows.

![](images/a272bfe8ab7606c5f0f51959fefd6eab2f6117ecf5595678522437994337f2d4.jpg)

# 3.2.2 Pycharm (optional)

PyCharm (https://www.jetbrains.com/pycharm/download/) is an integrated development environment (IDE) specifically designed for Python programming. Developed by JetBrains, PyCharm offers a wide range of features that streamline the coding process, making it a popular choice among Python developers.

(1) PyCharm Professional Edition requires a subscription or a one-time purchase. It includes advanced features that are particularly useful for professional developers. JetBrains offers a special program (https://www.jetbrains.com/student/) for students to access their Professional Edition tools, including PyCharm, for free. (2) PyCharm Community Edition is open-source and available for free to all users. It is suitable for students, hobbyists, and developers who need basic Python development capabilities.

# 3.2.3 Anaconda

If you’re in the data science community, you might already be using Anaconda (or Miniconda). Anaconda is a sort of one-stop shop for data science software that supports more than just Python.

### Images:
- data\Design and Analysis of Algorithms\Lab-01\page_006\Lab-01_page_006\auto\images\a272bfe8ab7606c5f0f51959fefd6eab2f6117ecf5595678522437994337f2d4.jpg
- data\Design and Analysis of Algorithms\Lab-01\page_006\Lab-01_page_006\auto\images\b8f53efc7f6492b85e9945dbb74ef6c690d7db044dac2434d455c064b7817ca7.jpg

---

## Lecture: Lab-01\page_007\Lab-01_page_007\auto

You can download Anaconda from the official website (https://www.anaconda.com/ download/success) and install it with default settings.

![](images/190d564b0c5eef126fbd88eff272f52b07e3b090fc3d6108f8e1344684ebcfc1.jpg)

Note: When installing Anaconda, you also need to check the option "Add Anaconda to my PATH environment variable". If you forget to check it, you will need to add the environment variable manually: locate the Anaconda installation directory (usually something like C:\ProgramData\Anaconda3 or C:\Users\YourUsername\Anaconda3), and add the following paths to the PATH of the system environment variables:

Anaconda installation directory Anaconda installation directory\Scripts Anaconda installation directory\Library\bin

# 4. Create and use virtual environments

# 4.1 Conda Source

We recommend using Tsinghua Tuna Mirror (https://mirrors.tuna.tsinghua.edu.cn/ help/anaconda/) to download packages of conda.

First, you can find .condarc file:   
(1) macOS: $\ S \{ \mathrm { H O M E } \}$ }/.condarc   
(2) Windows: C:\Users\ $\checkmark$ YourUserName>\.condarc

For windows users, you can execute conda config --set show_channel_urls yes in your terminal if you can not find .condarc file.

For macOS users, you can enter HOME directory and execute open -e .condarc to open the file.

After that, you can modify the contents of .condarc to use tuna mirror (copy the following content and paste it):

### Images:
- data\Design and Analysis of Algorithms\Lab-01\page_007\Lab-01_page_007\auto\images\190d564b0c5eef126fbd88eff272f52b07e3b090fc3d6108f8e1344684ebcfc1.jpg

---

## Lecture: Lab-01\page_008\Lab-01_page_008\auto

channels:

- defaults show_channel_urls: true default_channels:

- https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/msys2

custom_channels:

conda-forge: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud pytorch: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud

---

## Lecture: Lab-01\page_009\Lab-01_page_009\auto

# 4.2 Common conda commands

Managing Conda Itself

1. Check Conda Version: conda --version   
2. Update Conda: conda update conda

# Managing Environments

1. Create a New Environment: conda create -n your_env_name python=3.xx   
2. Activate an Environment: conda activate your_env_name   
3. Deactivate an Environment: conda deactivate   
4. List All Environments: conda env list   
5. Remove an Environment: conda remove -n your_env_name --all   
6. Export an Environment: conda env export --name env_name $>$ env_name.yml   
7. Create an Environment from a File: conda env create -f env_name.yml

# Managing Packages

1. List Installed Packages: conda list   
2. Install a Package: conda install package_name   
3. Install a Specific Version of a Package: conda install package_name $\equiv$ version   
4. Update a Package: conda update package_name   
5. Remove a Package: conda uninstall package_name

DO NOT MODIFY YOUR BASE ENVIRONMENT.

# 4.3 Create a virtual environment with conda

A Python virtual environment is an isolated environment that allows you to manage dependencies for a specific Python project without affecting other projects. It essentially creates a self-contained directory that contains a Python interpreter and copies of any necessary libraries.

# 0. Python version Management

Python has multiple versions, with the most significant division being between Python 2 and Python 3, which are not compatible with each other. Certain projects may require specific Python versions, so managing different versions is essential. Here, we introduce the conda tool, which helps in installing, switching, and using different Python versions.

---

## Lecture: Lab-01\page_010\Lab-01_page_010\auto

![](images/3e750a4a14952858938097443bf6f3d7c63dd6452448d752dd40a226e0040686.jpg)  
Python release cycle

# 1. Open Terminal or Command Prompt

Start by opening your terminal or command prompt where you have Conda installed. To create a new virtual environment, use the following command:

conda create --name your_env_name python $_ { 1 } { = } 3 . 1 2$

Replace your_env_name with the desired name for your new virtual environment.

# 2. Activate the Virtual Environment

Once the environment is created, activate it using the command:

![](images/c5bf3c055eafe1ee41a4230dd20b78441a29750d0f7eac6c83ad11ddf1cd1047.jpg)

This command switches your current Python environment to the newly created one.

# 3. Install Packages

You can now install packages into your virtual environment using Conda. For example, to install numpy, use:

![](images/86cc80c76413649203d3c306f09502d752a08ba2a9b7f296ae8660acb7546276.jpg)

Wait a moment the new package will be installed.

### Images:
- data\Design and Analysis of Algorithms\Lab-01\page_010\Lab-01_page_010\auto\images\3e750a4a14952858938097443bf6f3d7c63dd6452448d752dd40a226e0040686.jpg
- data\Design and Analysis of Algorithms\Lab-01\page_010\Lab-01_page_010\auto\images\86cc80c76413649203d3c306f09502d752a08ba2a9b7f296ae8660acb7546276.jpg
- data\Design and Analysis of Algorithms\Lab-01\page_010\Lab-01_page_010\auto\images\c5bf3c055eafe1ee41a4230dd20b78441a29750d0f7eac6c83ad11ddf1cd1047.jpg

---

## Lecture: Lab-01\page_011\Lab-01_page_011\auto

# 5. Usage of Vscode

# 5.1 Select a virtual environment

In VS Code, press Ctrl+Shift+P to open the Command Palette.

Type and select Python: Select Interpreter. Ensure your new environment is selected. It should look something like .\.venv\Scripts\python.exe. After this, you should see the selected interpreter in the bottom right corner.

![](images/9a1c2df6957aab177524b4c7ab637e5c01a825a59f0c58d67cdb6b5a6f46eedf.jpg)

# 5.2 Create Python scripts

1. Create a new project folder in the File Explorer.   
2. Use VS Code's File $>$ Open Folder to open the project folder you just created.

![](images/bf525a16229e35459955352523a9fab6633c932ea72bfde8d73cc885f5bd44b1.jpg)

4. From the File Explorer toolbar, select the New File button to create your .py file:

### Images:
- data\Design and Analysis of Algorithms\Lab-01\page_011\Lab-01_page_011\auto\images\9a1c2df6957aab177524b4c7ab637e5c01a825a59f0c58d67cdb6b5a6f46eedf.jpg
- data\Design and Analysis of Algorithms\Lab-01\page_011\Lab-01_page_011\auto\images\bf525a16229e35459955352523a9fab6633c932ea72bfde8d73cc885f5bd44b1.jpg

---

## Lecture: Lab-01\page_012\Lab-01_page_012\auto

![](images/b0e8da9c184644bc66e7cbb8a338b0ec4969a9e8c6b77636bb3d24fb14fa39de.jpg)

5. Name the file first.py, and VS Code will automatically open it in the editor:

![](images/4d75be3b7c948ce235a2fc51bd821602bd9c351016ce08e6b4341d960287178d.jpg)

6. Write Python code

# print('hello world!')

7. Click the Run Python File play button in the top-right side of the editor. The button opens a terminal panel in which your Python interpreter is automatically activated, then runs python3 first.py (macOS/Linux) or python first.py (Windows):

![](images/c3e856da8123f882969c3c9eaa16ecea034907a2435c7d88eaab7ddff42e08b9.jpg)

### Images:
- data\Design and Analysis of Algorithms\Lab-01\page_012\Lab-01_page_012\auto\images\4d75be3b7c948ce235a2fc51bd821602bd9c351016ce08e6b4341d960287178d.jpg
- data\Design and Analysis of Algorithms\Lab-01\page_012\Lab-01_page_012\auto\images\b0e8da9c184644bc66e7cbb8a338b0ec4969a9e8c6b77636bb3d24fb14fa39de.jpg
- data\Design and Analysis of Algorithms\Lab-01\page_012\Lab-01_page_012\auto\images\c3e856da8123f882969c3c9eaa16ecea034907a2435c7d88eaab7ddff42e08b9.jpg

---

## Lecture: Lab-01\page_013\Lab-01_page_013\auto

8. (Optional) Press $\mathrm { C t r l } { + }$ to open the Terminal. Find your current working path and press cd your_path to enter the working directory. In your terminal, press python first.py to execute your python scipt.

Congrats, you just ran your first Python code in Visual Studio Code!

# 5.3 Create a Jupyter Notebook

# 1. Install Required Extensions.

Open your terminal, activate your own virtual environment, and install a package:

![](images/3b074e8cccd1ba407bebc2eb72dcd90bf5437144b4ffffcf408445ec33c90640.jpg)

![](images/6b57f7c4b871338992e595fbf5664f3306f0a99f19b89c3a23ee54636000895d.jpg)

# 2. Create a New Jupyter Notebook

Click on the "File" menu and select New File. Save the new file with a .ipynb extension, for example, my_notebook.ipynb. You can now start writing your Jupyter notebook code in this file.

# 3. Write Code in Cells

(1) Open my_notebook.ipynb, click Select Kernel and select Python Environment.   
Chosse your own virtual environment.

![](images/add2f8e777ce87d50ea393534d022990cbfedae9a7380fdde4c47f05345518e9.jpg)

(2) To add a new code cell, click on the $^ +$ code button in the toolbar or press Alt $^ +$ Enter.

![](images/b25657f1c982008a78c3c4bb73bfa7170d188e2c734936a65e689d2af81a8cbc.jpg)

(3) Write your Python code in the cell.

(4) To execute the code in a cell, click on the Run button or press Shift $^ +$ Enter

![](images/7dba35441e0563fd8b8bc4c9a8ef8d059a1dde85d0f578d00028c0836788da51.jpg)

(5) To add an extra cell, press Shift+Enter or Click right button ${ } = > { }$ Insert Cell ${ } - > { }$ Insert

### Images:
- data\Design and Analysis of Algorithms\Lab-01\page_013\Lab-01_page_013\auto\images\3b074e8cccd1ba407bebc2eb72dcd90bf5437144b4ffffcf408445ec33c90640.jpg
- data\Design and Analysis of Algorithms\Lab-01\page_013\Lab-01_page_013\auto\images\6b57f7c4b871338992e595fbf5664f3306f0a99f19b89c3a23ee54636000895d.jpg
- data\Design and Analysis of Algorithms\Lab-01\page_013\Lab-01_page_013\auto\images\7dba35441e0563fd8b8bc4c9a8ef8d059a1dde85d0f578d00028c0836788da51.jpg
- data\Design and Analysis of Algorithms\Lab-01\page_013\Lab-01_page_013\auto\images\add2f8e777ce87d50ea393534d022990cbfedae9a7380fdde4c47f05345518e9.jpg
- data\Design and Analysis of Algorithms\Lab-01\page_013\Lab-01_page_013\auto\images\b25657f1c982008a78c3c4bb73bfa7170d188e2c734936a65e689d2af81a8cbc.jpg

---

## Lecture: Lab-01\page_014\Lab-01_page_014\auto

# Code Cell Below (or Above).

# 4. Write Markdown in Cells

(1) To add a new markdown cell, click on the $^ +$ Markdown button in the toolbar.

![](images/5ebcb8720dcbcbe4fb3868172be5bae6bf4c366d1fa2c27a704ce22133590fa8.jpg)

(2) Write your markdown code in the cell.   
To execute the code in a cell, click on the Run button.

![](images/b06508e967d711ba1ac4f1699338f5ea6e92942ac4fb96277e654dd5bb69a7f4.jpg)

# 5. Save and Export

Save your Jupyter notebook by clicking on the save icon or using Ctrl $+ \textsf { S }$ You can export your notebook to various formats using the "File" menu.

# 6. Usage of OJ platform

# 6.1 What is an Online Judge?

An Online Judge (OJ) is a system that automatically evaluates programming submissions. It typically provides a collection of problems, each with input and output specifications, and tests your code against hidden datasets. The OJ will return the result (e.g., Accepted, Wrong Answer, Time Limit Exceeded, Memory Limit Exceeded).

# 6.2 2. Getting Started

1. Register / Log in

url: https://onlinejudge.hkust-gz.edu.cn

Create an account on the OJ platform using your email or student ID.

### Images:
- data\Design and Analysis of Algorithms\Lab-01\page_014\Lab-01_page_014\auto\images\5ebcb8720dcbcbe4fb3868172be5bae6bf4c366d1fa2c27a704ce22133590fa8.jpg
- data\Design and Analysis of Algorithms\Lab-01\page_014\Lab-01_page_014\auto\images\b06508e967d711ba1ac4f1699338f5ea6e92942ac4fb96277e654dd5bb69a7f4.jpg

---

## Lecture: Lab-01\page_015\Lab-01_page_015\auto

![](images/ef413d35b334e4db21c5cb26480927117e571aa3f9bf9dd2672ff81bf22d05da.jpg)

# Welcome to OJ

![](images/e99f4222cfb954078437a85f525b2bd182a9ec972eb69fd68dee18079656e012.jpg)

Junning FENG

jfeng496@connect.hkust-gz.edu.cn

# The email already exists

![](images/c967060aebac02ae85d628dd0b4c486580315728a5fcf62e15c5ece3c6d901f4.jpg)

![](images/0f23f3577b05bc4ef33a760bbacd984a9615a9af3575a1f4d0eeed5e583ec8ed.jpg)

# Captcha

syH

captcha is required

Register

Already registed? Login now!

### Images:
- data\Design and Analysis of Algorithms\Lab-01\page_015\Lab-01_page_015\auto\images\0f23f3577b05bc4ef33a760bbacd984a9615a9af3575a1f4d0eeed5e583ec8ed.jpg
- data\Design and Analysis of Algorithms\Lab-01\page_015\Lab-01_page_015\auto\images\c967060aebac02ae85d628dd0b4c486580315728a5fcf62e15c5ece3c6d901f4.jpg
- data\Design and Analysis of Algorithms\Lab-01\page_015\Lab-01_page_015\auto\images\da799685d676d35ce8ae7392288ade3c170ad908ebbb869b92ae542ede927fbf.jpg
- data\Design and Analysis of Algorithms\Lab-01\page_015\Lab-01_page_015\auto\images\e99f4222cfb954078437a85f525b2bd182a9ec972eb69fd68dee18079656e012.jpg
- data\Design and Analysis of Algorithms\Lab-01\page_015\Lab-01_page_015\auto\images\ef413d35b334e4db21c5cb26480927117e571aa3f9bf9dd2672ff81bf22d05da.jpg

---

## Lecture: Lab-01\page_016\Lab-01_page_016\auto

# 2. Browse Problems

Navigate to the Contest page.

![](images/0f09daf321c94644f09a7d6497df24ea3a5d0f1aab849caecf30dcc987f821e6.jpg)

# Choose one of the problems from problem lists

![](images/90c2a4f35f6a2e38c889b8b4d82260360a5af28508e36342d7f2ac714907186e.jpg)

# 3. Read a Problem Statement

Each problem contains:

Description: the task you need to solve. Input format: how data is given. Output format: what your program must print. Constraints: limits on input size, time, and memory. Sample Input/Output: example to test your understanding.

![](images/68a1b6de3be9a4b6e20663b1965beed3b94bebd6045bf6fbae7bc494f8271385.jpg)

# 4. Writing and Testing Your Code

### Images:
- data\Design and Analysis of Algorithms\Lab-01\page_016\Lab-01_page_016\auto\images\0f09daf321c94644f09a7d6497df24ea3a5d0f1aab849caecf30dcc987f821e6.jpg
- data\Design and Analysis of Algorithms\Lab-01\page_016\Lab-01_page_016\auto\images\68a1b6de3be9a4b6e20663b1965beed3b94bebd6045bf6fbae7bc494f8271385.jpg
- data\Design and Analysis of Algorithms\Lab-01\page_016\Lab-01_page_016\auto\images\90c2a4f35f6a2e38c889b8b4d82260360a5af28508e36342d7f2ac714907186e.jpg

---

## Lecture: Lab-01\page_017\Lab-01_page_017\auto

# 1. Choose a Programming Language

The OJ support C, ${ \mathsf { C } } { + } { + }$ , Java, Python, etc.

Make sure your solution follows the input/output requirements exactly (no extra text).

![](images/e5a89d9d4507913de4a44e77ea9fcf539123d50f4f12e6576b20cffe258c4df2.jpg)

2. Test Locally

Use the sample input provided.

Run your program and check that the output matches the sample output exactly.

#

<table><tr><td>Sample1:</td></tr><tr><td>19-&gt;1^2+9^2=82</td></tr><tr><td>82-&gt;8^2+2^2=68</td></tr><tr><td>68-&gt;6^2+8^2=100</td></tr><tr><td>100-&gt;1^2+0^2+0^2=1</td></tr><tr><td>Sample2:</td></tr><tr><td>2-&gt;2^2=4</td></tr><tr><td>4-&gt;4^2=16</td></tr><tr><td>16-&gt;1^2+6^2=37</td></tr><tr><td>37-&gt;3^2+7^2=58</td></tr><tr><td>58-&gt;5^2+8^2=89</td></tr><tr><td>89-&gt;8^2+9^2=145</td></tr><tr><td>145-&gt;1^2+4^2+5^2=42</td></tr><tr><td>42-&gt;4^2+2^2=20</td></tr><tr><td>20-&gt;2^2+0^2=4</td></tr><tr><td></td></tr></table>

# 5. Submitting Your Code

1. Select your language from the drop-down menu.

2. Paste or upload your source code.

### Images:
- data\Design and Analysis of Algorithms\Lab-01\page_017\Lab-01_page_017\auto\images\e5a89d9d4507913de4a44e77ea9fcf539123d50f4f12e6576b20cffe258c4df2.jpg
- data\Design and Analysis of Algorithms\Lab-01\page_017\Lab-01_page_017\auto\images\eb1800a8d5af2547fe5734335bcb6f681f0fc976019f0433443707160e6ea228.jpg

---

## Lecture: Lab-01\page_018\Lab-01_page_018\auto

# 3. Click Submit and wait for the result.

![](images/50faea95452d89c408195b940ffdefb7b7f11a31690180f1c6972389d658a858.jpg)

5. Understanding the Verdicts

Accepted (AC): Your program passed all test cases.

Wrong Answer (WA): Output does not match the expected result.

Time Limit Exceeded (TLE): Your code is too slow. Try optimizing.

Memory Limit Exceeded (MLE): Your program uses too much memory.

Runtime Error (RE): Your program crashed (e.g., division by zero, array out of bounds).

Compilation Error (CE): The code did not compile successfully.

You can view the detailed error message by clicking the Compile Error button

### Images:
- data\Design and Analysis of Algorithms\Lab-01\page_018\Lab-01_page_018\auto\images\50faea95452d89c408195b940ffdefb7b7f11a31690180f1c6972389d658a858.jpg

---

## Lecture: Lab-01\page_019\Lab-01_page_019\auto

![](images/e61020474ab0d3ab929f369db9ad6179fa8b7d7b8f72f90719addc2bd05ba5ce.jpg)

![](images/07c6c4ecadf5e6dbd3db09e8e9bad9492391d0831ad288ebfd8cdb269371dd15.jpg)

# Compile Error

$\vartriangle { \mathbf { \Sigma } } = \ v { U } _ { \Sigma }$

$" ) "$ $\scriptstyle \mathtt { \mathtt { - > } }$

$^ { - > }$ $=$ $n \ ! = \ 1$ $n = = ~ 1$

_name

# Exercises

# 1. Create your own environment

Create a virtual conda environment named <yourname>_2043, i.e. jaden_2043.

Install the following packages:

<table><tr><td>numpy</td></tr><tr><td>matplotlib</td></tr><tr><td>scikit-learn</td></tr><tr><td></td></tr><tr><td>seaborn</td></tr><tr><td>pandas</td></tr><tr><td></td></tr><tr><td>scipy</td></tr></table>

Uninstall the following packages:

### Images:
- data\Design and Analysis of Algorithms\Lab-01\page_019\Lab-01_page_019\auto\images\07c6c4ecadf5e6dbd3db09e8e9bad9492391d0831ad288ebfd8cdb269371dd15.jpg
- data\Design and Analysis of Algorithms\Lab-01\page_019\Lab-01_page_019\auto\images\347cde93d5eb74e1682181b5c39c368eb5599a656abed680703ab6ec01a3d067.jpg
- data\Design and Analysis of Algorithms\Lab-01\page_019\Lab-01_page_019\auto\images\807e5809793d30b47be791d58fab16db30843e35db9888bda000b4aae35a76e9.jpg
- data\Design and Analysis of Algorithms\Lab-01\page_019\Lab-01_page_019\auto\images\e61020474ab0d3ab929f369db9ad6179fa8b7d7b8f72f90719addc2bd05ba5ce.jpg

---

## Lecture: Lab-01\page_020\Lab-01_page_020\auto

<table><tr><td>pandas</td></tr><tr><td></td></tr><tr><td>scipy</td></tr></table>

# 2. Two sum

Write a Python program, define two integer variables, and output the sum of the two numbers.

baseline:

$$
\begin{array} { l } { \mathbf { x } = 2 0 } \\ { \mathbf { y } = 4 3 } \\ { \mathbf { z } = \mathbf { x } + \mathbf { y } } \\ { \mathrm { p r i n t } ( ^ { \mathfrak { n } } \mathbf { x } + \mathbf { y } \mathbf { = } ^ { \mathfrak { n } } , \mathbf { z } ) } \end{array}
$$

### Images:
- data\Design and Analysis of Algorithms\Lab-01\page_020\Lab-01_page_020\auto\images\8203a63820c7c36415d4ba28ab7517f15c6396f309674b1c7cea095980867532.jpg
- data\Design and Analysis of Algorithms\Lab-01\page_020\Lab-01_page_020\auto\images\ff2ab26209a41464d91c99fc09bf1ea492c8301ab405eeb8a8d04fd180fb23d5.jpg

---

## Lecture: Lab-01\page_021\Lab-01_page_021\auto

# 3. Generating random numbers

Write a Python program using the NumPy library to generate an array containing 10 random integers.

baseline:

import numpy as np   
result $=$ np.random.randint(low ${ = } 0$ , high $\scriptstyle 1 = 2 0 4 3$ , size=10)   
print(result)

4. Complete the lab-week1-exercise01 and lab-week1-exercise02 released on the OJ platform.

# Problems List

<table><tr><td></td><td>#</td><td>Title</td><td>Total</td></tr><tr><td>√</td><td>Lab-week1-exercise 01</td><td>Array Sum</td><td></td></tr><tr><td></td><td>Lab-week1-exercise0 2</td><td>Array Maximum</td><td></td></tr></table>

### Images:
- data\Design and Analysis of Algorithms\Lab-01\page_021\Lab-01_page_021\auto\images\960fbc48de7c1e2a74b9f791e1da45c227b2495bb1641fbc697e0a5b7328ea1b.jpg

---

## Lecture: Lab-02\page_001\Lab-02_page_001\auto

# Lab Exercises 2: Binary Search & Python Debugging

# 1. Introduction

This guide reviews the fundamental algorithm of Binary Search and introduces how to debug Python scripts with VS Code on your computer. It also covers two common debugging scenarios:

（1） Debugging without parameters（2） Debugging with parameters

# 2. Binary Search Review

Binary Search is an efficient algorithm for finding an item from a sorted list of items.

Key idea: Binary Search repeatedly divides the list into two halves, and then focuses only on the half that could contain the target item.

# 2.1 Problem formulation

Given a sorted array of integers and a target value, the task is to determine whether the target exists in the array. If it is present, return its index. Otherwise, return $^ { - 1 }$ .

# 2.2 Algorithm

1. Divide the sorted array into two halves by finding the middle index

$$
m i d \gets \lfloor ( l e f t + r i g h t ) / 2 \rfloor
$$

2. Compare the middle element of the sorted array with the target.

3. If the target is found at the middle element, the process is terminated.

4. If the target is not found at the middle element, choose which half will be used as the next search space. $\mathrm { . > }$ If the target is smaller than the middle element, then the left side is used for the next search. $\mathrm { . > }$ If the target is larger than the middle element, then the right side is used for the next search.

### Images:
- data\Design and Analysis of Algorithms\Lab-02\page_001\Lab-02_page_001\auto\images\9c8112f10d0411597f9c8a59ddd85de1fd72928fae65e4e6e34617a08bb1e46e.jpg

---

## Lecture: Lab-02\page_002\Lab-02_page_002\auto

5. This process is continued until the target is found or the search space is exhausted (i.e. left $>$ right).

# 2.3 Example: Searching for 18 in a Sorted Array

Consider the sorted array:

$$
S = \{ 3 , 7 , 9 , 1 2 , 1 3 , 1 8 , 2 0 , 2 3 , 2 7 \}
$$

We want to determine whether target $= 1 8$ exists in S.

![](images/3a09df3e909f9f808faf0c6b493deed2c225eb426ab1a9d5c27f89a512780482.jpg)

Algorithm 1 Binary Search (nums, target)   
Input: a sorted array of integers nums, an integer target   
Output: index of target or $^ { - 1 }$   
1: $l e f t \gets 0$   
2: rig $\mathbf { \chi } _ { t } \gets \mathrm { l e n g t h } ( n u m s ) - 1$   
3: while left $: \le$ right do   
4: $m i d \gets \lfloor ( l e f t + r i g h t ) / 2 \rfloor$   
5: if nums[mid] $=$ target then   
6: return mid   
7: else if nums[mid] $<$ target then   
8: $l e f t \gets m i d + 1$   
9: else   
10: $r i g h t \gets m i d - 1$   
11: end if   
12: end while   
13: return $^ { - 1 }$

# 2.4 Exercises

We have published two exercises on Binary Search in the OJ contest DSAA2043 – Lab02 (password: dsaa2043). Your performance on these exercises will be counted toward your Lab Exercises score. Please complete before September 26.

We hope you can complete these exercises independently without relying on AI tools (Note that only about $20 \%$ of students passed these exercises last semester).

![](images/1a623bed27c40f5a3f7f48746e7ce2782f51e2afd1d5e926f0a9db5896cf93e9.jpg)

### Images:
- data\Design and Analysis of Algorithms\Lab-02\page_002\Lab-02_page_002\auto\images\1a623bed27c40f5a3f7f48746e7ce2782f51e2afd1d5e926f0a9db5896cf93e9.jpg
- data\Design and Analysis of Algorithms\Lab-02\page_002\Lab-02_page_002\auto\images\3a09df3e909f9f808faf0c6b493deed2c225eb426ab1a9d5c27f89a512780482.jpg
- data\Design and Analysis of Algorithms\Lab-02\page_002\Lab-02_page_002\auto\images\ff91560bb8d159cfc78d9cc30b9d031cbcf1fbbe3da2869f78cfa7b81691cc48.jpg

---

## Lecture: Lab-02\page_003\Lab-02_page_003\auto

<table><tr><td colspan="3">Problems List</td><td>AOverview</td></tr><tr><td>Tiltle #</td><td>Total</td><td>AC Rate</td><td>Announcements</td></tr><tr><td>Lab-week2-exercise 01</td><td>Binary Search</td><td>0%</td><td>Problems</td></tr><tr><td>Lab-week2-exercise</td><td>Find Cos BEmert in SotedAay</td><td>0</td><td>三Submissions</td></tr><tr><td>02</td><td></td><td></td><td>d Rankings</td></tr></table>

# 3. What is Bug?

A bug is an error that causes the program to produce an unexpected output, either different from the expected result or no output at all.

In this lab, we will show common types of errors through examples and demonstrate how to identify and resolve them using debugging techniques.

# 3.1 Syntax error

Cause:

When you write code in any programming language, you have to follow its syntax.   
When the syntax of Python is not followed, you get Syntax error.

Common issues:

Missing parentheses: Forgetting required parentheses in function calls, e.g.,   
print “hello”   
Spelling errors: Mistyping, e.g., iff $\mathbf { \boldsymbol { x } } { > } 0$   
Incomplete structure: Statements or brackets not properly closed, e.g.,   
nums=[1,2,3   
Indentation errors: Incorrect or inconsistent indentation, e.g.,   
Wrong： Correct：

![](images/a52c086a9427aaca991f4f7d70b39794df432077cacfb8ec477d56b74a94cb14.jpg)

![](images/1098f5ca17cdf7acd50963fd5b0e2d6bec20f830013da752d4e5bb3b18259a29.jpg)

Detection:

Vscode highlights the error location.

Solution:

Correct the highlighted syntax error. Run the code, and the output will give you some clues.

### Images:
- data\Design and Analysis of Algorithms\Lab-02\page_003\Lab-02_page_003\auto\images\1098f5ca17cdf7acd50963fd5b0e2d6bec20f830013da752d4e5bb3b18259a29.jpg
- data\Design and Analysis of Algorithms\Lab-02\page_003\Lab-02_page_003\auto\images\a1fa7d2e5d4af2a7e24da8a10f9a10cc3389883f53f9ce9e75f84d9f9ac23576.jpg
- data\Design and Analysis of Algorithms\Lab-02\page_003\Lab-02_page_003\auto\images\a52c086a9427aaca991f4f7d70b39794df432077cacfb8ec477d56b74a94cb14.jpg

---

## Lecture: Lab-02\page_004\Lab-02_page_004\auto

# 3.2 Runtime error

Cause:

Runtime error occurs when your syntax is correct but the compiler (or interpreter in case of Python), is still not able to run the code due to an error.

Common issues:

NameError: Undefined variablesm, e.g., print(a)   
TypeError: Operation applied to incorrect type of data, e.g., result $= 1 3 " + 3$ ValueError: When an operation receives a parameter of the correct type but an inappropriate value, e.g., number $= \operatorname { i n t } ( ^ { \prime } { \mathrm { a b c } } ^ { \prime } )$   
IndexError: When using indexes beyond the range of lists, tuples, strings, etc. E.g., $1 \mathrm { s t } = [ 1 , 2 , 3 ]$ print(lst[5])   
KeyError, ZeroDivisionError, AttributeError, etc.

Detection:

Error messages during program execution

Solution:

Analyzing the error message and using debugger

try: print(a)   
except Exception as e: print(f'NameError:{e}')   
try: result = '3' + 3   
except Exception as e: print(f'TypeError:{e}')   
try: \`number $=$ int('abc')   
except Exception as e: print(f'ValueError: {e}')   
try: lst = [1, 2, 3] print(lst [5])   
except Exception as e: print(f'IndexError:{e}')

### Images:
- data\Design and Analysis of Algorithms\Lab-02\page_004\Lab-02_page_004\auto\images\4bd59c47b6b03245d8b80f8341fb6287f78671a7f7a63cc3c42a03b5c99625d1.jpg

---

## Lecture: Lab-02\page_005\Lab-02_page_005\auto

# 3.3 Wrong answer/Logical error

Cause:

A logical error occurs when a program runs without producing any error messages but produces incorrect or unexpected output due to a flaw in the algorithm or logic. These errors are often the hardest to detect.

Common issues: s Off-by-one error:

nums = [1, 2 3 4 5]

# Wrong: loop ends too early for i in range(len(nums) 1): print(nums[i]) # Output: 12 3 4 (misses the last element)

# Correct for i in range(len(nums)): print(nums[i])

s Incorrect algorithm implementation:

Wrong: average formula is incorrect def average(a, b): return a + b / 2 # actually computes a + (b/2)

Correct

def average(a, b): return (a^+ b) / 2

Detection:

Test cases, edge cases, manual code review

Solution:

Debug step by step, use print statements, test with sample inputs

# 3.4 Time limit exceeded

Cause

Program takes too long to execute

Common issues:

---

## Lecture: Lab-02\page_006\Lab-02_page_006\auto

s infinite loops

# Wrong: Infinite loop (x never changes)   
X = 日   
while x < 5: print(x) # forgot to update x   
# Correct: Loop terminates properly   
X = 0   
while x < 5: print(x) ×+= ：1

• Detection:

Program timeout message

Solution:

Check for infinite loops, using debugger

# 4. Python Debugging

# 4.1 Installation

The following is a basic installation tutorial for Python extentions. On macOS and Windows systems, the operations are similar.

# 4.1.1 Install python extention locally

First, open VSCode and search for the Python extension. Install it, and it will automatically install both the Python and Python Debugger extensions. If your network is stable, the installation should complete within a few minutes.

![](images/6bea6b0c174e8f4bbe08d7a0aa22b8bf65fdcc0a7af315a75bcbf8de1e135aaf.jpg)

Similarly, search for and install the Pylance extension. This extension provides automatic code completion and syntax highlighting for your Python code, making it

### Images:
- data\Design and Analysis of Algorithms\Lab-02\page_006\Lab-02_page_006\auto\images\6bea6b0c174e8f4bbe08d7a0aa22b8bf65fdcc0a7af315a75bcbf8de1e135aaf.jpg

---

## Lecture: Lab-02\page_007\Lab-02_page_007\auto

# 4.1.2 Install Python extension remotely (Optional)

On the server, you can follow the same steps to install the Python extension. If the external network connection is unstable, you can download the Python extension in advance from the local machine and then install it on the server. See https://code.visualstudio.com/docs/editor/extension-marketplace#_can-i-download-an -extension-directly-from-the-marketplace.

# 4.2 Debug without parameters

First, create a Python file and assume that we have already written the following code.

![](images/b068883311bd0966ee170ad41c9b79178ac7ec572107a44e4ad205ab67fa6c54.jpg)

Next, set breakpoints at any position where you want to debug. Click to the left of the line number to make a red breakpoint appear.

![](images/c769f3d4d0b7a9c2daee2488c4149c4e9f4e9d6684bbebf5112ec2c2c8a38d34.jpg)

# Then, click the Run button and select Python Debugger: Debug Python File.

![](images/5012db044b93187f07cb9fef4a81511512b4355c5de64a24967696a0a75bb462.jpg)

Now you can check variables on the left toolbar.

### Images:
- data\Design and Analysis of Algorithms\Lab-02\page_007\Lab-02_page_007\auto\images\5012db044b93187f07cb9fef4a81511512b4355c5de64a24967696a0a75bb462.jpg
- data\Design and Analysis of Algorithms\Lab-02\page_007\Lab-02_page_007\auto\images\b068883311bd0966ee170ad41c9b79178ac7ec572107a44e4ad205ab67fa6c54.jpg
- data\Design and Analysis of Algorithms\Lab-02\page_007\Lab-02_page_007\auto\images\c769f3d4d0b7a9c2daee2488c4149c4e9f4e9d6684bbebf5112ec2c2c8a38d34.jpg

---

## Lecture: Lab-02\page_008\Lab-02_page_008\auto

![](images/5dc0a772bd2be438bc98efc7947429099c789116436b862a78461a6269218fed.jpg)

# (1) Continue: Continue to next breakpoint

Continue executing the program until the next breakpoint is encountered.

During program execution, the continue button will change to pause. Clicking it will stop at the current running line (for small programs, you may not see the button change to pause as it runs too fast).

(2) Step Over: Executes the current line of code but does not go inside functions. If the current line contains a function call, the function executes completely, and the debugger moves to the next line in the same scope.

If there is no breakpoint within the defined function, the function will be run directly without entering the function and running the code within it line by line.

Otherwise, if there is a breakpoint within the function (def block), the program will stop at the first breakpoint encountered within the custom function.

Use when you don’t want to debug inside a function but just see its result.

![](images/baff7fca5a271e8f51f895ca31742218d55a24eb9f816a87985feebf28b27035.jpg)

Step Over: Customed function with breakpoints vs without breakpoints

# (3) Step Into: Execute the current line and enter inside functions.

If the line contains a function, the debugger will jump inside that function regardless of whether there is a breakpoint inside the function. Therefore, you can debug it step by step.

Use when you want to debug inside a function.

### Images:
- data\Design and Analysis of Algorithms\Lab-02\page_008\Lab-02_page_008\auto\images\5dc0a772bd2be438bc98efc7947429099c789116436b862a78461a6269218fed.jpg
- data\Design and Analysis of Algorithms\Lab-02\page_008\Lab-02_page_008\auto\images\baff7fca5a271e8f51f895ca31742218d55a24eb9f816a87985feebf28b27035.jpg

---

## Lecture: Lab-02\page_009\Lab-02_page_009\auto

![](images/6409142c7e0fb98a2b865669be0106ed8a7bf92a6651e8d3cbecdf41584c8fa6.jpg)

(4) Step Out: Exits the current function and returns to where it was called Useful when you accidentally Step Into a function and want to return to the main code quickly.

(5) Restart & Stop: restart your debug & stop your debug.

# 4.3 Debug with parameters

When debugging a Python script with arguments, we cannot directly run the debugger. First, we need to add some code to enable the Python program to accept arguments.

import argparse   
def add_numbers(a, b): result $= a + b$ return result   
parser $=$ argparse.ArgumentParser()   
parser.add_argument $[ - x ^ { \prime }$ , type=int, help $\bullet ^ { \prime }$ First number')   
parser.add_argument('--y', type=int, help $| = "$ 'Second number')   
args $=$ parser.parse_args()   
$\mathsf { x } =$ args.x   
$\curlyvee =$ args.y   
sum_result $=$ add_numbers(x, y)   
print(sum_result)

Then, we click on the debug icon and select create a launch.json file from the toolbar.

### Images:
- data\Design and Analysis of Algorithms\Lab-02\page_009\Lab-02_page_009\auto\images\6409142c7e0fb98a2b865669be0106ed8a7bf92a6651e8d3cbecdf41584c8fa6.jpg

---

## Lecture: Lab-02\page_010\Lab-02_page_010\auto

![](images/7ce98d8ac578fd15c3b505e28327012451b8e3fa6508686f2f10f1268d585970.jpg)

Next, we choose Python Debugger $_ - >$ Python File with Arguments (Debug the currently active Python file with arguments). VSCode will automatically generate a launch.json file based on our selection.

![](images/8698cdf371b2078211515fe9b28ba570a5bbfc041a3e89cfeaa6bd033d19ce4d.jpg)

The next step is to modify the args parameter as shown in the image. Once the modification is complete, we return to the Python file that needs debugging and click Python Debugger: Debug using launch.json (Remember to create breakpoints).

![](images/cda52e32629bb1ea7b9eb58d4f806dc8e07572820ae6076e916098a06df24d37.jpg)

### Images:
- data\Design and Analysis of Algorithms\Lab-02\page_010\Lab-02_page_010\auto\images\7ce98d8ac578fd15c3b505e28327012451b8e3fa6508686f2f10f1268d585970.jpg
- data\Design and Analysis of Algorithms\Lab-02\page_010\Lab-02_page_010\auto\images\8698cdf371b2078211515fe9b28ba570a5bbfc041a3e89cfeaa6bd033d19ce4d.jpg
- data\Design and Analysis of Algorithms\Lab-02\page_010\Lab-02_page_010\auto\images\cda52e32629bb1ea7b9eb58d4f806dc8e07572820ae6076e916098a06df24d37.jpg

---

## Lecture: Lab-02\page_011\Lab-02_page_011\auto

![](images/a6a2df123d7648ee6b3da91ac0f5c067db47828ca9f157e8536c081f1825f9b9.jpg)

Now we can debug all types of python scripts.

### Images:
- data\Design and Analysis of Algorithms\Lab-02\page_011\Lab-02_page_011\auto\images\a6a2df123d7648ee6b3da91ac0f5c067db47828ca9f157e8536c081f1825f9b9.jpg

---

## Lecture: Lab-04\page_001\Lab-04_page_001\auto

# Lab Exercises 4

# Outline

• Problem 1. In-place Implementation of Quicksort • Problem 2. Two Sum Problem: Application of Sorting • Problem 3. Merge Sort & Quick sort Practice

# Problem 1. In-place Implementation of Quicksort

Quicksort is one of the most efficient sorting algorithms with an average time complexity of $O ( n \log n )$ . Let’s review the in-place implementation of quicksort.

The key idea behind quicksort is the ”divide and conquer” approach:

• Choose a pivot: Select an element from the array (usually the rightmost element).   
• Partition: Rearrange the array so that elements smaller than the pivot come before it, and elements greater than the pivot come after it. After this step, the pivot is in its final sorted position.   
• Recursively sort: Apply the same process to the sub-arrays on the left and right of the pivot.

”In-place” means we sort the array without using additional arrays for storage. We only use a constant amount of extra space regardless of the input size.

The key to in-place implementation is the partition step. Here’s how it works:

1. Choose the rightmost element as the pivot.

2. Start with two pointers: one just before the beginning of the array (let’s call it $\imath$ ) and another that scans through the array (let’s call it $j$ ).

3. For each element that $j$ points to:

• If the element is less than or equal to the pivot, increment $i$ and swap the elements at positions $i$ and $j$ .   
• If the element is greater than the pivot, just move $j$ forward.   
4. After completing the scan, swap the pivot (which is at the end) with the element at position $i + 1$ .   
5. Now the pivot is in its correct sorted position, with smaller elements to its left and larger elements to its right.

---

## Lecture: Lab-04\page_002\Lab-04_page_002\auto

# Time Complexity:

• Best and Average cases: $O ( n \log n )$   
• Worst case: $O ( n ^ { 2 } )$ (occurs when the array is already sorted or nearly sorted and we always pick the smallest/largest element as pivot)

# Tips for Optimization

1. Random pivot selection: Instead of always choosing the rightmost element, select a random element as the pivot to avoid worst-case scenarios.

2. Median-of-three: Choose the median of the first, middle, and last elements as the pivot.

3. Insertion sort for small arrays: For small subarrays (e.g., less than 10 elements), use insertion sort instead of continuing with quicksort.

4. Tail recursion elimination: Optimize the recursion by only making one recursive call instead of two.

Problem 2. Given an unsorted array $A$ of integers and a target value $\boldsymbol { v }$ , design an algorithm to determine whether $A$ contains two different integers $x$ and $y$ such that $x + y = v$ . The algorithm must run in $O ( n \log n )$ time.

Solution. To solve this problem efficiently,we’ll first sort the array and then use a two-pointer approach or binary search. Since we’re dealing with an unsorted array, we need to begin by sorting it, which takes $O ( n \log n )$ time.

Firstly, Sort the array $A$ in non-decreasing order, which takes $O ( n \log n )$ time.

Then, we can solve this problem by binary search. For each element $x$ in the array, we search for $v - x$ using binary search. The algorithm proceeds as follows:

1. Iterate through each element $x$ in the array $A$ (indexed as $A [ i ]$ ).   
2. Compute the target value $t = v - x$ .   
3. Use binary search to check whether $t$ exists in $A$ , ensuring that the index of $t$ is different   
from the index of $x$ (i.e., avoid using the same element twice).   
4. If $t$ is found, return true.   
5. If the iteration completes without finding such a pair, return false.

The pseudocode for the solution is as follows:

def two_sum (A , v ): for i in range (len( A )): x = A [ i ] t = v - x if binary_search (A , t , exclude_inde $\mathbf { x } = \dot { \mathbf { \hat { \mathbf { \mathbf { \mathbf { \mathbf { \mathbf { \varepsilon } } } } } } } }$ ) : return True return False

def binary_search (A , target , exclude_index ): low , high $\qquad = \quad 0$ , l e n ( A ) - 1 while low $< =$ high : mid $=$ ( low $^ +$ high ) // 2

---

## Lecture: Lab-04\page_003\Lab-04_page_003\auto

if A [ mid ] $= =$ target and mid ! $=$ exclude_index : return True elif A [ mid ] $<$ target : low $=$ mid + 1 else : high $=$ m i d - 1 return False

Additionally, we can also solve this problem by a two-pointer approach:

• Initialize two pointers: lef t pointing to the beginning of the sorted array and right pointing to the end.

• While $l e f t < r i g h t$ :

– If $A [ l e f t ] + A [ r i g h t ] = v$ , return true.   
– $[ \mathrm { f } ~ A [ l e f t ] + A [ r i g h t ] < v$ , increment lef t.   
– If $A [ l e f t ] + A [ r i g h t ] > v$ , decrement right.

• If the loop completes without finding such a pair, return false.

The pseudocode for the solution is as follows:

def two_sum (A , v ):

# Sort the array in O(n log n) time   
A . sort ()   
# Use two pointers   
left , right $\qquad = \quad 0$ , len( A ) - 1   
while left < right : current_sum $=$ A [ left ] + A [ right ] if current_sum $\begin{array} { r l r } { \mathbf { \Psi } } & { { } = } & { \mathbf { \Psi } } \\ { \mathbf { \Psi } } & { { } = } & { \mathbf { \Psi } } \\ { \mathbf { \Psi } } & { { } = } & { \mathbf { \Psi } } \\ { \mathbf { \Psi } } & { { } } & { \mathsf { V } } \end{array}$ : return True elif current_sum < v : left $\qquad + \qquad 1$ else : right -= 1   
return False

Problem 3(Finding the Kth Smallest Element). Given an unsorted array of $n$ distinct integers, design an algorithm to find the $k$ th smallest element in the array. Your solution should have an expected running time of $O ( n \log n )$ .

Solution. To find the $k$ th smallest element in an unsorted array, we can apply one of the efficient sorting algorithms , such as Quick Sort or Merge Sort, followed by direct access to the $k$ th element. This approach achieves the required $O ( n \log n )$ time complexity.

1. Sort the array using merge sort, which has a time complexity of $O ( n \log n )$ .

2. After sorting, the $k$ th smallest element will be at index $k - 1$ (assuming 0-based indexing).

3. Return the element at index $k - 1$ .

---

## Lecture: Lab-04\page_004\Lab-04_page_004\auto

The pseudocode for the solution of Quick Sort is as follows:

Quick Sort is an efficient, comparison-based sorting algorithm that follows the divide-andconquer paradigm. It works by selecting a ’pivot’ element and partitioning the array around this pivot.

def find_kth_smallest_quick_sort (A , k ):

# Apply Quick Sort quick_sort (A , 0 , len( A ) - 1)

# Return the k-th smallest element (0 - indexed array ) return A [k -1]

def quick_sort (A , low , high ): if low < high : # Partition the array and get the pivot index pivot_index $=$ partition (A , low , high ) # Recursively sort the subarrays quick_sort (A , low , pivot_index - 1) quick_sort (A , pivot_index $^ +$ 1 , high )

def partition (A , low , high ): # Choose the rightmost element as pivot piv $\mathrm { ~ \mathsf ~ { ~ o ~ t ~ } ~ } = \mathrm { ~ \mathsf ~ { ~ A ~ } ~ }$ [ high ] i = low - 1

$$
\begin{array} { r c l } { { \mathrm { i n } } } & { { \mathrm { r a n g e ( 1 o w , ~ h i g h ) : } } } & { { } } \\ { { \mathrm { } \varepsilon } } & { { \mathsf { A } \left[ \mathsf { j } \right] \quad < = \begin{array} { r c l } { { \mathsf { p i v o t : } } } & { { } } & { } \\ { { } } & { { } } & { { } } \end{array} } } \\ { { \dot { \mathrm { ~  ~ \rho ~ } } } } & { { \mathsf { i } \quad + = \begin{array} { r c l } { { \mathsf { 1 } } } & { { } } & { { } } \\ { { } } & { { } } & { { \mathsf { A } \left[ \mathsf { j } \right] } } \end{array} = \begin{array} { r c l } { { \mathsf { A } \left[ \mathsf { j } \right] , } } & { { \mathsf { A } \left[ \mathsf { i } \right] } } & { { } } \\ { { \mathsf { A } \left[ \mathsf { j } \right] \mathsf { ~ , } } } & { { \mathsf { A } \left[ \mathsf { i } \right] } } & { { } } \end{array} } } \end{array}
$$

$\mathrm { ~ \textsf ~ { ~ A ~ } ~ } [ \mathrm { ~ i ~ \textsf ~ { ~ + ~ } ~ } \mathrm { ~ } 1 ]$ , A [ high ] $=$ A [ high ] , A [ i + 1] return i + 1

The pseudocode for the solution of Merge Sort is as follows:

def find_kth_smallest_merge_sort (A , k ): # Check if k is valid if k $\qquad < 0$ or k > len( A ): raise ValueError ( " k ␣ must ␣ be ␣ between ␣ 1 ␣ and ␣ the ␣ length ␣ of ␣ the ␣ array " )

# Apply Merge Sort merge_sort (A , 0 , len( A ) - 1)

# Return the k-th smallest element (0 - indexed array ) return A [k -1]

def merge_sort (A , left , right ):

if left < right :

### Images:
- data\Design and Analysis of Algorithms\Lab-04\page_004\Lab-04_page_004\auto\images\6b6dcb1e94c089ce1e81bde33771c9b7a570a55ef75e6cae137e7d50001b09c8.jpg

---

## Lecture: Lab-04\page_005\Lab-04_page_005\auto

# Find the middle point mid $=$ ( left $^ +$ right ) // 2 # Sort first and second halves merge_sort (A , left , mid ) merge_sort (A , mid $^ +$ 1 , right )

# Merge the sorted halves merge (A , left , mid , right )

def merge (A , left , mid , right ):

# Create temporary arrays $\begin{array} { r l } { \mathrm { ~ L ~ } } & { { } = } \end{array}$ A [ left : mid + 1] R = A [ mid $^ +$ 1: right $^ +$ 1]

# Initial indices   
$\mathrm { ~ \bf ~ i ~ } = \mathrm { ~ \bf ~ j ~ } = 0$   
$\begin{array} { r c l } { \mathbf { k } } & { = } & { \mathbf { 1 } \mathtt { e } \mathbf { f } \mathtt { t } } \end{array}$

# Merge the temporary arrays back into A[ left .. right ] while i < len( L ) and j < len( R ):

if L [ i ] $< = \texttt { R } [ \mathrm { ~ j ~ } ]$ : $\begin{array} { r l r } { { \sf A } \left[ { \bf k } \right] } & { { } = } & { { \sf L } \left[ { \bf i } \right] } \end{array}$ i + = 1   
else :   
$\begin{array} { r c l } { { \texttt { A } [ \texttt { k } ] } } & { { = } } & { { \texttt { R } [ \texttt { j } ] } } \\ { { \texttt { j } _ { + = } } } & { { 1 } } & { { } } \\ { { \texttt { k } _ { + = } } } & { { 1 } } & { { } } \end{array}$

# Copy the remaining elements of L[] , if any while i < len( L ):

A [ k ] = L [ i ] $\begin{array} { r c l } { \dot { \mathrm { ~  ~ i ~ } } } & { + = } & { 1 } \\ { \ k _ { \mathrm { ~ \scriptsize ~ k ~ } } } & { + = } & { 1 } \end{array}$

# Copy the remaining elements of R[] , if any while j < len( R ):

$\begin{array} { r l r } { { \tt A } \left[ { \bf k } \right] } & { { } = } & { { \tt R } \left[ { \bf j } \right] } \end{array}$   
j + = 1   
k + = 1

# Time Complexity Analysis:

• Both Quick Sort and Merge Sort have an average time complexity of $O ( n \log n )$ . • Quick Sort has a worst-case time complexity of $O ( n ^ { 2 } )$ (though this is rare with good pivot selection strategies), while Merge Sort consistently runs in $O ( n \log n )$ time. • Accessing the element at index $k - 1$ after sorting takes $O ( 1 )$ time. • Therefore, the overall expected time complexity is $O ( n \log n )$ , which meets the requirement.

# Example:

### Images:
- data\Design and Analysis of Algorithms\Lab-04\page_005\Lab-04_page_005\auto\images\29c0389afcd013bf7a40c4e154a1f12ac8d2e1ca3e7eaa3ba31bd2934f1d72e4.jpg
- data\Design and Analysis of Algorithms\Lab-04\page_005\Lab-04_page_005\auto\images\982e1ec2db932460400e4d36c42aca0c6446b20264c26b64fb69de3e6b643d01.jpg

---

## Lecture: Lab-04\page_006\Lab-04_page_006\auto

Let’s work through an example to illustrate the algorithm:

• Array $A = [ 7 , 1 0 , 4 , 3 , 2 0 , 1 5 ]$ ] • Find the 3rd smallest element ( $k = 3$ )

1. Apply merge sort to $A$ :

• Divide: Split $A$ into [7, 10, 4] and [3, 20, 15]   
• Recursively sort each half: – [7, 10, 4] becomes [4, 7, 10] – [3, 20, 15] becomes [3, 15, 20]   
• Merge: Combine the sorted halves to get [3, 4, 7, 10, 15, 20]

2. The 3rd smallest element is at index 2, which is 7.

3. Return 7.

---

## Lecture: Lab3_DSAA2043_\page_001\DSAA2043_Lab3_page_001\auto

# Lab Exercises 3

# OUTLINE

• Example: Arranging functions in ascending order of growth rate   
• Theorem 1: For every $b > 1$ and every $x > 0$ , $\log _ { b } n = O ( n ^ { x } )$   
• Theorem 2: For every $r > 1$ and every $d > 0$ , $n ^ { d } = O ( r ^ { n } )$   
• Problem 1 (10 points): Classify functions using Big-O, Omega, and Theta notation   
• Problem 2 (10 points): Arrange functions in ascending order of growth rate   
• Problem 3 (10 points): True or False questions about Big-O notation   
• Problem 4 (10 points): Prove that $n ^ { 2 } = O ( 2 ^ { n } )$   
• Problem 5 Assignments on OJ platform

# IMPORTANT SUBMISSION INSTRUCTIONS:

• Problems 1-4: Submit on Canvas • Problem 5: Complete on the OJ platform • All submissions due by September 26th

Example. Take the following list of functions and arrange them in ascending order of growth rate. That is, if function $g ( n )$ immediately follows function $f ( n )$ in your list, then it should be the case that $f ( n )$ is $O ( g ( n ) )$ .

1. $f _ { 1 } ( n ) = 1 0 ^ { n }$   
2. f2(n) = n1/3   
3. $f _ { 3 } ( n ) = n ^ { n }$   
4. $f _ { 4 } ( n ) = \log _ { 2 } n$   
5. f5(n) = 2 log2 n

Theorem 1: For every $b > 1$ and every $x > 0$ , we have $\log _ { b } n = O ( n ^ { x } )$

$\textstyle \log _ { b } n = { \frac { \ln n } { \ln b } }$

$$
\log _ { b } n = { \frac { \ln n } { \ln b } }
$$

We know that for any $x > 0$ , the function $n ^ { x }$ grows faster than $\ln n$ as $n$ becomes large. Specifically, the limit:

$$
\operatorname* { l i m } _ { n \to \infty } { \frac { \ln n } { n ^ { x } } } = 0
$$

### Images:
- data\Design and Analysis of Algorithms\Lab3_DSAA2043_\page_001\DSAA2043_Lab3_page_001\auto\images\34b605132dad3e1e0e8655dcf8f329f849b6bd3dfc61505eff4faf963e22b753.jpg
- data\Design and Analysis of Algorithms\Lab3_DSAA2043_\page_001\DSAA2043_Lab3_page_001\auto\images\8b6281e51032030a9b08a4ff55c87eb2f1a69875eec6a61e4b414c2a6939a985.jpg

---

## Lecture: Lab3_DSAA2043_\page_002\DSAA2043_Lab3_page_002\auto

This means that for sufficiently large $n$ , $\ln n$ is dominated by $n ^ { x }$ .

Since $\begin{array} { r } { \operatorname* { l i m } _ { n  \infty } \frac { \ln n } { n ^ { x } } = 0 } \end{array}$ ln nnx = 0, there exists a constant C′ > 0 and an n0 such that for all n ≥ n0:

$$
{ \frac { \ln n } { n ^ { x } } } \leq C ^ { \prime }
$$

Multiplying both sides by $n ^ { x }$ and then by $\scriptstyle { \frac { 1 } { \ln b } }$ (which is positive since $b > 1$ ), we obtain:

$$
\log _ { b } n = { \frac { \ln n } { \ln b } } \leq { \frac { C ^ { \prime } \cdot n ^ { x } } { \ln b } }
$$

Let $\begin{array} { r } { C = \frac { C ^ { \prime } } { \ln b } } \end{array}$ C′ln b . Then:

$$
\log _ { b } n \leq C \cdot n ^ { x }
$$

We have shown that there exist constants $C > 0$ and $n _ { 0 }$ such that for all $n \geq n _ { 0 }$ , $\log _ { b } n \leq$ $C \cdot n ^ { x }$ . Therefore, $\log _ { b } n = O ( n ^ { x } )$ .

Theorem 2: For every $r > 1$ and every $d > 0$ , we have $n ^ { d } = O ( r ^ { n } )$ .

Proof: For $r > 1$ and $d > 0$ , the exponential function $r ^ { n }$ grows faster than the polynomial function $n ^ { d }$ as $n$ becomes large. Specifically, the limit:

$$
\operatorname* { l i m } _ { n \to \infty } \frac { n ^ { d } } { r ^ { n } } = 0
$$

This means that for sufficiently large $n$ , $n ^ { d }$ is dominated by $r ^ { n }$ .

Since $\begin{array} { r } { \operatorname* { l i m } _ { n  \infty } \frac { n ^ { d } } { r ^ { n } } = 0 } \end{array}$ , there exists a constant $C > 0$ and an $n _ { 0 }$ such that for all $n \geq n _ { 0 }$

$$
{ \frac { n ^ { d } } { r ^ { n } } } \leq C
$$

Multiplying both sides by $r ^ { n }$ , we obtain:

$$
n ^ { d } \leq C \cdot r ^ { n }
$$

We have shown that there exist constants $C > 0$ and $n _ { 0 }$ such that for all $n \geq n _ { 0 }$ , $n ^ { d } \leq C \cdot r ^ { n }$ Therefore, $n ^ { d } = O ( r ^ { n } )$ .

Solution: We can deal with functions $f _ { 2 }$ , and $f _ { 4 }$ very easily, since they belong to the basic families of polynomials and logarithms. In particular, by Theorem 1, we have $f _ { 4 } ( n ) = O ( f _ { 2 } ( n ) )$ . By Theorem 2, polynomial functions like $n ^ { 1 / 3 }$ are $O$ (exponential functions) like $1 0 ^ { n }$ , so $f _ { 2 } ( n ) =$ $O ( f _ { 1 } ( n ) )$ .

For and , we need to compare their growth rates. For large , grows faster than 10n. This can be seen by taking the ratio: nn10n = ( n10 )n. As n grows larger than 10, this ratio increases without bound, showing that $f _ { 1 } ( n ) = O ( f _ { 3 } ( n ) )$ .

Finally, we come to function $f _ { 5 }$ , which is admittedly kind of strange-looking. A useful rule of thumb in such situations is to try taking logarithms to see whether this makes things clearer. In this case, $\log _ { 2 } f _ { 5 } ( n ) = { \sqrt { \log _ { 2 } n } } = ( \log _ { 2 } n ) ^ { 1 / 2 }$ . $\log _ { 2 } f _ { 4 } ( n ) = \log _ { 2 } ( \log _ { 2 } n )$ , while $\log _ { 2 } f _ { 2 } ( n ) \ = \ { \frac { 1 } { 3 } } \log _ { 2 } n$ . All of these can be viewed as functions of $\log _ { 2 } n$ , and so using the notation $z = \log _ { 2 } n$ , we can write

$$
\begin{array} { l } { \displaystyle \log _ { 2 } f _ { 2 } ( n ) = \frac { 1 } { 3 } z } \\ { \displaystyle \log _ { 2 } f _ { 4 } ( n ) = \log _ { 2 } z } \\ { \displaystyle \log _ { 2 } f _ { 5 } ( n ) = z ^ { 1 / 2 } } \end{array}
$$

### Images:
- data\Design and Analysis of Algorithms\Lab3_DSAA2043_\page_002\DSAA2043_Lab3_page_002\auto\images\25d5096a554b76ac41453b7c99617a45a4c888b8f29188ee495445a5376f616e.jpg
- data\Design and Analysis of Algorithms\Lab3_DSAA2043_\page_002\DSAA2043_Lab3_page_002\auto\images\28aace831262f0252e8458862fdfb26e8f1ccff27c99aa298c0c1477e948e6cc.jpg
- data\Design and Analysis of Algorithms\Lab3_DSAA2043_\page_002\DSAA2043_Lab3_page_002\auto\images\3e7d876164872ce93c77a2ea791704c98544c483bee1df9a353ac53de9d10fa2.jpg
- data\Design and Analysis of Algorithms\Lab3_DSAA2043_\page_002\DSAA2043_Lab3_page_002\auto\images\7147cba0008bc51b614cfb7e97f97b4ac67f3b9d40ac3167f94aab7b970ac897.jpg
- data\Design and Analysis of Algorithms\Lab3_DSAA2043_\page_002\DSAA2043_Lab3_page_002\auto\images\7a103c4685bbb41b5440e13e407dc16b31d593e912a277156e2a9b5d0db947d8.jpg
- data\Design and Analysis of Algorithms\Lab3_DSAA2043_\page_002\DSAA2043_Lab3_page_002\auto\images\85eded4e9d0a8ce649f4c4fb9337d70d3576b52aad6806cfa6cc7918ac42a77c.jpg
- data\Design and Analysis of Algorithms\Lab3_DSAA2043_\page_002\DSAA2043_Lab3_page_002\auto\images\fb18c1e00548f422743785180604adf3f37282815421d5d9158dad7b38d756e0.jpg

---

## Lecture: Lab3_DSAA2043_\page_003\DSAA2043_Lab3_page_003\auto

Now it’s easier to see what’s going on. First, for $z \geq 1 6$ , we have $\log _ { 2 } z \le z ^ { 1 / 2 }$ . But the condition $z \geq 1 6$ is the same as $n \geq 2 ^ { 1 6 } = 6 5 5 3 6$ ; thus once $n \geq 2 ^ { 1 6 }$ we have $\log _ { 2 } f _ { 4 } ( n ) \ \leq$ $\log _ { 2 } f _ { 5 } ( n )$ , and so $f _ { 4 } ( n ) \leq f _ { 5 } ( n )$ . Thus we can write $f _ { 4 } ( n ) = O ( f _ { 5 } ( n ) )$ .

Similarly we have $z ^ { 1 / 2 } \leq \frac { 1 } { 3 } z$ once $z \geq 9$ (once $n \geq 2 ^ { 9 } = 5 1 2$ ). For $n$ above this bound we have $\log _ { 2 } f _ { 5 } ( n ) \leq \log _ { 2 } f _ { 2 } ( n )$ and hence $f _ { 5 } ( n ) \leq f _ { 2 } ( n )$ , and so we can write $f _ { 5 } ( n ) = O ( f _ { 2 } ( n ) )$ . Essentially, we have discovered that $2 { \sqrt { \log _ { 2 } n } }$ is a function whose growth rate lies somewhere between that of logarithms and polynomials.

The final list: $f _ { 4 } \leq f _ { 5 } \leq f _ { 2 } \leq f _ { 1 } \leq f _ { 3 }$

Problem 1 (10 points). For each row $i$ in Table 1, determine whether $A _ { i }$ belongs to $O ( B _ { i } )$ , $\Omega ( B _ { i } )$ , or $\Theta ( B _ { i } )$ . Place a checkmark ( $\checkmark$ ) in the appropriate column(s). The first two rows are provided as examples. No explanation is required.

Table 1: Big-O, Omega, and Theta Classification   

<table><tr><td>A</td><td>B</td><td>0</td><td>Ω</td><td>Θ</td></tr><tr><td>5n</td><td>n</td><td>√</td><td>√</td><td>√</td></tr><tr><td>5</td><td>n</td><td>√</td><td></td><td></td></tr><tr><td>n3</td><td>$n2</td><td></td><td></td><td></td></tr><tr><td>log n2</td><td>n</td><td></td><td></td><td></td></tr><tr><td>3n</td><td>2n</td><td></td><td></td><td></td></tr><tr><td>log(n!) √</td><td>n log n</td><td></td><td></td><td></td></tr><tr><td>(2)n</td><td>n0.5</td><td></td><td></td><td></td></tr><tr><td></td><td>1</td><td></td><td></td><td></td></tr><tr><td>n1.5</td><td>n(10g n)2</td><td></td><td></td><td></td></tr><tr><td>log2n</td><td>lnn</td><td></td><td></td><td></td></tr><tr><td>4n</td><td>22n</td><td></td><td></td><td></td></tr><tr><td>n</td><td>l0g(nn)</td><td></td><td></td><td></td></tr><tr><td>100n + 50</td><td>n</td><td></td><td></td><td></td></tr></table>

Problem 2 (10 points). Consider the following list of functions. Arrange them in ascending order of growth rate. If function $g ( n )$ immediately follows function $f ( n )$ in your list, then it should be the case that $f ( n ) = O ( g ( n ) )$ .

1. f1(n) = n2.5   
2. $f _ { 2 } ( n ) = { \sqrt { 2 ^ { n } } }$   
3. $f _ { 3 } ( n ) = n + 1 0$   
4. $f _ { 4 } ( n ) = 1 0 n$   
5. $f _ { 5 } ( n ) = 1 0 0 n$   
6. $f _ { 6 } ( n ) = n ^ { 2 } \log n$

# Requirements:

• Provide your final ordered list   
• For each consecutive pair $( f _ { i } , f _ { j } )$ , briefly justify why $f _ { i } = O ( f _ { j } )$   
• Consider asymptotic behavior as $n \to \infty$

Problem 3 (10 points). True or False? No explanation is required.

### Images:
- data\Design and Analysis of Algorithms\Lab3_DSAA2043_\page_003\DSAA2043_Lab3_page_003\auto\images\8e6c0298aae9ae06181eac6bcfe953d914fa6edc5e73058a4232a18c1bc8144f.jpg

---

## Lecture: Lab3_DSAA2043_\page_004\DSAA2043_Lab3_page_004\auto

1. Is $2 ^ { n + 1 } = O ( 2 ^ { n } )$   
2. Is $2 ^ { 2 n } = O ( 2 ^ { n } )$

Problem 4 (10 points). Prove that $n ^ { 2 } = O ( 2 ^ { n } )$ Problem 5. Complete the following assignments on the OJ platform before September 26th:

• DSAA2043 - Lab03: Lab-week3-exercise 02   
• DSAA2043 - Lab03: Lab-week3-exercise 03

---

## Lecture: Paper Exercises\DSAA2043_paper_exercise2\page_003\DSAA2043_paper_exercise2_page_003\auto

Problem 2. Let $S _ { 1 }$ be a set of $n$ integers, and $S _ { 2 }$ another set of $n$ integers. Each of $S _ { 1 }$ and $S _ { 2 }$ is stored in an array of length $n$ . The arrays are not necessarily sorted. Design an algorithm to determine whether $S _ { 1 } \cap S _ { 2 }$ is empty. Your algorithm must terminate in $O ( n \log n )$ time.

Answer 2. We solve this problem by combining the two input sets and sorting them as described in Problem 2. The steps are as follows:

1. Combine the arrays: Construct a new array $A$ of size $2 n$ , by combining $S _ { 1 }$ and $S _ { 2 }$ . Each element is represented as a pair $( v , t )$ , where:

• $v$ is the integer value.   
• $t$ is the source identifier: $t = 1$ if the element comes from $S _ { 1 }$ , and $t = 2$ if it comes from $S _ { 2 }$ .

2. Sort the combined array: Sort $A$ using the algorithm from Problem 2. The comparison of two elements $e _ { 1 } = ( v _ { 1 } , t _ { 1 } )$ and $e _ { 2 } = ( v _ { 2 } , t _ { 2 } )$ is defined as:

• If $v _ { 1 } < v _ { 2 }$ , then $e _ { 1 } < e _ { 2 }$ .   
• If $v _ { 1 } > v _ { 2 }$ , then $e _ { 1 } > e _ { 2 }$ .   
• If $v _ { 1 } = v _ { 2 }$ , then compare their source identifiers: – If t1 < t2, then $e _ { 1 } < e _ { 2 }$ . – Otherwise, e1 > e2.

Sorting $A$ takes $O ( n \log n )$ time.

3. Scan the sorted array: Traverse the sorted array $A$ , and for each consecutive pair of elements $e _ { 1 } = ( v _ { 1 } , t _ { 1 } )$ and $e _ { 2 } = ( v _ { 2 } , t _ { 2 } )$ :

• If $v _ { 1 } = v _ { 2 }$ and $t _ { 1 } \neq t _ { 2 }$ , then $S _ { 1 } \cap S _ { 2 } \neq \emptyset$ . Return true.   
• Otherwise, continue scanning.

Scanning $A$ takes $O ( n )$ time.

If no matching pair $( v _ { 1 } , t _ { 1 } )$ and $( v _ { 2 } , t _ { 2 } )$ is found, return false.

# Complexity Analysis:

• Constructing $A$ takes $O ( n )$ time.   
• Sorting $A$ takes $O ( n \log n )$ time.   
• Scanning $A$ takes $O ( n )$ time.

Thus, the total time complexity is $O ( n \log n )$ , as required.

Problem 3. Given an array A =< 46, 74, 53, 14, 26, 38, 86, 65, 27, 34 >, use the quicksort method with the first element as the pivot. Illustrate the step-by-step execution and the final result. The execution result of the first partition is given as follows:

---

## Lecture: Paper Exercises\DSAA2043_paper_exercise3\page_002\DSAA2043_paper_exercise3_page_002\auto

Problem 2. Suppose that an intermixed sequence of push and pop operations are performed. The pushes push the integers 0 through 9 in order; the pops print out the return value. Which of the following sequences could not occur?

(a) 4 3 2 1 0 9 8 7 6 5   
(b) 4 6 8 7 5 3 2 9 0 1   
(c) 2 5 6 7 4 8 9 3 1 0   
(d) 4 3 2 1 0 5 6 7 8 9

---

## Lecture: Paper Exercises\DSAA2043_paper_exercise3\page_004\DSAA2043_paper_exercise3_page_004\auto

Problem 4. A palindrome is a word, phrase, or number that is spelled the same forward and backward. For example, “dad” is a palindrome; “A man, a plan, a canal: Panama” is a palindrome if you take out the spaces and ignore the punctuation; and 1,001 is a numeric palindrome. We can use a Stack to determine whether or not a given string is a palindrome.

Answer the following questions:

Q4.1. Provide pseudocode or Python code for an algorithm that takes a string of letters and returns True or False to determine whether it is palindromic.

Q4.2. Analyze the time and space complexity of your algorithm.

---

## Lecture: Paper Exercises\DSAA2043_paper_exercise3\page_005\DSAA2043_paper_exercise3_page_005\auto

Problem 5. Given a string s representing an expression containing various types of brackets: $\{ \}$ , ( ), and [ ], provide pseudocode or Python code that reads in a string $s$ , and determines whether the brackets in the expression are balanced or not. A balanced expression is one where every opening bracket has a corresponding closing bracket in the correct order.

---

