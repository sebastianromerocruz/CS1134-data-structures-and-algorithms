<h2 align=center>Weeks 07 and 08</h2>

<h1 align=center>Sorting</h1>

<p align=center><strong><em>Song of the day</strong></em>: <em><a href="https://youtu.be/KrIsavBhgp8?si=lF59PqrJ-7EGw0ML"><strong>Nahuhulog Na Sa'yo (Live at The Cozy Cove)</a></strong> by Noah Alejandre (2024)</em></p>


### **Sections**

1. [**Introduction to Sorting**](#1)
2. [**Selection Sort**](#2)
3. [**Bubble Sort**](#3)
4. [**Insertion Sort**](#4)
5. [**Merge Sort**](#5)
6. [**Quick Sort**](#6)
7. [**Correctness & Loop Invariants**](#7)
8. [**Sorting Algorithm Summary**](#8)

---

## **The Sorting Problem**

Sorting is one of the most fundamental operations in computer science. It allows us to organize data in a meaningful order, making tasks like searching and comparison more efficient.

Sorting algorithms fall into two main categories:

- **Comparison-based Sorting** (Bubble Sort, Selection Sort, Merge Sort, Quick Sort)
- **Non-comparison-based Sorting** (not covered here, but includes algorithms like Radix Sort and Counting Sort)

We'll examine several sorting algorithms, focusing on their correctness, runtime complexity, and efficiency.

---


## **Selection Sort**

### **How It Works**

Selection Sort repeatedly selects the smallest element and swaps it with the first unsorted element. This process continues until the entire list is sorted.

### **Steps**

1. Find the smallest element in the unsorted portion.
2. Swap it with the first unsorted element.
3. Move the boundary of the sorted section one step forward.

### **Code**

```python
def selection_sort(lst):
    n = len(lst)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]  # Swap
```

### **Visualization**

TODO - 

### **Time Complexity**

- **T(n) = Σ(i=1 to n) i = (n(n-1))/2 = O(n²) = Θ(n²)**

- **T(n) = O(n²) = Θ(n²)**

- **Best Case:** O(n²)
- **Worst Case:** O(n²)
- **Average Case:** O(n²)

Selection Sort is inefficient for large datasets but works well for small lists.

---


## **3. Bubble Sort**

### **How It Works**

Bubble Sort repeatedly compares adjacent elements and swaps them if they are out of order. This process continues until the list is sorted.

### **Code**

```python
def bubble_sort(lst):
    n = len(lst)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True
        if swapped == False:
            return  # Stop if no swaps were made
```

### **Visualization**


### **Time Complexity**

- **T(n) = Σ(i=1 to n) i = (n(n-1))/2 = O(n²) = Θ(n²)**

- **T(n) = O(n²) = Θ(n²)**

- **Best Case:** O(n) (already sorted list)
- **Worst Case:** O(n²)
- **Average Case:** O(n²)

Bubble Sort is easy to understand but inefficient for large datasets.

---


## **4. Insertion Sort**

### **How It Works**

Insertion Sort builds the sorted list one element at a time by inserting each new element into its correct position.

### **Code**

```python
def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > key:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
```

### **Visualization**


### **Time Complexity**

- **T(n) = Σ(i=1 to n) i = (n(n-1))/2 = O(n²) = Θ(n²)**

- **T(n) = O(n²) = Θ(n²)**

- **Best Case:** O(n) (already sorted list)
- **Worst Case:** O(n²)
- **Average Case:** O(n²)

Insertion Sort is efficient for small datasets and nearly sorted lists.

---


## **5. Merge Sort**

### **How It Works**

Merge Sort is a **divide-and-conquer** algorithm that splits the list into smaller parts, sorts them recursively, and merges them back together in order.

### **Steps**
1. Divide the list into two halves.
2. Recursively sort each half.
3. Merge the sorted halves together.

### **Code**
```python
def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
```

### **Visualization**

TODO:
- Draw a tree-like diagram illustrating the recursive breakdown of the list.
- Label each split into sublists until they reach a base case.
- Show a merging step, where two sorted lists are combined.

### **Time Complexity**

- **T(n) = 2T(n/2) + O(n) = O(n log n) = Θ(n log n)**

- **Best Case:** O(n log n)
- **Worst Case:** O(n log n)
- **Average Case:** O(n log n)

Merge Sort is efficient but requires additional memory for merging.

---


## **6. Quick Sort**

### **How It Works**

Quick Sort follows a **divide-and-conquer** approach, selecting a pivot element and partitioning the list into smaller and larger elements.

### **Steps**
1. Choose a pivot element.
2. Partition the list into elements smaller and larger than the pivot.
3. Recursively sort both partitions.

### **Code**
```python
def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    pivot  = lst[len(lst) // 2]
    left   = [x for x in lst if x < pivot]
    middle = [x for x in lst if x == pivot]
    right  = [x for x in lst if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
```

### **Visualization**

TODO:
- Draw a partitioning diagram, showing how elements are divided based on the pivot.
- Highlight recursion, showing smaller partitions being sorted independently.
- Show the final concatenation into a single sorted list.

### **Time Complexity**

- **T(n) = T(k) + T(n-k-1) + O(n) = O(n log n) in average case, O(n²) in worst case**

- **Best Case:** O(n log n)
- **Worst Case:** O(n²) (if bad pivots are chosen)
- **Average Case:** O(n log n)

Quick Sort is often the fastest in practice.

---

## **7. Correctness & Loop Invariants**

### **What is a Loop Invariant?**
A **loop invariant** is a condition that is true **before and after every iteration** of a loop. It provides a structured way to prove that an algorithm works correctly.

### **Why Are Loop Invariants Important?**
When reasoning about an algorithm, we need to show that:
1. **Initialization** – The invariant is true **before the loop starts**.
2. **Maintenance** – If the invariant is true before an iteration, it **remains true** after the iteration.
3. **Termination** – When the loop ends, the invariant ensures the desired result has been achieved.

### **Example: Insertion Sort**
In **Insertion Sort**, the **loop invariant** is:
> "At the start of each iteration `i`, the first `i` elements of the list are sorted."

#### **Loop Invariant Proof for Insertion Sort**
1. **Initialization:** Before the loop starts, the first element `lst[0]` is trivially sorted.
2. **Maintenance:** At iteration `i`, the sublist `lst[:i]` is sorted. The algorithm inserts `lst[i]` into its correct position, ensuring that `lst[:i+1]` remains sorted.
3. **Termination:** When `i = n`, we have `lst[:n]`, meaning the entire list is sorted.

### **Code with Loop Invariant in Mind**
```python
def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > key:
            lst[j + 1] = lst[j]  # Shift elements right
            j -= 1
        lst[j + 1] = key  # Insert element in correct place
```

### **Visualization**


Loop invariants provide a structured way to prove correctness and help us build more reliable sorting algorithms.

---

This document follows your **Recursion** notes style. Let me know if you'd like any refinements!

