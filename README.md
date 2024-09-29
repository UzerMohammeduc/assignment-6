
### README for Assignment 6

This repository contains the implementations for **Assignment 6 Part 1** and **Part 2**, focusing on selection algorithms (median selection) and elementary data structures (arrays, stacks, queues, linked lists, and rooted trees). Below are the instructions for running the code and a summary of findings from both parts.

---

### Part 1: Selection Algorithms

In **Part 1**, two selection algorithms are implemented:
1. **Deterministic Median of Medians Algorithm** - A deterministic algorithm that guarantees worst-case linear time for selecting the \(k^{th}\) smallest element.
2. **Randomized Quickselect Algorithm** - A randomized algorithm that provides expected linear time for selection, but may degrade to \(O(n^2)\) in the worst case.

#### Files:
- **Assignment 6 Part 1.py** contains both algorithm implementations along with a benchmarking function to compare their performance on random, sorted, and reverse-sorted arrays.

#### How to Run:
1. Ensure you have Python 3 installed.
2. Clone this repository.
3. Open a terminal and navigate to the directory where the `Assignment 6 Part 1.py` file is located.
4. Run the following command:
   ```bash
   python Assignment 6 Part 1.py
   ```

#### Summary of Findings:
- The **Randomized Quickselect** algorithm performs very well on average, particularly with random arrays, but has the risk of poor performance in worst-case scenarios.
- The **Deterministic Median of Medians** algorithm is slower on average due to its complexity but offers guaranteed worst-case linear time, making it more reliable when worst-case performance is critical.

The benchmarking function compares both algorithms on arrays with different types of distributions (random, sorted, and reverse-sorted). The results indicate that Quickselect is typically faster in most average cases but less predictable than the deterministic method.

---

### Part 2: Elementary Data Structures

In **Part 2**, various elementary data structures are implemented, including:
1. **Arrays** – Basic operations for an array, including insertion, deletion, and access.
2. **Matrices** – A 2D array implementation for handling matrices, allowing element insertion and access by row and column.
3. **Stacks** – A Last-In-First-Out (LIFO) structure with `push`, `pop`, and `peek` operations.
4. **Queues** – A First-In-First-Out (FIFO) structure with `enqueue` and `dequeue` operations.
5. **Singly Linked Lists** – Dynamic data structures with insertion, deletion, and traversal capabilities.
6. **Rooted Trees** – Hierarchical data structures that represent nodes and their child relationships, with a recursive display function.

#### Files:
- **Assignment 6 Part 2.py** contains all the data structure implementations.

#### How to Run:
1. Ensure you have Python 3 installed.
2. Clone this repository.
3. Open a terminal and navigate to the directory where the `Assignment 6 Part 2.py` file is located.
4. Run the following command:
   ```bash
   python Assignment 6 Part 2.py
   ```

#### Summary of Findings:
- **Arrays** provide fast access (O(1)) to elements but are inefficient for insertion and deletion in the middle (O(n)).
- **Matrices** are an extension of arrays for two-dimensional data and are useful in various fields like machine learning and linear algebra.
- **Stacks** and **Queues** are efficient for their respective LIFO and FIFO operations, commonly used in algorithms like depth-first search (DFS) and breadth-first search (BFS).
- **Linked Lists** allow dynamic memory management with efficient insertions and deletions but suffer from O(n) access time.
- **Rooted Trees** are crucial for representing hierarchical data structures, such as file systems and decision trees, and support recursive traversal and insertion.

Each data structure has its strengths and is suited for specific applications, such as fast access (arrays), dynamic resizing (linked lists), and hierarchical relationships (trees).

---

### How to Use:
You can use the provided implementations as a reference for understanding basic data structures and selection algorithms. The code is modular, allowing you to test, modify, or extend these structures for further learning or integration into larger projects.

Make sure to follow the execution steps for each part to observe the functionality and performance of these data structures and algorithms.

---

### Contributions:
Feel free to fork this repository, add new features, or improve the performance of the algorithms and data structures.
