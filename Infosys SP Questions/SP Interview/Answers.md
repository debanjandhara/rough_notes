# Answers to the Questions

## 1. Database Management System (DBMS)

### a. Practical SQL Queries

#### Query 1: Retrieve the top 7 highest-paid employees from an employee table.
```sql
SELECT * FROM employees ORDER BY salary DESC LIMIT 7;
```

#### Query 2: Modify the name of a column in a given table.
```sql
ALTER TABLE table_name RENAME COLUMN old_column_name TO new_column_name;
```

### b. Conceptual Topics

#### BCNF (Boyce-Codd Normal Form)
- A stronger version of 3NF that ensures every determinant is a candidate key.
- Eliminates redundancy but may result in table decomposition.

#### 3NF (Third Normal Form)
- A table is in 3NF if it is in 2NF and has no transitive dependency.
- Less restrictive than BCNF, allows for some redundancy.

---

## 2. Operating System (OS) Fundamentals

### a. CPU Scheduling

- **FCFS (First Come First Serve)**: Non-preemptive, executes in order of arrival.
- **SJF (Shortest Job First)**: Can be preemptive or non-preemptive; prioritizes shortest jobs.
- **Round Robin**: Each process gets a fixed time slice; fair but may have high overhead.

### b. Deadlock

- **Deadlock** occurs when a set of processes are waiting for resources held by each other.

#### Prevention Techniques:
- Avoid circular wait by enforcing resource ordering.
- Use a wait-die or wound-wait scheme for resource allocation.

### c. Multithreading
- Allows multiple threads to execute simultaneously, improving performance.
- Used in web servers, database systems, and parallel computing.

---

## 3. Coding Challenges

### a. On-the-Spot Coding Tasks

#### Swapping Two Numbers Without a Third Variable
```python
a, b = 5, 10
a = a ^ b
b = a ^ b
a = a ^ b
print(a, b)  # Output: 10, 5
```

#### HashMap-Based Problem (Sorting Character-Integer Pairs by Character)
```python
pairs = {'c': 3, 'a': 1, 'b': 2}
sorted_pairs = dict(sorted(pairs.items()))
print(sorted_pairs)  # Output: {'a': 1, 'b': 2, 'c': 3}
```

#### Palindrome Check & Next Palindrome Computation
```python
def is_palindrome(n):
    return str(n) == str(n)[::-1]

def next_palindrome(n):
    while True:
        n += 1
        if is_palindrome(n):
            return n

print(next_palindrome(123))  # Output: 131
```

#### Binary Tree Traversal (Inorder Traversal Example)
```python
class Node:
    def _init_(self, val):
        self.left = self.right = None
        self.val = val

def inorder(root):
    return inorder(root.left) + [root.val] + inorder(root.right) if root else []

# Example
root = Node(1)
root.left = Node(2)
root.right = Node(3)
print(inorder(root))  # Output: [2, 1, 3]
```

### b. LeetCode-Style Coding Problems

#### Traveling Salesperson Problem (TSP) Explanation

##### Why TSP is NP-Hard?
- No polynomial-time solution exists for finding the shortest route through all cities.

#### Dynamic Programming Approach (Held-Karp Algorithm in Python)
```python
from itertools import permutations

def tsp(graph):
    n = len(graph)
    min_path = float('inf')
    for perm in permutations(range(1, n)):  
        cost = 0
        k = 0  
        for j in perm:
            cost += graph[k][j]
            k = j
        cost += graph[k][0]
        min_path = min(min_path, cost)
    return min_path

graph = [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]
print(tsp(graph))  # Output: Minimum cost
```

---

## 4. Scenario-Based and Resume-Based Discussions

### Scenario-Based Questions
- Justify approach, trade-offs, and problem-solving techniques.

### Resume-Based Questions
- Expect project-related questions, technology stack choices, and teamwork challenges.

---

## 5. Core Programming and Technical Topics

### a. Additional Technical Questions
- **Core Java**: Object-oriented programming, multithreading, collections framework.
- **Spring Boot & Microservices**: REST APIs, service discovery, scalability.

### b. Data Structures and Algorithms (DSA)

#### Longest Common Subsequence (LCS) Dynamic Programming Solution
```python
def lcs(X, Y):
    m, n = len(X), len(Y)
    dp = [[0] * (n+1) for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]

print(lcs("AGGTAB", "GXTXAYB"))  # Output: 4
```

#### Stock Buy and Sell Problem (Max Profit Calculation)
```python
def max_profit(prices):
    min_price, max_profit = float('inf'), 0
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    return max_profit

print(max_profit([7, 1, 5, 3, 6, 4]))  # Output: 5
```

#### Binary Search Recursive Solution
```python
def binary_search(arr, l, r, x):
    if r >= l:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, l, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, r, x)
    return -1

arr = [2, 3, 4, 10, 40]
print(binary_search(arr, 0, len(arr)-1, 10))  # Output: 3
```

---

## 6. Interview Structure

### a. Introduction & Personal Pitch
- **Tell me about yourself**: Briefly introduce background, skills, and projects.

### b. Technical Discussion
- Discussed concepts like TSP, dynamic programming, and Java frameworks.

### c. Final Discussion & Feedback
- Ask insightful questions about Infosys’s tech stack and future roles.

---

## 7. Preparation Tips

- **Resume Readiness**: Be confident about listed skills.
- **Problem-Solving Practice**: Use LeetCode, Codeforces, and real-world challenges.
- **Technical Knowledge Review**: Revise DBMS, OS, Java, and Microservices.
- **Effective Communication**: Structure answers clearly.

---

This should help you prepare comprehensively for the Infosys Specialist Programmer (SP) interview! 🚀 Let me know if you need further clarifications. 😊
