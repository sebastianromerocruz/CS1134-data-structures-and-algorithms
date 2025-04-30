<h2 align=center>Week 12</h2>

<h1 align=center>Abstract Data Types: <em>Maps</em></h1>

<p align=center><strong><em>Song of the day</strong></em>: <em><a href="https://youtu.be/mZOf5_rIfK4?si=G9eNqaO7YXGh0s9M"><strong><u>Rearrange My World</u></strong></a> by Daniel Caesar, Rex Orange County (2025)</em></p>

---

## Sections
1. [**The Anatomy of Python Dictionaries**](#1)
2. [**Implementations**](#2)
    - [**`UnsortedArrayMap`**](#2-1)
        - [**Insertion**](#2-1-1)
        - [**Lookup / Finding**](#2-1-2)
        - [**Deletion**](#2-1-3)
    - [**Other Implementations**](#2-2)
3. [**Addendum: _Map ADT Dunder Methods_**](#3)
    - [**Arithmetic and Bitwise**](#3-1)
    - [**Comparisons, Membership, Indexing, and More**](#3-2)
    
<p align=center><strong><em><a href="assets/Maps.pdf">Handwritten Class Notes</a></em></strong></p>

---

<a id="1"></a>

## The Anatomy of Python Dictionaries

The next ADT that we will cover is called a **map**, and it's one that you are already quite familiar with, as they form the basis of our favourite Python type: the dictionary class (`dict`)! As a general reminder, Let's list out some of the properties that Python dictionaries have, as we well as the operations we have available to us when we use them:

1. A **dictionary** (i.e. a map) is a collection of _key-value pairs_ where:
    - **Key**: Each key is unique i.e. no duplicate keys are allowed.
    - **Value**: Each key maps to exactly one value (not necessarily unique).
2 **Dynamic Size**: Maps grow and shrink as you add or remove items.
3. **Efficient Operations**: In Python dictionaries, operations like insertion, deletion, and lookup are typically O(1) due to a _hash table_ implementation. More on those in a couple of weeks.
4. **Mutable**: Can be modified after creation.
5. Maps in general, insert in a **completely random order**. However, as of Python 3.7, `dict` objects do maintain insertion order.
6. **Operations in the Map ADT**:

    | **Operation**  | **Description**                                                      | **Example Code**    |
    |----------------|----------------------------------------------------------------------|---------------------|
    | `m = Map()`    | Creates an empty map.                                                | `m = {}`            |
    | `m[k] = v`     | Adds or updates a value `v` with key `k`.                            | `m['a'] = 10`       |
    | `m[k]`         | Retrieves the value associated with key `k`. Raises `KeyError` if the key is not found. | `value = m['a']`   |
    | `del m[k]`     | Removes the key-value pair with key `k`. Raises `KeyError` if the key is not found.     | `del m['a']`       |
    | `len(m)`       | Returns the number of key-value pairs in the map.                    | `len(m)`            |
    | `iter(m)`      | Returns an iterator over the keys of the map. Can be used in a loop to iterate through all keys. | `for key in m:` |

    <sub>**Figure 1**: Classic operations belonging to a Map.</sub>

    This might look as follows in Python using as an example of the only k-pop group that matters:

    1. Creating an empty map:

        ```Python
        red_velvet = {}
        print(red_velvet)  # prints {}
        ```

    2. Adding key-value pairs:

        ```Python
        red_velvet["Irene"] = "Leader"
        red_velvet["Seulgi"] = "Dancer"
        red_velvet["Wendy"] = "Singer"
        red_velvet["Joy"] = "Dancer"
        red_velvet["Yeri"] = "Rapper"

        # prints {'Irene': 'Leader', 'Seulgi': 'Dancer', 'Wendy': 'Singer', 'Joy': 'Dancer', 'Yeri': 'Rapper'}
        print(red_velvet)
        ```

    3. Accessing values:

        ```python
        try:
            key = "Wendy"
            wendy = red_velvet[key]
            print(f"{key} exists!")
            
            key = "Taeyeon"
            taeyeon = red_velvet[key]
            print(f"{key} exists!")
        except KeyError:
            print(f"{key} does not exist!")
        ```

        Output:

        ```
        Wendy exists!
        Taeyeon does not exist!
        ```

    4. Deleting values

        ```Python
        try:
            key = "Wendy"
            del red_velvet[key]
            print(f"{key} removed!")
            
            key = "Taeyeon"
            del red_velvet[key]
            print(f"{key} removed!")
        except KeyError:
            print(f"{key} does not exist!")
        ```

        Output:

        ```
        Wendy removed!
        Taeyeon does not exist!
        ```

    5. Getting size of the map:
    
        ```Python
        print(len(red_velvet))  # prints 4
        ```

    6. Iterating over the keys of the map:

        ```Python
        red_velvet["Wendy"] = "Singer"
        
        for member in red_velvet:
            print(f"Member {member}.\tRole: {red_velvet[member]}")
        ```

        Output:

        ```
        Member Irene.   Role: Leader
        Member Seulgi.  Role: Dancer
        Member Joy.     Role: Dancer
        Member Yeri.    Role: Rapper
        Member Wendy.   Role: Singer
        ```

7. **Runtime of Map operations**: As explained above, our goal is to average out a constant time on our map operations. This is mostly possible, although as we'll see later, there are a couple of situations where this is not possible. In general, we have the following:

    | **Operation**          | **Average Case** | **Worst Case**  |
    |------------------------|------------------|-----------------|
    | Insertion (`m[k] = v`) | Θ(1)             | O(`n`)          |
    | Lookup (`m[k]`)        | Θ(1)             | O(`n`)          |
    | Deletion (`del m[k]`)  | Θ(1)             | O(`n`)          |
    | Size Query (`len(m)`)  | Θ(1)             | O(1)            |
    | Iteration (`iter(m)`)  | Θ(`n`)           | O(`n`)          |

    <sub>**Figure 2**: Runtimes of classic Map operations.</sub>

<br>

<a id="2"></a>

## Implementations

We know now that python dictionaries utilise something called a _hash table_ in their implementation in order to make their operations lightning quick (constant). We're not looking at those until a couple of weeks later, but we can start preparing for it by looking at other (less efficient) ways of implementing a map. The reason we'll be doing this is not only to practice using the syntax of map operations, but also because one of these implementations will be later used _as part of_ our hash map-based implementation.

Let's start with that one.

<a id="2-1"></a>

### `UnsortedArrayMap`

Like the name implies, the `UnsortedArrayMap` implementation makes use of an `ArrayList` in order to store, look up, insert, and delete key-value pairs. Each pair in the `UnsortedArrayMap` will be represented by an `Item` object, which is implemented as follows:

```python
class UnsortedArrayMap:
    class Item:
        def __init__(self, key, value=None):
            self.key = key
            self.value = value

    def __init__(self):
        self.table = ArrayList()
```

<a id="2-1-1"></a>

#### Insertion

Our primary goal here is to make the syntax of our `UnsortedArrayMap` look as follows:

```python
red_velvet = UnsortedArrayMap()

red_velvet["Irene"] = "Leader"
```

In order to do this, we have to tap into a new dunder method: **`__set_item__`**. Staying true to arrays, insertion will take the form of appending:

```python
    def __setitem__(self, key, value):
        # first, check if the key already exists in the array
        for item in self.table:
            # if it does, simply replace that item's value to the new value
            if key == item.key:
                item.value = value
                return
        
        # but if it doesn't, create a new Item object and add it
        self.table.append(UnsortedArrayMap.Item(key, value))
```

This will naturally give us _linear runtime_ (Θ(`n`)).

<a id="2-1-2"></a>

#### Lookup / Finding

In order to achieve the following syntax:

```python
print(red_velvet["Joy"])
```

we do something very similar to what we did in insertion. This time, we use the **`__get_item__`** dunder method, taking care of raising an exception if the queried key doesn't exist:

```python
    def __getitem__(self, key):
        # search the entire array for an item with the desired key
        for item in self.table:
            # if we find it, return its value
            if key == item.key:
                return item.value
            
        # if we didn't, raise an error
        raise KeyError("Key Error: " + str(key))
```

Once more, this is a linear operation.

<a id="2-1-2"></a>

#### Deletion

Finally, in order to delete keys with the following syntax:

```python
del red_velvet["Seulgi"]
```

we do the following:

```python
    def __delitem__(self, key):
        # search for the desired key using indexing
        for j in range(len(self.table)):
            # which we'll use with the pop method if found
            if key == self.table[j].key:
                self.table.pop(j)
                return
            
        # otherwise, raise an error
        raise KeyError("Key Error: " + str(key))
```

<a id="2-2"></a>

### Other Implementations

If we tried using other familiar data structures—like a linked list—for our map, we’d still face similar **linear runtimes** overall. Sorting the elements could help for faster lookups, but **insert** and **delete** would remain **O(n)**, since shifting or relinking is always involved. Here’s how that stacks up:

| **Map Implementation**     | **Find**    | **Insert**   | **Delete**   |
|----------------------------|-------------|-------------|-------------|
| **UnsortedArrayMap**       | Θ(`n`)        | Θ(`n`)        | Θ(`n`)        |
| **UnsortedLinkedListMap**  | Θ(`n`)        | Θ(`n`)        | Θ(`n`)        |
| **SortedArrayMap**         | Θ(log(`n`))   | Θ(`n`)        | Θ(`n`)        |
| **SortedLinkedListMap**    | Θ(`n`)        | Θ(`n`)        | Θ(`n`)        |
| **BinarySearchTreeMap**    | *(Coming soon!)* | *(Coming soon!)* | *(Coming soon!)* |

<sub>**Figure 3**: Data Structures for Map ADT.</sub>

But could we do better? Python’s built-in dictionaries somehow manage very efficient runtimes—even better than the **log(n)** solutions. In the next lessons, we’ll see how **binary trees** can already improve these results, and eventually explore **hashing** strategies that power Python’s dictionaries to achieve that extra speed.

<br>

<a id="3"></a>

## Addendum: _Map ADT Dunder Methods_

<a id="3-1"></a>

### Arithmetic and Bitwise

| **Common Syntax** | **Special Method Form**                               |
|-------------------|-------------------------------------------------------|
| `a + b`           | `a.__add__(b)`, alternatively `b.__radd__(a)`         |
| `a - b`           | `a.__sub__(b)`, alternatively `b.__rsub__(a)`         |
| `a * b`           | `a.__mul__(b)`, alternatively `b.__rmul__(a)`         |
| `a / b`           | `a.__truediv__(b)`, alternatively `b.__rtruediv__(a)` |
| `a // b`          | `a.__floordiv__(b)`, alternatively `b.__rfloordiv__(a)` |
| `a % b`           | `a.__mod__(b)`, alternatively `b.__rmod__(a)`         |
| `a ** b`          | `a.__pow__(b)`, alternatively `b.__rpow__(a)`         |
| `a << b`          | `a.__lshift__(b)`, alternatively `b.__rlshift__(a)`   |
| `a >> b`          | `a.__rshift__(b)`, alternatively `b.__rrshift__(a)`   |
| `a & b`           | `a.__and__(b)`, alternatively `b.__rand__(a)`         |
| `a ^ b`           | `a.__xor__(b)`, alternatively `b.__rxor__(a)`         |
| `a \| b`          | `a.__or__(b)`, alternatively `b.__ror__(a)`           |
| `a += b`          | `a.__iadd__(b)`                                       |
| `a -= b`          | `a.__isub__(b)`                                       |
| `a *= b`          | `a.__imul__(b)`                                       |
| … (and so on)     | …                                                    |
| `+a`              | `a.__pos__()`                                         |
| `-a`              | `a.__neg__()`                                         |
| `~a`              | `a.__invert__()`                                      |
| `abs(a)`          | `a.__abs__()`                                         |

<a id="3-2"></a>

### Comparisons, Membership, Indexing, and More

| **Common Syntax**  | **Special Method Form**                  |
|--------------------|------------------------------------------|
| `a < b`            | `a.__lt__(b)`                            |
| `a <= b`           | `a.__le__(b)`                            |
| `a > b`            | `a.__gt__(b)`                            |
| `a >= b`           | `a.__ge__(b)`                            |
| `a == b`           | `a.__eq__(b)`                            |
| `a != b`           | `a.__ne__(b)`                            |
| `v in a`           | `a.__contains__(v)`                      |
| `a[k]`             | `a.__getitem__(k)`                       |
| `a[k] = v`         | `a.__setitem__(k, v)`                    |
| `del a[k]`         | `a.__delitem__(k)`                       |
| `a(arg1, arg2, …)` | `a.__call__(arg1, arg2, …)`              |
| `len(a)`           | `a.__len__()`                            |
| `hash(a)`          | `a.__hash__()`                           |
| `iter(a)`          | `a.__iter__()`                           |
| `next(a)`          | `a.__next__()`                           |
| `bool(a)`          | `a.__bool__()`                           |
| `float(a)`         | `a.__float__()`                          |
| `int(a)`           | `a.__int__()`                            |
| `repr(a)`          | `a.__repr__()`                           |
| `reversed(a)`      | `a.__reversed__()`                       |
| `str(a)`           | `a.__str__()`                            |
