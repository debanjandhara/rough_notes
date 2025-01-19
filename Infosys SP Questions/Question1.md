### Problem Statement

Jerry has a set of `n` cheesecakes, each represented by a distinct value `a[i]`.

Tom wants to rearrange his sequence secretly. But, he can only change the order of the set and not delete or add any cheesecake so that Jerry does not suspect anything.

Tom chooses a positive integer `k` and replaces each cheesecake `a[i]` of the set `a` with `a[i] ^ k` (`^` denotes the bitwise XOR operation) such that Jerry cannot see any difference after he is done changing. After this transformation, Jerry's cheesecake set must remain unchanged as a set (order doesn't matter, and all elements must still be present without duplication).

Find the smallest positive integer `k` to achieve this goal. If it is not possible, return `-1`.

### Input Format

- The first line contains an integer, `n`, denoting the number of elements in `a`.
- Each of the next `n` lines contains an integer describing `a[i]`.

### Constraints

- `1 <= n <= 1024`
- `1 <= a[i] <= 1024`

### Sample Test Cases

#### Case 1

**Input:**

```
4
1
0
2
3
```

**Output:**

```
1
```

**Explanation:**

Here, `n = 4` and `a = [1, 0, 2, 3]`.

1 is a minimum positive integer and it satisfies all the conditions.

- `1 ^ 1 = 0`
- `0 ^ 1 = 1`
- `2 ^ 1 = 3`
- `3 ^ 1 = 2`

Hence, `k = 1`.

#### Case 2

**Input:**

```
2
0
2
```

**Output:**

```
2
```

#### Case 3

**Input:**

```
3
1
2
3
```

**Output:**

```
-1
```
