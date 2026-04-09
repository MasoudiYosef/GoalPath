# GoalPath

**GoalPath** is a graph-based decision support framework for soccer match analysis and goal-oriented path discovery.  
It models soccer matches as graphs and applies graph traversal techniques together with metaheuristic optimization algorithms to identify promising goal-scoring paths, recommend player substitutions, and support tactical decision-making.

This repository contains the **datasets**, **source code**, and **optimization algorithms** used in the GoalPath framework.

---

## Overview

GoalPath is designed to support soccer analytics by transforming match events and player interactions into graph structures.  
The framework can be applied to:

- Discover potential **goal-scoring paths**
- Analyze **team performance**
- Support **player substitution decisions**
- Assist in **tactical evaluation**
- Evaluate different optimization strategies for graph-based path discovery

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
│── data/

---

## Datasets

This repository includes datasets derived from **five real-world soccer matches**, with data organized separately for the **first half** and **second half** of each match.

The **first-half datasets** were used as the **reference data**, while the **second-half datasets** were used as the **validation set**.

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

Install the required dependencies:

```bash
pip install -r requirements.txt
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
