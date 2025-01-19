### Problem Statement

You are given an array `a` of length `n`. 

Let's say that element `a[i]` eats element `a[j]` (where `i < j`) if:

* The range sum of the array `a` from `i` to `k` for every `k` from `i` to `j-1` is greater than or equal to `a[k + 1]`.

More formally, `a[i]` eats `a[j]` if:

* `sum[i][k] >= a[k+1]` for `(i <= k < j)` where `sum[l][r]` is the sum of array elements from `l` to `r` (i.e., `a[l] + a[l+1] + ... + a[r]`).

For more explanation, if the following conditions are satisfied, then `a[i]` eats `a[j]`:

* `a[i] >= a[i + 1]`
* `a[i] + a[i + 1] >= a[i + 2]`
* `a[i] + a[i + 1] + a[i + 2] >= a[i + 3]`
* ...
* `a[i] + ... + a[j - 1] >= a[j]`

We define the distance of element `a[j]` as the minimum value of `j - i` where `i < j` and `a[i]` can eat `a[j]`. In case there is no `a[i]` that eats `a[j]`, then the distance of `a[j]` is 0.

**Task**: Find the sum of distances of all elements of `a`.

### Input Format

- The first line contains an integer, `n`, denoting the number of elements in `a`.
- Each of the next `n` lines contains an integer describing `a[i]`.

### Constraints

- `1 <= n <= 200000`
- `1 <= a[i] <= 10^9`

### Sample Test Cases

#### Case 1

**Input:**

```
1
1
```

**Output:**

```
0
```

**Explanation:**

Here, `n = 1` and `a = [1]`.

In this testcase, `distance[1]` is `0` because there is no element that can eat `a[1]`, so the answer is `0`.

#### Case 2

**Input:**

```
5
5
4
1
2
3
```

**Output:**

```
7
```

**Explanation:**

Here, `n = 5` and `a = [5, 4, 1, 2, 3]`.

In this testcase:

- `distance[5] = 0` as there is no element before it.
- `distance[4] = 1` as `5 >= 4`.
- `distance[1] = 1` as `4 >= 1`.
- `distance[2] = 2` as `1 < 2` and `(4 >= 2 and 4 + 1 >= 2)`.
- `distance[3] = 3` as `2 < 3`, `1 < 2`, and `(4 >= 1, 4 + 1 >= 2, 4 + 1 + 2 = 3)`.

Hence, the total sum of distances is `0 + 1 + 1 + 2 + 3 = 7`.

#### Case 3

**Input:**

```
5
5
4
1
2
3
```

**Output:**

```
7
```

### Function Signature

```cpp
long getDistances(int n, list<int> a);
```

### Explanation

The function `getDistances` should return the sum of distances for all elements in the array `a`.

- The function receives:
  - `n`: the number of elements in the array.
  - `a`: a list of integers representing the array.

- The function must calculate and return the sum of the distances for all elements in the array according to the conditions described in the problem statement.
