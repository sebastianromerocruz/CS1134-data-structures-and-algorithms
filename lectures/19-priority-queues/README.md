<h2 align=center>Week 15</h2>

<h1 align=center>Abstract Data Types: <em>Priority Queues (Heaps)</em></h1>

<p align=center><strong><em>Song of the day</strong></em>: <em><a href="https://youtu.be/a_426RiwST8?si=FjOzqQ_iESqBGV1q"><strong><u>Lonely Boy</u></strong></a> by The Black Keys (2011)</em></p>

---

## Sections

1. [**Motivation and Priority Queues**](#1)
2. [**Heap Fundamentals**](#2)
3. [**Heap Implementation**](#3)
	- [**Heap Items**](#3-1)
	- [**Insert and Upheap (`fix_up`)**](#3-2)
	- [**Find Minimum (`min`)**](#3-3)
	- [**Delete and Downheap (`fix_down`)**](#3-4)
	- [**Initialising Our `ArrayMinHeap`**](#3-5)
4. [**Runtime Analysis and Comparisons**](#4)

<p align=center><strong><em><a href="assets/Priority Queues 2.pdf">Handwritten Class Notes</a></em></strong></p>

---

<a id="1"></a>

## Motivation and Priority Queues

Imagine a busy airport line where not everyone is served in the exact order they arrived. Passengers with first-class tickets or special status can move ahead because their priority is higher. In computing, that idea is captured by a **priority queue**. It is a data structure where each item has a value and a priority, and the item with the best priority is removed first.

In a min-heap, the smallest priority is considered best. In a max-heap, the largest priority is considered best. The important part is that removals always return the current best item.

This structure shows up in many places: Dijkstra’s shortest-path algorithm, operating system schedulers, simulation event queues, and more. The challenge is to support frequent insertions while still finding the best item much faster than scanning the whole list.

<br>

<a id="2"></a>

## Heap Fundamentals

The easiest way to build a priority queue is with a **binary heap**. Think of it as a binary tree with two simple rules:

1. **Heap-order property**: In a _min-heap_, every parent is _no larger than_ its children. That’s why the smallest item always lives at the top.

2. **Complete binary tree**: The tree fills up level by level, left to right, and only the last level may be incomplete. That keeps the tree’s height down to about `Θ(log n)`.

Here’s an example of a valid min-heap:

```
        2
       / \
      4   3
     / \
    10  5
```

And here's one that violates the heap rules:

```
        7
       / \
      3   9
```

The `3` is smaller than the root `7`, which breaks the heap property.

<br>

<a id="3"></a>

## Heap Implementation

Although heaps can be represented as trees with nodes and pointers, the usual implementation uses **arrays** instead.

A complete binary tree can be stored compactly in a single array, and the parent/child relationships become simple index calculations. That avoids the extra memory overhead and bookkeeping of pointer-based trees while still letting us treat the structure like a tree.

In other words, the following tree:

```
        2
       / \
      4   3
     / \
    10  5
```

Would correspond to the following array:

```Python
[None, 2, 4, 3, 10, 5]
```

That `None` at index 0 is a placeholder—it makes the index arithmetic for parent/child navigation work out cleanly; **the actual heap elements start at index 1.**

With this 1-based layout, for any node at index `j`:

- Has a **left child** at index `2j`
	```Python
	def left(self, j):
		return 2 * j
	```
- Has a **right child** at index `2j + 1`
	```Python
	def right(self, j):
		return 2 * j + 1
	```
- Has a **parent** at index `j // 2`
	```Python
	def parent(self, j):
		return j // 2
	```

This means we can access tree nodes in constant time by index, without pointer chasing, and the array stays compact.

We can also use these ancillary methods to check whether or not any given node has a left and/or right child:

```Python
def has_left(self, j):
	return self.left(j) <= len(self.data) - 1

def has_right(self, j):
	return self.right(j) <= len(self.data) - 1
```

Both methods compute the candidate child index and check whether it falls within the bounds of `self.data`. If `2j` is already past the end of the array, there's no left child. Same logic for `2j + 1`.

<a id="3-1"></a>

### Heap Items

Remember that each item in a priority queue has both a value and a priority, and our implementation will reflect that. We will be using a plain Python `list` for our array, and since we're building a min-heap, we need a way to check if other items have a lesser priority:

```Python
class Item:
	def __init__(self, priority, value=None):
		self.priority = priority
		self.value = value

	def __le__(self, other):
		return self.priority <= other.priority
```

Two things in this class deserve attention:

- **`value=None`**: The value is optional because some use cases are purely priority-based—you only care about ordering, not what data is attached.

- **`__le__` (less-than-or-equal), not `__lt__`**: Both `fix_up` and `fix_down` use `<=` comparisons to decide whether a swap is needed. Specifically, `if self.data[parent_ind] <= self.data[curr_ind]` means "if the parent is already in the right place (≤ the child), stop." Defining `__le__` lets Python evaluate that expression directly on `Item` objects. Without it, Python wouldn't know how to compare two `Item`s, and the heap operations would crash.

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

`self.data.append(new_item)` adds the new item at the end. Right after, `len(self.data) - 1` gives us the index of the item we just appended—that's the starting position for `fix_up`.

Because simply appending it will likely result in us breaking the heap property, we must **"bubble it up"** if it's smaller than its parent. This process is also known as "upheaping". In our code, this is represented by the method `fix_up`. The idea is as follows:
> While the inserted node's priority is less than its parent's priority, **swap them**.

Suppose we have this initial heap:

Priority (shown as just numbers for clarity):

```
            2
          /   \
        5       8
       / \     /
     10  15  12
```

Corresponding array (index 0 is the `None` placeholder; real elements start at index 1):

```
Index:     0    1   2   3   4   5   6
Data:   [None,  2,  5,  8, 10, 15, 12]
```

Now we insert a new element with **priority `1`**.

#### Step 1: Insert at the end

```
Index:     0    1   2   3   4   5   6   7
Data:   [None,  2,  5,  8, 10, 15, 12,  1]

Tree:
            2
          /   \
        5       8
       / \     / \
     10  15  12   1   ← bad!
```

We break the heap property since `1` is smaller than `8`. We need to move `1` up:

#### Step 2: Fix-up begins

- `curr_ind = 7` → `data[7] = 1`
- `parent(7) = 7 // 2 = 3` → `data[3] = 8`
- Since `1 < 8`, **swap** indices 7 and 3:

```
Index:     0    1   2   3   4   5   6   7
Data:   [None,  2,  5,  1, 10, 15, 12,  8]

Tree:
            2
          /   \
        5       1     ← still bad!
       / \     / \
     10  15  12   8
```

#### Step 3: Continue fix-up

- `curr_ind = 3` → `data[3] = 1`
- `parent(3) = 3 // 2 = 1` → `data[1] = 2`
- Since `1 < 2`, **swap** indices 3 and 1:

```
Index:     0    1   2   3   4   5   6   7
Data:   [None,  1,  5,  2, 10, 15, 12,  8]

Tree:
            1
          /   \
        5       2
       / \     / \
     10  15  12   8
```

Now `curr_ind = 1`, which is the root, so we stop (`curr_ind > 1` is `False`). **Each level we move up**, we compare with the parent and possibly swap. The height of the tree is O(log `n`), so `fix_up` performs at most log `n` swaps and restores the heap property.

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

Reading through the while loop:

- **`curr_ind = j`**: We start at the index of the newly inserted item. Each iteration we'll move `curr_ind` one level up the tree.

- **`while keep_going and curr_ind > 1`**: The `curr_ind > 1` condition is why the `None` placeholder matters. Index `1` is the root—there's no parent above it. If we ever reach index `1`, we stop. (Index `0` is `None`, so we must never treat it as a real node.)

- **`if self.data[parent_ind] <= self.data[curr_ind]: keep_going = False`**: If the parent is already ≤ the current node, the heap order is satisfied from here upward—there's nothing left to fix. We set `keep_going = False` to exit cleanly.

- **`self.swap(curr_ind, parent_ind)` / `curr_ind = parent_ind`**: Otherwise, the parent is too large, so we swap and move `curr_ind` up one level to repeat the check.

---

<a id="3-3"></a>

### Find Minimum (`min`)

In a min-heap, the smallest element is always at the root—that's exactly what the heap-order property guarantees. So finding it is trivially O(1):

```Python
def min(self):
	if self.is_empty():
		raise Exception("Priority queue is empty.")
	return self.data[1]
```

We don't need to search at all. Since every parent is ≤ its children, whatever sits at index `1` must be smaller than everything else in the heap. We just return it directly. Note that this is a non-destructive **peek**—it returns the minimum without removing it.

---

<a id="3-4"></a>

### Delete and Downheap (`fix_down`)

Deleting from the heap means removing the minimum, which is always at the root (index `1`). We can't simply delete `data[1]` and shift everything left—that would destroy the complete binary tree structure. Instead, we use a two-step trick:

1. **Swap the root with the last element** in the array.
2. **Pop the last element** (which is now the minimum we want to return).
3. **Fix down** from the root to restore the heap order.

This works because popping the last array element is O(1) and keeps the tree structurally complete. The cost is that the new root is probably out of place, but `fix_down` corrects that.

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

The `if not self.is_empty()` guard handles the edge case where the heap had exactly one element. After the swap and pop it's now empty, so calling `fix_down(1)` would try to access `data[1]`, which no longer exists. The guard prevents that crash.

How does `fix_down` work? The idea is as follows:
> While the current node's priority is **greater than one of its children**, **swap it with the smaller child**.

Why always swap with the **smaller** child? Because if we swapped with the larger one, the node we just moved down might still be larger than the other child—we'd be creating a new violation immediately. Swapping with the smaller child guarantees both children of the original position end up with a parent ≤ them.

Suppose we have this heap before deleting:

```
            1
          /   \
        5       2
       / \     / \
     10  15  12   8
```

Corresponding array:

```
Index:     0    1   2   3   4   5   6   7
Data:   [None,  1,  5,  2, 10, 15, 12,  8]
```

Now we remove the root (`1`). To maintain the complete binary tree structure, we swap it with the last element (`8`) and pop it off.

#### Step 1: Replace root with last item

```Python
self.swap(1, len(self.data) - 1)  # swap root and last element
item = self.data.pop()            # pop the min off the end
```

New array:

```
Index:     0    1   2   3   4   5   6
Data:   [None,  8,  5,  2, 10, 15, 12]

Tree:
            8
          /   \
        5       2
       / \     /
     10  15  12      ← bad! root is too big!
```

We break the heap property since `8` is greater than `2`. We need to move `8` down:

#### Step 2: Fix-down begins

- `curr_ind = 1` → `data[1] = 8`
- `left(1) = 2` → `data[2] = 5`
- `right(1) = 3` → `data[3] = 2`
- Among the two children, the smaller one is `2` at index 3.
- Since `8 > 2`, **swap** indices 1 and 3:

```
Index:     0    1   2   3   4   5   6
Data:   [None,  2,  5,  8, 10, 15, 12]

Tree:
            2
          /   \
        5       8
       / \     /
     10  15  12
```

#### Step 3: Continue fix-down

- `curr_ind = 3` → `data[3] = 8`
- `left(3) = 6` → `data[6] = 12`
- `right(3) = 7` → `7 > len(self.data) - 1 = 6`, no right child
- Since `8 < 12`, no more swaps needed—stop here.

Heap is now valid!

```
            2
          /   \
        5       8
       / \     /
     10  15  12
```

Now `curr_ind = 3`, and its only child is larger—so we stop. **Each level we move down**, we compare with both children and possibly swap with the smaller one. The height of the tree is O(log `n`), so `fix_down` performs at most log `n` swaps; the heap property is restored.

Here's the full `fix_down` method:

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

Reading through the loop:

- **`while keep_going and self.has_left(curr_ind)`**: We stop as soon as we reach a leaf (a node with no left child). In a complete binary tree, the only way to have any children is to have a left child first. If there's no left child, there can't be a right child either—so `has_left` is the minimal check that tells us whether we're at a leaf.

- **`if self.has_right(curr_ind)` / `else`**: If the current node has two children, we compare them and pick the smaller one as the candidate to swap with (`small_child_ind`). If it has only one child, it must be the left—no choice to make.

- **`if self.data[right_ind] <= self.data[left_ind]: small_child_ind = right_ind`**: The right child is smaller (or equal) so it wins. We'll swap the current node with it if needed. The `<=` here means ties break in favour of the right child, though it doesn't matter for correctness.

- **`if self.data[curr_ind] <= self.data[small_child_ind]: keep_going = False`**: If the current node is already ≤ its smallest child, the subtree is in heap order. No swap needed—set `keep_going = False` to exit.

- **`self.swap(curr_ind, small_child_ind)` / `curr_ind = small_child_ind`**: Otherwise, swap and move down one level to repeat the check.

---

<a id="3-5"></a>

### Initialising Our `ArrayMinHeap`

Here's the full initialiser:

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

```Python
	self.data = [None]
```

This initialises the heap. `self.data` starts with `[None]` so that real elements begin at index 1, giving us the clean `2j` / `2j+1` / `j//2` formulas above. If no lists are passed in, the heap is simply empty—`self.data` holds only the sentinel and we're done.

If the user passed in two lists (priorities and values), we build the array of `Item` objects first:

```Python
	if priorities_lst is not None:
		for i in range(len(priorities_lst)):
			new_item = ArrayMinHeap.Item(priorities_lst[i], values_lst[i])
			self.data.append(new_item)
```

At this point `self.data` holds all the elements, but in no particular order—it's not a heap yet. The two-step process that follows turns it into one.

Then we find the last non-leaf node—the last index that could possibly have children:

```Python
		first_non_leaf_ind = self.parent(len(self.data) - 1)
```

The last element is at `len(self.data) - 1`. Its parent is the deepest node that isn't a leaf. Every node after `first_non_leaf_ind` (higher indices) is a leaf and trivially satisfies the heap property on its own. From there, we heapify downward from each non-leaf to the root:

```Python
		for i in range(first_non_leaf_ind, 0, -1):
			self.fix_down(i)
```

This loop runs from the deepest internal node up to the root (index 1, stopping before 0). At each step, `fix_down(i)` can assume both subtrees of node `i` are already valid heaps—because we've already processed everything below `i`. So it only needs to push `data[i]` down into the right position.

**Why is this Θ(`n`) and not Θ(`n` log `n`)?**

If we had instead called `insert()` `n` times, each insert does a `fix_up` that can touch up to log `n` nodes, giving Θ(`n` log `n`) total work. The bottom-up approach is more efficient because nodes near the bottom of the tree have very little to fix-down. Leaves do nothing. Nodes one level above leaves can only move down one level. Only the root can traverse the full height. When you sum up the total work across all levels—(n/2 nodes × 0 swaps) + (n/4 nodes × 1 swap) + (n/8 nodes × 2 swaps) + ...—the sum converges to Θ(`n`).

---

| Method         | What It Does                      | Time Complexity |
|----------------|-----------------------------------|-----------------|
| `insert`       | Adds new element                  | O(log `n`)      |
| `delete_min`   | Removes smallest element          | O(log `n`)      |
| `min`          | Returns smallest element          | O(1)            |
| `fix_up`       | Restores heap upward              | O(log `n`)      |
| `fix_down`     | Restores heap downward            | O(log `n`)      |
| `__init__`     | Builds heap from lists            | O(`n`)          |

<a id="4"></a>

## Runtime Analysis and Comparisons

Heaps are fast because a complete binary tree stays short even as `n` grows. In a complete tree, each level has twice as many nodes as the level above it, so a tree of height `h` contains at most:

> 1 + 2 + 4 + ... + 2<sup>`h`</sup> = 2<sup>`h` + 1</sup> - 1 ≈ `n`

Solving for `h` gives us:

> `h` ≈ log₂(`n`)

That means operations like `insert` and `delete_min` only move through a small number of levels, so they touch O(log `n`) nodes in the worst case. The result is a good balance between fast insertion and fast removal.

Compare this to simpler alternatives:

| Implementation | Insert | Find Min | Remove Min |
|:--------------:|:------:|:--------:|:----------:|
| Unsorted List  | Θ(1)   | Θ(`n`)   | Θ(`n`)     |
| Sorted List    | Θ(`n`) | Θ(1)     | Θ(1)       |
| Linked Tree    | Θ(log `n`) | Θ(log `n`) | Θ(log `n`) |
| **Heap (Array)** | **Θ(log `n`)** | **Θ(1)** | **Θ(log `n`)** |
