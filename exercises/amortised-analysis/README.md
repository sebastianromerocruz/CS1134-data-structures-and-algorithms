# **Amortized Runtime Analysis**

## **Instructions**
For each program, analyze the **worst-case**, **best-case**, and **amortized runtime** of the operations performed.

---

## **Problem 1: Appending to a List**
Consider the following Python function:

```python
def build_list(n):
    lst = []
    for i in range(n):
        lst.append(i)
    return lst
```

1. What is the **worst-case runtime** of a single `.append(i)`?
2. What is the **best-case runtime** of a single `.append(i)`?
3. What is the **total runtime** of the _loop_?
4. What is the **amortized runtime** of each `.append(i)` call?

---

## **Problem 2: Removing Elements from a List**
Consider the following Python function:

```python
def remove_elements(lst):
    while len(lst) > 0:
        lst.pop()
```

1. What is the **worst-case runtime** of a single `.pop()`?
2. What is the **best-case runtime** of a single `.pop()`?
3. What is the **total runtime** of the _loop_?
4. What is the **amortized runtime** of each `.pop()` call?

---

## **Problem 3: String Concatenation in a Loop**
Consider the following Python function:

```python
def concat_string(n):
    s = ""
    for i in range(n):
        s += str(i)
    return s
```

1. What is the **worst-case runtime** of `s += str(i)`?
2. What is the **best-case runtime** of `s += str(i)`?
3. What is the **total runtime** of the _loop_?
4. What is the **amortized runtime** of each string concatenation?