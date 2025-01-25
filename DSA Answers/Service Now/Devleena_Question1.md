This problem can be addressed using computational geometry and graph theory. Here's how we can solve it step by step:

---

### **1. Similar Leetcode Questions**
Some problems related to this one include:
1. **Escape the Light Circle** (geometry & graph traversal).
2. **Swim in Rising Water** (Dijkstra’s algorithm on a grid).
3. **Network Delay Time** (Dijkstra’s algorithm for shortest paths).
4. **Minimum Time to Visit Points** (movement with constraints).

---

### **2. Approach and Algorithm**

The goal is to minimize the time Alice spends traveling in the dark by leveraging illuminated areas provided by streetlights.

#### Key Observations:
1. **Illuminated Zones**: A streetlight at `(x, y)` with radius `r` defines a circle. If Alice’s path stays within these circles, she’s "in the light".
2. **Path**: Alice can take any arbitrary path. However, the shortest path will be a straight line from `a` to `b`.
3. **Travel in Dark Zones**: Alice spends time in the dark when she’s outside all the illuminated areas.

#### Plan:
1. **Model the Path**:
   - The path from `a` to `b` is a straight line.
   - Parameterize the path using a line segment: $(1 - t) \cdot a + t \cdot b$, where $t \in [0, 1]$.
   
2. **Check Streetlight Coverage**:
   - For a point $p(t)$ on the line, determine if it is within the illumination of any streetlight.
   - A point $p(x, y)$ is covered by a streetlight at $(cx, cy)$ with radius $r$ if:
     \[
     (x - cx)^2 + (y - cy)^2 \leq r^2
     \]

3. **Find Dark Zones**:
   - Calculate the portion of the line segment $a \to b$ not covered by any streetlight.
   - Use **binary search** or **sweep-line algorithms** for efficiency.

4. **Calculate Minimum Dark Time**:
   - Length of the dark segment corresponds to time spent in the dark, as Alice moves at a unit speed.

---

### **3. Detailed Steps**

#### Step 1: Parametrize the Line
The straight line from `a` to `b` can be expressed as:
\[
p(t) = (1 - t) \cdot a + t \cdot b
\]
Where $t \in [0, 1]$. For a given $t$, calculate:
\[
x = (1 - t) \cdot a[0] + t \cdot b[0]
\]
\[
y = (1 - t) \cdot a[1] + t \cdot b[1]
\]

#### Step 2: Check Coverage
For each streetlight at $(cx, cy, r)$, check if $p(t)$ is within the circle:
\[
(x - cx)^2 + (y - cy)^2 \leq r^2
\]

#### Step 3: Find Dark Zones
1. **Binary Search for Transition Points**:
   - For each streetlight, find the parameter range $t_1, t_2$ where $p(t)$ enters and exits the circle.
   - Use binary search to find these $t$ values efficiently.

2. **Merge Ranges**:
   - Combine overlapping ranges of $t$ values covered by streetlights.
   - The complement gives the dark segments.

#### Step 4: Compute Time
Calculate the length of the dark segments:
\[
\text{Dark time} = \sum (\text{length of uncovered segments on } t \in [0, 1])
\]

#### Step 5: Return Floor Value
Finally, return the floor of the total dark time.

---

### **4. Implementation**

Here’s the C++ implementation:

```cpp
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;

int minDist(vector<int> a, vector<int> b, vector<vector<int>> lights) {
    double ax = a[0], ay = a[1], bx = b[0], by = b[1];
    vector<pair<double, double>> intervals;

    for (auto& light : lights) {
        double cx = light[0], cy = light[1], r = light[2];
        // Line segment parameterization
        double dx = bx - ax, dy = by - ay;
        double A = dx * dx + dy * dy;
        double B = 2 * (dx * (ax - cx) + dy * (ay - cy));
        double C = (ax - cx) * (ax - cx) + (ay - cy) * (ay - cy) - r * r;
        double D = B * B - 4 * A * C;

        if (D < 0) continue; // No intersection
        D = sqrt(D);

        double t1 = (-B - D) / (2 * A);
        double t2 = (-B + D) / (2 * A);
        t1 = max(0.0, min(1.0, t1));
        t2 = max(0.0, min(1.0, t2));
        if (t1 < t2) intervals.push_back({t1, t2});
    }

    // Merge intervals
    sort(intervals.begin(), intervals.end());
    double covered = 0, end = 0;
    for (auto& interval : intervals) {
        if (interval.first > end) {
            covered += interval.second - interval.first;
            end = interval.second;
        } else if (interval.second > end) {
            covered += interval.second - end;
            end = interval.second;
        }
    }

    double total = sqrt((bx - ax) * (bx - ax) + (by - ay) * (by - ay));
    double darkTime = total - covered;

    return floor(darkTime);
}
```

---

### **5. Edge Cases**
1. No streetlights: Entire path is dark.
2. All streetlights overlap: Path is fully illuminated.
3. Edge of streetlight coverage: $p(t)$ exactly touches the circle boundary.
4. Large coordinate values.

--- 

### **6. Complexity**
- **Time**: $O(n \cdot \log(n))$ (for range merging and binary search).
- **Space**: $O(n)$.
