import networkx as nx
from posts import Post
import random
import numpy as np
g = nx.read_graphml("graph.graphml")

def choice(l, scale, level):
    weights = [l[i]["weight"] / scale for i in l]
    try:
        a = np.unique(random.choices(list(l.keys()), weights, k=random.choices([i for i in range(0, len(weights) - 1)], weights=[1 if i != 0 else level * 2 for i in range(0, len(weights) - 1)], k=1)[0]))
    except:
        a = []
    return {i:l[i] for i in a}

def steps(neighbours, post, level):
    likes = choice(neighbours, 2, level)
    commenter = choice(neighbours, 4, level)
    post.inc_views(neighbours)
    post.inc_comments(commenter)
    post.inc_likes(likes)
    return likes, commenter, level + 1

def recommend(l, post, level):
    print(list(l.keys()))
    for i in l:
        neighbours = g[i]
        likes, commenter, level = steps(neighbours, post, level)
        if likes != []:
            recommend(likes, post, level)
        elif commenter != []:
            recommend(commenter, post, level)
    

posts = [Post(user) for user in random.choices(list(g.nodes()), k=10)]

for post in posts:
    print("new\n")
    neighbours = g[post.user]
    print(list(neighbours.keys()))
    likes, commenter, level = steps(neighbours, post, 1)
    if likes != []:
        recommend(likes, post, level)
    elif commenter != []:
        recommend(commenter, post, level)
    print(len(set(post.views)))
    
    

