# Simple Readable Mathematical Language Interpreter

This is a fully featured interpreter for a simple, readable mathematical language, built from scratch in Python. This project showcases the implementation of tokenization, parsing, evaluation, and the core principles of how interpreted programming languages work. It also features a REPL(Read Eval Print Loop) for easy user access and experimentation. Please see bottom for the syntax guide.

## Features

-   **Arithmetic Operations:** Supports addition (`+`), subtraction (`-`), multiplication (`*`), division (`/`), and exponentiation (`^`).
-   **Correct Operator Precedence:** Follows standard PEMDAS rules.
-   **Correct Associativity:** Handles left-associative operators (`+`, `-`, `*`, `/`) and right-associative operators (`^`) correctly.
-   **Parentheses:** Supports nested parentheses for grouping expressions.
-   **Unary Operators:** Correctly parses and evaluates unary negation.
-   **Comparison Operators:** Supports `equals` (==), `nequals` (!=), `lt` (<), `lte` (<=), `gt` (>), `gte` (>=) for equality and magnitude comparisons.
-   **Variables:** Allows for variable assignment and usage throughout a session.
    ```
    define x as 10
    define y as x * 2
    y + 5  // Result: 25
    ```

## Core Files in Project Structure

-   `Interpreter.py`: Interpreter
-   `Parser.py`: Contains the tokenizer, turns input into AST(Abstract Syntax Tree)
-   `AST.py`: Defines the class structure for the nodes of the Abstract Syntax Tree (e.g., `NumberNode`, `OperatorNode`, `AssignmentNode`). Also includes evaluation methods for each type of Node.
-   `Evaluator.py`: A simple wrapper that starts the evaluation process on the root node of the AST.

## How It Works

### 1. Parsing

Parser -> Abstract Syntax Tree

-   **Tokenizer:** The input string is first broken down into a list of tokens (e.g., `"5 + 3 * 2"` -> `['5', '+', '3', '*', '2']`).
-   **Recursive Descent Parser:** The parser uses a series of hierarchical functions to build the AST. Each function is responsible for a specific level of operator/action precedence.
    -   `parse_whole` handles the main parsing logic and routes to appropriate parsers.
    -   `tokenize` converts input strings into tokens.
    -   `parse_basic` handles numbers, variables, booleans, and parentheses.
    -   `parse_unary_expression` handles `-var` and `!true`.
    -   `parse_high` handles `^`.
    -   `parse_med` handles `*` and `/`.
    -   `parse_low` handles `+` and `-`.
    -   `parse_comparison` handles `equals`, `nequals`, `lt`, `lte`, `gt`, `gte`.
    -   `parse_variable_assignment` handles variable definition.
    
    All these parsing functions are called in a hierarchical order such that each expression is evaluated in accordance to operator precedence.

    The core arithmetic parsing functions are:
    -   `parse_low` 
    -   `parse_med` 
    -   `parse_high`
    
    This core parsing hierarchy enforces the order of operations. For example, in 5 + 3 * 2, parse_low would first be called, which would call parse_med on the right of the `+`. parse_med would return an operator node containing `3, 2, and *`, which would represent that multiplication. Then, the original `+` would be evaluated, resulting in an AST following PEMDAS.

The output of the parser is the root node of the AST. For `5 + 3 * 2`, the tree would look like this:

```
      OperatorNode(+)
         /       \
NumberNode(5)   OperatorNode(*)
                   /       \
            NumberNode(3)   NumberNode(2)
```

### 2. Evaluation Phase

Once the AST is built, the evaluation is a simple recursive process.

-   The `run` method in the interpreter calls the `.eval()` method on the root node of the tree.
-   Each node in the tree has its own `.eval()` method:
    -   A `NumberNode` simply returns its value.
    -   A `VariableNode` looks up its value in the environment.
    -   An `OperatorNode` recursively calls `.eval()` on its left and right children to get their values, and then performs the specified operation.
-   The final result bubbles back up the tree to the root, which is then returned to the user.

An **environment** (a simple dictionary) is passed through the evaluation process to keep track of variable assignments.


## How to Run

The simplest way to see the interpreter in action is to run the test suite.

-   HTTPS
```bash
git clone https://github.com/yourusername/interpreter.git
cd interpreter
python REPL_tester.py
```

-   SSH

```bash
git clone git@github.com:yourusername/interpreter.git
cd interpreter
python REPL_tester.py
```


## Syntax Guide

Syntax is defined as follows:

-   To perform simple arithmetic, simply type the expression out i.e. `2 + 3 * 5` -> `17`
-   To assign a variable x to a number 5, say `define x as 5`
-   To compare two objects (same as python ==), say `1 equals 1`
-   In the opposite case, say `1 nequals 1`
-   To compare values of magnitude i.e. `<, <=, >, >=` in python, say `lt, lte, gt, gte`. For example, `2 gt 3` -> `False`
-   To print out values, use `display` keyword. For example, assuming `x` is defined as `5`, `display x` -> `5`
-   For unary operators on a single value or variables, `!` and `-` exist. For example, `-(-5)` -> `5`
-   `true` and `false` are used for booleans


## Planned Improvements

-   **More Data Types:** Add support for strings, lists, and functions.
-   **Conditional Logic:** Implement `if/else` statements.

