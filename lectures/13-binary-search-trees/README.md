<h2 align=center>Week 13</h2>

<h1 align=center>Abstract Data Types: <em>Binary Search Trees</em></h1>

<p align=center><strong><em>Song of the day</strong></em>: <em><a href="https://youtu.be/ZeylQF-5OSE?si=KGiamrO-RRsGBD-B"><strong><u>Something To Hold (Live at Glasshaus)</u></strong></a> by Bilal [feat. Questlove, Common, Robert Glasper, & Burniss Travis] (2024)</em></p>

---

## Sections
1. [**Searching Using Trees**](#1)
    - [**Our Search For The Perfect Search**](#1-1)
    - [**Intro To BSTs**](#1-2)
2. [**Runtime Analysis**](#2)
3. [**BST Operations**](#3)

---

<a id="1"></a>

## Binary (Search) Trees

<a id="1-1"></a>

### Our Search For The Perfect Search

Last time, we introduced the concept of maps with a pretty tall order of a promise: constant-time lookup speeds. As prelude to such amazing speeds, we discussed the potential implementation of maps using less-efficient data structures:

| **Map Implementation**     | **Find**    | **Insert**   | **Delete**  |
|----------------------------|-------------|-------------|--------------|
| **UnsortedArrayMap**       | Θ(`n`)        | Θ(`n`)        | Θ(`n`)   |
| **UnsortedLinkedListMap**  | Θ(`n`)        | Θ(`n`)        | Θ(`n`)   |
| **SortedArrayMap**         | Θ(log(`n`))   | Θ(`n`)        | Θ(`n`)   |
| **SortedLinkedListMap**    | Θ(`n`)        | Θ(`n`)        | Θ(`n`)   |

<sub>**Figure 1**: Data Structures for Map ADT.</sub>

These are pretty paltry runtimes, especially when you consider our constant-time goal. As we will see next week, these data structures are but a (necessary) prelude to implementing our super-efficient map. Before that, though, we'll introduce one more data structure that's like utilises our most recent ADT: the **binary search tree (BST)**.

<a id="1-2"></a>

### Intro To BSTs

The formal definition of these special trees goes as follows:

> Let **`T`** be a binary tree. We say that **`T`** is a Binary Search Tree, if for each node **`n`** in **`T`**:
>
> - All keys stored in the left subtree of `n` are less than the key stored in `n`.
>
> - All keys stored in the right subtree of `n` are greater than the key stored in `n`.

Here's an example of one, right alongside one that _isn't_:

![binary-vs-not](assets/binary-vs-not.png)

<sub>**Figure 2**: Because 42 is greater than its ancestor node 26, we cannot call this a BST.</sub>

<br>

<a id="2"></a>

## Runtime Analysis

You'll notice above that the runtime notation for both of these trees is slightly different. Namely, we say that the runtime of each operation in a BST is **Θ(`h`)** and not Θ(`n`), where `h` stands for the _height_ of the tree. Why is this the case?

Well, consider a situation where we start inserting the following numbers into a BST:

```python
bst = BinarySearchTree()
lst = [14, 18, 22, 24]

for number for lst:
    lst.insert(number)
```

Because the numbers in `lst` are already sorted, our BST would end up looking highly skewed to the right:

![bst-skewed-1](assets/bst-skewed-1.png)

<sub>**Figure 3**: This ends up looking more like a linked list.</sub>

Similarly, if the list contained numbers in descending order, like `[12, 10, 6, 2]`, we'd have a tree highly skewed to the left:

![bst-skewed-2](assets/bst-skewed-2.png)

<sub>**Figure 4**: We've got a similar, very _linear_ situation here.</sub>

Since the height, `h`, is defined as the longest possible path in a tree, then we must consider the possibility that _the BST could be simply a single path with length `h`_. So we say, as we've [**determined many times before**](https://github.com/sebastianromerocruz/CS1134-data-structures-and-algorithms/tree/main/lectures/03-asymptotic-analysis#analysing-code), that the runtime of such a traversal would be ***Θ(`n`)***.

<br>

<a id="3"></a>

## BST Operations

<a id="3-1"></a>

### Lookup

Searching for a value in a **Binary Search Tree (BST)** is simple because the tree is **ordered**: for any node with value `v`, everything in the left subtree is less than `v`, and everything in the right is greater.

Let’s say we’re searching for a value `8` in the following BST. Starting at our root node:

1. **If the current node is `None`**, return `None` → the value isn’t in the tree.
2. **If `8 == node.data`**, return the node, since we've found our target.
3. **If `8 < node.data`**, search the **left subtree**.
4. **If `8 > node.data`**, search the **right subtree**.

![search](assets/search.png)

<sub>**Figure 4**: We've got a similar, very _linear_ situation here.</sub>

Since we eliminate half of the tree with each step—just like with [**binary search**](https://github.com/sebastianromerocruz/CS1134-data-structures-and-algorithms/tree/main/lectures/04-searching-algos#2)—our average runtime of lookup _if the tree is not heavily skewed_ (which is a really big assumption that we don't usually make) can be logarithmic!

- **Best Case**: value is found near the root → Θ(1)
- **General Average Case**: Θ(`h`)
- **Balanced Average Case**: Θ(log `h`)
- **Worst Case**: Θ(`n`) if the tree is skewed (like a linked list)