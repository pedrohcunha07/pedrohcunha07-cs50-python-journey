# Real-Time Data Integration & CLI Tools (CS50P - Week 4)

This repository contains projects developed during **Harvard's CS50P Week 4**, focusing on the power of **Libraries** and **API Integration**. 

## Projects Overview

### 1. Currency Converter (USD to BRL)
A CLI tool that fetches real-time exchange rates from the **AwesomeAPI**.
- **Input:** Amount in USD via Command-Line Arguments.
- **Output:** Current value in BRL formatted to two decimal places.

### 2. Pokémon Skill Finder
Interacts with the **PokeAPI** to retrieve and list a specific Pokémon's abilities.
- **Complexity:** Handles deeply nested JSON structures and dynamic URL parameters.

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

- pip install requests
- python converter.py 100
