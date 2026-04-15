# Poké-Card CLI Generator

This project is an advanced implementation developed during **Week 4 (Libraries)** of Harvard's **CS50P**. It serves as a comprehensive capstone for the module, integrating command-line arguments, external APIs, and third-party styling libraries.

## Project Overview
The **Poké-Card Generator** is a CLI tool that fetches real-time data from the [PokéAPI](https://pokeapi.co/) and generates a stylized "info card" in the terminal. It transforms raw JSON data into a visually appealing layout using ASCII art and grammatically correct text formatting.

## Features

- **External API Integration:** Consumes RESTful data using the `requests` library, including robust error handling for network timeouts and 404 status codes.
- **Nested JSON Navigation:** Implements complex data mining to extract information from nested dictionaries and lists (e.g., retrieving specific ability names from multiple layers of nesting).
- **The Accumulator Pattern:** Utilizes loops and `.append()` to dynamically build lists of Pokémon skills.
- **Modular Architecture:** The program is divided into specialized "Worker" functions for data fetching, font rendering, and text formatting, orchestrated by a "Manager" (`main`) function.
- **Tuple Unpacking:** Efficiently handles multiple return values from functions to keep the code clean and "Pythonic."

## Libraries Used

| Library | Purpose |
| :--- | :--- |
| `requests` | To communicate with the PokéAPI and retrieve Pokémon data. |
| `pyfiglet` | To convert the Pokémon's name into stylized ASCII Art. |
| `inflect` | To format the list of abilities using the Oxford Comma. |
| `sys` | To handle command-line arguments. |
| `random` | To select a different font style for every search. |

## 📖 How to Use

1. **Install Dependencies:**
   ```bash
   pip install requests pyfiglet inflect
2. **Run the program:**
   ```bash
   python pokemon2.py pokemon name
   
