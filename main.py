from consistent_hash import ConsistentHashRing
from modulo_hash import ModuloHashing
from visualization import (
    plot_key_distribution,
    plot_key_migration,
    plot_execution_time,
    plot_virtual_node_comparison,
    plot_ring
)

import time

# ----------------------------------
# Generate Sample Keys
# ----------------------------------

NUM_KEYS = 10000

keys = [f"user_{i}" for i in range(NUM_KEYS)]


# ----------------------------------
# Consistent Hashing
# ----------------------------------

print("\n===== CONSISTENT HASHING =====\n")

ring = ConsistentHashRing(replicas=100)

initial_nodes = ["NodeA", "NodeB", "NodeC"]

for node in initial_nodes:
    ring.add_node(node)


# Store initial mapping
start_time = time.perf_counter()

before_mapping = {}

distribution_before = {}

for key in keys:
    node = ring.get_node(key)

    before_mapping[key] = node

    distribution_before[node] = (
        distribution_before.get(node, 0) + 1
    )

end_time = time.perf_counter()

consistent_time = end_time - start_time

print(f"\nConsistent Hashing Lookup Time: {consistent_time:.6f} sec")


print("Initial Key Distribution:")
print(distribution_before)


# Add new node
ring.add_node("NodeD")


# Store new mapping
after_mapping = {}

distribution_after = {}

for key in keys:
    node = ring.get_node(key)

    after_mapping[key] = node

    distribution_after[node] = (
        distribution_after.get(node, 0) + 1
    )


# Count migrated keys
consistent_moved = 0

for key in keys:
    if before_mapping[key] != after_mapping[key]:
        consistent_moved += 1


print("\nAfter Adding NodeD:")
print(distribution_after)

print(f"\nKeys moved in Consistent Hashing: {consistent_moved}")


# ----------------------------------
# Modulo Hashing
# ----------------------------------

print("\n===== MODULO HASHING =====\n")

modulo_before = ModuloHashing(
    ["NodeA", "NodeB", "NodeC"]
)

start_time = time.perf_counter()

before_mod_mapping = {}

for key in keys:
    before_mod_mapping[key] = modulo_before.get_node(key)

end_time = time.perf_counter()

modulo_time = end_time - start_time

print(f"\nModulo Hashing Lookup Time: {modulo_time:.6f} sec")


modulo_after = ModuloHashing(
    ["NodeA", "NodeB", "NodeC", "NodeD"]
)

after_mod_mapping = {}

for key in keys:
    after_mod_mapping[key] = modulo_after.get_node(key)


# Count migrated keys
modulo_moved = 0

for key in keys:
    if before_mod_mapping[key] != after_mod_mapping[key]:
        modulo_moved += 1


print(f"Keys moved in Modulo Hashing: {modulo_moved}")

def test_virtual_nodes(replicas):
    ring = ConsistentHashRing(replicas=replicas)

    nodes = ["NodeA", "NodeB", "NodeC"]

    for node in nodes:
        ring.add_node(node)

    distribution = {}

    for key in keys:
        node = ring.get_node(key)

        distribution[node] = (
            distribution.get(node, 0) + 1
        )

    return distribution

def calculate_imbalance(distribution):
    loads = list(distribution.values())

    max_load = max(loads)
    min_load = min(loads)

    avg_load = sum(loads) / len(loads)

    imbalance = (
        (max_load - min_load)
        / avg_load
    ) * 100

    return imbalance

dist_10 = test_virtual_nodes(10)

dist_100 = test_virtual_nodes(100)

dist_500 = test_virtual_nodes(500)

print("\nDistribution with 10 replicas:")
print(dist_10)

print("\nDistribution with 100 replicas:")
print(dist_100)

print("\nDistribution with 500 replicas:")
print(dist_500)

# ----------------------------------
# Visualizations
# ----------------------------------

plot_key_distribution(distribution_after)

plot_key_migration(
    modulo_moved,
    consistent_moved
)

plot_execution_time(
    modulo_time,
    consistent_time
)

plot_virtual_node_comparison(
    dist_10,
    dist_100,
    dist_500
)

plot_ring(ring)

# ----------------------------------
# Final Comparison
# ----------------------------------

print("\n===== FINAL COMPARISON =====\n")

print(f"Modulo Hashing Moved Keys     : {modulo_moved}")
print(f"Consistent Hashing Moved Keys : {consistent_moved}")

reduction = (
    (modulo_moved - consistent_moved)
    / modulo_moved
) * 100

print(f"\nMigration Reduction: {reduction:.2f}%")

print("\n===== NODE REMOVAL SIMULATION =====\n")

before_removal = {}

for key in keys:
    before_removal[key] = ring.get_node(key)

# Remove node
ring.remove_node("NodeB")

after_removal = {}

for key in keys:
    after_removal[key] = ring.get_node(key)

removed_keys = 0

for key in keys:
    if before_removal[key] != after_removal[key]:
        removed_keys += 1

print(f"Keys moved after removing NodeB: {removed_keys}")

imbalance = calculate_imbalance(distribution_after)

print(f"\nLoad Imbalance: {imbalance:.2f}%")