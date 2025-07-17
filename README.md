# THE CLASSIC CALCULATOR - A GUI based Python Project

### 📌 Overview
This project is based on a simple yet functional GUI-based calculator built using Python's tkinter module. It features a user-friendly interface with support for basic arithmetic operations, square, square root, percentage, and utility functions like clear, backspace, and double zero, designed with an intuitive graphical interface for ease of use.

### 🚀 Features
- **🖱️ Responsive GUI** : Responsive GUI using `tkinter`.
- **➕ Supports basic operations** : Supports basic operations like addition ![+](https://img.shields.io/badge/+-orange) , subtraction ![-](https://img.shields.io/badge/---orange) , multiplication ![*](https://img.shields.io/badge/*-orange)  and division ![/](https://img.shields.io/badge//-orange).
- **🧼 Clear button ![AC](https://img.shields.io/badge/AC-red)** : To reset the input.
- **🧩 Organized layout** : Provides organized layout with buttons and display.
- **⚠️ Error handling** : Error handling in cases like division with 0.

### 🧾 File Descriptions
- `tk.Tk()` : creates the main application window.
- `root.geometry()` : sets the window size.
- `root.title()` : sets the title of the app window.
- `tk.Entry()` : the display area for inputs and results.
- `on_click(symbol)` : Appends a symbol (number/operator) to the entry field.
- `clear()` : Clears the entire input.
- `calculate()` : Evaluates the expression and shows result; handles errors.
- `percent()` : Divides the number by 100.
- `backspace()` : Deletes the last digit/symbol.
- `double_zero()` : Appends 00 to the current input.

### 🔣 Button Functionalities
| Button          | Functionality                           |
| --------------- | --------------------------------------- |
| `0-9`           | Number inputs                           |
| `00`            | Inserts two zeros                       |
| `+ - * /`       | Arithmetic operators                    |
| `.`             | Decimal input                           |
| `=`             | Evaluates the expression using `eval()` |
| `AC`            | Clears the entry field completely       |
| `%`             | Converts input into a percentage        |
| `⌫`             | Removes the last character (backspace)  |

### 🎨 UI Design
- Uses grid layout to arrange buttons.
- Colors:
   - `=` → Blue (primary action)
   - `AC` → Red (reset)
   - `%`→ Green (utility)
   - `⌫` → Dark red (backspace)
   - `00`, digits(`0` to `9`) → Grey
   - Operators `+`,  `-`,  `*`,  `/` → Orange

### 🧰 Design Decisions

- I chose Python's `tkinter` library to create a clean and lightweight GUI without external dependencies.
- The button layout replicates the look and flow of a traditional calculator to enhance usability.
- I included additional functionality like percentage, and backspace to go beyond basic operations.
- Error handling (e.g., division by zero or invalid input) was implemented to improve robustness.
- Button colors were selected to visually distinguish between functions (e.g., red for clear, blue for equals).

### 🔍How to Run
Make sure your python is installed and then run it - 
python calculator.py  
