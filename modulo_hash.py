import hashlib

class ModuloHashing:
    def __init__(self, nodes):
        self.nodes = nodes

    def hash_function(self, key):
        return int(hashlib.md5(key.encode()).hexdigest(), 16)

    def get_node(self, key):
        hashed_key = self.hash_function(key)

        idx = hashed_key % len(self.nodes)

        return self.nodes[idx]