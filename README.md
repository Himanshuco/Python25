# Python25
My Python study notes + codes (2025).

# Python Notes

## Why Python for Beginners?

Python is an excellent choice for beginners due to the following reasons:

- **Easy-to-learn syntax**: Python has a clear, readable, and simple syntax, making it easier for beginners to understand programming concepts.
- **Quick setup**: Python can be easily installed and set up on most operating systems. The installation process is straightforward, and Python is ready to use almost immediately after installation.

## Sample Use Cases

Python is used in a variety of applications. Some popular use cases include:

- **Data processing**: Python's libraries like Pandas and NumPy make it great for handling and processing large datasets.
- **Web scraping**: Libraries such as BeautifulSoup and Scrapy allow you to extract data from websites for various purposes, such as research or automation.
- **Automation**: Python can be used to automate repetitive tasks like file management, web interactions, and more.
- **Web development**: Frameworks like Django and Flask are widely used to build web applications.

# Writing a Python Program

## Structure of a Python Program

A typical Python program is composed of several elements, including statements, functions, and comments. Let's break down the essential parts:

- **Writing your first "Hello, World!" program**:

  Python programs are simple and easy to write. Here is the traditional first program in Python:

  ```python
  print("Hello, World!")
```

```python
if True:
    print("This is indented")
```

# The Python Interactive Shell

## What is the Interactive Shell?

The **Python Interactive Shell** is an environment that allows you to execute Python code in a **REPL** (Read-Eval-Print Loop) manner. It provides an interactive way to test and debug Python code snippets. 

In a REPL, the process works as follows:
1. **Read**: You enter a line of code.
2. **Eval**: The code is evaluated (executed).
3. **Print**: The result of the evaluation is printed.
4. **Loop**: The process repeats, allowing you to interactively test and refine your code.

This environment is particularly useful for beginners and developers who want to quickly test code, learn syntax, or debug small pieces of code without writing an entire script.

## Accessing the Shell

You can launch the Python Interactive Shell in the following ways:

- **Launching via the terminal**:
  
  To access the shell through the terminal (on macOS, Linux, or Windows), open your command line interface and type the following command:

  ```bash
  python
  ```

# Values and Variables

## What are Values?

In Python, **values** represent data or information that is manipulated or used in calculations. Values can be of various types, such as numbers, strings, or more complex data structures. Python supports a wide range of data types.

### Examples of Values:
- **Integer**: A whole number without a decimal point.  
  Example: `42`
  
- **Float**: A number that contains a decimal point.  
  Example: `3.14`
  
- **String**: A sequence of characters enclosed in either single or double quotes.  
  Example: `"Hello"`, `'Python'`
  
### Other Data Types:
Python also has many other data types such as:
- **Booleans**: Represent `True` or `False` values.
- **Lists**: Ordered collection of items.
- **Tuples**: Immutable collection of items.
- **Dictionaries**: Key-value pairs for storing data.

## Variables

A **variable** is a symbolic name that is used to store a value. Variables are used to represent and store data that can be accessed and manipulated throughout the program.

### Syntax:
To create a variable in Python, you use the following syntax:

```python
variable_name = value
```

```python
valid_variable = 10
_valid_variable = 20
```

```python
invalid-variable = 5  # This will result in an error.
valid_variable_name = 6  # This is correct.
```

```python
myVar = 10
myvar = 20
print(myVar)  # Outputs: 10
print(myvar)  # Outputs: 20
```

# Expression and Arithmetic

## What is an Expression?

In Python, an **expression** is a combination of **values**, **variables**, and **operators** that Python evaluates to produce a result. Expressions can involve arithmetic, comparisons, logical operations, and more.

### Example of an Expression:

```python
2 + 3 * 5  # This evaluates to 17
```

# Operator Precedence
Python follows the standard order of operations, often referred to as PEMDAS (Parentheses, Exponentiation, Multiplication/Division, Addition/Subtraction). This defines the order in which operations are performed in an expression.

## Operator Precedence:
1. Parentheses (): Operations inside parentheses are evaluated first.
2. Exponentiation **: Exponentiation is evaluated next.
3. Multiplication *, Division /, Floor Division //, Modulus %: These operations are performed after exponentiation.
4. Addition +, Subtraction -: These operations are performed last.

  ```python
    result = (5 + 3) * 2  # Result is 16
  ```

  


