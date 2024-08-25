import json
import random


class Node:
    def __init__(self, user):
        self.user = user
        self.posts = {}
        self.edges = []
        self.neighbours = set()
        self.denom = 0
        self.avg = 0
        self.count = 0

    def add_edge(self, user):
        if user not in self.neighbours and user != self.user:
            self.neighbours.add(user)
            weight = 1 / len(self.neighbours)
            self.edges.append((user, weight))
            self.denom += 1
            self.edges = list(map(lambda x: (x[0], weight), self.edges))

    def read_edge(self, user, weight):
        self.neighbours.add(user)
        self.edges.append((user, weight))

    def add_post(self, post):
        self.posts[post.id] = post


def create_graph(existing=False, graph=None, path="data.json", n=None):
    if not existing:
        graph = [Node(i) for i in range(n)]
        for i in range(random.randint(n * 3, n * 5)):
            user1 = random.randint(0, n - 1)
            user2 = random.randint(0, n - 1)
            graph[user1].add_edge(user2)
            graph[user2].add_edge(user1)

    d = []
    for i in graph:
        obj = {
            "user": i.user,
            "posts": {
                j.id: {
                    "time": j.time,
                    "likes": list(j.likes),
                    "comments": list(j.comments),
                    "views": list(j.views),
                    "quality": j.quality,
                }
                for j in i.posts
            },
            "edges": i.edges,
            "neighbours": list(i.neighbours),
            "denom": i.denom,
            "average" : i.avg,
            "count" : i.count
        }
        d.append(obj)

    with open(path, "w") as f:
        json.dump(d, f, indent=4)
