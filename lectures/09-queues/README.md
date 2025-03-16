
<h2 align=center>Week 09</h2>

<h1 align=center>Abstract Data Types: <em>Queues</em></h1>

<p align=center><strong><em>Song of the day</strong></em>: <em><a href="https://youtu.be/7Tln_B11HgQ?si=QIAzJd2zFSMHg8Ms"><strong><u>Lesson Learnt (Live at COLORS)</u></strong></a> by Aaron Taylor (2017)</em></p>

---

## Sections

1. [**Queue ADT**](#1)
2. [**Queue Implementations**](#2)
   1. [**Dynamic Queue**](#2-1)
   2. [**Static Queue**](#2-2)
3. [**Queue Implementation Models**](#3)
4. [**Python Implementation**](#4)
   1. [**Static**](#4-1)
   2. [**Dynamic**](#4-2)

---

<a id="1"></a>

## **Queue ADT**

Next on our list of ADTs is the **queue**. Just forming a line to enter, say, an event or a restaurant, a queue is a data structure that maintains items in a **FIFO** order (First-In, First-Out). The earliest enqueued element is always the first one dequeued, or "popped". Its operations are as follow:

| **Operation**         | **Description**                                                                                  |
|-----------------------|--------------------------------------------------------------------------------------------------|
| `q = Queue()`         | Creates an empty queue                                                                           |
| `len(q)`              | Returns the number of items in `q`                                                               |
| `q.is_empty()`        | Returns `True` if `q` is empty, `False` otherwise                                               |
| `q.enqueue(item)`     | Adds `item` to the **end** of the queue                                                         |
| `q.dequeue()`         | Removes and returns the **front** item (the earliest enqueued); raises exception if empty        |
| `q.first()`           | Returns the **front** item without removing it; raises exception if empty                       |

<sub>**Figure 1**: The general queue operations we are to implement.</sub>

Just like with stacks, lists can provide some of this functionality, but certainly not all and not with the flexibility that we are after.

<br>

<a id="2"></a>

## **Queue Implementations**

Also just like stacks, we can implement a queue in two main ways: a **dynamic** one with no preset size limit, and a **static** one with a maximum capacity.

<a id="2-1"></a>

### **Dynamic Queue**

A **dynamic queue** expands memory usage as needed. It has no size limitation and can accommodate more data automatically. We, thus, have no need to check if our queue is full. Think of this as the queue to get into literally any NYU career fair:

| Operation       | Description                                                       |Time Complexity Goal (Amortised)|
|----------------|------------------------------------------------------------------|-|
| `q = Queue()`   | Creates an empty, dynamically sizable queue                      |Θ(1)|
| `enqueue(item)` | Adds `item` to the queue end                                    |Θ(1)|
| `dequeue()`     | Removes the earliest enqueued item and returns it               |Θ(1)|
| `first()`       | Returns the front item without removing it                      |Θ(1)|
| `len(q)`        | Returns the number of items in `q`                              |Θ(1)|
| `q.is_empty()`  | Checks if `q` has no items (returns True/False)                 |Θ(1)|

<sub>**Figure 2**: Methods of a dynamic queue alongside our target time complexities.</sub>

<a id="2-2"></a>

### **Static Queue**

A **static queue** uses a **fixed size** array and will raise an exception if it becomes full. For this, of course, we need an additional method.

| Operation             | Description                                                                              |Time Complexity Goal (Amortised)|
|-----------------------|------------------------------------------------------------------------------------------|-|
| `q = Queue(max_cap)`  | Creates an empty queue with capacity `max_cap`                                           |Θ(1)|
| `enqueue(item)`       | Adds `item` to the queue end, or raises exception if full                               |Θ(1)|
| `dequeue()`           | Removes and returns the earliest enqueued item, or raises exception if empty             |Θ(1)|
| `first()`             | Returns the front item without removing it, or raises exception if empty                |Θ(1)|
| `is_full()`           | Returns `True` if the queue is at max capacity, `False` otherwise                       |Θ(1)|
| `len(q)`              | Returns the number of items in `q`                                                      |Θ(1)|
| `q.is_empty()`        | Checks if `q` has no items (returns True/False)                                         |Θ(1)|

<sub>**Figure 3**: Methods of a static queue alongside our target time complexities.</sub>

Now, implementing these runtimes with stacks was relatively simple; under LIFO, `pop()` does not have to do much in order to remove an element from neither dynamic nor a static stack. Queues, however, are a little more complicated since we are removing the _first element_ when were dequeue. This introduces the key question when considering queues: _when we remove an element from the queue, **what happens to the rest of the elements?**_

Do they all shift one index to the left towards the "front" of the queue, or does index 1 become the new front of the queue? Can we achieve a constant runtime under both of those implementations? Well, let's look at an example of a queue to illustrate this.

<br>

<a id="3"></a>

## **Queue Implementation Models**

Consider the following queue in memory:

```python
q = Queue()
q.enqueue(2)
q.enqueue(4)
q.enqueue(6)
q.enqueue(8)

print(q.dequeue())  # -> 2
# Now queue has [4, 6, 8] (front is 4)
```

<a id="3-1"></a>

### Traditional Model

In this implementation `dequeue` requires shifting items so the new front is at index 0. This is more akin to a queue in real life. However, just like dequeuing in real life, this requires every single person in the queue to move a step forward, which is quite a bit of work. Indeed, the cost of implementing this is Θ(`n`), since we must recopy each element in the queue over again, just one step to the left:

![traditional](assets/traditional.png)

<sub>**Figure 4**: Clearly, we're not meeting our Θ(1) amortised runtime goal like this.</sub>

<a id="3-2"></a>

### Circular Model

The solution to this is to think in relative terms. Instead of making everybody in the line move one step forward, why not move the start of the queue one step back? We call this the circular model. This way, we can track the front and end positions (using pointers) without shifting every item. Finding the index of the next enqueued item is super easy, too, using the following formula (which is, itself, constant time):

> index<sub>(`front` + 1)</sub> = (index<sub>`front`</sub> + 1) % `capacity`

This way, doing the following:

```python
q.enqueue(1)
q.enqueue(0)
q.enqueue(7)
```

Would result in the following:

![circular](assets/circular.png)

<sub>**Figure 5**: As users of this queue, we can't really tell the difference, as we don't see what's actually going on in memory, but the runtime has now constant as opposed to linear.</sub>

Using an `ArrayList`, we might be looking at something like this in memory:

![queues-mem-1](assets/queues-mem-1.png)

<sub>**Figure 6**: Memory map is a dynamic `ArrayQueue`.</sub>

Here, the circular model is being implemented using the aforementioned index modulus strategy:

![queues-mem-2](assets/queues-mem-2.png)

<sub>**Figure 7**: In yellow, you can see how modulus perfectly "circulates" our queue positions as we add more elements.</sub>

A question remains in this situation, though: what about resizing? The circular model is great for solving the question of dequeuing—and enqueuing in the case of a static queue—but we have to come up with some appropriate method for our dynamic queue, which the `ArrayList`'s `resize()` method doesn't solve for us.

<br>

For example, we could approach resizing in the following way:

```python
q = Queue()

q.enqueue(2)
q.enqueue(4)
q.enqueue(6)
q.enqueue(8)

q.dequeue()  # 2
q.dequeue()  # 4
q.dequeue()  # 6

q.enqueue(10)
q.enqueue(12)
```

We could also this in the following way, creating a gap between the front of the line:

![queue-resize-2](assets/queue-resize-2.png)

<sub>**Figure 8**: A "gap-creating" approach.</sub>

![queue-resize-1](assets/queue-resize-1.png)

<sub>**Figure 10**: A "common-sense" approach.</sub>

The second approach might seem wasteful compared to just appending more space after the end of the queue—after all, we do want to avoid that Θ(`n`) left-shift that it involves, but it turns out that it doesn't really matter. Remember that resizing doesn't happen very often at all compared to the amount of times that we enqueue and dequeue, so the amortised runtime would be Θ(1) anyway.

Let's check out the Python implementations for both the static and dynamic queues.

<br>

<a id="4"></a>

## Python Implementation

<a id="4-1"></a>

### Static

```python
class StaticArrayQueue:
   def __init__(self, max_cap):
      self.data_arr = make_array(max_cap)
      self.capacity = max_cap
      self.n = 0
      self.front_ind = None

   def __len__(self):
      return self.n

   def is_empty(self):
      return len(self) == 0

   def is_full(self):
      return self.n == self.capacity

   def enqueue(self, item):
      if self.is_full():
         raise Exception("Queue is full")
      elif self.is_empty():
         self.data_arr[0] = item
         self.front_ind = 0
         self.n += 1
      else:
         back_ind = (self.front_ind + self.n) % self.capacity
         self.data_arr[back_ind] = item
         self.n += 1

   def dequeue(self):
      if self.is_empty():
         raise Exception("Queue is empty")
      
      value = self.data_arr[self.front_ind]
      self.data_arr[self.front_ind] = None
      self.front_ind = (self.front_ind + 1) % self.capacity
      self.n -= 1
      
      if self.is_empty():
         self.front_ind = None

      return value

   def first(self):
      if self.is_empty():
         raise Exception("Queue is empty")
      
      return self.data_arr[self.front_ind]
```

### Dynamic

<a id="4-2"></a>

```python
class ArrayQueue:
    INITIAL_CAPACITY = 8  # static constant

    def __init__(self):
        self.data_arr = make_array(ArrayQueue.INITIAL_CAPACITY)
        self.capacity = ArrayQueue.INITIAL_CAPACITY
        self.n = 0
        self.front_ind = None

    def is_empty(self):
        return len(self) == 0
    
    def resize(self, new_cap):
        new_data = make_array(new_cap)
        old_ind = self.front_ind
        
        for new_ind in range(self.n):
            new_data[new_ind] = self.data_arr[old_ind]
            old_ind = (old_ind + 1) % self.capacity
            
        self.data_arr = new_data
        self.capacity = new_cap
        self.front_ind = 0

    def enqueue(self, elem):
        if self.n == self.capacity:
            self.resize(2 * self.capacity)
        if self.is_empty():
            self.data_arr[0] = elem
            self.front_ind = 0
            self.n += 1
        else:
            back_ind = (self.front_ind + self.n) % self.capacity
            self.data_arr[back_ind] = elem
            self.n += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        
        value = self.data_arr[self.front_ind]
        self.data_arr[self.front_ind] = None
        self.front_ind = (self.front_ind + 1) % self.capacity
        self.n -= 1
        
        if self.is_empty():
            self.front_ind = None
            
        if self.n < self.capacity // 4 and self.capacity > ArrayQueue.INITIAL_CAPACITY:
            self.resize(self.capacity // 2)
            
        return value

    def first(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        
        return self.data_arr[self.front_ind]

    def __len__(self):
        return self.n
```

Once more, resizing works as follows: it changes the underlying array’s size to `new_cap`, then repositions the queue’s elements into the new array **in proper order**, starting at index `0`.

1. Creation of a New Array (`new_data`):
   - We allocate a new array (`new_cap` in size) using `make_array`.
   - This bigger (or smaller) array will hold the elements of our queue.

2. Copying Existing Elements in Proper Order:
   - We set `old_ind = self.front_ind` to begin reading from the queue’s current front.  
   - In a loop of `self.n` iterations (the number of items in the queue), we copy elements from `self.data_arr[old_ind]` into `new_data[new_ind]`.  
   - After each copy, we increment `old_ind` by 1, wrapping around with `% self.capacity` to handle any circular indexing.

3. Reassign Internal Fields:
   - `self.data_arr = new_data`: the queue’s backing array is now the newly created array.  
   - `self.capacity = new_cap`: update capacity.  
   - `self.front_ind = 0`: set the front to index `0`, because we lined them up neatly at the start of `new_data`.