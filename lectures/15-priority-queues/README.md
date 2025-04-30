<h2 align=center>Weeks 14 and 15</h2>

<h1 align=center>Abstract Data Types: <em>Priority Queues (Heaps)</em></h1>

<p align=center><strong><em>Song of the day</strong></em>: <em><a href="https://youtu.be/fexPzBFOhck?si=kJemvUQobStXynL-"><strong><u>before</u></strong></a> by slenderbodies (2024)</em></p>

---

## Sections

1. [**Motivation and Priority Queues**](#1)
2. [**Heap Fundamentals**](#2)
3. [**Heap Implementation**](#3)
	- [**Heap Items**](#3-1)
	- [**Insert and Upheap (`fix_up`)**](#3-2)
	- [**Delete and Downheap (`fix_down`)**](#3-3)
	- [**Initialising Our `ArrayMinHeap`**](#3-4)
4. [**Runtime Analysis and Comparisons**](#4)

<p align=center><strong><em><a href="assets/Priority Queues 2.pdf">Handwritten Class Notes</a></em></strong></p>

---

<a id="1"></a>

## Motivation and Priority Queues

Imagine a line at the airport. It’s not simply a first-come-first-serve scenario: passengers with different boarding classes and status levels can jump the line based on priority. In computing, the equivalent to this idea is the **priority queue**.

> A **priority queue** is an abstract data type where each element has a value and a priority. The item with the **highest** priority is served before others.

More specifically:

- **Insertions** are made freely.
- **Removals** always return the item with the **smallest** or **largest** priority, depending on whether it’s a min or max priority queue.

Why do we care?

- Priority queues are critical for task scheduling, pathfinding algorithms (like Dijkstra’s), and simulation systems.

We want an implementation that can insert elements quickly but also pull out the item with the highest priority *efficiently*.

<br>

<a id="2"></a>

## Heap Fundamentals

The most common implementation of a priority queue is a **binary heap**. It’s a binary tree that satisfies two conditions:

1. **Heap-order property**:

   - In a **min-heap**, each node is **less than or equal to** its children.
   - This ensures that the smallest element is always at the root.

2. **Complete binary tree**:

   - All levels are fully filled **except possibly the last**, which is filled **left to right**.
   - This means the height is **logarithmic** in the number of nodes: `h = Θ(log n)`.

Here's what a valid **min-heap** looks like:

```
        2
       / \
      4   3
     / \
    10  5
```

And here’s one that violates the heap rules:

```
        7
       / \
      3   9
```

The `3` is smaller than the root `7`, which breaks the heap property.

<br>

<a id="3"></a>

## Heap Implementation

While we can use nodes and pointers to build trees, heaps are almost always implemented using **arrays**. In other words, the following tree:

```
        2
       / \
      4   3
     / \
    10  5
```

Would correspond to the following array:

```Python
[2, 4, 3, 10, 5]
```

Why? Well, we know that since the tree is a priority queue, we know that it is a [**complete binary tree**](https://github.com/sebastianromerocruz/CS1134-data-structures-and-algorithms/tree/main/lectures/11-trees#binary-trees). Because of its uniform structure, this allows for some pretty nifty math. In particular, when represented by an array, any node at index `j`...

- Has a **left child** is at `2j`
	```Python
	def left(self, j):
		return 2 * j
	```
- Has a **right child** is at `2j + 1`
	```Python
	def right(self, j):
        return 2 * j + 1
	```
- Has a **parent** is at `(j) // 2`
	```Python
	def parent(self, j):
        return j // 2
	```

Pretty cool, right? This also eradicates an important issue with trees: their runtime. Granted, logarithmic runtimes are excellent, but making something into an array that one can simply index in constant time is even better. It's super efficient—no need for pointers, and everything stays tight in memory.

We can also use this anciliary methods to check whether or not any given node has a left and/or right child:

```Python
def has_left(self, j):
	return self.left(j) <= len(self.data) - 1

def has_right(self, j):
	return self.right(j) <= len(self.data) - 1
```

<a id="3-1"></a>

### Heap Items

Rememer that each item in a priority queue has both a value and a priority, and our implementation will reflect that. We will be using a regular old `list` items for our array (though our `ArrayList` would also be totally fine), and since we're building a min-heap, we need a way check if other items have a lesser priority:

```Python
class Item:
	def __init__(self, priority, value=None):
			self.priority = priority
			self.value = value

	def __le__(self, other):
			return self.priority <= other.priority
```

---

<a id="3-2"></a>

### Insert and Upheap (`fix_up`)

When a new item is inserted, it is **placed at the bottom** of the heap (the end of the array):

```Python
def insert(self, priority, value=None):
	new_item = ArrayMinHeap.Item(priority, value)
	self.data.append(new_item)

	self.fix_up(len(self.data) - 1)
```

Because simply appending it will likely result in us breaking the heap properties, we must **"bubble it up"** if it's smaller than its parent. This process is also known as "upheaping" or "heapifying". In our code, this is represented by the method `fix_up`. The idea is as follows:  
> While the inserted node’s priority is less than its parent’s priority, **swap them**.

Suppose we have this initial heap:

Priority (shown as just numbers for clarity):

```
            2
          /   \
        5       8
       / \     /
     10  15  12
```

Corresponding array:

```
Index:     0   1   2   3   4   5
Data:    [2,  5,  8, 10, 15, 12]
```

Now we insert a new element with **priority `1`**.

#### Step 1: Insert at the end
The new array:

```
Index:     0   1   2   3   4   5   6
Data:    [2,  5,  8, 10, 15, 12,  1]

Tree:
            2
          /   \
        5       8
       / \     / \
     10  15  12   1   ← bad!
```

We break the heap property since `1` is smaller than `8`. We need to move `1` up:

#### Step 2: Fix-up begins

- `curr_ind = 6` → Value = `1`
- `parent(6) = 2` → Value = `8`
- Since `1 < 8`, **swap**!

New heap (swap index 7 and 3):

```
            2
          /   \
        5       1     ← still bad!
       / \     / \
     10  15  12   8
```

Array:

```
Index:     0   1   2   3   4   5   6
Data:    [2,  5,  1, 10, 15, 12,  8]
```

#### Step 3: Continue fix-up

- `curr_ind = 2` → Value = `1`
- `parent(2) = 0` → Value = `2`
- Since `1 < 2`, **swap again**!

New heap:

```
            1         ← good! amazing! incredible!
          /   \
        5       2
       / \     / \
     10  15  12   8
```

Array:

```
Index:     0   1   2   3   4   5   6
Data:    [1,  5,  2, 10, 15, 12,  8]
```

Now `curr_ind = 0`, which is the root, so we stop. **Each level we move up**, we compare with the parent and possibly swap. The height of the tree is O(log `n`), so `fix_up` performs at most log `n` swaps; the heap property is restored.

```Python
def fix_up(self, j):
	curr_ind = j
	keep_going = True

	while keep_going == True and curr_ind > 1:
		
		parent_ind = self.parent(curr_ind)

		if self.data[parent_ind] <= self.data[curr_ind]:
			keep_going = False
		else:
			self.swap(curr_ind, parent_ind)
			curr_ind = parent_ind

def swap(self, i, j):
	self.data[i], self.data[j] = self.data[j], self.data[i]
```

---

<a id="3-3"></a>

### Delete and Downheap (`fix_down`)

Deleting an element from the heap involves removing the minimum element, which is always at the root. In its place, the last item in the heap is **moved to the root** to temporarily fill the empty spot. However, this often violates the heap property—the new root might be larger than one (or both) of its children. To restore the heap order, we must **"bubble it down"**. This process is called "downheaping" or "heapifying down" which, in our class, is taken care of by the `fix_down` method.

```Python
def delete_min(self):
	if self.is_empty():
		raise Exception("Priority queue is empty.")

	self.swap(1, len(self.data) - 1)
	item = self.data.pop()

	if not self.is_empty():
		self.fix_down(1)

	return item
```

How does `fix_down` work? The idea is as follows:  
> While the current node’s priority is **greater than one of its children**, **swap it with the smaller child**.

Suppose we have this heap before deleting:

Priority (shown as just numbers for clarity):

```
            1
          /   \
        5       2
       / \     / \
     10  15  12   8
```

Corresponding array:

```
Index:     0   1   2   3   4   5   6
Data:    [1,  5,  2, 10, 15, 12,  8]
```

Now we remove the root (`1`). To maintain the complete binary tree structure, we move the last element (`8`) to the root.

#### Step 1: Replace root with last item
New array:

```
Index:     0   1   2   3   4   5
Data:    [8,  5,  2, 10, 15, 12]

Tree:
            8
          /   \
        5       2
       / \     /
     10  15  12      ← bad! root is too big!
```

We break the heap property since `8` is greater than `2`. We need to move `8` down:

#### Step 2: Fix-down begins

- `curr_ind = 0` → Value = `8`
- `left(0) = 1` → Value = `5`
- `right(0) = 2` → Value = `2`
- Among the two children, the smaller one is `2` at index 2.
- Since `8 > 2`, **swap!**

New heap (swap index 0 and 2):

```
            2
          /   \
        5       8
       / \     /
     10  15  12
```

Array:

```
Index:     0   1   2   3   4   5
Data:    [2,  5,  8, 10, 15, 12]
```

#### Step 3: Continue fix-down

- `curr_ind = 2` → Value = `8`
- `left(2) = 5` → Value = `12`
- No right child (we’re at the bottom)
- Since `8 < 12`, no more swaps needed — stop here.

Heap is now valid!

```
            2         ← good! amazing! incredible!
          /   \
        5       8
       / \     /
     10  15  12
```

Array:

```
Index:     0   1   2   3   4   5
Data:    [2,  5,  8, 10, 15, 12]
```

Now `curr_ind = 2`, and its only child is larger — so we stop. **Each level we move down**, we compare with both children and possibly swap with the smaller one. The height of the tree is O(log `n`), so `fix_down` performs at most log `n` swaps; the heap property is restored.

In our class, this bubbling down process is done by the `fix_down` method:

```Python
def fix_down(self, j):
    curr_ind = j
    keep_going = True

    while keep_going and self.has_left(curr_ind):

        if self.has_right(curr_ind):
            left_ind = self.left(curr_ind)
            right_ind = self.right(curr_ind)

            if self.data[right_ind] <= self.data[left_ind]:
                small_child_ind = right_ind
            else:
                small_child_ind = left_ind
        else:
            small_child_ind = self.left(curr_ind)

        if self.data[curr_ind] <= self.data[small_child_ind]:
            keep_going = False
        else:
            self.swap(curr_ind, small_child_ind)
            curr_ind = small_child_ind
```

What does `self.has_left(curr_ind) == True` do? This checks whether the current node has a left child. In a binary heap (stored as an array), if a node has no left child, it cannot have a right child either—it’s a leaf. So this is our signal that we’ve reached the bottom of the heap, and we can stop.

Why left and not right? Because every non-leaf node in a complete binary tree (like a heap) will:

- Either have both children
- Or have only a left child

Having only a right child without a left child is not possible in a binary heap. So checking for a left child is the minimal check to ensure we're not at a leaf.

---

<a id="3-4"></a>

### Initialising Our `ArrayMinHeap`

Now that we understand the process of heapifying, let's take a look at the initialiser method of our class:

```Python
def __init__(self, priorities_lst=None, values_lst=None):
	self.data = [None]
	
	if priorities_lst is not None:
		for i in range(len(priorities_lst)):
			new_item = ArrayMinHeap.Item(priorities_lst[i], values_lst[i])
			self.data.append(new_item)
			
		first_non_leaf_ind = self.parent(len(self.data) - 1)
		
		for i in range(first_non_leaf_ind, 0, -1):
			self.fix_down(i)
```

Step by step, we have

```Python
def __init__(self, priorities_lst=None, values_lst=None):
    self.data = [None]
```

This initialises the heap. `self.data` is the array used to store the heap. It starts with `[None]` so that the first element is at index 1.

Why? Because the math for parent/child nodes becomes clean:

- **Left child**: 2 * j
- **Right child**: 2 * j + 1
- **Parent**: j // 2

If the user passed in two lists (priorities and values), we need to build the array of `Item` objects from the start.

```Python
	if priorities_lst is not None:
		for i in range(len(priorities_lst)):
			new_item = ArrayMinHeap.Item(priorities_lst[i], values_lst[i])
			self.data.append(new_item)

    first_non_leaf_ind = self.parent(len(self.data) - 1)
```

The last node in the heap is at `index len(self.data) - 1`. Its parent is the last **non-leaf** node—the last one that could have children.

From here, we’ll start heapifying from here and move upward:

```Python
    for i in range(first_non_leaf_ind, 0, -1):
        self.fix_down(i)
```

This runs in **linear time**, which is more efficient than inserting each item one-by-one.

---

| Method         | What It Does                      | Time Complexity |
|----------------|-----------------------------------|-----------------|
| `insert`       | Adds new element                  | O(log `n`)      |
| `delete_min`   | Removes smallest element          | O(log `n`)      |
| `min`          | Returns smallest element          | O(1)          |
| `fix_up`       | Restores heap upward              | O(log `n`)      |
| `fix_down`     | Restores heap downward            | O(log `n`)      |
| `__init__`     | Builds heap from lists            | O(`n`)          |

<a id="4"></a>

## Runtime Analysis and Comparisons

The main reason heaps are better is because the **height of a complete binary tree** is `Θ(log n)`. This makes the number of nodes from levels 0 to `h` is:


> 1 + 2 + 4 + ... + 2<sup>`h`</sup> ≈ 2<sup>`h` + 1</sup> - 1

If 2<sup>`h` + 1</sup> - 1, taking log:

> `h` ≈ log₂(`n`)

Thus, insertions and removals are logarithmic! In contrast, linked structures require pointer chasing. Lists (even sorted ones) require Θ(`n`) time for inserting.

| Implementation | Insert | Find Min | Remove Min |
|:--------------:|:------:|:--------:|:----------:|
| Unsorted List | Θ(1)   | Θ(`n`)     | Θ(`n`)       |
| Sorted List   | Θ(`n`)   | Θ(1)     | Θ(1)       |
| Linked Tree   | Θ(log `n`) | Θ(log `n`) | Θ(log `n`)   |
| **Heap (Array)** | **Θ(log `n`)** | **Θ(1)** | **Θ(log `n`)** |