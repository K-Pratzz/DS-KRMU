# 🧠 Time Complexity Cheat Sheet

## 🔥 Universal Logic

Everything depends on how many elements are processed.

| Pattern | Time Complexity |
|--------|----------------|
| Touch 1 element | O(1) |
| Touch all elements once | O(n) |
| Nested loops | O(n²) |
| Divide problem (half each step) | O(log n) |
| Divide + process all | O(n log n) |

---

## 📊 Sorting Algorithms

| Algorithm | Time Complexity |
|----------|----------------|
| Bubble Sort | O(n²) |
| Selection Sort | O(n²) |
| Insertion Sort | O(n²) |
| Merge Sort | O(n log n) |
| Quick Sort (avg) | O(n log n) |
| Counting Sort | O(n + k) |
| Radix Sort | O(nk) |

---

## 🌳 Binary Search Tree (BST)

| Operation | Time Complexity |
|----------|----------------|
| Search | O(log n) (avg) |
| Insert | O(log n) (avg) |
| Delete | O(log n) (avg) |
| Worst Case | O(n) |

---

## 🔗 Linked List

| Operation | Time Complexity |
|----------|----------------|
| Insert (Beginning) | O(1) |
| Insert (End) | O(n) |
| Delete | O(n) |
| Search | O(n) |

---

## 📦 Array

| Operation | Time Complexity |
|----------|----------------|
| Access | O(1) |
| Insert | O(n) |
| Delete | O(n) |
| Search | O(n) |

---

## 📚 Stack

| Operation | Time Complexity |
|----------|----------------|
| Push | O(1) |
| Pop | O(1) |
| Peek | O(1) |

---

## 🚶 Queue

| Operation | Time Complexity |
|----------|----------------|
| Enqueue | O(1) |
| Dequeue | O(1) |
| Peek | O(1) |

---

## 🧠 Hashing

| Operation | Time Complexity |
|----------|----------------|
| Insert | O(1) (avg) |
| Search | O(1) (avg) |
| Delete | O(1) (avg) |
| Worst Case | O(n) |

---

## 🌐 Graph

| Operation | Time Complexity |
|----------|----------------|
| BFS / DFS | O(V + E) |

---

## 💡 Universal Reasons (Use in Exams)

### 🔹 O(1)
Operation is performed directly without any traversal or iteration over elements. The result is obtained instantly regardless of input size. Hence, the time remains constant.

---

### 🔹 O(n)
All elements may need to be traversed once to complete the operation. The number of steps increases linearly with input size. Therefore, the time complexity is O(n).

---

### 🔹 O(n²)
The algorithm uses nested loops where each element is compared with others. This results in n × n operations in the worst case. Hence, the time complexity becomes quadratic.

---

### 🔹 O(log n)
The problem size is reduced by half at each step. This significantly decreases the number of operations needed. Therefore, the time complexity is logarithmic.

---

### 🔹 O(n log n)
The problem is divided into smaller parts (log n levels), and at each level all elements are processed. This combination results in O(n log n) time complexity.
