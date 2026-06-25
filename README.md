# 🧪 Chemical Reaction Database

## 📌 Overview
The **Chemical Reaction Database** is a lightweight, terminal-based Python application designed to help users store, search, and manage chemical reaction data. It allows users to quickly look up the main product of a reaction based on specific reactants, reagents, and environmental conditions (concentration and temperature). 

All data is persistently stored in a local JSON file, making it easy to read, backup, and share.

---

## 🚀 Features
* **Check Reactions:** Query the database by entering a reactant, acid/base, concentration, and temperature to find the resulting main product.
* **Add New Reactions:** Easily expand the database by inputting new chemical reactions through the interactive command-line interface.
* **Modify Existing Data:** Update incorrect or outdated reaction data directly from the menu without needing to manually edit the JSON file.
* **Persistent Storage:** All data is securely saved to `reaction_data.json` so no information is lost between sessions.

---

## 📂 Project Structure

| File Name | Description |
| :--- | :--- |
| `Main.py` | The main Python script containing the application logic and interactive CLI menu. |
| `reaction_data.json` | The local database file containing the chemical reaction records in JSON format. |

---

## 🛠️ Installation & Usage

### 1. Prerequisites
You need **Python 3.x** installed on your computer. No external libraries or dependencies (like `pip install`) are required, as the project solely relies on Python's built-in `json` and `os` modules.

### 2. Setup
Ensure both `Main.py` and `reaction_data.json` are placed in the same folder/directory.

### 3. Run the Application
Open your terminal or command prompt, navigate to the folder containing the files, and run:
```bash
python Main.py

==============================
 CHEMICAL REACTION DATABASE 
==============================
1. Check reaction
2. Add reaction
3. Modify or update reaction data
0. Exit app

# 🧪 Chemical Reaction Database

## 📌 Overview
The **Chemical Reaction Database** is an interactive web application built with Python and **Streamlit**. It helps users predict the main product of chemical reactions based on specific reactants, reagents, and environmental conditions (concentration and temperature).

By utilizing a dynamic web interface with dropdown menus, the application eliminates typing errors and instantly searches the local JSON database to provide accurate chemical products.

---

## 🚀 Features
* **Interactive Web Interface:** A clean, modern UI built with Streamlit—no terminal commands required!
* **Dynamic Dropdowns:** The application automatically reads `reaction_data.json` on startup and populates the dropdown menus with the exact available metals, acids/bases, temperatures, and concentrations.
* **Instant Predictions:** Query the database with your selected parameters to instantly find the resulting chemical compound.
* **Error Prevention:** By forcing users to select from available options, the app completely eliminates "Not Found" errors caused by typos or case-sensitivity issues.

---

## 📂 Project Structure

| File Name | Description |
| :--- | :--- |
| `app.py` | The main Python script that runs the Streamlit web application. |
| `reaction_data.json` | The local database file containing the chemical reaction records in JSON format. |

---

## 🛠️ Installation & Usage

### 1. Prerequisites
Ensure you have **Python 3.x** installed on your computer. You will also need to install the Streamlit library.

Open your terminal or command prompt and run:
```bash
pip install streamlit