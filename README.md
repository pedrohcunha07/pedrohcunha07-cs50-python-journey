# pedrohcunha07-cs50-python-journey

## Start of Unit-Testing on CS50P Course with -bank.py

This project contains the implementation of the "Home Federal Savings Bank" problem and its respective unit tests, developed as part of Harvard's CS50's Introduction to Programming with Python.

### File Structure

bank.py: The main program that evaluates a greeting and returns a monetary value.
test_bank.py: A suite of unit tests using pytest to ensure the logic works as expected.

**The program prompts the user for a greeting and outputs a value based on the following rules:**
_$0: If the greeting starts with "hello"._

_$20: If the greeting starts with the letter "h" (but does not start with "hello")._

_$100: For any other greeting._

### Testing

pytest test_bank.py

## The tests cover several edge cases, including:

**Case-insensitivity**: Ensures "HELLO", "Hello", and "hello" are treated equally.

**Partial matches**: Verifies that greetings starting with "H" (like "Howdy") return $20.

**Default case**: Ensures unrelated greetings return the full $100.

### Some details

The program uses _.lower().strip()_ to handle leading/trailing whitespace and case formatting.
The core logic is encapsulated in the value(greeting) function to allow for modular testing as required by the CS50P specifications.
