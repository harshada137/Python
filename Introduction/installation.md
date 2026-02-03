# 🧩  VS Code + Python Setup (Windows)

This guide helps you configure VS Code for a smooth, distraction-free Python development experience — from installation to productivity tweaks.

---

## 1️⃣ Install Visual Studio Code

1. Go to 👉 [https://code.visualstudio.com](https://code.visualstudio.com)
2. Download **VS Code for Windows**
3. Run the installer
4. During installation, **check these options**:

   * ✅ Add to PATH
   * ✅ Open with Code (right-click)
   * ✅ Register Code as an editor

✔ Finish installation

---

## 2️⃣ Install the Python Extension (Must-Have)

1. Open **VS Code**
2. Press **Ctrl + Shift + X** (Extensions)
3. Search: **Python**
4. Install **Python (by Microsoft)**

This extension gives:

* Syntax highlighting
* IntelliSense
* Linting
* Debugging
* Virtual environment support

---

## 3️⃣ Select the Python Interpreter

1. Open VS Code
2. Press **Ctrl + Shift + P**
3. Search:

   ```
   Python: Select Interpreter
   ```
4. Choose:

   * Your installed Python version (recommended)
   * OR a virtual environment (if available)

🟢 The selected interpreter appears in the bottom status bar.

---

## 4️⃣ Create a Python Project (Best Practice)

1. Create a new folder (e.g. `python-basics`)
2. Open it in VS Code
3. Create a file:

   ```
   main.py
   ```
4. Add:

   ```python
   print("VS Code + Python setup successful!")
   ```

---

## 5️⃣ Setup Virtual Environment (Highly Recommended)

Virtual environments keep your projects clean and dependency-safe.

### Create venv

Open VS Code terminal (**Ctrl + `**):

```
python -m venv venv
```

### Activate venv

```
venv\Scripts\activate
```

You should see `(venv)` in terminal.

### Select venv in VS Code

* Press **Ctrl + Shift + P**
* `Python: Select Interpreter`
* Choose the `venv` interpreter

---

## 6️⃣ Enable Auto Formatting (Clean Code)

### Install Formatter

Formatter usually included, but ensure:

* Extension: **Python (Microsoft)**

### Set Formatter

1. Press **Ctrl + Shift + P**
2. Search:

   ```
   Format Document
   ```

(Optional advanced formatter: `black`)

```
pip install black
```

---

## 7️⃣ Run Python Code in VS Code

### Option 1: Run Button

* Click ▶️ at top-right of editor

### Option 2: Terminal

```
python main.py
```

---

## 8️⃣ Debugging Setup

1. Click **Run & Debug** (Ctrl + Shift + D)
2. Click **Run and Debug**
3. Choose **Python File**

You can now:

* Set breakpoints
* Step through code
* Inspect variables

---

## 9️⃣ Useful VS Code Settings (Optional but Powerful)

Open **Settings (JSON)** and add:

```json
{
  "python.defaultInterpreterPath": "python",
  "editor.formatOnSave": true,
  "python.terminal.activateEnvironment": true
}
```

---

## 🔟 Recommended VS Code Extensions for Python

* ✅ Python (Microsoft)
* 🔍 Pylance (auto-installed)
* 🎨 Material Icon Theme (aesthetic)
* ✨ Error Lens (instant error hints)
* 📁 Path Intellisense

---

## 🎯 Final Result

With this setup, you get:

* Clean project structure
* Fast execution
* Smart suggestions
* Proper debugging
* Professional workflow


Just tell me 🌸
