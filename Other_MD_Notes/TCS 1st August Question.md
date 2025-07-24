Of course! Here are the details of the programming questions demonstrated in the video, presented in a clear and organized format.

***

### **Problem 1: Find the Index of a Character**

**Question Details:**
Write a Java program that takes a string and a character as input. The program should find the index of the first occurrence of the given character within the string and print that index to the console.

**Example from the video:**
*   **String Input:** `Xplore`
*   **Character Input:** `r`
*   **Output:** `4`
*   **Explanation:** In the string "Xplore", the character 'r' is found at index 4 (using 0-based indexing).

***

### **Problem 2: Count Lowercase Characters**

**Question Details:**
Write a Java program that takes a string as input and counts the total number of lowercase alphabetical characters within it. The final count should be printed to the console.

**Example from the video:**
*   **String Input:** `DataBaSe`
*   **Output:** `5`
*   **Explanation:** The lowercase characters in "DataBaSe" are 'a', 't', 'a', 'a', and 'e', for a total of 5.

***

### **Problem 3: Print Last Character of Each Word**

**Question Details:**
Write a Java program that takes a sentence (string) as input. The program must find the last character of every word in the sentence and print them together as a single string.

**Condition:**
*   Ignore any "words" that contain digits or are just whitespaces.

**Example from the video:**
*   **Input String:** `Hey3 Java Learners`
*   **Output:** `as`
*   **Explanation:**
    1.  The word "Hey3" is ignored because it contains a digit.
    2.  The last character of "Java" is 'a'.
    3.  The last character of "Learners" is 's'.
    4.  Concatenating these results gives "as".

***

### **Problem 4: Count Spaces with a Condition**

**Question Details:**
Write a Java program to compute the number of spaces in a given string.

**Condition:**
*   If the total count of spaces is greater than or equal to 3, print the count.
*   Otherwise (if the count is less than 3), print the string "NA".

**Examples from the video:**
*   **Example 1:**
    *   **Input:** `Hello what is your name`
    *   **Output:** `4` (since 4 is greater than or equal to 3)
*   **Example 2:**
    *   **Input:** `hello arpit`
    *   **Output:** `NA` (since the space count is 1, which is less than 3)

***

### **Problem 5: Sum of Digits and Divisibility Check**

**Question Details:**
Write a Java program that takes an integer as input and calculates the sum of its individual digits.

**Condition:**
*   If the calculated sum is divisible by 3, the program should print `True`.
*   Otherwise, it should print `False`.

**Examples from the video:**
*   **Example 1:**
    *   **Input:** `123`
    *   **Logic:** 1 + 2 + 3 = 6. Since 6 is divisible by 3, the output is `True`.
    *   **Output:** `True`
*   **Example 2:**
    *   **Input:** `1234`
    *   **Logic:** 1 + 2 + 3 + 4 = 10. Since 10 is not divisible by 3, the output is `False`.
    *   **Output:** `False`

***

### **Problem 6: Find the Largest Word in a Sentence**

**Question Details:**
Write a Java program to find and print the largest word from a given sentence.

**Condition:**
*   If two or more words have the same maximum length, the program should print the first one that appears in the sentence.

**Example from the video:**
*   **Input:** `TCS is the best Company ever`
*   **Output:** `Company`
*   **Explanation:** The word "Company" has a length of 7, which is the longest in the sentence.
