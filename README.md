# Little Professor - Math Practice Simulator

This project is part of Harvard's **CS50's Introduction to Programming with Python (Week 4)**. It simulates an educational math tool that generates addition problems based on a chosen difficulty level, challenging the user to solve 10 consecutive equations.

## Goals
The main objective was to build a robust command-line application that manages complex loops and strictly validates user input without crashing.

## Technical Highlights

- **Nested Loop Logic:** Implemented a main loop for 10 math problems, with an internal sub-loop allowing up to 3 attempts per question.
- **Dynamic Integer Generation:** Developed a custom function to generate random integers based on the number of digits (Level 1, 2, or 3), handling specific constraints like including zero only in Level 1.
- **Defensive Programming:** Used `try/except` blocks to handle non-numeric inputs and `raise ValueError` to enforce function contracts.
- **Modular Architecture:** Structured the program into distinct functions (`main`, `get_level`, and `generate_integer`) to ensure code reusability and clean execution.

## How it Works
1. The program asks for a difficulty level (1, 2, or 3).
2. It generates 10 addition problems (e.g., `X + Y = ?`).
3. The user has 3 chances to answer correctly.
4. If the user fails 3 times, the correct answer is displayed.
5. Finally, the program outputs the total score out of 10.
## Key Technical Concepts

### 🔹 Third-Party Libraries & Connectivity
Leveraged the `requests` library to break the "localhost" barrier, allowing the software to communicate with global servers via HTTP requests.

### 🔹 Command-Line Interface (CLI)
Implementation of `sys.argv` to create professional-grade scripts. This approach removes the need for interactive prompts, making the tools scriptable and automatable.

### 🔹 Resilience & Error Handling (EAFP)
Following the "Easier to Ask for Forgiveness than Permission" philosophy, the code is guarded against:
- **Network Failures:** `HTTPError`, `ConnectionError`, and `Timeout`.
- **User Input Errors:** Using `ValueError` to catch non-numeric entries.
- **API Exceptions:** Handling missing endpoints or invalid data keys.

## How to Run
```bash
python professor.py
