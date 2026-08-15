# Python Turtle Crossing Game

A Frogger-style Turtle Crossing game built with Python using the built-in `turtle` graphics library. The project uses object-oriented programming to separate the player, traffic, scoreboard, and main game logic into individual modules.

## Features

* Player-controlled turtle movement
* Randomly spawning cars
* Multiple car colors
* Collision detection
* Level tracking
* Automatic player reset after completing a level
* Increasing traffic speed as levels progress
* Game-over detection
* Modular object-oriented design

## Controls

Use the arrow keys to control the turtle:

* **↑ Up Arrow** — Move forward
* **↓ Down Arrow** — Move backward

The goal is to safely reach the top of the screen without colliding with a car.

## Project Structure

```text
Python-Turtle-Crossing/
│
├── main.py
├── player.py
├── car_manager.py
├── scoreboard.py
├── .gitignore
└── README.md
```

### `main.py`

Runs the main game loop, listens for keyboard input, handles car movement, checks for collisions, detects level completion, and increases game speed as the player progresses.

### `player.py`

Contains the `Player` class responsible for:

* Creating the player turtle
* Positioning the player at the starting point
* Moving forward and backward
* Resetting the player after completing a level

### `car_manager.py`

Contains the `CarManager` class responsible for:

* Randomly creating cars
* Assigning random car colors
* Positioning cars across the screen
* Moving traffic across the game area
* Managing multiple car objects

### `scoreboard.py`

Contains the `Scoreboard` class responsible for:

* Tracking the current level
* Updating the displayed level
* Displaying a game-over message after a collision

## How to Run

1. Make sure Python is installed on your computer.

2. Clone this repository:

```bash
git clone YOUR_REPOSITORY_URL
```

3. Navigate into the project folder:

```bash
cd Python-Turtle-Crossing
```

4. Run the game:

```bash
python main.py
```

No external packages are required because the project uses Python's built-in `turtle` module.

## What I Practiced

This project helped me practice:

* Python object-oriented programming
* Classes and inheritance
* Working with multiple Python modules
* Keyboard event handling
* Random object generation
* Collision detection
* Coordinate-based movement
* Game loops
* Level progression
* Managing multiple game objects
* Increasing game difficulty dynamically

## Built With

* Python
* Python Turtle Graphics
