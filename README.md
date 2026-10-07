# Route Optimization for Newspaper Delivery

## Project Overview
This project focuses on finding an efficient route for newspaper delivery using different search algorithms. The delivery locations are represented as a weighted graph based on the AIUB campus.

Three algorithms are implemented and compared to find an efficient delivery route:
- Hill Climbing
- Simulated Annealing
- Beam Search

## Objective
The main objective of this project is to minimize the delivery route cost and compare the performance of different search algorithms based on their route cost and execution time.

## Algorithms Used 
**Hill Climbing**  
Finds a better route by making small changes to the current solution.

**Simulated Annealing**  
Explores different solutions and can accept worse solutions temporarily to avoid getting stuck in a local optimum.

**Beam Search**  
Keeps a limited number of the most promising routes at each step.

## Results
| Algorithm | Route Cost | Execution Time |
|---|---:|---:|
| Hill Climbing | 90 | 7.874 ms |
| Simulated Annealing | 90 | 26.179 ms |
| Beam Search | 90 | 0.280 ms |

### Reported Best Route
(Main Gate → Sports Gallery → D Building → Annex 8 → Annex 9 → C Building → Annex 5 & 6 → Annex 2, 3 & 4 → Annex 1)
  **Total Route Cost: 90 distance units**

## Technologies Used
- Python
- Graph Algorithms
- Local Search
- Heuristic Search
- Dijkstra's Algorithm

## Research Paper
The complete research paper is included in this repository with the detailed methodology, results, limitations, and future work.

## Future Work
- Test the algorithms on larger datasets
- Add traffic and time constraints
- Support multiple vehicles and depots
- Explore hybrid search algorithms

