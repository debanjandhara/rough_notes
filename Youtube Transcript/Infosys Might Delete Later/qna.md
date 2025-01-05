# Chess Piece Placement Problem  

A famous chess grandmaster was analyzing one of his games in his head and suddenly forgot the positions of two important pieces. However, he is sure about some facts:  

- The location of the first piece on the board is \((x_1, y_1)\), and \(x_{l1} \leq x_1 \leq x_{r1}, y_{l1} \leq y_1 \leq y_{r1}\).  
- The location of the second piece on the board is \((x_2, y_2)\), and \(x_{l2} \leq x_2 \leq x_{r2}, y_{l2} \leq y_2 \leq y_{r2}\).  
- The chessboard cells corresponding to the pieces are of the same color.  

In other words, he doesn't remember the exact positions of the pieces. However, for every piece, he is sure about the part of the board where it can be. The part of the board here is just a rectangular submatrix described by 4 coordinates.  

**Note**:  
- Two pieces cannot occupy the same location.  

The grandmaster is wondering how many placements of these two pieces are possible if he remembers everything correctly.  

---

## Input Format  

- The first line contains an integer \(x_{l1}\), denoting the minimum possible row of the first piece.  
- The next line contains an integer \(x_{r1}\), denoting the maximum possible row of the first piece.  
- The next line contains an integer \(y_{l1}\), denoting the minimum possible column of the first piece.  
- The next line contains an integer \(y_{r1}\), denoting the maximum possible column of the first piece.  
- The next line contains an integer \(x_{l2}\), denoting the minimum possible row of the second piece.  
- The next line contains an integer \(x_{r2}\), denoting the maximum possible row of the second piece.  
- The next line contains an integer \(y_{l2}\), denoting the minimum possible column of the second piece.  
- The next line contains an integer \(y_{r2}\), denoting the maximum possible column of the second piece.  

---

## Constraints  

- \(1 \leq x_{l1} \leq 8\)  
- \(x_{l1} \leq x_{r1} \leq 8\)  
- \(1 \leq y_{l1} \leq 8\)  
- \(y_{l1} \leq y_{r1} \leq 8\)  
- \(1 \leq x_{l2} \leq 8\)  
- \(x_{l2} \leq x_{r2} \leq 8\)  
- \(1 \leq y_{l2} \leq 8\)  
- \(y_{l2} \leq y_{r2} \leq 8\)  
