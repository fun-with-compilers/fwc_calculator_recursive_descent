# Fun With Compilers

## Calculator with recursive descent parser

In this chapter, we will implement a simple calculator in Python by 
constructing a [recursive descent parser](https://en.wikipedia.org/wiki/Recursive_descent_parser).

The language definition is very simple in [EBNF](https://en.wikipedia.org/wiki/Extended_Backus%E2%80%93Naur_form):
```
        expression = [ "+"|"-"] term { ("+"|"-") term};
        term = factor {("*"|"/") factor};
        factor = number | "(" expression ")";
        number = ['-'] digit { digit };
        digit = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9";
```
### Rules
- We support two additive (plus and minus) and two multiplicative (asterisk and slash) operators
- Operator precedence is implicitly defined by the language rules
- Operands are natural numbers with optional negative sign as prefix
- Parentheses are supported

## Sections

### m00_common

Utility libraries to be used by:

- m01_calculator interpreter
- m02_calculator_code_gen

#### Contents

- *parser* 
  - **SourceHandler**: Interface to read source code. Current implementation works on strings
  - **parser_utils**: Helper functions to the AbstractParser class and its derivatives
  - **AbstractParser**: The base class for our parsers, contains utility functions to *get next token/character*, *skip whitespace*, *check next token/character*
- **CalculatorTestBase**: defines test cases for calculators, so we won't copy&paste code into for our different calculator implementations


### m01_calculator_interpreter

A calculator implementation that interprets the expression while parsing. No interfaces, code generation in the middle.

### m02_calculator_code_gen

A calculator implementation that uses a code generator interface. The code generator uses a simple pseudo assembly language with a few stack operations: push, pop, add, sub, mul, div. We have two implementations: one that executes the instructions immediately (thus acting similarly to the interpreter version in the previous example) and another that stores the instructions for later execution.