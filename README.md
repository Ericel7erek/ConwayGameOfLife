# Conway's Game of Life 🎮

Welcome to **Conway's Game of Life** – a classic cellular automaton brought to life in both **Pygame** and **Three.js**! This project demonstrates two different visual implementations of the Game of Life:
- **2D version in Python using Pygame**
- **3D version in JavaScript using Three.js**

Each version brings Conway's famous rules into interactive, animated form. Explore and play with the code to see how simple rules can create complex, beautiful patterns over time.

---

## Table of Contents 📜

- [About the Game of Life](#about-the-game-of-life)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
    - [Running the Pygame Version](#running-the-pygame-version)
    - [Running the Three.js Version](#running-the-threejs-version)
- [How It Works](#how-it-works)

---
<a name="about-the-game-of-life"></a>
## About the Game of Life 🌱

The **Game of Life**, devised by the mathematician **John Conway**, is a zero-player game where cells on a grid evolve through generations based on a set of rules:
1. Any live cell with two or three live neighbors survives.
2. Any dead cell with exactly three live neighbors becomes a live cell.
3. All other live cells die in the next generation, and all other dead cells stay dead.

Through these simple rules, the Game of Life simulates the behavior of cellular life, creating endless patterns, oscillations, and even "gliders" that seem to move across the grid!

---
<a name="project-structure"></a>
## Project Structure 🗂
conways-game-of-life/<br>
├── README.md # Specific instructions for Pygame 
# 2D Python implementation using Pygame 
├── game_of_life.py # Main script for Pygame version
# 3D Javascript implementation using Threejs 
├── index.html # Main file for Three.js version 

---
<a name="getting-started"></a>
## Getting Started 🚀

To get started with either version of Conway's Game of Life, follow the steps below.

<a name="running-the-pygame-version"></a>
### Running the Pygame Version 🐍

1. **Install Python**: Make sure Python is installed on your machine. You can download it from [python.org](https://www.python.org/).

2. **Install Pygame**: Use pip to install Pygame:
   ```bash
   pip install pygame
   ```
   or
   ```bash
   pip3 install pygame
   ```
<a name="running-the-threejs-version"></a>
### Running the Threejs Version 🌐
  Open in Browser:
  <br>
  Simply open the index.html file located in the threejs_version folder with your preferred web browser.
<a name="how-it-works"></a>
### How It Works ⚙️
# Pygame Version
**Grid**: Implemented as a 2D array, where each cell is either alive or dead.<br>
**Rules**: Each cell's state is determined based on its neighboring cells, following Conway's Game of Life rules.<br>
**Rendering**: Cells are drawn as colored squares on a Pygame window, with each update representing a new generation.
# Three.js Version
**Grid**: Implemented in a 3D environment, where cells are represented as cubes.<br>
**Rules**: The same rules as the Pygame version, but displayed in a visually appealing 3D space.<br>
**Rendering**: Uses Three.js to render the 3D environment, with each cube's state determining its color and visibility.
