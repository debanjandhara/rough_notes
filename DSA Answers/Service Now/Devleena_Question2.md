## Problem Statement

In the kingdom of Geekland, the King has ordered a series of secret missions to prepare for an upcoming battle. There are `n` knights in the kingdom (this includes the King). The missions require multiple squads containing exactly two knights to succeed, but strict rules govern who can pair up with whom.

The knights are organized in a hierarchy. The King (0-th knight) is the supreme Commander with no superiors at the top. Every other knight `i` (1 <= i <= n-1) directly reports to their direct superior knight `arr[i-1]`.

A knight `X` is considered superior (direct or indirect) to knight `Y` if:
- Knight `X` is the direct superior of knight `Y`.
- Or, knight `X` is a superior of the direct superior of knight `Y`.

To form a squad, no knight can be superior to their squadmate, either directly or indirectly, and no knight can be part of more than one squad.

### Task

As the royal strategist of Geekland, calculate the maximum number of two-knight squads possible.

**Note:** No two knights can be superior to each other.

### Input

- An array `arr[]` of size `n-1` where `arr[i]` denotes the direct superior of knight `i+1`.

### Output

- The maximum number of two-knight squads possible.

### Examples

#### Example 1

**Input:**
```text
arr[] = [0, 0, 2, 1, 1, 3]
```

**Output:**
```text
3
```

**Explanation:**
- Squads `(1, 2)`, `(3, 5)`, and `(4, 6)` can be created.

**Tree:**
```markdown
    0
   / \
  1   2
 /|   |
4 5   3
      |
      6
```

#### Example 2

**Input:**
```text
arr[] = [0, 1, 0]
```

**Output:**
```text
1
```

**Explanation:**
- Either squad `(2, 3)` or `(1, 3)` can be created.

#### Example 3

**Input:**
```text
arr[] = [0, 1, 2]
```

**Output:**
```text
0
```

**Explanation:**
- No squad can be created.

### Constraints
- `2 <= n <= 10^5`
- `arr.size() = n-1`
- `0 <= arr[i] <= n-1`

### Function Signature

```cpp
int maxPossibleSquad(vector<int>& arr);
```
