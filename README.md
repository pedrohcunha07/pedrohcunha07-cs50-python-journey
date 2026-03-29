
# 🎓 CS50P - Python Journey (HarvardX)

This repository tracks my progress through Harvard's **CS50's Introduction to Programming with Python**, focusing on professional standards, robust logic, and systems analysis.

---

## 🚀 Project Spotlight: Intergalactic Parking System (Week 3 Final)

This project was my "Final Boss" for **Week 3 (Exceptions & Dictionaries)**. I designed it to move beyond basic exercises and force myself to handle complex logic, nested data structures, and the **EAFP** philosophy independently.

### 🛠️ Technical Highlights:
- **Philosophy (EAFP):** Implemented robust `try/except` blocks to handle `KeyError` (invalid ship models/names) and `ValueError` (invalid time/menu inputs), ensuring the system never crashes due to "dirty" user input.
- **Data Architecture:** Utilized **Nested Dictionaries** to map unique ship names to specific models and cross-reference them with a static pricing catalog. This allows for high **Scalability**—adding new models requires zero changes to the core logic.
- **Atomic State Management:** Used the `.pop()` method to safely remove ships from the yard while simultaneously retrieving their model data for billing, ensuring **Data Integrity**.
- **Logic Safeguards:** Implemented validation to prevent negative billing and handle "non-existent" ships gracefully.

### 🔹 The "Design 3D" Connection: Logic Retopology
As a 3D Designer (Blender), I see code logic as **Mesh Topology**. An infinite loop or an unhandled exception is like a *non-manifold* geometry—it crashes the "render" (execution). 
Refactoring this system was like performing a **Retopology**: removing redundant `if/else` "polygons" and replacing them with a clean, efficient `try/except` flow.

---

## 📁 Week 3 - Module Overview (Exceptions)

This module focused on writing resilient code that can handle unexpected user behavior without crashing.

### 📝 Technical Documentation:
- **`estacionamento.py`**: A complete management system featuring modular functions (`main`, `estacionar`, `liberar`, `exibir_patio`) and advanced error handling.
- **`fuel.py`**: Handles input validation for fractions, catching `ZeroDivisionError` and `ValueError`.
- **`taqueria.py`**: Manages a restaurant menu using dictionary lookups and handling `EOFError` for clean exits.

---

## 🏁 How to Run
1. Ensure you have **Python 3.x** installed.
2. Clone this repository: `git clone https://github.com/pedrohcunha07/pedrohcunha07-cs50-python-journey.git`
3. Navigate to the desired script and run: `python script_name.py`

## 🚀 Project Spotlight: Intergalactic Parking Management System

This project was my "Final Boss" for **CS50P Week 3**. It was designed to move beyond basic exercises and force me to handle complex logic, nested data structures, and the **EAFP** philosophy independently.

### 🛠️ Technical Highlights:
- **EAFP Philosophy:** Implemented robust `try/except` blocks to handle `KeyError` (invalid ship models/names) and `ValueError` (invalid time/menu inputs), ensuring the system never crashes due to "dirty" user input.
- **Data Architecture:** Utilized **Nested Dictionaries** to map unique ship names to specific models and cross-reference them with a static pricing catalog.
- **Atomic State Management:** Used the `.pop()` method to safely remove ships from the yard while simultaneously retrieving their model data for billing—ensuring data integrity.
- **Revenue Protection:** Implemented logic to prevent negative billing and handle "non-existent" ships gracefully.

### 🔹 The "Design 3D" Analogy: Clean Topology
As a 3D Designer (Blender), I see code logic as **Mesh Topology**. An infinite loop or an unhandled exception is like a *non-manifold* geometry or a broken subdivision—it crashes the "render" (execution). 
Refactoring this system was like performing a **Retopology**: removing redundant `if/else` "polygons" and replacing them with a clean, efficient `try/except` flow.

### 📂 Files:
- `estacionamento.py`: The full Intergalactic Parking System implementation.
- `fuel.py` & `taqueria.py`: Official Harvard Problem Sets for Week 3.

