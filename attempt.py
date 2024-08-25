import math
import utils
from posts import Post
import random
import node

g = utils.read_graph("depracated/data2.json")
po = [Post(random.randint(0, 99)) for i in range(500)]


def new_avg(avg, count, value):
    return ((avg * (count - 1)) + value) / count


def feedback(centre, act, q):
    denom = g[centre].denom
    e = {i[0]: i[1] * denom for i in g[centre].edges}
    for i in act:
        e[i[0]] += 1
        g[i[0]].avg = new_avg(g[i[0]].avg, g[i[0]].count, q)
    denom = sum(e.values())
    g[centre].edges = [(i, e[i] / denom) for i in e]
    g[centre].denom = int(denom)


def propagate(centre, level, post):
    print(f"Centre: {centre}")
    print(f"Level: {level}")
    likes, commenter = choose(centre, post)
    if level == 3:
        changes(post, centre, likes, commenter)
    elif len(likes) != 0:
        changes(post, centre, likes, commenter)
        feedback(centre, likes, post.quality)
        for i in likes:
            propagate(i[0], level + 1, post)
    elif len(commenter) != 0:
        changes(post, centre, likes, commenter)
        feedback(centre, commenter, post.quality)
        for i in commenter:
            propagate(i[0], level + 1, post)
    else:
        changes(post, centre, likes, commenter)


def qual(neighbours, quality):
    return list(filter(lambda x: abs(g[x[0]].avg - quality) <= 0.05, neighbours))


def choose(centre, post):
    neighbours = sorted(g[centre].edges, key=lambda x: x[1], reverse=True)

    k = random.randint(0, (len(neighbours) - 1))
    likes1 = neighbours[:k]
    likes2 = qual(neighbours, post.quality)
    if len(likes2) == 0:
        likes2 = neighbours
    likes = list(set(likes1).intersection(set(likes2)))

    k1 = random.randint(0, (len(neighbours) - 1) // 2)
    commenter1 = neighbours[:k1]
    commenter2 = qual(neighbours, post.quality)
    if len(commenter2) == 0:
        commenter2 = neighbours
    commenter = list(set(commenter1).intersection(set(commenter2)))
    return likes, commenter


def changes(post, centre, likes, commenter):
    neighbours = list(map(lambda x: x[0], g[centre].edges))
    likes = list(map(lambda x: x[0], likes))
    commenter = list(map(lambda x: x[0], commenter))
    for i in likes:
        g[i].count += 1
    for i in commenter:
        g[i].count += 1
    post.inc_views(neighbours)
    post.inc_likes(likes)
    post.inc_comments(commenter)


for p in po:
    try:
        g[p.user].add_post(p)
    except:
        print(p.user)
    op = p.user
    propagate(op, 0, p)

node.create_graph(True, graph=g, path="data1.json")
