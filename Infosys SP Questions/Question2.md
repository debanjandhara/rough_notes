### Problem Statement

You are given an undirected connected graph consisting of `n` nodes and `m` edges and an integer `k`.

You want to make a trip in the graph and you can move from node `a` to node `b` *if and only if* there exists an edge between `a` and `b`.

The trip consists of `k` days and you can start the trip at any node you want. At the end of each day, you have to move from the current node to any of its *neighboring nodes*.

You will also be given a grid `a` of size `n * k`, where `a[i,j]` (1 <= `a[i,j]` <= 100000) denotes the enjoyment you get if you stay at the `i`th node during the `j`th day.

Find the maximum enjoyment you can get if you start the trip at any node you want.

### Input Format

- The first line contains an integer, `n`, denoting the number of nodes.
- The next line contains an integer, `m`, denoting the number of edges.
- The next line contains an integer, `h`, denoting the number of columns in the edges.
- The next line contains an integer, `k`, denoting the number of days.
- Each of the next `m` lines contains `h` space-separated integers describing the edges.
- Each of the next `n` lines contains `k` space-separated integers describing the enjoyment grid `a`.

### Constraints

- `1 <= n <= 10^5`
- `n - 1 <= m <= min((n * (n - 1)) / 2, 10^5)`
- `2 <= h <= 2`
- `1 <= k <= 100`
- `1 <= edges[i][j] <= n`
- `1 <= a[i][j] <= 10^5`

### Sample Test Cases

#### Case 1

**Input:**

```
2
1
2
2
1 2
1 10
10 1
```

**Output:**

```
20
```

**Explanation:**

Here, `n = 2`, `m = 1`, `h = 2`, `k = 2`, `edges = [[1, 2]]` and `a = [[1, 10], [10, 1]]`.

We can start from node 2 on day 1 with enjoyment 10 and move to node 1 for day 2 with enjoyment 10. 

Hence, the total enjoyment is `10 + 10 = 20`.

#### Case 2

**Input:**

```
3
3
2
3
1 2
1 3
2 3
5 1 1
1 3 1
1 4 10
```

**Output:**

```
18
```

**Explanation:**

Here, `n = 3`, `m = 3`, `h = 2`, `k = 3`, `edges = [[1, 2], [1, 3], [2, 3]]` and `a = [[5, 1, 1], [1, 3, 1], [1, 4, 10]]`.

- Day 1 -> Node 1 (enjoyment = 5)
- Day 2 -> Node 2 (enjoyment = 3)
- Day 3 -> Node 3 (enjoyment = 10)

This gives a maximum possible enjoyment of `5 + 3 + 10 = 18`.

#### Case 3

**Input:**

```
4
3
2
2
1 2
2 3
3 4
3 4
10 2
30 1
4 9
```

**Output:**

```
39
```

**Explanation:**

Here, `n = 4`, `m = 3`, `h = 2`, and `k = 2`, `edges = [[1, 2], [2, 3], [3, 4]]` and `a = [[3, 4], [10, 2], [30, 1], [4, 9]]`.

- Day 1 -> Node 3 (enjoyment = 30)
- Day 2 -> Node 4 (enjoyment = 9)

Hence, the total enjoyment is `30 + 9 = 39`.

### Function Signature

```cpp
int GetMaxEnjoyment(int n, int m, int h, int k, list<int> edges, list<int> a);
```

### Explanation

The function `GetMaxEnjoyment` should return the maximum possible enjoyment that can be obtained while traveling across the graph for `k` days, starting from any node.

- The function receives:
  - `n`: number of nodes in the graph.
  - `m`: number of edges in the graph.
  - `h`: number of columns in the edges list.
  - `k`: number of days.
  - `edges`: a list of edges describing the graph.
  - `a`: a list of enjoyments representing the enjoyment values of each node over `k` days.

- The function must calculate and return the maximum enjoyment obtainable starting from any node.
