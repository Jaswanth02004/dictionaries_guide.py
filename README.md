# dictionaries_guide.py
A beginner-friendly Python reference guide covering essential dictionary operations, nested structures, dictionary comprehensions, and set-like key operations.

# 🐍 Python Dictionaries: Operations & Practice

A structured, hands-on Python script demonstrating how to create, modify, iterate through, and manipulate dictionaries[cite: 2]. This is the first installment in a Python learning repository.

## 📌 Topics Covered

The script (`Dictionaries & playing with it - Copy.py`) is organized into 8 commented sections for easy step-by-step execution[cite: 2]:

1. **Creation & Access** – Initializing dictionaries using `{}` and `dict()`, and retrieving values by key[cite: 2].
2. **Updating Values** – Modifying existing key-value pairs in place[cite: 2].
3. **Removing Elements & Iteration** – Removing items using `.pop()` and `.popitem()`, and looping through `.keys()`, `.values()`, and `.items()`[cite: 2].
4. **Nested Dictionaries** – Structuring and accessing multi-level dictionaries[cite: 2].
5. **Adding New Entries** – Dynamically inserting new key-value pairs[cite: 2].
6. **Safe Lookups with `.get()`** – Retrieving values with default fallbacks to avoid `KeyError`[cite: 2].
7. **Dictionary Comprehension** – Transforming dictionary values concisely in a single line[cite: 2].
8. **Set Operations on Keys** – Comparing dictionary keys using difference (`-`), intersection (`&`), symmetric difference (`^`), and union (`|`)[cite: 2].

## 🚀 How to Run

1. Make sure you have **Python 3.x** installed.
2. Clone the repository or download the script.
3. Open the file in your preferred code editor, uncomment the section (`''' ... '''`) you want to test[cite: 2], and run:
   ```bash
   python "Dictionaries & playing with it - Copy.py"

   a = {"a": 1, "b": 2}
b = {"b": 2, "c": 4}

print(a.keys() - b.keys())  # Output: {'a'} (Difference)
print(a.keys() & b.keys())  # Output: {'b'} (Intersection)
print(a.keys() ^ b.keys())  # Output: {'a', 'c'} (Symmetric Difference)
print(a.keys() | b.keys())  # Output: {'a', 'b', 'c'} (Union)
