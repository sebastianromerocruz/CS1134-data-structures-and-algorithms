<h2 align=center>Solution</h2>

<h1 align=center>Question 1: Hashing and Compression</h1>

Keys to insert: `12, 56, 22, 106, 36, 72, 902, 86, 96, 62, 42`

---

## a) Division method, `N = 10`

`h2(k) = k % 10`

| Key | Computation | Index |
|-----|-------------|-------|
| 12  | 12 % 10     | 2     |
| 56  | 56 % 10     | 6     |
| 22  | 22 % 10     | 2     |
| 106 | 106 % 10    | 6     |
| 36  | 36 % 10     | 6     |
| 72  | 72 % 10     | 2     |
| 902 | 902 % 10    | 2     |
| 86  | 86 % 10     | 6     |
| 96  | 96 % 10     | 6     |
| 62  | 62 % 10     | 2     |
| 42  | 42 % 10     | 2     |

```
Index | Chain
------+-----------------------------------
  0   |
  1   |
  2   | 12 → 22 → 72 → 902 → 62 → 42
  3   |
  4   |
  5   |
  6   | 56 → 106 → 36 → 86 → 96
  7   |
  8   |
  9   |
```

With a non-prime table size, keys sharing the same last digit pile into the same bucket. All 11 keys land in just 2 of the 10 buckets.

---

## b) Division method, `N = 13`

`h2(k) = k % 13`

| Key | Computation           | Index |
|-----|-----------------------|-------|
| 12  | 12 % 13               | 12    |
| 56  | 56 − 4×13 = 4         | 4     |
| 22  | 22 − 1×13 = 9         | 9     |
| 106 | 106 − 8×13 = 2        | 2     |
| 36  | 36 − 2×13 = 10        | 10    |
| 72  | 72 − 5×13 = 7         | 7     |
| 902 | 902 − 69×13 = 5       | 5     |
| 86  | 86 − 6×13 = 8         | 8     |
| 96  | 96 − 7×13 = 5         | 5     |
| 62  | 62 − 4×13 = 10        | 10    |
| 42  | 42 − 3×13 = 3         | 3     |

```
Index | Chain
------+------------
  0   |
  1   |
  2   | 106
  3   | 42
  4   | 56
  5   | 902 → 96
  6   |
  7   | 72
  8   | 86
  9   | 22
 10   | 36 → 62
 11   |
 12   | 12
```

The prime table size spreads the keys much more evenly—9 of the 13 buckets are occupied, and only 2 have collisions.

---

## c) MAD method, `N = 10`

`h2(k) = ((125 × k + 342) % 1009) % 10`

| Key | 125k + 342 | % 1009 | % 10 | Index |
|-----|------------|--------|------|-------|
| 12  | 1842       | 833    | 3    | 3     |
| 56  | 7342       | 279    | 9    | 9     |
| 22  | 3092       | 65     | 5    | 5     |
| 106 | 13592      | 475    | 5    | 5     |
| 36  | 4842       | 806    | 6    | 6     |
| 72  | 9342       | 261    | 1    | 1     |
| 902 | 113092     | 84     | 4    | 4     |
| 86  | 11092      | 1002   | 2    | 2     |
| 96  | 12342      | 234    | 4    | 4     |
| 62  | 8092       | 20     | 0    | 0     |
| 42  | 5592       | 547    | 7    | 7     |

```
Index | Chain
------+------------
  0   | 62
  1   | 72
  2   | 86
  3   | 12
  4   | 902 → 96
  5   | 22 → 106
  6   | 36
  7   | 42
  8   |
  9   | 56
```

Even with a non-prime table size, the MAD compression function distributes the keys well—9 of 10 buckets are occupied, with only 2 collisions. The multiplicative scrambling prevents the clustering seen in part (a).
