## Problem Statement

Alice and Bob live in a city represented as a 2D plane. Alice is currently at the coordinates `a[0], a[1]` and she wants to meet Bob, who is at the coordinates `b[0], b[1]`. 

The city has `n` streetlights, each illuminating a circular area. A streetlight located at `(lights[i][0], lights[i][1])` provides light within a circle of radius `lights[i][2]`. The illuminated areas of different streetlights may overlap.

Alice can take any path on the 2D plane to meet Bob. She can move in any arbitrary direction at a constant speed of 1 unit per second. Since it is nighttime, Alice wants to avoid traveling through dark areas as much as possible. 

Determine the minimum time Alice has to spend traveling in the dark.

Finally, you need to return the greatest integer less than or equal to the result (i.e., the floor value of the answer). For example, if the answer is 4.97, you should return 4.

### Examples

#### Example 1:

**Input:**
```cpp
a[] = [-2, 2], b[] = [2, -2], lights[] = [[1, 1, 2], [2, 2, 1]]
```

**Output:**
```cpp
2
```

**Explanation:** Alice needs to use the first streetlight with a radius of 2 to minimize the time spent in the dark. In this case, the minimum possible time will be 2.324 seconds, and the floor of 2.324 is 2.

#### Example 2:

**Input:**
```cpp
a[] = [-1, -1], b[] = [1, 1], lights[][] = [[0, 0, 1], [0, 0, 2]]
```

**Output:**
```cpp
0
```

**Explanation:** Both Alice and Bob and the entire path are covered under the street lights.

### Constraints:
- `1 <= n <= 500`
- `a.size() = b.size() = 2`
- `-10^5 <= a[i], b[i] <= 10^5`
- `lights[i].size() = 3`
- `-10^6 <= lights[i][0], lights[i][1] <= 10^6`
- `1 ≤ lights[i][2] ≤ 10^5`

### Function Signature:
```cpp
int minDist(vector<int> a, vector<int> b, vector<vector<int>> lights);
```

### Notes:
- The function should return the minimum time spent in the dark, rounded down to the nearest integer.
- Alice’s movement is unrestricted, meaning she can move in any direction and at any speed, but we aim to minimize the time spent outside the illuminated areas of the streetlights.
