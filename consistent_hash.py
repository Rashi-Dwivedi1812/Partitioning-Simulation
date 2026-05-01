import hashlib
import bisect

class ConsistentHashRing:
    def __init__(self, replicas=100):
        self.replicas = replicas
        self.ring = {}
        self.sorted_keys = []

    def hash_function(self, key):
        return int(hashlib.md5(key.encode()).hexdigest(), 16)

    def add_node(self, node):
        for i in range(self.replicas):
            virtual_node = f"{node}:{i}"

            hashed = self.hash_function(virtual_node)

            self.ring[hashed] = node
            self.sorted_keys.append(hashed)

        self.sorted_keys.sort()

    def remove_node(self, node):
        for i in range(self.replicas):
            virtual_node = f"{node}:{i}"

            hashed = self.hash_function(virtual_node)

            if hashed in self.ring:
                del self.ring[hashed]
                self.sorted_keys.remove(hashed)

    def get_node(self, key):
        if not self.ring:
            return None

        hashed_key = self.hash_function(key)

        idx = bisect.bisect(self.sorted_keys, hashed_key)

        if idx == len(self.sorted_keys):
            idx = 0

        return self.ring[self.sorted_keys[idx]]