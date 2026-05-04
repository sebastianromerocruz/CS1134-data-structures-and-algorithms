<h2 align=center>Practice Questions</h2>

<h1 align=center>Abstract Data Types: <em>Hash Tables</em></h1>

**Note**: For all coding questions, you may only use data structures defined in this course—such as `ChainingHashTableMap`, `DoublyLinkedList`, `UnsortedArrayMap`, `ArrayQueue`, `ArrayStack`, etc. Do not use Python built-ins like `set`, `dict`, or `collections` in place of these.

---

## Question 1: Hashing and Compression

Insert the following keys into **three different hash tables**:

```plaintext
12, 56, 22, 106, 36, 72, 902, 86, 96, 62, 42
```

All collisions should be resolved by **chaining**. Each table differs by size and compression method.

**Note**:
1. Assume the keys are used directly (i.e., `h1(k) = k`).
2. You do **not** need to perform rehashing.

### a) Division method, table size `N = 10` (non-prime)

Compression function: `h2(k) = k % 10`. Draw the resulting hash table.

### b) Division method, table size `N = 13` (prime)

Compression function: `h2(k) = k % 13`. Draw the resulting hash table.

### c) MAD method, table size `N = 10` (non-prime)

Compression function:

```python
h2(k) = ((125 * k + 342) % 1009) % 10
```

where `p = 1009`, `a = 125`, `b = 342`. Draw the resulting hash table.

---

## Question 2: Intersection of Two Lists

Given the function signature:

```python
def intersection_list(lst1, lst2):
```

write a function that takes two lists of integers and returns a list of elements that appear in **both** lists. Assume no duplicates within either list.

For example:

```python
intersection_list([3, 9, 2, 7, 1], [4, 1, 8, 2]) → [2, 1]
```

### a) Write an implementation with the **best worst-case runtime**.

### b) Write an implementation with the **best average-case runtime**.

---

## Question 3: Space Optimization in `ChainingHashTableMap`

Modify the `ChainingHashTableMap` class from lecture to **optimize space** by:

- Representing empty buckets as `None`, rather than empty `UnsortedArrayMap` instances.
- When a bucket holds **only one item**, store the `Item` directly instead of using `UnsortedArrayMap`.
- Only using `UnsortedArrayMap` when a bucket contains **two or more** items.

---

## Question 4: FIFO Iteration Order

Modify `ChainingHashTableMap` so that `__iter__` yields keys in **FIFO order**—i.e., in the order they were first inserted.

To be clear:
- Updating an existing key's value does **not** affect its position in the iteration order.
- Search, insert, and delete must run in **Θ(1)** expected time (average case).
- Iteration must run in **Θ(n)** worst-case time.

---

## Question 5: Inverted File

An **inverted file** is a data structure used in search engines and book indexes. Given a document `D` viewed as a flat list of words:

```python
D = ['row', 'row', 'row', 'your', 'boat', 'gently', 'down', 'the', 'stream', ..., 'please', 'let', 'it', 'off', 'the', 'hook']
```

the inverted file maps each word to the list of **indices** where it appears:

```python
{'row': [0, 1, 2, 18, 19, 20], 'the': [7, 25, 37]}
```

Implement the following class:

| Operation | Explanation | Target Runtime |
|---|---|---|
| **`InvertedFile(file_name)`** | Initializes the structure from a text file | Θ(n) expected, where n = total words |
| **`inv.indices(word)`** | Returns a list of indices where `word` appears; `[]` if not found | Θ(1) expected (average case) |

For example:

```python
>>> inv_file = InvertedFile("row your boat.txt")
>>> inv_file.indices("row")
[0, 1, 2, 18, 19, 20]
>>> inv_file.indices("the")
[7, 25, 37]
>>> inv_file.indices("done")
[]
```

**Note**: Casing and punctuation should be ignored—`'Row'` = `'row'` and `'row,'` = `'row'`.
