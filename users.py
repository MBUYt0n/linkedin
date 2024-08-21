import networkx as nx
from posts import Post
import random
import math

g = nx.read_graphml("graph.graphml")

for i in range(100):
    posts = [Post(user) for user in random.choices(list(g.nodes()), k=10)]

    for post in posts:
        neighbors = list(g.neighbors(post.user))
        post.inc_views(neighbors)
        post.inc_likes(random.choices(neighbors, k=random.randint(0, len(neighbors))))
        post.inc_comments(random.choices(neighbors, k=random.randint(0, len(neighbors))))
        for i in post.likes:
            a = g[post.user][i]["weight"]
            g[post.user][i]["weight"] += (math.exp(-a) * a)
        for i in post.comments:
            a = g[post.user][i]["weight"]
            g[post.user][i]["weight"] += (math.exp(-a) * a)

nx.write_graphml(g, "graph1.graphml")