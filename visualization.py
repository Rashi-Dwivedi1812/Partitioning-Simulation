import matplotlib.pyplot as plt
import numpy as np

def plot_key_distribution(distribution):
    nodes = list(distribution.keys())
    counts = list(distribution.values())

    plt.figure(figsize=(8, 5))

    plt.bar(nodes, counts)

    plt.xlabel("Nodes")
    plt.ylabel("Number of Keys")
    plt.title("Key Distribution Across Nodes")

    plt.savefig("key_distribution.png")

    plt.show()


def plot_key_migration(modulo_moved, consistent_moved):
    methods = ["Modulo Hashing", "Consistent Hashing"]
    values = [modulo_moved, consistent_moved]

    plt.figure(figsize=(8, 5))

    plt.bar(methods, values)

    plt.ylabel("Keys Migrated")
    plt.title("Key Migration Comparison")

    plt.savefig("key_migration.png")

    plt.show()

def plot_execution_time(modulo_time, consistent_time):
    methods = ["Modulo", "Consistent"]

    times = [modulo_time, consistent_time]

    plt.figure(figsize=(8, 5))

    plt.bar(methods, times)

    plt.ylabel("Execution Time (sec)")

    plt.title("Execution Time Comparison")

    plt.savefig("execution_time.png")

    plt.show()

def plot_virtual_node_comparison(dist10, dist100, dist500):
    nodes = list(dist10.keys())

    values10 = list(dist10.values())
    values100 = list(dist100.values())
    values500 = list(dist500.values())

    x = range(len(nodes))

    plt.figure(figsize=(10, 6))

    plt.plot(x, values10, marker='o', label="10 Replicas")
    plt.plot(x, values100, marker='o', label="100 Replicas")
    plt.plot(x, values500, marker='o', label="500 Replicas")

    plt.xticks(x, nodes)

    plt.ylabel("Keys Assigned")

    plt.title("Virtual Node Comparison")

    plt.legend()

    plt.savefig("virtual_nodes.png")

    plt.show()


def plot_ring(ring):
    plt.figure(figsize=(8, 8))

    ax = plt.subplot(111, polar=True)

    positions = []

    labels = []

    max_hash = 2**128

    for key, node in ring.ring.items():
        angle = (key / max_hash) * 2 * np.pi

        positions.append(angle)

        labels.append(node)

    ax.scatter(positions, [1]*len(positions), alpha=0.75)

    plt.title("Consistent Hash Ring")

    plt.savefig("hash_ring.png")

    plt.show()