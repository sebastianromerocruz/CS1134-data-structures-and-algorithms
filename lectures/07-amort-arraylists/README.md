<h2 align=center>Week IV: <em>Day 1</em> and Week V</h2>

<h1 align=center><code>ArrayList</code></h1>

<p align=center><strong><em>Song of the day</strong>: <a href="https://youtu.be/34ckxHVZqoI?si=sv6JNeU0GIMlmMzO"><strong><u>断气</u></strong></a> by 回春丹 (2022), recommended by Xin Chen.</em></p>

---

## Sections

1. [**Python Lists and the Reality of `.append()`**](#1)
    1. [**`.append()` Under the Hood**](#1-1)
    2. [**Python Lists and Arrays**](#1-2)
    3. [**How `.append()` Works in Reality**](#1-3)
2. [**Amortised Analysis**](#2)
<!-- 3. [**`ArrayList`**](#3)
    1. [**Dynamic Array Growth**](#3-1)
    2. [**The Python Implementation**](#3-2)
4. [**Addendum A: _Important Summations To Know_**](#4)
5. [**Addendum B: _Dunder Methods_**](#5) -->

<p align=center><strong><em><a href="assets/ArrayList I.pdf">Day 1 Handwritten Class Notes</a></em></strong></p>

---

<a id="1"></a>

## Python Lists and the Reality of `.append()`

<a id="1-1"></a>

### `.append()` Under the Hood

When we first learn to program in Python, we often assume that the `.append()` method simply places a new element directly into the next available memory slot. For example:

```python
lst = [1, 2, 3]
lst.append(4)
```

You might imagine `.append()` working like this:

![append-wrong](assets/append-wrong.png)

<sub>**Figure 1**: How we might initially think `.append()` works, with the new value immediately placed at the next memory location.</sub>

However, this understanding is a bit misleading. In reality, Python's memory model doesn't guarantee that the memory adjacent to the list is available. The computer's RAM is being shared by many applications, which may already occupy those memory blocks. For instance, consider these memory allocations:

|  Process Name  | Memory in Use            |
|:--------------:|:------------------------:|
|  Python        | 0xfbc3b5ea - 0xfbc3c71a  |
|                | 0x2e48a424 - 0x4e48a424  |
|  Zoom          | 0xd0c2f880 - 0xd4c2d133  |
|  Brave Browser | 0x54356cfe - 0x75336afe  |
|  Slack         | 0x1dbbda19 - 0x1dbbcdee  |
|  Steam         | 0x8906e993 - 0x892c453e  |

<sub>**Figure 2**: Example of memory blocks being used by various processes.</sub>

Since Python can't assume the next block is free, `.append()` does something much smarter.

<a id="1-2"></a>

### Python Lists and Arrays

Under the hood, Python lists are implemented using something called a **dynamic array**. At its core, this involves an **array**, which is a fixed-size data structure that:
- Stores a sequential collection of values.
- Has all its elements stored contiguously in memory.
- Requires all elements to be of the same size.

Consider this Python list:

```python
lst = [10, 20, 30, 40, 50]

print(len(lst))  # Output: 5
print(lst[4])    # Output: 50
```

Visually, the memory model for this list might look like this:

![array-list](assets/arraylist.png)

<sub>**Figure 3**: Memory model of a Python list.</sub>

Here’s what happens:
- The green boxes represent the **array** part of the list.
- Because arrays have a fixed size and are stored contiguously, we can access any element in **constant time** using this formula:
  ```
  Address of lst[k] = base_address_of_array + (k * size_of_an_element)
  ```

For example, if the base address is `0x4a003` and each element takes 8 bytes, the address of `lst[4]` can be calculated directly:
```
Address of lst[4] = 0x4a003 + (4 * 8) = 0x4a023
```

<a id="1-3"></a>

### **How `.append()` Works in Reality**

If arrays have a **fixed size**, how can Python lists grow dynamically? This is where **dynamic arrays** (also known as **`ArrayLists`**) come into play. Instead of directly appending elements into the next available memory slot, Python lists handle growth in a more sophisticated way:

1. **Preallocate Extra Memory:** When a list is created, Python allocates more memory than is immediately needed. So, if we were to need a list of 3 elements, Python might allocate enough memory for _6_.
2. **Use Reserved Space:** Because of that extra allocated memory, `.append()` can add a few elements **without resizing** as long as there is free space available.
3. **Resize When Full:** Once there is no more space available, Python **allocates a larger array, copies the existing elements into it, and then appends the new element**.

This strategy not only prevents unnecessary resizing every time an element is added, but it also, believe it or not, makes appends significantly more efficient.

![append-right](assets/append-right.png)  

<sub>**Figure 4**: When the array reaches its limit, a completely new array (ID `2000`) is created, and all elements are copied over.</sub>  

But how does it do this, and just how much more efficient is it? Also, more efficient than what, exactly?

<a id="1-3-1"></a>

#### Naïve Resizing

A simple (though inefficient) way to resize an array would be to increase its size by just 1 every time an element is appended.

<a id="naive"></a>

![append-naive](assets/append-naive.png)  

<sub>**Figure 5**: Increasing the array size by 1 for every `.append()` call.</sub>  

Under this approach:
- Each `.append()` requires allocating a new array _one slot larger_, and copying _all elements_.
- Since copying takes **Θ(k)** time (where `k` is the current length of the list), the total time for `n` appends is:

  > **T(`n`)** = 1 + 2 + 3 + ... + `n` = **Θ(`n`²)**[**\***](#4)

This quadratic runtime is, as [**we've seen**](https://github.com/sebastianromerocruz/CS1134-data-structures-and-algorithms/blob/main/lectures/06-searching-algos/assets/runtimes.jpg), quite inefficient for a common operation like `.append()`. As you can imagine, Python's developers did not opt to go this route, and instead chose a much more efficient way of going about it.

<a id="1-3-2"></a>

#### Our Optimisation

Instead of increasing the size by 1, Python lists actual **double in size** whenever they run out of space. This is **far more efficient**.

<a id="optimised"></a>

![append-optimised](assets/append-optimised.png)  

<sub>**Figure 6**: When the array reaches capacity, it is resized to **double** its previous size.</sub>  

Why on Earth would this be more efficient? Well, let's go about this methodically. When we append elements to a list under this method, the runtime becomes:
- **Best Case:** Ω(1), when there is available space.
- **Worst Case:** O(`k`), when resizing happens.

The work being donw in this case becomes a _sum of the powers of 2_ for `n` appends is now:

> **T(`n`)** = 1 + 2 + 4 + 8 + ... + `n` = **Θ(`n`)**[**\***](#4)

So we've achieved **Θ(`n`)**[**\***](#4) runtime doing this! So, is `append` a linear operation. Under the worst-case scenario, yes. But no longer for the best-case scenario. Does this change anything at all?

Turns out that it does. As `n` approaches infinity, we don't double the array does anywhere as much as we index and place an element. Because of this, we say that the **average (or _amortised_) time per `.append()` operation is actually _Θ(1)_**—constant time.

<br>

<a id="2"></a>

## Amortised Analysis

Wait, what? There's no way!—you might say. At first glance, this strategy may seem stuck in linear limbo forever—after all, copying `n` elements during a resize takes O(`n`) time (worst-case). However, because the _frequency of resizes decreases exponentially_ as `n` approaches infinity, the overall cost of doubling the array size when appending `n` elements remains stops mattering completely. 

This brings us to an important concept in algorithm analysis: **amortised analysis**, which helps explain why `.append()` is efficient _on average_, even though some operations take longer than others. According to [**Wikipedia**](https://en.wikipedia.org/wiki/amortised_analysis):

> _The motivation for amortised analysis is that looking at the worst-case run time can be too pessimistic. Instead, amortised analysis averages the running times of operations in a sequence over that sequence._

In other words, we need not always look at the dark side of life. We measure amortised analysis by the following formula:

> **T<sub>amortised</sub>(`n`) = total cost of the entire series of operations / `n`**

This means that for our [**naive approach**](#naive), our amortised runtime is as follows:

> **T<sub>amortised</sub>(`n`)** = Θ(`n`<sup>2</sup>) / `n` = **Θ(`n`)**

And our [**optimised approach**](#optimised) is:

> **T<sub>amortised</sub>(`n`)** = Θ(`n`) / `n` = **Θ(`1`)**

Amazing, I know. The power of a little optimism is crazy.

<br>

<!-- <a id="3"></a>

## **`ArrayList`: The True Story of Python Lists**

This all brings us back to Python lists. Consider the following piece of code:

```python
lst = []
for i in range(1, 6):
    lst.append(10 * i)
```

<a id="3-1"></a>

### **Dynamic Array Growth**

Initially, the list starts with a small capacity—just enough to hold a single element. As we append elements, Python dynamically resizes the list when necessary. The result is something like this:

![arraylist-1](assets/arraylist-1.png)

<sub>**Figure 6**: The list's capacity doubles each time it runs out of space, resulting in three resizing operations here.</sub>

As we now know, Python doesn't simply expand the existing memory; instead, it creates a completely new, larger array, copies the existing elements into it, and then appends the new element. 

For instance, just when we're about to append `50` to the list, an accurate memory map would look like this:

![arraylist-2](assets/arraylist-2.png)

<sub>**Figure 7**: The array portion of the list is stored in a separate memory location, and the resizing involves copying data to this new space.</sub>

<a id="3-2"></a>

### **The Python Implementation**

Behind the scenes, Python lists rely on a dynamic array implementation. While we can't see the exact C-level details directly, we can simulate a simplified version in Python:

```python
import ctypes  # provides low-level arrays


def make_array(n):
    return (n * ctypes.py_object)()


class ArrayList:
    def __init__(self):
        self.data_arr = make_array(1)
        self.capacity = 1
        self.n = 0

    def resize(self, new_size):
        new_array = make_array(new_size)
        for i in range(self.n):
            new_array[i] = self.data_arr[i]
        self.data_arr = new_array
        self.capacity = new_size

    def append(self, val):
        if (self.n == self.capacity):
            self.resize(2 * self.capacity)
        self.data_arr[self.n] = val
        self.n += 1

    def extend(self, iter_collection):
        for elem in iter_collection:
            self.append(elem)

    def __len__(self):
        return self.n

    def __getitem__(self, ind):
        if (not (0 <= ind <= self.n - 1)):
            raise IndexError('invalid index')
        return self.data_arr[ind]

    def __setitem__(self, ind, val):
        if (not (0 <= ind <= self.n - 1)):
            raise IndexError('invalid index')
        self.data_arr[ind] = val

    def __iter__(self):
        for i in range(len(self)):
            yield self.data_arr[i]  #could also yield self[i]
```

Note here in this implementation:
- The **`resize` method** handles the creation of a larger array and the transfer of existing elements.
- The **`append` method** doubles the array’s capacity when needed by calling `resize` and using `2 * self.capacity` as an argument.

<br>

<a id="4"></a>

## Addendum A: _Important Summations To Know_

1. 

> 1 + 2 + 3 + 4 + 5 + ... + `n` = `n`(`n` - 1) / 2 = **Θ(`n`<sup>2</sup>)**

2.

> 1 + 2 + 3 + 4 + 5 + ... + √`n` = **Θ(`n`)**

3.

> 1 + 2 + 3 + 4 + 5 + ... + log(`n`) = **Θ(log<sup>2</sup>(`n`))**

4.

> 1 + 2 + 4 + 8 + 16 + ... + 2<sup>`n`</sup> = 2<sup>`n` - 1</sup> - 1 = **Θ(2<sup>`n`</sup>)**

5.

> 1 + 2 + 4 + 8 + 16 + ... + `n` = 2`n` - 1 = **Θ(`n`)**

<br>

<a id="5"></a>

## Addendum B: _Dunder Methods_

| Common Syntax     | Special Method Form                  |
|--------------------|--------------------------------------|
| `a + b`           | `a.__add__(b)`, alternatively `b.__radd__(a)` |
| `a - b`           | `a.__sub__(b)`, alternatively `b.__rsub__(a)` |
| `a * b`           | `a.__mul__(b)`, alternatively `b.__rmul__(a)` |
| `a / b`           | `a.__truediv__(b)`, alternatively `b.__rtruediv__(a)` |
| `a // b`          | `a.__floordiv__(b)`, alternatively `b.__rfloordiv__(a)` |
| `a % b`           | `a.__mod__(b)`, alternatively `b.__rmod__(a)` |
| `a ** b`          | `a.__pow__(b)`, alternatively `b.__rpow__(a)` |
| `a << b`          | `a.__lshift__(b)`, alternatively `b.__rlshift__(a)` |
| `a >> b`          | `a.__rshift__(b)`, alternatively `b.__rrshift__(a)` |
| `a & b`           | `a.__and__(b)`, alternatively `b.__rand__(a)` |
| `a ^ b`           | `a.__xor__(b)`, alternatively `b.__rxor__(a)` |
| `a \| b`           | `a.__or__(b)`, alternatively `b.__ror__(a)` |
| `a += b`          | `a.__iadd__(b)`                     |
| `a -= b`          | `a.__isub__(b)`                     |
| `a *= b`          | `a.__imul__(b)`                     |
| `+a`              | `a.__pos__()`                       |
| `-a`              | `a.__neg__()`                       |
| `~a`              | `a.__invert__()`                    |
| `abs(a)`          | `a.__abs__()`                       |
| `a < b`           | `a.__lt__(b)`                       |
| `a <= b`          | `a.__le__(b)`                       |
| `a > b`           | `a.__gt__(b)`                       |
| `a >= b`          | `a.__ge__(b)`                       |
| `a == b`          | `a.__eq__(b)`                       |
| `a != b`          | `a.__ne__(b)`                       |
| `a in b`          | `a.__contains__(b)`                 |
| `a[k]`            | `a.__getitem__(k)`                  |
| `a[k] = v`        | `a.__setitem__(k, v)`               |
| `del a[k]`        | `a.__delitem__(k)`                  |
| `a(arg1, arg2, ...)` | `a.__call__(arg1, arg2, ...)`    |
| `len(a)`          | `a.__len__()`                       |
| `hash(a)`         | `a.__hash__()`                      |
| `iter(a)`         | `a.__iter__()`                      |
| `next(a)`         | `a.__next__()`                      |
| `bool(a)`         | `a.__bool__()`                      |
| `float(a)`        | `a.__float__()`                     |
| `int(a)`          | `a.__int__()`                       |
| `repr(a)`         | `a.__repr__()`                      |
| `reversed(a)`     | `a.__reversed__()`                  |
| `str(a)`          | `a.__str__()`                       | -->