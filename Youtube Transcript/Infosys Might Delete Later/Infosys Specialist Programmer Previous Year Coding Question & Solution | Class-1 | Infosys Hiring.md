# Infosys Specialist Programmer Preparation Guide

## Overview
- **Role**: Specialist Programmer (SP)
- **CTC**: ₹9.5 LPA
- **Target Batch**: 2024
- **Exam Month**: July 2024
- **Hiring Mode**: Off-campus recruitment shared via colleges.

## Key Details
- **Test Format**: 
  - **Questions**: 3 coding problems.
  - **Difficulty**: Medium to Hard.
  - **Topics**: Arrays, Strings, Stacks, Queues, Trees, Graphs, Dynamic Programming (DP), Heaps, Searching, Sorting.
- **Eligibility**: 
  - Resume/profile screening based on Infosys criteria.
  - No aptitude test, coding-focused evaluation.

## Preparation Strategy 📝
- **Recommended Platforms**:
  - **CodeChef**, **CodeForces**, **LeetCode**, **HackerRank**, **HackerEarth**.
- **Focus Areas**:
  - Practice **Medium** and **Hard-level** coding problems.
  - Cover **competitive programming** concepts extensively.
- **Key Topics**:
  - Arrays & Strings: Expect 1-2 questions.
  - Graphs, Trees, and DP: High-priority topics.
  - Searching and Sorting techniques.

---

## Example Problem: Largest Subset with Modulo Condition

### Problem Statement 📄
- **Input**: Integer `n`.
- **Task**: From the range `[1, n-1]`, find the largest subset `S` such that:
  - Product of elements in `S` modulo `n` = 1.
- **Output**: Length of the largest subset.

### Example
1. **Input**: `n = 4`  
   **Output**: `1`  
   Explanation: Subset `{1}` satisfies the condition.
   
2. **Input**: `n = 7`  
   **Output**: `5`  
   Explanation: Subset `{1, 2, 3, 4, 5}` satisfies the condition.

### Constraints
- `2 ≤ n ≤ 10^5`.

---

## Approach 💡
1. **Understand the Modulo Property**:
   - Identify subsets whose product modulo `n` equals `1`.
2. **Iterative Calculation**:
   - Use brute force or optimize using modular arithmetic.
3. **Efficiency**:
   - Ensure the approach handles large `n` efficiently, avoiding timeouts.

---

## Preparation Tips 🌟
- **Daily Routine**:
  - Solve 1-2 medium/hard problems.
  - Review key topics like **modular arithmetic**.
- **Exam Readiness**:
  - Simulate test environments.
  - Prioritize solving problems under time constraints.
- **Resources**:
  - Follow preparation playlists and curated question sets on coding platforms.

---

# Subset Selection Problem and Infosys Preparation

## Problem Definition
- **Objective**: Find the length of the largest subset such that the product of all elements modulo \( n \) equals 1.
- **Input**:
  - \( n \): A positive integer.
  - Elements: Range from \( 1 \) to \( n-1 \).
- **Output**: Length of the largest subset satisfying the condition.

## Solution Approach
### Problem Analysis
1. **Key Idea**: Start from the largest possible subset and calculate the product.
2. **Condition**: \( \text{product of subset} \mod n = 1 \).

### Algorithm
1. **Traverse Backward**:
   - Start from \( n-1 \) down to \( 1 \).
   - Calculate factorial (product) at each step.
2. **Check Condition**:
   - If \( \text{factorial} \mod n = 1 \), return the current length.
3. **Implementation**:
   - Use a loop to decrement from \( n-1 \) to \( 1 \).
   - Maintain a function to compute factorial.

### Python Implementation
```python
def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

n = int(input("Enter the value of n: "))
for i in range(n-1, 0, -1):
    if factorial(i) % n == 1:
        print(i)
        break
```

## Testing and Examples
- **Input**: \( n = 7 \)
  - **Output**: \( 5 \)
- **Input**: \( n = 4 \)
  - **Output**: \( 1 \)

---

## Infosys SP Profile Preparation
- **Role**: Specialist Programmer (SP) – 9.5 LPA.
- **Exam Pattern**:
  - 3 coding questions.
  - **Difficulty**: Medium to Hard.

### Recommended Practice
- **Platforms**:
  - HackerRank
  - CodeChef
  - CodeForces
- **Daily Goal**: Solve 1–2 medium or hard problems.

### Key Topics
- Arrays
- Strings
- Dynamic Programming (DP)
- Bit Manipulation
- Graphs
- Stacks and Queues

### Strategy
1. Focus on medium to hard problems.
2. Revise fundamental topics.
3. Attempt previous year questions for Infosys and similar exams.

---

## Additional Resources
- **JobOn Test**:
  - **Opportunity**: Access multiple companies through one test.
  - **Link**: [JobOn Test Link](#)
- **Infosys Playlist**: [Previous Year Infosys Exam Preparation](#)

---


