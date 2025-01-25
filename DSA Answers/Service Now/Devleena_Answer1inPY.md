To solve the problem, we can break it into several steps and ensure an optimized solution that works for all edge cases. Here's the step-by-step approach:

### Step 1: Analyze the Problem
1. **Input:** Starting position of Alice (`a`), Bob's position (`b`), and a list of streetlights with their positions and radii.
2. **Output:** Minimum time spent in the dark for Alice to travel to Bob, rounded down to the nearest integer.

Alice can move in a straight line from `a` to `b`, but parts of this line may lie outside the illuminated areas of the streetlights. We need to calculate the length of the path that lies outside the illumination.

### Step 2: Identify Similar Problems
This problem is geometrically related to the **shortest path in a weighted graph**, but instead of discrete nodes, the challenge is to deal with continuous regions (the illuminated areas).

Leetcode problems like:
- **Max Points on a Line**
- **Optimal Path with Constraints**
- **Circular Ranges**
may share some conceptual overlap.

### Step 3: Plan the Algorithm
1. **Straight Line Path:** Represent Alice's path as the line segment connecting `a` and `b`.
2. **Illumination Check:** Determine which parts of this line lie outside the streetlight regions.
3. **Intersection Calculation:** For each streetlight, calculate the portion of the line segment that intersects its illuminated circle.
4. **Dark Distance:** Subtract the total illuminated distance from the total path length to get the "dark" distance.

### Step 4: Optimized Approach
1. Calculate the total distance between `a` and `b`.
2. For each streetlight:
   - Compute the intersection of the light's circle with the line segment.
   - Sum up all the illuminated parts.
3. Subtract the illuminated parts from the total distance to compute the time spent in the dark.
4. Return the floor of the result.

### Step 5: Edge Cases
- No streetlights (`lights=[]`): The entire path is dark.
- All streetlights completely cover the path.
- Some streetlights only partially cover the path.

Here's the Python implementation:

```python
import math

def minDist(a, b, lights):
    def dist(p1, p2):
        """Calculate the Euclidean distance between two points."""
        return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

    def segment_circle_intersection(a, b, c, r):
        """Calculate the illuminated length of segment (a, b) inside circle (c, r)."""
        ax, ay = a
        bx, by = b
        cx, cy = c

        # Vector math to find projection and distances
        abx, aby = bx - ax, by - ay
        acx, acy = cx - ax, cy - ay
        ab_length = math.sqrt(abx ** 2 + aby ** 2)
        ab_unit = (abx / ab_length, aby / ab_length)
        projection = acx * ab_unit[0] + acy * ab_unit[1]
        closest_point = (ax + projection * ab_unit[0], ay + projection * ab_unit[1])
        distance_to_circle = dist(closest_point, c)

        # No intersection
        if distance_to_circle > r:
            return 0

        # Calculate intersection points
        d = math.sqrt(r ** 2 - distance_to_circle ** 2)
        t1 = projection - d
        t2 = projection + d
        t1 = max(0, t1)  # Clamp to segment
        t2 = min(ab_length, t2)
        if t1 > t2:
            return 0
        return t2 - t1

    total_distance = dist(a, b)
    illuminated_distance = 0

    for light in lights:
        cx, cy, r = light
        illuminated_distance += segment_circle_intersection(a, b, (cx, cy), r)

    dark_distance = total_distance - illuminated_distance
    return math.floor(max(0, dark_distance))

# Driver code
if __name__ == "__main__":
    # Test case 1
    a = [-2, 2]
    b = [2, -2]
    lights = [[1, 1, 2], [2, 2, 1]]
    print(minDist(a, b, lights))  # Output: 2

    # Test case 2
    a = [-1, -1]
    b = [1, 1]
    lights = [[0, 0, 1], [0, 0, 2]]
    print(minDist(a, b, lights))  # Output: 0
```

### Explanation
- The `dist` function computes Euclidean distances.
- The `segment_circle_intersection` function calculates the part of the line segment within a circle.
- We iterate over all streetlights to compute the total illuminated distance.
- The result is the total path length minus the illuminated length, floored to the nearest integer.

This approach ensures efficiency with $O(n)$ complexity per streetlight for the intersection calculation, suitable for $n \leq 500$.
