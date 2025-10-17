### JAVASCRIPT
**Definition:** JavaScript is a fundamental prerequisite skill in any web developer's repertoire.
**Notes:**
* Designing a web page with just HTML and CSS is not sufficient; there needs to be a layer that can handle custom validations and business logic that HTML just cannot support.
* Originally designed to be just a language that can run on the browser, JavaScript has now evolved to be both a client and server-side language.
* JavaScript has led to the creation of several frameworks and consequently, far more interactive and dynamic web pages.
* This course is designed to introduce the learner to the fundamental concepts of JavaScript and then move on to advanced concepts like testing and usage of Web APIs.
* These features help developers deal with complex requirements and make the code shorter and more efficient.
* Target audience: Developers
*CrossReferences:* HTML, CSS, Web APIs

### JavaScript Learning Outcomes
**Definition:** JavaScript course is designed to introduce the basic features of JavaScript and its object-oriented features. This course also deals with handling asynchronous programming. It will help you to learn JavaScript through hands-on approach.
**Attributes:**
* Write a program using JavaScript to solve a given problem with proper syntax and semantics
* Perform asynchronous operations
* Deal with asynchronous data using promises
* Apply DOM concept to access or manipulate a web page components
* Perform form validation using event handlers for a given requirement
*CrossReferences:* promises, DOM, event handlers

### ECMA Script
**Definition:** ECMA is an committee which lays down the standards for a general purpose language that can also run on the browser.
**Notes:**
* You can download the ES2020 specification and create your own implementation of this standard.
* JavaScript is a language which implements the standards.
* There are many other languages like JScript and ActionScript which also implement the ECMAScript standard.
*CrossReferences:* ES2020 specification, JScript, ActionScript

### ECMAScript Versions
**Notes:**
* There are many versions of ECMAScript specification and the latest is ES2018.
* ECMAScript went through a major change from version 5 to 6.
* ECMAScript 6 or ES6 was released in 2015.
* The committee decided to release a newer version of the standard every year around June, and to include the year in the version name to avoid confusion.
* The major ECMAScript versions are: ES6 (also called ES2015), ES2016, ES2017, ES2018, ES2019, ES2020.
* We will be covering the latest version of the language, which is an implementation of ES2018.
* All browsers do not support all the features of ES specifications (e.g., IE does not support most of the ES6 features and above).
* Developers usually will transpile the ES6+ code into ES5 syntax using Babel.
* We will not be covering Babel in this course and will be using Chrome.
*CrossReferences:* ES2018, ES6, ES5, Babel, Chrome

### About JavaScript
**Definition:** JavaScript is a language developed in 1995, even before ECMAScript. It was later modified to adopt to the ES specifications. JavaScript was originally created as a scripting language for the web browser. But over the years, it has evolved into a full fledged general purpose language, that can not only run on the browser, but also on the server side.
**Examples:**
* Chrome uses V8 engine.
* FireFox uses SpiderMonkey engine.
* Edge uses Chakra engine.
* Environments outside the browser using JavaScript engine: Node, Deno.
* Other environments: Photoshop, Flash player, etc.
**Notes:**
* JavaScript is an interpreted language created by Brendan Eich.
* The code is interpreted and executed by what is called a JavaScript engine (also called as JavaScript Virtual Machine).
* In JS, even though (semicolon) is optional at the end of each statement, it is ideal to use it to avoid unforeseen consequences in the code execution.
**CommonMistakes:**
* ⚠️ Unforeseen consequences due to missing semicolon (avoided by using semicolon).
*CrossReferences:* ECMAScript, Brendan Eich, Node, Deno

### A Quick look at JavaScript
**Definition:** JavaScript has a simple syntax and supports all the fundamental programming constructs like variables, arrays, loops, conditional statement, exception handling, etc.
*CrossReferences:* variables, arrays, loops, conditional statement, exception handling

### Datatypes
**Notes:**
* We will look at undefined and object later.
**Attributes:**
* number
* string
* boolean
* null
* undefined
* object

### Comments
**Syntax:**
* Single line comments: `//`
* Multi-line comments: `/* */`

### Variable
**Syntax:**
```javascript
/* This code illustrates
the various data types*/

ticketCost = 100; // number
placeTovisit = 'New York'; // string
a; // undefined
isGoing = true; // boolean
paragliding = null; // object
```
**Notes:**
* We can create variables directly by giving a name and assigning a value to it.
* Since JS is a dynamically typed language, the type of the variable is automatically determined based on the value assigned to it (e.g., `a="100"` creates a string type variable, `a=100` creates a number type variable).
* Variables in JavaScript cannot have keywords.

### console.log()
**Definition:** console.log() is used to print any value in the console.
**Syntax:**
```javascript
place = "Florida"
console.log(place); // Florida
console.log("Hello World!");// Hello World!
```

### Running JavaScript
**Definition:** There are many ways to run JavaScript. Two ways which you will be using throughout the course are running on Node and running on browser (implied).

#### 1. Running on Node
**Definition:** Node is an environment which uses the Chrome's V8 JavaScript engine.
**Syntax:**
```
node -v
```
```javascript
console.log("Hello World!")
```
```
node demo.js
```
**Notes:**
* To verify Node installation: Open Visual Studio code IDE and press `[Ctrl + \`]` to open the integrated console. Type `node -v`.
* If installed correctly, the terminal output will show the version (e.g., v8.9.1).
* To create first application: Create file `demo.js` (extension `.js`), write JavaScript code, open terminal, and type `node demo.js`.
* Output example: `Hello World!`
*CrossReferences:* Node, V8 JavaScript engine, Visual Studio code IDE

#### 2. Running on browser
(content not found in source)

### Undefined vs Null
**Definition:** undefined and null may seem the same, but they are different.

#### undefined
**Definition:** undefined is a variable which is declared, but not assigned any value.
**Syntax:**
```javascript
var placeTovisit;
console.log(placeTovisit);
// undefined
```
**Notes:**
* We will discuss about 'var' later in the course.

#### null
**Definition:** null is an empty value which means nothing. A variable left unassigned is not null. Null must be assigned explicitly.
**Syntax:**
```javascript
cabDetail = null;
console.log(cabDetail);
// null
```

### Operators
**Definition:** There are several categories of operators in JavaScript.
**Attributes:**
| Operators | Description |
|---|---|
| Assignment Operators | `=`, `+=`, `-=`, `*=`, `/=`, `%=` |
| Arithmetic Operators | `+`, `-`, `*`, `/`, `%`, `++`, `--` |
| Comparison Operators | `==`, `!=`, `===`, `!==`, `>`, `<`, `>=`, `<=` |
| Unary Operators | `typeOf` etc. |
| Logical Operators | `&&`, `||`, `!` |
| Conditional (Ternary) Operators | `Condition ? val1 : val2` |
**Notes:**
* You are already familiar with most of the operators. However some of them must be new to you. Let us now look at those.

### Double equals (==) vs Triple Equals (===)

#### Double Equals (==)
**Definition:** Double equals compares the values only, irrespective of the data types.
**Syntax:**
```javascript
console.log('100' == 100) // string & number
// true

var x = 5; // number
var y = '5' // string
console.log(x == y) // true
```

#### Triple Equals (===)
**Definition:** Triple equals test strict equality which means value and type both should be same.
**Syntax:**
```javascript
console.log('100' === 100) // string & number
// false

var x = 5; // number
var y = '5' // string
console.log(x === y) // false
```

### + operator on string
**Definition:** Using + operator on strings will concatenate those two strings together into single string.
**Syntax:**
```javascript
console.log('hello' + ' world!') // 'hello world!'
console.log('Trip' + ' to ' + 'Florida') // 'Trip to Florida'
```
```javascript
console.log('Trip' + 100) // 'Trip100'
console.log('Trip' + undefined) // 'Trip undefined'
console.log('100' + 20) // '10020'
console.log(null + 'Trip') // 'nullTrip'
```
**Notes:**
* Even if any one of the value is string, it will convert other values into string first and concatenate them into single string later.

### Typeof and Exponentiation operators

#### typeof operator
**Definition:** typeof operator returns the data type of variable / value in string format.
**Syntax:**
```javascript
console.log(typeof 100); // "number"
console.log(typeof 'Lets go to Trip'); // "string"
trip = null;
console.log(trip); // "null"
console.log(typeof trip); // "object"
```

#### Exponentiation operator (**)
**Definition:** Exponentiation operator (**) is used to create a value to the power of another value. This is similar to exponentiation operator in python.
**Syntax:**
```javascript
console.log(5 ** 2) // 25
val=5
console.log(val ** 2) // 25
```
*CrossReferences:* python

### Tryout: Data types and operators
**Definition:** The given code snippet shows the use of different data types and operators.
**Syntax:**
```javascript
//Below code shows use of console.log()
place = "Florida"
console.log(place); // Florida
console.log("Hello World!");// Hello World!

//Below code shows difference between undefined and null
//undefined
var placeTovisit;
console.log(placeTovisit); //undefined

//null
cabDetail = null;
console.log(cabDetail); //null

//Double equals and tripe equals
//Double equals
// comparison between string and number
console.log('100' == 100) //true
var x = 5; // number
var y = '5' // string
console.log(x == y) // true

//Tripe quals
// comparison between string and number
console.log('100' === 100) // false
var x = 5; // number
var y = '5' // string
console.log(x === y) // false
```
**Notes:**
* Shows the usage of following commands: console.log(), undefined and null, Double equals and triple equals.

### Tryout: Data types and operators-2
**Definition:** The following data types and operators are shown: concatenation of string (use of + operator on string), typeof(), Exponentiation operator (**).
**Syntax:**
```javascript
// use of + operator on string
console.log('hello' + ' world!'); // 'hello world!'
console.log('Trip' + ' to ' + 'WonderLand'); // 'Trip to WonderLand'
console.log('Trip' + 100); // 'Trip100'
console.log('Trip' + undefined); // 'Trip undefined'
console.log('100' + 20); //10020
console.log(null + 'Trip'); // 'nullTrip'

//use of typeof() operator
console.log(typeof 100); // "number"
console.log(typeof 'Lets go to Trip'); // "string"
trip = null;
console.log(typeof trip); // "object"

//use of exponentiation operator (**)
console.log(5**2); // 25
```

### Making decisions in JavaScript code
(content not found in source)

### If else
**Definition:** if-else in JavaScript follows the similar syntax as in other languages. Unlike Python, JS uses flower brackets instead of indentation.
**Syntax:**
```javascript
// syntax
if (expression) {
//statements
}
else{
// statements
}
```
```javascript
//example
n = 10;
if (n % 2 == 0) {
console.log("n is even");
}
else{
console.log("n is odd");
}
```
*CrossReferences:* Python

### Security concern (Conditional Statements)
**Notes:**
* Conditionals should start on new lines: Code is clearest when each statement has its own line.
* It is a common pattern to combine on the same line an if and its resulting then statement.
**CommonMistakes:**
* ⚠️ When an if is placed on the same line as the closing `}` from a preceding then, else or else if part, it is either an error (else is missing) or the invitation to a future error as maintainers fail to understand that the two statements are unconnected.

### Constraints (else-if)
**Definition:** JavaScript does not have an else-if construct. So we nest a if-else statements inside an else block.
**Syntax:**
```javascript
// syntax
if (expression) {
//statements
} else if{
//statements
}else{
//statements
}
```
```javascript
// example
n=10;
if (n > 0) {
console.log("n is positive");
} else if(n < 0) {
console.log("n is negative");
} else
{
console.log("n is zero");
}
```

### Switch Case Statement
**Definition:** switch is used to execute different set of statements based on different conditions. It is equivalent to an else-if statement.
**Syntax:**
```javascript
// syntax
switch (expression) {
case label_1: //statements
[break;]

case label_n: //statements
[break;]
default: //statements
[break;]
}
```
```javascript
//example
choice = 'a';
switch(choice) {
case 'a': console.log("Trip to Paris");
break;
case 'b': console.log("Trip to New York");
break;
default: console.log("Trip to switzerland");
}
```
**Notes:**
* Learn more about switch statements (implied cross-reference).

### Looping in JavaScript
**Definition:** Syntax for looping statements in JavaScript.

#### for
**Definition:** for is used to loop through block of code multiple time based on a condition and increment/decrement expression.
**Syntax:**
```javascript
// syntax
for (initial_expression; condition; increment/decrement_expression) {
//statements
}
```
```javascript
// example
n = 10
for (i=0; i < n; i++) {
console.log(i);
}
```

#### while
**Definition:** while loop executes a block of code until condition is true.
**Syntax:**
```javascript
// syntax
while(condition) {
//statements
}
```
```javascript
// example
n = 10;
while (n > 0) {
console.log(n);
n = n-1;
}
```
**Notes:**
* JS also supports a do-while loop.
*CrossReferences:* do-while loop

### Summary (Control Structures)
**Notes:**
* JavaScript is an interpreted language.
* JS has 5 data types: number, string, undefined, null, object.
* `===` is also called as strict equals.
* `typeof` helps us identify the type of a variable or value.
* JavaScript supports the regular conditional and iterational control structures.
*CrossReferences:* strict equals

### Security concern (Control Structures - Blocks)
**Notes:**
* Nested blocks of code should not be left empty: Most of the time a block of code is empty when a piece of code is really missing. So such empty block must be either filled or removed. Also, it is a waste of resources.
* Non-empty statements should change control flow or have at least one side-effect: Any statement (other than a null statement, which means a statement containing only a semicolon ;) which has no side effect and does not result in a change of control flow will normally indicate a programming error, and therefore should be refactored.
**CommonMistakes:**
* ⚠️ Empty blocks of code (waste of resources).
* ⚠️ Statements without side effects or change of control flow (programming error).

### Tryout: Iterational Statements
**Definition:** The code demonstrates the usage of iteration structures (if-else inside for-loop).
**Syntax:**
```javascript
var x,y;
var chr='';
for(x=1; x <=5; x++)
{
for (y=1; y <= x; y++)
if(y%2!=0){
chr=chr+("*");
}
else{
chr=chr+("#")
}
}
console.log(chr);
chr=
```
**Examples:**
* Pattern:
```
*#
*#*
*#*#
*#*#*
```
**Notes:**
* A Javascript program is given to construct a pattern.
*CrossReferences:* for-loop, if-else

### Exercise: Iterational Statements
**Definition:** Write a JavaScript loop to print the below output.
**Examples:**
* Output:
```
1
12
123
1234
12345
```

### Functions
**Definition:** A function is a named block of code.
**Syntax:**
```javascript
function functionName(param1, param2,..) {
//statements
}
```
```javascript
function myFunction (num1, num2){
num3=num1*num2;
return num3
}
```
**Attributes:**
* `function` keyword
* `functionName` (name of the function)
* `param1, param2,...` (parameters)
**Notes:**
* A function can be created using `function` keyword, followed by name and parameters.
* The body of the function is placed inside the curly braces.

### Security concern (Functions)
**Notes:**
* Return values from functions without side effects should not be ignored: If results are ignored, the function call is useless and should be dropped or the source code doesn't behave as expected. This rule triggers issues only on a predefined list of known objects & functions.
* Function returns should not be invariant: When a function is designed to return an invariant value, it may be poor design, but when it happens on all paths through the logic, it is likely a mistake and should be avoided at any cost.
**CommonMistakes:**
* ⚠️ Ignoring return values from functions without side effects.
* ⚠️ Designing functions with invariant returns across all logic paths (likely a mistake).

### Functions as objects
**Definition:** In JavaScript, functions are actually objects. That means a function can be stored in a variable.
**Syntax:**
```javascript
funVariable = function myFunc(num1, num2) {
num3=num1*num2;
return num3
}
```
```javascript
console.log(funVariable(10,20));
// 200
```
**Notes:**
* Since functions are treated as objects, they can be stored in a variable and invoked using that variable name.
* Functions can also be passed as a parameter to another function.

### Functions as objects (Passing as Parameter)
**Syntax:**
```javascript
function welcome() { console.log("Hello World");}
function goodbye(){ console.log("See you later");}

function greet(choice){
choice();
}

greet(welcome);
greet(goodbye);
```
**Notes:**
* We are passing the functions welcome() and goodbye() as parameters to the function greet().
*CrossReferences:* greet()

### Higher Order Functions and First Class Citizen
**Syntax:**
```javascript
function greet(){
var hello=function welcome(){console.log("Hello World");}
return hello;
}

var retFunc=greet();
retFunc();
```
**Notes:**
* Since functions are treated as objects, you can also return them from a function.

#### Higher Order Functions
**Definition:** Functions which can either accept other functions as parameters or return other functions as parameters are called as Higher Order Functions.
**Notes:**
* Many in-built functions in JS are Higher Order Functions.

#### First Class Citizen
**Definition:** Any object which can be assigned, passed as a parameter and returned from a function is called a First Class Citizen in a programming language.
**Notes:**
* Thus, all functions are First Class Citizens in JS.

### Anonymous function in HOF
**Definition:** Functions without a name are called anonymous functions.
**Syntax:**
```javascript
function greet(choice){
choice();
}

greet(function(){ console.log("Hello World")});
// Hello World
```
**Notes:**
* We have seen that we can pass one function as a parameter to another function.
* Usually, for such purposes we can create a function without a name.
* The function which is being passed as a parameter does not have a name.
*CrossReferences:* HOF (Higher Order Function)

### Arrow functions
**Definition:** An arrow function is a concise way of writing a function. Arrow functions are anonymous functions as they don't have a name.
**Syntax:**
```javascript
(parameter) => function body
```
```javascript
function greet(choice){
choice();
}

greet(function(){ console.log("Hello World") }); // Hello World
greet(()=>{ console.log("Hello World") }); // Hello World
```
**Notes:**
* Arrow functions provide a shorter way of writing anonymous functions.

### Where to use arrow functions?

#### Syntax 1: Multi parameter, multi line code
**Definition:** If code is in multiple lines, we need to have {}.
**Syntax:**
```javascript
calculateCost = (ticketPrice, noofPerson)=>{
noofPerson = ticketPrice * noofPerson;
return noofPerson;
}
console.log(calculateCost(500, 2));
// 1000
```

#### Syntax 2: No parameter, single line code
**Definition:** If the code is single line, we don't need {}. The expression is evaluated and automatically returned.
**Syntax:**
```javascript
trip = () => "Let's go to trip."
console.log(trip());
// Let's go to trip.
```

#### Syntax 3: One parameter, single line code
**Definition:** If only one parameter, we don't need ().
**Syntax:**
```javascript
trip = place => "Trip to " + place;
console.log(trip("Paris"));
// Trip to Paris
```

#### Syntax 4: One parameter, single line code
**Definition:** If only one parameter, we can simply use _ and a variable name is not needed. (Note: The provided example does not use '_')
**Syntax:**
```javascript
trip = place => "Trip to " + place;
console.log(trip("Paris"));
// Trip to Paris
```

### Global Scope
**Definition:** A variable is said to be in global scope when it is accessible throughout the program, across functions, across files.
**Syntax:**
```javascript
function validateTravellerPassword (password) {
for (i=0; i < password.length; i++) {
}
}
function validateTravellerName(name) {
console.log("The value of i is "+i);
for (i=0; i < name.length; i++) {
}
}
validateTravellerPassword("12345");
validateTravellerName("Jack");
```
**Notes:**
* All variables in JavaScript are global by default.
* The variable `i` used in the for-loop of `validateTravellerPassword()` is global.
* At the end of `validateTravellerPassword()`, the value of `i` becomes 5 (if length is 5).
* The same value of `i` is also accessible in `validateTravellerName()`, since `i` has global scope.
*CrossReferences:* validateTravellerPassword(), validateTravellerName()

### Security concern (Variables)
**Notes:**
* Variables should not be shadowed: Overriding or shadowing a variable declared in an outer scope can strongly impact the readability, and therefore the maintainability, of a piece of code. Further, it could lead maintainers to introduce bugs.
**CommonMistakes:**
* ⚠️ Introducing bugs due to variable shadowing.

### Local Scope
**Definition:** Local scope is when a variable is accessible only within a function. This is also called function scope.
**Syntax:**
```javascript
function validateTravellerPassword (password) {
for (var i = 0; i < password.length; i++) {
}
}
function validateTravellerName(name) {
console.log("The value of i is "+i);
for (var i = 0; i < name.length; i++) {
}
}
validateTravellerPassword("password");
validateTravellerName("Josh");
```
**Notes:**
* In JavaScript, any variable declared with the `var` keyword inside a function is considered local.
* If the variable is created with `var` outside a function, it still behaves like a global variable.
* To restrict the scope of `i`, the `var` keyword must be added to `i` within the loop initialization.
**CommonMistakes:**
* ⚠️ Observe that in line 6 of `validateTravellerName()`, we are printing the value of `i`, even before it is declared. (Implied error or hoisting introduction).
*CrossReferences:* var, validateTravellerPassword(), validateTravellerName()

### Security concern (Unused assignments)
**Notes:**
* Unused assignments should be removed: A dead store happens when a local variable is assigned a value that is not read by any subsequent instruction.
* Calculating or retrieving a value only to then overwrite it or throw it away, could indicate a serious error in the code.
* If not an error, it is at best a waste of resources. Therefore all calculated values should be used.

### Variable Hoisting
**Definition:** Hoisting is a phenomenon, where no matter where the variable is declared inside the function, they are all pushed as the first statements inside the function during the function execution.
**Syntax:**
```javascript
function validateTravellerName(name) {
//var i; (internally the variable i gets hoisted as the first statement of the function)
console.log("The value of i is "+i);
for (var i=0; i < name.length; i++) {
}
console.log(i);
}
```
**Notes:**
* The code accessing a variable before declaration will not throw an error.
* Only variable name is hoisted and not its value. That is why we get `undefined` instead of zero in the console when accessing before assignment.
**CommonMistakes:**
* ⚠️ Expecting a variable accessed before assignment to have a value (it will be `undefined`).
*CrossReferences:* validateTravellerName()

### Block scope and const

#### Block scope
**Definition:** A variable with a block scope is accessible only within the block of statements and not throughout the function.
**Syntax:**
```javascript
function validateTravellerName(name) {
for (let i = 0; i < name.length; i++) {
}
console.log(i); // This will give an error as i is not accessible outside the for block.
}
validateTravellerName("Josh");
```
**Notes:**
* In `validateTravellerName()` or `validateTravellerPassword()`, the value of `i` makes sense only within the `for-loop` block, but because it was declared with `var`, it is accessible throughout the function.
* Block scoped variables are created with the `let` keyword.
* Block scoped variables are not hoisted.
**CommonMistakes:**
* ⚠️ Accessing a `let` variable outside its block scope (will give an error).
*CrossReferences:* let, var, hoisting

#### Const
**Definition:** const is a keyword which is also used to create a block scoped variable. But the difference between const and let is that, a const variable cannot be modified. It is constant.
**Syntax:**
```javascript
{
const a=10
a=20 // Error expected
}
```
```javascript
{
const a=10;
}
console.log(a); // Error expected
```
**Notes:**
* `const` variables cannot be modified after initialization.
* Accessing a `const` variable outside its block scope will result in an error.
**CommonMistakes:**
* ⚠️ Modifying a `const` value (will give an error).
* ⚠️ Accessing a `const` outside its block (will give an error).
*CrossReferences:* let

### Summary (Variable Scopes)
**Notes:**
* Functions are objects in JS.
* Functions can be stored in variables, passed as parameters or returned as values.
* Functions without names are called anonymous functions.
* Arrow functions are shorter way to write anonymous functions.
* Variables can either be in global, local or block scope.

### Number()
**Definition:** Number(), which is the constructor of Number object, converts value of an object to a number. If it is unable to convert the value, it returns NaN.
**Syntax:**
```javascript
Number(argument)
```
```javascript
var x="123";
console.log(Number(x)); //123
console.log(Number("123")); // 123
console.log(Number("123.1")); // 123.1
console.log(Number(10/0)); // Infinity
console.log(Number(NaN)); // NaN
console.log(Number("123abc")); // NaN
```
**Notes:**
* JS has many useful in-built functions, including Number() and String().
* NaN stands for Not a Number.
* In JS, anything divided by 0 is Infinity.
*CrossReferences:* String()

### String()
**Definition:** String() converts the value of an object to a string. It is the constructor of the String object.
**Syntax:**
```javascript
String(argument)
```
```javascript
console.log(String(1)); // "1"
console.log(String("Hello")); // "Hello"
```

### Tryout: Functions
**Definition:** The given code shows how we can create the functions and how the function can be called.
**Syntax:**
```javascript
function myFunction (num1, num2){
num3=num1*num2;
return num3;
}
mulVal=myFunction(10,20);
console.log(mulVal); //200
```

### Tryout: Functions as Objects
**Definition:** The given code demonstrates how a function is passed as a parameter.
**Syntax:**
```javascript
// function passed as a paramter
function welcome(){
console.log("Hello World");
}

function goodbye(){
console.log("See you later");
}

function greet(choice){
choice();
}

greet(welcome);
greet(goodbye);
```

### Tryout: Arrow Functions (Multi/No Parameter)
**Definition:** The given code shows the usage of different scenario of arrow functions. These are the following types: Multi parameter, multi line code. No parameter, single line code.
**Syntax:**
```javascript
// Multi parameter, multi line code
calculateCost = (ticketPrice, noofPerson)=>{
noofPerson = ticketPrice * noofPerson;
return noofPerson;
}
console.log(calculateCost(500, 2)); //1000

//No parameter, single line code
trip = () => "Lets go to trip."
console.log(trip()); //// Lets go to trip.
```

### Tryout: Arrow Functions (One Parameter)
**Definition:** The given code demonstrates the two syntax of the arrow functions: One parameter, single line code.
**Syntax:**
```javascript
//One parameter, single line code
let trip = place => "Trip to " + place;
console.log(trip("Paris")); // Trip to Paris

//One parameter, single line code:
trip = place => "Trip to " + place; // Note: Syntax ambiguity/repeat in source text
console.log(trip("Paris")); // Trip to Paris
```

### Tryout: Anonymous function
**Definition:** The given code shows the creation of the function without the name that is an anonymous function.
**Syntax:**
```javascript
function greet(choice){
choice();
}
greet(function(){ console.log("Hello World")}); // Hello World
```

### Built-in objects in JavaScript
**Definition:** Objects have properties and methods. JavaScript provides many standard built-in objects. In addition to that it also provides an option to create user defined objects.
**Attributes:**
* Array
* Date
* String
**Notes:**
* String -> Refer the "Quick References" module for String methods.
*CrossReferences:* Array, Date, String

### Array Object
**Definition:** An array is used to store multiple values in a single variable. We can easily access the values stored in an array using the index position of the data stored in the array.
**Syntax:**
```javascript
var arr1 = [elemento, element1, .., elementN];
```
```javascript
placesToVisit = ["Paris", "New York", "Switzerland"];
console.log(placesToVisit[0]); // Paris
console.log(placesToVisit[2]); // Switzerland
```
**Notes:**
* Array built-in object is used to create arrays.
* Indexing in array start with 0.

#### Array destructuring
**Definition:** We can destructure an existing array. Just by assigning multiple variables to the array, we can access individual items.
**Syntax:**
```javascript
numArr=[100,200,300];
var [a,b,c]=numArr;
// the numArr is now destructured and individual values are stored in the individual variables.
console.log(a);
console.log(b);
console.log(c);
```
**Notes:**
* If the variable is prefixed by three dots (`...`) then it is called a rest variable and can store more than one property.
**CommonMistakes:**
* ⚠️ Note that rest variable feature is the latest ES2018 feature and is not yet supported by any browser.
*CrossReferences:* ES2018

### Array Functions
**Definition:** Arrays comes with many built-in functions which makes working with array very easy in javascript.

#### 1. push()
**Definition:** push() is used to insert a new element at the end of the array.
**Syntax:**
```javascript
places = ["Paris", "New York"];
places.push("Switzerland");
console.log(places);
// ["Paris", "New York", "Switzerland"]
```

#### 2. pop()
**Definition:** pop() is used to remove last element of array.
**Syntax:**
```javascript
places = ["Paris", "New York", "Switzerland"];
places.pop();
console.log(places);
// ["Paris", "New York"]
```

#### 3. indexOf()
**Definition:** indexOf() is used to find index of given elements.
**Syntax:**
```javascript
places = ["Paris", "New York", "Switzerland"];
console.log(places.indexOf("New York"));
// 1
```
**Notes:**
* indexOf() will return -1 if the value is not present.

#### 4. splice(pos, n)
**Definition:** splice(pos, n) will remove n elements from pos index position.
**Syntax:**
```javascript
places = ["Paris", "New York", "Switzerland"];
places.splice(1, 2); // This will remove 2 elements from index 1
console.log(places);
// ["Paris"]
```
**Attributes:**
* `pos`: Starting index position.
* `n`: Number of elements to remove.

#### 5. forEach()
(content not found in source)

#### map()
**Definition:** The map() array function generates a new array. It iterates over each element in the array, just like forEach. It invokes a function on each element, just like forEach.
**Syntax:**
```javascript
placesToVisit= ["Paris", "New York", "Switzerland"];
function display_uppercase(place) {
return place.toUpperCase();
}

placesUpparCase = placesToVisit.map(display_uppercase);
console.log(placesUpparCase);
```
**Notes:**
* The difference is forEach just invokes a function on each item in the array. It does not create a new array. Hence, map() creates a new array based on what the function does.
*CrossReferences:* forEach

#### filter()
**Definition:** filter accepts a function. It iterates over each element and creates a sub array if the function returns true.
**Syntax:**
```javascript
placesToVisit= ["Paris", "New York", "Switzerland"];

function filterPlaces (val) {
if (val.length > 5) {
return true;
}
}

filteredPlaces = placesToVisit.filter(filterPlaces);
console.log(filteredPlaces );
```
**Notes:**
* What if we want to get all words whose length is greater than 5? For this we can use filter().

#### find()
**Definition:** It returns the first element in the array which satisfies a given condition. It takes a callback. It executes the callback for each element in the array.
**Syntax:**
```javascript
placesToVisit= ["Paris", "New York", "Switzerland"];

function findPlaces(val) {
if (val.length > 5) {
return true;
}
}

foundPlaces = placesToVisit.find(findPlaces);
console.log(foundPlaces);
```
**Notes:**
* If the callback returns true, then find returns the element for which the callback returned true and stops further iteration. If it was false for all elements, it returns undefined.

### Arrow Functions Revisited

#### 1. Arrow in forEach()
**Definition:** The forEach() function of an array takes another function as parameter and invokes the function for every item in the array.
**Syntax:**
```javascript
placesToVisit= ["Paris", "New York", "Switzerland"];

placesToVisit.forEach(place => console.log("Trip to " + place));
// Trip to Paris
// Trip to New York
// Trip to Switzerland
```
*CrossReferences:* forEach()

#### 2. Arrow in map()
**Definition:** An array object has a map() function that creates a new array based on what the passed callback function does. This map() can also be written using arrow function.
**Syntax:**
```javascript
placesToVisit= ["Paris", "New York", "Switzerland"];
placesUpperCase = placesToVisit.map(place => place.toUpperCase());
console.log(placesUpperCase);
// ["PARIS", "NEW YORK", "SWITZERLAND"]
```
*CrossReferences:* map()

#### 3. Arrow in filter()
**Definition:** An array object has a filter() function that returns a filtered sub array based on what the passed callback function does. This filter() can also be written using arrow function.
**Syntax:**
```javascript
placesToVisit = ["Paris", "New York", "Switzerland"];
filteredPlace = placesToVisit.filter(place => place.length > 5);
console.log(filteredPlace);
// [ 'New York', 'Switzerland']
```
*CrossReferences:* filter()

#### 4. Arrow in find()
**Definition:** An array object has a .find() function that returns the first element in the array based on what is passed as callback function. This find() can also be written using arrow function.
**Syntax:**
```javascript
placesToVisit = ["Paris", "New York", "Switzerland"];
FindPlace = placesToVisit.find(place => place.length > 5);
console.log(findPlace);
// "New York"
```
*CrossReferences:* .find()

### Tryout: Array Object
**Definition:** The given code highlights - Usage of various array functions and Usage of built-in array functions.
**Syntax:**
```javascript
placesToVisit = ["Paris", "New York", "Switzerland"];

//array index starts from 0
console.log(placesToVisit[0]);

//the last element will be removed from the array
placesToVisit.pop();
console.log("after pop operation", placesToVisit);

//push the element at the end of array
placesToVisit.push("Switzerland");
console.log("after push operation", placesToVisit);

//give the index value for element
console.log("index value of New York is", placesToVisit.indexOf("New York"));

//forEach() is used to interate over an array.
console.log("forEach:");
placesToVisit.forEach(function(place) {
console.log(place);
})

//The map() array function generates a new array.
console.log("map:");
function display_uppercase(place) {
return place.toUpperCase();
}
placesUpparCase = placesToVisit.map(display_uppercase);
console.log("output of map function", placesUpparCase);

// filter iterates over each element and creates a sub array if the function returns true
console.log("filter:")
function filterPlaces (val) {
if (val.length > 5) {
return true;
}
}
filteredPlaces = placesToVisit.filter(filterPlaces);
console.log("output of filter function", filteredPlaces );

// find returns the first element in the array which satisfies a given condition.
// ... (find implementation missing/truncated)
```

### Tryout: Array Functions
**Definition:** The given code highlights usage of built-in array functions (forEach and map, using arrow syntax).
**Syntax:**
```javascript
const employees = [
{ name: "John", salary: 25000 },
{ name: "Jane", salary: 30000 },
{ name: "Jim", salary: 35000 },
]

//forEach() is used to interate over an array.
console.log("forEach:");
employees.forEach( (employee) => {
let bonus = 5000;
console.log(
"Updated Salary of " + employee.name + " is " + (employee.salary + bonus)
);
});

//The map() array function generates a new array.
console.log("map:");
empWithLocation = employees.map( (employee) => {
return {...employee, location: "Mysore" };
});
console.log("Output of map function", empWithLocation);

// filter iterates over each element and creates a sub array if the function returns true
// ... (filter implementation missing/truncated)
```
*CrossReferences:* forEach, map, filter (implied)

### Date Object
**Definition:** Date is a built-in object which is used to create a Date instance. Date instance can be created using new Date();
**Attributes:**
| Method | Description |
|---|---|
| `new Date()` | Will create date instance for today's date |
| `new Date(value)` | Value should be in milliseconds, the date instance will be created for (0 + value) milliseconds since 1 Jan, 1970 UTC |
| `new Date(dateString)` | Some of the valid formats are as follows: "YYYY-MM-DD", "YYYY-MM" etc. |
**Notes:**
* Some methods of object are listed above.
* Month in Date is 0 based.

### Summary (Date Object)
**Notes:**
* JS has many useful built-in objects.
* Some of the key array methods are: foreach, find, map, filter, push, pop, splice.
* Arrow functions ease the use of array functions.
* `new Date()` will create a date object with current date.

### Tryout: Date Object
**Definition:** The below given code shows - the creation of Date object, and the Date object operations.
**Syntax:**
```javascript
// to get today's Date
var today = new Date();
console.log("Today's Date is ",today);

// pass value in milliseconds
var startingDate = new Date(0);
console.log("Date starts from ", startingDate); //the starting date is January 01, 1970 00:00:00 UTC
var dateInMillisecond = new Date(100000000000);
console.log("Date for given milliseconds is ",dateInMillisecond); // approximate date will be 03 March 1973

// pass value in yyyy, mm, dd
var dateObj = new Date(2019,02,21);
console.log("Date for given value is", dateObj); // Month starts from 0

//get month from given date
var month_name = function(dt){
mlist = [ "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December" ];
return mlist[dt.getMonth()];
};
console.log(month_name(new Date("10/11/2009")));
console.log(month_name(new Date("02/12/2019")));

//set the value of year
var todayDate = new Date();
todayDate.setFullYear(2020);
console.log("Value of todayDate after setFullYear", todayDate)
```

### Exercise: String Operations (Unique Characters)
**Definition:** Write a JavaScript function to extract unique characters from a string.
**Examples:**
* Example string: "thequickbrownfoxjumpsoverthelazydog"
* Expected Output: "thequickbrownfxjmpsvlazydg"
**Notes:**
* Hint: Refer the String Operations tables in the Quick Reference section.
*CrossReferences:* String Operations tables

### Exercise: Check Palindrome
**Definition:** Write a function, check_palindrome() to check whether the given string is a palindrome or not. The function should return true if it is a palindrome else it should return false.
**Examples:**
* Example palindromes: MAN, civic, WOW etc.
**Notes:**
* Assume that all the letters in the given string are all of the same case.
* Note: Initialize the string with various values and test your program.
* Hint: Refer the String Operations tables in the Quick Reference section.
*CrossReferences:* String Operations tables

### Exercise: String Operations (Name Processing)
**Definition:** Write a JavaScript code to process name as the sample below.
**Examples:**
* Sample Input: Rama Krishna Narayan
* Sample Output: R. K. Narayan
**Notes:**
* Hint: Refer the String Operations tables in the Quick Reference section.
*CrossReferences:* String Operations tables

### Exercise: Date Operations (Date Calculation)
**Definition:** Write a JavaScript code to formulate date for a specified date after given 'n' number of days.
**Examples:**
* Sample Input: 16th Jul, 2018 and n=30
* Sample output: 15th August, 2018
**Notes:**
* Note: Don't forget to account for leap years!
* Hint: Refer the Date Operations tables in the Quick Reference section.
*CrossReferences:* Date Operations tables

### Exercise: Date Operations (Current Day/Time Display)
**Definition:** Write a JavaScript program to display the current day and time in the following format.
**Examples:**
* Sample Output: Today is: Tuesday. Current time is: 10 PM: 30: 38
**Notes:**
* Hint: Refer the Date Operations tables in the Quick Reference section.
*CrossReferences:* Date Operations tables

### Exercise: Date Operations (Format Check)
**Definition:** Write a JavaScript function checkDate() to check if a given date is in the correct format or not.
**Examples:**
* Correct date format: "MM-DD-YYYY" (for example: 03-18-2018)
* Sample Input: 19-12-1995
* Sample Output: False
**Notes:**
* If the date format is as above, the function should print true else it should print false.
* Hint: Refer the Date Operations tables in the Quick Reference section.
*CrossReferences:* Date Operations tables

### Exercise: Functions (Marks Reports)
**Definition:** A teacher is in the process of generating few reports based on the marks scored by the students of her class in a project based assessment. The marks are out of 25.
**Examples:**
* Sample Input: list_of_marks = [12,18,25,24,2,5,18,20,20,21]
* Sample Output: more than average: 70.0, frequency: [0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2, 0, 2, 1, 0, 0, 1, 1]
**Notes:**
* Assume that the marks of her 10 students are available in an array.
* Required functions: `find_more_than_average()` (Find and return the percentage of students who have scored more than the average mark of the class), `generate_frequency()` (Find how many students have scored the same marks, up to 25. Result should be populated in a list and returned).

### Object creation using Object literal
**Definition:** To create an object using object literal, write your object attributes and methods.
**Syntax:**
```javascript
objName={
propertyName:value,
propertyName:value,
...,
methodName(){
},
methodName(){
}
}
```
```javascript
var empOne = {
name: "John",
empNumber: 1001,
emailId: "John@gmail.com",
swipeIn(){console.log("Swipe In by "+this.name)}
};
```
**Notes:**
* In the next page, we will learn how to access object property.

### How to access the properties of an object?
**Syntax:**
```javascript
var empOne = {
name: "John",
empNumber: 1001,
emailId: "John@gmail.com",
swipeIn(){console.log("Swipe In by "+this.name)}
};
console.log(empOne.empNumber);
empOne.empNumber=1002;
console.log(empOne.empNumber);
empOne.swipeIn();
```
**Notes:**
* object.property: To get the value (`var name = empOne.name;`), To set the value (`empOne.name = "Hello";`).
* object[property]: To get the value (`var name= empOne["name"];`), To set the value (`empOne["name"] = "John";`).
* Note: `object[property]` access should be used mainly when the property names are having space, hyphen, or one that starts with a number.

### Object iteration

#### for..in
**Definition:** The for..in loop iterates over the object and gives the property values of the object.
**Syntax:**
```javascript
for(let property in empOne){
console.log(empOne[property]);
}
```

#### Object.values()
**Definition:** Object.values() will give all the values of an object in an array.
**Syntax:**
```javascript
console.log(Object.values(empOne));
```

#### Object destructuring
**Definition:** We can destructure an existing object into variables.
**Syntax:**
```javascript
let { name, ...rest } = empOne
console.log(name)
// 'John'

console.log(rest)
/*{
empNumber: 1001,
emailId: "John@gmail.com"
}*/
```
**Notes:**
* If the variable is prefixed by three dots (`...`) then it is called a rest variable and can store more than one property.
**CommonMistakes:**
* ⚠️ Note that this feature is the latest ES2018 feature and is not yet supported by any browser.
*CrossReferences:* ES2018

### Tryout: Object literal
**Definition:** The given code highlights the creation of an Object. Usage of Object.values() method to get values of property in an Object. A JavaScript program to get property names and it's values.
**Syntax:**
```javascript
var empOne = {
name: "John",
empNumber: 1001,
emailId: "John@gmail.com"
};

//to get property names
console.log("property names:")
for(let property in empOne){
console.log(property);
}

// to get the values of property
console.log("property values:")
for(let property in empOne){
console.log(empOne[property]);
}

// to get the values of property using Object.values()
console.log("property values using Object.values():")
console.log(Object.values (empOne));
```

### Class creation in Javascript
**Definition:** JavaScript is a object oriented language. So far we have seen how to use built-in classes and objects like Date. We can also create our own classes in JavaScript.
**Syntax:**
```javascript
class Employee{
constructor(id, name, age) {
this.id=id;
this.name=name;
this.age=age;
}
swipeIn(){
console.log("Employee "+this.id+" has swiped in at "+new Date());
}
}

e1=new Employee(100, "Mark", 23);
e2=new Employee(101, "Jane",24);
console.log(e1.age);
e1.swipeIn();
e2.swipeIn();
```
**Attributes:**
| OOP Feature | Description |
|---|---|
| Class | Can be created using the `class` keyword |
| Constructor | Can be created using the `constructor` keyword |
| Attributes | Variables created as `this.<variableName>` inside the constructor become attributes |
| Methods | Functions created inside the class become methods |
| Object | Created using the `new` keyword |
| Access | The attributes and methods can be accessed using the dot operator on the object |
**Notes:**
* The `this` keyword is used to create attributes inside a class. This is equivalent to `self` in Python.
*CrossReferences:* Date, Python

### Static methods in class
**Definition:** Just like in other programming languages, we can create static methods in JavaScript using the `static` keyword.
**Syntax:**
```javascript
class Employee{
// ... constructor and swipeIn() ...
static code(){
console.log("Employee is coding");
}
}

Employee.code();
```
**Notes:**
* Static values can be accessed only using the classname and not using `this` keyword.
* The example shows a static method `code` accessed using `Employee.code()`.
**CommonMistakes:**
* ⚠️ Accessing static values/methods using `this` keyword (will lead to an error).

### Inheritance
**Definition:** In JavaScript, one class can inherit another class using the `extends` keyword. The subclass inherits all the methods (both static and non-static) of the parent class.
**Syntax:**
```javascript
class Employee{
// ... (implementation)
}

class PartTimeEmployee extends Employee{
// ...
}

e1=new Employee(100, "Mark", 23);
e2= new PartTimeEmployee();
PartTimeEmployee.code();
e2.swipeIn();
```
**Notes:**
* We are creating a child class called `PartTimeEmployee` which extends the `Employee` class.
**CommonMistakes:**
* ⚠️ `e2.swipeIn()` gives undefined for the id if values are not passed to the parent constructor.
*CrossReferences:* extends

### The super keyword
**Definition:** In order to access the parent class constructor, the child class constructor need to invoke it using `super()` and pass the necessary values.
**Syntax:**
```javascript
class Employee{
// ... (implementation)
}

class PartTimeEmployee extends Employee{
constructor (id, name, age, contractPeriod){
super(id, name, age);
this.contractPeriod=contractPeriod;
}
}

e1=new Employee(100, "Mark", 23);
e2= new PartTimeEmployee (101, "Jane", 34, 3);
PartTimeEmployee.code();
e2.swipeIn();
console.log(e2.contractPeriod);
```
**Notes:**
* `super` keyword must appear before `this` keyword in the constructor.
*CrossReferences:* super()

### Tryout: Class-Tryout
**Definition:** The code given explains the usage of static method, Inheritance and super keyword.
**Syntax:**
```javascript
class Employee{
constructor(id, name, age){
this.id=id;
this.name=name;
this.age=age;
}
swipeIn(){
console.log("Employee "+this.id+" has swiped in at "+new Date());
}
//static method that can be called only by using class name.
static code(){
console.log("Employee is coding");
}
}
//child class that can inherit all the properties of parent class (Employee)
class PartTimeEmployee extends Employee{
constructor(id, name, age, contractPeriod){
//to access parent class constructor
super(id, name, age);
this.contractPeriod=contractPeriod;
}
}
e1=new Employee(100, "Mark", 23);
e2= new PartTimeEmployee (101, "Jane", 34,3);
Employee.code();
e2.swipeIn();
console.log(e2.contractPeriod);
```
**Notes:**
* Highlights creation of a class, Inheritance, usage of static method and super keyword.
* Task: Call the static method (`code()`) using the child class name and observe the output.
*CrossReferences:* static method, Inheritance, super keyword

### What is JSON?
**Definition:** JSON stands for JavaScript Object Notation. JSON is a way of formatting the text in such a way that it looks like a JavaScript literal object.
**Notes:**
* When two different programs want to pass data to each other, they need a commonly accepted format (e.g., plain text, xml, json, etc.).
*CrossReferences:* JavaScript Object Notation, XML

### Object literal (JSON)
**Syntax:**
```javascript
let empObj = {
name: "John",
empNumber: 1001,
emailId: "John@gmail.com"
}
```

### JavaScript Object Notation
**Syntax:**
```javascript
let empJson = '{"name":"John", "empNumber":1001, "emailId":"John@gmail.com"}'
```
**Notes:**
* The keys in JSON string must be a string enclosed within quotes.
* The values can be any valid JavaScript value: null, number, string, etc. It can have arrays as well as other JSON objects as values.
* JavaScript provides a standard built-in object called JSON which has methods for parsing and generating JSON data.
*CrossReferences:* JSON

#### parse()
**Definition:** This function is used to convert JSON string into an JavaScript object.
**Syntax:**
```javascript
var json = '{ "firstName":"John", "lastName":"Doe"}';
var nameObj= JSON.parse(json);
//will convert JSON string into an JavaScript object
console.log(nameObj.firstName +" "+ nameObj.lastName);
```
*CrossReferences:* JSON.parse()

#### stringify()
**Definition:** This function is used to convert object to JSON string.
**Syntax:**
```javascript
var jScores = { "Java": 70, "JavaScript": 80, "CSS": 30};
var tScores = JSON.stringify(jScores);
//will convert object to JSON string
console.log(typeof(jScores)); // returns Object
console.log(typeof(tScores)); // returns String
```
*CrossReferences:* JSON.stringify()

### Summary (JSON)
**Notes:**
* Object literals can have attributes and methods.
* We can create class in JS using `class` keyword. `constructor` keyword is used to create constructor in a class.
* Functions inside a class/object become methods.
* `this` keyword is used inside an object/class to access the attributes.
* JSON is a way to create a string such that the string looks like a JS object literal.
* JSON is used to transfer data between different programs.

### Tryout: JSON
**Definition:** The given code highlights the creation of a JSON object. Usage of parse and stringify functions.
**Syntax:**
```javascript
// use of parse()
var json = '{ "firstName":"John", "lastName":"Doe"}';
var nameObj = JSON.parse(json); //will convert JSON string into an JavaScript object
console.log(nameObj.firstName +" "+ nameObj.lastName);

// use of stringify()
var jScores = { "Java": 70, "JavaScript": 80, "CSS": 30 };
var tScores = JSON.stringify(jScores); //will convert object to JSON string
console.log(typeof(jScores)); // returns Object
console.log(typeof(tScores)); // returns String
```
*CrossReferences:* JSON.parse(), JSON.stringify()

### Exercise - JSON
**Definition:** Write a JavaScript to code to get the following output in console from the JSON object.
**Syntax:**
```javascript
var mobJson='{"productId":1001, "product":{"name":"Moto", "series":"G5+","color":"NightSky"},"price":14900, "category": "Electronics", "shippingDetails": { "shipmentNo":"1DEL009","company": "Intel Marketing", "receivedOn":"2018-6-19"}, "seller":{"name": "xyz Mobile", "location":"New York", "stock":17}}'
```
**Examples:**
* Expected Output: `xyz Mobile shipped a Moto G5+ worth 14900 with productId: 1000.`
**Notes:**
* Note: The JSON object contains the following JSON (provided in Syntax field).

### Regular Expression
**Definition:** Regular Expression or regex is basically a sequence of characters indicating a pattern.
**Syntax:**
```javascript
function validateName(name) {
if(name.match(/\$/)){
return false;
}
else {
return true;
}
}
```
**Notes:**
* With the help of this pattern, we can search or match with other strings which follow the pattern indicated.
* The sequence of characters `/\$/` is an regular expression. It indicates "any character which is $".
* When a regular expression is passed as a parameter to a match function, it checks if the pattern is present in the given string. If found, the match function returns an array, else null.
*CrossReferences:* validateName(), match function

### Parts of Regular Expression
**Notes:**
* Various symbols and characters are used to form regular expressions.
* Three parts of Regular Expression: Meta characters, Quantifiers, Pre-defined classes (A pre-defined group of meta characters).
*CrossReferences:* Meta characters, Quantifiers, Pre-defined classes

### Steps to create a RegEx

#### Step 1: Create a regex pattern
**Definition:** A pattern is a series of characters that we want to search in the given test-string. Anything present in between '/' and '/' will become a pattern which can be used on a test-string.
**Attributes:**
| This regex will match | This regex will not match |
|---|---|
| "helloworld" | "Hello" (Regex is case sensitive. Hence 'H' is not as same as 'h') |
| "hhelloooooo0" | "helllo" (there is an extra l) |
| "hello wolrd" | "hello" (there is an extra space between h and e |
**Examples:**
* `/hello/` will check if the sequence of characters, h e l l o are present in the specified order, anywhere in the given string to be tested.

#### Step 2: Use meta-characters like [], ^, $
**Definition:** A meta-character is a character that has a special meaning (instead of a literal meaning).
**Attributes:**
| This regex will match | This regex will NOT match |
|---|---|
| "hallo" | "hello" (h is not followed by either 'a' or 'b' or'c' |
| "hbllo" | "habllo" ( a single character substitution. Hence eventhough h is followed by 'a' the subsequent characters should be "llo" |
**Examples:**
* The meta character `.` indicates a single character.
* For example, `/h[abc]llo/` matches a single character present inside brackets.
* The pattern `/h[^abc]llo/` will match "hello", "hfllo", "h6llo" but not "hallo".
**Notes:**
* The text shows examples where `/h[abc]llo/` matches "hallo" and "hbllo".
* `[^abc]` will match any single character except the ones given inside brackets.

#### Step 3: Use quantifiers like +, *, ? and {n}
**Definition:** Quantifier are symbols which specify the frequency at which a character can appear.
**Attributes:**
| This regex will match | This regex will NOT match |
|---|---|
| 'car' | 'cr' (there should be atleast one 'a' after 'c') |
| 'caaar' | 'cra' (there should be atleast one 'a' after 'c') |
| 'caar' | 'cr' |
**Examples:**
* `+` quantifier matches the preceding element one or more times.
* For example, `/c[a]+r/` checks if there is at least one 'a' after c.

### Meta characters (Details)
**Definition:** Meta characters are the characters which have special meaning in regular expressions.
**Attributes:**
| Meta Character | Description | Example |
|---|---|---|
| `[]` | Bracket expressions create a character class to match a single character within the brackets. `-` can be used to specify a range. | `[xyz]` matches 'x','y','z'. `[a-z]` matches any letter from 'a' to 'z' |
| `.` | Matches any single character, except a newline. Inside a bracket expression, it becomes a real dot. | `b.t` matches "bat", "bRt", "b8t" etc. |
| `[^]` | Matches a single character that is not within the brackets. | `[^xyz]` matches 'a','6' etc. |
| `\|` | "or" expression to match alternatives | `bat\|cat` matches "bat" or "cat" |
| `()` | Groups expressions to form sub expressions. Also used to capture groups | `Ma(nn\|itt)er` matches "Matter" or "Manner" |
| `^` | which specifies the beginning of the string | `^an` matches "ant", "ankle". Does not match "man" "plan" |
| `$` | which specifies the end of the string | `an$` matches "man","plan". Does not match "ant","ankle" |
**Notes:**
* These are the following few important meta characters.

### Quantifiers (Details)
**Definition:** Quantifiers are the symbols which specify the frequency at which a character should/can appear.
**Attributes:**
| Meta Character | Description | Example |
|---|---|---|
| `?` | Matches the preceding element zero or one time | `Ba?it` matches "Bait" and "Bit" |
| `*` | Matches the preceding element zero or more time | `10*1` matches "11","1001"etc |
| `+` | Matches the preceding element one or more time | `10+1` matches "101","10001" etc |
| `{m}` | Matches the preceding element exactly m times | `10{4}1` matches "100001" |
| `{m,}` | Matches the preceding element m or more time | `10{3,}1` matches "10001","100001"etc |
| `{m,n}` | Matches the preceding element minimum m times and maximum n times | `xy{2,3}z` matches "xyyz" and "xyyyz" |

### Predefined Classes
**Definition:** Predefined classes are set of meta characters grouped together and given a special symbol.
**Attributes:**
| Meta Character | Description | Alternative |
|---|---|---|
| `\w` | Alphanumeric characters and the underscore | `[A_Za-z0-9]` |
| `\W` | Non-word characters | `[^A_Za-z0-9]` |
| `\d` | Digits | `[0-9]` |
| `\D` | Non-Digits | `[^0-9]` |
| `\s` | Whitespace characters | `[\t\n\f\r]` |
| `\S` | Non-whitespace characters | `[^\t\n\f\r]` |
**Notes:**
* These are the following commonly used predefined classes.

### Escaping characters that have special meaning
**Notes:**
* To escape any characters which has special meaning just prefix it by `\`.
**Examples:**
* For example, `\S` indicates escape the special meaning of S and treat it as a regular character.

### Tryout: Pattern Matching
**Definition:** The given code helps you to understand the concept of regular expressions, usage of match function, and a JavaScript program to check whether the string matches with regular expression.
**Syntax:**
```javascript
function validateName(name, pattern) {
if(name.match(pattern)){
console.log("match found");
}
else {
console.log("match not found");
}
}
var name = "$John";
var regEx = /\$/; //check for $ character in the name"
validateName(name, regEx)
```
**Attributes:**
| regEx | name |
|---|---|
| /hello/ | "helloworld", "hhelloworld", "Hello" (Does not match), "hello" (Matches), "hhello", "hablello", "hallo" |
| /h[abc]llo/ | "hello" (Does not match), "hablello", "hallo" |
| /c[a]+r/ | "car", "cr" (Does not match), "caar", "caer" (Does not match) |
**Notes:**
* Task: Change the value of `regEx` and `name` with different expressions as given in the table.
*CrossReferences:* match function

### Error in Code
**Definition:** The below code will throw an error.
**Syntax:**
```javascript
function validateName(name) {
if(name.Match(/[\$\#]/)){ // Error here: Match is capitalized
console.log("Input is invalid");
return false;
}
else {
console.log("Input is valid");
return true;
}
}
function validate(){
validateName("Hello");
}
validate()
```
**Notes:**
* The error occurs because the `validateName()` method has a typing mistake. The method name is 'match' and not 'Match' with a uppercase 'M'.
* Because of this the code will crash.
**CommonMistakes:**
* ⚠️ Code will crash due to capitalization error: `name.Match` is not a function.
* ⚠️ When the code crashes, the end user will not get any message in the browser screen. We have to look at the details of the error in the console.
*CrossReferences:* validateName()

### Error Stack
**Definition:** When an error occurs, the stack trace of the error is displayed in the console.
**Examples:**
* Stack Trace:
```
►Uncaught TypeError: name.Match is not a function at validateName (fullScreenPreview.html:9) at validate (fullScreenPreview.html:5) at fullScreenPreview.html:1
```
**Notes:**
* It provides information regarding the name, message, error stack, and the location of the error, which helps in debugging.
* Tracing the error (from stack trace): Error occurred at `validateName()` method; `validateName()` was called by `validate()` method; `validate()` was invoked by click of button in the browser.
*CrossReferences:* validateName(), validate()

### Exception Propagation
**Definition:** In JavaScript, all errors are of type error object. These objects carry the information related to the error, including the stack trace.
**Syntax:**
```javascript
function validateName (name) {
if(name.Match(/[\$\#]/)){
console.log("Input is invalid");
return false;
}
else {
console.log("Input is valid");
return true;
}
}
function validate(){
validateName("Hello");
}
validate()
```
**Notes:**
* Whenever an exceptional event occurs, the browser environment generates the error object and throws it.
* The moment an error object is thrown, further execution of the program is stopped.
* If error is not handled, then the error will be propagated to the calling environment (calling method or browser).
* Exception propagation steps: Error generated inside `validateName()` -> propagated back to `validate()` -> propagated back to button click event -> propagated back to its calling environment i.e. browser.
* When the browser receives the error, it shows the stack trace in the console and terminates the program.
*CrossReferences:* validateName(), validate()

### Error Object
**Notes:**
* The Error object contains three properties: name, message, stack.
**Attributes:**
* name: Defines name/type of the error (e.g., 'TypeError').
* message: Is a short description about the error (e.g., 'name.Match is not a functiori', because Match() function with uppercase 'M does not exist).
* stack: A full stack trace of the error, with error name, error message, file name, method, line information about where the error has occurred.

### Here are some built-in error objects in JS
**Notes:**
* There can be different values for the name property, which signify different Error objects thrown during the execution of JS program.
* EvalError: Is an instance of Error which represents than an error occurred regarding the global function. Example: `eval()`.
* InternalError: Is an instance of Error which represents an internal error in the JavaScript engine. Example: "too much recursion".
* RangeError: Is an instance of Error which represents than an error occurred when a numeric variable or parameter is outside of its valid range.
* ReferenceError: Is an instance of Error which represents than an error occurred when de-referencing an invalid reference.
* SyntaxError: Is an instance of Error which represents than an error occurred while parsing some input in `eval()` or in `JSON.parse()`.
* TypeError: Is an instance of Error which represents than an error occurred when a variable or parameter is not of a valid type.
* URIError: Is an instance of Error which represents than an error occurred when `encodeURI()` or `decodeURI()` are passed with invalid parameters.
*CrossReferences:* eval(), JSON.parse(), encodeURI(), decodeURI()

### Try-catch block
**Definition:** Error handling is important, as unhandled errors can lead to abrupt termination of the program. These errors can be handled by using try-catch block.
**Syntax:**
```javascript
function validateName(name) {
try {
if (name.Match(/[\$\#]/)) {// error occurs here
/* All the below lines of try do not run
as error was thrown in previous Line*/
return false;
}
else {
return true;
}
}
catch (error) {
// code for Handling error
console.log(error.message);
}
}
validateName("Josh")
```
**Notes:**
* The code that can throw an error should be enclosed inside the `try` block.
* A `try` block should be immediately followed by a `catch` block.
* A `catch` block is an error handler which can handle the error.
* The error object thrown from `try` block will be passed as parameter to `catch` block.
**CommonMistakes:**
* ⚠️ Once the error object has been thrown, the next immediate lines in the `try` block will not be executed.
* ⚠️ If the wrong method name (e.g., `name.Match`) is used, an error object is created and thrown. This object is caught by the catch block.
*CrossReferences:* validateName()

### Conditional Statements in a Catch block
**Definition:** Since JavaScript is dynamically typed language, we cannot specify the different catch blocks for each error instance. Instead, we can use some conditional statements inside the catch block.
**Syntax:**
```javascript
function validateName(name) {
try {
if (name.Match(/[\$\#]/)) {// error occurs here
/* All the below lines of try do not run
as error was thrown in previous Line*/
return false;
}
else {
return true;
}
}
catch (error) {
if (error instanceof TypeError)
console.log("Type Error Occurred");
else if (error instanceof RangeError)
console.log("Range Error Occurred");
else if (error instanceof SyntaxError)
console.log("Syntax Error Occurred");
else
console.log("Some other Error Occurred");
}
}
validateName("Josh$");
```
**Notes:**
* Inside the catch block, we check the type of the error object by using `instanceof` operator and handle them separately.
*CrossReferences:* instanceof, TypeError, RangeError, SyntaxError

### Finally block
**Definition:** The finally block ensures that the code will be executed, irrespective of whether an error has occurred or not.
**Syntax:**
```javascript
function validateName(name) {
try {
if (name.Match(/[\$\#]/)) {// error occurs here
/* ALL the below lines of try do not run
as error was thrown in previous Line*/
return false;
}
else {
return true;
}
}
catch (error) {
console.log("Error Occurred");
}
finally{
console.log("Cleaning up resources");
}
}
validateName("josh$");
```
**Notes:**
* An error inside a try block causes the rest of the code to be skipped.
* Important code which must be executed in all conditions (e.g., closing database/file connection, releasing memory for objects) should be kept inside `finally`.
* A try block should be always followed by either a catch block or a finally block or both.
**CommonMistakes:**
* ⚠️ Keeping crucial code inside `try` block when errors are possible (execution cannot be guaranteed).
*CrossReferences:* try-catch-finally

### Throwing of Error
**Definition:** Apart from the code throwing errors, we can also programmatically create our own errors and throw them to change the flow of execution.
**Syntax:**
```javascript
var err = new Error();
//You can pass the message or not it is optional
err.name = "InvalidEmailError";
err.message = "Invalid Email";
throw err;
```
```javascript
function validateName(name) {
try {
if (name.match(/\$/)) {
throw new Error("Name should not contain $");
}
else {
return true;
}
}
catch (error) {
console.log(error.message);
}
finally{
console.log("Cleaning up resources");
}
}
validateName("Hello$");
```
**Notes:**
* This can be done by creating a new object of `Error` class and passing our own name and message to it.
*CrossReferences:* Error class

### Summary (Error Handling)
**Notes:**
* When an error occurs, the JavaScript program crashes and we need to handle it.
* Exceptions propagate from across functions until handled.
* `try`, `catch`, `finally` is used to handle errors.
* `finally` block of code will **always run**.
*CrossReferences:* try catch finally

### Tryout: trycatchfinally
**Definition:** The given code highlights the creation of try-catch and finally block. A JavaScript program to check whether the string has '$' symbol in it, and if the name has $ (dollar symbol) then the function will throw an error.
**Syntax:**
```javascript
function validateName(name) {
try {
if (name.match(/\$/)) {
throw new Error("Name should not contain $");
}
else {
return true;
}
}
catch (error) {
console.log(error.message);
}
finally{
console.log("Cleaning up resources");
}
}
validateName("Hello$");
```
*CrossReferences:* try-catch, finally block, throw new Error

### Exercise: Regular Expression (Date search assignment)
**Definition:** Write a JavaScript program to search a date within a string.
**Examples:**
* Sample Input: "Albert Einstein was born in Ulm, on 14/03/1879."
* Sample Output: 14/03/1879.

### Exercise: Regular Expression (Email validation pattern)
**Definition:** Write a pattern that matches e-mail addresses. Syntax: localpart@domain
**Attributes:**
| Sample Input | Sample Output |
|---|---|
| JohnDoe.12#4@gmail.com | "Matches the pattern" |
| John..Doe12#4@gmail.com | "Not matching" |
**Notes:**
* The local part (The text before @ symbol) contains the following ASCII characters: Uppercase (A-Z) and lowercase (a-z) English letters, Digits (0-9), Characters `! # $ % & * + - / = ? ^ _ { } ~`.
* Character `.` (dot) provided that it is not the first or last character and it will not come one after the other.

### JSON and Exception Handling Assignment - Exercise
**Definition:** Write a JavaScript function to validate whether a given value type is pure json object or not.
**Attributes:**
| Sample Input | Sample Output |
|---|---|
| key1: value1, key2: value2 | Invalid JSON |
| "key1": "value1", "key2": "value2" | Valid JSON |

### Exercise: JavaScript Object - Assignment
**Definition:** Write a JavaScript program to list the properties of a JavaScript object.
**Syntax:**
```javascript
var student = {
name: "David Rayy",
sclass: "VI",
rollno: 12
};
```
**Examples:**
* Sample Output: David Rayy, VI, 12

### What is an API?
**Definition:** An intermediate code through which you can interact partially with servers that have their code running on them.
**Examples:**
* google maps, tweets, Facebook post, etc. features in a webpage.
**Notes:**
* So far, core language features worked same in browser and Node.
* HTTP is stateless, meaning the server does not know which client is making the request.
* Companies don't give full access to their server code; instead they provide an API.
*CrossReferences:* HTTP, Node

### Web API
**Definition:** The API provided to our JS code by the browser is called as Web API.
**Examples:**
* Change the width of the browser.
* Load a different page in the address bar.
* Close the browser.
* Send a browser notification.
**Notes:**
* Apart from 3rd party API's, the environment (Node/Browser) in which the JS code runs has its own set of API's.
* The Web API allow us to interact with the browser through our JS code.
* `console.log()` is actually provided by the browser as part of its API, allowing interaction with the browser and printing to the console.
* Web APIs covered in the course are: XMLHttpRequest, DOM, Notification, Storage.
* Since these API's are provided by the browser, they will not work in Node.
*CrossReferences:* XMLHttpRequest, DOM, Notification, Storage, Node

### Security concern (Web API)
**Examples:**
* Example attack: XSS attack (Cross-Site Scripting).
**Notes:**
* Dynamically executing code is security-sensitive.
* Some APIs enable the execution of dynamic code by providing it as strings at runtime.
* Use of such APIs is frowned upon as they increase the risk of Injected Code (XSS attack) and have a huge impact on an application's security.
*CrossReferences:* XSS attack

### Asynchronous in JavaScript

#### How can we make JavaScript asynchronous?
**Notes:**
* JavaScript is single threaded, meaning all code will be executed in sequence. If code takes a long time (e.g., 2 seconds), the browser freezes, causing a bad user experience.
* We must execute code asynchronously whenever it takes a longer time to execute.
* The DOM API provides the facility to execute code asynchronously via `setTimeout(functionName, timeInMilliseconds)`.
* The asynchronous function `display` will print "After" before printing "Let's go to Trip" because `console.log("After")` does not wait for the previous step.
**Syntax:**
```javascript
function display(){
console.log("Let's go to Trip");
};
console.log("Before");
setTimeout(display, 3000)
console.log("After");
```
*CrossReferences:* DOM API, setTimeout

### AJAX
**Definition:** AJAX is a technique for sending request to the server without involving a page refresh.
**Notes:**
* Just like `setTimeout()`, AJAX techniques are also asynchronous in nature.
* When a request is sent to the server using AJAX, the page will not freeze till the response is received.
*CrossReferences:* setTimeout()

### Steps in AJAX
**Definition:** The JavaScript code can asynchronously connect to a server by using a new XMLHttpRequest() object. This is also called as AJAX.
**Syntax:**
```javascript
var xhr = new XMLHttpRequest(); // 1. Create request object

xhr.open('GET', url); // 2.Open the URL

xhr.onload = function () { // 3. Mention code to run when response is received
console.log("The response from server is "+xhr.responseText);
};

xhr.send(); // 4. Send the Request
```
**Notes:**
* Our JS code can contact the server and send/fetch data using the XMLHttpRequest API.
* The four steps for using AJAX are: Create new `XMLHttpRequest()`, Open a URL using the request object, Mention what should happen when a response is received, Actually send the request.
*CrossReferences:* XMLHttpRequest API

### AJAX DEMO
**Notes:**
* Highlights: Creation of AJAX call, An AJAX call to get data from a JSON file.
* The demo involves creating three files: `places.json`, `placesToVisit.html`, `placesToVisit.js`.
* `placesToVisit.js` defines `placesToVisit()` which uses `XMLHttpRequest` to fetch `places.json` and dump the response text into a div element.
*CrossReferences:* XMLHttpRequest, places.json

### Need for Callback
**Syntax:**
```javascript
let value;
function check(val) {
console.log(val);
}
function getTrip() {
setTimeout(function () {
value = "Let's go to Trip";
}, 1500);
}
getTrip();
check(value);// undefined
```
**Notes:**
* The function `check()` will print `undefined` because it does not wait for `setTimeout` (lines 6-8) which takes 1.5 seconds to execute.
* This problem of asynchronous function can be solved using callback.
**CommonMistakes:**
* ⚠️ Calling `check(value)` synchronously before the asynchronous operation completes (results in `undefined`).
*CrossReferences:* setTimeout, callback

### What is Callback?
**Definition:** A callback is a function which will get executed automatically after some other function gets executed completely. Thus, it is also called as call-after.
**Syntax:**
```javascript
function display(){
console.log("Let's go to Trip");
};
setTimeout(display, 3000);
```
**Notes:**
* We have already been looking at callbacks since we started discussing about `setTimeout`.
* In the example, `display()` is invoked automatically by `setTimeout` after 3000 milliseconds.
* Callback functions are those functions which are passed as a parameter to another function and invoked after the other function has completed its execution.
*CrossReferences:* setTimeout

### Asynchronous Callback
**Definition:** Using callback to address the problem of dealing with data in an asynchronous situation.
**Syntax:**
```javascript
let value;
function check(val) {
console.log(val);//"Let's go to Trip";
}
function getTrip(callback) {
setTimeout(function () {
value = "Let's go to Trip";
callback(value);
}, 1500);
}
getTrip(check);
```
**Notes:**
* We are passing `check` function as a callback to the `getTrip()` function.
* Now `check()` will be invoked inside `setTimeout()` instead of returning the data.
* Typically third party libraries expect you to pass a callback and they will invoke your callback after they have completed the task.
*CrossReferences:* setTimeout

### Tryout: Callback
**Definition:** The code given will explain the callback function, that can be used to avoid asynchronous execution of function. Here check function is passed as a callback in getTrip function.
**Syntax:**
```javascript
function check(value){
console.log(value);
}
function getTrip (callback) {
setTimeout(function () {
callback("Lets go to Trip");
}, 1500);
}
getTrip(check);
```
*CrossReferences:* callback, getTrip function

### Callback Hell
**Definition:** When a callback has a callback, the callbacks get nested to each other which leads to callback hell.
**Notes:**
* While doing multiple asynchronous operations, the callback get nested.
* Callback functions cannot be chained together which leads to nested callback while calling it multiple time.
* To overcome the problem of callback hell, we use promise.
**CommonMistakes:**
* ⚠️ Nested callbacks in multiple asynchronous operations (Callback Hell).
*CrossReferences:* promise

### AJAX - Exercise
**Definition:** Create a simple XMLHttpRequest, and retrieve data from a pets.json file and display it in the browser.
**Syntax:**
```javascript
{
"name":"John",
"age":31,
"pets":[
{ "animal": "dog", "name":"Fido" },
{ "animal":"cat", "name":"Felix" },
{ "animal":"hamster", "name":"Lightning" }
]
}
```
**Notes:**
* Note: The `pets.json` file contains the provided json object (in Syntax field).
*CrossReferences:* XMLHttpRequest, pets.json

### Promise
**Definition:** Just like in real life, a promise is an object that may produce a single value some time in the future.
**Syntax:**
```javascript
function getTrip(){
return new Promise(function(resolve){
setTimeout(function() {
resolve("Lets go to Trip");
}, 2000);
});
};
```
**Attributes:**
* A promise can be: resolved (succeeded), rejected (failed), pending (Hasn't fulfilled or rejected yet).
**Notes:**
* Promise can be created using `new Promise()`.
* When creating a promise, we pass a function as a parameter. The code that will be executed in future is placed inside this function.
* `resolve` is the data that we are promising.
*CrossReferences:* new Promise(), setTimeout

### How to resolve a promise?
**Syntax:**
```javascript
promiseObject.then(
function (futureData) {
...
})
```
```javascript
getTrip().then(
function (futureData){
console.log(futureData);
}
);
```
**Notes:**
* The above example will invoke the function inside `then` after 2000 milliseconds as `getTrip()` resolves a promise only after 2000 ms.

### Resolve and Reject in a Promise object
**Definition:** Resolving a promise is valid only if nothing goes wrong. What if something goes wrong and we are not able to keep the promise? Then we need to reject the promise instead of resolving the promise. So instead of returning the promised data, we can return an error. In any new Promise we can define resolve and reject both.
**Syntax:**
`new Promise (resolve, reject) { }`
**Examples:**
* Example 1 (Resolved):
```javascript
function getTrip (location) {
return new Promise(function(resolve, reject) {
if (location == "ooty") {
resolve("Trip to " + location);
} else {
reject(Error("Some error occured"));
}
});
}
// Calling resolved case
getTrip("ooty").then(
function(data) {
console.log(data);
},
function(error) {
console.log(error);
}
);
// Trip to ooty
```
* Example 2 (Rejected):
```javascript
getTrip("coorg").then(
function(data) {
console.log(data);
},
function(error) {
console.log(error.message);
}
);
// Error: Some error occurred
```
**Notes:**
* In any new Promise we can define resolve and reject both.

### Promise Chaining in Javascript
**Definition:** Sometimes in real life, we make multiple promises which are interdependent on each other. Only if we fulfill the first promise, the second promise even makes sense. If we fail to keep the first promise, then the second promise cannot be fulfilled.
**Syntax:**
```javascript
function bookFlight(){
return new Promise(function(resolve){
setTimeout(resolve(5600), 2000);
})
}
function bookHotel (flightPrice){
return new Promise(function(resolve){
setTimeout(resolve(7000+flightPrice), 1000);
})
}
```
**Notes:**
* Example: one to book flight and the other to book hotel. Each promise is resolving the amount of money spent for the booking.

### Resolving promise chaining
**Definition:** To ensure that the second promise is resolved only after the first promise is resolved, we can chain these promises together.
**Syntax:**
```javascript
function bookFlight() {
return new Promise(function (resolve) {
setTimeout(resolve(5600), 2000);
})
}
function bookHotel (flightPrice) {
return new Promise(function (resolve) {
setTimeout(resolve(7000 + flightPrice), 1000);
})
}
bookFlight()
.then(function (flightData) { return bookHotel (flightData) })
.then(function (cumulativeData) { console.log(" Total is " + cumulativeData) })
```
**Notes:**
* The promise returned by the first `then` is chained and resolved in the next `then`.

### Rejecting chained promises
**Definition:** What will happen if any of promises fail in the chained promises? Promises after the failed promise will not be resolved. It will throw an error and promises in chain will not be executed after it.
**Syntax:**
```javascript
function bookFlight(airline) {
return new Promise(function (resolve, reject) {
if (airline == "AirIndia") {
setTimeout(resolve(5600), 2000);
} else {
reject(Error("Flight can not be booked"))
}
})
}
function bookHotel (flightPrice) {
return new Promise(function (resolve) {
setTimeout(resolve(7000 + flightPrice), 1000);
})
}
bookFlight("indigo")
.then(function (flightData) { return bookHotel(flightData) })
.then(function (cumulativeData) { console.log(" Total is " + cumulativeData) })
.catch(e => console.log(e.message))
```
**Notes:**
* The promise returned by the first then will throw error.

### Usage of Async/Await to handle promises
**Definition:** We can simplify chaining of promises using a concept called as async-await.
**Syntax:**
```javascript
function bookFlight() {
return new Promise(function (resolve) {
setTimeout(resolve(5600), 2000);
})
}
function bookHotel (flightPrice) {
return new Promise(function (resolve) {
setTimeout(resolve(7000 + flightPrice), 1000);
})
}
function getTotal(){
bookFlight()
.then(function (flightData) { return bookHotel(flightData) })
.then(function (cumulativeData) { console.log(" Total is " + cumulativeData) })
}
getTotal()
```
```javascript
async function getTotal(){
var flightData=await bookFlight();
var cumulativeData=await bookHotel(flightData);
console.log(" Total is " + cumulativeData)
}
```
**Notes:**
* Simplifying promise handling using async/await involves two steps: 1. Add `async` keyword in front of `getTotal()`. 2. Instead of using `then()`, add `await` keyword in front of method invocation and store the returned value.
* Whenever we have await, the code will wait for the promise to be resolved/rejected.
* `await` can be used only inside `async` functions.

### Security Concern (Async/Await)
**Notes:**
* `Await` should only be used in promises: The point of await is to pause execution until the Promise's asynchronous code has run to completion. With anything other than a Promise, there's nothing to wait for. This rule raises an issue when an awaited value is guaranteed not to be a Promise.

### Tryout: Async / Await
**Definition:** To simplify the given code we can use async and await in Promise Chaining. Copy and replace the `getTotal` function with given code.
**Syntax:**
```javascript
function bookFlight() {
return new Promise(function (resolve) {
setTimeout(resolve(5600), 2000);
})
}
function bookHotel (flightPrice) {
return new Promise(function (resolve) {
setTimeout(resolve(7000+ flightPrice), 1000);
})
}
function getTotal(){
bookFlight()
.then(function (flightData) { return bookHotel(flightData) })
.then(function (cumulativeData) { console.log(" Total is " + cumulativeData) })
}
getTotal()
```

### Unit Testing
**Definition:** Unit testing involves the execution of a JavaScript function to evaluate if the output returned is the expected one. It helps us test if one or more features of a JavaScript function are working as per expectation.
**Notes:**
* Features indicate the extent to which the JavaScript application being tested: meets the requirements that guided its design and development, responds correctly to all kinds of inputs, achieves the general result its stakeholders desire.

### Automated Testing
**Notes:**
* JavaScript has no compiler and no static type-checking in the code. As JavaScript developers we continuously write new code or extend the existing code. In either of the scenarios, if code fails, as developers we can see it only on the browser during execution and not before that.
* To debug or write endless console statements in our code are manual ways of testing the JavaScript code. This process is too slow.
* We should have automated ways of finding the bug in the code and avoid the chaotic and time consuming debugging. Automated testing will enable us to programmatically check or test the functionality of our code before we execute it and watch it fail.
* In this course we will use Jasmine unit testing framework.

### Jasmine Testing
**Syntax:**
```javascript
function totalTravelFare (baseFare, taxPercentage){
var finalFare;
finalFare = baseFare*(1+taxPercentage/100);
return finalFare;
}
```
**Notes:**
* Steps to test this code: Step 1: A test suite should be created. Step 2: Test specs should be created for all the possible scenarios. Step 3: Test specs should be created in order to check whether the result variable is defined or not. Step 4: Test suite should be executed with the help of Karma.

### Test suite
**Definition:** A test suite is a grouping of relevant test cases which are executed together.
**Syntax:**
`describe(title, function(){})`
```javascript
describe('TotalTravelFare calculation Suite:',function(){
});
```
**Notes:**
* `describe()` is a global Jasmine function.
* It helps in defining the test context by creating a new test suite.
* It accepts two parameters: A title (of string type) or name of the test suite, A function containing specs which belong to this suite.

### Test spec
**Definition:** A test spec is the actual test case.
**Syntax:**
```javascript
describe('TotalTravelFare calculation Suite:',function(){
it('Test Case 1: Inputs are correct', function(){
expect(totalTravelFare(1000,20)).toEqual(1200);
});
});
```
**Notes:**
* `it` is also a global Jasmine function.
* It helps translate the acceptance criteria into Jasmine spec.
* It accepts two parameters: Title or name of the test suite, Function containing spec code.

### expect()
**Definition:** It is a global Jasmine function that helps in writing the assertions.
**Notes:**
* It takes only one parameter: Actual value to be tested.

### toEqual()
**Definition:** Matcher is used to compare the actual and expected output.

### Matchers
**Definition:** Matchers are Javascript functions which are used to compare the expected and the actual output in any test case.
**Attributes:**
| Method | Description |
|---|---|
| toBe(expected) | expect the actual value to be `===` to the expected value |
| toBeDefined() | expect the actual value to be defined. (Not `undefined`) |
| toBeFalsy() | expect the actual value to be falsy |
| toBeTruthy() | expect the actual value to be truthy. |
| toBeGreaterThan(expected) | expect the actual value to be greater than the expected value. |
| toBeLessThan(expected) | expect the actual value to be less than the expected value. |
| toEqual(expected) | expect the actual value to be equal to the expected, using deep equality comparison. |
| toMatch(expected) | expect the actual value to match a regular expression |
| toThrow(expected) | expect a function to `throw` something |
**Notes:**
* Note: To learn and explore more about Jasmine Matchers.

### Karma - a test runner
**Definition:** Karma is a test runner tool.
**Syntax:**
`npm install -g karma jasmine-core`
**Notes:**
* Karma is: A tool that spawns a web server which executes the source code against the test code for each browsers connected.
* When executed, it automatically captures the browser specified by the developer during Karma configuration.
* It then displays the results on the command line.
* It watches all the files specified within configuration file and if there are any changes, it will trigger the corresponding spec again on the browser.

### Summary (Jasmine components)
**Notes:**
* In the last section we learnt the following about unit testing in JavaScript.
* Create a test suite
* Create a test spec
* Create positive and negative test cases
* Run test suites with the help of Karma
* Use different matchers in Jasmine

### Problem Statement:- (Testing Assignment - Exercise)
**Definition:** Create the test suite and test specs for the following code.
**Syntax:**
```javascript
var result = 0;

function add(a, b) {
result = a + b;
return result;
}

function isZero(b) {
return (b == 0) ? true : false;
}

function divide(a, b) {
return isZero(b) ? "Cannot divide by zero" : result = a / b;
}

function substract(a, b) {
return result = a - b;
}

function multiply(a, b) {
return result = a * b;
}
```
**Notes:**
* Write two test specs for each of the above functions.

### Problem Statement:- (Promise Assignment - Exercise)
**Definition:** Create a Promise that generates a random number after 2 seconds. If the random number is greater than 0.5, the Promise should be resolved and the result should be logged to the console. If the random number is less than or equal to 0.5, the Promise should be rejected and the error should be logged to the console.

### Problem Statement:- (AJAX Assignment - Exercise)
**Definition:** Create a simple HTML page with some initial text and a button. An AJAX call should be made when clicked on the button. The initial text must change to the text received from the response.

### DOM Structure
**Notes:**
* Here the DOM objects are shown along with the HTML code.
* Before we learn how to access these DOM objects (also known as Nodes), we will see how they are arranged in a hierarchical fashion.
* Note: Window object depicts our browser. It is root node for the rest of the objects.

### DOM Hierarchy
**Notes:**
* The above diagram is a simple hierarchy of the few important objects that depicts how the DOM Tree is represented for an HTML document with an image tag, an anchor tag and a form tag which consists of input controls like text, textarea, checkbox and radio buttons.

### DOM methods
**Definition:** Here are a few widely used DOM methods.
**Notes:**
* `getElementById(id)`: It is used to access element by its id.
* `getAttribute("attributeName")`: It is used to access the tag attribute of the DOM object.

### DOM atttributes
**Definition:** Few widely used DOM attributes are as follows-
**Notes:**
* `innerHTML`: innerHTML is used to set or get the HTML content of the element.
* `innerText`: innerText is used to set or get the Text content to element.
* `value`: value is used to get or set value of the element.
* `checked`: checked is used on checkbox and radio button. It is used to check either they are checked or not. If they are checked, it returns true else it returns false.
* `disabled`: disabled is used to get or set the disabled status of the element. If disabled is set to true, then the element becomes disabled.

### Some common methods associated with the window object are
**Examples:**
* `window.alert("Hello");` is the same as `alert("Hello");`
**Notes:**
* `alert("message")` - this will display an alert box with the given message.
* `confirm("message")` - this will display an confirm box with the given message.
* Since window is the top most object, we can ignore it in the code.

### One of the most common method associated with the document object is
**Notes:**
* `write("message")` - this will overwrite the existing HTML content of the page with the message given.

### DOM Example
**Definition:** In this example, we will see how to access text input, checkbox and radio button in DOM as well as how to set HTML to document.
**Notes:**
* The script to access DOM should be after all the DOM elements are loaded. Therefore the script tag for DOM access is placed as the last statement of the body tag.
* This example will cover previous concepts.

### Event Object
**Definition:** When an event occurs, an event object is created, which will have details about the event.
**Notes:**
* In order to access the event object, we need to pass it in the event handler as a parameter.
* The event object is passed as a parameter to a JS function called `display`. We can access the event object in the JavaScript code as shown below: `function display(e){ console.log(e); }`.
* The output displays all details of the event object. We can see that event object has many details. We will focus only on some of them in the coming pages.

### Event Target
**Definition:** We can get details of the element on which the event took place using `event.target`.
**Notes:**
* The target object gives the DOM object and from it we can get the various properties.

### Event Bubbling
**Definition:** When an event occurs on an element, that event 'bubbles' up to all its parent tags as well. This will in turn trigger the event handlers of those parent tags as well.
**Notes:**
* Div2 is a child of Div1. Both of them have onclick event handlers which execute different functions. When Div2 is clicked, it executes the div2Click() and then the event bubbles up to its parent which is Div1. Now the click event comes to Div1 and it executes div1Click() event handler as well. This is called as event bubbling. To stop event bubbling, divClick2 has to be modified (content not shown).

### Event Prevention
**Definition:** Sometimes, when an event occurs, we may want to stop its further behaviour.
**Notes:**
* For example, we may want to stop a page from getting submitted, if the validations fail or we may want to prevent event bubbling from happening. In such cases if we use `event.preventDefault()` it will prevent the default behaviour of the event.
* The page submission will now not happen if the username is less than 6 chars.

### Web Storage API

#### What is web storage?
**Definition:** Web Storage is basically a local storage space in the clients hard disk. The data is stored in the clients' local storage rather that being sent to the server.
**Notes:**
* HTTP is stateless. HTML5 introduced Web Storage API.
* For example, if you add items to a cart on a shopping app, they can be stored in the local storage rather than being sent to the server.
* Thus, when the page loads again, the data can be retrieved from the local storage itself, thereby reducing load on the server.
* Note: Each website has a separate localstorage area allotted to them. Therefore Google cannot access what Amazon has stored in the clients localstorage. Also each browser has a different localstorage. That means what Google stores in localstorage of a client machine using chrome, will not be able to access that data if the user logins from Internet Explorer as IE has its own localstorage.
*CrossReferences:* HTTP, HTML5

#### Web Storage API (Features)
**Notes:**
* Large amount of data can be stored - Atleast 5MB data can be stored in client machine.
* Reduced network overhead - Stored data is never send back to web server. Hence, there are no additional HTTP request-response cycle.
* Secure - Each domain is given a part of memory in client's machine. Webpages from same domain can share data. One domain cannot override/access data of another domain. Hence, it is ensures data security.

#### How to use Web Storage
**Notes:**
* We can store the data using web storage in two ways:
* 1. For particular session i.e. session storage: For session storage, `sessionStorage` object is used
* 2. Across sessions i.e. local storage: For local storage, `localStorage` object is used
* Both these objects are created by JS runtime engine of browser.
* Web storage API provides following four methods for managing data: `setItem(key, value)`, `getItem(key)`, `removeItem(key)`, `clear()`.
* Data is stored in the form of (key, value) pair and both key and value are stored as String.

### Notification API
**Definition:** We can create desktop notifications in JavaScript using the Notification API
**Notes:**
* Showing desktop notification involves 2 steps: 1. User needs to grant permission to website for displaying notifications. In order to request the permission from the user `requestPermission()` of Notification object can be used as show below: `Notification.requestPermission()`. 2. Create a notification. This is discussed in the upcoming page.

#### Create a Notification API
**Syntax:**
`new Notification (title, options)`
**Notes:**
* Function `notify()` combining steps: `Notification.requestPermission()`, check permission == "default", if so alert("Please grant permission"), else `var notify = new Notification("New Mail", {body: "You have 1 unread email"});`.

#### Properties of Notification object
**Notes:**
* `body`: Defines notification message.
* `permission`: Static property representing current permission status (denied, granted, default).

### XSS Vulnerability
**Definition:** Cross-Site Scripting (XSS) attacks are nothing but injecting an attack code on the client-side.
**Notes:**
* Responsive web pages handle information related to end user. Example: username and password.
* And these information needs to be protected. Information assurance is the practice towards achieving the same.
* A vulnerability is a weakness of system which when exploited can reduce that system's information assurance.
* These vulnerabilities can give way to attacks with intend to access and manipulate application as well as sensitive information.
* Hackers can exploit these vulnerabilities to extract user's private data, like cookies or other session information.
* One such vulnerability is Cross site scripting (XSS). It is one among the ten most critical web application security risks as per OWASP Top 10 – 2013.

#### XSS vulnerabilities example
**Notes:**
* XSS vulnerabilities may occur when: Inputs provided to the web app are not validated, HTML encoding is not applied, then the browser interprets output as code.
* Prevention rules: Validation to filter out user input; Encoding escapes the user input only as data, not as code so that the browser interprets accordingly.

### Summary (Cross Site Scripting)
**Notes:**
* In this course, we learned the following features of JavaScript
* Create and access variables in different scopes
* Perform form input field validations using RegEx
* Handle various errors using try-catch and finally blocks
* Use HTML APIs like local storage, notification
* Create test cases for a JavaScript function using Jasmine
* Run test cases by using Karma as test runner

<CoverageCheck>
- Total topics extracted: 98
- Any missing or unclear sections: The topic "How to resolve a promise?" had its content structure cut off in the provided snippet, requiring manual reconstruction based on surrounding context in the OCR.
- Approx. compression ratio vs original text: Moderate (Structured lists/tables replace dense paragraphs).
- Warnings (if text seemed incomplete): The definition for several early topics (Datatypes, Comments, Variable, ECMAScript Versions) was implicitly missing, replaced with 'Skipped'.
</CoverageCheck>
