import math
import utils
from posts import Post
import random
import node

g = utils.read_graph()
p = Post(3)
g[p.user].add_post(p)
op = p.user


def feedback(centre, act):
    denom = g[centre].denom
    e = {i[0]: i[1] * denom for i in g[centre].edges}
    for i in act:
        e[i[0]] += 1
    denom = sum(e.values())
    g[centre].edges = [(i, e[i] / denom) for i in e]
    g[centre].denom = int(denom)


def propagate(centre, level):
    print(centre, level)
    likes, commenter = choose(centre)
    if level == 3:
        changes(p, centre, likes, commenter)
    elif len(likes) != 0:
        changes(p, centre, likes, commenter)
        feedback(centre, likes)
        for i in likes:
            propagate(i[0], level + 1)
    elif len(commenter) != 0:
        changes(p, centre, likes, commenter)
        feedback(centre, commenter)
        for i in commenter:
            propagate(i[0], level + 1)
    else:
        changes(p, centre, likes, commenter)


def choose(centre):
    neighbours = sorted(g[centre].edges, key=lambda x: x[1], reverse=True)
    k = random.randint(0, (len(neighbours) - 1))
    likes = neighbours[:k]
    k1 = random.randint(0, (len(neighbours) - 1) // 2)
    commenter = neighbours[:k1]
    return likes, commenter


def changes(post, centre, likes, commenter):
    neighbours = map(lambda x: x[0], g[centre].edges)
    likes = map(lambda x: x[0], likes)
    commenter = map(lambda x: x[0], commenter)
    post.inc_views(neighbours)
    post.inc_likes(likes)
    post.inc_comments(commenter)


propagate(op, 0)
node.create_graph("data1.json")