# Consistent Hashing Ring: Partitioning Simulation

A Python-based simulation and benchmarking project that demonstrates how **Consistent Hashing** improves scalability, fault tolerance, and load balancing in distributed database systems compared to traditional **Modulo Hashing**.

This project was developed as part of the **Introduction to Large-Scale Database Systems (21B12CS314)** course.

---

## 📌 Project Objective

The goal of this project is to:

- Implement a **Consistent Hashing Ring**
- Simulate **node addition** and **node removal**
- Measure **key migration cost**
- Compare Consistent Hashing with **Modulo Hashing**
- Analyze **load balancing**
- Study the effect of **virtual nodes**
- Generate visualizations for distributed partitioning behavior

---

## 🚀 Features

✅ Consistent Hashing Ring Implementation  
✅ Virtual Nodes (Replicas)  
✅ Modulo Hashing Comparison  
✅ Node Addition Simulation  
✅ Node Removal Simulation  
✅ Key Migration Analysis  
✅ Execution Time Benchmarking  
✅ Load Imbalance Calculation  
✅ Virtual Node Comparison (10 / 100 / 500 replicas)  
✅ Histogram Visualization  
✅ Circular Hash Ring Visualization  

---

## 🧠 Concepts Used

- Distributed Systems
- Data Partitioning
- Consistent Hashing
- Virtual Nodes
- Load Balancing
- Fault Tolerance
- Scalability
- Hash Rings

---

## ⚙️ Technologies Used

| Technology | Purpose |
|---|---|
| Python 3 | Core implementation |
| hashlib | Hash generation |
| bisect | Efficient ring lookup |
| matplotlib | Graph visualization |
| numpy | Circular ring plotting |

---

## 📂 Project Structure

```text
project/
│
├── main.py
├── consistent_hash.py
├── modulo_hash.py
├── visualization.py
│── results/
│        ├──  key_distribution.png
│        ├── key_migration.png
│        ├── execution_time.png
│        ├──virtual_nodes.png
│        ├──hash_ring.png
│
└── README.md
```

---

## 🔧 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/consistent-hashing-project.git
```

Move into the project directory:

```bash
cd consistent-hashing-project
```

Install dependencies:

```bash
python3 -m pip install matplotlib numpy
```

---

## ▶️ Running the Project

Run the simulation using:

```bash
python3 main.py
```

---

## 📊 Experiments Performed

### 1. Initial Key Distribution

Distributes 10,000 keys across multiple nodes using Consistent Hashing.

---

### 2. Node Addition Simulation

Adds a new node and measures:
- migrated keys
- redistribution behavior
- scalability impact

---

### 3. Node Removal Simulation

Removes an existing node to simulate:
- server failure
- cluster scaling down
- fault tolerance behavior

---

### 4. Modulo Hashing Comparison

Compares:
- key remapping percentage
- migration overhead
- scalability

---

### 5. Virtual Node Comparison

Tests:
- 10 replicas
- 100 replicas
- 500 replicas

to analyze load balancing improvements.

---

### 6. Execution Time Benchmarking

Measures lookup time for:
- Consistent Hashing
- Modulo Hashing

---

## 📈 Sample Results

| Metric | Modulo Hashing | Consistent Hashing |
|---|---|---|
| Lookup Time | 0.004529 sec | 0.006587 sec |
| Migrated Keys | 7466 | 2311 |
| Migration Reduction | — | 69.05% |
| Load Imbalance | Higher | 16.60% |

---

## 📉 Key Findings

- Consistent Hashing reduced key migration by approximately **69%**
- Virtual nodes significantly improved load balancing
- Modulo Hashing was slightly faster
- Consistent Hashing provided much better scalability and fault tolerance

---

## 📷 Visualizations

The project generates:
- Key Distribution Histogram
- Key Migration Comparison Graph
- Execution Time Comparison Graph
- Virtual Node Comparison Graph
- Circular Hash Ring Visualization

---

## 🌍 Real-World Applications

Consistent Hashing is widely used in:
- Apache Cassandra
- Amazon DynamoDB
- Redis Cluster
- CDN Systems
- Distributed Caching Systems

---

## 📌 Conclusion

This project demonstrates how Consistent Hashing minimizes redistribution overhead while improving scalability and load balancing in distributed systems. Experimental results validate why modern distributed databases prefer Consistent Hashing over traditional Modulo Hashing.
