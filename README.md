**GoalPath**

<p align="justify">
GoalPath is a graph-based decision support framework for soccer match analysis and goal-oriented path discovery. It models soccer matches as graphs and applies graph traversal techniques, together with metaheuristic optimization algorithms, to identify promising goal-scoring paths, recommend player substitutions using the DFS algorithm, and support tactical decision-making by revealing potential weaknesses in the opposing team and the strategies they use to create scoring opportunities. Furthermore, these analyses can be extended to identify key players on the opposing team, enabling soccer analysts to develop strategies to neutralize their impact and prevent dangerous situations they may create.<br>
This repository contains the datasets and source code associated with the optimization algorithms, as well as the additional algorithms used to generate the results reported in the paper. The code is freely available under the MIT License, and users are welcome to extend and modify it to suit their specific needs.
</p>

---

**Overview**
<p align="justify">
GoalPath divides a soccer field into multiple subfields, each represented as a node in a graph. The edges of the graph represent ball transitions between these subfields, enabling the analysis of ball movement patterns and attacking strategies. The framework can be applied to:
</p>
- Discover potential goal-scoring paths using metaheuristic optimization algorithms.
- Analyze team performance based on passes exchanged between different field zones.
- Support player substitution decisions by identifying isolated or underutilized players within the graph.
- Assist tactical evaluation through the analysis of previous matches and the identification of key opposing players.
- Support team formation and lineup planning by considering the strengths, weaknesses, and playing patterns demonstrated by the opposing team.

---

## Repository Contents

```text
GoalPath/
│── README.md
│── LICENSE
│── requirements.txt
│── Trader.py
│── WCC.py
│── Wolf.py
│── FireFly.py
│── WOA.py
│── GraphFunctions.py
│── ShowField.py
│── data/
```

---

## Datasets
<p align="justify">
This repository includes datasets derived from 10 real-world soccer matches, with data organized separately for the first and second halves of each match. The first-half datasets were used as the reference data, while the second-half datasets served as the validation set. The match data are represented using a weighted edge list graph representation. In each text file, every row corresponds to an edge and contains the source node, target node, and the weight of the edge connecting them. In the context of GoalPath, nodes represent field subregions, while edge weights indicate the frequency of ball transitions between those subregions.
</p>

**Dataset Summary**

| League Name | Target Team | Opponent Team | Match Date | Passes by Target Team (First Half) | Passes by Target Team (Second Half) | Final Score |
|------------|------------|---------------|------------|------------------------------------|-------------------------------------|-------------|
| Bundesliga | Bayern | Freiburg | 22.11.2025 | 408 | 401 | 6–2 |
| English Premier League | Chelsea | Liverpool | 05.10.2025 | 257 | 277 | 1–0 |
| Turkish Süper Lig | Galatasaray | Beşiktaş | 04.10.2025 | 294 | 169 | 1–1 |
| Spain La Liga | Real Madrid | Barcelona | 26.10.2025 | 258 | 197 | 2–1 |
| Iran Premier League | Tractor | Persepolis | 30.10.2025 | 271 | 327 | 1–1 |
| Italian Serie A | Inter Milan | Juventus | 14.02.2026 | 301 | 456 | 3–2 |
| Major League Soccer | Inter Miami | New England | 05.10.2025 | 380 | 285 | 4–1 |
| UEFA Champions League | PSG | Tottenham | 20.09.2025 | 350 | 272 | 5–3 |
| Saudi Pro League | Al Nassr | Al Riyadh | 28.05.2025 | 284 | 292 | 5–1 |
| Campeonato Brasileiro Série A | Palmeiras | Sporting Cristal | 30.10.2025 | 252 | 221 | 3–2 |



Dataset abbreviations

BF: Bayern Munich vs Freiburg
CL: Chelsea vs Liverpool
GB: Galatasaray vs Beşiktaş
RB: Real Madrid vs Barcelona
TP: Tractor vs Persepolis
IJ: Inter vs Juventus
IN: Inter Miami vs New England
PT: Paris Saint-Germain (PSG) vs Tottenham
NR: Al Nassr vs Al Riyadh
SP: Sporting Cristal vs Palmeiras

---

## Implemented Optimization Algorithms
<p align="justify">
GoalPath incorporates five well-known optimization algorithms. These algorithms were selected because previous studies have demonstrated their effectiveness in terms of convergence speed, solution quality, and stability. Furthermore, the algorithms employ different search operators and exploration strategies, which can lead to the discovery of diverse goal-scoring paths and provide soccer analysts and coaches with a broader range of tactical recommendations.
</p>
The implemented algorithms are described below:
<p align="justify">
  
**Trader (TR)**: This algorithm is inspired by trader behavior in financial markets. The file Trader.py contains a ready-to-run implementation of the algorithm.
</p>
<p align="justify">
  
**WCC (World Competitive Contests)**: This algorithm is inspired by competitive contests and sporting competitions. The file WCC.py contains a ready-to-run implementation of the algorithm.
</p>
<p align="justify">
  
**Firefly Algorithm (FF)**: This algorithm is inspired by the flashing behavior and attraction mechanism of fireflies. The file FireFly.py contains a ready-to-run implementation of the algorithm.
</p>
<p align="justify">
  
**Whale Optimization Algorithm (WOA)**: This algorithm is inspired by the social behavior and hunting strategies of whales. The file WOA.py contains a ready-to-run implementation of the algorithm.
<p align="justify">
  
**Grey Wolf Optimization Algorithm (Wolf)**: This algorithm is inspired by the leadership hierarchy and hunting behavior of grey wolves. The file Wolf.py contains a ready-to-run implementation of the algorithm.
</p>

### Running the Algorithms

The source code can be executed on different operating systems with minimal configuration. Before running an algorithm, follow these steps:

Ensure that the input data are provided in the weighted edge list format, as illustrated in the dataset folder.
Set the FP variable to the path of the match graph (dataset) you wish to analyze.
Configure the rn variable, which specifies the number of independent executions. To run an algorithm only once, set the corresponding range to (1, 2).
Create an empty RST folder, as the algorithms store their output files in this directory.

### Output

After running an algorithm, the results will be automatically generated in the RST folder. A separate output file is created for each algorithm, dataset, and execution run.

The generated files contain the best goal-scoring path identified during the optimization process, which can subsequently be analyzed by soccer analysts, coaches, and researchers for tactical evaluation and decision support. By running each algorithm, a convergence diagram is also generated.


</p>

---
## Installation

Clone the repository:

```bash
git clone https://github.com/MasoudiYosef/GoalPath.git
cd GoalPath
```
---

## Library requirements

The implemented algorithms require a minimal number of library dependencies, as all code has been developed in a library-free manner as much as possible. To run the algorithms, only the numpy and matplotlib libraries are required. These are used for numerical computations and matrix operations, and for visualizing the results, respectively.

To install these libraries, users can run the following commands in the command prompt:

- **pip install numpy**
  
- **pip install matplotlib**
  
---


## Usage

Run any of the optimization algorithms individually:

```bash
python Trader.py
python WCC.py
python Wolf.py
python FireFly.py
python WOA.py
```

You may modify the input datasets and algorithm parameters depending on the target match and experimental setting.

---

## Graph Analysis Functions (GrahFunctions.py)

This python-format file contains a set of graph-related utility functions used in the GoalPath framework. The functions support graph construction, traversal, strongly connected component detection (SCC), subgraph filtering, and combinatorial node analysis.

These utilities are designed to work with weighted directed graphs derived from soccer match data.

---

### Features

- Depth-First Search (DFS) traversal
- Strongly Connected Components (SCC) detection
- Graph reading and construction from datasets
- Graph transposition
- Subgraph filtering
- Generation of node subsets (combinatorial analysis)

---

### Functions

#### DFS Traversal

##### `DFS(node, V, F, G, n, T, ST)`
Performs depth-first search on a graph.

Purpose:
- Visits all reachable nodes
- Computes discovery and finishing times
- Stores nodes in finishing order (stack)

---

##### `DFS2(node, V, G, n, GR)`
Performs DFS on the transposed graph.

Purpose:
- Assigns component labels to nodes
- Used in SCC detection

---

##### `DFS3(node, V, F, G, n, T, Flag)`
Alternative DFS with condition tracking.

Purpose:
- Tracks traversal conditions
- Used for specialized analysis

---

#### Graph Analysis

##### `SCC(G)`
Computes Strongly Connected Components of a directed graph.

Method:
- DFS to compute finishing order
- Graph transposition
- DFS on transposed graph

Output:
- Component labels for each node

---

#### Graph Construction

##### `ReadGraph(FN)`
Reads adjacency matrix from a file.

Input:
- CSV-like matrix file

Output:
- NumPy adjacency matrix

---

##### `GetGraph(FP)`
Constructs a weighted adjacency matrix from an edge-list dataset.

Output:
- 51 × 51 weighted graph matrix

---

### Graph Manipulation

##### `FilterGraph(G, Nodes, n)`
Creates a subgraph by removing nodes not in the given list.

---

##### `Transpose(G)`
Returns the transpose of a graph (reverses edge directions).

---

### Combinatorial Analysis

##### `AllPossible(Nodes, V, index, LS)`
Generates all possible subsets of a node set.

Purpose:
- Enumerates combinations of nodes for analysis

---

## Soccer Field Division into Subfields (ShowField.py)

This module generates a visual representation of a soccer field and divides it into 50 equal subfields. Each subfield can be used as a node in a graph-based representation for soccer analytics tasks such as tracking ball movement, transition modeling, and tactical analysis in the GoalPath framework.

---

### Overview

The soccer field is modeled as a rectangle of size:

- Width: 80 units  
- Height: 50 units  

The field is divided into a 10 × 5 grid, resulting in 50 subfields. Each subfield is assigned a unique identifier (1 to 50), which can later be used as graph nodes.

---

### Features

- Draws a full soccer field layout
- Includes center circle and penalty areas
- Divides the field into 50 equal rectangular zones
- Labels each subfield with a unique ID
- Saves both:
  - Full field image (`Field.jpg`)
  - Divided field image (`DividedField.jpg`)

---

### Field Construction

The field includes the following components:

- Outer boundary rectangle
- Center circle
- Penalty areas (left and right)
- Halfway line
- Grid overlay for subfield division

---

### Subfield Division

- The field is divided into:
  - 10 vertical segments
  - 5 horizontal segments
- Each cell represents one subfield
- Subfields are numbered sequentially from left to right, bottom to top

---

## Authors

- **Yosef Masoudi-Sobhanzadeh**
- **Sercan Saglam**
- **Ali Kazemi Niari**

---

## License

This project is licensed under the **MIT License** - see the `LICENSE` file for details.
