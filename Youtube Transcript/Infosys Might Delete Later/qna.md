

Here’s the question formatted properly with appropriate structure and spacing for readability:

---

### Problem Statement

A famous chess grandmaster was analyzing one of his games in his head when he suddenly forgot the positions of two important pieces. However, he is sure about some facts:

- The location of the first piece on the board is \((x_1, y_1)\), and the coordinates satisfy the following conditions:
  \[
  x_{l1} \leq x_1 \leq x_{r1}, \quad y_{l1} \leq y_1 \leq y_{r1}
  \]

- The location of the second piece on the board is \((x_2, y_2)\), and the coordinates satisfy the following conditions:
  \[
  x_{l2} \leq x_2 \leq x_{r2}, \quad y_{l2} \leq y_2 \leq y_{r2}
  \]

- The chessboard cells corresponding to the two pieces are of the **same color**.

In other words, he doesn't remember the exact positions of the pieces, but he knows the rectangular submatrices where they can be located. Each submatrix is described by 4 coordinates.  

**Note**:  
- Two pieces **cannot** occupy the same location.  

The grandmaster is wondering how many valid placements of the two pieces are possible if his memory is correct.

---

### Input Format

The input consists of 8 integers:

1. \(x_{l1}\): Minimum possible row of the first piece.  
2. \(x_{r1}\): Maximum possible row of the first piece.  
3. \(y_{l1}\): Minimum possible column of the first piece.  
4. \(y_{r1}\): Maximum possible column of the first piece.  
5. \(x_{l2}\): Minimum possible row of the second piece.  
6. \(x_{r2}\): Maximum possible row of the second piece.  
7. \(y_{l2}\): Minimum possible column of the second piece.  
8. \(y_{r2}\): Maximum possible column of the second piece.  

---

### Constraints

- \(1 \leq x_{l1} \leq 8\)  
- \(x_{l1} \leq x_{r1} \leq 8\)  
- \(1 \leq y_{l1} \leq 8\)  
- \(y_{l1} \leq y_{r1} \leq 8\)  
- \(1 \leq x_{l2} \leq 8\)  
- \(x_{l2} \leq x_{r2} \leq 8\)  
- \(1 \leq y_{l2} \leq 8\)  
- \(y_{l2} \leq y_{r2} \leq 8\)  

---

### Output Format

The output should be the total number of valid placements of the two pieces.  

