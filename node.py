import json
import random


class Node:
    def __init__(self, user):
        self.user = user
        self.posts = set()
        self.edges = []
        self.neighbours = set()

    def add_edge(self, user):
        if user not in self.neighbours and user != self.user:
            self.neighbours.add(user)
            weight = 1 / len(self.neighbours)
            self.edges.append((user, weight))
            self.edges = list(map(lambda x: (x[0], weight), self.edges))

    def read_edge(self, user, weight):
        self.neighbours.add(user)
        self.edges.append((user, weight))

    def add_post(self, post):
        self.posts.add(post)


def create_graph():
    graph = [Node(i) for i in range(10)]
    for i in range(random.randint(30, 50)):
        user1 = random.randint(0, 9)
        user2 = random.randint(0, 9)
        graph[user1].add_edge(user2)
        graph[user2].add_edge(user1)

    d = []
    for i in graph:
        obj = {
            "user": i.user,
            "posts": list(i.posts),
            "edges": i.edges,
            "neighbours": list(i.neighbours),
        }
        d.append(obj)

    with open("data.json", "w") as f:
        json.dump(d, f, indent=4)
