# **Solutions**
## **Problem 1: Appending to a List**
### **Solution:**

1. **Worst-case runtime of `.append(i)`**  
   - When the list runs out of capacity, Python **doubles its size** and copies all elements, taking **Θ(n)** in rare cases.

2. **Best-case runtime of `.append(i)`**  
   - If there’s available space, inserting a new element takes **Θ(1)**.

3. **Total runtime of the loop**  
   - Most `.append(i)` calls take **Θ(1)** time.
   - Only a few calls take **Θ(n)** when the array resizes.

4. **Amortized runtime of `.append(i)`**  
   - Over `n` iterations, the expensive resizing happens **log(n)** times.
   - Using **amortized analysis**, the **average cost** of each `.append(i)` is:
     > **Θ(1) amortized**  

---

## **Problem 2: Removing Elements from a List**
### **Solution:**
1. **Worst-case runtime of `.pop()`**  
   - Python lists support **constant-time `.pop()`** when removing from the end, so **Θ(1)** in all cases.

2. **Best-case runtime of `.pop()`**  
   - Also **Θ(1)** because removing from the end is always direct.

3. **Total runtime of the loop**  
   - The loop runs `n` times, each time calling `.pop()`, so the total runtime is:
     > **Θ(n)**

4. **Amortized runtime of each `.pop()`**  
   - Since each `.pop()` is **always Θ(1)**, there’s no additional cost from resizing.
   - **Amortized time per `.pop()`** remains:
     > **Θ(1) amortized**

Unlike `.append()`, **popping from the end does not require resizing**, so its amortized cost is always **Θ(1)**.

---

## **Problem 3: String Concatenation in a Loop**
### **Solution:**
1. **Worst-case runtime of `s += str(i)`**  
   - Strings are **immutable** in Python, so every `s += str(i)` creates a **new string** and copies all previous characters.
   - This takes **Θ(i)** time at iteration `i`.

2. **Best-case runtime of `s += str(i)`**  
   - There’s no best case since every iteration always creates a new string.

3. **Total runtime of the loop**  
   - The loop runs `n` times, with increasing costs:
     ```
     Θ(1) + Θ(2) + Θ(3) + ... + Θ(n) = Θ(n²)
     ```
   - This follows the **sum of first n natural numbers**, which is **Θ(n²)**.

4. **Amortized runtime of each string concatenation**  
   - Since the total cost across `n` iterations is **Θ(n²)**, the **average cost per iteration** is:
     > **Θ(n) amortized**  
   - This means string concatenation **gets more expensive as `n` grows**, making this approach **very inefficient**.

String concatenation in Python is slow because every `+=` creates a new copy of the string.

---

| Problem | Worst-Case | Best-Case | Total Runtime | Amortized Cost |
|---------|------------|------------|----------------|-----------------|
| **List Appends** | Θ(n) (when resizing) | Θ(1) | Θ(n) | **Θ(1)** |
| **List Pops** | Θ(1) | Θ(1) | Θ(n) | **Θ(1)** |
| **String Concatenation** | Θ(i) per iteration | - | Θ(n²) | **Θ(n)** |