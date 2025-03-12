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



# Solution : 

We can observe that the recursive cost function

$C(x, y)=
\begin{cases}
x, & \text{if } x < y,\\[1mm]
C\left(\lfloor x/y \rfloor, y\right) + (x \bmod y), & \text{otherwise},
\end{cases}$

is exactly the sum of the digits of $x$ when written in base $y$. (In base‐\(y\) notation, if
$x = a_k y^k + a_{k-1} y^{k-1} + \cdots + a_1 y + a_0,$
then $C(x, y)= a_k + a_{k-1} + \cdots + a_1 + a_0$.)

---

### Key Observations

1. **For $y > x$:**  
   If $x < y$, then $C(x,y)=x$. Thus, if $c=x$ the cost condition is met for any $y > x$. In particular, the smallest such $y$ is $x+1$.

2. **For $y \le x$:**  
   In this case the cost function is the sum of digits of $x$ in base $y$. There is no obvious monotonicity so we must check every candidate $y$ in the range \([2,x]\).

3. **Edge Cases:**  
   - If $c > x$ then it’s impossible to have a representation whose digit sum exceeds $x$ (since even the one‐digit representation for $y > x$ is $x$).  
   - For $x=1$, note that for any $y>1$ the function returns \(1\). So if $c\neq 1$ the answer is \(-1\).

---

### The Algorithm

1. **Define a helper function** to compute the sum of digits of $x$ in base $y$:

   ```python
   def digit_sum(x, base):
       s = 0
       while x:
           s += x % base
           x //= base
       return s
   ```

2. **Search for the smallest $y$ in \([2, x]\)** such that $$\text{digit\_sum}(x,y) = c$$. Since $x \le 10^5$, iterating from 2 to $x$ is efficient.

3. **If no $y$ in \([2,x]\) is found**, then check if $c = x$. If so, $y = x+1$ is the answer (because when $y > x$, $C(x, y)=x$). Otherwise, return $-1$.

---

### Step-by-Step Code Implementation

Below is the complete Python implementation:

```python
def digit_sum(x, base):
    """Return the sum of digits of x in base 'base'."""
    s = 0
    while x:
        s += x % base
        x //= base
    return s

def find_smallest_base(x, c):
    # Check for candidates where y is between 2 and x (inclusive)
    for base in range(2, x+1):
        if digit_sum(x, base) == c:
            return base
    # For y > x, the function always returns x.
    if x == c:
        return x + 1
    return -1

if __name__ == "__main__":
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        # Sample test cases if no input is provided:
        test_cases = [(3, 2), (4, 4)]
        for x, c in test_cases:
            print(find_smallest_base(x, c))
    else:
        x = int(data[0])
        c = int(data[1])
        print(find_smallest_base(x, c))
```

---

### Explanation of the Code

- **digit_sum Function:**  
  It repeatedly adds the remainder of $x$ when divided by $\text{base}$ (which gives the least significant digit) and then updates $x$ to be the quotient. This continues until $x$ becomes 0.

- **find_smallest_base Function:**  
  It iterates over all possible bases from 2 to $x$ and checks if the digit sum equals $c$. The first valid $y$ is returned immediately. If no candidate is found in that range and if $c$ equals $x$, then $y = x+1$ is returned. Otherwise, it returns \(-1\).

- **Main Section:**  
  It reads input from standard input and applies the function. If no input is provided, it runs the two sample test cases.

---

### Testing on Sample Cases

- **Case 1:**  
  Input: $x=3,\, c=2$  
  - $y=2$ gives $3$ in base 2 as “11” (sum $1+1=2$).  
  Output: **2**

- **Case 2:**  
  Input: $x=4,\, c=4$  
  - For $y \le 4$:  
    - $y=2$ gives “100” (sum $1$),  
    - $y=3$ gives “11” (sum $1+1=2$),  
    - $y=4$ gives “10” (sum $1$).  
  - For $y > 4$:  
    - The smallest $y$ is $4+1=5$ and $f(4,5)=4$.  
  Output: **5**

---

### Final Notes

This solution is optimized for the given constraints. Iterating over $y$ from 2 to $x$ results in at most $10^5$ iterations and each digit sum computation is $O(\log_{y}(x))$, which is efficient enough for $x \le 10^5$. All edge cases are covered by the direct check and handling for $y > x$.

This is the final optimized solution with all test cases in mind.
