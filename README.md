# 🚀 Rover Mission Control

## 📌 Overview

This project simulates the navigation of robotic rovers on a rectangular plateau.

Each rover:

* Has a position (`x`, `y`) and a direction (`N`, `E`, `S`, `W`)
* Receives a sequence of commands to move and rotate
* Must stay within the plateau boundaries

---

## 🧠 Features

* Object-Oriented Design (Rover & Plateau classes)
* Clean separation of concerns
* Boundary validation
* Command-driven movement system
* Scalable and easy to extend

---

## 📂 Project Structure

```
mars-rover-simulator/
│
├── main.py          # Entry point of the application
├── rover.py         # Rover logic (movement, rotation)
├── plateau.py       # Plateau boundary validation
├── constants.py     # Direction and movement mappings
└── README.md        # Project documentation
```

---

## ⚙️ Requirements

* Python 3.8 or higher

---

## 🛠️ Setup Instructions (Run Locally)

### 1. Clone the repository

```bash
git clone https://github.com/mr-bott/rover-mission-control
cd rover-mission-control
```

### 2. Run the program

```bash
py main.py
```

---

## 🧪 Sample Input

```
5 5
1 2 N
LMLMLMLMM
3 3 E
MMRMMRMRRM
```
---
## ✅ Expected Output

```
1 3 N
5 1 E
```

---

## 🧩 Input Format

1. First line: Plateau upper-right coordinates
2. For each rover:

   * Line 1: Initial position (`x y direction`)
   * Line 2: Command string (`L`, `R`, `M`)

---

## 🧭 Movement Rules

* `N` → y + 1
* `E` → x + 1
* `S` → y - 1
* `W` → x - 1

---

## 💡 Design Approach

* **Plateau class** handles boundary validation
* **Rover class** handles movement and command execution
* Constants are separated for better maintainability
