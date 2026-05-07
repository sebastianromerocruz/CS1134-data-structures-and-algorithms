<h2 align=center>Week III: <em>Day 1</em></h2>

<h1 align=center>Algorithm Correctness</h1>

<p align=center><strong><em>Song of the day</strong>: <a href="https://youtu.be/8vEahj1dd2E?si=xolYZwJgVFHl8Qtl"><strong><u>Arcturus Beaming</u></strong></a> by The Crane Wives (2024)</em></p>

---

## Sections

1. [**Algorithms And Their Analyses**](#1)
2. [**Testing For Prime Numbers**](#2)
3. [**Runtime Analyses**](#3)

---

<a id="1"></a>

## Algorithms And Their Analyses

Back in the 1930s, Alan Turing low-key changed the world when he created his eponymous [**machine**](https://en.wikipedia.org/wiki/Turing_machine)—that is, a mechanism that can implement any and every algorithm with just a set of inputs and a simple table of rules. The coolest thing about is that this machine is purely _abstract_—it required no specific hardware, let alone software, to work. Despite this simplicity, it was proven to be able to solve _every single computational problem_ possible. How could this possibly be the case?

Well, it helps to define exactly _what_ a computational problem / algorithm actually is. A semi-formal definition of it goes as follows:

> **Algorithm**: A well-defined computational procedure that describes how to transform any given _input_ to its desired _output_.

When we state any such problem we must:

1. Define a set of _legal inputs_, and...
2. Define the _required output_ for each input.

```
              + ————————— +
 input —————> | ALGORITHM | —————> output
              + ————————— +
```

Now, the way that we prove this algorithm will work is by analysing its _correctness_. An algorithm is correct for _every_ valid input if:

1. It terminates (halts) and...
2. It provides the desired output

Makes sense, right? Now, what modern programmers are usually concerned with is with the _performance_ of an algorithm. That is...

- How **long** does it take to execute (time of computation)
- How **much space** it occupies in your computer during execution (usage of either memory or disk storage)

Other things that affect performance are:
- Disk access time, the number of bytes of data, and the number of requests made to the disk.
- The number of processors in your computer (parallelisation)

And many, many more. Now, while we can't do much about the hardware of the machine running our programs, we can certainly design our algorithms towards being _time and space efficient_. In 1114, we didn't really care about performance at all. Now, it is the only thing that matters.

<a id="2"></a>

<br>

## Testing For Prime Numbers

So this has all been kind of abstract, so let's go ahead and do a simple example of algorithm correctness testing—whether or not a number is _prime_ (primality testing). Let us make a formal definition of what it means to be a prime number:

> Let **`num`** be an integer >= 2 (since 2 is the first prime number). We can say that the value `num` is a **prime number** is its only whole number divisors are _1 and itself_.

For example, 13 is a prime number because the only numbers we can divide it by (divisors) are 1 and itself, 13. Any other divisor will result in a fractional number. 12 is not prime because we can calculate a 12 using several combinations of _complimentary divisors_, such as 1, 2, 3, 4, 6, and 12.

```
Complimentary divisors of 12
1 x 12 = 12
2 x 6  = 12
3 x 4  = 12
```

So how can we prove primality?

### Naïve (Brute Force) Version

The first solution that comes to your head is probably to check every single number from 1 to `num` for divisibility using the following algorithm:

```
VERSION 1
---------
1, 2, 3, 4, ..., num
|                 |
+—————————————————+
  consider every
      number
```

```python
def is_prime_naive(num):
    divisor_count = 0

    for curr in range(1, num + 1):
        if num % curr == 0:
            divisor_count += 1
    
    return divisor_count == 2 # that is, only 1 and num
```

<sub>**Code Block 1**: We call this solution "naïve" because it doesn't attempt any sort of optimisation.</sub>

### First Half Version

Might there be a way for us to test primality without considering every single number from 1 to `num`? Well, it doesn't hurt to try. Let's try cutting the amount numbers in half, and see if only checking either the left half or the right half leads also results in the correct solution:

```
VERSION 1
---------
1, 2, 3, 4, ..., num
|                 |
+—————————————————+
  consider every
      number

VERSION 2
---------
1, 2, 3, 4, ..., num / 2, ..., num
|                    |
+————————————————————+
  consider the left
    half of nums
```

```python
def is_prime_left_half(num):
    divisor_count = 0

    for curr in range(1, num // 2 + 1):
        if num % curr == 0:
            divisor_count += 1
    
    return divisor_count == 1 # that is, only 1


def main():
    num = 13
    print(f"{num} is a prime number: {is_prime_left_half(num)}")

    num = 12
    print(f"{num} is a prime number: {is_prime_left_half(num)}")

if __name__ == "__main__":
    main()
```

Output:

```
13 is a prime number: True
12 is a prime number: False
```

It seems to be working, at least for 13 and 12, but can we prove this to be true for _all_ numbers? 

Suppose `num` is not prime at all, but actually composite, i.e. it has a divisor `k` that is not `1` or `num`.

Let's call this divisor **`k`** and place it on the right side of our list so that `k > num/2`.

```
1, 2, 3, 4, ..., num / 2, ..., k, ..., num
|                    |                  |
+————————————————————+——————————————————+
      left half           right half
```

Because `k` divides into `num` evenly, then we know that there has to be a complimentary divisor (like 2 and 3 are complimentary divisors of 6). Let's call this hypothetical complimentary divisor `d`:

```
    num
d = ———
     k
```

Now let's examine the possible value of `d` (i.e. where in the number line it lies). As `k` grows larger, the fraction `num/k` becomes smaller and vice versa. The smallest value `k` can take in order to be an integer on the right half is `num / 2 + 1`, right?

If this is the case, we can substitute `k` with `num / 2` as our "lower limit". This means that `d` has to be a number of the left side because:

1. `d = num / k` gets smaller as `k` gets larger.
2. The smallest `k` in the right half is `num / 2`, and at this point `d = 2`, which is on the left half.
3. As `k` increases further, `d` gets even smaller, always staying in the left half.

If `k`<sub>min</sub> is `num / 2 + 1`, this leads us to the following inequality:

```
    num      num
d = ——— < —————————
     k    (num / 2)
```

We can simplify this inequality a little further:

```
    num     2 * num
d = ——— < ————————————
     k        num
```

```
    num
d = ——— < 2
     k
```

We thus get the `d` has to be less that 2...meaning it _has to be 1_; there's no other choice. So, if:

```
num
——— = 1
 k
```

Then solving for `k` gives us `num`. The shows that **the only value for `k` (divisor) in the right half _has to be_ `num` itself**. That's the very definition of a prime number. 

Dividing the numbers by half works! This is a great optimisation. For large datasets, cutting the amount of operations by half is huge. We might be satisfied with this result but, could we potentially cut this set of numbers even more?

### Square Root Version

Suppose instead of cutting this set by half we cut it even earlier. How about the square-root of `num`. Why not?

```
VERSION 1
---------
1, 2, 3, 4, ..., num
|                 |
+—————————————————+
  consider every
      number

VERSION 2
---------
1, 2, 3, 4, ..., num / 2, ..., num
|                    |
+————————————————————+
  consider the left
    half of nums

VERSION 3
---------
1, 2, 3, 4, ..., √num, ..., num / 2, ..., num
|                  |
+——————————————————+
   from 1 to √num
```

```python
def is_prime_left_half(num):
    divisor_count = 0

    for curr in range(1, sqrt(num) + 1):
        if num % curr == 0:
            divisor_count += 1
    
    return divisor_count == 1 # that is, only 1
```

Okay, well, let's split these two groups again, getting a left side (smaller) and a right side (larger):

```
1, 2, 3, 4, ... √num, .............................................., num
|                 |          k and d are somewhere in here           |
+—————————————————+——————————————————————————————————————————————————+
     left side                        right side
```

Let's assume that `k` and `d` are complimentary divisors of `num` again. Another way of proving things in mathematics is by something called _contradiction_—that is, if we can prove that `not a` is false, then `a` is true.

In this case, if we suppose that there are values over `√num` for `k` and `d` that result in complimentary divisors of `num`, then we could prove that method 3 doesn't work, since we will have to have checked numbers _over_ `√num`. So, if `k > √num` and `d > √num`, then...

```
k * d = num             k * d > √num * √num
      |                       |
      +———————————+———————————+
                  |
                  v
        num = k * d > √num * √num
```

...wait, though. Doesn't this lead to something weird?

```
num > √num * √num
    |
    v
num > num
```

That's logically not true, meaning that we now have a contradiction! Hence our assumption is false: at least one member of every divisor pair must be ≤ √`num`.

In other words, if a divisor ≤ √`num` exists, the loop will find it and correctly report it as a composite number (i.e. not prime). However, ff the loop finishes without finding any divisor, no divisor can exist at all (otherwise its partner would have been ≤ √`num`). The only remaining divisors are 1 and `num` itself, so `num` is prime.

We were able to cut the data set, and therefore the algorithm **runtime**, even more!

<a id="3"></a>

<br>

## Runtime Analysis

### Analysing The Runtime of Algorithms

So we know that there are ways to optimise programs. In computer science, we have this measure for analysing the runtime of an algorithm based on the size of the input. So, in our case, primality testing has a runtime based on the size of the data set (i.e. 1 to `num`). In this sense, we could say that we're analysing the runtime as a function like this:

```
T(num), where T stands for runtime
```

In computer science this "size" measure is modelled after the random access memory (RAM) model of computation—that is, any value that occupies constant storage and can be read and/or written in constant time (that is, it never changes regardless of how many times we do it). Examples of operations that execute in constant time are mathematical operations, such as `+`, `-`, `*`, `/`, `sqrt`, `lower`, `upper`, etc.)

Since we can't measure runtime analysis for every single possible input, we sort of generalise by finding instead the order of growth of `T(n)`. In other words, we:

> Find the **asymptotic** order of the number of primitive operations executed by an algorithm as a _function of its input size_.

### Runtime Analysis Based on Input Size

Let's rename `num` to `n`, to generalise it. Let's take our primality testing algorithm:

```python
def is_prime_naive(n):
    divisor_count = 0  # runtime of, say, 4

    for curr in range(1, n + 1):
        # runtime of, say, 5
        if n % curr == 0:
            divisor_count += 1 
    
    return divisor_count == 2  # runtime of 2
```

Note the comments above, denoting that `divisor_count` takes a constant runtime of 4 (I completely made up this number. As long as it's constant, it works). Say that the inside of the `for`-loop takes a constant runtime of 5, and `return divisor_count == 2` takes a runtime of, say, 2. We can thus define this hypothetical runtime (`T(n)`) as follows:

> T<sub>naïve</sub>(n) = 4 + (Σ(`i` = 1 to `n`) 5) + 2 = **5n + 6**

For our `num / 2` algorithm, the runtime formula would instead be:

> T<sub>half</sub>(n) = 4 + (Σ(`i` = 1 to `n` / 2) 5) + 2 = 5(n / 2) + 6 = **5n / 2 + 6**

And for our `√num` algorithm, the runtime formula would be:

> T<sub>sqrt</sub>(n) = 4 + (Σ(`i` = 1 to √`n`) 5) + 2 = **5√n + 6**

Make sense? So, for asymptotic analysis, we're interested in finding how the runtime (`T(n)`) grows as `n` gets really really large. Say that `n`, for example, equalled 1,000, 1,000,000, and 1,000,000,000:

> T<sub>naïve</sub>(n) = 5(1,000,000) + 6 = **5,000,006**
>
> T<sub>half</sub>(n) = 5(1,000,000) / 2 + 6 = **2,500,006**
>
> T<sub>sqrt</sub>(n) = 5(√1,000,000) + 6 = 5(1,000) + 6 = **5,006**

As `n` grows larger and larger, the value of the constant stops mattering at all. So, in asymptotic analysis, we always drop the low-order terms. Morover, we also ignore the leading constants of the highest-order term:

> T<sub>naïve</sub>(n) = 5n + 6 ≅ n
>
> T<sub>half</sub>(n) = 5n / 2 + 6 = (5 / 2)n + 6 ≅ n
>
> T<sub>sqrt</sub>(n) = 5√n + 6 ≅ √n

To formally express this computer science, we use something called **big-theta** notation:

> T<sub>naïve</sub>(n) has a **Θ(n)** runtime.
>
> T<sub>half</sub>(n) has a **Θ(n)** runtime.
>
> T<sub>sqrt</sub>(n) has a **Θ(√n)** runtime.