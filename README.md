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
