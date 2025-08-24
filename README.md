# Simple Readable Mathematical Language Interpreter

This is a fully featured interpreter for a readable simple mathematical language, built from scratch in Python. This project showcases the implementation of tokenization, parsing, evaluation, and the core principles of how programming languages work.

## Features

-   **Arithmetic Operations:** Supports addition (`+`), subtraction (`-`), multiplication (`*`), division (`/`), and exponentiation (`^`).
-   **Correct Operator Precedence:** Follows standard PEMDAS rules.
-   **Correct Associativity:** Handles left-associative operators (`+`, `-`, `*`, `/`) and right-associative operators (`^`) correctly.
-   **Parentheses:** Supports nested parentheses for grouping expressions.
-   **Unary Operators:** Correctly parses and evaluates unary negation.
-   **Variables:** Allows for variable assignment and usage throughout a session.
    ```
    define x = 10
    define y = x * 2
    y + 5  // Result: 25
    ```

## Core Project Structure

-   `Interpreter.py`: Interpreter
-   `Parser.py`: Contains the tokenizer, turns input into AST(Abstract Syntax Tree)
-   `AST.py`: Defines the class structure for the nodes of the Abstract Syntax Tree (e.g., `NumberNode`, `OperatorNode`, `AssignmentNode`). Also includes evaluation methods for each type of Node.
-   `Evaluator.py`: A simple wrapper that kicks off the evaluation process on the root node of the AST.


## How to Run

The simplest way to see the interpreter in action is to run the test suite.

```bash
git clone 
cd interpreter
python Tester.py
```

## How It Works

### 1. Parsing

Parser -> Abstract Syntax Tree

-   **Tokenizer:** The input string is first broken down into a list of tokens (e.g., `"5 + 3 * 2"` -> `['5', '+', '3', '*', '2']`).
-   **Recursive Descent Parser:** The parser uses a series of hierarchical functions (`parse_low`, `parse_med`, `parse_high`) to build the AST. Each function is responsible for a specific level of operator precedence:
    -   `parse_low` handles `+` and `-`.
    -   `parse_med` handles `*` and `/`.
    -   `parse_high` handles `^`.
    This hierarchy enforces the order of operations. For example, in 5 + 3 * 2, parse_low would first be called, which would call parse_med on the right of the `+`. parse_med would return an operator node containing `3, 2, and *`, which would represent that multiplication. Then, the original `+` would be evaluated, resulting in an AST following PEMDAS.

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

## Planned Improvements

-   **Interactive REPL:** Create a true Read-Eval-Print Loop so the interpreter can be used interactively from the command line.
-   **More Data Types:** Add support for Booleans, strings, and lists.
-   **Conditional Logic:** Implement `if/else` statements.
