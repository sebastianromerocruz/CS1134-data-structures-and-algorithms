## **Runtime Complexity Analysis**

Analyse the runtime of three Python functions. For each function:

1. **Determine its overall asymptotic complexity (Θ notation).**
2. **Break down the complexity of each operation.**
3. **Explain why the total runtime follows the given complexity.**

---

### **Problem 1:**
This function counts how many even numbers are in the list.

```python
def count_evens(lst):
    count = 0

    for num in lst:
        if num % 2 == 0:
            count += 1

    return count
```

---

### **Problem 2**
This function builds a list by checking if each number is already present before appending.

```python
def unique_append(n):
    result = []

    for i in range(n):
        if i in result:
            continue
        result.append(i)

    return result
```

---

### **Problem 3**
This function reduces the size of `n` by half in each step.

```python
def reduce_by_half(lst):
    n = len(lst)
    count = 0

    while n > 1:
        n = n // 2
        count += 1

    return count
```

---

[***Solutions***](SOLUTIONS.md)