# CSP-MapColoring-Problem-Solver

This is a **Python** implementation of the **Map Coloring** Problem using Constraint Satisfaction Problem (CSP) techniques. The program lets users choose between the USA and Australia maps and solve them using different combinations of search methods and heuristics. It ensures that no neighboring states share the same color, using as few colors as possible.

## Group Members 
- Parth Patel
- Sai Priyanka Taduri

## Features

- Lets you solve map coloring using:
  - Depth-first search only
  - Depth-first search + forward checking
  - Depth-first search + forward checking + singleton propagation
- Option to use heuristics for smarter choices:
  - MRV (Minimum Remaining Values)
  - LCV (Least Constraining Value)
- Displays output in a clean, easy-to-read format:
  - Lists each color used with states assigned to it
  - Shows minimum number of colors needed
  - Shows number of backtracks 
  - Shows the time required to compute (in milliseconds)

---

## Getting Started

### Prerequisites

Ensure you have **Python 3.x** installed. You can check your current version by running:

```bash
python3 --version
```
## Installation & Running the Program

### Clone the Repository:

```bash
git clone https://github.com/parth448812/CSP-MapColoring-Problem-Solver.git
cd CSP-MapColoring-Problem-Solver
```
### Run the Solver:

```bash
python3 map_coloring_solver.py
```

### Provide Input:

- Select a map:
  - Enter `1` for **USA**.
  - Enter `2` for **Australia**.
- Choose whether or not to use heuristics:
  - Enter `1` for **Without Heuristics**.
  - Enter `2` for **With Heuristics**.
- Choose a method:
  - Enter `1` for **Depth-first search only**.
  - Enter `2` for **Depth-first search + forward checking**.
  - Enter `3` for **Depth-first search + forward checking + singleton propagation**.

### View the Output:

- The program will return the **list of colors used and their assigned states**. 
- It will also print:
  - **Minimum Colors Required**.
  - **Number of Backtracks**.
  - **Time Required to Compute**.

### Example Run

#### Input:

```bash
Select a map:
1. USA
2. Australia

Enter Choice (1-2): 1

Use heuristics?
1. Without Heuristics
2. With Heuristics

Enter Choice (1-2): 2

Select Method:
1. Depth-first search only
2. Depth-first search + forward checking
3. Depth-first search + forward checking + singleton propagation

Enter Choice (1-3): 3
```
#### Output:

```bash
----------------------------------------------------
Map Coloring Solution (Minimum Colors Required: 4):
----------------------------------------------------

Blue:
  Alabama
  Arkansas
  Connecticut
  Iowa
  Kansas
  Kentucky
  Michigan
  Nevada
  New Mexico
  North Carolina
  North Dakota
  Pennsylvania
  Vermont
  Washington
  Wyoming

Red:
  Alaska
  California
  Colorado
  Delaware
  Georgia
  Hawaii
  Idaho
  Mississippi
  Missouri
  New Hampshire
  New York
  Ohio
  South Dakota
  Texas
  Virginia
  Wisconsin

Yellow:
  Arizona
  Indiana
  Maryland
  Rhode Island

Green:
  Florida
  Illinois
  Louisiana
  Maine
  Massachusetts
  Minnesota
  Montana
  Nebraska
  New Jersey
  Oklahoma
  Oregon
  South Carolina
  Tennessee
  Utah
  West Virginia

Number of Backtracks: 0
Time Required to Compute: 460.73 ms
