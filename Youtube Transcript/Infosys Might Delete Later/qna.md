

### Chess Puzzle: Piece Placement Analysis 🧩  

A famous chess grandmaster was analyzing one of his games in his head when he suddenly forgot the positions of two important pieces. However, he remembers some key facts:  

- The **location of the first piece** on the board is \((x_1, y_1)\), where:
  - \(x_{\text{l1}} \leq x_1 \leq x_{\text{r1}}\)
  - \(y_{\text{l1}} \leq y_1 \leq y_{\text{r1}}\)  

- The **location of the second piece** on the board is \((x_2, y_2)\), where:
  - \(x_{\text{l2}} \leq x_2 \leq x_{\text{r2}}\)
  - \(y_{\text{l2}} \leq y_2 \leq y_{\text{r2}}\)  

- The chessboard cells corresponding to the pieces are of the **same color**.  

In other words, he doesn't remember the exact positions of the pieces. However, for each piece, he is sure about the part of the board where it can be, defined as a rectangular submatrix described by four coordinates.  

#### Additional Rules:  
- Two pieces **cannot** occupy the same cell.  

Now, the grandmaster wonders:  
**How many possible placements of these two pieces are there if all the conditions are satisfied?**  

---

### Input Format  

1. **First piece constraints:**  
   - The first line contains an integer \(x_{\text{l1}}\), the minimum possible row of the first piece.  
   - The second line contains an integer \(x_{\text{r1}}\), the maximum possible row of the first piece.  
   - The third line contains an integer \(y_{\text{l1}}\), the minimum possible column of the first piece.  
   - The fourth line contains an integer \(y_{\text{r1}}\), the maximum possible column of the first piece.  

2. **Second piece constraints:**  
   - The fifth line contains an integer \(x_{\text{l2}}\), the minimum possible row of the second piece.  
   - The sixth line contains an integer \(x_{\text{r2}}\), the maximum possible row of the second piece.  
   - The seventh line contains an integer \(y_{\text{l2}}\), the minimum possible column of the second piece.  
   - The eighth line contains an integer \(y_{\text{r2}}\), the maximum possible column of the second piece.  

---

### Constraints  

- \(1 \leq x_{\text{l1}} \leq 8\)  
- \(x_{\text{l1}} \leq x_{\text{r1}} \leq 8\)  
- \(1 \leq y_{\text{l1}} \leq 8\)  
- \(y_{\text{l1}} \leq y_{\text{r1}} \leq 8\)  
- \(1 \leq x_{\text{l2}} \leq 8\)  
- \(x_{\text{l2}} \leq x_{\text{r2}} \leq 8\)  
- \(1 \leq y_{\text{l2}} \leq 8\)  
- \(y_{\text{l2}} \leq y_{\text{r2}} \leq 8\)  

---

### Task  

Calculate the total number of valid placements of the two pieces under the given constraints.  

