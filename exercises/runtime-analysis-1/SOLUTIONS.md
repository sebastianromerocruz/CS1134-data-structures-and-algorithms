## **Solutions**

### **Solution 1: _Linear Complexity (Θ(`n`))_**
- `count = 0` → **Θ(1)**
- **Loop runs `n` times**:
  - Checking `num % 2 == 0` → **Θ(1)**
  - Incrementing `count` → **Θ(1)**
- `return count` → **Θ(1)**.

#### **Total Cost:**
- The loop runs **`n`** times, each doing **Θ(1)** work.
- **Final Complexity: Θ(`n`).**

---

### **Solution 2: _Quadratic Complexity (Θ(`n`²))_**
- `result = []` → **Θ(1)**
- **Loop runs `n` times**:
  - **`if i in result`**:
    - Searching in a list takes **Θ(i)** time (worst case, since the list grows over time).
  - **`result.append(i)`** → **Θ(1)**.

#### **Total Cost:**
- The `if i in result` check starts fast but slows down as `result` grows:
  ```
  Θ(0) + Θ(1) + Θ(2) + ... + Θ(`n` - 1) = Θ(`n`²)
  ```
- **Final Complexity: Θ(`n`²).**

---

### **Solution 3: _Logarithmic Complexity (Θ(log `n`))_**
- `len(lst)` → **Θ(1)**
- `count = 0` → **Θ(1)**
- **`while n > 1` loop**:
  - `n = n // 2` reduces `n` by half each iteration.
  - The number of iterations needed for `n` to reach `1` is **log₂(`n`)**.
  - Each iteration runs in **Θ(1)**.
- `return count` → **Θ(1)**.

#### **Total Cost:**
- The loop runs **log₂(`n`)** times.
- Each iteration takes **Θ(1)** time.
- **Final Complexity: Θ(log `n`).**

---

| Complexity | Example | Explanation |
|------------|---------|-------------|
| **Θ(`n`)** | `count_evens()` | Iterates over `n` elements, each taking Θ(1) work. |
| **Θ(`n`²)** | `unique_append()` | Each `.append()` involves an increasing `.find()` cost. |
| **Θ(log `n`)** | `reduce_by_half()` | Cuts `n` in half each iteration. |
