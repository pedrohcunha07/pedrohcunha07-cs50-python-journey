## 🎥 Project Spotlight: Cinema Ticketing System Evolution

This project demonstrates my technical growth between **Week 2** and **Week 3** of Harvard's **CS50P**. I performed a full **refactoring** of a cinema booking system to make it more robust, scalable, and "Pythonic".

### 🛠️ Key Improvements:
- **From LBYL to EAFP:** Moved from a "Look Before You Leap" approach (manual `if/else` checks) to the **EAFP** philosophy (*Easier to Ask for Forgiveness than Permission*) using `try/except` blocks.
- **Data Structure Optimization:** Replaced static `match-case` logic with **Nested Dictionaries**, allowing the system to handle data dynamically.
- **Robust Exception Handling:** Implemented specific handling for `KeyError` (invalid movies) and `ValueError` (invalid age/quantity inputs) to prevent system crashes.
- **Scalability:** The new architecture allows adding new movies by simply updating the dictionary, without touching the core logic.

### 📂 File Comparison:
- `bilheteria_v1`: Initial logic using Week 1 concepts.
- `bilheteria_v2`: Refactored version using Week 3 professional standards.
