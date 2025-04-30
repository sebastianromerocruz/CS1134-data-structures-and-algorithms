<h2 align=center>Week 14</h2>

<h1 align=center>Abstract Data Types: <em>Hash Maps</em></h1>

<p align=center><strong><em>Song of the day</strong></em>: <em><a href="https://youtu.be/r4G0nbpLySI?si=QsycBKcGoJqhapq-"><strong><u>Wait for the Moment</u></strong></a> by Vulfpeck (2013)</em></p>

---

## Sections

1. [**Maps: _Recap_**](#1)
    - [**Bucket Arrays**](#1-1)
    - [**Hashing**](#1-2)
2. [**Hash Tables**](#2)
    - [**Collisions**](#2-1)
    - [**Hash Functions**](#2-2)
3. [**Coding Functions**](#3)
    - [**Integer Casting**](#3-1)
    - [**Component Sum**](#3-2)
    - [**Polynomial Accumulation**](#3-3)
4. [**Compression Functions**](#4)
    - [**The Division Method**](#4-1)
    - [**The Multiplication-Add-Divide (MAD) Method**](#4-2)

<p align=center><strong><em><a href="assets/Hash Tables.pdf">Handwritten Class Notes</a></em></strong></p>

---

<a id="1"></a>

## Maps: _Recap_

We’ve been using balanced binary search trees—like AVL trees—to speed up our map operations. Thanks to their structure, we can guarantee that lookup, insert, and delete take Θ(log `n`) time. That’s a big improvement over the Θ(`n`) we saw with unsorted lists and arrays. But is log `n` really the best we can do? Is it possible to get even faster? We’ve been cutting the problem in half at each step—binary search style—but what if we could skip the search altogether and jump straight to the spot where the key goes?

This is it, y'all. After a lengthy conversation on various ways of implementing maps, it's time to get our legendary constant runtime. This involves us considering the idea of _direct access_: hhat if we could just compute where a key belongs in constant time, instead of searching for it (through an AVL, for example)? That’s the dream, and where the idea of a **bucket array** comes in.

<a id="1-1"></a>

### Bucket Arrays

Think of a _bucket array_ as this giant list of spots (buckets), and each key is mapped to a particular index in the array using some sort of deterministic (that is, fairly predictable) rule. For example, if I wanted to insert or find the key `"cat"`, I can jump directly to the bucket where it would belong—no searching required.

In this case, we would have no need for comparison-based searching and potential for constant runtime! So, how do we know where a key should go? If we just try to use the key as an index—like `array["cat"]`—that won’t work, since keys like strings or large numbers aren’t valid indices (which need to be _unsigned, or positive, integers_). We need a way to translate keys into valid array indices.

This is where _hashing_ comes into play.

<a id="1-2"></a>

### Hashing

A **hash function** lets us take any kind of key—strings, integers, whatever—and _deterministically convert it into a number_. This process ideally would take any key and match them to individual indices.

A (very, very) simple hashing function might be taking the key's length and using that number as its index. So, the following strings would have the following keys:

<a id="bad-hash"></a>

|`val`|`len(val)`|`key`|
|-----|----------|-----|
|`"cat"`| 3 | 3 |
|`"guitar"`| 6 | 6 |
|`"tar"`| 3 | 3 |
|`range(10)`| 10 | 10 |
|`(1, 2, 3)`| 3 | 3 |

<sub>**Figure 1**: A hash function using the value's length as its basis for hashing.</sub>

As you can see above, sometimes we end up mapping multiple keys to the same index. That’s called a **collision**. With a hash function as simple as `len(val)`, we'd get collision quite often, even for extremely different keys. We're definitely going to have to do better than this. The structure we build to manage these collisions is what gives rise to the **Hash Table**.

A hash table is basically a bucket array with some clever logic behind the scenes:
- A hash function to compute the bucket index.
- A collision strategy to handle overlap.

Thought this way, we get the following space and runtime complexities:

| **Data Structure**           | **Find**        | **Insert**      | **Delete**      | **Space**                           |
|-----------------------------|------------------|------------------|------------------|--------------------------------------|
| **UnsortedArrayMap**        | Θ(`n`)             | Θ(`n`)             | Θ(`n`)             | Θ(`n`)                                 |
| **UnsortedLinkedListMap**   | Θ(`n`)             | Θ(`n`)             | Θ(`n`)             | Θ(`n`)                                 |
| **SortedArrayMap**          | Θ(log(`n`))        | Θ(`n`)             | Θ(`n`)             | Θ(`n`)                                 |
| **SortedLinkedListMap**     | Θ(`n`)             | Θ(`n`)             | Θ(`n`)             | Θ(`n`)                                 |
| **BinarySearchTreeMap**     | Θ(`n`)<br>Also, Θ(`h`) | Θ(`n`)<br>Also, Θ(`h`) | Θ(`n`)<br>Also, Θ(`h`) | Θ(`n`)                                 |
| **AVLTreeMap**              | Θ(log(`n`))        | Θ(log(`n`))        | Θ(log(`n`))        | Θ(`n`)                                 |
| **BucketArray**             | Θ(`1`)             | Θ(`1`)             | Θ(`1`)             | Could be asymptotically larger than `n` |
| **Hash Table**              | Θ(`1`)             | Θ(`1`)             | Θ(`1`)             | Θ(`n`)                                 |

<sub>**Figure 2**: Hello, constant runtime.</sub>

<br>

<a id="2"></a>

## Hash Tables

As with every data structure we cover, we'll start with some definitions:

- **Universe (`U`)**: A [**set**](https://www.splashlearn.com/math-vocabulary/sets#0-what-is-a-set) from which the keys will be taken.
- **Hash Table (`T[0, …, (N-1)]`)**: An array with `N` slots, where entries will be stored.
- **Hash Function (`h(U) → {0, 1, …, (N-1)}`)**: A function that maps keys from the universe to slots in the table (`T`).

![hash-table-1](assets/hash-table-1.png)

<sub>**Figure 3**: Here, each of our keys (e.g. `k`<sub>1</sub>, `k`<sub>2</sub>, `k`<sub>3</sub>, etc.) in our universe `U` is passed through some undefined hash function `h` to determine their respective indices.</sub>

<br>

<a id="2-1"></a>

### Collisions

Say, under this hash function `h`, the key of `k`<sub>4</sub> would be hashed to the index of `2`. This would lead to a collision with `k`<sub>2</sub>, which also hashed to index `2`. As explained earlier, this would lead to a **collision**.

There are multiple ways to handle collisions, but one of the simplest solutions is by doing something called **chaining**: storing all entries that are mapped to the same slot in some other, secondary collection (like an array or a linked list):

![hash-table-collision](assets/hash-table-collision.png)

<sub>**Figure 4**: Chaining `k`<sub>4</sub> after it hashed to the same index as `k`<sub>2</sub>.</sub>

Now, the problem with this approach is that, if lots of keys hash out to the same index (like with [**our first attempt at a hash function**](#bad-hash)), a lot of keys could end up being stored at the same slot, leading to bad performance. The solution to this would be, naturally, a really good hashing function. Ideally, we would like keys, regardless of their similarity, to never map to the same index, but since hash functions are _deterministic_, this is nigh impossible.

Instead we'd like a function that would, at the very least, _uniformly distribute_ these indices, which is definitely doable. So, how would such a function work?

<a id="2-2"></a>

### Hash Functions

A **uniform hashing function** is formally defined as:

> A function that when given a randomly chosen key, it will be equally likely mapped to any of the `N` slots of `T`, independently of where any other key has hashed to.

Typically, we say that there are two portions to the hashing process (`h`):

<a id="hashing-parts"></a>

1. **A coding function (`h`<sub>1</sub>)**: a (constant-time) process that transforms a key (like a string, number, or object) into an integer. Its goal is to take any kind of input and give you a (possibly large) number that represents it uniquely and consistently.
    Python has a function called `hash` that does this for you (although we'll be creating our own later):
    ```python
    hash("cat")  # might return something like 9873452010298
    ```

2. **A compression function (`h`<sub>2</sub>)**: Since the numbers coming out of the coding function can be quite large (usually a 64-bit number), this second function takes that big integer produced by the coding function and shrinks it down into a valid index within your bucket array.
    This is because our hash table might only have, say, a `capacity` number slots (i.e. indices `0`, `1`, `2`, ..., `capacity - 1`). A typical number returned by a hash function could be as large as, say, `9873452010298`. Because of this, we'd need to _compress_ this number to `0 ≤ index < capacity`.

So, our hashing process would look like this:

> **`h`(`key`) = `h`<sub>2</sub>(`h`<sub>1</sub>(`key`)) = `index`**

![coding-compression](assets/coding-compression.png)

<sub>**Figure 5**: A more detailed process for hashing.</sub>

Let's take a look at a few common coding function approaches.

<br>

<a id="3"></a>

## Coding Functions

<a id="3-1"></a>

### Integer Casting

The first one we'll look at is called integer casting, where we do the following:

1. Look at the binary representation of the key.
2. Take the 8 least significant bytes.
3. Interpret it as a 64-bit 2's complement number


For example, let’s say our key is:

```python
key = "cat"
```

#### Step 1: Look at the Binary Representation

In memory, `"cat"` is stored as a sequence of bytes using **ASCII** encoding:

- `'c'` → 99 → `01100011`
- `'a'` → 97 → `01100001`
- `'t'` → 116 → `01110100`

So the full byte sequence for `"cat"` is:

```
01100011 01100001 01110100
```

Or in hex:  
```
"cat" → 0x636174
```

That’s only 3 bytes—not 8—so we pad with zeros at the front:

```
00000000 00000000 00000000 00000000 00000000 00000000 01100011 01100001 01110100
```

Now we interpret this whole thing as a 64-bit [**two's complement integer**]().

#### Step 2: Interpret as a 64-bit Integer

That binary number corresponds to:

```
0x0000000000636174 = 6501204 (in decimal)
```

So, our **coding function** gives us:

```python
hash_value = 6501204
```

The problem with this approach is that, because we're only looking at the 8 most significant bytes, there is the possibility of the parts being ignored are the parts where keys actually differ. As a result, many distinct keys get mapped to the **same hash value**, which creates **collisions**.

<a id="same-prefix"></a>

For example, imagine you’re building a hash table keyed on **student IDs**, all of which follow this format:

```
"NYU2025-0001"
"NYU2025-0002"
"NYU2025-0003"
...
"NYU2025-0123"
```

Let’s say your integer casting implementation only reads the first 8 bytes (or even worse, just the beginning characters for the hash):

```python
"NYU2025-0001" →  bytes: ['N', 'Y', 'U', '2', '0', '2', '5', '-']
"NYU2025-0002" →  bytes: ['N', 'Y', 'U', '2', '0', '2', '5', '-']
```

That’s _identical_ across all keys — the only changing part is _after_ byte 8!

If your hash function does this:
```python
first_eight = key[:8]  # Only considers "NYU2025-"
hash_val = to_int(first_eight)  # Convert to int from those 8 bytes
```

Then **every single key will produce the same hash**! Let's, then, try something else.

<a id="3-2"></a>

### Component Sum

The component sum approach is defined as follows:

> Break the key into its components: key = (`k`<sub>0</sub>, `k`<sub>1</sub>, `k`<sub>2</sub>, `k`<sub>3</sub>, …, `k`<sub>`m`-1</sub>). The coding function h1 would add all the components of a key. That is: `h1`(`k`) = `k`<sub>0</sub> + `k`<sub>1</sub> + `k`<sub>2</sub> + `k`<sub>3</sub> + … + `k`<sub>`m`-1</sub>

More simply put, we might...

1. Take each byte (or character) of the key,
2. Convert each one into an integer, and then...
3. Add them all together to get a final sum.

For example, let’s take the key:

```python
key = "abc"
```

Using ASCII values:

| Char | ASCII |
|------|--------|
| a    | 97     |
| b    | 98     |
| c    | 99     |

Component sums:
- `"abc"` → 97 + 98 + 99 = **294**

Now, this approach is particularly vulnerable because it **completely ignores the order of a key's components**. For example:

- `"abc"` → 97 + 98 + 99 = **294**
- `"cab"` → 99 + 97 + 98 = **294**
- `"bca"` → 98 + 99 + 97 = **294**

This causes causes high collision rates, especially in datasets where:
  - Key components are reused or permuted,
  - Or where prefixes/suffixes are common (see our [**`NYU2025-` example**](#same-prefix) above).

This goes against our goal of making a good hash function: to distribute keys as evenly and uniquely as possible across buckets.

<a id="3-3"></a>

### Polynomial Accumulation

Polynomial accumulation is defined as follows:

> Let `z` be an integer ≥ 2. To code a `key`, break it into its components so that:
> <p align=center><code>h</code><sub>1</sup>(<code>key</code>) = <code>k</code><sub>0</sub> * <code>z</code><sup>0</sup> + <code>k</code><sub>1</sub> * <code>z</code><sup>1</sup> + <code>k</code><sub>2</sub> * <code>z</code><sup>2</sup> + … + <code>k</code><sub><code>m</code>-1</sub> * <code>z</code><sup><code>m</code>-1</sup></p>

For example, using `"abcd"` as a key:

```python
hash = ord('a') * x³ + ord('b') * x² + ord('c') * x¹ + ord('d') * x⁰
```

Or, mathematically:

```python
hash = Σ[ord(key[i]) * x^(n - 1 - i)] for i from 0 to n-1
```

Let’s walk through hashing the key `"cat"` using base `x = 33`.

1. Get ASCII values:
   - `c` = 99
   - `a` = 97
   - `t` = 116

2. Plug into the polynomial:

```
hash = 99 * 33² + 97 * 33¹ + 116 * 33⁰
     = 99 * 1089 + 97 * 33 + 116 * 1
     = 107811 + 3201 + 116
     = 111128
```

Polynomial accumulation gives _each character a position-based weight_. That’s what makes it better:

- Characters at the beginning of the string (which might often be the same) don’t dominate the outcome.
- Even small differences in character order result in very different hash values.

<br>

<a id="4"></a>

## Compression Functions

Moving on to the next part of our hashing process: the compression function, as we [**mentioned earlier**](#hashing-parts), takes the 64-bit integer produced by the coding functions and reduces them to an acceptable index within our table (`h`[`0`...`N`-1]). We'll start with very simple ones and slowly work our way up to the one we want to use.

<a id="4-1"></a>

### The Division Method

Possibly the most obvious of these is the division method, through which we take the 64-bit number and _mod it by `N` (the size of the table). In other words:

> **`h`<sub>2</sub>(`k`) = `k` mod `N`**

Say, for example, that our table was of size `N=1000`. If we took our earlier key of `"cat"`, from which we got the hash `111128`, and mod it by `N`:

> **`index` = `111128 % 1000` = _128_**

Meaning that `"cat"` would be placed in the 128th bucket of our array.

Now, this compression function is very common because it's easy to implement and, in fact, works pretty uniformly **if the keys are unbiased**. What does this mean? Well, consider the situation where we have an `N=10` and the following keys:

```python
{0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55}
```

Using the division method would yield the following results:

![div-method-col](assets/div-method-col.png)

<sub>**Figure 6**: Oh no, so many collisions!</sub>

In this situation, the keys are biased in the sense that they have similar properties (i.e. divisible by the size of the table, and/or by half of the size of a table), so this results on long chains and bad performance. Ideally, we'd like even keys like this to be able to be distributed evenly, so this might not be ideal in all cases.

If you're set on using the division method, one common heuristic is to **choose `N` (the size of the table) to be a prime number**. This guarantees that divisibility will not be a common issue when distributing your keys across the bucket array:

![div-method-prime](assets/div-method-prime.png)

<sub>**Figure 7**: Oh hey, not so many collisions!</sub>

<a id="4-2"></a>

### The Multiplication-Add-Divide (MAD) Method

The compression method that we'll be using in our implementation is a little more involved, and is known as the **multiplication-add-divide, or MAD, method**. The formal definition goes as follows:

> Let `p` be a prime number such that `p` > |`U`| (i.e. the size of `U`).
> Let `a` be a random number from `1` to `p - 1`.
> Let `b` be a random number from `0` to `p - 1`.
> We thus define: **`h`<sub>2</sub>(`k`) = [(`a` * `k` + `b`) mod `p`] mod `N`**

For example, if |`U`| = `60` and the keys are:

```python
{0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55}
```

Let's choose `p = 101`, `a = 31`, and `b = 6` for a table size of `N = 10`. Thus, our hashing function becomes:

> **`h`<sub>2</sub>(`k`) = [(`31` * `k` + `6`) mod `101`] mod `10`**

![mad](assets/mad.png)

<sub>**Figure 8**: Oh yay, even less collisions!</sub>

Pretty nice, right? Since all of these operations are constant, and indexing is also constant, we've achieved the legendary constant runtime we've been looking for. In the next section, we'll do a proper analysis to prove this.

<br>

<a id="5"></a>

## Runtime Analysis

When we use a hash table, the general idea is simple: apply a hash function to a key, and it tells us which bucket—or slot—in the table to check. If two keys happen to hash to the same slot (a collision), we store both in a **chain**, like a list or linked list, at that bucket.

So what does it actually take to **find** a key?

1. First, compute the hash to figure out which slot to look in.
2. Then, search through the chain in that slot until we find the key (or determine it’s not there).

Now, let’s talk about the **worst case**. Imagine if **every key** hashed to the exact same slot. That would mean one long chain with all `n` elements in it—and searching becomes a linear scan through the entire table. In that case, `find` takes **Θ(`n`)** time, completely negating the advantages of hashing.

But in practice, with a **good hash function**—one that distributes keys uniformly across the table—we expect the keys to be spread out more evenly. This means most chains stay short, and we get much better performance.

To describe this more precisely, we introduce the **load factor**, denoted by `α`:

```
α = n / N
```

Where:
- `n` is the number of keys in the table
- `N` is the number of buckets

So `α` is the **average number of elements per chain**. If we have 100 keys and 100 buckets, then `α = 1`, meaning we expect one key per chain on average.

With this in mind, the expected time to `find` a key breaks down like this:

1. **O(1)**: Compute the hash and jump directly to the correct slot.
2. **O(α)**: Scan through the chain in that slot.

This gives us a total expected time of:

```
O(1 + α)
```

Now, here’s the good news: as long as we **maintain `α` ≤ 1**—by resizing the table when it gets too full—we keep the chains short, and the runtime stays close to constant:

```
O(1 + α) → O(1 + 1) → O(2) → Θ(1)
```

That’s why **dynamic resizing** is so critical in a hash table: it keeps the number of buckets proportional to the number of elements, which in turn keeps our operations efficient. When done right, finding a key in a hash table is—on average—**constant time**.

---

Let’s wrap up with a few important implementation details when building our hash table.

- **When it comes to generating the hash, we’ll lean on Python’s built-in `hash()` function**. It’s fast, flexible, and works on all sorts of key types—strings, numbers, even tuples. But remember: the number it gives us might be huge (or even negative), and our goal is to map that value into a much smaller, non-negative range—the indices of our array.

- That’s where the **compression function** comes in. Specifically, we will use the **MAD method**. The idea is to scramble the output of `hash()` a bit further before finally taking modulo `N` to land somewhere within our table. This extra step helps spread things out more evenly and avoids some of the patterns and clustering you can get if you just use a basic modulo.

- Now of course, collisions are inevitable. At some point, two different keys will end up in the same slot. When that happens, we don’t overwrite—we **chain**. That means each slot of our table isn’t just a single value; it’s actually a tiny map of its own, where we can store multiple entries. For this secondary structure, **we use an `UnsortedArrayMap`**. It’s lightweight, simple, and works great when the number of items per bucket is small—as it should be.

- To keep our performance solid, we need to manage the table’s **load factor**, which is just the ratio of the number of stored items `n` to the total number of slots `N`. As long as we make sure `n` doesn’t exceed `N`—and ideally stays comfortably below—we’re in good shape. Chains stay short, and our lookups, inserts, and deletes stay fast.

That’s the key to a good hash table: a solid hashing process, smart collision handling, and careful attention to load.