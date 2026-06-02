# GoalPath
<p align="justify">
**GoalPath** is a graph-based decision support framework for soccer match analysis and goal-oriented path discovery. It models soccer matches as graphs and applies graph traversal techniques, together with metaheuristic optimization algorithms, to identify promising goal-scoring paths, recommend player substitutions using the DFS algorithm, and support tactical decision-making by revealing potential weaknesses in the opposing team and the strategies they use to create scoring opportunities. Furthermore, these analyses can be extended to identify key players on the opposing team, enabling soccer analysts to develop strategies to neutralize their impact and prevent dangerous situations they may create.<br>
This repository contains the datasets and source code associated with the optimization algorithms, as well as the additional algorithms used to generate the results reported in the paper. The code is freely available under the MIT License, and users are welcome to extend and modify it to suit their specific needs.
</p>

---

## Overview
<p align="justify">
GoalPath divides a soccer field into multiple subfields, each represented as a node in a graph. The edges of the graph represent ball transitions between these subfields, enabling the analysis of ball movement patterns and attacking strategies. The framework can be applied to:

- Discover potential goal-scoring paths using metaheuristic optimization algorithms.
- Analyze team performance based on passes exchanged between different field zones.
- Support player substitution decisions by identifying isolated or underutilized players within the graph.
- Assist tactical evaluation through the analysis of previous matches and the identification of key opposing players.
- Support team formation and lineup planning by considering the strengths, weaknesses, and playing patterns demonstrated by the opposing team.
</p>

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
### Match Summary

| League Name | Target Team | Opponent Team | Match Date | Passes by Target Team (First Half) | Passes by Target Team (Second Half) | Final Score |
|------------|------------|---------------|------------|------------------------------------|-------------------------------------|-------------|
| Bundesliga | Bayern | Freiburg | 22.11.2025 | 408 | 401 | 6–2 |
| English Premier League | Chelsea | Liverpool | 05.10.2025 | 257 | 277 | 1–0 |
| Turkish Süper Lig | Galatasaray | Beşiktaş | 04.10.2025 | 294 | 169 | 1–1 |
| Spain La Liga | Real Madrid | Barcelona | 26.10.2025 | 258 | 197 | 2–1 |
| Iran Premier League | Tractor | Persepolis | 30.10.2025 | 271 | 327 | 1–1 |

---

## Implemented Optimization Algorithms

This repository provides implementations of **five optimization algorithms** used within the GoalPath framework.

### Included Algorithms

- **Trader** – inspired by trader behaviors in financial markets
- **WCC** – inspired by the competitive dynamics of soccer teams
- **Firefly Algorithm**
- **Whale Optimization Algorithm (WOA)**
- **Grey Wolf Optimization Algorithm (GWO)**

### Source Files

- `Trader.py`
- `WCC.py`
- `Wolf.py`
- `FireFly.py`
- `WOA.py`

---

## Methodology

GoalPath models match events and player interactions as a graph structure, where:

- **Nodes** represent subfields
- **Edges** represent ball transitions, passes, or movements
- **Graph traversal** is used to explore strongly connected components
- **Metaheuristic optimization algorithms** are used to identify promising paths and support tactical recommendations

The framework can be used for both:

- **Pre-match analysis**
- **In-game decision support**

---

## Installation

Clone the repository:

```bash
git clone https://github.com/MasoudiYosef/GoalPath.git
cd GoalPath
```
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


## Authors

- **Yosef Masoudi-Sobhanzadeh**
- **Sercan Sağlam**
- **Ali Kazemi Niari**

---

## License

This project is licensed under the **MIT License** - see the `LICENSE` file for details.
