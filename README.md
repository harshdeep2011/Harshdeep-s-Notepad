# 📝 Harshdeep's Enhanced Notepad

A modern multi-tab desktop application built using **Python 3.13 and PyQt5**.  
This project demonstrates real-world GUI development, file handling, dark theme styling, and executable packaging.

---

## 📸 Application Preview

![App Preview](assets/app-preview.png)

---

## 🚀 About The Project

Harshdeep's Enhanced Notepad is not just a basic text editor.  
It is a structured desktop application featuring:

- 📝 Text Editor with Open & Save functionality  
- 📊 Progress Simulation System  
- 🎛 Interactive Slider Controls  
- 🎨 Custom Dark Theme using QSS  
- 🛠 Toolbar, Menu Bar & Status Bar  
- 🗂 Multi-Tab Interface Design  

This project was created to understand how professional Windows desktop applications are built and converted into standalone software.

---

## 🛠 Technologies Used

- Python 3.13  
- PyQt5 (GUI Framework)  
- VS Code  
- Windows 11  
- PyInstaller  

---

# ▶️ How To Run This Project (Beginner Guide)

## STEP 1 — Install Python

1. Visit: https://www.python.org/downloads/
2. Download Python 3.13
3. During installation, check:

   ✅ **Add Python to PATH**

4. Complete installation.

---

## STEP 2 — Verify Python & pip

Open Command Prompt (Press `Win + R`, type `cmd`, press Enter)

Check Python:

python --version


Check pip:

pip --version


If pip is missing, run:

python -m ensurepip --upgrade


---

## STEP 3 — Install PyQt5

Inside Command Prompt:

pip install PyQt5


Wait until installation completes successfully.

---

## STEP 4 — Run the Application

Navigate to your project folder:

cd path-to-your-project-folder


Then run:

python "Harshdeep's NotePad Code.py"


The application window will open.

---

# 🏗 How To Build Windows Executable (.exe)

To convert this Python project into a real Windows application:

## Install PyInstaller

pip install pyinstaller


## Build Command

pyinstaller --onefile --windowed --icon="harhdep notepad icon.ico" "Harshdeep's NotePad Code.py"


### What These Flags Mean:

- `--onefile` → Creates a single executable file  
- `--windowed` → Removes black console window  
- `--icon` → Sets custom application icon  

---

## 📦 After Building

These will be created:

- `build/` folder  
- `dist/` folder  
- `.spec` file  

The final `.exe` file will be inside the `dist` folder.

---

# 📂 Project Structure

Harshdeep-Enhanced-Notepad/
│
├── README.md
├── Harshdeep's NotePad Code.py
├── harhdep notepad icon.ico
│
└── assets/
└── app-preview.png


---

# 🧠 Learning Outcomes

Through this project, I gained practical understanding of:

- Object-Oriented GUI design using PyQt5  
- File handling in desktop applications  
- Timer-based progress simulation  
- Custom UI styling with QSS  
- Packaging Python apps into distributable software  

---
# 👨‍💻 Author

**Harshdeep Singh**  
Student Developer | Exploring Desktop Application Development  

---

⭐ If you found this project interesting, consider giving it a star.
