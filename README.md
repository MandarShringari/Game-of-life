# Conway's Game of Life (Pygame)

An interactive implementation of Conway's Game of Life built using Python and Pygame.

## Features

- **Interactive Grid:** Click on any cell in the grid to toggle its state (alive or dead).
- **Start / Pause Simulation:** Toggle the simulation on and off anytime using the Spacebar.
- **Clear Grid:** Reset the entire grid instantly.
- **Custom Generation Logic:** Uses classic Conway's Game of Life rules to calculate cell generations dynamically.

## Game Controls

| Action | Control |
| :--- | :--- |
| **Toggle Cell State** | Left Click on a grid block |
| **Start / Pause Simulation** | `Spacebar` |
| **Clear Grid / Reset** | `Delete` key |

## Setup & Running

### Prerequisites

You need Python 3 and Pygame installed on your machine.

1. **Install Pygame:**
   ```bash
   pip install pygame
python main.py

---
## Rules of Conway's Game of Life
	1.	Underpopulation: Any live cell with fewer than two live neighbors dies.
	2.	Survival: Any live cell with two or three live neighbors lives on to the next generation.
	3.	Overpopulation: Any live cell with more than three live neighbors dies.
	4.	Reproduction: Any dead cell with exactly three live neighbors becomes a live cell.

