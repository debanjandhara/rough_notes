### Core Java Concepts You MUST Know

Before you start, quickly review these topics. Every single question in your file uses them:
1.  **POJO (Plain Old Java Object):** A simple class with `private` attributes, a constructor to initialize them, and `public` getters/setters.
2.  **Arrays of Objects:** How to declare, create, and populate an array of objects (e.g., `Employee[] emp = new Employee[4];`).
3.  **Static Methods:** Understanding how to define and call methods like `public static void myMethod(...)` from `main`.
4.  **Scanner Class:** Reading different types of input (`nextInt()`, `nextLine()`, `nextDouble()`, etc.) and handling the `nextLine()` trap after reading numbers.
5.  **Loops & Conditionals:** Standard `for` loops and `if/else` statements to iterate through arrays and make decisions.
6.  **String Manipulation:** Using methods like `.equalsIgnoreCase()`, `.split()`, and `.charAt()`.
7.  **Basic Sorting Logic:** The classic nested `for` loop (Bubble Sort) is used frequently in the solutions to sort arrays of objects.

---

### Your 2-Day Exam Preparation Plan

This plan is structured to build your confidence and skills progressively.

### **Day 1: Building the Foundation**

#### **Morning Session: Core Java & Easy Problems (15 Marks)**
Let's start with the basics to get you comfortable with Java syntax, logic, and handling input/output. These questions focus on a single algorithm.

1.  **Question: `Calculator.java`**
    *   **Difficulty:** Easy (15 Marks)
    *   **Topic Tags:** `[Basic I/O]`, `[Conditionals]`
    *   **Why solve it?** This is the perfect warm-up. It ensures you can take user input and use `if-else` or `switch` statements correctly, which is fundamental for all other problems.

2.  **Question: `ReverseString.java`**
    *   **Difficulty:** Easy (15 Marks)
    *   **Topic Tags:** `[Loops]`, `[String Manipulation]`
    *   **Why solve it?** This teaches you how to iterate through a string and manipulate it character by character—a core skill.

3.  **Question: `CountVowel.java`**
    *   **Difficulty:** Easy (15 Marks)
    *   **Topic Tags:** `[Loops]`, `[String Manipulation]`, `[Conditionals]`
    *   **Why solve it?** It combines loops and conditionals to analyze a string. This pattern of iterating and checking is used in almost every difficult problem.

#### **Afternoon Session: Intro to OOP and Arrays (The 35-Mark Pattern)**
Now, let's tackle the structure of the harder problems. The goal here is not to solve the hardest logic yet, but to master the setup.

4.  **Question: `IPA14` (Movie Budget)**
    *   **Difficulty:** Medium (35 Marks)
    *   **Topic Tags:** `[OOP Basics]`, `[Arrays of Objects]`, `[Filtering]`
    *   **Why solve it?** This is your ideal introduction to the 35-mark question format. You will practice:
        1. Creating a simple `Movie` class (POJO).
        2. Reading input to create an array of `Movie` objects.
        3. Implementing a static method that **filters** the array based on a condition (`genre`).

5.  **Question: `IPA15` (Phone Price)**
    *   **Difficulty:** Medium (35 Marks)
    *   **Topic Tags:** `[OOP Basics]`, `[Arrays of Objects]`, `[Filtering]`, `[Calculation]`
    *   **Why solve it?** It builds directly on the previous problem. After filtering the array (by brand), you will perform a **calculation** (summing the prices). This covers two major patterns: filtering and aggregating data.

#### **Evening Session: Sorting and Searching**
Sorting is a critical skill that appears in many of the harder problems.

6.  **Question: `IPA12` (Medicine Price)**
    *   **Difficulty:** Medium (35 Marks)
    *   **Topic Tags:** `[Arrays]`, `[Filtering]`, `[Sorting]`
    *   **Why solve it?** This problem asks you to filter medicines and return their prices in sorted order. It's a great way to practice sorting on a simple array of integers (`int[]`) before sorting complex objects.

7.  **Question: `IPA18` (Antenna VSWR)**
    *   **Difficulty:** Medium (35 Marks)
    *   **Topic Tags:** `[Arrays of Objects]`, `[Filtering]`, `[Sorting Objects]`
    *   **Why solve it?** This is the next logical step: sorting an array of **custom objects** (`Antenna`) based on an attribute (`antennaVSWR`). The provided solution uses a bubble sort, which is a perfect and easy-to-understand sorting algorithm to learn.

---

### **Day 2: Mastering Complex Problems**

#### **Morning Session: Combining Logic (The Nth Element)**
This is a very common and high-value problem type. If you can solve this, you are in great shape.

8.  **Question: `2nd_Lowest_Salary` (Employee)**
    *   **Difficulty:** Hard (35 Marks)
    *   **Topic Tags:** `[Sorting Objects]`, `[Arrays of Objects]`, `[Edge Cases]`
    *   **Why solve it?** This is a classic question. It forces you to combine sorting with careful logic to find the "second" element, handling potential duplicates and edge cases (like arrays with fewer than two elements). It's a comprehensive test of everything from Day 1.

9.  **Question: `IPA10` (Employee with Second Highest Rating)**
    *   **Difficulty:** Hard (35 Marks)
    *   **Topic Tags:** `[Sorting Objects]`, `[Filtering]`
    *   **Why solve it?** This is a variation of the previous problem. It adds a **filtering** step (`who are not using company transport`) before finding the second-highest element. Solving this proves you can combine multiple requirements.

#### **Afternoon Session: Advanced Concepts**
Let's cover the remaining unique concepts from your file.

10. **Question: `Company_Employee`**
    *   **Difficulty:** Hard (35 Marks)
    *   **Topic Tags:** `[OOP Basics]`, `[Arrays of Objects]`, `[Calculation]`, `[Filtering]`
    *   **Why solve it?** This problem involves two custom classes (`Employee` and `Company`) and asks for multiple calculations (average salary, max salary) and a filter. It’s great practice for managing slightly more complex class relationships.

11. **Question: `IPA42` (Person, Student, Faculty)**
    *   **Difficulty:** Hard (35 Marks)
    *   **Topic Tags:** `[OOP Basics]`, `[Inheritance]`
    *   **Why solve it?** This is the **only** problem in your file that uses **inheritance** (`Student extends Person`). It's a critical OOP concept that you must not miss. Understanding how to use `super()` in the constructor is key.

#### **Evening Session: Final Review and Polish**
Let's finish with problems that test specific skills and serve as a final review.

12. **Question: `IPA17` (Student Date)**
    *   **Difficulty:** Medium (35 Marks)
    *   **Topic Tags:** `[String Manipulation]`, `[Filtering]`, `[Sorting Objects]`
    *   **Why solve it?** This question requires you to parse a date string (`DD/MM/YYYY`) to extract the month. This is a fantastic test of your string manipulation skills (`.split("/")` is the easiest way).

13. **Final Review: `IPA3` (Student Score)**
    *   **Difficulty:** Hard (35 Marks)
    *   **Topic Tags:** `[Arrays of Objects]`, `[Filtering]`, `[Calculation]`, `[Sorting]`
    *   **Why solve it?** This problem is a perfect final review. It has two methods that test everything: one calculates a count based on a filter, and the other finds the second-highest score for a different filtered group. If you can solve this comfortably, you are ready for the exam.
