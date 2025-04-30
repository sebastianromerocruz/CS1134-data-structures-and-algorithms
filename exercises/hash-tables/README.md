# Hash Tables: Practice Questions

## Question 1: Hashing and Compression

Insert the following keys into **three different hash tables**:

```plaintext
12, 56, 22, 106, 36, 72, 902, 86, 96, 62, 42
```

All collisions should be resolved by **chaining**. Each table differs by size and compression method.

### a) Division method, table size `N = 10` (non-prime)

Compression function:

```python
h2(k) = k % 10
```

Draw the resulting hash table after inserting the keys.

---

### b) Division method, table size `N = 13` (prime)

Compression function:

```python
h2(k) = k % 13
```

Draw the resulting hash table after inserting the keys.

---

### c) MAD method, table size `N = 10` (non-prime)

Compression function:

```python
h2(k) = ((125 * k + 342) % 1009) % 10
```

Constants:
- `p = 1009`
- `a = 125`
- `b = 342`

---

**Note**:

1. Assume the keys are used directly (i.e., `h1(k) = k`).
2. You do **not** need to perform rehashing.

---

## Question 2: Intersection of Two Lists

You are given the function signature:

```python
def intersection_list(lst1, lst2):
```

This function takes two lists of integers and returns a list of the elements that appear in **both** lists.

Example:

```python
intersection_list([3, 9, 2, 7, 1], [4, 1, 8, 2]) → [2, 1]
```

Assume no duplicates within a list.

### a) Write an implementation with the **best worst-case runtime**.

---

### b) Write an implementation with the **best average-case runtime**.

---

## Question 3: Space Optimization in `ChainingHashTableMap`

Modify the `ChainingHashTableMap` class from lecture to **optimize space** by:

- Representing empty buckets as `None`, rather than empty `UnsortedArrayMap` instances.
- When a bucket holds **only one item**, store the `Item` directly instead of using `UnsortedArrayMap`.
- Only use `UnsortedArrayMap` when a bucket contains **two or more** items.

Update the class implementation to support this optimization.

---

## Question 4: FIFO Iteration Order

Modify the `ChainingHashTableMap` so that its `__iter__` method yields keys in **FIFO order** — i.e., keys are returned in the order they were first inserted.

### Requirements

- Updating an existing key’s value **does not** affect its position in the iteration order.
- Support:
  - Search, insert, and delete in **Θ(1)** expected time (average case)
  - Iteration in **Θ(n)** worst-case time

---

## Question 5: Inverted File

An **inverted file** is a data structure used in search engines or book indexes.

Given a document (text file) `D`, viewed as a flat list of words:

```python
D = ['row', 'row', 'row', 'your', 'boat', 'gently', 'down', 'the', 'stream', ..., 'please', 'let', 'it', 'off', 'the', 'hook']
```

The inverted file maps each word to a list of the **indices** where it appears:

```python
{
    'row': [0, 1, 2, 18, 19, 20],
    'the': [7, 25, 37]
}
```

---

### Class Specification

```python
class InvertedFile:
    def __init__(self, file_name):
        '''Initializes an InvertedFile object from file_name'''

    def indices(self, word):
        '''Returns a list of indices where `word` appears'''
```

---

### Behavior Examples

```python
>>> inv_file = InvertedFile("row your boat.txt")
>>> inv_file.indices("row")
[0, 1, 2, 18, 19, 20]
>>> inv_file.indices("the")
[7, 25, 37]
>>> inv_file.indices("done")
[]
```

---

### Requirements

1. `__init__` must run in **Θ(n)** expected time (where `n` = total number of words).
2. `indices(word)` must run in **Θ(1)** expected time (average-case).
3. Casing and punctuation should be ignored:
   - `'Row'` = `'row'`
   - `'row,'` = `'row'`