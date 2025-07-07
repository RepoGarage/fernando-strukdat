# Data Structures in Python (Struktur Data)

A comprehensive collection of data structure implementations in Python for educational purposes. This repository contains various data structure implementations ranging from basic stacks and queues to advanced probabilistic data structures and graph algorithms.

## Table of Contents

- [Overview](#overview)
- [Requirements](#requirements)
- [File Structure](#file-structure)
- [Usage Examples](#usage-examples)
- [Running the Code](#running-the-code)
- [Author](#author)

## Overview

This repository serves as a learning resource for understanding fundamental and advanced data structures through Python implementations. Each file demonstrates different concepts and approaches to data structure design, from traditional implementations to creative variations inspired by quantum mechanics.

## Requirements

- **Python 3.10 or higher** (uses modern Python features like union types with `|`)
- No external dependencies required (uses only Python standard library)

## File Structure

### Core Data Structure Implementations

#### **contoh.py**
Comprehensive examples of basic data structures including:
- Arrays (Python lists)
- Linked Lists with append functionality
- Stacks (LIFO implementation)
- Queues (FIFO implementation)
- Placeholder implementations for trees, heaps, tries, sets, and graphs

#### **week2.py**
Basic Stack implementation with:
- Fixed capacity stack with overflow protection
- Push, pop, peek, and clear operations
- Interactive command-line interface
- String representation for debugging

#### **week3.py**
Double Stack implementation:
- Two stacks sharing a single array
- Efficient memory usage with opposing growth directions
- Interactive interface for managing both stacks

#### **week4.py**
Circular Stack implementation:
- Fixed-size circular buffer behavior
- Configurable starting position
- Prevents overflow by wrapping around

#### **week5.py**
Queue implementation using Linked Lists:
- Dynamic size queue with linked list backend
- FIFO (First In, First Out) operations
- Interactive menu system for queue operations

### Advanced Implementations

#### **real-tree.py**
Binary Search Tree (BST) implementation:
- Tree node insertion with proper BST ordering
- Pretty-print functionality with indentation
- Demonstrates tree traversal and structure

#### **scro/main.py**
Schrödinger Stack - Quantum-inspired probabilistic stack:
- Elements exist in "superposition" until observed
- Weighted probability system for element ordering
- Collapse mechanism that determines final stack order
- Unique implementation demonstrating advanced concepts

#### **jalur/main.py**
Graph implementation with shortest path algorithms:
- Node-based graph structure with weighted edges
- Dijkstra's algorithm for shortest path finding
- Interactive graph building and pathfinding interface
- Add/remove nodes and connections dynamically

### Specialized Queue Implementations

#### **circular-queue.py**
Circular queue with array-based implementation

#### **double-queue.py** & **double-queue-with-arr.py**
Double-ended queue (deque) implementations with different approaches

#### **praktikum5.py**
Additional queue practice implementations

### Utility Files

#### **class_bot.py** & **robot.py**
Support files for specific assignments or demonstrations

## Usage Examples

### Running Basic Stack Operations

```python
# From week2.py
python3 week2.py
```
Interactive menu will allow you to:
1. Push new data
2. Pop data  
3. Print stack contents
4. Clear stack
5. Peek at top element

### Binary Search Tree Demo

```python
# From real-tree.py
python3 real-tree.py
```
Output shows tree structure:
```
> 10
  > 5
    > 7
  > 12
    > 13
```

### Schrödinger Stack Demonstration

```python
# From scro/main.py
cd scro && python3 main.py
```
Shows quantum superposition and collapse:
```
Pushing elements with weights:
Quantum state: [('α', 1.0), ('β', 3.0), ('γ', 2.0), ('δ', 1.5)]

--- First Collapse ---
Peek (collapses): β
Collapsed state: ['α', 'δ', 'γ', 'β']
```

### Graph and Shortest Path

```python
# From jalur/main.py
cd jalur && python3 main.py
```
Interactive interface for:
1. Building graphs with weighted edges
2. Finding shortest paths between nodes
3. Managing graph structure

### Basic Data Structure Examples

```python
# From contoh.py
python3 contoh.py
```
Demonstrates all basic data structures with simple examples.

## Running the Code

### Individual Files
Most files can be run directly:
```bash
python3 filename.py
```

### Interactive Programs
Several files provide interactive command-line interfaces:
- `week2.py` - Stack operations
- `week3.py` - Double stack management
- `week4.py` - Circular stack operations
- `week5.py` - Queue operations
- `jalur/main.py` - Graph building and pathfinding

### Directory-based Programs
Some implementations are in subdirectories:
```bash
cd scro && python3 main.py    # Schrödinger Stack
cd jalur && python3 main.py   # Graph algorithms
```

## Author

Fernando - Data Structures Course Implementation

*This repository is designed for educational purposes to help students understand data structure concepts through practical Python implementations.*
