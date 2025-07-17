An index of topics from a student's notebook on Java programming, covering functions, encapsulation, and constructors.

### Page 1: Index

| S.No. | Date | Topic | Teacher's Sign & Remark |
| :--- | :--- | :--- | :--- |
| 1 | 10th March, 2015 | Functions (User-Defined) | (Signature) good |
| 2 | 29th April, 2025 | Constructors | |

***

### Page 2: Encapsulation - Simple Interest Program

**ENCAPSULATION**

<u>Program for simple interest</u>
- **class name** -> Bank
- **Data members** -> SI, amt, P, R, T
- **Members functions** -> `Display()`, `Compute()`, `Accept()`

Calculate simple interest and amt for the given data by user.
```java
import java.util.Scanner;

class Bank {
    int P, R, T, SI, Amt;

    void Accept() // to accept principal, rate and time
    {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the principal");
        P = sc.nextInt();
        System.out.println("Enter the rate of interest");
        R = sc.nextInt();
        System.out.println("Enter the time in years");
        T = sc.nextInt();
    }

    void Compute() {
        SI = (P * R * T) / 100; // Calculating SI
        Amt = P + SI; // Calculating amount
    }

    void Display() {
        System.out.println("Simple Interest = " + SI);
        System.out.print("Amount = " + Amt);
    } // Displaying SI and amount

    public static void main() {
        // Accept(); // accepting P, R, T
        // Compute(); // calculations
        // Display(); // Printing
        
        Bank ob = new Bank();
        ob.Accept(); // accepting data
        ob.Compute(); // calculations
        ob.Display(); // Printing
    } // end of main
} // end of class
```

***

### Page 3: Marksheet Program

`ob` in the `main` method is responsible for calling the functions, taking input from user, doing computation and displaying output. Outsiders can access methods provided by object and data is secured from accidental alteration.

<u>PROGRAM TO COMPUTE THE AVERAGE MARKS AND GRADE FOR A GIVEN SET OF DATA BY THE USER</u>
- **Class name:** Marksheet
- **Data members:** String `name`, double `m1`, `m2`, `m3` (marks of 3 subjects out of 100).
- **Member methods:**
  - `accept()` -> To accept the marks of 3 subjects
  - `compute()` -> To calculate the avg marks and grade
  - `display()` -> to display all the details. In main, create an object and call the method `accept`.

**Grading:**
- 80 - 100 -> Grade A
- 60 - 79 -> B
- 50 - 59 -> Grade C
- <50 -> D

```java
import java.util.Scanner;

class Marksheet {
    String name, grade;
    double m1, m2, m3, avgmarks;

    void Accept() {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the marks of 3 subjects out of 100");
        m1 = sc.nextDouble();
        m2 = sc.nextDouble();
        m3 = sc.nextDouble();
        
        // Accepting marks from user
        
        System.out.println("Enter your name");
        name = sc.nextLine(); // Note: This might have issues after nextDouble()
    } // Accepting name and marks from user

    void Compute() {
        avgmarks = (m1 + m2 + m3) / 3;
        if (avgmarks < 50)
            grade = "D";
```

***

### Page 4: Marksheet Program (contd.) & Variable Table

```java
        else if (avgmarks < 60)
            grade = "C";
        else if (avgmarks < 80)
            grade = "B";
        else
            grade = "A";
    } // calculating average marks and hence calculating grade

    void Display() {
        System.out.println("Your name is " + name);
        System.out.print("Your grade is " + grade);
    } // printing name and grade

    public static void main() {
        Marksheet obj = new Marksheet(); // creating object
        obj.Accept();
        obj.Compute();
        obj.Display();
        // calling member methods to calculate and display grade
    } // end of main() method
} // end of class
```

**TABLE**
| VARIABLE | DATA TYPE | DESCRIPTION |
| :--- | :--- | :--- |
| name | String | To store student's name |
| grade | String | To store student's grade |
| sc | Scanner | To access Scanner input methods |
| obj | Marksheet | To access Marksheet member methods |
| m1 | double | To store marks of first subject |
| m2 | double | To store marks of second subject |
| m3 | double | To store marks of third subject |
| avgmarks | double | To store avg marks of 3 subjects |

***

### Page 5: Functions / Methods

**FUNCTIONS / METHODS**
e.g. `public static void main(String args[])`

**STRUCTURE OF FUNCTION**
`<Access specifier> <static> <return type> <function name> (list of arg);` -> prototype
e.g. `public static int xyz(int a, b)` -> Function definition

**Function definition** -> It is the combination of access specifier, static keyword, prototype of the function, function name and list of arguments.

**COMPONENTS OF FUNCTION**
- Function prototype / function declaration
- Function definition
- Function invoking

**FUNCTION INVOKING**
The process of executing the function definition body to run the given set of statements is known as invoking / calling / executing / accessing the function.

`<Class name> <object> = new <classname>();`
OR
`<class name> <object>;`
`<object> = new <classname>();`

So for class `XYZ`,
`XYZ obj = new XYZ();`

<u>Write a program to calculate the factorial of a given number given by user using function.</u>
```java
import java.util.*;

class Factorial {
    public void Fact(int n) {
        int f = 1;
        for (int i = 1; i <= n; i++) // loop runs from 1 to n
        {
            f *= i; // calculating factorial
        }
        System.out.println("Factorial = " + f); // printing factorial
    } // end of Fact
```

***

### Page 6: Factorial Program (contd.) & Sum Program

```java
    public static void main() {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int m = sc.nextInt(); // Accepting the no.
        
        // Fact(m); // invoking function to calculate factorial
        
        Factorial obj = new Factorial();
        obj.Fact(m); // declaring object and invoking Fact()
    } // end of main()
} // end of class
```

**TABLE**
| VARIABLE | DATA TYPE | DESCRIPTION |
| :--- | :--- | :--- |
| obj | Factorial | To invoke member method `Fact()` |
| n | int | To serve as function argument for `Fact()` function to accept the no. |
| f | int | To store the value of factorial of the no. |
| i | int | To serve as loop counter variable for factorial loop |

<u>WAP to accept 2 no.s from user and display the sum of the no.s.</u>
```java
import java.util.Scanner;

class Sum_of_Two_Nos {
    int m, n;
    
    void Accept() // to accept the no.s through Scanner
    {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the 2 no.s");
        m = sc.nextInt();
        n = sc.nextInt();
    } // Accepting the 2 no.s
    
    void Sum(int a, int b) {
        int c = a + b;
        System.out.print("Sum = " + c);
    } // Calculating and printing the sum
    
    public static void main() {
        Sum_of_Two_Nos obj = new Sum_of_Two_Nos();
        obj.Accept(); // calling Accept() to take input
        obj.Sum(m, n); // calling of Sum() function
    }
}
```

***

### Page 7: Variable Table & Function Types

**TABLE**
| VARIABLE | DATA TYPE | DESCRIPTION |
| :--- | :--- | :--- |
| m | int | To accept value of first no. from user |
| n | int | To accept value of second no. from user |
| a | int | To store value of first argument of `Sum()` |
| b | int | To store value of second argument of `Sum()` |
| c | int | To store the value of the sum of the nos |
| sc | Scanner | To access Scanner input methods |
| obj | Sum_of_Two_Nos | To invoke the `Sum()` function |

**Return keyword** -> Used to return a value from the function and immediately terminates the function. They transfer the control back to the function-calling statement.

**User defined function** -> It is a group of statements separate out of the `main()` module and defined within a user defined name and performs a specific function as defined by user.

**TYPES OF FUNCTIONS**
- **Non return type (void)**
- **Return type** (double, int, char, long, float...)

- If some / any function is declared with `static` keyword then no object is required to call it from a static method.
- Non-return type is always processed by `void` keyword.
- Return type method is always processed by primitive data-type.

<u>WAP in Java to calculate the value of nCr by accepting values of n and r from user, where nCr = n! / ((n-r)! * r!)</u>
```java
import java.util.Scanner;

class NCR {
    public static int factorial(int p) {
        int f = 1;
```

***

### Page 8: nCr Program & Error Identification

```java
        for (int i = p; i != 0; i--) // Loop for factorial calculation
        {
            f *= i; // calculating factorial
        }
        return f; // returning value to calling method
    } // end of factorial()

    public static void main() {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the values of n and r");
        int n = sc.nextInt();
        int r = sc.nextInt(); // Accepting the values
        
        int f1 = factorial(n); // Calculating n factorial
        int f2 = factorial(r); // Calculating factorial of r
        int f3 = factorial(n - r); // Calculating (n-r) factorial
        
        System.out.print("nCr = " + (f1 / (f2 * f3)));
        // Calculating and printing nCr
    } // end of main()
} // end of class
```
**TABLE**
| VARIABLE | DATA TYPE | DESCRIPTION |
| :--- | :--- | :--- |
| f1 | int | To store value of factorial of n |
| f2 | int | To store factorial of r |
| f3 | int | To store factorial of (n-r) |
| p | int | To store factorial of p |
| i | int | To serve as argument for factorial() function |
| sc | Scanner | To access Scanner input methods |
| n | int | To store value of n from user |
| r | int | To accept value of r from user |

<u>Q. Identify the error</u>
```java
void fact() {
    int n;
    int f = 0;
    for (i = n; i > 0; i--) {
        f = f * i;
    }
    return f;
}
```

***

### Page 9: Error Correction & Method Types

**Error -> `i` is not declared**
**Syntax error -> `return f` is invalid for `void` return type**
**Logical error -> Infinite loop if `i <= 0` or the loop will not work if the condition is `i > 0`**
**If `f` is zero, then the whole factorial will be zero.**

<u>Code with rectifications:</u>
```java
int fact() {
    int n;
    int f = 1;
    for (int i = n; i > 0; i--) {
        f = f * i;
    }
    return f;
}
```

**DIFFERENCE BETWEEN STATIC AND INSTANCE METHODS**

| STATIC METHOD | INSTANCE METHOD |
| :--- | :--- |
| This method is created using `static` keyword. | This method does not require `static` keyword for creation. |
| This method is invoked or called without an object. | An object is needed to invoke or call this method. |
| This method can access `static` methods and `static` variables and cannot access `instance` methods and `instance` variables without the help of an object. | This method can access `instance` methods and variables as well as `static` methods and `static` variables. |

**VARIABLES WITHIN CLASS**
- **INSTANCE VARIABLE** -> The variables declared or created within the class but outside the function or method or scope is called instance variable.
- **STATIC VARIABLE** -> The variable declared or created using `static` keyword within the class but outside the function or method or scope. Its value remains same throughout the program.
  e.g. `static int a = 20;`
  `a = 10;` -> Error
- **LOCAL VARIABLE** -> The variable declared or created within the method, functions or scopes.

***

### Page 10: Twin Primes Program

<u>WAP in Java to check if two given no.s are Twin Primes.</u>
(Two no.s are said to be twin primes if their no.s are primes themselves)

```java
import java.util.Scanner;

class Twin_Primes {
    public static boolean isPrime(int a) {
        boolean f = true;
        for (int i = 2; i < a; i++) // loop to check for prime No.
        {
            if (a % i == 0) // if a is divisible by any other no.
            {
                f = false; // a is not a prime no. if it is divisible
                break; // terminating the loop immediately
            } // end of if()
        }
        return f;
    } // end of isPrime()

    public static void main() {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter two numbers");
        int m = Math.abs(sc.nextInt()); // Accepting absolute value of 1st no.
        int n = Math.abs(sc.nextInt()); // Accepting absolute value of 2nd no.

        if (isPrime(m) && isPrime(n) && (Math.abs(m-n) == 2))
        // checking if entered nos are prime and they differ by 2
        {
            System.out.println(m + " and " + n + " are Twin Primes");
        } else // if entered nos are not prime or they don't differ by 2
        {
            System.out.println(m + " and " + n + " are not Twin Primes");
        }
        // printing messages accordingly
    } // end of main() function
} // end of class
```
**TABLE**
| VARIABLE | DATA TYPE | DESCRIPTION |
| :--- | :--- | :--- |
| a | int | To serve as argument for `isPrime()` function |
| m | int | To store the first no. as entered by user |
| n | int | To store the second no. as entered by user |
| sc | Scanner | To access input methods of Scanner class |
| i | int | To serve as loop counter variable in prime-check loop |
| f | boolean | To store the boolean value. If the no. is prime it stores true and if it is not, then it stores false |

* `Math.abs`

***

### Page 11: Function Calling and Parameters

**FUNCTION - CALLING**

**ARGUMENTS** -> The list of variables along with their respective datatypes given / passed at the time of function definition and without datatypes at the time of function calling / invoking are known as arguments / parameters.

- **ACTUAL PARAMETERS**
  The parameters that appear during function calling are called actual parameters. They determine the actual values passed through the function as arguments.
- **FORMAL PARAMETERS**
  The parameters that appear in front of a function definition are formal parameters. They are the part of the function definition and the function.

```java
// import java.util.Scanner;
class Parameters {
    int xyz(int a, int b) // a and b are formal parameters
    {
        return a + b;
    }
    
    void main() {
        // Scanner sc = new Scanner(System.in);
        // int m = sc.nextInt();
        // int n = sc.nextInt();
        
        int sum = xyz(m, n); // m and n are actual parameters
    }
}
```

<u>WAP to compute and print the sum of given series till n terms `1! + 2! + 3! ...`</u>
Your program will show actual and formal parameters used in the program.
```java
import java.util.Scanner; // importing Scanner

class Sum_Series {
    public static int Fact(int a) // a is the formal parameter
    {
        int f = 1;
        for (int i = 1; i <= a; i++) // loop for calculating factorial
        {
            f *= i;
        }
        return f; // returning value of factorial
    }
    
    public static void main() {
```

***

### Page 12: Call by Value

```java
        int sum = 0;
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the no. of terms");
        int n = sc.nextInt();
        
        for (int i = 1; i <= n; i++) // loop for calculating sum of series
        {
            sum += Fact(i); // calculating sum by adding factorials. 'i' is actual parameter.
        }
        System.out.print("The sum of series = " + sum);
    }
}
```

**CALL BY VALUE** -> Also known as pass by value, it is the method of calling a function by a value. The formal parameters will receive duplicate values from the actual counterparts. In the case of this method, there exist two copies of the same value in the memory, as there are two separate memory locations for them.

Given below, is an example of a function called using this method.
```java
class Example {
    public void change(int a) {
        a++;
        System.out.println("Value of a = " + a);
    }
    
    public void main() {
        int x = 10;
        System.out.println("Before function call " + x);
        change(x);
        System.out.println("After function call " + x);
    }
}
```
We can see that there exist two separate variables `x` and `a` in the memory. `x` is for `main()` method and `a` for `change` method.
During the function call to `change()`, the variable `a` will receive a duplicate copy of the value 10.

***

### Page 13: Call by Reference

**OUTPUT**
```
Before function call 10
Value of a = 11
After function call 10
```
So, even after the execution of the `change()` function, the value of `a` gets incremented to 11. But there will be no change in the value of the variable (`x`).
In conclusion, in the call-by-value method, whatever changes are made in the formal parameter, it will not be reflected back to the actual parameter.

**CALL BY REFERENCE (or Pass-By-Reference)**:
When a function is called by reference, the formal parameter will receive the address of the actual parameter instead of duplicate values. In this case, though there exist 2 separate memory locations in the form of 2 variable names, they share the same value.
```java
class Example {
    int a;
    
    public void change(Example ob) // Example is class name and ob is object
    {
        ob.a++; // linking a with the memory location of ob
        System.out.println("Value of a in change = " + ob.a);
    }
    
    public static void main() {
        Example obj = new Example();
        obj.a = 10;
        
        System.out.println("Before function call = " + obj.a);
        obj.change(obj);
        System.out.println("After " + obj.a);
    }
}
```
**OUTPUT:-**
```
Before function call = 10
Value of a in change = 11
After 11
```
We can see that there exist 2 separate objects `obj` (for the `main()` method) and `ob` (for the `change()` method) in the memory. Now, when the `main()` method, `ob.a` will receive the address of `obj.a` instead of the duplicate value of the variable `a`. Thus, after the execution of the function `change()`, when the value of `ob.a` gets incremented to 11, the same will be reflected back to `obj.a` as well.

***

### Page 14: Function Overloading

In conclusion, in the call-by-reference method whatever changes are made in formal parameters will reflect back in the actual parameter(s). Generally, whenever any `object` or `array` or `String` is passed to a function, it is passed to a function, it is called by reference and for all other types of variables it is called by value.

**FUNCTION OVERLOADING**
The logical process of defining various functions by the same name that are differentiated by their data types or number of formal parameters, is known as function overloading.

**[Advantages of function overloading]**
- It increases the readability of code.
- It makes the program code less complex.
- It gives the flexibility to invoke the same method for different argument values, e.g. `Math.pow()`
- It reduces the execution time as well as processor's time.
- It also helps in the 'divide and conquer' process.

**Example -**
If we define a function `Area()`, the probable overloading of it will be
- `Area()` of Rhombus, `Area()` of Equilateral Triangle, `Area()` of Trapezoid
or any other geometrical figures can be calculated using the same function `Area()`.

<u>SAMPLE PROGRAM TO DEMONSTRATE OVERLOADING OF STATIC METHODS</u>
```java
class Sum {
    // overloading first method
    public static int Sum(int x, int y) {
        return (x + y);
    } // end of method 1
    
    public static double Sum(double a, double b) {
        return (a + b);
    } // end of method 2
    
    public static void main() {
```

***

### Page 15: Pure and Impure Functions

```java
        System.out.println(Sum(10, 20));
        System.out.println(Sum(10.5, 20.5));
    } // end of main()
} // end of class
```

**PURE FUNCTION**
- The function that does not change or modify the state of arguments and returns the same, if arguments are passed is called pure function.
  e.g., `pow()`, `sqrt()`, `cbrt()`, `print()`
```java
public int main(int a, int b) {
    return a * b;
}
```

**IMPURE FUNCTION**
- The function that may not return a value, but changes or modifies the state of the variable is called a mutator or impure function.
  e.g., `random()`, `time()`
```java
public int main(int a, int b) {
    return (++a * b--);
}
```

***

### Page 16: Constructors

**CONSTRUCTORS**
- A Constructor is a special member method of the class, having the same name as the class.
- It is used to initialize the data members of a class, i.e object at the time of memory allocation. This is known as object instantiation.

**PROPERTIES**
A constructor of a class has the following properties -
- It has the same name as the class.
- It has no return type not even `void`.
- It must be a `public` member of a class.
- It cannot be called explicitly unlike other methods.
- It is called implicitly at the time of object creation using the `new` keyword.
- It is mainly used to initialize the data members (instance variables or objects) of a class at the time of object creation.
- A class can have multiple constructors, but in that case, each constructor must be different from the other one(s) in their function signature. The concept of multiple constructors in a class is known as constructor overloading.

**TYPES OF CONSTRUCTORS**
- **Parameterised constructors**
  - It is a constructor that has parameters in its function definition and initializes the data members passed by those parameters.
- **Non parameterised (default) constructors**
  - It is a constructor that does not have any parameter in its function definition and this type of constructor generally initializes the data members with either their default values or with some fixed set of values.

**DEFAULT CONSTRUCTORS** -> A non-parameterized constructor that initializes the data members of the class with their default values.

***

### Page 17: Overloading `display()` Function

<u>Define a class to overload a function `display()` with the following prototype -</u>
1. `void display()` ->
   ```
   1 2 1 2 1
   1 2 1 2 1
   1 2 1 2 1
   ```
2. `void display(int n, int m)` -> Sum = m + m²/2! + m³/3! ... mⁿ/n!
3. `void display(double a, double b, double c)` -> z = p * q, where p = (a+b)/c and q = a+b+c. Print the value of z.

```java
class Func_Overloading {
    void display() {
        for (int i = 3; i != 0; i--) // loop for printing rows
        {
            for (int j = 5; j != 0; j--) // loop for printing the number
            {
                if (j % 2 != 0) // if column no. is odd
                {
                    System.out.print("1" + " ");
                } else // if column no. is even
                {
                    System.out.print("2" + " ");
                }
            } // end of inner loop
            System.out.println(); // new line
        } // end of outer loop
    } // end of 1st display() function
    
    void display(int m, int n) {
        double sum = 0.0;
        for (int k = 1; k <= n; k++) {
            double num = Math.pow(m, k); // Calculating numerator
            double den = 1;
            for (int y = k; y != 0; y--) // factorial
            {
                den *= y; // calculating denominator as factorial of k
            }
            sum += (num / den); // calculating sum
        } // end of 2nd display function
        System.out.println("Sum = " + sum); // Printing sum
    }
    
    void display(double a, double b, double c) {
        double p, q, z; // initializing the variables
        p = (a + b) / c; // calculating value of p
        q = a + b + c; // calculating value of q
```

***

### Page 18: Overloading `display()` (contd.) & Variable Table

```java
        z = p * q; // calculating value of z
        System.out.print("Value of z = " + z); // Printing z
    } // end of 3rd display() function
    
    public static void main() {
        Func_Overloading ob = new Func_Overloading();
        // creating object of the class
    }
}
```
**TABLE**
| VARIABLE | DATA TYPE | DESCRIPTION |
| :--- | :--- | :--- |
| i | int | To serve as loop-counter variable for outer loop for printing |
| j | int | To serve as loop-counter variable for printing the no |
| m | int | To serve as first argument for 2nd method |
| n | int | To serve as second argument for 2nd method |
| sum | double | To store value of sum of series |
| k | int | To serve as LCV for outer loop |
| y | int | To serve as LCV for factorial loop |
| num | double | To store value of numerator of term |
| den | double | To store value of denominator of term |
| a | double | To serve as first argument of third function |
| b | double | To serve as second argument of third function |
| c | double | To serve as third argument of third function |
| p | double | To store value of sum of a and b divided by c |
| q | double | To store sum of a, b and c |
| z | double | To store product of p and q |

***

### Page 19: Constructors (Continued)

**CONSTRUCTORS (Continued..)**

**Parameterised constructor**
- Example:- `SI(double p, double r, int t)` is a parameterised constructor that is initializing the data members `principal`, `rate` and `time` with the values from `p`, `r`, `t` respectively.

**Default (Non-parameterised constructor)**
- Example:-
```java
class ExampleStudent {
    // data members
    int roll;
    String name;
    double marks;
    char grade;
    
    public ExampleStudent() // non-parameterized constructor
    {
        roll = 0;
        name = "";
        marks = 0.0;
        grade = '\u0000';
    }
}
```
In the above program code, the non-parameterized constructor is initializing the data members with their default values (0 for int, 0.0 for double, `""` for String and `\u0000` for char data type).

Also if a programmer does not declare any constructor in the class, then at the time of object creation, the compiler creates the default constructor (of the System) to initialize the data members with their default values.
