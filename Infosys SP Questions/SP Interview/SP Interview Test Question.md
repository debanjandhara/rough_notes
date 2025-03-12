## Problem Statement

It is given that for two integers `x` and `y`, the cost function `C(x, y)` is defined as follows:

- If `x < y`, then `C(x, y) = x`.
- Otherwise, `C(x, y) = C(x / y, y) + x MOD y`.

You have been given two integers `x` and `c`, such that `C(x, y) = c` for some `y`. Find the smallest value of `y`, which satisfies the above-defined cost function. If no such `y` exists, return `-1`.

### Note:

- It is given that `2 <= y <= 2 * 10^9`.

---

## Input Format

- The first line contains an integer, `x`, denoting the given integer `x`.
- The next line contains an integer, `c`, denoting the value `c` described in the problem.

### Constraints

- `1 <= x <= 10^5`
- `1 <= c <= 10^5`

---

## Sample Test Cases

### Case 1

#### Input:

```
3
2
```

#### Output:

```
2
```

#### Explanation:

- `C(3, 2) = C(1, 2) + 1`
- `C(1, 2) = 1`

Thus, `C(3, 2) = 2`.

No smaller `y` will satisfy `C(3, y) = 2`.

---

### Case 2

#### Input:

```
4
4
```

#### Output:

```
5
```
